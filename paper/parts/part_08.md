# Часть 8: с. 17–19

[с. 17]
P. Seurin and K. Shirvan

2116
Table 3 Statistics for each weights value over 10 experiments
IR (MO)

Avg (Me)

Best (Me)

σ (Me)

IR (Me)

0.5247

0.946

-5.500

-4.570

0.4536

0.952

0.4362

0.992

-5.680

-5.557

0.086711

0.988

0.4994

0.787

-5.725

-5.602

0.08524

0.981

-4.590

0.4716

0.973

-5.573

-4.683

0.2993

0.974

-4.577

0.4834

0.968

-5.693

-5.614

0.04588

0.978

-5.447

-4.628

0.4037

0.993

-5.685

-5.588

0.05552

0.997

75,000

-4.947

-4.579

0.508

0.998

-5.683

-5.606

0.0555

0.9555

100,000

-5.480

-4.572

0.441

0.849

-5.717

-5.635

0.05234

0.966

weights

Avg (MO)

Best (MO)

1,000

-5.438

-4.570

5,000

-5.460

-4.569

15,000

-5.132

-4.582

25,000

-4.953

40,000

-5.356

50,000

σ (MO)

MO stands for Max Objective and Me for Mean objective per episode. The objectives are calculated based on the normalized objective value of
(12). The best objective values are highlighted in red

time for all weights . It is interesting to note that this happens for both mean score and max objective signifying that
the agents behave well almost at the same time as they are
hitting a feasible pattern and hence received a boost in reward.
Additionally, the seemingly less smooth behavior compared to other hyper-parameter studies (e.g., see Figs. 7 and
9) is due to the normalizing of the objective with (12). In
all cases, the max objective keeps increasing late during the
search, as confirmed by the high IR provided in Table 3 and
the standard deviation are in the same range. Therefore, no
significant differences can be observed in terms of absolute
performance. On top of that, the p-value for the FT with the
max score is 0.351 and 0.876 for the mean. Hence these tests
failed. However, we decided to stop the experiments as we did
not observe significant differences in the performance with
the different weights in contrast to the hyper-parameters
studied in the next sections. We defined however more metrics at the beginning of this section and Tables 3 and 4 could
provide more information and better-informed pathways to
decide which weights to pursue the study with.

Table 4 Mean Objective SE and the σ SE for the different weights
cases
Weights

Mean Objective SE

σ SE

1,000

-5.8573

0.09069

5,000

-5.8074

0.08265

15,000

-5.8096

0.08514

25,000

-5.7360

0.07093

40,000

-5.7971

0.0841

50,000

-5.7956

0.0838

75,000

-5.7590

0.09441

100,000

-5.8166

0.08657

The latter is obtained by averaging the reward obtained over the last
generation and over 10 experiments. The best performance for both is
obtained with weights equal to 25,000. The best values are highlighted in red

123

In light of Table 3, the best average behavior for the max
objective is obtained with weights 75,000, which also
achieves a very competitive best pattern overall. In RL literature, it is sometimes advised to normalize the reward,
otherwise, the magnitude of the gradients will be too different. But here one small change in the core with 75,000
may result in the blowout of the cumulative reward, which
could be counter-intuitive. The fact that NF and n_steps
equal 2 and 4, respectively, and the use of a clipping term
and max_grad_norm mitigate this effect. On top of that,
the best pattern was found with weights 5,000, while the
case 1,000 achieves the best mean score per episode with
25,000 being very close for this metric. But the behavior
among the weights is not linear, as a weights of 25,000
achieves better results than 40,000, 50,000, and 100,000 in
total, while a better mean score than 75,000 and almost as
good max objective. Additionally, case 25,000 achieves the
second best performance in terms of mean score, with a mean
objective SE at - 5.7360, the highest one. Even though the
differences do not look significant, the case 25,000 has the
lowest σ SE at the last generation given in Table 4, signifying greater stability. Hence if the input variables were to
change without the possibility to run 10 experiments due to
time constraints (e.g., in case of emergency core redesign) we
could imagine that utilizing 25,000 could help find a feasible
pattern with a higher probability.
The breakdown of the FOMs of the best patterns found in
each case is given in Table 5. The constraints c6 and c7 turned
out to be usually satisfied and were omitted from the table,
which will be the case in the remainder of the study. It should
be noted that for the best pattern, some constraints are close
to being tight (e.g., F h , Cb , and Pin Peak Bu) in contrast to
the one found with weights 25,000 for instance. This may
show that to optimize the LCOE further, penalties on some
constraints may need to be taken.
The 2D projection of the best pattern found (i.e., with
weights equal to 5,000) is given in Fig. 6. This case

[с. 18]
2117

Assessment of reinforcement learning algorithms...
Table 5 Best patterns found for
each case throughout all
experiments

Objective

LCOE

Cycle length

Fq

F h

Cb

Pin peak Bu

5,000

-4.569

5.569

519.1

1.812

1.448

1189.3

61.262

1,000

-4.570

5.570

510.8

1.831

1.436

1195.8

61.581

100,000

-4.572

5.572

507.4

1.801

1.439

1179.5

61.485

40,000

-4.577

5.577

505.5

1.813

1.449

1199.1

59.759

75,000

-4.579

5.579

501.1

1.834

1.450

1198.3

60.773

15,000

-4.582

5.582

511.3

1.810

1.419

1190.6

61.518

25,000

-4.590

5.590

511.7

1.835

1.438

1183.0

61.058

50,000

-4.628

5.628

505.0

1.824

1.448

1138.1

59.767

Weights

An Objective above - 5.00 signifies that the pattern is feasible and the agents are optimizing the LCOE only

presents a high IR and a low σ SE throughout the 10 experiments. It means that the agents are constructing high-quality
patterns at each episode, which is a testament of the agents’s
understanding of the objective space. There, the agents
employed several classical designer’s tactics even though no
prior knowledge of the physics involved was given before the
search started: the inner part of the core is mostly arranged
like a checkerboard between fresh and once-burned FAs, a
higher BP concentration is given to the FAs closer to the center, and FAs with a higher k∞ are located near the periphery,
which help to reduce the peaking factor and boron concentration [9]. This is worth noting as many papers instead impose
that these expert heuristics are satisfied in the decision process as in [8, 9, 71]. However, usually designer put more
WABA in the diagonal and the ring of fire because the power
is shifted from the center of the core (where low enrichment
and high IFBA are placed) to there. But here the agent decided

to also utilize high WABA in-board but not in the ring of fire.
This may be explained by the fact that WABA costs money,
hence reducing its amount is pivotal, and removing it from the
ring of fire may be the path of lowest resistance. Other Expert
tactics for twice-burned include choosing once-burned with
the highest k∞ to obtain enough carry-over energy for the
next cycle and FAs with low average burnup to limit the risk
of high peak pin burnup at the periphery. Here the average
burnup of twice-burned at EOC is not high but not particularly low neither for the ones on both sides of the diagonal
(48.5 GWd/tHm at BOC). These FAs will then peak at 61.0.
The peak pin burnup is also close to 62 GWd/tHm (61.3
GWd/tHm for the fourth FA starting from the left or the top).
This may be explained because we are not only studying
safety parameters. There is no penalty as long as the peak pin
burnup is within 62 GWd/tHm, but the LCOE is decreased
by extracting more energy out of these FAs.

Fig. 6 Lower right quadrant of the best pattern found obtained for
weights equal to 5,000. On the left, from top to bottom: Assembly group number, fuel average enrichment, number of IFBA rods,
and number of WABA rods. Blue is for twice-burned FAs, green
for once-burned, and red for fresh (colors pattern also utilized in

ROSA [72]). In violet, location where WABA cannot be placed. On
the right, from top to bottom: Beginning of cycle k∞ and assembly average burnup, peak pin Burnup at EOC, and F h when the
maximum over the cycle is reached. R means reflector, where the
water is

123

[с. 19]
P. Seurin and K. Shirvan

2118

Fig. 7 Error bar plots averaged over 10 experiments for the Max (left)
and Mean (right) Objective per episode for different NF values. The
Mean was obtained by averaging the mean score obtained per episode

within a window of X episodes, where X depends on the total number
of samples generated (usually around 400 samples for NF equal to 1
to obtain 100 generations). The length of the bars is two σ

To conclude this section, we can say that the weights
do not participate in the exploration/exploitation trade-off,
which makes sense as they are affecting the magnitude
of the reward only. It remains a very important parameter nonetheless. It behaves as a fudge factor which could
result in an improvement on the economic side and the
stability of the agents. Comparing the LCOE of the patterns found with weights 5,000 and 25,000, a gain of
about 180,000 and 220,000 $/year/plant for a 1,000 and
1200 MWe NPP, respectively, could be achieved by tuning the weights appropriately. However, we demonstrated
with a multi-measure analysis that looking at the maximum
objective is not sufficient, specifically because it does not
necessarily yield to a better mean objective SE, which does
not offer high certainty to find a feasible pattern rapidly with
a different seed. The latter becomes instrumental if different input variables were given and a new problem must be
solved rapidly which is achieved with more certainty with

25,000 as weights . All the observations made in this section motivated us to pursue with 25,000 as it presented the
best trade-off between our multiple performance metrics.
A.2 Numframes NF study
A prior study [67] showed that NF should not vary beyond
100. Here, the values are 1, 2, 7, 10, 25, 75, and 100. Figure 7
showcases the evolution of the mean score and max objective
over 100 generations. For all NF there is continuous learning occurring however it is clear in this figure that very low
NF values (i.e., 1 and 2) outperform higher ones, which is
confirmed by Table 6 for the Avg (Me). Regarding the righthand side of Fig. 7, we could imagine that the performance
of the case NF equal to 1 saturates after the 50th generation.
Nevertheless, this is simply the effect of scaling. The IR is
high above 87% meaning that the agents are still improving
their learning of the system and the high σ SE of Table 7 confirms this hypothesis. More generally for all cases, the IR is

Table 6 Statistics for each NF value over 10 experiments
Numframes

Avg (MO)

Best (MO)

σ (MO)

IR (MO)

Avg (Me)

Best (Me)

σ (Me)

IR (Me)

1

-4.599

-4.556

0.0257

0.879

-4.600

-4.5560

0.0257

0.879

2

-5.454

-4.556

1.646

0.879

-18.009

-4.5600

17.6663

0.807

7

-30.421

-14.403

18.408

0.846

-624.044

-518.000

95.611

0.797

10

-51.106

-9.100

27.522

0.855

-790.045

-625.610

67.623

0.998

25

-44.986

-5.710

24.495

0.567

-1200.059

-1036.77

91.847

0.991

75

-43.779

-4.566

35.0578

0.863

-1479.925

-1316.27

90.349

0.799

100

-53.470

-18.956

30.311

0.691

-1648.797

-1434.82

234.060

0.855

MO stands for Max Objective and Me for Mean objective per episode. The best result for each column is highlighted in red

123

