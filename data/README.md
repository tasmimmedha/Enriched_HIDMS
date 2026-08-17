# Data

Datasets live here, organised by processing stage (cookiecutter-data-science convention):

| Folder      | Purpose                                                        |
| ----------- | -------------------------------------------------------------- |
| `raw/`      | Original, unmodified data (never edit in place)                 |
| `interim/`  | Partially processed / transformed data                          |
| `processed/`| Final, model-ready datasets                                     |
| `external/` | Public / third-party reference data                             |

## ⚠️ Privacy first

HIDMS works with health data. **Never commit raw patient data to this repository.**
Use only consented, de-identified, or synthetic datasets. If you must version data,
use [DVC](https://dvc.org/) or Git LFS instead of committing it directly.
