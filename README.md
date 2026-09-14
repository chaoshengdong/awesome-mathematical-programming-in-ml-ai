<div align="center">

# Awesome Mathematical Programming in ML & AI

**A guide to the mathematical programming models behind machine learning, and AI systems.**

[![arXiv: 2609.07254](https://img.shields.io/badge/arXiv-2609.07254-b31b1b)](https://arxiv.org/abs/2609.07254)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[Paper on arXiv](https://arxiv.org/abs/2609.07254) · [Applications and papers](#taxonomy) · [Contribute](CONTRIBUTING.md)

</div>

This repository accompanies **[“Mathematical Programming in Machine Learning and Artificial Intelligence: A Unified Taxonomy of Models and Applications”](https://arxiv.org/abs/2609.07254)** by [Chaosheng Dong](mailto:ensteindcs@gmail.com). It collects applications and primary research papers across ten mathematical-programming paradigms.

![Overview of mathematical programming models and their applications in machine learning and artificial intelligence](figure/MP%20applications.png)

## Contents

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
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)
- [Acknowledgment](#acknowledgment)

<a id="taxonomy"></a>
## Linear Programming

<a id="app-01"></a>
### Compressed sensing and basis pursuit

- David L. Donoho. [Compressed Sensing](https://doi.org/10.1109/TIT.2006.871582). *IEEE Transactions on Information Theory*, 2006.

### LP with Network-Flow Structure

<a id="app-02"></a>
#### Min-cost network flow for multi-object tracking

- Li Zhang, Yuan Li, and Ramakant Nevatia. [Global Data Association for Multi-Object Tracking Using Network Flows](https://doi.org/10.1109/CVPR.2008.4587584). *CVPR*, 2008.

## Quadratic Programming

<a id="app-03"></a>
### Local reconstruction weights in Locally Linear Embedding

- Sam T. Roweis and Lawrence K. Saul. [Nonlinear Dimensionality Reduction by Locally Linear Embedding](https://doi.org/10.1126/science.290.5500.2323). *Science*, 2000.

## Binary and Mixed-Integer Programming

<a id="app-04"></a>
### RAG context selection under a token budget

- Shijia Xu et al. [Self-Correcting RAG: Enhancing Faithfulness via MMKP Context Selection and NLI-Guided MCTS](https://arxiv.org/abs/2604.10734). *arXiv preprint*, 2026.

<a id="app-05"></a>
### Mixture-of-experts routing

- Yanqi Zhou et al. [Mixture-of-Experts with Expert Choice Routing](https://proceedings.neurips.cc/paper_files/paper/2022/hash/2f00ecd787b432c1d36f3de9800728eb-Abstract-Conference.html). *NeurIPS*, 2022.

<a id="app-06"></a>
### Tool or agent-component selection

- Michelle Yuan et al. [Automated Composition of Agents: A Knapsack Approach for Agentic Component Selection](https://proceedings.neurips.cc/paper_files/paper/2025/hash/39c51d0fe64c273413a4d358361b3daa-Abstract-Conference.html). *NeurIPS*, 2025.

<a id="app-07"></a>
### Notification/email allocation and frequency optimization

- Bo Zhao et al. [Notification Volume Control and Optimization System at Pinterest](https://doi.org/10.1145/3219819.3219906). *KDD*, 2018.
- Xingwen Zhang et al. [Solving Billion-Scale Knapsack Problems](https://doi.org/10.1145/3366423.3380084). *The Web Conference*, 2020.

<a id="app-08"></a>
### Test-time reasoning and exploration-budget allocation

- Charlie Snell et al. [Scaling LLM Test-Time Compute Optimally Can Be More Effective than Scaling Model Parameters](https://openreview.net/forum?id=4FWaWZtd2n). *ICLR*, 2025.

<a id="app-09"></a>
### Optimal decision-tree construction

- Dimitris Bertsimas and Jack Dunn. [Optimal Classification Trees](https://doi.org/10.1007/s10994-017-5633-9). *Machine Learning*, 2017.

<a id="app-10"></a>
### Best subset selection

- Dimitris Bertsimas, Angela King, and Rahul Mazumder. [Best Subset Selection via a Modern Optimization Lens](https://doi.org/10.1214/15-AOS1388). *The Annals of Statistics*, 2016.

<a id="app-11"></a>
### Constrained maximum-inner-product retrieval

- Kohei Hirata et al. [Categorical Diversity-Aware Inner Product Search](https://doi.org/10.1109/ACCESS.2023.3234072). *IEEE Access*, 2023.

<a id="app-12"></a>
### Mixed-precision neural-network quantization

- Zhewei Yao et al. [HAWQ-V3: Dyadic Neural Network Quantization](https://proceedings.mlr.press/v139/yao21a.html). *ICML*, 2021.

<a id="app-13"></a>
### Diversity-aware recommendation

- Mi Zhang and Neil Hurley. [Avoiding Monotony: Improving the Diversity of Recommendation Lists](https://doi.org/10.1145/1454008.1454030). *RecSys*, 2008.

<a id="app-14"></a>
### Globally optimized k-means clustering

- Kolos Cs. Ágoston and Marianna Eisenberg-Nagy. [Mixed Integer Linear Programming Formulation for K-means Clustering Problem](https://doi.org/10.1007/s10100-023-00881-1). *Central European Journal of Operations Research*, 2024.
- Jan Pablo Burgard et al. [Mixed-Integer Programming Techniques for the Minimum Sum-of-Squares Clustering Problem](https://doi.org/10.1007/s10898-022-01267-4). *Journal of Global Optimization*, 2023.

<a id="app-15"></a>
### Video frame or keyframe selection

- Bo Fang et al. [Threading Keyframe with Narratives: MLLMs as Strong Long Video Comprehenders](https://proceedings.iclr.cc/paper_files/paper/2026/hash/675a31be2d051be53d57bced52c6631f-Abstract-Conference.html). *ICLR*, 2026.

## Conic Programming

<a id="app-16"></a>
### Group Lasso as SOCP

- Ming Yuan and Yi Lin. [Model Selection and Estimation in Regression with Grouped Variables](https://doi.org/10.1111/j.1467-9868.2005.00532.x). *Journal of the Royal Statistical Society: Series B*, 2006.

<a id="app-17"></a>
### Sparse PCA as SDP

- Alexandre d'Aspremont et al. [A Direct Formulation for Sparse PCA Using Semidefinite Programming](https://proceedings.neurips.cc/paper/2628-a-direct-formulation-for-sparse-pca-using-semidefinite-programming). *NIPS*, 2004.

## Bilevel Programming

<a id="app-18"></a>
### Hyperparameter optimization

- Luca Franceschi et al. [Bilevel Programming for Hyperparameter Optimization and Meta-Learning](https://proceedings.mlr.press/v80/franceschi18a.html). *ICML*, 2018.

<a id="app-19"></a>
### Neural architecture search

- Hanxiao Liu, Karen Simonyan, and Yiming Yang. [DARTS: Differentiable Architecture Search](https://openreview.net/forum?id=S1eYHoC5FX). *ICLR*, 2019.

<a id="app-20"></a>
### Coreset selection and data subsampling

- Xiao Zhou et al. [Probabilistic Bilevel Coreset Selection](https://proceedings.mlr.press/v162/zhou22h.html). *ICML*, 2022.

<a id="app-21"></a>
### Autonomous scientific discovery and AI Scientist systems

- Pingchuan Ma et al. [LLM and Simulation as Bilevel Optimizers: A New Paradigm to Advance Physical Scientific Discovery](https://proceedings.mlr.press/v235/ma24m.html). *ICML*, 2024.
- Yuanqi Du et al. [Accelerating Scientific Discovery with Autonomous Goal-evolving Agents](https://arxiv.org/abs/2512.21782). *arXiv preprint*, 2025.

<a id="app-22"></a>
### Diffusion-model hyperparameter and noise-schedule optimization

- Quan Xiao et al. [A First-order Generative Bilevel Optimization Framework for Diffusion Models](https://proceedings.mlr.press/v267/xiao25i.html). *ICML*, 2025.

## Multi-Objective Optimization

<a id="app-23"></a>
### Multi-task learning

- Ozan Sener and Vladlen Koltun. [Multi-Task Learning as Multi-Objective Optimization](https://proceedings.neurips.cc/paper/2018/hash/432aca3a1e345e339f35a30c8f65edce-Abstract.html). *NeurIPS*, 2018.
- Michinari Momma, Chaosheng Dong, and Jia Liu. [A Multi-objective / Multi-task Learning Framework Induced by Pareto Stationarity](https://proceedings.mlr.press/v162/momma22a.html). *ICML*, 2022.

## Inverse Optimization

<a id="app-24"></a>
### Inverse reinforcement learning

- Andrew Y. Ng and Stuart J. Russell. [Algorithms for Inverse Reinforcement Learning](https://ai.stanford.edu/~ang/papers/icml00-irl.pdf). *ICML*, 2000.
- Chaosheng Dong, Yiran Chen, and Bo Zeng. [Generalized Inverse Optimization through Online Learning](https://proceedings.neurips.cc/paper_files/paper/2018/hash/28dd2c7955ce926456240b2ff0100bde-Abstract.html). *NeurIPS*, 2018.
- Chaosheng Dong and Yijia Wang. [Towards Generalized Inverse Reinforcement Learning](https://arxiv.org/abs/2402.07246). *arXiv preprint*, 2024.

## Distributionally Robust Optimization

<a id="app-25"></a>
### Contrastive learning as DRO

- Junkang Wu et al. [Understanding Contrastive Learning via Distributionally Robust Optimization](https://proceedings.neurips.cc/paper_files/paper/2023/hash/48aaa5ea741ae8430bd58e25917d267d-Abstract-Conference.html). *NeurIPS*, 2023.

<a id="app-26"></a>
### Distributionally robust DPO for LLM alignment

- Zaiyan Xu et al. [Robust LLM Alignment via Distributionally Robust Direct Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/272efd3a6091ceefcbc79f1f3a6fdba4-Abstract-Conference.html). *NeurIPS*, 2025.

## Submodular Optimization

<a id="app-27"></a>
### Data subset selection and active learning

- Kai Wei, Rishabh Iyer, and Jeff Bilmes. [Submodularity in Data Subset Selection and Active Learning](https://proceedings.mlr.press/v37/wei15.html). *ICML*, 2015.

<a id="app-28"></a>
### Document summarization

- Hui Lin and Jeff Bilmes. [A Class of Submodular Functions for Document Summarization](https://aclanthology.org/P11-1052/). *ACL*, 2011.

<a id="app-29"></a>
### KV-cache eviction for LLM inference

- Zhenyu Zhang et al. [H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html). *NeurIPS*, 2023.

<a id="minmax-and-saddle-point-optimization"></a>
## Min–Max and Saddle-Point Optimization

<a id="app-30"></a>
### Generative adversarial networks

- Ian J. Goodfellow et al. [Generative Adversarial Nets](https://proceedings.neurips.cc/paper_files/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html). *NIPS*, 2014.

## Contributing

Corrections, bibliographic updates, and primary-source links are welcome. Please follow [CONTRIBUTING.md](CONTRIBUTING.md) and identify the application name and relevant primary source.

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

Please also cite the original papers for the methods you use. Their records are collected in the [application and reference catalog](data/applications.json).

## License

This repository is released under the [MIT License](LICENSE), copyright © 2026 Chaosheng Dong. Linked research papers retain their respective licenses.

## Acknowledgment

This repository is maintained by the authors of Mathematical Programming in Machine Learning and Artificial Intelligence: A Unified Taxonomy of Models and Applications.
