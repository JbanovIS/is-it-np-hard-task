# Часть 2: с. 4–5

[с. 4]
2103

Assessment of reinforcement learning algorithms...
Fig. 1 Classical RL iteration
procedure. The policy is
computed through a neural
network in the figure. Each
agent is following the same
policy. The reinforcement
mechanism is the algorithm
(here PPO) that updates the
parameter θ based on the
agents’ experiences

or an objective function in case of optimization. Figure 1
summarizes the procedure:
One or several agents in parallel are trained to take a
sequence of actions a ∈ A from observable states s ∈ S
following a policy: a ∼ π(·, s; θk ), where θk is a learnable parameter to improve this sequence. A policy π =
(d1 , ...) is a sequence of decision rules di : S− > A,
which represents the probability of taking action a ∈ A
being in state s ∈ S. It specifies which action to take
when in state s. Each action a ∈ A taken after observing a state s ∈ S generates a reward r (s, a) ∈ R or
r (s, a) ∈ R N in case of multi-objective RL. The number
of actions taken, also named the length of an episode or the
horizon, is denoted τ . Over the course of an episode, a history H = 
(s0 , a0 , ..., sτ ) is generated, on which the sum
of rewards τt=0 rt (at , st ) must be maximized. The quality
of the sequence is then defined through a value- or stateτ r (s , π (s )))
action value function 
V πθ (s; θ ) = EH (t=0
t
θ t
π
or Q θ (s, a; θ ) = E( t≥0 r( st , at )|s0 = s, a0 = a, at =
πθ (st )) (where V πθ (s0 ; θ ) = Q πθ (s0 , πθ (s0 ); θ )) respectively. The value function V πθ (s) is the expected sum of
rewards following a certain policy πθ being in state s, while
the action value function Q πθ (s, a) is the expected sum of
rewards taking action a being in this state going forward. If
the optimum policy π  is found, following it would result in
the highest value function. The classical formulation of the
RL problem starting from an initial state s0 then becomes:

architectures to represent the value function and the policy. We will use the RL notation to denote both RL and
deep RL interchangeably. Therefore θ could represent the
weights in a neural network. The power of the RL mechanism lies in the possibility to exceed expert knowledge
by training a policy based on a reward signal [24]. Nevertheless, if the policy is poorly parameterized, or if the
experiences are not representative of the search space, the
policy will perform inadequately [24]. The latter is called
the exploration/exploitation trade-off. A sufficient amount
of exploration is necessary for the agents to get a proper representation of the search space, such that they can properly
optimize their decisions during the exploitation phase.

τ γ t r (s , a )) = Q πθ (s , π (s ); θ ) = V πθ (s ; θ)
max EH (t=0
t t
0 θ 0
0

where is the manifold of smoothly parametrized policies.
Policy-based algorithms have the advantage of simplicity
by having fewer hyper-parameters to tune and also scale well
for parallel computing. There are three types: tabular policy iteration, derivative-free optimization (e.g., covariance
matrix adaptation (CMA), Cross Entropy Method (CEM)...),
and policy gradients [27]. Tabular policy-iteration-based
approach cannot be leveraged due to the size of our search
space. Derivative-free optimization approaches suffer from
low sample complexity meaning that it requires more samples to collect (i.e, objective function evaluation) to obtain

θ

subjectto at = π(st ; θ )

where γ ∈ [0, 1] is a hyper-parameter added to favor shortterm reward if closer to 0, which translates the appeal that
early returns are more important than long-term ones (e.g,
early return on investment are more attractive to investors).
Additionally, it helps make the problem mathematically
sound (e.g., prevents the cumulative reward to explode).
Deep RL will refer to RL methods that utilize deep learning

2.2 Theory behind solving an RL problem
There are two types of algorithms to solve this optimization:
value iteration and policy iteration. The former class of methods benefited from many improvements [25] and is widely
used, but they were inferior to policy-based algorithms in
particular Proximal Policy Optimization (PPO) [26] in our
application. Policy iteration is based on optimizing the policy directly by a parameterization π(·, ·|θ ). The problem to
solve becomes
max V (π(·|θ ))

π(·|θ)∈

123

[с. 5]
P. Seurin and K. Shirvan

2104

satisfying result and they do not behave well for large problems [27]. This was one of the motivation for introducing
advanced sample efficient (defined in [28] as "The amount
of data required for a learning system to attain any chosen target level of performance") gradient-based methods
which already demonstrated superiority on supervised learning tasks in many instances [27]. In the original policy
gradient method, the parameter θ is updated by policy gradient ascent with the relation:

θt+1 = θt + ηt ∇θ V (π(θ ))

(1)

τ R(τ )∇ log π (a |s ))). This
where ∇θ V (π(θ )) = EH (t=1
θ
θ t t
formulation translates the fact that directions with high
 −1 
τ −1 t  −t
expected returns R(τ ) = τt=0
γ rt or R(τ ) =
γ
rt 

t =t
will be pushed with greater magnitude. The estimate of the
gradient can be obtained by Monte-Carlo sampling over multiple trajectories, which led to classes of methods called
REINFORCE [29]. This method suffers however from high
variance, high sensitivity to step sizes, sample inefficiencies, and unstable learning [30]. One alternative to reduce
the variance is to replace R(τ ) with the advantage function
Aπθ (s, a; θ ) = Q πθ (s, a; θ ) − V πθ (s; θ ), which represents
the additional expected return by taking action a compared
to the average expected return by taking random actions.
Nevertheless, these methods have lots of shortcomings.
Therefore much research on alternative gradient techniques
and improved loss functions were conducted. This yields a set
of new policy gradient paradigms with Conservative Policy
Iteration [31] and Natural policy gradient [32], which led to
Trust Region Policy Optimization [27] and finally Proximal
Policy Optimization (PPO) [26].
PPO was developed as an improvement of TRPO. PPO
is a trade-off between simplicity of implementation, tuning,
and Sample Efficiency (SE). It is a major concern for RL, as
the amount of data in real world problems is usually scarce
per unit of computing time. This is the case in this work
because of the slow time of the physics simulation software.
Therefore the optimization techniques developed are primarily aimed at increasing this SE [30]. For this purpose, PPO
relies on a clipping term and a learning rate to scale up to massive parallelism, which TRPO was struggling to do [26]. The
PPO version utilized in this work is the first-order constraintfree clipping loss method, where the clipping plays the same
role as the KL divergence in TRPO [27], ensuring that the
policies between updates are close enough to each other
and avoid catastrophic losses of performance. For the latter,
if rt (θ ) = ππθ θ is the probability ratio, the new surroold
gate objective (presented as a loss) to optimize is a clipped

123

objective:
L cli p (θ ) = E(min(rt (θ )A(θ ), clip(1−, 1+, rt (θ ))A(θ )))
(2)
where  is an hyper parameter, which guarantee to penalize large policy updates. Indeed, it prevents the probability
ratio to lies outside [1 − , 1 + ]. Moreover, as the advantage estimation Aπθ (s, a; θ ) was used, another value loss
L V F (θ ) = (V πθ (st ; θ ) − Vtarget (st ))2 was introduced to
ensure a proper approximation of the value function (which is
used in the Generalized Advantage Estimation (GAE) to estimate Aπθ (s, a; θ ) [26]). Lastly, an entropy term H (θ ), which
corresponds to the entropy of the policy distribution, was
introduced to enhance exploration. The final loss becomes:
L f inal (θ ) = E(L cli p (θ ) − c1 L V F (θ ) + c2 H (θ ))

(3)

where c1 and c2 are hyper-parameters (given by vf_coef
and ent_coef in stable-baselines [33], respectively).

2.3 Proximal policy optimization hyper-parameters
To understand the role of the hyper-parameters studied in
Appendices A and B and summarized in Section 5.2, we first
need to understand how PPO works. PPO [26] is based on
policy improvement by pessimistic lower bound maximization. It is built on top of TRPO and relies on a clipping term
and a learning rate, while TRPO relies on a complex secondorder method to ensure policy improvement, as discussed in
Section 2.2. A pseudo code for the classical PPO training is
detailed in Algorithm 1.
A set of hyper-parameters is first defined and the environment (e.g., reward, state, and action spaces), as well as the
learning parameters, are initialized (e.g., weights of a neural
network). The algorithm runs as long as a termination criterion has not been reached (e.g., number of generations).
PPO is executed in parallel with ncores . Before a parameter update, each agent (corresponding to each core) generates
n_steps trajectories by taking actions and observing states
(lines 7 to 13 in Algorithm 1). The notation NF stems from
Numframes and corresponds to the length of an episode,
which will be explained in Section 4.1. Then the different
inputs to the PPO surrogate objective must be evaluated. The
cumulative reward R(τ ) is evaluated (line 14) to calculate
the value function loss, and the variance-reduced advantagefunction estimators Â is estimated for the clipped portion of
the objective (line 15). Then the networks’ parameters of the
policy (θ) are updated thanks to a Monte-Carlo estimate of
the surrogate loss (lines 16 to 18). Then, a counter k is incremented and if a pre-defined condition is reached (e.g, k equal

