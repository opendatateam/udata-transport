# udata-transport

This plugin acts as a bridge between uData and transport.data.gouv.fr system.

## Compatibility

**udata-transport** requires Python 3.7+ and [uData][].

## Installation

Install [uData][].

Remain in the same virtual environment (for Python).

Install **udata-transport**:

```shell
pip install udata-transport
```

Modify your local configuration file of **udata** (typically, `udata.cfg`) as following:

```python
PLUGINS = ['transport']
TRANSPORT_DATASETS_URL = 'https://path/to/transport.data.gouv.fr/datasets/api'
```

- `TRANSPORT_DATASETS_URL`: The URL of the API endpoint listing datasets on transport.data.gouv.fr. _Default_: `None`

## Usage

### Mapping dataset

The mapping is done by a job, runnable by hand or scheduled.
The job is idempotent, previous URLs are cleaned before mapping new ones.

```shell
udata job run map-transport-datasets
```

This plugin will store the mapping URL in the dataset extras `transport:url` key:

```json
{
"id": "dataset-id",
"extras": {
    "transport:url": "https://path/to/datasets"
  }
}
```

[uData]: https://github.com/opendatateam/udata
