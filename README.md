# 🩺 Enriched_HIDMS — Health Intelligence & Diagnostic Monitoring System

**AI-Powered Preventive Healthcare Platform · Thesis Project · Data Science (AI/ML)**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Tests](https://img.shields.io/badge/tests-pytest-green.svg)](tests/)

> A preventive, AI-driven healthcare ecosystem that continuously collects and analyzes
> individual health data to detect early warning signs of disease, support clinical and
> mentoring decisions, and enable timely interventions in schools, workplaces, and
> communities.

---

## 📌 Overview

The Health Intelligence & Diagnostic Monitoring System (**HIDMS**) targets individuals of
all age groups, with a strong focus on preventing and managing conditions such as
cardiovascular disease, diabetes, obesity, and other chronic or acute illnesses.

**Problem statement.** Many institutions and communities still lack structured, continuous
health monitoring. This leads to:

- **Lack of routine health tracking** — few schools or communities maintain ongoing records
- **Delayed diagnosis** — early symptoms are ignored until conditions become severe
- **No predictive support** — traditional systems rarely use AI-based risk prediction
- **Fragmented and insecure data** — health information is often unstructured and poorly protected
- **Limited healthcare access** — rural and low-income populations struggle to obtain timely care
- **High treatment costs** — late detection leads to expensive treatments that could have been prevented

**Solution.** HIDMS introduces a preventive AI-assisted healthcare ecosystem that collects
structured health data, uses ML to identify health risks early, supports professionals and
guardians in decisions, enables remote monitoring, and promotes community-level awareness.

---

## ✨ Key Features

1. **AI-Based Health Risk Analysis** — ML applied to health trends and reported symptoms;
   generates risk scores and decision-support insights (to be validated by medical professionals).
2. **Community Health Data Collection** — weekly/bi-weekly entry via mobile & web, IoT
   integration (smart thermometers, digital scales), structured cloud-based health records.
3. **Digital Health Profile System** — secure personal profiles; medical history, allergies,
   vaccinations, reports; role-based access control.
4. **Real-Time Alerts & Monitoring** — risk-level alerts to guardians/providers/institutions,
   automated follow-up reminders, early response to abnormal indicators.
5. **RAG-Based AI Health Assistant** — a Retrieval-Augmented Generation chatbot for symptom
   guidance, health education, care navigation, and communication among students, parents,
   teachers, and healthcare providers.

---

## 🗂 Repository Structure

```
Enriched_HIDMS/
├── data/                    # Datasets (raw → interim → processed)
├── docs/                    # Thesis write-up, architecture, application guide
├── models/                  # Trained models & checkpoints
├── notebooks/               # EDA & experiments (numbered, reproducible)
├── reports/                 # Generated analyses & thesis figures
├── src/hidms/               # Main Python package (pip install -e .)
│   ├── data.py              #   Data loading & preprocessing
│   ├── features.py          #   Feature engineering
│   ├── models.py            #   Model definitions & training
│   ├── evaluation.py        #   Metrics & validation
│   ├── config.py            #   Paths & configuration
│   └── utils.py             #   Shared helpers (seeds, logging)
├── tests/                   # Unit tests (pytest)
├── .gitignore
├── LICENSE                  # MIT License
├── Makefile                 # Common tasks (install, test, lint)
├── README.md
├── environment.yml          # Conda environment
├── pyproject.toml           # Packaging & tool configuration
└── requirements.txt         # Python dependencies
```

### Branch strategy

| Branch     | Purpose                                                          |
| ---------- | ---------------------------------------------------------------- |
| `main`     | Stable, thesis-ready code and documentation                       |
| `Develop`  | Active development (work-in-progress code)                        |
| `research` | Zotero research library (translators, styles, references, PDFs)   |

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/tasmimmedha/Enriched_HIDMS.git
cd Enriched_HIDMS

# 2. (Recommended) Create the conda environment
conda env create -f environment.yml
conda activate hidms

# 3. Or install with pip
pip install -r requirements.txt
pip install -e ".[dev]"

# 4. Run the test suite
make test        # or: pytest

# 5. Start exploring
jupyter lab notebooks/
```

---

## 🚀 Live Demo (Diabetes-Risk Prediction)

A small, interactive demo ships with the repo: it generates **simulated,
de-identified** patient records, trains a Random Forest on them, and predicts
diabetes risk for any set of measurements.

```bash
# 1. Train the demo model (creates models/demo_diabetes_risk.joblib)
make train-demo            # or: python scripts/train_demo.py

# 2a. CLI demo — try three example patients
make demo                  # or: python -m hidms.demo --sample

# 2b. Interactive CLI prompt (enter your own measurements)
python -m hidms.demo

# 3. Web app (needs streamlit: pip install streamlit)
make web                   # or: streamlit run app.py
```

Demo artifacts: `data/raw/demo_health_records.csv` (simulated records),
`reports/demo_metrics.json` (accuracy / F1 / ROC-AUC),
`reports/figures/demo_feature_importance.png`.

> ⚠️ **Demo only.** The data is simulated and the model is for
> demonstration/education — never for real clinical decisions.

Want it live on the web for free? Follow the
**[zero-to-deploy guide](docs/deployment_guide.md)** — it publishes the app
on Streamlit Community Cloud in ~15 minutes.

---

## 🧪 Research & Thesis

- **Thesis outline** → [`docs/thesis_outline.md`](docs/thesis_outline.md)
- **System architecture** → [`docs/architecture.md`](docs/architecture.md)
- **MIT application guide** → [`docs/mit_application_guide.md`](docs/mit_application_guide.md)
- **Research library** (Zotero: papers, references, PDFs) → `research` branch

---

## 📈 Project Pipeline (Roadmap)

- [ ] Data collection & anonymization (consented, de-identified datasets)
- [ ] Exploratory data analysis (`notebooks/01_exploratory_data_analysis.ipynb`)
- [ ] Feature engineering & selection (`src/hidms/features.py`)
- [ ] Risk-prediction models (baseline → tuned) (`src/hidms/models.py`)
- [ ] Evaluation & clinical metrics (`src/hidms/evaluation.py`)
- [ ] RAG-based health assistant (retrieval + generation)
- [ ] Real-time alerting & monitoring service
- [ ] Thesis write-up (`docs/`)

---

## 🛡 Data & Ethics

Health data is sensitive. This project follows a **privacy-first** approach:

- Only de-identified / consented datasets are used
- Never commit raw patient data to the repository
- Role-based access control for any deployed system
- AI outputs are decision *support* only — always validated by medical professionals

---

## 👤 Author

**Tasmim Rahman Medha** — Data Science (AI/ML)

## 📄 License

Distributed under the [MIT License](LICENSE).
