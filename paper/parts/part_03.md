# Часть 3: с. 6–7

[с. 6]
2105

Assessment of reinforcement learning algorithms...

to 40,000 iterations) done is set to True and the algorithm
terminates (lines 19 to 23). Then the last policy is returned
(line 24).
Algorithm 1 Pseudocode for proximal policy optimization
(PPO).
1: •Set
algorithm’s
hyper-parameters
( n_steps , ent_coef , VF_coef , noptepochs ,,γ ,
LR ,λ, nminibatches , max_norm , condition )
2: •Initialize the environment (i.e., input variables, reward, action, and
observation space)
3: •Initialize the neural network parameters
4: •Set done = False
5: •Set k = 0
6: while not done do
7:
for Agent j = 1,..., ncores do
8:
for p = 1,..., n_steps do
9:
•An action is sampled from the current policy a p ∈ A ∼
πθk
10:
•Action a p is evaluated by the environment and a reward
r p is returned
11:
•A new state s p ∈ S is observed and the state is set to s p
12:
end for
13:
end for
14:
•The cumulative reward Rk is evaluated with τ equal to
ncores × NF and γ
15:
•The advantage function Âk is estimated via GAE with λ and γ
16:
•The neural network parameters (θk ) are updated by stochastic gradient ascent (for noptepochs steps, with learning
rate LR , maximum value for the gradient max_norm , with
nminibatches batches) such that:
ncores n_steps −1
θk+1 ∈ arg max
θ

1





ncores × n_steps

i=1

τ =0

πθ (aτ,i |sτ,i ))
(
Aπ (aτ,i , sτ,i ), g ∗ (, Aπθk (aτ,i , sτ,i ))
πθk (aτ,i |sτ,i ) θk

− VF_coef (V πθ (sτ,i ; θ) − Ri (τ ))2 ) + ent_coef × H (θ)
17:
•k = k + 1
18:
if condition then
19:
•Set done = True
20:
end if
21: end while
22: •Return πθ Ngen

(1 + )A if A ≥ 0
.
(1 − )A if A < 0
The most influential hyper-parameters will be studied in
Appendix A. The first hyper-parameter is the shape of the
reward. The reward drives the search towards an influential
area of the search space. It is going to be studied in Appendix
A.1. Another hyper-parameter is the length of the episode τ
or NF in this work. Its role in the exploration/exploitation
trade-off will be unraveled in Appendix A.2. A higher value
will render the learning more difficult as more loading design
must be optimized, but it might allows the agents to explore
where g ∗ (, A) = {

more how the search space behaves. Another fundamental
parameter is n_steps , which corresponds to the number
of actions each agent will perform before one optimization
step. Thus the value obtained by multiplying n_steps with
the number of agents is the number of steps before θ is
updated. It controls, therefore, the estimation of the gradient of the PPO loss. This parameter has a large influence on
the quality of the best pattern found as it plays a major role
in the exploration/exploitation trade-off of RL by controlling the estimation of the gradient of the PPO’s loss. The last
hyper-parameter is ent_coef . The latter plays a role in the
exploration/exploitation trade-off as it influences the contribution of the entropy term in (3). A lower value will increase
the exploitation, which will be studied in Appendix A.4.
We have seen in this section the main motivation behind
the development of PPO as well as the major hyperparameters that characterize it. The question then becomes
how can we apply it to solve our problem? The first step is
to analyze how RL was applied to similar problems in the
realm of CO, which is the topic of Section 3.

3 Related works and classical applications
of RL to CO problems
Deep RL has been applied to solve optimization for more than
two decades [23]. Nevertheless, the application to large-scale
problems specifically large-scale CO [34] is more recent, and
we will focus on the latter literature for the review, as loading pattern optimization falls into this class. CO problems
are by essence extraordinarily hard to solve, in that they
are NP-hard problems. For instance, solving the TSP with
Exact methods requires dynamic programming. The global
solution is obtained in O(n 2 2n ) (called Held-Karp algorithm
[35]), much lower than n! obtained by enumerating all possible permutations. It is still very high, and preemptive from
applicability for real-world large-scale problems. Deep learning and in particular deep RL are frameworks that do not
work with analytical representation of an objective function
but with objects (e.g., function approximator) that are constructed statistically with a large number of data and then
mathematically optimized. The following characteristics are
generally necessary to solve the CO problems:
1. An objective function and a reward associated (e.g., sum
of partial costs or differences between two solutions)
2. A neural architecture (e.g., Feedforward, Graph, pointer
networks...)
3. A decision or MDP formulation (either a partial solution
or a complete solution is available at each step)
4. An algorithm used to solve the problem (e.g., A3C,
DQN...)

123

[с. 7]
2106

A large literature exists [17, 34], in which authors are solving different canonical problems (e.g., Traveling Salesman
(TSP) or Knapsack Problem (KP)). In [16], the authors are
using a Graph embedding called structure2vec [36], Deep Qlearning, and fitted Q-iteration to solve typical CO problems:
(MVC, MAXCUT, and TSP). Expressing these problems as
a Graph, they are learning which node (e.g., a city) is going
to be selected for each new action (decision) and the reward
is the sum of the partial tour formed at each step. In [15], they
are leveraging a policy gradient with critic to train a recurrent policy network (in particular a pointer network [37]) that
predicts the optimal tour in the TSP with the reward being
the negative total tour length and the item distribution for the
Knapsack. Similarly, in [38], they are solving the TSP vehicle
routing by policy gradient (REINFORCE [29] and A3C [39]
for the stochastic version of VRP), with a simplified version
of the pointer network. A mixture of Monte-Carlo tree search
and deep RL is proposed in [40] to solve the TSP, where the
graph defined by the cities is represented by the tree, which
policy is updated depending on a value function trained by
RL. There, the reward is equal to r (st+1 ) = c(st ) − c(st+1 ),
the difference between the previous solution and the new
one. Based on the same idea, [41] utilized policy gradient for
solving problems involving permutation but does not yet generalize well, while [42] is utilizing it with graph embedding
instead of a pointer network to learn good heuristics for the
TSP and VRP on different instance sizes. In these works, the
weights are trained to generate solution end-to-end of unseen
instances of problems at inference rather than restarting the
training every time a new instance is studied [34]. However,
the end-to-end inference strategy in [17] is not implementable
when the objective function is time-consuming to evaluate
[43], which is the case for the problem at hand [21].
Another different approach includes [44], which combined
value-based iteration with Mixed-Integer-Programming, which
exploits the combinatorial structure of the problem at hand, to
define a deterministic policy that is evaluated by solving the
optimal Bellman equation applied to the Capacitated Vehicle
Routing Problem (CVRP). They compete with state-of-theart RL approaches but are only solving one problem at a time,
which contrasts to the previous works cited where multiple
instances are solved at once [34]. Their idea is also limited
to the existence of a functional form of the problem, which
cannot be of use in this work [21].
However, the closest application of deep RL to core optimization can be found in [19] where the authors made the
parallel between optimizing a nuclear fuel assembly and the
classical application of RL to games, in which fuel designer
tactics are implemented as rules of a game RL agents are trying to solve. With the help of expert rules, the authors found
that RL outperforms classical heuristics methods such as GA
and SA when the problem becomes large and challenging,
which is the case for core optimization as well. In [45], the

123

P. Seurin and K. Shirvan

authors coupled RL and Evolutionary Strategy (ES) to solve
the multi-zone BWR bundle optimization. RL was pivotal
for narrowing down the search space in high-quality regions
to inform ES with candidate solutions, where ES then diversified the search, improving the number of feasible candidate
designs from 14 (RL standalone) to 82. In these works, however, no study of the significance of the RL hyper-parameters
was conducted and it is unclear why RL behaves better than
SO-based approaches. They would therefore benefit greatly
from an understanding of the behavior of the latter to be able
to apply RL optimally for large-scale constrained engineering problems.
Following up on these promising works, we derived a
framework in which agents are trained to build a LP for PWR
optimization. The agents will sequentially construct different
LPs by choosing the arrangement of FAs in the core, as well
as their compositions. The reward will be based on an objective function that the core designer aims to maximize: the
objective function will contain the LCOE and key safety and
operational constraints. This approach differs from heuristicbased methods, in which actions would be taken randomly,
while here the actions depend on the understanding of the
objective space from the agents. Such added physical insights
will likely lead to better solutions.
The next Section 4 will derive an RL-compliant formulation of the loading pattern optimization problem, define
proper action and state spaces, present the experimental setup
or the core design studied, as well as the reward for the problem at hand,.

4 RL algorithmic’s assessment on the core
optimization problem
4.1 Markov decision process (MDP) for the core
loading pattern optimization
The loading pattern optimization problem can be solved by
casting the problem with an appropriate formulation. One
such formulation is the Markov Decision Process (MDP). A
(discounted) MDP is a tuple M = (A, S, γ , p, r ), where
A is the action space, S is the state space, γ is a discount
factor, p is a transition probability with Markov Property:
p(st+1 |s, a) = p(st+1 |s = st , a = at ) (each state depends
only on the previous state). An MDP generates a history
H = (s0 , a0 , ..., sτ , aτ ), where τ is the episode length. A policy π = (d1 , ...) is a sequence of decision rules di : S− > A.
Solving the MDP corresponds to finding a policy π  that
solves maxπ V π (s0 ) as described in Section 2.2. In the literature for solving canonical CO problems such as the Traveling
Salesman Problem (TSP), the Maximum Cut Problem (MaxCut), the Bin Packing Problem (BPP), the Minimum Vertex
Cover (MVC), or even the Maximum Independent Set (MIS),

