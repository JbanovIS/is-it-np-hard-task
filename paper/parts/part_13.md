# Часть 13: с. 34–35

[с. 34]
2133

Assessment of reinforcement learning algorithms...
Table 26 Figure of Merits for the depth and breadth of the architecture
studied
Depth values 

Best (MO)

1

-4.5892

-6.8169

19.2774

2

-4.6006

-7.9264

23.4465

3

-4.6101

-6.2860

26.1353

4

-4.6158

-5.0907

5.63168

1 + 32

-4.5999

-22.4148

59.2805

2 + 32

-4.5699

-13.1631

22.2361

3 + 32

-4.6480

-16.9550

39.3686

4 + 32

-4.5973

-33.7441

194.4261

Mean Objective SE

σ SE

Cases 1, 2, 3, and 4 have 64 hidden nodes per layer. The default case is
highlighted in red. 43,000 samples were drawn
 The difference between the average standard deviation in Tables 26
and 16 is that here the experiment were ran once with more samples.
Looking at experiment per experiment, in some instances, the algorithm
ran longer and a generation covered more time-steps, increasing the σ SE

No cases are close to convergence except case 4. There
the mean objective SE is lower than - 5.00, meaning that a
feasible pattern is not always found in average. What might
have happened is that it overfitted towards lower optima due
to its larger number of trainable parameters. On top of that,
the behavior of the number of hidden layer is opposite when
having 64 or 32 nodes. For cases with 64 nodes, the cases 2
and 3 have a lower mean objective SE and higher σ SE, which
is the opposite for cases with 32 hidden nodes. Moreover, the
case 4 + 32 is really far from convergence and has found an
excellent best pattern very rapidly. It is as if removing nodes
per layer smoothed out its learning and enable to escape local
optima. The default value of 2 exacerbates a lower mean
objective SE and higher σ SE, promising more potential for
improvement and stability if utilized for further optimization.
Overall, most of the cases competed with the default case 2
but the differences are not large enough and we concluded
that we did not need to delve into more studies.
Acknowledgements This work is sponsored by Constellation (formally
known as Exelon) Corporation under the award (40008739). Feedback
from Neil Huizenga and Antony Damico of Constellation were helpful
in setting up the problem constraints.
Author Contributions Methodology, software, formal analysis and
investigation, visualization, writing - original draft preparation: Paul
Seurin; conceptualization, methodology, funding acquisition, supervision, writing - review and editing: Koroush Shirvan. All authors have
read and agreed to the published version of the manuscript.
Data availability statement The sponsor of this study did not give written consent for their data to be shared publicly, so due to the sensitive
nature of the research supporting data is not available.

Declarations

Conflict of Interests The authors declare that they have no known
competing financial interests or personal relationships that could have
appeared to influence the work reported in this paper.

References
1. NEI. “NUCLEAR COSTS IN CONTEXT." Nuclear Energy Institute, NEI (2020)
2. Kropaczek DJ (2011) “COPERNICUS: A multi-cycle optimization
code for nuclear fuel based on parallel simulated annealing with
mixing of states. Progress Nuclear Energy 53(6):554–561
3. Park TK, Joo HG, Kim CH (2009) Multiobjective Loading Pattern
Optimization by Simulated Annealing Employing Discontinuous Penalty Function and Screening Technique. Nuclear Sci Eng
162:134–147
4. Parks GT (1996) Multiobjective pressurized water reactor reload
core design by nondominated genetic algorithm search. Nuclear
Sci Eng 124(1):178–187
5. de Moura Meneses AA, Araujo LM, Nast FN, Vasconcelos da Silva
P, Schirru R (2019) Optimization of Nuclear Reactors Loading Patterns with Computational Intelligence Methods. In: Platt G, Yang
XS, Silva Neto A (eds) Computational intelligence, optimization
and inverse problems with applications in engineering. Springer,
Cham
6. de Moura Meneses A, Schirru R (2015) A cross-entropy method
applied to the In-core fuel management optimization of a Pressurized Water Reactor. Progress Nuclear Energy 83:326–335
7. de Lima AMM, Schirru FC, da Silva R, Medeiros JACC (2008)
A nuclear reactor core fuel reload optimization using artificial ant
colony connective networks. Ann Nuclear Energy 35:1606–1612
8. Wu SC, Chan TH, Hsieh MS, Lin C (2016) Quantum evolutionary algorithm and tabu search in pressurized water reactor loading
pattern design. Ann Nuclear Energy 94:773–782
9. Lin S, Chen YH (2014) The max-min ant system and tabu search
for pressurized water reactor loading pattern design. Ann Nuclear
Energy 71:388–398
10. Erdoğan A, Geçkinli M (2003) A PWR reload optimisation (Xcore)
using artificial neural network and genetic algorithm. Ann Nuclear
Energy 30:35–53
11. Li Z, Huang J, Wang J, Ding M (2022) Comparative study of
meta-heuristic algorithms for reactor fuel reloading optimization
based on the developed BP-ANN calculation method. Ann Nuclear
Energy 165:108685
12. Ortiz JJ, Requena I (2004) “Using a multi-state recurrent neural networks to optimize loading patterns in BWRs. Ann Nuclear Energy
31:789–803
13. Yamamoto A (2003) Application of Neural Network for Loading
Pattern Screening of In-Core Optimization Calculations. Nuclear
Technol 144(1):63–75
14. Gozalvez JM, Yilmaz S, Alim F, Ivanov K, Levine SH (2006)
Sensitivity study on determining an efficient set of fuel assembly parameters in training data for designing of neural networks in
hybrid genetic algorithms. Ann Nuclear Energy 33:457–465
15. Bello I, Pham H, Le QV, Norouzi M, Bengio S (2016) “Neural combinatorial optimization with reinforcement learning."
arXiv:1611.09940
16. Khalil E, Dai H, Zhang Y, Dilkina B, Song L (2017) “Learning
combinatorial optimization algorithms over graphs." In NIPS’17:
Proceedings of the 31st international conference on neural information processing systems, pp 6348–6358
17. Li K, Zhang T, Wang R (2021) Deep Reinforcement Learning for
Multi-Objective Optimization. IEEE Trans Cybernet 51(6):3103–
3114

123

[с. 35]
2134
18. Nissan E, Siegelmann H, Galperin A, Kimhi S (1997) Upgrading
Automation for Nuclear Fuel In-Core Management: from the Symbolic Generation of Configurations, to the Neural Adaptations of
Heuristics. Eng Comput 13:1–19
19. Radaideh MI, Wolverton I, Joseph J, Tusar JJ, Otgonbaatar U, Roy
N, Forget B, Shirvan K (2021) “Physics-informed reinforcement
learning optimization of nuclear assembly design. Nuclear Eng Des
372:110966
20. Rempe KR, Smith KS, Henry AF (1989) “SIMULATE-3 pin power
reconstruction: methodology and benchmarking. Nuclear Sci Eng
103(4):334–342
21. Seurin P, Shirvan K (2022) “PWR Loading Pattern Optimization with Reinforcement Learning." International conference on
physics of reactors (PHYSOR 2022), pp 1166–1175
22. Seurin P, Shirvan K (2023) “Pareto Envelope Augmented with
Reinforcement Learning: Multi-objective reinforcement learningbased approach for Pressurized Water Reactor optimization." In
The international conference on mathematics and computational
methods applied to nuclear science and engineering (M&C 2023).
Niagara Falls, Ontario, Canada, August 13-17
23. Bertsekas DP, Tsitsiklis JN (1996) Neuro-Dynamic Programming.
Athena scientific Belmont, MA volume, p 1
24. Bengio Y, Lodi A, Prouvost A (2018) “Machine Learning for Combinatorial Optimization: a Methodological Tour d’Horizon.". Eur
J Oper Res 290(2):405–421
25. Hessel M, Modayil J, van Hasselt H, Schaul T, Ostrovski W,
Dabney G, Horgan D, Piot B, Azar M, Silver D (2018) “Rainbow: Combining Improvements in Deep Reinforcement Learning.
AAAI’18/IAAI’18/EAAI’18: Proceedings of the Thirty-Second
AAAI conference on artificial intelligence and thirtieth innovative applications of artificial intelligence conference and eighth
aaai symposium on educational advances in artificial intelligence
393:pp 3215–3222
26. Schulman J, Wolski F, Dhariwal P, Radford A, Klimov O (2017)
“Proximal policy optimization algorithms." arXiv:1707.06347
27. Schulman J, Levine S, Moritz P, Jordan M, Abbeel P (2017) “Trust
Region Policy Optimization." arXiv:1502.05477v5
28. Botvinick M, Ritter S, Wang JX, Kurth-Nelson Z, Blundell C, Hassabis D (2019) “Reinforcement Learning: Fast and Slow. Trends
Cognit Sci 23(5):408–422
29. Williams RJ (1992) Simple statistical gradient-following algorithms for connectionest reinforcement learning. Mach Learn
8(3):229–256
30. Wu Y, Mansimov E, Liao S, Grosse R, Ba J (2017) “Scalable
trust-region method for deep reinforcement learning using the
Kronecker-factored approximation." NIPS’17: Proceedings of the
31st International conference on neural information processing systems, pp 5285–5294
31. Kakade S, Langford J (2002) Approximately Optimal Approximate
Reinforcement Learning. ICML 2:267–274
32. Kakade S (2001) “A natural policy gradient. NIPS’01: Proceedings of the 14th International conference on neural information
processing systems: natural and synthetic, pp 1531–1538
33. Hill A, Raffin A, Ernestus M, Gleave A, Kanervisto A, Traore R,
Dhariwal P, Hesse C, Klimov O, Nichol A, Plappert M, Radford
A, Schulman J, Sidor S, Wu Y (2018) “Stable Baselines." https://
github.com/hill-a/stable-baselines
34. Mazyavkina N, Sviridov S, Ivanov S, Burnaev E (2021) Reinforcement Learning for Combinatorial Optimization: A survey. Comput
Oper Res 134:105400
35. Bertsimas D, Tsitsiklis JN (2008) Introduction to Linear Optimization. Athena Scientific, Dynamic Ideas
36. Dai H, Dai B, Song L (2016) “Discriminative embeddings of latent
variable models for structured data." ICML’16: Proceedings of
the 33rd International conference on international conference on
machine learning 48:2701–2711

123

P. Seurin and K. Shirvan
37. Vinyals O, Fortunato M, Jaitly N (2015) “Pointer networks."
NIPS’15: Proceedings of the 28th International Conference on
Neural Information Processing Systems 2:2692–2700
38. Nazari M, Oroojlooy A, Snyder LV, Takac M (2018) “Deep Reinforcement Learning for Solving the Vehicle Routing Problem."
NIPS’18: Proceedings of the 32nd International Conference on
Neural Information Processing Systems, pp 9861–9871
39. Mnih V, Badia AP, Mirza M, Graves A, Lillicrap TP, Harley
T, Silver D, Kavukcuoglu K (2016) “Asynchronous methods for
deep reinforcement learning. ICML’16: Proceedings of the 33rd
International Conference on International Conference on Machine
Learning 48:1928–1937
40. Xing R, Tu S, Xu L (2020) “Solve Traveling Salesman Problem by Monte Carlo Tree Search and Deep Neural Network."
arXiv:2005.06879v1
41. Emami P, Ranka S (2018) “Learning Permutations with Sinkhorn
Policy Gradient." arXiv:1805.07010v1
42. Kool W, Van Hoof H, Welling M (2018) “Attention Solves Your
TSP, Approximately." arXiv:1803.08475v2
43. Solozabal R, Ceberio J, Takáč M “Constrained Combinatorial Optimization with Reinforcement Learning." arXiv:2006.11984
44. Delarue A, Anderson R, Tjandraatmadja C (2020) “Reinforcement
Learning with Combinatorial Actions: An Application to Vehicle
Routing." NIPS’20: Proceedings of the 34th International conference on neural information processing systems 52:609–620
45. Radaideh MI, Forget B, Shirvan K (2021) Large-scale design optimisation of boiling water reactor bundles with neuroevolution. Ann
Nuclear Energy 160:108355
46. Kerkar N, Paulin P (2007) Exploitation des coeurs REP. EDP SCIENCES, 17, avenue du Hoggar, Parc d’activités de Courtaboeuf,
BP 112, 91944 Les Ulis Cedex A, France
47. del Campo CM, François JL, Avendano L, Gonzalez M (2004)
Development of a BWR loading pattern design system based on
modified genetic algorithms and knowledge. Ann Nuclear Energy
31:1901–1911
48. Castillo A, Alonso G, Morales LB, del Campo CM, François JL,
del Valle E (2004) BWR fuel reloads design using a Tabu search
technique. Ann Nuclear Energy 31:151–161
49. Radaideh MI, Shirvan K (2021) Rule-based reinforcement learning methodology to inform evolutionary algorithms for constrained optimization of engineering applications. Knowl-Based
Syst 217:106836
50. Nijimbere D, Zhao S, Gu X, Esangbedo MO (2021) TABU
SEARCH GUIDED BY REINFORCEMENT LEARNING FOR
THE MAX-MEAN DISPERSION PROBLEM. J Indust Manag
Optimizat 17:3223–3246
51. Saccheri JGB, Todreas NE, Driscoll MJ (2004) “A tight lattice,
Epithermal Core Design for the Integral PWR." In Proceedings of
ICAPP ’04, p 4359. Pittsburgh, PA, USA
52. “0523 - 0504P - Westinghouse Advanced Technology
- 03.4 - Analysis of Technical Specifications Unit 4."
nrc.gov/docs/ML1121/ML11216A087.pdf
53. Liu Y, Halev A, Liu X (2021) “Policy Learning with Constraints
in Model-free Reinforcement Learning: A Survey." International
Joint Conferences on Artificial Intelligence Organization, Survey
Track, pp 4508–4515. https://doi.org/10.24963/ijcai.2021/614
54. Li Z, Wang J, Ding M (2022) A review on optimization methods for nuclear reactor fuel reloading analysis. Nuclear Eng Des
397:111950
55. Kropaczek DJ, Turinsky PJ (1991) In-core nuclear fuel management optimization for pressurized water reactors utilizing
simulated annealing. Nuclear Technol 95(1):9–32
56. François JL, Ortiz-Sevrin JJ, Martin-del Campo C, Castillo A,
Esquivel-Estrada J (2012) Comparison of metaheuristic optimization techniques for BWR fuel reloads pattern design. Ann Nuclear
Energy 51:189–195

