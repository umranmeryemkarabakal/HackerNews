# HackerNews

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Tkinter-1F2A44?style=for-the-badge" alt="Tkinter" />
  <img src="https://img.shields.io/badge/Requests-2B5B84?style=for-the-badge" alt="Requests" />
  <img src="https://img.shields.io/badge/BeautifulSoup-3C873A?style=for-the-badge" alt="BeautifulSoup" />
</p>

## Overview

Fetches the links on the Hacker News front page with Requests and BeautifulSoup, then lets you pick one by number in a small Tkinter window and shows the selected URL.

**Quick start:** `pip install -r requirements.txt && python main.py`

## Proje hakkında

Hacker News ana sayfasındaki bağlantıları `requests` ve `BeautifulSoup` ile toplayan, Tkinter arayüzünde seçilen sıradaki haberin adresini gösteren küçük bir web kazıma uygulaması.

## Özellikler

- `news.ycombinator.com` sayfasından `http/https` bağlantılarını çeker
- Spinbox ile kaçıncı haberin gösterileceği seçilir
- Sayfa alınamazsa HTTP durum kodunu yazdırır

## Kurulum ve çalıştırma

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

```bash
python main.py
```

## Dosya yapısı

```text
HackerNews/
└── main.py
```
