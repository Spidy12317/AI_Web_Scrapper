# WebPilot AI (AI_Web_Scrapper): A Multimodal Approach to Web Data Extraction  
DA623: Multimodal Data Analysis and Learning (Winter 2025)  
Indian Institute of Technology Guwahati  

---

## Overview

**WebPilot AI** is a multimodal web scraping framework that combines traditional HTML parsing, visual reasoning via Vision-Language Models (VLMs), and browser automation. It addresses challenges where classic scrapers fail especially on dynamic, JavaScript-rendered, or visually structured websites.

---

## Motivation

Traditional web scraping techniques often fail when:
- Content loads dynamically via JavaScript
- Data appears only after user interactions (scrolling, clicking)
- Information is embedded in images or canvas elements

**WebPilot AI** tackles these limitations by combining:
- HTML parsing (for static pages)
- Vision-based data extraction (for visually complex sites)
- Browser automation (for user interaction emulation)

This hybrid, multimodal approach ensures robustness across various web architectures.

---

## Relevance to Multimodal Learning

This project focuses on **multimodal learning** by integrating multiple data modalities:
- **Textual**: DOM parsing from HTML documents
- **Visual**: Image-based reasoning via Vision-Language Models (e.g., GPT-4V, LLaVA)
- **Behavioral**: Simulated user interactions through automated browsing (scrolling, clicking)

Together, these components reflect the principles of multimodal AI—fusing diverse sources of information for intelligent behavior.

---

## Project Architecture

WebPilot AI operates in three modes:

### 1. HTML Scraping (Textual Modality)
- Uses `requests`, `BeautifulSoup`, and `pandas`
- Ideal for static, well-structured pages
- Fastest and most efficient when applicable

### 2. Vision-Based Extraction (Visual Modality)
- Uses `Playwright` to capture full-page screenshots
- Feeds images to Vision-Language Models (GPT-4V / LLaVA)
- Effective on poorly structured or canvas-based pages

### 3. Automated Browsing (Behavioral Modality)
- Uses `Playwright` for headless browsing
- Simulates user interactions (clicks, scrolls, typing)
- Useful for JavaScript-heavy sites or infinite scrolling pages

---

## Example Use Case: Scraping Google Search Results

**Challenge**: Google renders results after dynamic user input  
**Why HTML fails**: Initial HTML has only placeholders  
**Solution**:
1. Launch browser using Playwright
2. Enter query → simulate Enter key
3. Wait for content to load
4. Extract visible titles and URLs

---

## Comparative Analysis

| Mode               | Strengths                                | Limitations                                   |
|--------------------|-------------------------------------------|-----------------------------------------------|
| HTML Scraping      | Fast, simple, great for static sites      | Fails with JS-rendered or interactive pages   |
| Vision-based       | Layout-aware, works on visual structure   | Dependent on VLM quality, slower              |
| Automated Browsing | Handles complex interactivity             | Slower, higher resource usage                 |

---

## Key Learnings

- No single scraping method is universally sufficient.
- Vision-Language Models offer a human-like ability to interpret visual data.
- Combining textual, visual, and behavioral techniques maximizes coverage and resilience.

---

## Folder Structure (expected)
<pre><code>```bash AI_Web_Scrapper/ │ ├── LICENSE │ ├── README.md │ └── WebPilot_AI_blog.ipynb  ``` </code></pre>

---

## Tools & Libraries Used

- `BeautifulSoup` / `requests` / `pandas`
- `Playwright` (browser automation)
- `GPT-4V`, `LLaVA` (Vision-Language Models)
- `Python`, `Jupyter Notebook`

---

## References

- [Playwright Documentation](https://playwright.dev/python/)
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/)
- [GPT-4V (OpenAI)](https://openai.com/gpt-4v)
- [LLaVA](https://llava-vl.github.io/)

---

## Reflections

- **Scope for improvement**: Speed optimization, better model prompting, CAPTCHA-handling, and using self-hosted open models for cost-efficiency.

---

## GitHub Repo

🌐 *[Link to GitHub repository (https://github.com/Spidy12317/AI_Web_Scrapper.git)]*

---

## Thank You

