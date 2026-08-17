# Notebooks

Exploratory and experimental notebooks, numbered in execution order:

| Notebook | Purpose |
| -------- | ------- |
| `01_exploratory_data_analysis.ipynb` | EDA: distributions, missing values, correlations |
| `02_feature_engineering.ipynb`       | Feature experiments (then moved to `src/hidms/`) |
| `03_model_benchmarks.ipynb`          | Baseline + tuned model comparisons |

**Convention:** when an experiment stabilises, promote the code into the
`src/hidms/` package instead of leaving it in the notebook. Keep notebooks
readable top-to-bottom (clean outputs before committing).
