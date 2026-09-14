# Structured application catalog

[applications.json](applications.json) is a standalone, curated catalog based on [the survey on arXiv](https://arxiv.org/abs/2609.07254). It contains 30 application records, 10 paradigm records, and 36 primary literature references. The `survey_url` field links to the survey's arXiv record.

Each application records its title, paradigm, and citation keys. Internal identifiers and stable anchors support validation and existing links; they are not displayed as application numbering in the README.

The `references` object contains bibliographic metadata: citation key, title, authors, venue, year, and primary URL, with DOI and page information where available. Application citation keys identify these records. Verify metadata against a primary publisher, proceedings, or author record when making corrections.

Edit the catalog directly, keep the README citations consistent with any changes, and validate from the repository root:

```sh
python3 scripts/validate.py
```
