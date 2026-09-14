# Modeling guide: 30 applications of mathematical programming in ML and AI

This guide condenses the formulations in the companion [paper on arXiv](https://arxiv.org/abs/2609.07254). Its 30 numbered applications follow the paper's taxonomy; it is a reading guide, not an implementation or a claim that every cited system uses a general-purpose solver. Bibliographic details live in the [application and reference catalog](../data/applications.json).

The relationship labels distinguish **Explicit formulation** (the source uses the paradigm), **Equivalent formulation** (an exact representation of a source objective), and **Natural MP reformulation** (the survey's modeling abstraction). An explicit paradigm does not make every normalized equation a verbatim source formulation. Where the current manuscript's label is broader than its equation warrants, a fidelity note makes that distinction visible.

## Shared notation

| Symbol | Meaning |
| --- | --- |
| $i,j;q;g;k;\tau$ | Items/samples; query; group; option/cluster/expert; time |
| $\mathcal I,\mathcal J,\mathcal G,\mathcal K,\mathcal Q$ | Corresponding finite index sets |
| $\mathbf a_i,y_i$ | Observed features and label/response |
| $\mathbf A,\mathbf b,\mathbf y$ | Known matrix, right-hand side, response vector |
| $\theta\in\Theta$ | Learned parameters and their feasible set |
| $\lambda$ | Hyperparameters or nonnegative trade-off weight; $\Lambda$ is its feasible set |
| $\mathbf x$ | Continuous decision or latent state |
| $z_i,z_{ik}\in\{0,1\}$ | Selection and assignment decisions, except explicitly relaxed flow variables |
| $w_i,w_{ij}$ | Continuous weights |
| $r_i,c_i,s_{ij}$ | Utility, nonnegative resource cost, pairwise similarity |
| $B,m$ | Resource budget and cardinality limit |
| $S\subseteq\mathcal V$ | Selected subset of a finite ground set |
| $L_{\mathrm{tr}},L_{\mathrm{val}},\Phi,\Psi$ | Training, validation, upper-level, and lower-level objectives |
| $\widehat P,Q,\mathcal U(\widehat P)$ | Empirical law, alternative law, and ambiguity set |
| $F$ | Set function; submodularity is stated where required |

Vectors and matrices use bold symbols where practical; parameters retain the paper's $\theta,\lambda$ convention. All sums range over the indices indicated in the surrounding text. Domains and symbols that specialize this table are defined in each application.

## Linear programming

An LP has a linear objective and linear constraints. A discrete interpretation does not require integer variables when a totally unimodular network matrix supplies integrality.

<a id="app-01"></a>
### 01. Compressed sensing and basis pursuit

Given measurements $\mathbf b\in\mathbb R^p$ and sensing matrix $\mathbf A\in\mathbb R^{p\times d}$, $p<d$, recover a sparse signal $\mathbf x$. The auxiliary vector $\mathbf t$ bounds absolute values:

$$
\begin{aligned}
&\min_{\mathbf x\in\mathbb R^d}\|\mathbf x\|_1\quad\text{s.t. }\mathbf A\mathbf x=\mathbf b,\\
&\equiv\quad\min_{\mathbf x\in\mathbb R^d,\,\mathbf t\in\mathbb R_+^d}\sum_{j=1}^d t_j
\quad\text{s.t. }\mathbf A\mathbf x=\mathbf b,\ -t_j\le x_j\le t_j\quad(1\le j\le d).
\end{aligned}
$$

**LP; Equivalent formulation.** Minimization makes the absolute-value epigraph tight. LP optimality is distinct from sparse-signal recovery, which also needs assumptions on the sensing matrix. Interior-point and primal–dual methods solve the convex model; the equality constraint abstracts measurement noise.

[Donoho, IEEE TIT 2006](https://doi.org/10.1109/TIT.2006.871582)

### LP with Network-Flow Structure

<a id="app-02"></a>
#### 02. Min-cost network flow for multi-object tracking

Let $\mathcal E$ contain admissible forward-time detection transitions and $M$ be the specified track count. Costs $\gamma^{\mathrm{det}},\gamma^{\mathrm{tr}},\gamma^{\mathrm{in}},\gamma^{\mathrm{out}}$ score detection, transition, entry, and exit. Continuous variables $z_i,w_{ij},u_i,v_i\in[0,1]$ represent their flows:

$$
\begin{aligned}
\min\quad &\sum_i\gamma_i^{\mathrm{det}}z_i+\sum_{(i,j)\in\mathcal E}\gamma_{ij}^{\mathrm{tr}}w_{ij}
+\sum_i(\gamma_i^{\mathrm{in}}u_i+\gamma_i^{\mathrm{out}}v_i)\\
\text{s.t.}\quad &u_i+\sum_{j:(j,i)\in\mathcal E}w_{ji}=z_i=v_i+\sum_{j:(i,j)\in\mathcal E}w_{ij}\quad(i\in\mathcal I),\\
&\sum_i u_i=\sum_i v_i=M,\qquad 0\le z_i,u_i,v_i,w_{ij}\le1.
\end{aligned}
$$

**Network LP; Explicit formulation.** Node splitting exposes an incidence matrix; integral supplies and capacities guarantee an integral optimal extreme point. Conservation assembles trajectories and unit capacities prevent detection reuse. Network simplex or successive shortest paths exploit this structure; general non-network couplings can destroy integrality. Accuracy still depends on detections, transition arcs, and calibrated costs.

[Zhang, Li, and Nevatia, CVPR 2008](https://doi.org/10.1109/CVPR.2008.4587584)

## Quadratic programming

<a id="app-03"></a>
### 03. Local reconstruction weights in Locally Linear Embedding

For fixed observation $\mathbf a_i\in\mathbb R^d$ and neighborhood $\mathcal N_i\subseteq\mathcal I\setminus\{i\}$, choose real reconstruction weights:

$$
\begin{aligned}
\min_{w_{ij}\in\mathbb R}\quad &\left\|\mathbf a_i-\sum_{j\in\mathcal I}w_{ij}\mathbf a_j\right\|_2^2\\
\text{s.t.}\quad &\sum_{j\in\mathcal I}w_{ij}=1,\qquad w_{ij}=0\quad(j\notin\mathcal N_i).
\end{aligned}
$$

**Convex QP; Explicit formulation.** The affine constraint gives translation invariance, not nonnegativity. Each observation has an independent small QP with positive-semidefinite curvature. Linear-system solves and diagonal regularization handle singular local covariance. Neighborhood quality and the later embedding stage remain outside this local optimization.

[Roweis and Saul, Science 2000](https://doi.org/10.1126/science.290.5500.2323)

## Binary and mixed-integer programming

BIP denotes a binary integer program; MILP adds continuous variables to a linear integer model; BQP has binary quadratic terms. MIQP usually means a quadratic objective with linear constraints; a model with quadratic constraints is more precisely MIQCP. Branch-and-bound certificates, relaxation bounds, and heuristic incumbents should be reported separately.

<a id="app-04"></a>
### 04. RAG context selection under a token budget

For a fixed query, $\mathcal I_g$ are passage alternatives in semantic group $g$. Utilities $r_i$ estimate relevance/faithfulness; $c_{ih}$ and $B_h$ are consumption and budget for resource $h\in\mathcal H$, including tokens:

$$
\begin{aligned}
\max_{z_i\in\{0,1\}}\quad &\sum_{g\in\mathcal G}\sum_{i\in\mathcal I_g}r_i z_i\\
\text{s.t.}\quad &\sum_g\sum_{i\in\mathcal I_g}c_{ih}z_i\le B_h\quad(h\in\mathcal H),\\
&\sum_{i\in\mathcal I_g}z_i\le1\quad(g\in\mathcal G).
\end{aligned}
$$

**BIP/MMKP; Explicit formulation.** Multiple-choice rows limit redundant alternatives; mandatory groups can use equality. Pareto-pruned dynamic programming or MIP addresses the multidimensional multiple-choice knapsack problem. Additive utilities omit evidence interactions and passage ordering. The bibliography records an arXiv preprint, without asserting unverified ACL proceedings metadata.

[Xu et al., 2026](https://arxiv.org/abs/2604.10734)

<a id="app-05"></a>
### 05. Mixture-of-experts routing

Token $i$ has expert affinity $r_{ik}$, prescribed multiplicity $h_i$, and expert $k$ has capacity $C_k$:

$$
\begin{aligned}
\max_{z_{ik}\in\{0,1\}}\quad &\sum_{i\in\mathcal I}\sum_{k\in\mathcal K}r_{ik}z_{ik}\\
\text{s.t.}\quad &\sum_k z_{ik}=h_i\quad(i\in\mathcal I),\qquad
\sum_i z_{ik}\le C_k\quad(k\in\mathcal K).
\end{aligned}
$$

**BIP with an integral transportation relaxation; Natural MP reformulation.** Pure bipartite assignment admits exact min-cost flow for integral capacities. The cited expert-choice router instead fixes expert bucket sizes and permits variable experts per token: its token multiplicities are not prescribed $h_i$. Thus the displayed model is a capacity-aware abstraction, not an equivalent description of that router. Parallel sorting is inexpensive; global assignment omits communication and end-to-end learning effects.

[Zhou et al., NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/2f00ecd787b432c1d36f3de9800728eb-Abstract-Conference.html)

<a id="app-06"></a>
### 06. Tool or agent-component selection

Components have predicted utility $r_i$, cost $c_i$, conflicts $\mathcal E^-$, and dependencies $\mathcal D$; $(i,j)\in\mathcal D$ means $i$ requires $j$:

$$
\begin{aligned}
\max_{z_i\in\{0,1\}}\quad &\sum_i r_i z_i\\
\text{s.t.}\quad &\sum_i c_i z_i\le B,\quad z_i+z_j\le1\quad(\{i,j\}\in\mathcal E^-),\\
&z_i\le z_j\quad((i,j)\in\mathcal D).
\end{aligned}
$$

**Knapsack-style BIP; Explicit formulation.** Budget, conflict, and prerequisite rows turn capability estimates into a feasible component set. Exact MIP or online knapsack policies can be used; additive utility abstracts component complementarity and execution order. The guide retains the manuscript's deterministic normalization of the cited composition problem.

[Yuan et al., NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/39c51d0fe64c273413a4d358361b3daa-Abstract-Conference.html)

<a id="app-07"></a>
### 07. Notification/email allocation and frequency optimization

Users $i$, messages $j$, and eligible times $\tau$ have send utility $r_{ij\tau}$ and cost $c_{ij\tau}$. Channel $h(j)$, user caps $f_i,f_{ih}$, and campaign bounds $L_j,U_j$ are known:

$$
\begin{aligned}
\max_{z_{ij\tau}\in\{0,1\}}\quad &\sum_{i,j,\tau}r_{ij\tau}z_{ij\tau}\\
\text{s.t.}\quad &\sum_{j,\tau}z_{ij\tau}\le f_i\quad(i\in\mathcal I),\\
&\sum_{j:h(j)=h}\sum_\tau z_{ij\tau}\le f_{ih}\quad(i\in\mathcal I,h\in\mathcal H),\\
&L_j\le\sum_{i,\tau}z_{ij\tau}\le U_j\quad(j\in\mathcal J),\qquad
\sum_{i,j,\tau}c_{ij\tau}z_{ij\tau}\le B.
\end{aligned}
$$

**BIP; Natural MP reformulation.** Dual prices decompose many user decisions once shared quotas and budgets are relaxed. The sources describe Pinterest volume control and a separate industrial knapsack system; neither is asserted to solve this generalized user–message–time program verbatim. Fatigue, causal carryover, and uncertainty in long-term value are abstracted.

[Zhao et al., KDD 2018](https://doi.org/10.1145/3219819.3219906) · [Zhang et al., WWW 2020](https://doi.org/10.1145/3366423.3380084)

<a id="app-08"></a>
### 08. Test-time reasoning and exploration-budget allocation

For each query $q$, choose one compute level $k\in\mathcal K_q$, whose estimated success utility and cost are $r_{qk},c_{qk}$:

$$
\begin{aligned}
\max_{z_{qk}\in\{0,1\}}\quad &\sum_{q\in\mathcal Q}\sum_{k\in\mathcal K_q}r_{qk}z_{qk}\\
\text{s.t.}\quad &\sum_{k\in\mathcal K_q}z_{qk}=1\quad(q\in\mathcal Q),\qquad
\sum_q\sum_{k\in\mathcal K_q}c_{qk}z_{qk}\le B.
\end{aligned}
$$

**Multiple-choice knapsack BIP; Natural MP reformulation.** A shared compute budget couples query decisions. Dynamic programming, pricing, or MIP can optimize calibrated level curves. Snell et al. motivate difficulty-adaptive compute; they are not credited with this across-query BIP. Discrete levels abstract interruptible search, verifier errors, and correlated samples.

[Snell et al., ICLR 2025](https://openreview.net/forum?id=4FWaWZtd2n)

<a id="app-09"></a>
### 09. Optimal decision-tree construction

The template has branch nodes $\mathcal B$, candidate leaves $\mathcal L$, classes $\mathcal C$, and left/right ancestor sets $\mathcal A_l^L,\mathcal A_l^R$. Binary $d_t,p_{jt},z_{il},u_l,q_{lc},e_i$ respectively activate a split, select its feature, assign a sample, activate a leaf, choose its class, and record error. Real $b_t$ is a threshold; $U_t,M_t$ are valid bounds, $\varepsilon>0$ is a separation tolerance:

$$
\begin{aligned}
\min\quad &\sum_i e_i+\lambda\sum_{t\in\mathcal B}d_t\\
\text{s.t.}\quad &\sum_{j=1}^d p_{jt}=d_t,\quad 0\le b_t\le U_t d_t\quad(t\in\mathcal B),\\
&\sum_l z_{il}=1\quad(i\in\mathcal I),\quad \sum_{c\in\mathcal C}q_{lc}=u_l,\quad z_{il}\le u_l\quad(i,l),\\
&z_{il}\le d_t\quad(i,l,t\in\mathcal A_l^L\cup\mathcal A_l^R),\\
&\sum_j a_{ij}p_{jt}\le b_t+M_t(1-z_{il})\quad(i,l,t\in\mathcal A_l^L),\\
&\sum_j a_{ij}p_{jt}\ge b_t+\varepsilon-M_t(1-z_{il})\quad(i,l,t\in\mathcal A_l^R),\\
&e_i\ge z_{il}-q_{l,y_i}\quad(i,l),\qquad d_t,p_{jt},z_{il},u_l,q_{lc},e_i\in\{0,1\}.
\end{aligned}
$$

**MILP; Explicit formulation.** Path rows enforce routing; leaf predictions and error variables measure classification loss. Feature scaling must justify nonnegative thresholds and big-$M$ constants. **Template caveat:** this is the paper's compact display, which explicitly omits hierarchy constraints. An executable prunable-tree model additionally needs consistent terminal-node eligibility, ancestor activation, and exclusion of simultaneous ancestor/descendant leaves. Branch-and-cut and greedy warm starts can certify gaps for moderate problems; this display alone is not a complete implementation specification.

[Bertsimas and Dunn, Machine Learning 2017](https://doi.org/10.1007/s10994-017-5633-9)

<a id="app-10"></a>
### 10. Best subset selection

For design $\mathbf A\in\mathbb R^{n\times d}$ and response $\mathbf y\in\mathbb R^n$, select at most $m$ coefficients using valid bounds $M_j>0$:

$$
\begin{aligned}
\min_{\theta\in\mathbb R^d,\,\mathbf z\in\{0,1\}^d}\quad &\tfrac12\|\mathbf y-\mathbf A\theta\|_2^2\\
\text{s.t.}\quad &-M_jz_j\le\theta_j\le M_jz_j\quad(1\le j\le d),\qquad \sum_j z_j\le m.
\end{aligned}
$$

**Convex MIQP; Explicit formulation.** The quadratic continuous objective is convex; binary support choices remain combinatorial. Linking rows zero unselected coefficients. Tight bounds, indicator/perspective formulations, screening, and sparse warm starts improve branch-and-bound. Collinearity and post-selection uncertainty remain statistical concerns even after global optimization.

[Bertsimas, King, and Mazumder, Annals of Statistics 2016](https://doi.org/10.1214/15-AOS1388)

<a id="app-11"></a>
### 11. Constrained maximum-inner-product retrieval

Query embedding $\mathbf v_q$ and item embedding $\mathbf a_i$ give $r_i=\langle\mathbf v_q,\mathbf a_i\rangle$. Matrix $\mathbf C$ and bounds $\mathbf l,\mathbf u$ encode categories, coverage, or fairness; $s_{ij}\ge0$ penalizes redundancy:

$$
\begin{aligned}
\max_{\mathbf z\in\{0,1\}^{|\mathcal I|}}\quad
&\sum_i r_i z_i-\lambda\sum_{i<j}s_{ij}z_i z_j\\
\text{s.t.}\quad &\sum_i z_i=m,\qquad \mathbf l\le\mathbf C\mathbf z\le\mathbf u.
\end{aligned}
$$

**BIP/MILP when $\lambda=0$; BQP/MIQP when pairwise penalties are retained; Natural MP reformulation.** These are two variants of one application. Pair products admit exact MILP linearization. The cited categorical-diversity search algorithm supports the retrieval motivation, not a claim that it solves these general fairness/pairwise programs. Candidate pruning, approximate indexing, and local search introduce losses separate from any solver gap.

[Hirata et al., IEEE Access 2023](https://doi.org/10.1109/ACCESS.2023.3234072)

<a id="app-12"></a>
### 12. Mixed-precision neural-network quantization

Layer $i$ can use bit-width option $k\in\mathcal K_i$. Loss proxy $d_{ik}\ge0$ and measured resource consumption $c_{ikh}\ge0$ are known:

$$
\begin{aligned}
\min_{z_{ik}\in\{0,1\}}\quad &\sum_i\sum_{k\in\mathcal K_i}d_{ik}z_{ik}\\
\text{s.t.}\quad &\sum_{k\in\mathcal K_i}z_{ik}=1\quad(i\in\mathcal I),\qquad
\sum_i\sum_{k\in\mathcal K_i}c_{ikh}z_{ik}\le B_h\quad(h\in\mathcal H).
\end{aligned}
$$

**BIP/ILP; Explicit formulation.** Exactly-one rows choose layer precision; resource rows impose size or latency limits. HAWQ-V3 uses Hessian-based perturbation and hardware-aware integer optimization. MIP, dynamic programming, and dual pricing exploit separability. Static sensitivity proxies and additive latency can miss cross-layer or kernel effects.

[Yao et al., ICML 2021](https://proceedings.mlr.press/v139/yao21a.html)

<a id="app-13"></a>
### 13. Diversity-aware recommendation

For a user, relevance $r_i$, similarity $s_{ij}\ge0$, and optional feasibility matrix/bound $\mathbf C,\mathbf u$ determine the list:

$$
\begin{aligned}
\max_{\mathbf z\in\{0,1\}^{|\mathcal I|}}\quad &\sum_i r_i z_i-\lambda\sum_{i<j}s_{ij}z_i z_j\\
\text{s.t.}\quad &\sum_i z_i=m,\qquad \mathbf C\mathbf z\le\mathbf u.
\end{aligned}
$$

**BQP/MIQP; Natural MP reformulation.** Similar co-selected pairs incur a penalty; relevance is additive. Exact product linearization yields a potentially large MILP, while marginal-gain selection and local swaps trade certificates for speed. The source motivates accuracy–diversity optimization, without being credited with this precise solver model. Pairwise diversity does not encode user-specific novelty, position, or exposure effects.

[Zhang and Hurley, RecSys 2008](https://doi.org/10.1145/1454008.1454030)

<a id="app-14"></a>
### 14. Globally optimized $k$-means clustering

Given $\mathbf a_i\in\mathbb R^d$ and $K$ clusters, let $\mathbf\mu_k$ be centroids and $t_{ik}\ge0$ charged assignment costs. Make the manuscript's assumed bounded centroid domain explicit as $\mathcal M$; choose $M_{ik}\ge\max_{\mathbf\mu\in\mathcal M}\|\mathbf a_i-\mathbf\mu\|_2^2$:

$$
\begin{aligned}
\min_{\mathbf z,\mathbf\mu,\mathbf t}\quad &\sum_i\sum_{k=1}^K t_{ik}\\
\text{s.t.}\quad &\sum_{k=1}^K z_{ik}=1\quad(i\in\mathcal I),\quad \sum_i z_{ik}\ge1\quad(1\le k\le K),\\
&t_{ik}\ge\|\mathbf a_i-\mathbf\mu_k\|_2^2-M_{ik}(1-z_{ik})\quad(i,k),\\
&z_{ik}\in\{0,1\},\quad t_{ik}\ge0,\quad\mathbf\mu_k\in\mathcal M.
\end{aligned}
$$

**Mixed-integer convex quadratically constrained model; Explicit formulation family.** Take $\mathcal M$ to be a bounded convex set containing all data and their means. The model then charges exactly the chosen squared distances at optimum. Direct products $z_{ik}\|\mathbf a_i-\mathbf\mu_k\|_2^2$ instead give MINLP; alternative exact formulations can be MIQP or MILP. This is not simply BQP. Bounds and symmetry breaking help global methods; fixed $K$ and Euclidean geometry remain modeling assumptions.

[Burgard et al., JGO 2023](https://doi.org/10.1007/s10898-022-01267-4) · [Ágoston and Eisenberg-Nagy, CEJOR 2024](https://doi.org/10.1007/s10100-023-00881-1)

<a id="app-15"></a>
### 15. Video frame or keyframe selection

Frames have query relevance $r_i$ and redundancy $s_{ij}\ge0$; $\mathcal E_\Delta$ contains pairs too close in time to retain together:

$$
\begin{aligned}
\max_{z_i\in\{0,1\}}\quad &\sum_i r_i z_i-\lambda\sum_{i<j}s_{ij}z_i z_j\\
\text{s.t.}\quad &\sum_i z_i\le m,\qquad z_i+z_j\le1\quad((i,j)\in\mathcal E_\Delta).
\end{aligned}
$$

**BQP/integer quadratic programming; Explicit formulation.** The cited work explicitly models relevance and diversity with integer quadratic selection, using a customized greedy alternative. Temporal constraints are optional in this normalized version. MIP after pruning or sparse pairwise local search reduces cost; selected still frames can miss action dynamics and narrative continuity.

[Fang et al., ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/675a31be2d051be53d57bced52c6631f-Abstract-Conference.html)

## Conic programming

<a id="app-16"></a>
### 16. Group Lasso as SOCP

Feature groups $\mathcal J_g$ partition coefficients $\boldsymbol\beta$, with group weights $\omega_g>0$. Introduce nonnegative epigraphs $u,v,t_g$ and rotated cone $\mathcal Q_r^3=\{(a,b,c):a,b\ge0,\ 2ab\ge c^2\}$:

$$
\begin{aligned}
&\min_{\boldsymbol\beta\in\mathbb R^d}\tfrac12\|\mathbf y-\mathbf A\boldsymbol\beta\|_2^2+\lambda\sum_g\omega_g\|\boldsymbol\beta_g\|_2\\
&\equiv\quad\min_{\boldsymbol\beta\in\mathbb R^d,\,u,v\ge0,\,\mathbf t\in\mathbb R_+^{|\mathcal G|}}\ v+\lambda\sum_g\omega_g t_g\\
&\text{s.t. }\|\mathbf y-\mathbf A\boldsymbol\beta\|_2\le u,\quad
\|\boldsymbol\beta_g\|_2\le t_g\quad(g\in\mathcal G),\quad(v,1,u)\in\mathcal Q_r^3.
\end{aligned}
$$

Here $\boldsymbol\beta$ is unrestricted; only epigraph variables are nonnegative. **SOCP; Equivalent formulation.** The rotated cone enforces $v\ge u^2/2$, so the optimum equals the Group Lasso objective. Conic solvers and proximal/block methods exploit convexity. Group design, shrinkage, and correlated predictors affect the statistical result.

[Yuan and Lin, JRSS-B 2006](https://doi.org/10.1111/j.1467-9868.2005.00532.x)

<a id="app-17"></a>
### 17. Sparse PCA as SDP

Let $\boldsymbol\Sigma\succeq0$ be a covariance matrix and $\kappa>0$ a sparsity-surrogate budget. Lift a loading $\mathbf v$ to $\mathbf X=\mathbf v\mathbf v^\top$:

$$
\begin{aligned}
\max_{\mathbf X}\quad &\langle\boldsymbol\Sigma,\mathbf X\rangle\\
\text{s.t.}\quad &\operatorname{tr}(\mathbf X)=1,\quad
\|\mathbf X\|_1:=\sum_{i,j}|X_{ij}|\le\kappa,\quad\mathbf X\succeq0,\\
&\operatorname{rank}(\mathbf X)=1\quad\text{in the rank-one model; omit this row for the SDP relaxation.}
\end{aligned}
$$

**SDP relaxation; Explicit formulation.** The $\ell_1$ budget is a sparsity surrogate, not an exact support-cardinality constraint. Removing rank one supplies an upper variance bound; a higher-rank optimum does not directly give an exact sparse loading. Spectral first-order methods and rounding address scale and recovery, but the lift needs quadratic storage.

[d’Aspremont et al., NeurIPS 2004](https://proceedings.neurips.cc/paper/2628-a-direct-formulation-for-sparse-pca-using-semidefinite-programming)

## Bilevel programming

An outer decision is evaluated through an inner optimized response. Nonunique inner minimizers need a selection convention; finite training and approximate hypergradients generally do not solve the exact global bilevel problem.

<a id="app-18"></a>
### 18. Hyperparameter optimization

Training and validation data define distinct losses; choose $\lambda\in\Lambda$ after accounting for the trained response $\theta^\star(\lambda)$:

$$
\min_{\lambda\in\Lambda}L_{\mathrm{val}}(\theta^\star(\lambda),\lambda)
\quad\text{s.t.}\quad
\theta^\star(\lambda)\in\arg\min_{\theta\in\Theta}L_{\mathrm{tr}}(\theta,\lambda).
$$

**Bilevel; Explicit formulation.** Validation measures the downstream consequence of training with the proposed hyperparameters. Unrolling and implicit differentiation provide hypergradients under different computational/regularity assumptions. Truncation changes the optimized response; repeated validation reuse can overfit.

[Franceschi et al., ICML 2018](https://proceedings.mlr.press/v80/franceschi18a.html)

<a id="app-19"></a>
### 19. Neural architecture search

For search-graph edge $e$, $\lambda_{ek}$ mixes operations $k\in\mathcal K_e$; $\theta$ contains network weights:

$$
\begin{aligned}
\min_{\lambda}\quad &L_{\mathrm{val}}(\theta^\star(\lambda),\lambda)\\
\text{s.t.}\quad &\theta^\star(\lambda)\in\arg\min_{\theta\in\Theta}L_{\mathrm{tr}}(\theta,\lambda),\\
&\lambda_{ek}\ge0,\quad\sum_{k\in\mathcal K_e}\lambda_{ek}=1\quad\text{for each edge }e.
\end{aligned}
$$

**Nonconvex bilevel with continuous architecture relaxation; Explicit formulation.** The simplex represents soft operation mixtures (DARTS parameterizes them with softmax logits). Alternating updates or truncated unrolling reduce cost. Discretizing and retraining can change performance, so the relaxed optimum is not an exact certificate for the final architecture.

[Liu, Simonyan, and Yang, ICLR 2019](https://openreview.net/forum?id=S1eYHoC5FX)

<a id="app-20"></a>
### 20. Coreset selection and data subsampling

For sample losses $\ell_i(\theta)$, the manuscript's continuous weights $w_i\in[0,1]$ limit total selected mass:

$$
\begin{aligned}
\min_{\mathbf w\in[0,1]^{|\mathcal I|}}\quad &L_{\mathrm{val}}(\theta^\star(\mathbf w))\\
\text{s.t.}\quad &\theta^\star(\mathbf w)\in\arg\min_{\theta\in\Theta}
\frac{\sum_i w_i\ell_i(\theta)}{\sum_i w_i},\qquad 0<\sum_i w_i\le m.
\end{aligned}
$$

**Bilevel; Explicit formulation at the paradigm level.** This display is deterministic weighted-risk training. Interpreting $w_i$ as sampling probabilities gives an expected-size constraint, but training on expected weights is generally not equivalent to averaging validation loss after training on sampled subsets. The source's probabilistic subset objective and policy-gradient method preserve that stochastic distinction. Binary weights yield an exact subset variant; continuous weighted training is a useful surrogate, with rounding and validation dependence remaining limitations.

[Zhou et al., ICML 2022](https://proceedings.mlr.press/v162/zhou22h.html)

<a id="app-21"></a>
### 21. Autonomous scientific discovery and AI Scientist systems

Let $\lambda\in\Lambda$ encode a scientific criterion, $\mathbf x\in\mathcal X$ a hypothesis/design, $\Psi$ a criterion-guided search objective, and $\Phi$ an external scientific evaluation:

$$
\min_{\lambda\in\Lambda}\Phi(\lambda,\mathbf x^\star(\lambda))
\quad\text{s.t.}\quad
\mathbf x^\star(\lambda)\in\arg\min_{\mathbf x\in\mathcal X}\Psi(\mathbf x,\lambda).
$$

**Bilevel architectural abstraction.** The manuscript labels this **Equivalent formulation**, but calls the equation normative and disclaims equivalence to conventional differentiable bilevel optimization. Read its label as architectural normalization, not a mathematical equivalence theorem. Ma et al. explicitly use an LLM–simulation bilevel framework; SAGA evolves goals through an agentic outer process. Propose–simulate–analyze loops need not optimize a fixed smooth $\Phi$, solve inner argmins globally, or converge. Scientific validity and simulator fidelity require evidence beyond an optimizer's status.

[Ma et al., ICML 2024](https://proceedings.mlr.press/v235/ma24m.html) · [Du et al., SAGA 2025](https://arxiv.org/abs/2512.21782)

<a id="app-22"></a>
### 22. Diffusion-model hyperparameter and noise-schedule optimization

Schedule $\lambda\in\Lambda$ produces noisy state $\mathbf x_\tau(\mathbf a,\boldsymbol\epsilon;\lambda)$ from clean data $\mathbf a\sim P_{\mathrm{data}}$, noise $\boldsymbol\epsilon\sim P_\epsilon$, and sampled diffusion step $\tau$. Denoiser $\boldsymbol\epsilon_\theta$ is trained before evaluating generation loss $L_{\mathrm{gen}}$:

$$
\begin{aligned}
\min_{\lambda\in\Lambda}\quad &L_{\mathrm{gen}}(\theta^\star(\lambda),\lambda)\\
\text{s.t.}\quad &\theta^\star(\lambda)\in\arg\min_{\theta\in\Theta}
\mathbb E_{\mathbf a,\tau,\boldsymbol\epsilon}
\left\|\boldsymbol\epsilon-\boldsymbol\epsilon_\theta(\mathbf x_\tau(\mathbf a,\boldsymbol\epsilon;\lambda),\tau)\right\|_2^2.
\end{aligned}
$$

**Stochastic generative bilevel; Explicit formulation.** The outer loss assesses quality after the inner generative process. The expectation includes a specified training distribution over diffusion times. First-order estimators and truncated dynamics control cost; an inference-only variant changes the inner response. Finite training, noisy quality metrics, and sampler-specific schedules limit guarantees.

[Xiao et al., ICML 2025](https://proceedings.mlr.press/v267/xiao25i.html)

## Multi-objective optimization

<a id="app-23"></a>
### 23. Multi-task learning

Task losses $L_t(\theta)$, $1\le t\le T$, share parameters. At the current iterate, $\mathbf g_t=\nabla_\theta L_t(\theta)$; simplex weights $\alpha_t$ form a minimum-norm gradient combination:

$$
\begin{aligned}
&\min_{\theta\in\Theta}\bigl(L_1(\theta),\ldots,L_T(\theta)\bigr),\\
&\min_{\boldsymbol\alpha\in\mathbb R^T}\tfrac12\left\|\sum_{t=1}^T\alpha_t\mathbf g_t\right\|_2^2
\quad\text{s.t. }\alpha_t\ge0,\quad\sum_{t=1}^T\alpha_t=1.
\end{aligned}
$$

**Multi-objective with a convex QP subproblem; Explicit formulation.** A nonzero minimum-norm combination gives a common descent direction after negation; zero supplies first-order Pareto stationarity for unconstrained parameters (constrained domains require feasible-direction conditions). It is not global Pareto optimality for neural losses. Gradient approximations and scalarization improve practicality but affect trade-offs; one run need not find the entire Pareto front.

[Sener and Koltun, NeurIPS 2018](https://proceedings.neurips.cc/paper/2018/hash/432aca3a1e345e339f35a30c8f65edce-Abstract.html)

## Inverse optimization

<a id="app-24"></a>
### 24. Inverse reinforcement learning

Known finite dynamics $P(s'\mid s,a)$, discount $\gamma\in[0,1)$, expert policy $\pi_E$, and reward features $\boldsymbol\phi(s,a)$ define $r_\theta(s,a)=\theta^\top\boldsymbol\phi(s,a)$. Let $V_s\in\mathbb R$ be values, $\xi_{sa}\ge0$ slacks, $C>0$, and $(\mathcal P_aV)_s=\sum_{s'}P(s'\mid s,a)V_{s'}$:

$$
\begin{aligned}
\min_{\theta,V,\xi}\quad &\tfrac12\|\theta\|_2^2+C\sum_s\sum_{a\ne\pi_E(s)}\xi_{sa}\\
\text{s.t.}\quad &V_s=r_\theta(s,\pi_E(s))+\gamma(\mathcal P_{\pi_E(s)}V)_s\quad(s),\\
&V_s\ge r_\theta(s,a)+\gamma(\mathcal P_aV)_s+1-\xi_{sa}\quad(s,a\ne\pi_E(s)),\\
&\theta\in\mathbb R^d,\quad V_s\in\mathbb R,\quad\xi_{sa}\ge0.
\end{aligned}
$$

**Inverse optimization, here a convex QP; Explicit inverse-optimality formulation family.** Bellman equalities evaluate the expert; inequalities favor expert actions with a soft unit margin. This is the manuscript's regularized normalization, not a claim that the original paper presents this exact quadratic objective. LP/QP and constraint-generation methods apply to finite known dynamics. Reward nonidentifiability and imperfect demonstrations remain central limitations.

[Ng and Russell, ICML 2000](https://ai.stanford.edu/~ang/papers/icml00-irl.pdf)

## Distributionally robust optimization

DRO optimizes against probability laws in an ambiguity set. Divergence balls reweight empirical support; transport balls allow moves under a specified ground cost. These perturbations are modeling choices, not universal guarantees against distribution shift.

<a id="app-25"></a>
### 25. Contrastive learning as DRO

Encoder $f_\theta$ defines $s_\theta(\mathbf u,\mathbf v)=\langle f_\theta(\mathbf u),f_\theta(\mathbf v)\rangle$. Positive-pair law $\widehat P_+$ and negative law $\widehat P_-$ are empirical; temperature $\eta>0$, divergence $D_\varphi$, and radius $\rho\ge0$ define $\mathcal U_\varphi=\{Q:D_\varphi(Q\Vert\widehat P_-)\le\rho\}$:

$$
\min_{\theta\in\Theta}\mathbb E_{(\mathbf a,\mathbf a^+)\sim\widehat P_+}
\left[\max_{Q\in\mathcal U_\varphi}\mathbb E_{\mathbf a^-\sim Q}
\log\left(1+\exp\left(\frac{s_\theta(\mathbf a,\mathbf a^-)-s_\theta(\mathbf a,\mathbf a^+)}{\eta}\right)\right)\right].
$$

**DRO/min–max; Explicit formulation at the paradigm level.** The manuscript uses a robust pairwise logistic contrastive model to express uncertainty in negatives. It is not an assertion that every contrastive objective equals this particular surrogate. Fixed-loss distributional duality may be tractable; neural outer learning remains nonconvex. Adversarial reweighting can overemphasize false negatives, and finite batches alter the ambiguity estimate.

[Wu et al., NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/48aaa5ea741ae8430bd58e25917d267d-Abstract-Conference.html)

<a id="app-26"></a>
### 26. Distributionally robust DPO for LLM alignment

Preference example $\xi=(\mathbf a,y^+,y^-)$ contains a prompt and preferred/rejected responses. Policy $\pi_\theta$, fixed reference $\pi_{\mathrm{ref}}$, scale $\beta>0$, and logistic $\sigma(t)=(1+e^{-t})^{-1}$ define the DPO loss. Discrepancy $D$ and radius $\rho$ define the adversary:

$$
\begin{aligned}
\ell_{\mathrm{DPO}}(\theta;\xi)&=-\log\sigma\left(\beta\left[\log\frac{\pi_\theta(y^+\mid\mathbf a)}{\pi_{\mathrm{ref}}(y^+\mid\mathbf a)}-\log\frac{\pi_\theta(y^-\mid\mathbf a)}{\pi_{\mathrm{ref}}(y^-\mid\mathbf a)}\right]\right),\\
\min_{\theta\in\Theta}\ &\max_{Q:\,D(Q,\widehat P)\le\rho}\mathbb E_{\xi\sim Q}\ell_{\mathrm{DPO}}(\theta;\xi).
\end{aligned}
$$

**DRO; Explicit formulation.** The adversary emphasizes high-loss preferences under KL reweighting or moves mass under Wasserstein transport. Dual approximations and stochastic gradients address the nonconvex policy problem. Ambiguity geometry, ground cost, and preference-label quality determine which shifts are represented.

[Xu et al., NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/272efd3a6091ceefcbc79f1f3a6fdba4-Abstract-Conference.html)

## Submodular optimization

For $A\subseteq B\subseteq\mathcal V$ and $i\notin B$, diminishing returns means $F(A\cup\{i\})-F(A)\ge F(B\cup\{i\})-F(B)$. Normalization means $F(\varnothing)=0$; monotonicity means $F(A)\le F(B)$. Standard greedy achieves $1-1/e$ under a cardinality budget for normalized monotone submodular functions. Different constraints and dynamic problems require their own guarantees.

<a id="app-27"></a>
### 27. Data subset selection and active learning

Nonnegative similarities $s_{ij}$ measure how well representative $j$ covers datum $i$. Define the empty-set maximum as zero:

$$
\max_{S\subseteq\mathcal V} F(S):=\sum_{i\in\mathcal V}\max_{j\in S}s_{ij}
\quad\text{s.t.}\quad |S|\le m.
$$

**Monotone submodular maximization; Explicit formulation family.** Facility location credits each datum's best representative and has diminishing returns. In active learning, uncertainty filtering can precede the same set selection. Lazy or stochastic greedy scales marginal-gain evaluation; the cardinality greedy guarantee concerns $F$, not downstream accuracy or preservation of every rare class.

[Wei, Iyer, and Bilmes, ICML 2015](https://proceedings.mlr.press/v37/wei15.html)

<a id="app-28"></a>
### 28. Document summarization

Sentences $i$ have length $c_i$, concept coverage $a_{ig}\ge0$, and salience $r_i\ge0$. Concept weights $\omega_g\ge0$, topic partition $\mathcal V_k$, and $\lambda\ge0$ define coverage and diversity:

$$
\begin{aligned}
\max_{S\subseteq\mathcal V}\quad &F(S):=\sum_{g\in\mathcal G}\omega_g\min\left\{1,\sum_{i\in S}a_{ig}\right\}
+\lambda\sum_k\sqrt{\sum_{i\in S\cap\mathcal V_k}r_i}\\
\text{s.t.}\quad &\sum_{i\in S}c_i\le B.
\end{aligned}
$$

**Monotone submodular maximization with a knapsack constraint; Explicit formulation family.** Capped concept credit reduces redundancy; concave topic utility favors broader coverage. Budget-aware greedy with appropriate enumeration has guarantees under its assumptions; naive ratio greedy does not inherit the cardinality theorem automatically. Extractive set quality does not ensure sentence coherence or factual completeness.

[Lin and Bilmes, ACL 2011](https://aclanthology.org/P11-1052/)

<a id="app-29"></a>
### 29. KV-cache eviction for LLM inference

At time $\tau$, candidates are $G_\tau=S_{\tau-1}\cup\{\tau\}$. Accumulated attention scores $o_{\tau i}\ge0$, a nondecreasing concave function $h$, and reserved recent tokens $R_\tau\subseteq G_\tau$ define a one-step cache objective:

$$
\begin{aligned}
S_\tau\in\arg\max_{S\subseteq G_\tau}\quad &F_\tau(S):=h\left(\sum_{i\in S}o_{\tau i}\right)\\
\text{s.t.}\quad &|S|=B,\quad |S\setminus S_{\tau-1}|\le1,\quad R_\tau\subseteq S.
\end{aligned}
$$

**Dynamic submodular framework; Explicit formulation family.** Reserve size must permit feasibility; before filling the cache, use $|S|\le B$ and admit the new token. H2O combines historical heavy hitters with recency and attention-dependent updates; evicted tokens are unavailable without recomputation. Concave-over-modular $F_\tau$ is submodular (normalized if $h(0)=0$); for increasing $h$ its one-step ranking can coincide with the modular sum. Thus the meaningful distinction from static top-$k$ is the evolving accessible set, reserved recency, and endogenous scores. A one-removal decision can be enumerated exactly, without implying global future optimality; the paper's dynamic guarantee needs its additional assumptions.

[Zhang et al., NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html)

## Min–max and saddle-point optimization

<a id="app-30"></a>
### 30. Generative adversarial networks

Let $P_{\mathrm{data}}$ be the real-data law, $P_\epsilon$ a noise law, $G_{\theta_G}$ a generator, and $D_{\theta_D}:\mathbb R^d\to(0,1)$ a discriminator:

$$
\min_{\theta_G}\max_{\theta_D}\left[
\mathbb E_{\mathbf a\sim P_{\mathrm{data}}}\log D_{\theta_D}(\mathbf a)
+\mathbb E_{\boldsymbol\epsilon\sim P_\epsilon}\log\left(1-D_{\theta_D}(G_{\theta_G}(\boldsymbol\epsilon))\right)\right].
$$

**Min–max game; Explicit formulation.** The discriminator separates real and generated data while the generator tries to fool it. In the ideal unrestricted equilibrium, generated and real laws agree and the discriminator outputs one half. Neural parameterizations are nonconvex–nonconcave; alternating stochastic updates need not converge to a global saddle. Cycling, mode collapse, and finite-sample effects separate the practical algorithm from the ideal game.

[Goodfellow et al., NeurIPS 2014](https://proceedings.neurips.cc/paper_files/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html)

## Reading guarantees correctly

Optimization certificates apply to the specified model and its supplied data. A candidate-generation miss, inaccurate utility estimate, surrogate objective, relaxed feasible set, early solver stop, and approximate execution are distinct sources of error. The cross-paradigm discussion in the [paper on arXiv](https://arxiv.org/abs/2609.07254) explains these distinctions. In particular, an exact LP reformulation, an SDP bound, a greedy approximation ratio, a Pareto-stationary point, and an agentic iteration are different mathematical claims.
