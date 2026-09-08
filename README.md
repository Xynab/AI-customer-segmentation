# AI Customer Segmentation

An e-commerce customer segmentation project: a Jupyter notebook does the actual machine learning (feature engineering, KMeans clustering, PCA visualization), and a Flask web dashboard displays the segmented results with interactive charts and a data table.

---

## How it works

**1. Feature engineering** (`notebooks/01_load_data.ipynb`) — raw customer data is cleaned and enriched: `Purchase_History` (a JSON-like list per customer) is parsed into a purchase count, and a numeric rating is extracted from free-text product reviews via regex. Final features: Age, Annual Income, Time on Site, Total Purchases, Avg Rating.

**2. Clustering** — features are standardized (`StandardScaler`), then the optimal cluster count is chosen using the **elbow method** (inertia across k=1–10) and validated with **silhouette scores** (k=2–6). The final model is **KMeans with k=3**.

**3. Segment labeling & PCA** — each cluster is mapped to a business-friendly label (*Premium Browsers*, *Standard Customers*, *Loyal Fast Buyer (VIP)*) with a matching marketing-strategy recommendation, and the clusters are visualized in 2D via **PCA**. The labeled result is exported to `outputs/segmented_customers.csv`.

**4. Dashboard** (`app.py`, Flask) — accepts an uploaded CSV and renders it: KPI cards (segment counts), a Chart.js bar chart of segment distribution, and a browsable data table. The Flask app itself does not run any clustering — it expects a CSV that already has the `Customer_Type` column, i.e. the notebook's output file re-uploaded. The "Business Insights" panel is a fixed set of marketing bullet points, not generated per-dataset.

## Tech stack

**ML:** Python, pandas, scikit-learn (StandardScaler, KMeans, PCA, silhouette_score), matplotlib

**Web:** Flask, Tailwind CSS, Chart.js

## Architecture

```
notebooks/
└── 01_load_data.ipynb      # all the actual ML: feature engineering,
                             # scaling, KMeans, silhouette validation,
                             # PCA, cluster labeling
outputs/
└── segmented_customers.csv # notebook's output — the file the dashboard expects
app.py                      # Flask app: upload → value_counts → render dashboard
upload.html / dashboard.html
```

## Running it

**Reproduce the clustering:**
```bash
jupyter notebook notebooks/01_load_data.ipynb
```
Run all cells — this regenerates `outputs/segmented_customers.csv`.

**View the dashboard:**
```bash
pip install flask pandas
python app.py
```
Open `http://127.0.0.1:5000`, then upload `outputs/segmented_customers.csv` (or any CSV with the same `Customer_Type` column already populated).

## Notes on scope

This is deliberately split into an offline analysis step and a lightweight results viewer, rather than a single live pipeline. The clustering logic (feature engineering, scaling, elbow/silhouette validation, KMeans, PCA) is genuine and the part worth walking through in an interview. The web app's job is presentation, not computation — uploading a raw, unsegmented dataset won't work, since there's no clustering step wired into Flask. A natural next step would be to move the notebook's pipeline into `app.py` so the dashboard can cluster a fresh upload on the spot.
