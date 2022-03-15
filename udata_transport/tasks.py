import requests
from flask import current_app
from udata.tasks import job
from udata.commands import success, error
from udata.models import Dataset


def process_dataset(dataset):
    target_dataset = Dataset.objects(id=dataset['datagouv_id']).first()
    if not target_dataset:
        error(f"Dataset {dataset['id']} not found")
        return
    target_dataset.extras['transport_url'] = dataset['page_url']
    target_dataset.save()


@job("map-transport-datasets")
def map_transport_datasets(self):
    datasets = Dataset.objects(extras__transport_url__exists=True).no_cache().timeout(False)
    for dataset in datasets:
        dataset.extras.pop('transport_url', None)

    source = current_app.config.get('TRANSPORT_DATASETS_URL', None)
    if not source:
        error('TRANSPORT_DATASETS_URL variable must be set.')
        return

    response = requests.get(source)
    if response.status_code != 200:
        error('Remote platform unreachable.')
        return
    results_list = response.json()
    for dataset in results_list:
        process_dataset(dataset)
    success(f'Done. {len(results_list)} datasets mapped to transport')
