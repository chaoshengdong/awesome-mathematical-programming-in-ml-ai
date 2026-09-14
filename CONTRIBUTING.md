# Contributing

This repository accompanies *Mathematical Programming in Machine Learning and Artificial Intelligence: A Unified Taxonomy of Models and Applications*. Its application scope follows [the paper on arXiv](https://arxiv.org/abs/2609.07254): **30 applications within 10 paradigms**.

Contributions can correct references, add verified primary papers to an existing application, or improve navigation. Please keep entries concise: an application heading followed by its citations.

## Adding or correcting a reference

1. Identify the existing application by name.
2. Link a primary publisher, conference proceedings, PMLR, ACL Anthology, OpenReview, or author/arXiv record. Check title, authors, venue/status, year, and available identifiers. Do not infer acceptance from a planned venue or a preprint.
3. Add or correct the citation under the matching unnumbered README heading. Include authors, the linked paper title, venue or preprint status, and year.
4. Update the corresponding application or reference metadata directly in [data/applications.json](data/applications.json), then run the checks below. Keep the survey link pointed to its arXiv record.

## Organization

Use unnumbered application headings under the relevant mathematical-programming paradigm. Keep network-flow tracking under Linear Programming. Keep combined entries together: data subset selection and active learning; notification/email allocation and frequency; diffusion hyperparameters and noise schedules; and both constrained and diversity-aware inner-product retrieval.

The README is a reading list. Detailed formulations and discussion belong in the linked research papers.

## Local checks

Python 3.9 or newer is sufficient; no extra Python packages are required.

```sh
python3 scripts/validate.py
```

The catalog is maintained as standalone JSON. Keep citation keys consistent across its application and reference records, and update the README when citations change. See [the catalog documentation](data/README.md) for its fields.

GitHub Actions checks application coverage, catalog consistency, citation keys, unnumbered headings, and local documentation links.

Include the validation result and a short explanation of the change in your pull request.
