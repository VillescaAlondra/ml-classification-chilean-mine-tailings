# 🏔️ ML Classification of Chilean Mine Tailings

**Clasificación de Depósitos de Relaves Mineros en Chile mediante Machine Learning**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📄 Overview | Resumen

**EN:** This project applies a hybrid unsupervised + supervised machine learning pipeline to classify Chilean mine tailings deposits based on their geochemical signatures. Using publicly available data from SERNAGEOMIN (~2,000 samples, 57 geochemical variables), the methodology groups deposits into geologically interpretable clusters and trains classifiers to predict deposit types — addressing an extreme class imbalance ratio of 237:1.

**ES:** Este proyecto aplica un pipeline híbrido de machine learning (no supervisado + supervisado) para clasificar depósitos de relaves mineros chilenos según sus firmas geoquímicas. Utilizando datos públicos de SERNAGEOMIN (~2.000 muestras, 57 variables geoquímicas), la metodología agrupa depósitos en clusters geológicamente interpretables y entrena clasificadores para predecir tipos de depósitos, abordando un desbalance de clases extremo de 237:1.

---

## 🔬 Methodology | Metodología

### Pipeline

```
Raw Geochemical Data (SERNAGEOMIN)
        │
        ▼
┌─────────────────────┐
│   Preprocessing     │
│  log₁₀(x+1) + Z-Score │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Unsupervised      │
│   K-Means (k=4)     │
│   Cluster Formation │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Cluster Selection │
│   Composite Score:  │
│   60% Enrichment +  │
│   40% Mutual Info   │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Supervised        │
│   Classification    │
│   LR / SVM / RF /   │
│   TabNet            │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Validation        │
│   3D t-SNE & UMAP   │
│   Geological interp.│
└─────────────────────┘
```

### Geological Groups Identified | Grupos Geológicos Identificados

| Group | Description | Key Elements |
|-------|-------------|-------------|
| **CuAu_Mixto** | Porphyry-epithermal Cu-Au continuum | Cu, Au |
| **CuMo_Pórfidos** | Cu-Mo porphyry deposits | Cu, Mo (+81.8%) |
| **ZnPb_Polimetálicos** | Polymetallic Zn-Pb deposits | Zn (+99.5%), Pb |
| **Carbonatos_Reemplazo** | Carbonate replacement deposits | Ca, Mg |

---

## 📊 Key Results | Resultados Principales

### Classification Performance (Balanced Accuracy)

| Model | Balanced Accuracy |
|-------|:-----------------:|
| **Logistic Regression** | **0.8062** |
| SVM | 0.7678 |
| TabNet | 0.6647 |
| Random Forest | 0.6580 |

### Additional Metrics

- **Class imbalance reduction:** 237:1 → ~16:1 after clustering
- **Statistical validation:** χ² > 6,000 | p < 10⁻²⁰ | 92.9% of variables significant (Kruskal-Wallis)
- **Silhouette (minority groups):** used for model selection due to extreme imbalance

### Dimensionality Reduction (3D Visualization)

| Method | Parameters | Silhouette (islands) |
|--------|-----------|:--------------------:|
| **UMAP** | n_neighbors=15, min_dist=0.3 | **+0.261** |
| t-SNE | perplexity=50, lr=100, iter=1500 | +0.241 |

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **ML & Data:**
  - scikit-learn (Random Forest, SVM, Logistic Regression, K-Means, PCA, Self-Training)
  - PyTorch + TabNet
  - UMAP-learn
  - pandas, NumPy
- **Statistics:** SciPy, statsmodels (Kruskal-Wallis, Mann-Whitney U, Bonferroni correction)
- **Visualization:** Matplotlib, Seaborn, Plotly (3D)

---

## 📁 Repository Structure

```
├── notebooks/
│   ├── 01_pipeline_principal.ipynb      # Complete ML pipeline
│   ├── 02_experimento_binario_AuCu.ipynb # Binary Au-Cu classification experiment
│   └── 03_experimento_Au_Cu_AuCu.ipynb   # Multi-class Au/Cu/Au-Cu experiment
├── src/
│   └── eda_datos_geoquimicos.py          # EDA and data cleaning functions
├── docs/                                  # Additional documentation
├── figures/                               # Generated plots and visualizations
├── requirements.txt                       # Python dependencies
├── .gitignore                             # Git ignore rules
├── LICENSE                                # MIT License
└── README.md                              # This file
```

---

## 🚀 Getting Started | Cómo Empezar

### Prerequisites | Requisitos

```bash
pip install -r requirements.txt
```

### Usage | Uso

1. Download the SERNAGEOMIN geochemical dataset (publicly available)
2. Place the data file in the project root directory
3. Open `notebooks/01_pipeline_principal.ipynb` and follow the pipeline step by step

---

## 📚 References | Referencias

- Reyes Reyes, F.A., Pérez Cortés, S., & Gramsch Labra, E. (2025). *Machine Learning Applied to Geochemical Classification of Mine Tailings.* Minerals, 16(1), 5. [DOI: 10.3390/mins16010005](https://doi.org/10.3390/mins16010005)
- Sillitoe, R.H. (2010). *Porphyry Copper Systems.* Economic Geology, 105(1), 3–41.
- Sillitoe, R.H. & Hedenquist, J.W. (2003). *Linkages between volcanotectonic settings, ore-fluid compositions, and epithermal precious metal deposits.* SEG Special Publications, 10, 315–343.
- Leach, D.L. et al. (2005, 2010). *Sediment-hosted lead-zinc deposits.*
- Meinert, L.D. et al. (2005). *World Skarn Deposits.* Economic Geology 100th Anniversary Volume.
- Heinrich, C.A. (2024). *Fluid Evolution and Ore Formation in Porphyry-Epithermal Systems.*

---

## 📝 Data Source | Fuente de Datos

Geochemical data from **SERNAGEOMIN** (Servicio Nacional de Geología y Minería de Chile), 2023 dataset. Publicly available at [sernageomin.cl](https://www.sernageomin.cl/).

---

## 👥 Authors | Autores

- **Guillermo** — Mining Engineering + Data Science
- **Alondra Villesca** — Primary author

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
