# tool-bicon

Runs network-constrained biclustering with BiCoN and exports sample clusters and gene modules.

## Runtime inputs

Supply input files according to the schemas in `app.yml`.

## Inputs and outputs

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `net` | TSV | Network data file (TSV format) containing gene interactions |
| `expr` | CSV | Gene expression data file (CSV format) with genes as rows and samples as columns |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `cluster_map` | STRING | Cluster map visualization showing patient stratification |
| `network` | STRING | Network visualization showing identified subnetworks |
| `result` | CSV | Results file containing biclustering analysis results |

## Configuration

| Name | Default | Description |
| --- | --- | --- |
| `l_g_min` | `10` | Minimum size of subnetwork for biclustering |
| `l_g_max` | `15` | Maximum size of subnetwork for biclustering |
| `max_iter` | `15` | Maximum number of iterations for the search algorithm |

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
# Set APP_ID and platform URLs before connecting.
python main.py
```

The Docker base image provides the FL-Net API. `requirements.txt` lists additional
runtime dependencies; `requirements-dev.txt` includes the API for local development.
Runtime datasets and trained models must be supplied separately; see `data/README.md`.

Build with `docker build -t tool-bicon .`.
