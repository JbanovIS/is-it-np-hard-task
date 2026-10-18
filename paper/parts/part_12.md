# Часть 12: с. 30–33

[с. 30]
2129

Assessment of reinforcement learning algorithms...

Fig. 16 Evolution of the Mean Score per episode (left) and Max Objective (right) overall found by the agents for the noptepochs study

the left of Fig. 16 seems to indicate a random local drop in
performance at the last generation for case 20, which may
be due to the randomness of the policy, because it is clear
from Fig. 16 that it has not converged yet. Table 22 seems
to hint about why higher noptepochs leads to higher σ SE.
The clipfrac increases with noptepochs . This might
be explained by the fact that the policy is more different
with more steps in the gradient ascent, hence increasing the
likelihood of changing the policy more. Therefore, the steps
taken are less controlled yielding instability in learning. As a
consequence, the entropy remains high (see Table 22) and the
policy remains more random. The sweet spot is then between
5 and 10.
Only the case 5 competed with the default case 10, but the
differences were not significant enough and we decided to
not delve into any more study.
B.5 nminibatches study
nminibatches (line 16 or Algorithm 1) is the number of
mini batches used in training during a step of the algorithm.
Essentially, the size of the batches for training is equal to
n_steps × ncores
nminibatches

. As showcased in Fig. 17, all cases

are no observed policy learning for the case 128 and greater
values would not be possible since n_steps × ncores is
equal to the latter.
Overall, a higher value of this parameter lead to slower
learning. However, there seem to be a sweet spot for the case
equal to 4. There, the size of the batches is equal to the number of cores. Both SE measures are better even though the
case 2 found a high quality pattern with only a difference
in magnitude about 0.01 in the LCOE. It could be interesting to see what happens when the ratio

n_steps
nminibatches

is

kept constant and we left that for future work. Above 4, the
behavior seems to remain linear. Only 16 found a worse best
pattern than 32, but regarding the high σ SE of Table 23, it
must have been found randomly.

B.6  and  studies
In PPO, the advantage function is estimated via Generalized
Advantage Estimation (GAE) [26]. The latter represents an
exponential average of the advantage function with parameter λ. This estimate suffers from the bias-variance trade-off
and the λ parameter helps control it. Greater value of λ will

exacerbate a smooth learning. We stopped at 64 because there
Table 21 Figure of Merits for
the noptepochs study

noptepochs values

Best (MO)

Mean Objective SE

σ SE

1

-278.2698

-13133.0550

18291.9926

5

-4.6176

-18.0850

36.5557

10

-4.5820

-9.9267

32.6367

15

-38.1449

-1747.9683

1355.6888

20

-157.1052

-4890.5444

3636.5023

25

-156.3375

-4518.5616

4608.1392

30

-210.1378

-4894.9650

5039.9094

The default case is highlighted in red

123

[с. 31]
P. Seurin and K. Shirvan

2130

Table 22 Loss related Figure of
Merits for noptepochs

noptepochs

approx_kl

clipfrac

entropy

LC L I P

VF_loss

1

1.2905e-7

0.0

67.49082

-6.8025e-5

136777920.0

5

6.944e-4

0.0

28.1128

-8.3063e-3

42998.188

10

2.8199e-2

0.2875

44.3150

-4.0714e-2

218030.05

15

1.0937e-1

0.5615

62.2872

-9.7497e-2

2916480.0

20

1.0234e-1

0.6555

65.1677

-9.7205e-2

13611875.0

25

1.1506e-1

0.7391

65.6561

-1.1411e-1

16522170.0

30

1.1097e-1

0.7560

65.8907

-1.0928e-1

25375224.0

clipfrac is the fraction for which the probability ratio is outside the [1 − , 1 + ] range. The default
case is highlighted in red

Fig. 17 Evolution of the Mean Score per episode (left) and Max Objective (right) overall found by the agents for the nminibatches study

Table 23 Figure of Merits for
the nminibatches study

nminibatches values

Mean Objective SE

σ SE

2

-4.5918

-31.8550

95.3676

4

-4.5820

-9.9267

32.6367

8

-40.6294

-2002.2990

2694.3910

16

-99.5715

-2669.2012

2501.2163

32

-93.1650

-2900.84154

2621.0595

64

-149.1445

-4104.2863

4151.5750

128

-287.3326

-16225.4743

20260.0626

The default case is highlighted in red

123

Best (MO)

[с. 32]
2131

Assessment of reinforcement learning algorithms...

Fig. 18 Evolution of the Mean Score per episode (left) and Max Objective (right) overall found by the agents for the VF_coef study

decrease the bias of the estimator by allow greater contribution to later states (up to max( NF , n_steps ) for each
agent) at the cost of increasing the variance due to the presence of more terms. Because the length of the episode is 1,
neither λ or γ should influence the algorithm. The only differences observed by running different values must be due
to the randomness of the policies resulting in slightly different SE measures. Indeed, the advantage estimation becomes
[75]:
Aπθ (s0 , a0 ; θ ) = r0 +γ E(V (s1 ))−V (s0 ) = r0 −V (s0 ) (13)
γ is the discount factor in the cumulative reward, which is
a sum over one term. Therefore, no study are presented here.
B.7 VF_coef study
VF_coef is the weight assigned to the value function’s term
in the PPO loss of (3). The algorithm was very sensitive
to this term. It turned out that the number of samples for
this particular case in the configuration studied had a big

Table 24 Figure of Merits for
the VF_coef study

VF_coef values

impact on the figure of merits found. We used 43,000 as
the maximum number of samples. Figure 18 showcases the
evolution of the mean score per episode and max objective
for the VF_coef study.
In all cases, there is a smooth learning. Case 2 finds a feasible pattern slower than the others, as if it spent more time
exploring. It is interesting to see that, except for case 1.5, the
lower the VF_voef , the higher the mean objective SE and
the lower the σ SE as displayed in Table 24. Reducing the
impact of the value function in the loss seems to increase the
exploitation. We first hypothesized that reducing the impact
of the value function would increase the speed of the convergence of the policy loss. Therefore, we tried to find an
explaination looking at the loss FOMs such as in Table 22
via Table 25. Nevertheless, no clear behaviors were drawn.
The impact of VF_coef cannot be explained by only looking at loss-related performance metrics, especially with the
particular case 1.5. Several interesting explanation removing
case 1.5 can be however made. Comparing the entropy of case
0.2 to 1.0 versus 1.2, we can say that a lower entropy does not

Best (MO)

Mean Objective SE

σ SE

0.20

-4.6097

-5.71826

10.7914

0.5

-4.5756

-5.6684

9.6340

0.8

-4.5967

-6.2679

15.4157

1.0

-4.5820

-7.3352

25.7293

1.2

-4.6216

-11.2973

44.7394

1.5

-4.6335

-7.3875

20.6081

2.0

-4.6148

-22.6870

45.4516

0.8 + ent_coef = 0.001

4.59014

-4.863

5.4473

The default case is highlighted in red

123

[с. 33]
P. Seurin and K. Shirvan

2132
Table 25 Loss related Figure of Merits for VF_coef
VF_coef

H

LC L I P

0.2

9.0399

-0.0372

0.5

12.3117

-0.0346

872.3915

0.8

3.9508

-0.0438

573.3726

1.0

4.0087

-0.0274

1248.4656

1.2

5.7303

-0.0507

1588.7722

2.0

15.1559

-0.0135

2906.0786

0.8 + ent_coef = 0.001

0.0696

-0.0046

0.64881

VF_loss
468.7824

The default case is highlighted in red

result in a high mean objective or σ SE. Similarly, for 0.2 to
0.8, a better policy or value function loss results in a higher
mean objective SE and lower σ SE. The case 1.0 and 2.0 both
have a better policy loss but a much worse value function
loss, resulting in a lower mean objective SE and higher σ SE.
It seems that there is a trade-offs between the losses but that
the value loss has a greater impact. This is confirmed by comparing 2.0 and 1.2. 2.0 exacerbates a worse SEs even though
the policy losses improve about twice as much.
A nice trade-off could be to utilize a value of 0.8 for
VF_coef because the mean objective SE is higher than for
the case 1.0 and the best pattern found is very close. Nevertheless, the σ SE is at 15.4157 and we made the choice
of reducing the entropy in Appendix A.4, which already
reduced the σ SE with a better mean objective SE. We would
risk to reach a worse local optima if we combined it with a
lower VF_coef value. To verify that, we also ran a case with
VF_coef and ent_coef equal to 0.8 and 0.001, respectively (last row of Table 24). There, the best pattern found was

worse than the base case, and the σ SE is much lower. Keep
in mind that these hyper-parameters may be used to pursue
further study and the latter value is too low, meaning that the
algorithm was already too close to converge. Therefore, we
decided not to pursue deeper studies with this parameter or
another combination with ent_coef .

B.8 Depth and breadth of the architecture studies
The depth of the neural architecture representing the policy
corresponds to the number of hidden layer in the neural network. The breadth is the number of hidden nodes per layer.
The number of hidden nodes is equal to 64 or 32. Figure 19
showcases the evolution of the mean score and max objective
per episode of the different values of the depth and breadth
studied. In all cases there is a smooth learning. The effect on
the number of hidden layer is small compared to the other
hyper-parameters studied in this appendix. The breadth has
an impact on the learning as for each case the mean objective
SE and σ SE are lower and higher, respectively, as shown in
Table 26. The best patterns found seem to also be better for
smaller number of nodes.
Another interesting behavior is that the best patterns are
found faster when the number of hidden nodes is divided by
two as confirmed by Fig. 19. However, the mean objective
SE is smaller and the σ SE higher. In this case what might
have happened is that it took more samples for cases with
64 hidden nodes to learn to reproduce better patterns but
they managed to produce pattern closer to a better optima
because of a better understanding of the search space. The
number of hidden nodes therefore plays a role in the exploration/exploitation trade-off.

Fig. 19 Evolution of the Mean Score per episode (left) and Max Objective (right) overall found by the agents for the depth and breadth of the
architecture studies

123

