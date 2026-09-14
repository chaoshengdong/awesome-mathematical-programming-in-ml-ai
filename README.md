<div align="center">

# Awesome Mathematical Programming in ML & AI

**A guide to the models behind learning, retrieval, recommendation, and AI systems.**

[![Applications: 30](https://img.shields.io/badge/applications-30-2563eb)](#taxonomy)
[![Paradigms: 10](https://img.shields.io/badge/paradigms-10-0f766e)](#taxonomy)
[![arXiv: 2609.07254](https://img.shields.io/badge/arXiv-2609.07254-b31b1b)](https://arxiv.org/abs/2609.07254)
[![References: 36](https://img.shields.io/badge/references-36-7c3aed)](data/applications.json)

[Paper on arXiv](https://arxiv.org/abs/2609.07254) · [Explore the taxonomy](#taxonomy) · [Modeling guide](docs/modeling-guide.md) · [Contribute](CONTRIBUTING.md)

</div>

This repository accompanies **[“Mathematical Programming in Machine Learning and Artificial Intelligence: A Unified Taxonomy of Models and Applications”](https://arxiv.org/abs/2609.07254)** by [Chaosheng Dong](mailto:ensteindcs@gmail.com), available as **arXiv:2609.07254**. It organizes the manuscript's **30 applications across 10 mathematical-programming paradigms**, with links to primary papers and short explanations of the decisions, constraints, and computational structure.

The starting point is a practical question: **how do predictions become decisions?** A relevance score becomes a context under a token budget; routing scores become capacity-feasible assignments; several task losses become a Pareto trade-off. The taxonomy makes those connections explicit while distinguishing the formulation in a primary paper from an equivalent representation or a modeling interpretation introduced by the survey.

Read the [paper on arXiv](https://arxiv.org/abs/2609.07254) for the full formulations, notation, assumptions, and limitations. This repository is a literature and modeling companion; it does not provide implementations or benchmarks of the listed methods.

## Contents

- [Paper and repository](#paper-and-repository)
- [Taxonomy](#taxonomy)
- [How to read the relationship labels](#relationship-labels)
- [Linear Programming](#linear-programming)
- [Quadratic Programming](#quadratic-programming)
- [Binary and Mixed-Integer Programming](#binary-and-mixed-integer-programming)
- [Conic Programming](#conic-programming)
- [Bilevel Programming](#bilevel-programming)
- [Multi-Objective Optimization](#multi-objective-optimization)
- [Inverse Optimization](#inverse-optimization)
- [Distributionally Robust Optimization](#distributionally-robust-optimization)
- [Submodular Optimization](#submodular-optimization)
- [Min–Max and Saddle-Point Optimization](#minmax-and-saddle-point-optimization)
- [Research challenges](#research-challenges)
- [Contributing](#contributing)
- [Citation](#citation)
- [Acknowledgment](#acknowledgment)

## Paper and repository

| Resource | What it contains |
| :--- | :--- |
| [Paper on arXiv](https://arxiv.org/abs/2609.07254) | Public preprint, first submitted September 7, 2026 |
| [Application and reference catalog](data/applications.json) | Structured records for the 30 application units and 36 primary literature references |
| [Modeling guide](docs/modeling-guide.md) | Modeling distinctions and practical considerations across paradigms |
| [Contribution guide](CONTRIBUTING.md) | How to propose corrections and source-grounded updates |

Use the arXiv record for the survey's public preprint and citation. The separate RAG context-selection anchor, Xu et al., is recorded as a **2026 arXiv preprint**, following the bibliographic qualification in the manuscript.

## Taxonomy

The scope includes conventional linear, quadratic, mixed-integer, and conic programs, together with nested optimization, vector objectives, inverse problems, distributional uncertainty, set functions, and games. These are grouped by the modeling structure emphasized in the paper; the categories can overlap mathematically.

| Paradigm | Count | Applications | Central structure |
| :--- | ---: | :--- | :--- |
| [Linear Programming](#linear-programming) | 2 | [01](#app-01)–[02](#app-02) | Linear feasibility; absolute-value epigraphs; integral network-flow structure |
| [Quadratic Programming](#quadratic-programming) | 1 | [03](#app-03) | Local squared reconstruction error with affine constraints |
| [Binary and Mixed-Integer Programming](#binary-and-mixed-integer-programming) | 12 | [04](#app-04)–[15](#app-15) | Selection, assignment, logic, budgets, and pairwise interactions |
| [Conic Programming](#conic-programming) | 2 | [16](#app-16)–[17](#app-17) | Norm epigraphs and positive-semidefinite matrix lifts |
| [Bilevel Programming](#bilevel-programming) | 5 | [18](#app-18)–[22](#app-22) | Outer decisions evaluated through an inner optimization response |
| [Multi-Objective Optimization](#multi-objective-optimization) | 1 | [23](#app-23) | Conflicting task losses and Pareto stationarity |
| [Inverse Optimization](#inverse-optimization) | 1 | [24](#app-24) | Recovering an objective from observed behavior |
| [Distributionally Robust Optimization](#distributionally-robust-optimization) | 2 | [25](#app-25)–[26](#app-26) | Worst-case expectations over a specified ambiguity set |
| [Submodular Optimization](#submodular-optimization) | 3 | [27](#app-27)–[29](#app-29) | Diminishing returns under cardinality, length, or dynamic cache constraints |
| [Min–Max and Saddle-Point Optimization](#minmax-and-saddle-point-optimization) | 1 | [30](#app-30) | Competing generator and discriminator objectives |

Network-flow optimization is nested under **Linear Programming**. Combined entries remain single applications: notification/email allocation and frequency; constrained inner-product retrieval with linear and pairwise-diversity variants; diffusion hyperparameters and noise schedules; and data subset selection and active learning.

<a id="relationship-labels"></a>
## How to read the relationship labels

| Label | Meaning |
| :--- | :--- |
| **Explicit formulation** | The cited work directly formulates the application in the stated paradigm or a matching form. The survey may normalize notation and simplify the presentation. |
| **Equivalent formulation** | The survey presents an equivalent representation of the cited model or objective. Auxiliary variables or a different representation do not imply that the cited implementation used that solver form. |
| **Natural MP reformulation** | The survey translates an algorithmic or systems idea into a useful mathematical program. The primary paper is not claimed to solve the displayed program. |

The labels below follow the current manuscript. [Application 21](#app-21) needs particular care: its architectural normalization does **not** establish that an agentic scientific-discovery loop is a differentiable or globally solved bilevel program.

## Linear Programming

Linear programming (LP) minimizes or maximizes a linear objective subject to linear equalities and inequalities. A continuous formulation can also yield discrete decisions when its constraint structure guarantees integral extreme points.

<a id="app-01"></a>
### 01. Compressed sensing and basis pursuit

**Model insight.** Recover a signal from linear measurements by minimizing its ℓ₁ norm. Introducing nonnegative absolute-value epigraph variables converts basis pursuit to an LP: minimize their sum, preserve the measurement equations, and bound each signal coordinate between its negative and positive epigraph values. Exact sparse recovery requires assumptions on the sensing matrix in addition to solving the LP.

**Relationship:** Equivalent formulation. · [Formulation](docs/modeling-guide.md#app-01)

- David L. Donoho. [Compressed Sensing](https://doi.org/10.1109/TIT.2006.871582). *IEEE Transactions on Information Theory*, 2006.

### LP with Network-Flow Structure

<a id="app-02"></a>
#### 02. Min-cost network flow for multi-object tracking

**Model insight.** Select detections and transitions that form complete trajectories, minimizing detection, transition, start, and end costs. Flow conservation, source/sink supplies, and unit capacities enforce coherent tracks. With integral supplies and capacities, the node–arc incidence structure is totally unimodular and admits an integral optimal extreme point. Extra non-network coupling can remove that guarantee.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-02)

- Li Zhang, Yuan Li, and Ramakant Nevatia. [Global Data Association for Multi-Object Tracking Using Network Flows](https://doi.org/10.1109/CVPR.2008.4587584). *CVPR*, 2008.

## Quadratic Programming

Quadratic programming (QP) combines a quadratic objective with linear constraints. A positive-semidefinite objective Hessian yields convexity.

<a id="app-03"></a>
### 03. Local reconstruction weights in Locally Linear Embedding

**Model insight.** For each observed feature vector, minimize its squared reconstruction error using neighboring observations. Weights sum to one and vanish outside the fixed neighborhood; they need not be nonnegative. Each observation gives an independent convex QP. Nearly singular local covariance matrices motivate regularization.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-03)

- Sam T. Roweis and Lawrence K. Saul. [Nonlinear Dimensionality Reduction by Locally Linear Embedding](https://doi.org/10.1126/science.290.5500.2323). *Science*, 2000.

## Binary and Mixed-Integer Programming

Binary integer programming (BIP) encodes selection and assignment. Mixed-integer linear programming (MILP) combines discrete and continuous variables with linear constraints; mixed-integer quadratic programming (MIQP) retains quadratic objectives. Pairwise binary products produce binary quadratic programs (BQPs) or can be linearized at the cost of additional variables. Complexity and useful relaxations depend on the precise formulation.

<a id="app-04"></a>
### 04. RAG context selection under a token budget

**Model insight.** In retrieval-augmented generation (RAG), select passages that maximize estimated relevance or faithfulness within token and other resource budgets. At-most-one or exactly-one choices within passage groups yield a multidimensional multiple-choice knapsack problem (MMKP). The source uses Pareto-pruned dynamic programming for context selection before its generation-stage search.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-04)

- Shijia Xu et al. [Self-Correcting RAG: Enhancing Faithfulness via MMKP Context Selection and NLI-Guided MCTS](https://arxiv.org/abs/2604.10734). *arXiv preprint*, 2026. The manuscript does not assert unverified conference proceedings metadata.

<a id="app-05"></a>
### 05. Mixture-of-experts routing

**Model insight.** Binary token-to-expert assignments maximize routing scores while satisfying token assignment requirements and expert capacities. The pure capacitated bipartite structure can have an integral LP relaxation. Expert Choice instead fixes expert bucket sizes and permits a variable number of experts per token; the survey's normalized assignment model is not a claim that the router runs a BIP solver.

**Relationship:** Natural MP reformulation. · [Formulation](docs/modeling-guide.md#app-05)

- Yanqi Zhou et al. [Mixture-of-Experts with Expert Choice Routing](https://proceedings.neurips.cc/paper_files/paper/2022/hash/2f00ecd787b432c1d36f3de9800728eb-Abstract-Conference.html). *NeurIPS*, 2022.

<a id="app-06"></a>
### 06. Tool or agent-component selection

**Model insight.** Choose components that maximize expected task utility under monetary, latency, or token costs. Knapsack constraints set resource limits, conflict constraints prevent incompatible pairs, and dependency constraints require prerequisites. The resulting BIP exposes feasibility clearly, while additive utilities abstract away order effects and component interactions.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-06)

- Michelle Yuan et al. [Automated Composition of Agents: A Knapsack Approach for Agentic Component Selection](https://proceedings.neurips.cc/paper_files/paper/2025/hash/39c51d0fe64c273413a4d358361b3daa-Abstract-Conference.html). *NeurIPS*, 2025.

<a id="app-07"></a>
### 07. Notification/email allocation and frequency optimization

**Model insight.** User–message–time binaries maximize engagement or long-term value subject to user frequency caps, channel limits, campaign quotas, and a shared resource budget. Dual prices can separate many local choices. The survey combines insights from a notification-volume system and a separate industrial knapsack study; neither source is credited with the full generalized joint BIP.

**Relationship:** Natural MP reformulation. · [Formulation](docs/modeling-guide.md#app-07)

- Bo Zhao et al. [Notification Volume Control and Optimization System at Pinterest](https://doi.org/10.1145/3219819.3219906). *KDD*, 2018.
- Xingwen Zhang et al. [Solving Billion-Scale Knapsack Problems](https://doi.org/10.1145/3366423.3380084). *The Web Conference*, 2020.

<a id="app-08"></a>
### 08. Test-time reasoning and exploration-budget allocation

**Model insight.** Give each query exactly one reasoning-compute level with an estimated accuracy and cost, then maximize aggregate utility under a batch-wide compute budget. This multiple-choice knapsack model formalizes allocation across queries. Snell et al. motivate adaptive compute allocation, but do not present this across-query BIP.

**Relationship:** Natural MP reformulation. · [Formulation](docs/modeling-guide.md#app-08)

- Charlie Snell et al. [Scaling LLM Test-Time Compute Optimally Can Be More Effective than Scaling Model Parameters](https://openreview.net/forum?id=4FWaWZtd2n). *ICLR*, 2025.

<a id="app-09"></a>
### 09. Optimal decision-tree construction

**Model insight.** Jointly choose activated splits, split features and thresholds, sample-to-leaf assignments, and leaf predictions. A mixed-integer model trades misclassification against tree complexity while path constraints enforce consistent routing. Tight bounds, hierarchy constraints, symmetry handling, and warm starts matter for computational performance; early termination gives an incumbent and a gap rather than an exactness claim.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-09)

- Dimitris Bertsimas and Jack Dunn. [Optimal Classification Trees](https://doi.org/10.1007/s10994-017-5633-9). *Machine Learning*, 2017.

<a id="app-10"></a>
### 10. Best subset selection

**Model insight.** Fit regression coefficients by squared error while selecting at most a specified number of features. Binary indicators and valid coefficient-linking bounds force unselected coefficients to zero. The continuous quadratic objective is convex, but the full MIQP is combinatorial. Bounds, screening, and good feasible solutions can materially affect the solver's search.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-10)

- Dimitris Bertsimas, Angela King, and Rahul Mazumder. [Best Subset Selection via a Modern Optimization Lens](https://doi.org/10.1214/15-AOS1388). *The Annals of Statistics*, 2016.

<a id="app-11"></a>
### 11. Constrained maximum-inner-product retrieval

**Model insight.** Maximize query–item inner-product scores under a fixed list size and linear category, fairness, or coverage bounds. Adding a penalty on similarities of co-selected item pairs changes the linear binary model into a BQP/MIQP-style model, or an expanded MILP after exact product linearization. Both variants belong to this single retrieval application. The cited search algorithm is not claimed to solve the survey's generalized program.

**Relationship:** Natural MP reformulation. · [Formulation](docs/modeling-guide.md#app-11)

- Kohei Hirata et al. [Categorical Diversity-Aware Inner Product Search](https://doi.org/10.1109/ACCESS.2023.3234072). *IEEE Access*, 2023.

<a id="app-12"></a>
### 12. Mixed-precision neural-network quantization

**Model insight.** Assign exactly one bit-width to every layer, minimizing sensitivity-based estimated accuracy loss under model-size or hardware latency budgets. This is a multiple-choice integer linear program. HAWQ-V3 uses Hessian-based sensitivity and hardware-aware constraints; the quality of the resulting assignment depends on the accuracy of those loss and cost proxies.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-12)

- Zhewei Yao et al. [HAWQ-V3: Dyadic Neural Network Quantization](https://proceedings.mlr.press/v139/yao21a.html). *ICML*, 2021.

<a id="app-13"></a>
### 13. Diversity-aware recommendation

**Model insight.** Construct a fixed-length recommendation list by rewarding relevance and penalizing pairwise similarity among selected items. Optional linear constraints encode list feasibility. Binary products create a BQP; linearization introduces variables for item pairs. The survey's quadratic rendering expresses the accuracy–diversity trade-off without attributing a particular exact solver to the cited work.

**Relationship:** Natural MP reformulation. · [Formulation](docs/modeling-guide.md#app-13)

- Mi Zhang and Neil Hurley. [Avoiding Monotony: Improving the Diversity of Recommendation Lists](https://doi.org/10.1145/1454008.1454030). *RecSys*, 2008.

<a id="app-14"></a>
### 14. Globally optimized k-means clustering

**Model insight.** Jointly optimize binary cluster assignments and continuous centroids, charging squared distance only to each assigned cluster and requiring nonempty clusters. Direct assignment–centroid products yield a mixed-integer nonlinear program. Valid bounded reformulations can instead use quadratic epigraph constraints or specialized MILP constructions. This problem should not be labeled simply as a BQP; global certificates remain much harder to obtain than local clustering solutions.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-14)

- Kolos Cs. Ágoston and Marianna Eisenberg-Nagy. [Mixed Integer Linear Programming Formulation for K-means Clustering Problem](https://doi.org/10.1007/s10100-023-00881-1). *Central European Journal of Operations Research*, 2024.
- Jan Pablo Burgard et al. [Mixed-Integer Programming Techniques for the Minimum Sum-of-Squares Clustering Problem](https://doi.org/10.1007/s10898-022-01267-4). *Journal of Global Optimization*, 2023.

<a id="app-15"></a>
### 15. Video frame or keyframe selection

**Model insight.** Select query-relevant video frames under cardinality, temporal, or computation limits while penalizing redundant pairs. Pairwise terms produce an integer quadratic formulation. The cited work explicitly models this choice and uses a customized greedy method for efficiency; the heuristic is not a global optimality certificate.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-15)

- Bo Fang et al. [Threading Keyframe with Narratives: MLLMs as Strong Long Video Comprehenders](https://proceedings.iclr.cc/paper_files/paper/2026/hash/675a31be2d051be53d57bced52c6631f-Abstract-Conference.html). *ICLR*, 2026.

## Conic Programming

Second-order cone programming (SOCP) represents Euclidean norm constraints. Semidefinite programming (SDP) optimizes over positive-semidefinite matrices. These representations can expose convex geometry or provide bounds through relaxation.

<a id="app-16"></a>
### 16. Group Lasso as SOCP

**Model insight.** Minimize squared regression error plus weighted group ℓ₂ norms. Epigraph variables bound each group norm, and a rotated cone represents the squared residual cost, giving an equivalent convex SOCP. Block sparsity arises from the norm penalty without binary variables. Proximal or block-coordinate methods can solve the same objective without explicitly constructing cones.

**Relationship:** Equivalent formulation. · [Formulation](docs/modeling-guide.md#app-16)

- Ming Yuan and Yi Lin. [Model Selection and Estimation in Regression with Grouped Variables](https://doi.org/10.1111/j.1467-9868.2005.00532.x). *Journal of the Royal Statistical Society: Series B*, 2006.

<a id="app-17"></a>
### 17. Sparse PCA as SDP

**Model insight.** Lift a loading vector to a positive-semidefinite matrix with trace one, maximize explained variance, and constrain an entrywise ℓ₁ sparsity surrogate. Dropping the rank-one condition gives an SDP relaxation and an upper bound. Recovering a loading from a higher-rank solution is an additional approximation, not an exact equivalence to the original sparse component.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-17)

- Alexandre d'Aspremont et al. [A Direct Formulation for Sparse PCA Using Semidefinite Programming](https://proceedings.neurips.cc/paper/2628-a-direct-formulation-for-sparse-pca-using-semidefinite-programming). *NIPS*, 2004.

## Bilevel Programming

Bilevel models evaluate an outer decision through the response of an inner optimizer. In the manuscript's notation, the outer objective is Φ(λ, θ⋆(λ)), where θ⋆(λ) minimizes the inner objective Ψ(θ, λ). Unrolling, implicit differentiation, and approximate inner solves produce different computational approximations; a practical training loop need not reach a global bilevel solution.

<a id="app-18"></a>
### 18. Hyperparameter optimization

**Model insight.** Choose hyperparameters at the outer level to minimize validation loss after the inner level trains model parameters. This separates the data used to fit weights from the criterion used to choose training settings. Hypergradient quality depends on inner convergence, differentiability, and the treatment of optimizer dynamics.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-18)

- Luca Franceschi et al. [Bilevel Programming for Hyperparameter Optimization and Meta-Learning](https://proceedings.mlr.press/v80/franceschi18a.html). *ICML*, 2018.

<a id="app-19"></a>
### 19. Neural architecture search

**Model insight.** Optimize architecture parameters using validation loss while training network weights at the inner level. DARTS relaxes discrete operation choices into continuous mixtures. Architecture gradients become available, but selecting discrete operations after search creates a relaxation gap and requires independent evaluation of the final architecture.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-19)

- Hanxiao Liu, Karen Simonyan, and Yiming Yang. [DARTS: Differentiable Architecture Search](https://openreview.net/forum?id=S1eYHoC5FX). *ICLR*, 2019.

<a id="app-20"></a>
### 20. Coreset selection and data subsampling

**Model insight.** Outer subset indicators or selection probabilities specify a small training set; inner optimization trains the model on that selected or weighted data. A coreset-size constraint limits the selection. Probabilistic selection supports stochastic outer updates, but expected subset size and realized subset quality are different guarantees.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-20)

- Xiao Zhou et al. [Probabilistic Bilevel Coreset Selection](https://proceedings.mlr.press/v162/zhou22h.html). *ICML*, 2022.

<a id="app-21"></a>
### 21. Autonomous scientific discovery and AI Scientist systems

**Model insight.** An outer process designs or revises a scientific objective; an inner process searches for hypotheses or scientific designs under that objective. The manuscript normalizes these roles as a bilevel model. Ma et al. explicitly describe an LLM–simulation bilevel framework; SAGA uses goal-evolving agents and an inner optimizer. This architectural correspondence does not establish smoothness, differentiability, convergence, or global optimality for the entire agentic process.

**Relationship:** Equivalent formulation. · [Formulation](docs/modeling-guide.md#app-21)

- Pingchuan Ma et al. [LLM and Simulation as Bilevel Optimizers: A New Paradigm to Advance Physical Scientific Discovery](https://proceedings.mlr.press/v235/ma24m.html). *ICML*, 2024.
- Yuanqi Du et al. [Accelerating Scientific Discovery with Autonomous Goal-evolving Agents](https://arxiv.org/abs/2512.21782). *arXiv preprint*, 2025. **SAGA**.

<a id="app-22"></a>
### 22. Diffusion-model hyperparameter and noise-schedule optimization

**Model insight.** Choose diffusion hyperparameters or a feasible noise schedule at the outer level using generation quality or a validation surrogate. The inner problem represents diffusion training or the generative inference process. Stochastic first-order bilevel estimators reduce differentiation cost, while the chosen quality surrogate and inner approximation determine what is actually optimized.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-22)

- Quan Xiao et al. [A First-order Generative Bilevel Optimization Framework for Diffusion Models](https://proceedings.mlr.press/v267/xiao25i.html). *ICML*, 2025.

## Multi-Objective Optimization

Multi-objective models preserve a vector of losses and compare solutions through Pareto dominance. A first-order stationarity condition is weaker than global Pareto optimality.

<a id="app-23"></a>
### 23. Multi-task learning

**Model insight.** Optimize shared and task-specific parameters against several task losses. A small convex QP finds a minimum-norm convex combination of task gradients using nonnegative weights that sum to one. A nonzero solution supplies a common descent direction; zero indicates Pareto stationarity under the relevant assumptions. Preference-aware formulations address which trade-off is desired.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-23)

- Ozan Sener and Vladlen Koltun. [Multi-Task Learning as Multi-Objective Optimization](https://proceedings.neurips.cc/paper/2018/hash/432aca3a1e345e339f35a30c8f65edce-Abstract.html). *NeurIPS*, 2018.
- Michinari Momma, Chaosheng Dong, and Jia Liu. [A Multi-objective / Multi-task Learning Framework Induced by Pareto Stationarity](https://proceedings.mlr.press/v162/momma22a.html). *ICML*, 2022.

## Inverse Optimization

Inverse optimization infers objectives or other hidden components that rationalize observed decisions. Its central difficulty is often identifiability: several different models may explain the same behavior.

<a id="app-24"></a>
### 24. Inverse reinforcement learning

**Model insight.** Infer reward parameters so that a demonstrated policy is optimal or nearly optimal. The manuscript uses Bellman equalities for the expert policy, inequalities against alternative actions, and slack penalties in a normalized soft-margin QP. Reward regularization addresses ambiguity. Generalized inverse optimization and generalized inverse reinforcement learning broaden the setting beyond this known-dynamics reward model.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-24)

This label concerns the inverse-optimality approach; the displayed soft-margin model is a normalization, not a common verbatim formulation of every paper below.

- Andrew Y. Ng and Stuart J. Russell. [Algorithms for Inverse Reinforcement Learning](https://ai.stanford.edu/~ang/papers/icml00-irl.pdf). *ICML*, 2000. Primary IRL anchor.
- Chaosheng Dong, Yiran Chen, and Bo Zeng. [Generalized Inverse Optimization through Online Learning](https://proceedings.neurips.cc/paper_files/paper/2018/hash/28dd2c7955ce926456240b2ff0100bde-Abstract.html). *NeurIPS*, 2018. Related inverse-optimization background.
- Chaosheng Dong and Yijia Wang. [Towards Generalized Inverse Reinforcement Learning](https://arxiv.org/abs/2402.07246). *arXiv preprint*, 2024.

## Distributionally Robust Optimization

Distributionally robust optimization (DRO) minimizes worst-case expected loss over an ambiguity set of probability distributions around an empirical law. Both the geometry and radius of that set determine which shifts are covered.

<a id="app-25"></a>
### 25. Contrastive learning as DRO

**Model insight.** Treat the negative-sampling law as an adversarial distribution within a divergence-based ambiguity set. The encoder then minimizes a robust contrastive loss, while the inner distribution emphasizes difficult negatives. The source connects contrastive objectives and temperature to distributional robustness; the interpretation depends on the specified negative distribution and ambiguity model.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-25)

- Junkang Wu et al. [Understanding Contrastive Learning via Distributionally Robust Optimization](https://proceedings.neurips.cc/paper_files/paper/2023/hash/48aaa5ea741ae8430bd58e25917d267d-Abstract-Conference.html). *NeurIPS*, 2023.

<a id="app-26"></a>
### 26. Distributionally robust DPO for LLM alignment

**Model insight.** Minimize worst-case direct preference optimization (DPO) loss over alternative preference distributions near the empirical data. Kullback–Leibler ambiguity permits adversarial reweighting; Wasserstein ambiguity uses a chosen transport geometry. Robustness protects against the represented distributional shifts and does not establish correctness of the underlying preference labels.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-26)

- Zaiyan Xu et al. [Robust LLM Alignment via Distributionally Robust Direct Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/272efd3a6091ceefcbc79f1f3a6fdba4-Abstract-Conference.html). *NeurIPS*, 2025.

## Submodular Optimization

A submodular set function has diminishing returns: adding an item gives no larger marginal benefit when the selected set is larger. For a normalized, monotone submodular objective under a cardinality constraint, standard greedy achieves a 1 − 1/e approximation. Other constraints, dynamic settings, and nonmonotone objectives require their own analysis.

<a id="app-27"></a>
### 27. Data subset selection and active learning

**Model insight.** Select a representative subset under a cardinality budget using a facility-location objective: each observation receives the similarity value of its best selected representative. Nonnegative similarities make this objective normalized, monotone, and submodular. Active learning can first filter for uncertainty and then select a diverse batch. The approximation guarantee concerns the set function, not downstream test accuracy.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-27)

- Kai Wei, Rishabh Iyer, and Jeff Bilmes. [Submodularity in Data Subset Selection and Active Learning](https://proceedings.mlr.press/v37/wei15.html). *ICML*, 2015.

<a id="app-28"></a>
### 28. Document summarization

**Model insight.** Choose sentences to maximize capped concept coverage and a concave topic-diversity reward within a word budget. With nonnegative inputs, these terms give a monotone submodular objective. Sentence length creates a knapsack constraint, so a cardinality-only greedy guarantee cannot be applied unchanged. The objective scores content selection; it does not ensure discourse coherence.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-28)

- Hui Lin and Jeff Bilmes. [A Class of Submodular Functions for Document Summarization](https://aclanthology.org/P11-1052/). *ACL*, 2011.

<a id="app-29"></a>
### 29. KV-cache eviction for LLM inference

**Model insight.** Retain an evolving token set under a fixed key–value (KV) cache budget. H2O combines accumulated attention-derived heavy hitters with a protected recent window, using dynamic submodular reasoning for eviction. The feasible candidates are the current cache plus the arriving token; scores change as generation proceeds. A modular one-step score is a special case, but static top-k selection omits the evolving state and recency constraints.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-29)

- Zhenyu Zhang et al. [H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html). *NeurIPS*, 2023.

<a id="minmax-and-saddle-point-optimization"></a>
## Min–Max and Saddle-Point Optimization

Min–max formulations model opposing objectives. Convex–concave games have useful saddle-point theory, whereas neural parameterizations generally fall outside those conditions.

<a id="app-30"></a>
### 30. Generative adversarial networks

**Model insight.** A generator minimizes the canonical adversarial value while a discriminator maximizes its log-likelihood of distinguishing real and generated samples. In the ideal unrestricted game, matching the data distribution yields an uninformative discriminator. Finite neural models create a nonconvex–nonconcave game, and alternating stochastic updates can cycle or collapse modes rather than reach a global equilibrium.

**Relationship:** Explicit formulation. · [Formulation](docs/modeling-guide.md#app-30)

- Ian J. Goodfellow et al. [Generative Adversarial Nets](https://proceedings.neurips.cc/paper_files/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html). *NIPS*, 2014.

## Research challenges

The manuscript identifies several questions that connect the ten paradigms:

- **Uncertainty in learned coefficients.** How should uncertainty in relevance, cost, similarity, and response estimates enter an optimization model without making it excessively conservative?
- **Differentiation through approximate decisions.** How can learning use discrete solvers, greedy selections, and truncated inner training while accounting for bias, memory, and feasibility?
- **Scalable certificates.** When can decomposition, screening, and learned heuristics deliver useful bounds at the scale of information-access systems?
- **Dynamic objectives and constraints.** What guarantees remain meaningful when actions change future data, preferences, or scientific goals?
- **Semantics of diversity and fairness.** How well do similarities, quotas, and coverage features correspond to the user outcomes they are meant to represent?
- **Auditability of agentic optimization.** How should revised objectives, constraint provenance, solver status, and approximation traces be recorded?
- **Formulation fidelity.** Can evaluations distinguish coefficient error, candidate-generation loss, relaxation gap, optimization gap, and execution drift?

See the manuscript's cross-paradigm discussion and the [modeling guide](docs/modeling-guide.md) for the distinction between a feasible decision, an approximation guarantee, a stationary point, and a global optimality certificate.

## Contributing

Corrections, clearer modeling explanations, verified bibliographic updates, and better primary-source links are welcome. Please follow [CONTRIBUTING.md](CONTRIBUTING.md), identify the relevant application number, and explain whether the proposed change affects its formulation or relationship label. The catalog currently tracks the manuscript's 30 application units; additions within an existing unit should preserve that scope and its source provenance.

## Citation

If this repository supports your work, please cite the paper:

> Chaosheng Dong. *Mathematical Programming in Machine Learning and Artificial Intelligence: A Unified Taxonomy of Models and Applications.* arXiv:2609.07254, 2026. [Paper on arXiv](https://arxiv.org/abs/2609.07254).

```bibtex
@misc{dong2026mathematicalprogramming,
  author        = {Dong, Chaosheng},
  title         = {Mathematical Programming in Machine Learning and Artificial Intelligence: A Unified Taxonomy of Models and Applications},
  year          = {2026},
  eprint        = {2609.07254},
  archivePrefix = {arXiv},
  primaryClass  = {math.OC},
  url           = {https://arxiv.org/abs/2609.07254}
}
```

Please also cite the original papers for the individual methods or formulations you use. Their records are collected in the [application and reference catalog](data/applications.json).

## Acknowledgment

The organization of this companion repository was inspired by [rishieraj/awesome-multimodal-agents](https://github.com/rishieraj/awesome-multimodal-agents). Its literature summaries and taxonomy are grounded in the accompanying mathematical-programming manuscript.
