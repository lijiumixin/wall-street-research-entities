# Wall Street Research Entities (Multilingual Financial Entity & Broker Alias Dataset)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Languages](https://img.shields.io/badge/Languages-11-green.svg)](#coverage)
[![Powered by UnHideA](https://img.shields.io/badge/Live%20Research-UnHideA-111827.svg)](https://unhidea.com/en/)

An open, structured **11-language canonical entity dictionary** covering **405 global public companies** and **73 major investment banks / sell-side research institutions**, built for financial NLP, cross-border equity research pipelines, RAG entity normalization, and AI investment agents.

Maintained by **[UnHideA](https://unhidea.com/en/)** ([`@UnHideA` on X](https://x.com/UnHideA)) — a multilingual Wall Street research & market briefing platform covering [company hubs](https://unhidea.com/en/companies) and [research institutions](https://unhidea.com/en/institutions) across 11 languages.

---

## Why This Dataset Exists

Sell-side equity research, earnings transcripts, and cross-border market news routinely refer to the same company or bank under inconsistent names across languages and desks (for example: `Goldman Sachs` / `高盛` / `ゴールドマン・サックス`, `Bank of America` / `美银` / `美銀` / `バンク・オブ・アメリカ`, or `TSMC` / `台积电` / `Taiwan Semiconductor`).

This dataset provides clean, deduplicated canonical slugs, tickers, raw aliases, and 11-language localized labels so financial agents and search pipelines can normalize entities without writing ad-hoc regexes.

---

## Coverage

| File | Records | Format | Contents |
|---|---:|---|---|
| [`data/companies.json`](data/companies.json) | 405 | JSON | Canonical slug, English name, ticker (when available), aliases, 11-language labels, and live [UnHideA company hub URL](https://unhidea.com/en/companies) |
| [`data/companies.csv`](data/companies.csv) | 405 | CSV | Flat table (`slug`, `name_en`, `ticker`, `zh_hans`, `zh_hant`, `ja`, `aliases`, `hub_url_en`) |
| [`data/institutions.json`](data/institutions.json) | 73 | JSON | Canonical slug, English name, aliases, 11-language labels, and live [UnHideA institution hub URL](https://unhidea.com/en/institutions) |
| [`data/institutions.csv`](data/institutions.csv) | 73 | CSV | Flat table (`slug`, `name_en`, `ticker`, `zh_hans`, `zh_hant`, `ja`, `aliases`, `hub_url_en`) |

**Supported locales (11):** `en`, `zh-hans`, `zh-hant`, `ja`, `es`, `pt`, `ru`, `tr`, `id`, `ms`, `vi`.

---

## Record Schema

```json
{
  "slug": "bank-of-america",
  "name_en": "Bank of America",
  "ticker": "",
  "aliases": ["美银", "Bank of America"],
  "labels": {
    "en": "Bank of America",
    "zh-hans": "美银",
    "zh-hant": "美銀",
    "ja": "バンク・オブ・アメリカ",
    "es": "Bank of America",
    "pt": "Bank of America",
    "ru": "Bank of America",
    "tr": "Bank of America",
    "id": "Bank of America",
    "ms": "Bank of America",
    "vi": "Bank of America"
  },
  "hub_url_en": "https://unhidea.com/en/institution/bank-of-america"
}
```

---

## Quick Start (Python)

```bash
python3 examples/resolve.py "高盛" "苹果" "Morgan Stanley" "美银"
```

Example output:

```text
高盛 -> institution/goldman-sachs (Goldman Sachs) | https://unhidea.com/en/institution/goldman-sachs
苹果 -> company/apple (Apple) | https://unhidea.com/en/company/apple
Morgan Stanley -> institution/morgan-stanley (Morgan Stanley) | https://unhidea.com/en/institution/morgan-stanley
美银 -> institution/bank-of-america (Bank of America) | https://unhidea.com/en/institution/bank-of-america
```

---

## Live Research Hubs

Browse live structured research summaries mapped to these entities on UnHideA:

- **All Companies:** https://unhidea.com/en/companies (e.g. [Apple](https://unhidea.com/en/company/apple), [Microsoft](https://unhidea.com/en/company/microsoft), [Amazon](https://unhidea.com/en/company/amazon), [Meta](https://unhidea.com/en/company/meta), [Tesla](https://unhidea.com/en/company/tesla), [AMD](https://unhidea.com/en/company/amd))
- **All Institutions:** https://unhidea.com/en/institutions (e.g. [Goldman Sachs](https://unhidea.com/en/institution/goldman-sachs), [J.P. Morgan](https://unhidea.com/en/institution/j-p-morgan), [Morgan Stanley](https://unhidea.com/en/institution/morgan-stanley), [Citi](https://unhidea.com/en/institution/citi), [Bernstein](https://unhidea.com/en/institution/bernstein))
- **Updates on X:** https://x.com/UnHideA

## License

MIT License — free for commercial and research use. See [LICENSE](LICENSE).
