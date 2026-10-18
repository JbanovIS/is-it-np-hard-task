# Часть 7: с. 14–16

[с. 14]
2113

Assessment of reinforcement learning algorithms...
n_steps must be decreased to find the lowest value for
which learning is observed. Thereupon, the entropy coefficient ent_coef must be decreased until learning is not
efficient anymore. The other hyper-parameters could then be
perturbed for trading-off exploration and exploitation even
more.
We should note that the approach mentioned above did not
leverage any particular structure of the loading pattern problem beyond the shape of the reward. The approach is problem
agnostic in that it can be extended to any other engineering
problem in particular with combinatorial structure, where
physic solver or SO-based approaches must be utilized. Typically, RL can seamlessly replace GA as the optimizer in [64]
for solving an instance of the Hybrid Flowshop Scheduling
Problem (HFSP). An action would represent a chromosome
structure, which results in a candidate. If the episode length
NF is greater than 1 (which we argument against), NF HFSP
solutions or chromosomes are generated per episode. The
difference with this paper of course is that we provide one
solution based on the template strategy (see Section 4.2.1).
In [64] however, they utilize GA as a decision-support tool
to gain managerial insights about strategy implemented to
solve a problem. Utilizing our approach instead could help
improve their insights on lot streaming strategies and subplots methodologies for gaining even more performance on

the HFSP. Similarly, [22] addresses the multi-objective version of our problem and the multi-objective RL can replace
the NSGA-II in the Multi-Objective Disassembly Line Balancing Problem (MODLBP) [65] to gain managerial insights
about tactical strategies and operational scenarios for the
MODLBP [65].
In Section 5.3 we apply this approach to classical benchmarks and empirically demonstrate that the aforementioned
approach extends to other types of problems.

Fig. 4 Application of our methodology with changes in (from top to
bottom) NF , nsteps , and ent_coef to four classical benchmarks (from left to right) Sphere, func4, func5, and func6. We use
ncores equal 8. 20 experiments of 10,000 samples are run for each

experiment for NF and nsteps , and 20,000 for ent_coef . The
other hyper-parameters are similar to that of the PWR loading pattern
problem (see Section 5.2)

5.3 Application of the method to classical
benchmarks
In this section, we apply our approach to four classical
benchmark functions: one is the Sphere function and the others originate from the CEC17 test suite [66] namely, func4
(shifted and rotated rosenbrock), func5 (shifted and rotated
rastrigin), and func6 (shifted and rotated expended schaffer).
For the NF and nsteps tests we choose an input dimension of nx equal to 2, while 10 for ent_coef . As we are
aiming at solving CO problems, the input space is a subset of {−35, 35}nx for the Sphere and {−100, 100}nx for the
functions of the CEC17 test suite. Hence, the number of solutions is (nx)70 or (nx)200 . Moreover, the data points in the
discretization of NF , nsteps , and ent_coef are spaced

123

[с. 15]
2114

enough to illustrate the behavior of these parameters and
are not guided by any desiderata of fine-tuned optimization.
The benchmark, as well as the algorithm, are available in
NEORL’s package [67]. The results are showcased in Fig. 4,
where the optimal objective for each function is the number
times 100 (e.g., for func2 it is 2 × 100 = 200):
As observed on the first row of Fig. 4, NF equal to 1 outperforms the other. In practice, for the higher NF to converge
to the optimal values, we needed to increase the number of
samples collected to at least 40,000, matching the observation
for the PWR problem, which is not efficient. For the second
row, we observe a trade-off between the different n_steps ,
where lower values result in faster convergence, but the value
of 8 (hence ncores × nsteps = 64, similar to case 2 of
Table 11) results in more stable learning (e.g, for func6 cases
2 and 4 have high variance). Lastly, for the third row, very
high ent_coef leads to no learning (e.g., 0.1 and 0.01 (for
all but the Sphere)), due to the high randomness of the policy
as observed for the PWR problem, while decreasing its value
results in faster convergence. Interestingly, a value of 0.001
results in the global optimum systematically as observed for
the PWR problem. We, therefore, demonstrated the extent
to which our approach to applying RL described in the last
paragraphs of Section 5.2 is more sample efficient beyond
only the PWR loading pattern optimization problem.

6 Concluding remarks
Deep RL is a framework which gained popularity in recent
years thanks to its ability to uncover solutions to problems which outclass expert designers [24] with applications
to ATARI games [68], GO [69], or CO [34] for instance.
There, RL does not work with an analytical representation
of an objective function but rather with objects (e.g., function approximators) that are constructed statistically with a
large number of data and which are then mathematically optimized. In that respect, this work proposed the first-of-a-kind
approach to deal with an RL-compliant PWR loading pattern
optimization.
In this work, a first-of-a-kind hyper-parameter study of
the RL framework applied to solve the loading pattern optimization problem over 24 hours is presented. The shape of
the reward, specifically the weights assigned to the constraints, is pivotal in finding feasible patterns. It behaves
as a fudge factor that could lead to substantial economical improvement but also affect the stability of the solutions
found throughout different experiments, which is an essential factor for scaling the algorithm to other applications. On
top of that, we found that the quality of the best LP found
is highly dependent on the exploration/exploitation trade-off
that manifests through the NF , n_steps , and ent_coef

123

P. Seurin and K. Shirvan

coefficients. Low values for the latter result in high exploitation, which allows the agents to find high-quality patterns
very rapidly, and is interesting for the core designer in case of
emergency core re-design. We show that the optimum value
for NF is 1, which means that RL is optimally leveraged
when it is applied similar to a Gaussian Process where the
acquisition function is learned via a policy, which then converges close to the optimum solution after a certain number
of steps. However, the behavior for low values for n_steps
and ent_coef is not always linear anymore, where a sweet
spot must be found to trade off quality, speed of convergence,
and stability. While n_steps controls the quality of the estimation of the gradient of the loss, ent_coef controls the
randomness of the policy. They must both be decreased until
no learning is observed or instability occurs to achieve the
highest sample efficiency. Additionally, the small deviation
of the SE metrics over the experiments for the set of hyperparameters found demonstrated that RL-based approaches
are robust and stable, which is what core designers are looking for to adopt a novel set of techniques in their work.
We also briefly studied the other parameters but empirically
showed that they were less important.
Most importantly, we argue that for different engineering
problems, the values can differ but the behavior could be similar. We demonstrated this by applying this approach to four
classical benchmarks with an integer input space. It makes
the approach developed in this work suitable for any largescale constrained problem in which expensive physic solver
or SO-based approaches must be utilized, in particular in the
realm of CO.
On top of that, due to the nature of the end-user, it is fundamental to propose a multi-measure approach in the decision
of determining the best set of hyper-parameters. We show that
classical metrics expected by the core designer such as the
max objective is not sufficient anymore when dealing with
the RL framework, for which the mean and standard deviation of the objective are testament of the potential of the RL
agents to improve in longer runs. In this prospect, we proposed to look at the max objective and the best mean objective
per episode, the improvement ratio, the mean objective SE,
the σ SE, and the p-value of statistical tests namely FT and
NT. Nonetheless, these metrics based on a single scalar value
for the reward will not be sufficient when a multi-objectivebased optimization is performed. In this prospect, the work
in [22] extends the current study with multi-objective RL
and attempts to propose appropriate supplementary metrics
to tackle this limitation.
Lastly, we found that the economic gain from the original pattern (with slightly empirically optimized hyperparameters) of Appendix A.1 with LCOE at 5.590 to 5.529
of Appendix A.4 is of the order of 535,000 - 642,000
$/year/plant for a 1,000 and 1,200 MWe NPP, respectively.

[с. 16]
2115

Assessment of reinforcement learning algorithms...

This illustrates the requirement to conduct a thorough hyperparameter study. Nevertheless, these hyper-parameters only
belong to the realm of the PPO framework and we have not
compared the latter against legacy SO heuristic-based methods such as SA, GA, or TS. This comparison will be all the
more interesting as we argued that using NF equal to 1 can
be thought of as if the agents are trying to find the steepest
ascent direction based on their understanding of the curvature
of the objective space, while SO-based methods are taking
random steps to find it. Can we gain robustness and stability when these directions are learned? Future work should
include the comparison to ensure the benefit of introducing
a RL-based framework for the PWR optimization problem.
But the works conducted in [19, 45] on lattice and bundle
designs, respectively, give hope that RL can outperform SObased heuristic methods on our problem.

weights , the length of an episode via NF , the n_steps ,
and the entropy coefficient ent_coef .

A.1 weights study
Defining the reward for the agent behaving in accordance
with the designer’s goals is called reward hacking. Defining the reward to optimize the performance of the agents
is called reward shaping. This study explores the influence
of setting weights on design constraints. Weights of 1,000,
5,000, 15,000, 25,000, 40,000, 50,000, 75,000, and 100,000
are considered. Moreover, all constraints will have the assignment of the same weight, since good quality results could not
be found when we manually experimented with varying the
individual weights. To compare the obtained pattern on the
same baseline, the penalization of the obtained pattern is normalized as follows [70]:


Appendix A: PPO hyper-parameters studies

D(x, C) =

 ci (x) − ci
(
)2
cimax − cimin

(12)

i∈C

In this appendix we provide the results of the major hyperparameters alluded in Section 2.3. The shape of the reward via

They were obtained by running one optimization and taking a lower
and upper bound with the best and worst cases

where D(x, C) is the distance of the core x to the space of
feasible core C in the objective space, and ci , i ∈ {1, ..., 5}
are the constraints defined in Section 4.2.2 (c6 , c7 are always
satisfied), which ranges are given in Table 2.
Figure 5 showcases the evolution of the mean score (left)
and max objective (right) per generation. A generation is
defined such that the experiments span 100 generations,
therefore one contains between 400 to 500 SIMULATE3
evaluations. As expected, the mean score is constantly
increasing meaning that the agents are learning. The intricate
behavior starting around the 60th generation is happening
when a feasible pattern has been found and the agents are
only optimizing the LCOE. This occurs at about the same

Fig. 5 Error bar plots averaged over 10 experiments for the Max (left)
and Mean (right) Objective per episode for different Weights values. The Mean was obtained by averaging the mean score obtained per

episode within a window of X episodes, where X depends on the total
number of samples generated (usually around 400 samples for NF
equal to 1 to obtain 100 generations). The length of the bars is two σ

Table 2 Upper and lower bounds utilized to calculate the range in (12)
FOMs

Upper bound

Lower bound

Fq [-]

2.911

1.768

F h [-]

2.206

1.429

Cb [ppm]

1405.1

952.7

Pin Peak Bu [GWd/tHm]

68.044

55.506

Cycle length [days]

530.8

468.9

123

