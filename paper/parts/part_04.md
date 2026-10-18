# Часть 4: с. 8–9

[с. 8]
Assessment of reinforcement learning algorithms...

the recipe for casting the problem in an MDP are similar
[34]. The state space S represents a full or partial solution,
an action a adds a node to the partial solution or perturbs
a sub-optimal one, the reward is directly related to the cost
function characterizing each problem (e.g., the cost of a partial tour or the difference between two tours in case of the
TSP), and the horizon is the number of nodes to construct a
solution or arbitrary stopping criteria if complete solutions
are perturbed at each step. The mapping between state and
action is enabled by the use of an encoder such as a recurrent
neural network (RNN), a Graph Neural Network (GNN), or
a Multi-Layer Perceptron (MLP), with sometimes the help of
attention mechanisms. See Section 3 for practical examples.
For our purposes, an action is constructing one LP. The
action space, therefore, depends on the number of FAs
available, and the complexity of the problem (i.e., decision
variables including shuffling, rotation, and pure assignment).
The state space is the space represented by all possible LPs
achievable from our choice of fresh fuels and existing burned
assemblies. A state must correspond to a unique core [10].
Consequently, the state of a core will be augmented by
a feature embedding of the physics characteristic of each
core generated (e.g., F H , BP, and enrichment of each fuel
assembly...): s ∈ S = {s i : i = 1, 2, ..., N F A }, where
s i = {s1i , ..., sdi }, where d is the embedding size of the fuel
assembly s i as will be described in Section 4.2.1. The mapping between the state and the action is enabled by one-layer
feature extractor and two hidden layers with 64 hidden units
each fully connected, which is the default fully-connected
neural network in stable-baselines.
The γ is fixed at 0.99 in this study. The transition probability is either deterministic or stochastic. In the deterministic
case, a choice of FAs will always yield the same pattern.
For the stochastic case, a choice of action can be complemented by random assignments if the action is prohibited
(e.g., a fuel assembly has already been picked). The reward
is given by the computation of the objective function derived
in Section 4.2.2, which is a testament to the quality of the
LP. The episode terminates when a certain number of LPs
Numframes ( NF ) has been generated.

2107

assemblies, 89 of which are fresh. This means that 89 will
remain in the reactor (but potentially at a different positions)
for the next operational cycle after refueling, while 16 will
remain for three cycles in total. The schematic is shown in
Fig. 2. The equilibrium cycle is obtained by applying the
same LP recursively until there is the convergence of the
physics parameters. Therefore, we know exactly how much
energy is extracted from each FA (also called exposure or burnup) and how much they cost, which is why we can express
the LCOE in $/MWh [2]. To reduce the search space, mirror
one-eighth symmetry boundary conditions are applied. This
symmetry is widely utilized for scoping analysis in literature
(as in [7–10, 12, 13]).
If the agents never receive high-quality rewards or if it
remains flat, they will never learn. To help them receive
good rewards more rapidly, certain rules to the loading pattern optimization were applied. Throughout the literature,
there are important rules/heuristics enforced. Twice-burned
FAs or assemblies with the highest exposure are placed at
the core periphery systematically [46–48] which reduces the
load on the reactor vessel (called a low leakage pattern) for
increasing its lifetime [9, 46], and improves the cycle length
(equal to the theoretical length of an operational cycle) [8,
9], lowering the fuel cycle cost [2]. It also can lower the BOC
excess of reactivity, hence the Moderator Temperature Coefficient (MTC) [8] at the same time. It is however a trade-off
with the peaking factor flattening, which will be harder to
accomplish. The MTC and peaking factors (e.g., F h ) must
remain below a threshold to ensure the theoretical safety of
the reactor. Some optimization techniques are even solely
utilizing heuristics to create a LP [18]. Imposing heuristics
can have its limitation and for this work, few of them will be
enforced, while most will be learned by the RL agents. One

4.2 Description of the problem within the RL
framework
In this section, the nuclear reactor core studied to apply the
method, the objective, and the constraints involved will be
described.
4.2.1 Description of the reactor core, action, and state space
To demonstrate the performance of the RL algorithms, a
loading pattern optimization study is performed for the equilibrium cycle of a 4-loop Westinghouse-type reactor with 193

Fig. 2 PWR core arrangement and symmetries. Elements within the
eighth symmetry (dark gray) are permuted together, while elements
on the symmetry lines (light gray) are permuted together. The center
element is chosen to have the lowest enrichment and highest BP concentration

123

[с. 9]
P. Seurin and K. Shirvan

2108
Fig. 3 Example of
transformation of a 2D core to a
1D array. The FAs in the eighth
symmetry appear first in the
array, while the element in the
quarter symmetry lines appear
second starting from the
diagonal, due to the particular
treatment needed for these
locations. The center assembly
is blurred as it does not belong
to the action space

typical rule includes putting twice-burned fuel at the periphery and preventing fresh ones from being located there. To
even out the power, a ring of fresh FAs between the in-board
and the periphery is placed. On top of that, to limit the risk
of fuel failure during Reactivity Initiated Accident (RIA), no
square of fresh FAs are allowed in the core, which is a typical
rule often enforced by the Nuclear Regulatory Commission
(NRC). Because the FAs are not homogeneously burned, they
are sometimes rotated for the next cycle. However, since the
impact of assembly rotations is relatively small [9], it is not
included in the current study. Similarly, the compositions
of the twice-burned FAs (but not locations) are fixed. The
original number of possible patterns in eighth symmetry was
∼ 1052 . Such rules, based on core design best practices,
reduce the number of possibilities to ∼ 1029 .
Each action represents a choice of a template pattern and
all the FAs that are going to be placed inside it. The action
space for the fresh fuels is constant and depends on the available fresh fuels provided by the user. Here, the fresh FAs
(14 choices for eighth symmetry) are chosen from 24 different types that are characterized by their enrichment and
BP distribution. In this work IFBA and WABA are utilized
as BP. The uranium 235 enrichment varies between 4.00 to
4.95%, the IFBA and WABA loading are discrete between
128x or 156x, and 12 or 24 guide tubes, respectively. WABAs
are placed in water rods in which control mechanisms could
be inserted in case of an emergency shutdown of the reactor. Therefore, locations under Control Rods (CRDs) cannot
hold WABA to not obstruct their insertions. Therefore a randomly sampled fresh fuel without WABA is selected if the
FA chosen by the agent for this specific location is forbidden.
It could be possible to learn to not take forbidden actions via
learning rules as in a game prior to running SIMULATE3 as
done in [49] with CASMO4e. Nevertheless, we found out
that it did not penalize the learning to simply replace forbidden by randomly sampling valid ones. The action space
must then decrease when choosing once- and twice-burned
FAs. To improve the search efficiency we need to prevent random actions to be taken [50]. For this purpose, we adopted
the MultiDiscrete option of stable-baselines to define
the action space. There, for each once- and twice- burned

123

location, the action space decreases by 1 for each new action,
which prevent forbidden action to be taken.
The new action obtained by accounting for the forbidden
actions must then be decoded before being evaluated. The
decoding is straightforward. Each entry is a location in the
2D core as shown in Fig. 3.
Each entry of the action’s vector is an integer, which corresponds to a fuel assembly. The input is spanned sequentially,
while the core locations are treated depending on their types
and locations as provided in Fig. 3. First fresh fuel locations are filled and then once- and twice-burned locations
are treated. For fresh fuel, once-, and twice-burned location
j, integer k j corresponds to the kth element of the list of
possible fresh fuel, available once-, and twice-burned FAs,
respectively. The list of possible fresh fuel is constant, while
the list of available burned assemblies decreases.
Then the state must also be defined. Initially, no pattern
were generated and the starting state is an array of zeros. As
the algorithm progresses, the starting state at the beginning
of each episode will be the embedding of the best pattern
ever found. The reason is to mimic the way a core designer
would iterate on the best pattern found as it progresses toward
finding a loading pattern by hand. The parameters chosen for
embedding are the relative position of the FAs, their enrichment, their BP’s content (IFBA or WABA), the Radial Power
Fraction (RPF), the F h , and the pin peak exposure at the End
Of Cycle (EOC) for each individual fuel assembly. For an
equilibrium cycle, the first 4 fully defined a fuel pattern and
the last 3 were added to help the agent. However, no thorough
analysis of the influence of embedding has been conducted.
The core is then evaluated following the objective function
defined in Section 4.2.2.
4.2.2 Reward construction with the objectives
and constraints
The classical formulation of an optimization problem can be
proposed as follows without loss of generality:
min f (x) = [ f 1 (x), f 2 (x), ...., f F (x)]T
x

