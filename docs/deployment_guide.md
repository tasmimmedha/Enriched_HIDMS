# 🚀 Deploying the HIDMS Demo — Step-by-Step (Zero to Live)

This guide takes the HIDMS diabetes-risk demo from an idea to a **public,
shareable web app** that anyone can open in a browser. Everything needed to
deploy is already in this repository.

**Cost:** $0 (free tiers of GitHub + Streamlit Community Cloud).
**Time:** ~15 minutes.
**What you need:** a GitHub account (you already have one) and an email address.

---

## Part 0 — What "deploy" means here

| Term | Meaning |
| ---- | ------- |
| GitHub repo | Your code's home on the internet (`tasmimmedha/Enriched_HIDMS`) |
| Deployment | Putting your app on a server so others can open it with a URL |
| Streamlit Community Cloud | Free hosting for Streamlit apps, connected to your GitHub repo |
| The app | `app.py` — the interactive diabetes-risk demo |

When someone visits your deployed URL, they see the demo web page and can
move the sliders themselves. The Streamlit cloud service installs your
dependencies (from `requirements.txt`) and runs `app.py`.

---

## Part 1 — Push the demo code to GitHub

Your demo code must be in the GitHub repo before it can be deployed.

```bash
# 1. See what changed
git status

# 2. Add the demo files (NOT the Zotero research files)
git add app.py requirements.txt Makefile .streamlit/ scripts/ src/hidms/demo.py \
        src/hidms/synthetic.py tests/test_synthetic.py \
        models/demo_diabetes_risk.joblib \
        data/raw/demo_health_records.csv \
        reports/demo_metrics.json reports/figures/demo_feature_importance.png \
        docs/deployment_guide.md

# 3. Commit
git commit -m "Add interactive diabetes-risk demo (CLI + Streamlit web app)"

# 4. Push
git push origin main
```

> The trained model (`models/demo_diabetes_risk.joblib`) is committed on
> purpose, so the deployed app works instantly without re-training. The data
> in `data/raw/demo_health_records.csv` is **simulated** — safe to share.

---

## Part 2 — Deploy on Streamlit Community Cloud (recommended)

### 2.1 Create a free Streamlit account
1. Open https://share.streamlit.io
2. Click **Sign up** → choose **Continue with GitHub**
3. Authorize Streamlit to access your GitHub account (it needs this to read
   your repository — it cannot modify it).

### 2.2 Deploy your app
1. After signing in, click **New app** (top-right).
2. In the **Repository** box, type: `tasmimmedha/Enriched_HIDMS`
   (pick it from the dropdown if shown).
3. **Branch:** `main`
4. **Main file path:** `app.py`
5. Click **Deploy**.

Streamlit will now:
- read `requirements.txt` and install the packages (2–4 minutes),
- run `app.py`,
- give you a public URL like `https://enriched-hidms.streamlit.app`.

### 2.3 Share it
- The URL is public — share it in your CV, thesis, LinkedIn, and MIT
  application.
- Streamlit auto-redeploys whenever you push new code to `main`.

### 2.4 (Optional) Nice URL & custom domain
In the Streamlit dashboard → **Settings** → **App URL** you can pick a
custom subdomain (e.g. `tasmim-hidms.streamlit.app`).

---

## Part 3 — Alternative: Hugging Face Spaces

Hugging Face Spaces is another free option, very popular in the AI/ML
community (a plus for a Data Science application).

1. Create a free account at https://huggingface.co/join
2. Click your profile → **New Space**:
   - **Space name:** `hidms-demo`
   - **License:** MIT
   - **SDK:** Streamlit
3. Choose **"Import a Space from a Git repository"** →
   paste `https://github.com/tasmimmedha/Enriched_HIDMS`
4. Set **Branch:** `main`, then **Create Space**.
5. The Space auto-deploys. Your app is now live at
   `https://huggingface.co/spaces/<username>/hidms-demo`.

---

## Part 4 — After deployment

- Add a **live demo badge** to your README so reviewers can click straight
  into the app:

  ```markdown
  [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://enriched-hidms.streamlit.app)
  ```

- Keep the deployment honest: add a short note in the app or README that the
  model is trained on **simulated data** and is a thesis demo, not a medical
  device (already present in `app.py`).

---

## Troubleshooting

| Problem | Fix |
| ------- | --- |
| App shows "ModuleNotFoundError: hidms" | Ensure `src/` layout is imported: the package is not installed on the cloud. Run `pip install -e .` locally and add it to the deploy script if needed. |
| Build fails on `streamlit` | Make sure `streamlit` is listed in `requirements.txt` (it is). |
| App deploys but crashes | Check **Deploy log** / **App logs** in the Streamlit dashboard; share the error if you need help. |
| Changes don't appear | Push to `main` — Streamlit auto-redeploys on every push. |

---

## Summary

```
GitHub (code)  →  Streamlit Community Cloud (hosting)  →  Public URL
     ↑                                                          ↑
  git push                                              share the link!
```

**Next step:** push the demo to GitHub, then follow Part 2. The whole thing
takes about 15 minutes and costs nothing.
