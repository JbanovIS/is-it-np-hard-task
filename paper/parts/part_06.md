# Часть 6: с. 12–13

[с. 12]
2111

Assessment of reinforcement learning algorithms...

last generation. If the latter is low it means that the agents
are close to convergence. We are aiming at seeing both high
mean objective SE and σ SE. To sum up, assessing the performance of hyper-parameters is a multi-measure problem.
It needs:
1. A high Max objective function ever found that complies
with the designer’s interest.
2. A high mean objective SE (at the time the algorithm stops)
over multiple generations and a high σ SE (potential for
future improvement) which comply with the RL interest.
3. A high improvement ratio, which means that the algorithm
has recently improved and is not behaving sub-optimally.
Additionally, the policy is by essence stochastic hence
comparing the results over one single optimization run is theoretically not sufficient. Commonly, a better approach would
be based on running N times each algorithm on the same
problem (e.g., N equal to 10 in [57], 15 in [58], 50 in [6], or
30 in [56]) and evaluate the best, mean, and standard deviation of the objective over all experiments for each type of
algorithms and draw conclusions from it. However, this does
not provide the level of certainty at which these conclusions
are valid (e.g., how high N should be). The latter issues can
be addressed via non-parametric statistical tests, which is a
class of popular methods adopted for instance in the world
of swarm and evolutionary computations [59, 60].
Hypothesis Testing (HT) [59, 61] is a classical inference
tool that lies at the basis of the parametric and non-parametric
tests. In HT, two hypotheses H0 , the null hypothesis, and H1 ,
the alternative hypothesis are a partition of the hypothesis
space. The goal for the experimenter is to decide whether
to accept or reject H0 after observing a sample based on a
hypothesis test, which defined the sample region for which
the null hypothesis is accepted or rejected. For our purpose,
the H0 could be that the two algorithms are equivalent in
performance for pairwise comparison [59], and rejecting H0
would signify that for a particular or a set of problems, one
algorithm outperforms the other. Furthermore, in the case of
multiple algorithms, the error from drawing a false conclusion from multiple pairwise comparisons may accumulate.
The Friedman Test (FT) [59] is the non-parametric version
of the repeated measures ANOVA [59, 61] test, which is used
to compare a set of assumptions at the same time. The inputs
to the tests for each instance of hyper-parameters will be
the value of the max objective and max mean objective per
episode for each experiment. This test however only confirms
that at least two instances come from different distribution
but do not provide conclusion on pairwise tests. Once an FT
is successful, post-hoc tests can be performed [59] to draw
the a conclusion between each assumption (e.g., which set
of hyper-parameters are the best). Even though it has limited
power [59], we will use here the Nemenyi Test (NT) due to

its simplicity and that it has been applied in a work related
to loading pattern optimization in [60]. At most 10 experiments for each variation of the parameters are run (with
the same seed for each variation of the parameters studied
and 10 seeds in total). The p values will also be provided,
which provide quantitative information on how certain are
we to reject one or the other hypothesis compared to a level
of significance α. Roughly, the p-value is the probability of
observing an instance at least as extreme as your results if the
null hypothesis H0 was true. The smaller it is, the more likely
we are to reject H0 . For a mathematical definition see [61].
The tests are implemented through the scipy.stats [62] and
scikit posthocs [63] packages for Friedman and Nemenyi,
respectively, with α equal to 0.05 as suggested in [60].
A previous in-housestudyled to the initial PPO hyper-parameters: nminibatches is 4, LR is 0.00025, max_grad_norm
is 0.5,  is 0.2, n_steps is 4, vf_coef is 1.0, and
noptepochs is set to 10. These were obtained by changing the hyper-parameters by hand until we had a significant
number of feasible patterns within 24 hours of run. Then,
all the weights in (5) were set to 25,000 except for constraints c6 , c7 , for which 1,000 is used. The vectorized state
is passed through a feature extractor (one flattened layer)
and the extracted features input a feed-forward two-layer
perceptron neural network policy with 64 hidden weights
per layer. The time to reach a feasible solution is also of
importance. For instance, emergency core re-designs can
be limited to 1-3 days because about a million dollars per
day is assumed to be lost during the shutdown of the NPP.
Therefore, it is important to tune the hyper-parameters to
achieve a similar level of speed. As a result, we decided to
limit the computing time allocated to our optimizations. For
all experiments, PPO agents ran from scratch for 24 hours,
which amounted to about 40,000-50,000 SIMULATE3 calls
or objective function evaluation on the Massachusetts Green
Energy High-Performance Computing Center, when using
one node of 2x16 cores (i.e., 32 agents) Intel Xeon 2.1 GHz
with 128 GB RAM. Section 5.2 summarizes our findings.

5.2 Summary of the studies conducted
In this section, we present a summary of the findings made
in this work (from Appendices A and B).
We first studied the shape of the objective function via
the weights in Appendix A.1. This parameter behaves as
a fudge factor which could result in an improvement on the
economic side but also the stability of the learning. Then, we
studied the parameter NF in Appendix A.2. This parameter plays a role in the exploration/exploitation trade-off. A
higher value will yield a lower mean objective. Due to the
significance of the statistical tests, we suggest however, to
always choose a value of 1, with the restarted state being

123

[с. 13]
P. Seurin and K. Shirvan

2112

Table 1 Summary of the hyper-parameters studied, the corresponding ranges, the default and final chosen value for each, and appendices in which
these studies can be found
Hyper-parameters

Range Studied

Default in stable-baselines

Best chosen

Corresponding appendix

weights

[1,000 - 100,000]

-

25,000

A.1

NF

[1-100]

-

1

A.2

n_steps

[1-75]

128

4

A.3

ent_coef

[0 - 0.01]

0.01

0.001

A.4

 These two hyper-parameters ( weights

and NF ) are specific to the core design optimization and not stable-baselines, hence there are no default

values for them

the best ever found. This formulation can be thought of as a
gradient ascent problem: At each episode, based on the understanding of the curvature of the objective space, the agents
are trying to find the steepest ascent direction. We also studied n_steps in appendix A.3 , which is a hyper-parameter
that controls the exploration/exploitation by playing with the
bias/variance trade-offs in the estimation of the gradient of
the PPO loss. A very low value may result in instability
of the agents and being stuck in local optima as few samples are exploited to evaluate the gradient. A higher value
may result in slow learning and a poorer quality of the best
pattern found because more samples will be needed before
optimization of the policy network’s parameters. Lastly, we
studied ent_coef in appendix A.4, which controls the randomness of the policy during training. It also controls the
exploration/exploitation trade-off. Lower values yield faster
convergence but are prone to local optima. On the other hand,
a high value will result in slower convergence. A sweet spot
between the speed of convergence, the quality of the pattern
found, and the stability of the learning of the agent resulted
in our choices of hyper-parameters and are summarized in
Table 1.
The reader should note that the value of the hyperparameter n_steps which was found to be optimal is excessively different from the default value in stable-baselines (4
against 128). This also underlines the need to perform a thorough evaluation of the hyper-parameters’ performance.
We also recall the conclusions of the studies in Appendix B:

1. The default value of LR equal to 0.00025 demonstrated
the optimum trade-off between fast learning with a premature convergence for higher values of LR but no learning
at all for lower values. See Appendix B.1 for more details.
2. The clipping parameter  can be very sensitive as a change
from 0.02 to 0.01 substantially worsened the performance
of the agents as showcased in Table 19. The default value
of 0.02 corresponds to a sweet spot between higher exploration but slow convergence for higher values but slow and
unstable learning for lower values. See Appendix B.2 for
more details.

123

3. For the hyper-parameter max_grad_norm the differences are not as visible as for LR or . Other values than
the default 0.5 could be competitive such as 1.0, 1.2, and
1.5. However, when coupled with the final ent_coef ,
0.5 demonstrated better SE measures than all of them. See
Appendix B.3 for more details.
4. A value of 10 for noptepochs was kept. Higher values
yielded a higher entropy of the policy network and therefore more random actions were taken. A lower value of 5
exacerbated similar performance in terms of the best pattern found and σ SE but a lower mean objective SE, while
a value of 1 prevented the agents to ever learn anything.
See appendix B.4 for more details.
5. The hyper-parameter nminibatches can be sensitive
and low values (below 4) are preferred. In spite of observing a smooth learning, higher values yielded very low
mean objective SE with very high σ SE. The default value
of 4 exacerbated better SE measures compared to 2. See
Appendix B.5 for more details.
6. Reducing the impact of the value function via reducing
VF_coef seemed to increase the exploitation. Lower
value often resulted in lower σ SE and higher mean objective SE and the trade-off sits between 1.0 and 0.8. The
study also revealed that improving the value function loss
had more impact on the SE measures than improving the
policy one. See Appendix B.7 for more details.
7. Halving the breadth (i.e., the number of hidden nodes per
layer) of the policy network systematically decreased the
mean objective SE and increased the σ SE, while the best
pattern found is very similar. On top of that, more layers (i.e., increasing the depth) resulted in slower learning
but a better average behavior. The default value of 2 was
kept thanks to a higher mean objective SE and σ SE. See
Appendix B.8 for more details.

Overall, we argue that the most sample efficient way to
apply RL is as follows: Due to the significance of the statistical tests for NF , a value of 1 should always be considered,
where a pattern is replaced by a problem-dependent input.
Then, for a given amount of sample, the hyper-parameter

