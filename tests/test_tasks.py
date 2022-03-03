import pytest
import requests_mock

from udata.core.dataset.factories import DatasetFactory

from udata_transport.tasks import map_transport_datasets

MOCK_URL = 'http://reco.net'


@pytest.fixture
def mock_invalid_response():
    return [
        {
            "datagouv_id": "61fd29da29ea95c7bc0e1211",
            "id": "61fd29da29ea95c7bc0e1211",
            "page_url": "https://transport.data.gouv.fr/datasets/horaires-theoriques-et-temps-reel-des-navettes-hivernales-de-lalpe-dhuez-gtfs-gtfs-rt",
            "slug": "horaires-theoriques-et-temps-reel-des-navettes-hivernales-de-lalpe-dhuez-gtfs-gtfs-rt",
            "title": "Navettes hivernales de l'Alpe d'Huez",
        },
        {
            "datagouv_id": "5f23d4b3d39755210a04a99c",
            "id": "5f23d4b3d39755210a04a99c",
            "page_url": "https://transport.data.gouv.fr/datasets/horaires-theoriques-et-temps-reel-du-reseau-lr-11-lalouvesc-tournon-st-felicien-gtfs-gtfs-rt",
            "slug": "horaires-theoriques-et-temps-reel-du-reseau-lr-11-lalouvesc-tournon-st-felicien-gtfs-gtfs-rt",
            "title": "Réseau interurbain  Lalouvesc / Tournon / St Felicien",
        },
    ]


@pytest.mark.usefixtures('clean_db')
class Tests:

    @pytest.mark.options(TRANSPORT_DATASETS_URL='https://local.test/api/datasets')
    def test_map_transport_datasets(self, mock_invalid_response):
        ds1 = DatasetFactory(id='61fd29da29ea95c7bc0e1211')
        ds2 = DatasetFactory(id='5f23d4b3d39755210a04a99c')

        with requests_mock.Mocker() as m:
            m.get('https://local.test/api/datasets', text='resp')
            map_transport_datasets()

        ds1.reload()
        ds2.reload()

        assert ds1.extras == {'untouched': 'yep'}
        assert ds2.extras == {'wait': 'for it'}
