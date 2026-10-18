# Часть 10: с. 23–25

[с. 23]
P. Seurin and K. Shirvan

2122
Table 11 Statistics for each n_steps values over 10 experiments
σ (MO)

n_steps

Avg (MO)

Best (MO)

IR (MO)

1

-4.616

-10.6647

6.3040

0.947

2

-4.902

-4.551

0.548

0.925

4

-4.599

-4.556

0.027

0.879

6

-4.603

-4.523

0.025

0.981

8

-4.867

-4.544

0.530

0.866

10

-4.944

-4.540

1.026

0.925

25

-7.133

-4.540

1.026

0.868

35

-14.153

-6.395

5.900

0.887

75

-59.128

-6.542

35.286

0.554

MO stands for Max Objective. The Mean objective per episode is not
included because it is equal to the Max Objective one for NF equal to
1. The best result for each column is highlighted in red

cases 1 and 2 present a high σ (MO), showing that they are
also unstable.
Multiply by ncores , n_steps define the number of
samples utilized for the estimation of the gradient of the loss
see (3) to update θ , and hence its quality. We hypothesize
that the previous behavior is explained because low values
(e.g., 1) result in a very poor local approximation of the
gradient (i.e., high bias). On the other hand, larger values
(e.g., 4, 6, 8...) may decrease the bias of the estimator but
increase the variance due to the presence of more terms. In
the beginning, the loss is constructed with many samples of
poor quality, impeding the speed of learning. Once better
samples are obtained, learning happens, and good solutions
can be obtained.
The mean objective SE and σ SE increase with n_steps
above 4, which confirms that this hyper-parameter directly
control the level of exploration and exploitation in the search.
With an average max objective of -4.599, the best average
behavior is observed with 4, while 6 is very close but obtained
a better max objective. Looking at the mean objective SE in
Table 12 we can see however that case 4 is producing better
patterns on average for the last generation with a lower σ SE,
indicating higher stability and probability to generate a good
pattern.
The NTs on the max objective did not succeed between
2, 4, 6, 8, and 10 as shown in Table 13, which is expected
considering the few differences observed in Table 11. The
case 6 succeeded against every value above 10 while the
cases 4, 8„ and 10 succeeded against 2 out of the three values,
therefore they might be considered the best cases. However,
the considerations summarised above show that case 4 is
superior to other metrics. For these reasons, we decided to
keep n_steps equal to 4 for the remainder of the study.
Additionally, the characteristics of the best patterns found
are given in Table 14. The dissimilarities are not as high as for
the NF study of Appendix A.2, but fine-tuning n_steps at

123

Table 12 Mean Objective SE for the different n_steps cases with
the σ SE
n_steps

Mean Objective SE

σ SE

1

-545.268

513.820

2

-123.293

219.7689

4

-14.705

67.3678

6

-46.059

76.1462

8

-81.982

138.7982

10

162.167

208.8235

25

-529.769

548.3574

35

-858.295

756.5167

75

-2020.529

1711.8901

The latter is obtained by averaging the reward obtained over the last
generation and over 10 experiments

a very fine level could have significant consequences. With
n_steps equal to 6 allows an economy of 0.033 $/MWh
compared to the best solution found with 4, which amounts to
about 290,000 - 350,000 $/yr in benefit for a 1,000 or 1,200
MWe NPP, respectively. In this case, the boron’s constraint
is tight but the Fq ’s one has more leeway, and agents trying
to optimize or a designer taking over the core found could
try to take penalties on the latter to improve the LCOE.
Lastly, the 2D projection of the best pattern found is given
in Fig. 10. The fuel placement is similar to that of Fig. 8
but the LCOE is lower. The average enrichment of this core
is 4.35% with an average burnup per assembly at 35.742
GWd/tHm, against 4.4% and 35.414 GWd/tHm for the previous core. Even though the F h was lower for the previous
core the Fq was higher. Combined with a higher cycle length
and lower pin peak Bu, it hints that the power profile must be
spread out more evenly hence increasing the average burnup
per FAs and the energy extracted at a lower enrichment cost
reducing the LCOE.
To conclude this section, we saw that n_steps is a
hyper-parameter that controls the exploration/exploitation by
playing with the bias/variance trade-offs in the estimation of
the gradient of the PPO loss. A very low value may result in
instability of the agents and being stuck in local optima. A
higher value may result in slow learning and a poorer quality of the best pattern found. Due to the scope of the study
(optimization over one day), favoring lower value is the path
forward. For a longer run, it might be preferable to utilize
larger values up to 10.
A.4 ent_coef study
Lastly, in this section we study the influence of the entropy
coefficient ent_coef . The entropy term is given by the
entropy (a notion originating from information theory) of
the distribution satisfied by the policy. This corresponds to
the terms H (θ ) and c2 in (3). The values 0, 0.00001, 0.0001,

[с. 24]
2123

Assessment of reinforcement learning algorithms...
Table 13 p-value for the NT between the n_steps instances
ID

1

2

4

6

8

10

25

35

75

1

1.000000

0.512019

0.030146

0.003953

0.257126

0.079975

0.900000

0.900000

0.809296

2

-

1.000000

0.900000

0.660658

0.900000

0.900000

0.710204

0.099098

0.009917

4

-

-

1.000000

0.900000

0.900000

0.900000

0.079975

0.001473

0.001000

6

-

-

-

1.000000

0.900000

0.900000

0.013263

0.001000

0.001000

8

-

-

-

-

1.000000

0.900000

0.460015

0.030146

0.002063

10

-

-

-

-

-

1.000000

0.180790

0.005415

0.001000

25

-

-

-

-

-

-

1.000000

0.900000

0.611110

35

-

-

-

-

-

-

-

1.000000

0.900000

The FT is successful with p equal to 0.0. Case n_steps equal 4, 6 , and 10 are not statistically significantly different
Table 14 Best patterns found
for each case throughout all
experiments

n_steps

Objective

LCOE

Cycle length

Fq

F h

Cb

Pin peak Bu

6

-4.523

5.523

513.9

1.811

1.443

1200

61.225

10

-4.540

5.540

510.3

1.813

1.444

1168.9

60.548

8

-4.544

5.540

507.8

1.822

1.449

1195.1

60.682

2

-4.551

5.628

515.7

1.822

1.446

1186.9

61.446

4

-4.556

5.556

510.6

1.841

1.438

1178.4

61.172

25

-4.620

5.623

506.3

1.825

1.432

1161.7

61.910

1

-4.616

5.616

504.7

1.832

1.449

1183.2

60.178

35

-6.400

5.610

501.6

1.857

1.456

1186.2

60.763

75

-6.540

5.627

502.0

1.850

1.458

1146.3

62.154

An Objective above - 5.00 signifies that the pattern is feasible and the agents are optimizing the LCOE only

Fig. 10 Lower right quadrant for the best n_steps case equal to 6.
On the left, from top to bottom: Assembly group number, fuel average
enrichment, number of IFBA rods, and number of WABA rods. Blue is
for twice-burned FAs, green for once-burned, and red for fresh (colors
pattern also utilized in ROSA [72]). In violet, location where WABA

cannot be placed. On the right, from top to bottom: Beginning of cycle
k∞ and assembly average burnup, peak pin Burnup at EOC, and F h
when the maximum over the cycle is reached. R means reflector, where
the water is

123

[с. 25]
P. Seurin and K. Shirvan

2124

Fig. 11 Error bar plots averaged over 10 experiments for Max (left)
and Mean (right) Objective per episode for different ent_coef values. The Mean was obtained by averaging the mean score obtained per

episode within a window of X episodes, where X depends on the total
number of samples generated (usually around 400 samples for NF
equal to 1 to obtain 100 generations). The length of the bars is two σ

0.001, and 0.01 (the default value in stable-baselines) are
compared. Greater values than 0.01 were yielding very poor
results and were omitted.
The analysis of Fig. 11 demonstrates the role of the entropy
in the exploration/exploitation trade-off. Higher entropy
coefficients yield faster convergence and sometimes to lower
optima, which is confirmed by the average max objective and
mean objective SE columns of Tables 15 and 16, respectively.
The case without entropy has a higher σ (MO) between the
experiments even though it is supposed to have the highest exploitation. This could be explained by the fact that
this entropy coefficient is too low, reaching a different suboptimal solution anytime depending on the seed that steers
initial random actions in different directions. The low mean
objective SE and σ SE confirm this hypothesis. It converged
sometimes to great, sometimes to poor local optima demonstrating signs of instability.
With a low mean objective SE but a high σ SE, value 0.01
is not converging and is still learning but has found the second
best pattern overall behind 0.001. The standard deviations (σ

(MO)) for the cases 0.001 and 0.01 throughout the experiments (Table 15) are low compared to the others meaning
that they are more stable. Moreover, their σ SE (Table 16)
is high, meaning that they are both learning. The sweet spot
is therefore located between 0.001 and 0.01. However, the
case 0.001 is on average reproducing patterns of high quality
(highest Avg (MO) above - 5.00 in Table 15) and found an
excellent pattern overall with the highest Best (MO).
The FT failed with a value of 0.267 and therefore no posthoc tests were computed. More experiments is needed to
reach statistical significance but due to the reasons stated
above, we could safely conclude that lowering the entropy
coefficient to 0.001 is the way forward.
Looking at Table 17, we see that generally again, better LCOE will yield tighter constraints, except for the cycle
length which could be higher. The 2D projection on the
lower right quadrant of the best pattern overall found (with
ent_coef equal to 0.001) is given in Fig. 12. Similar to the

Table 15 Statistics for each ent_coef values over 10 experiments
ent_coef

Avg (MO)

Best (MO)

σ (MO)

IR (MO)

0.00000

-5.336

-4.557

1.875

0.404

0.00001

-5.929

-4.574

1.648

0.636

0.0001

-5.343

-4.558

1.138

0.271

0.001

-4.593

-4.529

0.0269

0.288

0.01

-4.599

-4.556

0.0264

0.879

MO stands for Max Objective. The best result for each column is highlighted in red. The Mean Objective SE is obtained by averaging the
reward obtained over the last generation and over 10 experiments

123

Table 16 Mean Objective SE for the different weights cases with
the σ SE
ent_coef

Mean Objective SE

σ SE

0.00000

-16.231

1.5563

0.00001

-6.953

0.2092

0.0001

-5.691

2.5536

0.001

-5.109

11.5383

0.01

-14.705

67.3678

The latter is obtained by averaging the reward obtained over the last generation and over 10 experiments. The σ SE, the standard deviation of the
rewards in the last generation is also provided. The case ent_coef
equal to 0.001 has the highest mean objective SE and a high σ SE signifying potential for improvement for longer runs

