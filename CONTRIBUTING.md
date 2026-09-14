# Contributing

This repository accompanies *Mathematical Programming in Machine Learning and Artificial Intelligence: A Unified Taxonomy of Models and Applications*. Its application scope follows [the paper on arXiv](https://arxiv.org/abs/2609.07254): **30 applications within 10 paradigms**.

Contributions can correct references, improve explanations, add verified primary papers or author-maintained implementations to an existing application, clarify mathematical assumptions, or improve navigation. When proposing a new application category, open a scope discussion first; the companion should continue to agree with the paper.

## Adding or correcting a reference

1. Identify the existing application number (1–30) and explain the connection.
2. Link a primary publisher, conference proceedings, PMLR, ACL Anthology, OpenReview, or author/arXiv record. Check title, authors, venue/status, year, and available identifiers. Do not infer acceptance from a planned venue or a preprint.
3. State whether the relationship is **Explicit formulation**, **Equivalent formulation**, or **Natural MP reformulation**. Explain any surrogate, relaxation, architectural interpretation, or modified assumptions.
4. Update the corresponding README entry and, where relevant, the [modeling guide](docs/modeling-guide.md). Label code links as official only when the authors identify them as such.
5. Update the corresponding application or reference metadata directly in [data/applications.json](data/applications.json), then run the checks below. Keep the survey link pointed to its arXiv record.

## Mathematical fidelity

Preserve the paper's application numbering. Keep network-flow tracking under Linear Programming. Keep combined entries together: data subset selection and active learning; notification/email allocation and frequency; diffusion hyperparameters and noise schedules; and both constrained and diversity-aware inner-product retrieval.

Distinguish observed data from decision variables. State principal domains and assumptions. Do not transfer a guarantee for a subproblem, surrogate, or relaxation to an entire learning system. In particular, a stationary point is not a global optimum, an agentic two-level loop need not be differentiable bilevel optimization, and an approximate cache policy is not an exact static subset optimizer.

## Local checks

Python 3.9 or newer is sufficient; no extra Python packages are required.

```sh
python3 scripts/validate.py
```

The catalog is maintained as standalone JSON. Keep citation keys consistent across its application and reference records, and update the README and modeling guide when a change affects their explanations or citations. See [the catalog documentation](data/README.md) for its fields.

GitHub Actions checks application coverage, catalog consistency, citation keys, and local documentation links. Mathematical correctness and attribution still require human review.

Include the validation result and a short explanation of the change in your pull request.
