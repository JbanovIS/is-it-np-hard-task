# Часть 9: с. 20–22

[с. 20]
2119

Assessment of reinforcement learning algorithms...
Table 7 Mean Objective SE and σ SE for the different weights
cases
NF

Mean Objective SE

σ SE

1

-14.705

67.368

2

-188.447

177.915

7

-1548.257

514.939

10

-1689.118

481.794

25

-1928.256

335.519

75

-1887.0760

186.982

100

-2174.317

118.620

The latter is obtained by averaging the reward obtained over the last
generation and over 10 experiments. The case NF equal to 1 has the
best combination of both

high for both the mean and the max objective, meaning that
the agent’s decisions are indeed improving, except for the
max objective of case 100, which may hint that this solution
has been found randomly. The very low mean objective SE
for case 100 given in Table 7 confirms this hypothesis.
10 experiments for each case were ran. The p values for
the FT tests are all 0.00. Cases 1,2, and 7 were not statistically
significantly different as provided in Tables 8 and 9. However,
the p-value of case 1 versus case 7 is lower than that of case 2
versus case 7 for both max and mean score, which may hint
that case 1 is superior. The differences are sharper than that of
the weights ’s study. This should mean that 1 outperforms
the other cases, which aligns with our previous observation
and we decided to pursue with this value for the following
studies.
Overall, it is clear that the case NF equal to 1 outperforms the others and Tables 6 and 7 show that there is a very
sharp learning improvement when NF is decreased at a value
lower than 7, while the difference is less obvious above 7. In
addition, we can observe in Table 6 that a lower value of NF
usually yields a lower variance between the results at each
generation and always a better average behavior promising
better stability. In the first order, therefore, NF is a manifestation of the exploration/exploitation trade-off. Higher
NF yields higher exploitation and lower mean objective but
sometimes a better max objective (e.g., the max objective
Table 8 p-value for the NT
between the NF instances for
the maximum score

with NF equal to 75 exceeds that of 2 to 25), which is of
interest to the core designer. For low and high values of NF ,
the σ SE decreases as seen in Table 7. This column shows that
something else is happening. A high NF does not necessarily
involve slower convergence but in light of the column mean
objective SE it does imply a lower mean objective. Therefore
high NF should be avoided even if the optimization was run
longer due to the risk of being stuck in a local optimum.
It could be surprising to observe such a low mean objective
SE even for the case NF equal to 2 compared to 1. Having
NF equal to 1 with the restarted state being the best ever
found can be thought of as a gradient ascent problem: At
each episode, based on the understanding of the curvature of
the objective space, the agents are trying to find the steepest ascent direction similar to SO-based methods where the
steps are taken however randomly. Indeed in SO, the agents
are following a rule of thumb (i.e. heuristic) in the decision
process. It is a guided random walk. In RL, we have a policy
that generates solutions, while a critic learns and evaluates
the quality of these solutions. The heuristic is learned. In
this sense, it is similar to a Gaussian Process [73] in which
the acquisition function is a policy we learn, and the policy converges close to the optimum solution found. To the
author of this work, there is no obvious mathematical intuition behind greater NF . We initially thought that asking the
agent to solve multiple LPs at the same time would help as
one state of a pattern is the restarting state for the action to
choose the next pattern. These information could have helped
the agent draw better conclusions from one state to the next.
Nevertheless, it is clear that we are asking the agents to solve
multiple loading designs at the same time, therefore more
samples must be drawn to fully comprehend how an episode
is constructed, which might be more difficult and explains
why it is seemingly easier with the lowest NF . This study
may also explain why value-based methods (e.g., Deep QLearning (DQN) [68] or Double Q-Learning [74]) were not
performing well. One explanation might be that they required
one or multiple-step look-ahead to optimize the Q-function
[25]. However, as it was described in Section 4.1, each action
is a core created. Since a full core is created for each action,

NF

1

2

7

10

25

75

100

1

1.000000

0.900000

0.026662

0.001000

0.002000

0.013555

0.00100

2

-

1.000000

0.114484

0.004459

0.013555

0.066772

0.00654

7

-

-

1.000000

0.900000

0.900000

0.900000

0.90000

10

-

-

-

1.000000

0.900000

0.900000

0.90000

25

-

-

-

-

1.000000

0.900000

0.90000

75

-

-

-

-

-

1.000000

0.90000

The FT succeeded with p-value equal to 0.00. NF equal to 1 is the case that outperforms most of the other
experiments. The tests that succeeded are highlighted in red

123

[с. 21]
P. Seurin and K. Shirvan

2120
Table 9 p-value for the NT
between the NF instances for
the mean score per episode

NF

1

2

7

10

25

75

100

1

1.000000

0.900000

0.339674

0.087581

0.001315

0.001000

0.001000

2

-

1.000000

0.777817

0.404855

0.019139

0.001000

0.001000
0.005411

7

-

-

1.000000

0.900000

0.503923

0.022624

10

-

-

-

1.000000

0.869118

0.129190

0.042827

25

-

-

-

-

1.000000

0.808251

0.564789

75

-

-

-

-

-

1.000000

0.900000

The FT succeeded with the p-value equal to 0.00. If α = 0.1, which is sometimes considered [59], NF equal
to 1 is the case that outperforms most of the other experiments

each one fundamentally should not influence the generation
of the next and the Q-update might be ineffective.
Figure 8 showcases the 2D projection of the best pattern
found in this study (corresponding to the top row of Table 10).
There, in contrast to Fig. 6, rings of fire are observed from
the periphery to the center, which is also a typical designer
strategy. Lastly, by comparing the solution of NF equal to 1
and 2 in Table 10, the constraints are tighter for this design,
which helped again to reduce the LCOE.
Because the case NF equal to 2 presented a higher variance with a good Avg (Me), hence learning potential, we also
tried to restart the experiment with the trained policy from this
case for another one day of optimization. We also increases

NF to 250 and stopped at 6 experiments because the σ were
very low. It turned out that 75 was the best case on average but
no parametric tests succeeded as the differences were not significant, and the results are not presented for conciseness. The
better performance of 75 (max and average max objectives
of -4.558 and -4.573 respectively with σ ∼ 0.0120 averaged
over 6 experiments) corresponds to a boost in exploration.
In consequence, depending on the context of optimization,
there is a trade-off between exploration/exploitation. Preparing the next core cycle, which can take weeks, starting with
multiple runs with higher NF might lead to achieving a better solution than lower NF , but we should be wary of the
faster convergence if NF is increased.

Fig. 8 Lower right quadrant of the best pattern found with NF equal
to 1. On the left, from top to bottom: Assembly group number, fuel
average enrichment, number of IFBA rods, and number of WABA rods.
Blue is for twice-burned FAs, green for once-burned, and red for fresh
(colors pattern also utilized in ROSA [72]). In violet, location where

WABA cannot be placed. On the right, from top to bottom: Beginning of
cycle k∞ and assembly average burnup, peak pin Burnup at EOC, and
F h when the maximum over the cycle is reached. R means reflector,
where the water is

123

[с. 22]
2121

Assessment of reinforcement learning algorithms...
Table 10 Breakdown of the
FOMs for the best patterns
found for each case throughout
all experiments

Numframes

Objective

LCOE

Cycle length

Fq

F h

Cb

Pin peak Bu

1

-4.547

5.547

510.8

1.845

1.440

1178.8

61.198

2

-4.556

5.556

510.6

1.841

1.438

1178.4

61.172

75

-4.566

5.566

519.0

1.764

1.448

1195.3

61.204

10

-9.100

5.735

498.9

1.863

1.463

1191.8

61.285

7

-14.403

5.602

511.7

1.841

1.457

1221.7

62.082

25

-17.734

5.686

493.4

1.856

1.473

1208.1

59.623

100

-18.956

5.610

513.4

1.867

1.473

1169.3

62.872

An objective above - 5.00 signifies that the pattern is feasible and the agents are optimizing the LCOE only

To conclude this section, we can say that NF plays a role
in the exploration/exploitation trade-off. A higher value will
yield a lower mean objective. Nevertheless, a lower value
may lead to faster convergence, hence reaching and being
trapped in an unacceptable local optimum (see case 75). This
study also highlighted the importance of fine-tuning. Indeed,
a very small change in NF may drastically change the optimum value found. In terms of the LCOE between 1 and 2 for
a 1,000 or 1,200 MWe NPP, we get a gain of 79 - 95 k $/yr. On
top of that, case 7 did not even find a feasible design within
one day of optimization, which is fundamental for certain
application as we alluded in Section 5.1.
A.3 n_steps study
The parameter n_steps also plays a role in the exploration/exploitation trade-off as presented in Section 2.3. The
chosen values for the study are 1, 2, 4, 6, 8, 10, 25, 35, and
75, which were run over 10 experiments. Figure 9 showcases
the evolution of the max and mean objective over 100 gen-

Fig. 9 Error bar plots averaged over 10 experiments for the Max (left)
and Mean (right) Objective per episode for different n_steps values. The Mean was obtained by averaging the mean score obtained per

erations. It should be observed that there is smooth learning
for all values of n_steps .
Similar to the NF study, large values of n_steps yields
poor results with an average lower than - 5.00. The best patterns found are not even feasible for cases 35 and 75 as
highlighted by Table 11. The mean objective columns of
Table 11 are omitted as they are similar to that of the max
objective with NF equal to 1. They all have a high IR except
for case 75, but its low mean objective SE and σ SE hint that
the solution was found randomly. Moreover, the variance in
the results and the σ SE also increased with n_steps for
large values. However, this behavior is not linear anymore
below 4, where case 1 and 2 yield worse performances than
4, 6, 8, and 10 with a lower mean objective SE and a higher
σ SE as shown in Table 12. This may be a manifestation
of the exploration/exploitation trade-off as too few samples
are recorded with n_steps equal to 1 or 2, which yields
sub-optimum behavior. Column σ SE helps confirm the significance of n_steps regarding the trade-off. The higher
the value the higher the σ except below 4. Moreover, the

episode within a window of X episodes, where X depends on the total
number of samples generated (usually around 400 samples for NF
equal to 1 to obtain 100 generations). The length of the bars is two σ

123

