# 🥷 halfprice-hunter-agent

An autonomous AI Agent that helps you detect and track **50% off bento boxes** at your local supermarket.  
Combining OCR + user preferences + timing prediction, this Agent answers the big daily question:

> ❓ “Should I go now and grab that bento?”  

---

## 🎯 Features

- 📸 **Image OCR**: Upload a photo of the discount shelf, get instant recognition of items + discounts.
- 🤖 **Preference Matching**: Tells you whether today's discounted items match your favorite foods.
- ⏰ **Smart Timing**: Learns the best time to go based on past discount patterns.
- 🔔 **Go/No-Go Recommendation**: Suggests whether it's worth heading out now or skipping today.

---

## 📦 Tech Stack

- [Mines](https://github.com/deepthinking-xyz/mines) - for managing the Agent
- `EasyOCR` / `PaddleOCR` - for image recognition
- Python 3.10+
- Optional: Telegram Bot or LINE for image upload & notifications

---

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/halfprice-hunter-agent.git
cd halfprice-hunter-agent
pip install -r requirements.txt
python main.py
