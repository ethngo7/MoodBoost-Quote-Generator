# 💬 MoodBoost Quote Generator

A work-in-progress web app that turns your written feelings into hand-picked motivational quotes. 

This project involves sentimental analysis, keyword extraction, and is built with **Python**, **Streamlit**, and lightweight NLP.

<img width="836" alt="Screenshot 2025-06-19 at 23 38 35" src="https://github.com/user-attachments/assets/4b1cba74-b8b3-451b-9c0f-fd60716067db" />


---

## ✨ What It Does
1. **User writes how they feel** (e.g. “I’m burnt out and anxious.”).  
2. **Sentiment & keyword analysis** runs locally:
   - Keyword matching across an expanded emotion dictionary.
   - Fast polarity check via TextBlob (backup).
3. The app assigns **emotion tags** (e.g. `["burnout", "anxiety"]`).
4. Press _“Show me quotes!”_  
   → Returns 2-3 quotes whose tags overlap with the detected emotions.
5. **“Get more quotes”** radio grabs a fresh batch on demand.

---

## 🔍 Under the Hood
| Layer                 | Library / Approach                                    |
|-----------------------|-------------------------------------------------------|
| UI                    | Streamlit                                             |
| NLP                   | TextBlob + custom keyword mapping                     |
| Quote retrieval       | Local `quotes.json` (≈ 30 curated quotes, tagged)     |
| Randomization         | Python `random.sample()`                              |

> **Planned:** swap or augment the local JSON with a live quotes API (e.g. [Quotable.io](https://github.com/lukePeavey/quotable)) for deeper variety.

---

## 🚀 Quick Start

```bash
git clone https://github.com/your-handle/moodboost-quotes.git
cd moodboost-quotes
pip install -r requirements.txt
streamlit run app_streamlit.py
