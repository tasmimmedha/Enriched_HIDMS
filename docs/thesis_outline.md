# Thesis Outline — HIDMS

**Health Intelligence & Diagnostic Monitoring System**
*An AI-powered preventive healthcare platform*

> This outline follows the standard structure expected by graduate programs
> (MIT-style: problem → method → experiments → results → impact).

---

## Chapter 1 — Introduction
- 1.1 Background & motivation (preventive vs. reactive healthcare)
- 1.2 Problem statement
- 1.3 Research questions
  - RQ1: Can ML risk scores reliably flag early warning signs of chronic disease?
  - RQ2: Which feature sets / models perform best on community health data?
  - RQ3: Does a RAG-based assistant improve health literacy and care navigation?
- 1.4 Contributions
- 1.5 Thesis organisation

## Chapter 2 — Literature Review
- 2.1 Preventive & community health monitoring systems
- 2.2 Risk prediction in chronic disease (cardiovascular, diabetes, obesity)
- 2.3 Machine learning for health risk scoring
- 2.4 Retrieval-Augmented Generation (RAG) in health assistants
- 2.5 Gaps addressed by HIDMS

## Chapter 3 — Methodology
- 3.1 System architecture (data collection → analysis → alerting)
- 3.2 Data collection & ethics (consent, de-identification)
- 3.3 Data preprocessing & feature engineering
- 3.4 Risk-scoring models (baselines → tuned ensemble)
- 3.5 Evaluation protocol (metrics, cross-validation, clinical validation)

## Chapter 4 — Implementation
- 4.1 Data pipeline (`src/hidms/data.py`)
- 4.2 Feature engineering (`src/hidms/features.py`)
- 4.3 Model training & selection (`src/hidms/models.py`)
- 4.4 Evaluation (`src/hidms/evaluation.py`)
- 4.5 RAG health assistant & alerting service

## Chapter 5 — Experiments & Results
- 5.1 Datasets & experimental setup
- 5.2 Baseline results
- 5.3 Model comparison (tables + figures)
- 5.4 Ablation / feature importance
- 5.5 Limitations & failure cases

## Chapter 6 — Discussion
- 6.1 Interpretation of results
- 6.2 Practical implications for schools / communities
- 6.3 Ethical considerations (privacy, bias, clinical validation)

## Chapter 7 — Conclusion & Future Work
- 7.1 Summary of contributions
- 7.2 Future directions (IoT scale-up, federated learning, deployment)

---

## Appendices
- A. Dataset description & consent forms
- B. Additional figures & tables
- C. Reproducibility instructions (environment, commands)
