# Structured application catalog

[applications.json](applications.json) is a standalone, curated catalog based on [the survey on arXiv](https://arxiv.org/abs/2609.07254). It contains 30 application records, 10 paradigm records, and 36 primary literature references. The `survey_url` field links to the survey's arXiv record.

Each application records its number, documentation anchor, title, paradigm, classification, main decision variable, principal constraint or structure, survey relationship label, and representative and additional citation keys. These records support navigation and comparison; the [modeling guide](../docs/modeling-guide.md) explains the formulations and assumptions.

The `references` object contains bibliographic metadata: citation key, title, authors, venue, year, and primary URL, with DOI and page information where available. Application citation keys identify these records. Verify metadata against a primary publisher, proceedings, or author record when making corrections.

Edit the catalog directly, keep the README and modeling guide consistent with any changes, and validate from the repository root:

```sh
python3 scripts/validate.py
```

The catalog records the **manuscript's labels**. A label by itself is not a claim that every displayed normalization is identical to a cited algorithm. Read the qualifications in the [modeling guide](../docs/modeling-guide.md), especially for agentic scientific discovery, coreset surrogates, and dynamic cache selection.
