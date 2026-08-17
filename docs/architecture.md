# HIDMS System Architecture

## High-level view

```
┌────────────────┐     ┌──────────────────────┐     ┌────────────────────────┐
│  Data sources  │ ──► │  Ingestion & storage │ ──► │  AI / ML analysis      │
│  - mobile/web  │     │  (structured records)│     │  - risk scoring        │
│  - IoT devices │     │  - role-based access │     │  - trend detection     │
│  - questionnaires│    └──────────────────────┘     │  - RAG health assistant│
└────────────────┘                                    └───────────┬────────────┘
                                                                  ▼
                                        ┌─────────────────────────────────────┐
                                        │  Decision support & alerting        │
                                        │  - dashboards for professionals      │
                                        │  - alerts to guardians / institutions│
                                        └─────────────────────────────────────┘
```

## AI / ML pipeline

1. **Data ingestion** — structured health records from mobile/web forms and IoT sensors.
2. **Preprocessing** — cleaning, de-identification, imputation (`src/hidms/data.py`).
3. **Feature engineering** — vital signs, trends, comorbidity flags, derived indices
   such as BMI (`src/hidms/features.py`).
4. **Risk scoring** — supervised models trained on labelled outcomes; outputs a risk
   score per individual (`src/hidms/models.py`).
5. **Evaluation** — accuracy, precision/recall, ROC-AUC, plus clinical decision-support
   metrics (`src/hidms/evaluation.py`).
6. **RAG health assistant** — retrieval-augmented generation over curated health
   knowledge to guide symptom assessment and care navigation.
7. **Alerting** — threshold-based and trend-based alerts to guardians, providers,
   and institutions.

## Design principles

- **Privacy-first** — de-identified data, role-based access, no raw patient data in the repo.
- **Reproducible** — fixed seeds, pinned environments (`environment.yml`), numbered notebooks.
- **Tested** — unit tests for core modules (`tests/`), CI-ready.
- **AI as decision support** — all model outputs are intended for validation by medical professionals.
