# Talent_Lens

> **Analyze your resume and portfolio securely — 100% inside your browser. Zero uploads. Zero tracking.**

![TalentLens Banner](https://img.shields.io/badge/TalentLens-Sandbox%20Core%20v2.0-7c3aed?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMiAxNWwtNS01IDEuNDEtMS40MUwxMCAxNC4xN2w3LjU5LTcuNTlMMTkgOGwtOSA5eiIvPjwvc3ZnPg==)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Zero Backend](https://img.shields.io/badge/backend-none-blue?style=for-the-badge)
![HTML Only](https://img.shields.io/badge/stack-HTML%20%2B%20JS-orange?style=for-the-badge)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Live Demo / Quick Start](#-live-demo--quick-start)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Running Locally](#-running-locally)
- [Scoring Methodology](#-scoring-methodology)
- [Privacy Model](#-privacy-model)
- [Limitations & Known Gaps](#-limitations--known-gaps)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧠 Overview

**TalentLens** is a fully client-side, privacy-first tool for evaluating resumes and developer portfolios. It gives job seekers instant, structured feedback without sending a single byte to any server.

There are two core analyzers:

| Analyzer | Input | Output |
|---|---|---|
| **Resume Grader** | Upload PDF, DOCX, or TXT | ATS Score, skills map, strengths & weaknesses |
| **Portfolio Grader** | Enter a website URL | Heuristic score for UI/UX, projects, and mobile-friendliness |

When both are used together, TalentLens produces a **Composite Hireability Index** — a weighted score combining your resume and portfolio performance.

---

## ⚡ Live Demo / Quick Start

### Option 1 — Open directly in browser (zero setup)

```bash
# Just double-click index.html — no server needed
open index.html
```

### Option 2 — Run with the local dev server

```bash
# Requires Python 3
python main.py
```

The server will start at `http://localhost:8000` and automatically open your browser.

### Option 3 — Portable Single-File App

Inside the running app, click **"Download Portable HTML Application"** in the footer to get a self-contained `.html` file you can use anywhere, share with friends, or keep offline.

---

## ✨ Features

### 📄 Resume Grader
- **Drag-and-drop or click-to-upload** — supports PDF, DOCX, and TXT formats
- **ATS Score (0–100)** — simulates Applicant Tracking System evaluation
- **Skill detection** — scans for 14+ in-demand tech skills (React, Python, Docker, AWS, etc.)
- **Role targeting** — tailor analysis to a specific job title (Frontend Developer, Data Scientist, etc.)
- **One-click role presets** — Frontend, Backend, Full Stack, Data Scientist
- **Strengths & Weaknesses** — structured feedback on metrics, action verbs, and links
- **Word count check** — flags resumes that are too short
- **Export to PDF** — download a formatted grader report via jsPDF
- **Sandbox history** — stores your last 10 scans in `localStorage` for quick revisit
- **History management** — reload, delete, or clear all past scans

### 🌐 Portfolio Grader
- **URL-based heuristic evaluation** — enter any portfolio website URL
- **Sub-scores** for three key dimensions:
  - 🎨 UI/UX Design
  - 🗂️ Projects quality
  - 📱 Mobile-friendliness
- **Strengths & Weaknesses** panel with actionable suggestions

### 🏆 Composite Hireability Index
- Unlocks when **both** resume and portfolio are analyzed
- Weighted formula: `Resume × 55% + Portfolio × 45%`
- Color-coded animated score ring (green / amber / red)
- Verdict text: *Top Tier*, *Strong Cohesion*, or *Room to Grow*
- Animated progress bars for each component score

### 🎨 UI & UX
- Dark-mode glassmorphic design using `oklch()` color space
- Smooth fade-in and ring animations
- Fully responsive — works on mobile and desktop
- Drag-and-drop file support with visual feedback

---

## 🔬 How It Works

### Resume Analysis Pipeline

```
User uploads file
       │
       ▼
  extractDocText()
  ┌────────────────────────────────┐
  │  .txt  → FileReader API        │
  │  .docx → Mammoth.js parser     │
  │  .pdf  → PDF.js text extractor │
  └────────────────────────────────┘
       │
       ▼
  evaluateResume(text, role)
  ┌────────────────────────────────────────────────────────┐
  │  1. Keyword match against SKILLS array (14 items)      │
  │  2. Regex check for quantified metrics (%, $, n+)      │
  │  3. Presence of professional links (GitHub, LinkedIn)  │
  │  4. Action verb detection (led, built, designed…)      │
  │  5. Word count validation (< 200 = flagged)            │
  │                                                        │
  │  Score = 35 + (skills × 3.5) + (metrics ? 15 : 0)     │
  │            + (links ? 10 : 0) + (verbs × 4.5)         │
  │  Clamped to [10, 100]                                  │
  └────────────────────────────────────────────────────────┘
       │
       ▼
  Result saved to localStorage (up to 10 scans)
  Rendered with animated score ring + tag grid
```

### Portfolio Analysis Pipeline

```
User enters URL
       │
       ▼
  runPortfolioAnalysis()
  ┌─────────────────────────────────────────────────────────┐
  │  Deterministic hash of URL string                       │
  │  → Pseudo-random but consistent scores per URL          │
  │  → UI Score, Projects Score, Mobile Score derived       │
  │  → Composite weighted: 40% + 40% + 20%                  │
  │  Fixed strengths/weaknesses catalogue returned          │
  └─────────────────────────────────────────────────────────┘
       │
       ▼
  Rendered with sub-score grid + strengths/weaknesses panel
```

> **Note:** Portfolio analysis is currently heuristic/simulated. It does not fetch or crawl the URL. See [Roadmap](#-roadmap) for planned real analysis.

---

## 📁 Project Structure

```
talentlens/
│
├── index.html          # The entire application — UI, logic, styles
├── main.py             # Optional Python local dev server (port 8000)
└── README.md           # This file
```

TalentLens is intentionally a **single-file application**. Everything — HTML, CSS, JavaScript — lives in `index.html` for maximum portability.

---

## 🛠 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Document parsing** | [PDF.js 3.4.120](https://mozilla.github.io/pdf.js/) | Extract text from PDF files |
| **Document parsing** | [Mammoth.js 1.6.0](https://github.com/mwilliamson/mammoth.js) | Extract text from DOCX files |
| **PDF export** | [jsPDF 2.5.1](https://github.com/parallax/jsPDF) | Generate downloadable PDF reports |
| **Icons** | [Lucide](https://lucide.dev/) | SVG icon library |
| **Fonts** | [Google Fonts](https://fonts.google.com/) | Inter (body) + Outfit (headings) |
| **Dev server** | Python `http.server` | Zero-dependency local file server |
| **Storage** | Browser `localStorage` | Persists scan history client-side |
| **Styling** | Vanilla CSS + `oklch()` | Glassmorphic dark UI, no framework |

**No build tools. No npm. No framework. No backend.**

---

## 🚀 Running Locally

### Prerequisites

- A modern browser (Chrome, Firefox, Edge, Safari)
- Python 3.x *(only if using `main.py`)*

### Method 1: Direct file open

```bash
# Clone the repo
git clone https://github.com/your-username/talentlens.git
cd talentlens

# Open in browser
open index.html           # macOS
xdg-open index.html       # Linux
start index.html          # Windows
```

### Method 2: Python dev server

```bash
python main.py
# Server starts at http://localhost:8000
# Browser opens automatically after ~0.8s
# Press Ctrl+C to stop
```

The Python server avoids browser restrictions on local `file://` URLs (some browsers block certain APIs like `crypto.randomUUID()` on file protocol).

---

## 📊 Scoring Methodology

### Resume ATS Score

| Signal | Points |
|---|---|
| Base score | 35 |
| Per matched skill keyword | +3.5 (up to 14 skills) |
| Quantified metrics found (`%`, `$`, `n+`) | +15 |
| Professional links (GitHub/LinkedIn) | +10 |
| Per action verb (`led`, `built`, `managed`, etc.) | +4.5 |
| **Maximum** | **100** |
| **Minimum** | **10** |

**Skills detected:** JavaScript, TypeScript, React, Next.js, Node.js, Python, SQL, AWS, Docker, GraphQL, HTML, CSS, Tailwind, Git

### Portfolio Score

Sub-scores are derived deterministically from a hash of the URL:

| Dimension | Weight |
|---|---|
| UI/UX Design | 40% |
| Projects | 40% |
| Mobile Friendliness | 20% |

### Composite Hireability Index

```
Composite = (Resume Score × 0.55) + (Portfolio Score × 0.45)
```

| Range | Verdict |
|---|---|
| 80–100 | 🟢 Top Tier Profile |
| 60–79 | 🟡 Strong Cohesion |
| 0–59 | 🔴 Room to Grow |

---

## 🔒 Privacy Model

TalentLens is built around a strict **local sandbox** principle:

- ✅ All file parsing happens inside your browser using Web APIs
- ✅ No resume text is sent to any server
- ✅ No analytics, no tracking, no cookies
- ✅ Scan history is stored in `localStorage` — only on your device
- ✅ The app functions fully offline after initial load (except CDN fonts/icons)
- ❌ Portfolio analysis does **not** crawl or fetch the URL you enter

---

## ⚠️ Limitations & Known Gaps

- **Portfolio scoring is simulated.** Scores are generated from a URL hash, not real page analysis. The same URL will always return the same score, but it does not reflect actual page quality.
- **Resume scoring is heuristic.** It does not use an actual ATS engine or NLP model. It works on keyword presence and simple regex patterns.
- **No multi-page layout awareness.** PDF parsing is text-only; visual structure (columns, tables) is not interpreted.
- **Skills list is fixed.** The 14-skill dictionary is hardcoded. Niche or emerging skills won't be detected.
- **No network fetching.** The portfolio grader cannot access or screenshot the target URL due to browser CORS restrictions.

---

## 🗺 Roadmap

- [ ] **Real portfolio crawling** via a lightweight serverless function (opt-in)
- [ ] **Expanded skill taxonomy** — DevOps, cloud, design tools, soft skills
- [ ] **Job description matching** — paste a JD and score resume alignment
- [ ] **AI-powered suggestions** — integrate Claude/GPT for richer feedback
- [ ] **Multi-resume comparison** — side-by-side score diff
- [ ] **Dark/light theme toggle**
- [ ] **CSV export** of scan history

---

## 🤝 Contributing

Contributions are welcome! Since this is a single-file project, keeping it lean and dependency-free is a core goal.

```bash
# 1. Fork the repo
# 2. Make your changes in index.html
# 3. Test in at least two browsers
# 4. Submit a pull request with a clear description
```

Please keep PRs focused. Avoid introducing npm, build tools, or server-side dependencies unless there's a compelling reason.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

<p align="center">
  Built with ♥ · TalentLens Sandbox Core v2.0
</p>
 


