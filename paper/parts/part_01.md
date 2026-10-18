# Часть 1: с. 1–3

[с. 1]
Applied Intelligence (2024) 54:2100–2135
https://doi.org/10.1007/s10489-023-05013-5

Assessment of reinforcement learning algorithms for nuclear power
plant fuel optimization
Paul Seurin1 · Koroush Shirvan1
Accepted: 8 September 2023 / Published online: 29 January 2024
© The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024

Abstract
The nuclear fuel loading pattern optimization problem belongs to the class of large-scale combinatorial optimization. It is also
characterized by multiple objectives and constraints, which makes it impossible to solve explicitly. Stochastic optimization
methodologies including Genetic Algorithms and Simulated Annealing are used by different nuclear utilities and vendors
but hand-designed solutions continue to be the prevalent method in the industry. To improve the state-of-the-art, Deep
Reinforcement Learning (RL), in particular, Proximal Policy Optimization is leveraged. This work presents a first-of-akind approach to utilize deep RL to solve the loading pattern problem and could be leveraged for any engineering design
optimization. This paper is also to our knowledge the first to propose a study of the behavior of several hyper-parameters
that influence the RL algorithm. The algorithm is highly dependent on multiple factors such as the shape of the objective
function derived for the core design that behaves as a fudge factor that affects the stability of the learning. But also an
exploration/exploitation trade-off that manifests through different parameters such as the number of loading patterns seen by
the agents per episode, the number of samples collected before a policy update nsteps , and an entropy factor ent_coef
that increases the randomness of the policy during training. We found that RL must be applied similarly to a Gaussian Process
in which the acquisition function is replaced by a parametrized policy. Then, once an initial set of hyper-parameters is found,
reducing nsteps and ent_coef until no more learning is observed will result in the highest sample efficiency robustly
and stably. This resulted in an economic benefit of 535,000 - 642,000 $/year/plant. Future work must extend this research to
multi-objective settings and comparing them to state-of-the-art implementation of stochastic optimization methods.
Keywords Fuel loading pattern · Optimization · Reinforcement learning · Proximal policy optimization

NF
PPO
RL
VF_coef
ent_coef
n_steps
LR
Clip or 
noptepochs

Proximal Policy Optimization
Reinforcement Learning
Value Function Coefficient
Entropy Coefficient
Number of steps per agent before
parameter update
Learning Rate
Clipping range
Number of epoch to run the gradient
ascent

B Koroush Shirvan

kshirvan@mit.edu
Paul Seurin
paseurin@mit.edu

1

Massachusetts Institute of Technology, 77 Massachusetts
Avenue, Cambridge, MA 02139, USA

123

LP
NF A
FAs
BP
CRD
NPP
CO
SO
NT
FT
SE
HT
MDP
FOM

Numframes: Number of pattern generated per episode
Loading Pattern
Number of fuel assemblies in the core
Fuel Assemblies
Burnable Poison
Control Rod
Nuclear Power Plant
Combinatorial Optimization
Stochastic Optimization
Nemenyi Test
Friedman Test
Sample Efficiency
Hypothesis Testing
Markov Decision Process
Figure of Merit

[с. 2]
Assessment of reinforcement learning algorithms...

1 Introduction
The commercial Nuclear Power Plants (NPP)s in the USA,
comprised of Pressurized Water Reactors (PWR)s and Boiling Water Reactors (BWR)s, represent the largest single
source of carbon-free energy in the country, generating
20% of the electricity use year-round. Nevertheless, existing power plants are threatened to shut down early as they
fail to be economical against alternative ones such as gas
power plants or heavily subsidized solar and wind. Optimizing the fuel cycle cost via the optimization of the core
Loading Pattern (LP) is one way of combating this lack of
competitiveness. The loading pattern optimization problem
aims to optimize the fuel cycle cost which accounts for 2030% of the total cost of electricity generation for the existing
fleet [1] while meeting operational, regulatory, and safety
goals. For the remainder of the paper, the notation LCOE
(Levelized Cost of Electricity) refers to the fuel cycle cost.
To solve this problem, a reactor designer must choose a set
of Fuel Assemblies (FAs) to refuel its reactor. A reactor is
fueled with a certain number of solid FAs of two types to
choose from: either fresh or burned. The burned FAs (about
two-thirds of them) have already been in the core for a certain period (here about 18 or 36 months), while the fresh FAs
have not. There is also a discrete choice of fresh FAs (which
corresponds to a discrete set of input parameters such as
the average enrichment of the fuel). This problem, therefore,
belongs to the class of Combinatorial Optimization (CO),
which is a sub-field of applied mathematics combining techniques to solve problems over discrete structures. Without a
suitable objective function, combinatorial problems require
evaluations of all possibilities to ensure a global optimum is
found.
For the loading pattern optimization, the size of the state
space and the time to evaluate one candidate solution makes
it prohibitive to utilize brute force enumeration. Furthermore,
in this application, a closed-form objective function and
analytical derivatives are not accessible. As such, Stochastic Optimization (SO) with heuristic methods has prevailed.
Simulated Annealing (SA) and Genetic Algorithm (GA) are
utilized to drive the search in [2, 3] and [4] respectively.
Ant Colony System (ACS), Particle Swarm Optimization
(PSO), Cross-Entropy (CE), Population-based Incremental
Learning (PBIL), and Artificial Bee Colonies (ABC) were
also successfully leveraged [5–7], while hybrid methods
employing Quantum Evolutionary Algorithm (QEA) and
Max-Min Ant System (MMAS) are utilized coupled with
Tabu Search (TS) in [8, 9], respectively. This list is however
non-exhaustive.
Other classes of methods leverage Deep Learning from
which Deep Reinforcement Learning (RL) also originates.
Deep learning was experimented in [10, 11] for a PWR or [12]
for a BWR, in which the authors utilized pre-trained neural

2101

networks to reduce the computational burden of evaluating
a pattern candidate in their algorithms. The deep models can
take as input the composition of what is contained inside
a nuclear reactor, specifically the FAs. For instance, two
important parameters namely the ke f f (the effective neutron
multiplication factor, which is a measure of the change in the
fission neutron population in a multiplying system with leakages) and the power fraction are predicted by a single layer
neural network in [10] from the fuel assembly distribution in
the core, which was trained with 2000 randomly generated
LPs. Then a GA leverages this surrogate to evaluate candidates during the optimization of the Almaraz Power Plant in
Spain. This resulted in the reduction of the computing time
by a factor of 60. Nonetheless, there are several limitations in
these papers: the Figures of Merits (FOMs) utilized for training are the only ones possible for optimization, which limits
the surrogate application [10]. Furthermore, it is known that
after using a surrogate, the best pattern found must be handoptimized because of the surrogate modeling discrepancy
[3]. Very recently in [11], two neural networks were pretrained on almost 140,000 data points with almost 60,000
validating data points to predict ke f f and another important
parameter the power peak factor (ppf), respectively. The neural network-based optimization (accompanied with various
heuristics such as GA or PSO) only spent 0.7% of the computing time compared with using a reactor physic code. In
spite of checking the accuracy of the trained model on new
data points generated during the optimization to ensure the
soundness of the model developed (which remained low), it
took about 98 and 120 hours to pre-train the networks. Nevertheless, many more parameters must be considered for a
real-world loading pattern optimization. This large training
time and low accuracy on test data are evident impediments
to seamless scaling to more FOMs.
Instead of replacing the core simulator, screening procedures could be utilized to improve the search process
efficiency. In [13] a dynamically trained Neural Network was
partially used as a screening procedure by evaluating a subset
of the FOMs to screen out poor quality patterns accounting
for errors in the surrogate, while a GA drives the search. In
[14], a neural network and two GAs are coupled to solve
LP design and the Burnable Poison (BP) assignment for the
TMI-1 core. BPs are utilized in FAs to control the excess of
power during the early operational cycle of a nuclear reactor
before refueling. The Beginning of Cycle (BOC) k∞ (the infinite neutron multiplication factor, which is a measure of the
change in the fission neutron population in an infinite multiplying system (e.g., reflected assembly) from one neutron
generation to the subsequent generation) for each assembly
is used to predict core parameters for the LP design problems, while BP design data are also used for the BP design
problem. Two networks are trained for each problem, one
being utilized as a fine filter while training only on solutions

123

[с. 3]
P. Seurin and K. Shirvan

2102

with higher fitness. This substantially increases the number
of good candidates’ pattern evaluations but is limited by the
target FOMs trained to be represented by the surrogate, and
the network has to be somehow dynamically retrained with
the generated candidate to avoid failed extrapolation and poor
accuracy.
On the other hand, Deep RL has been applied to solving
CO Problems somewhat differently. For instance, in [15–
17], RL learning agents are optimizing by taking sequential
decisions to build a candidate solution while receiving information (also known as reward signals) on the quality of
solutions that it produces. The decisions could be which city
to travel to next, and the reward be the length of a partial
tour in case of the Traveling Salesman Problem (TSP). The
trained network effectively learns the anatomy of a class of
problems (e.g., all possible TSP with N-city distribution in
([0, 1]2 ) N with 20 to 100 cities [15]), and can solve the ones
with similar underlying structures in a matter of seconds [17].
The network does not replace the computer program as utilized by the works mentioned in representing the pattern but
infers how to construct the most optimal one. The neural networks output a set of action values rather than FOMs, which
translates which actions to take to maximize the reward or
objective function, which itself embeds the FOMs. Moreover,
the network is learning a screening procedure online, while
other methods require the careful preparation of datasets in
advance. Previous works related to core optimization utilizing RL include [7], in which Q-learning was leveraged to
inform a “global updating rule" in an Ant Colony System
(ACS), and in [18] to automate revision rule-sets translated
into a procedural language that a recurrent neural network
can produce. However, the closest application of deep RL
to core optimization can be found in [19] where the authors
made the parallel between optimizing a nuclear fuel assembly and the classical application of RL to games, in which
fuel designer tactics are implemented as rules of a game RL
agents are trying to solve. With the help of expert rules, the
authors found that RL outperforms classical heuristics methods such as GA and SA when the problem becomes large and
challenging, which is the case for core optimization as well.
In this work, agents are trained to build a LP for PWR
optimization. The agents will sequentially construct different LPs by choosing the arrangement of FAs in the core, as
well as their compositions. The reward will be based on an
objective function that the core designer aims to maximize:
the objective function will be a scalar value which contains
the LCOE and key safety and operational constraints. SIMULATE3 [20], a reactor physic code with licensing grade
accuracy, will be utilized to obtained the figure of merits
of interests. This paper studies the set of hyper-parameters
that enable the agents to uncover high-quality LPs from the
ground up in a reasonable amount of time. The main novelties
of this work are listed as follows:

123

• Propose a novel and innovative Deep RL-compliant
framework to optimize large-scale constrained problems
and employ it to the core loading pattern optimization,
becoming the first application of deep RL to this problem.
• Provide a parameter sweep to tune hyper-parameters for
RL, an intuition behind the behavior in response to a
change in these parameters, and understand the role of
exploration/exploitation trade-off in the defined problem.
• Utilize the Levelized Cost of Electricity (LCOE) to rigorously assess the true economic performance of the
different algorithm configurations.
The framework developed in this work is an extension of a
work presented at the PHYSOR conference held in Pittsburgh
in 2022 [21], and is currently being utilized by Constellation (formerly known as Exelon) Corporation, a leading
U.S. nuclear electric power generation company. There, a
simple hyper-parameter study applied to our problem was
conducted. Nevertheless, here we prolong this study by deriving a problem-agnostic approach to obtain a sample efficient
method to apply RL, which also extends to any engineering
design problem. We however only deal with single-objective
optimization. A multi-objective version of this work was also
presented at the International Conference on Mathematics
and Computational Methods Applied to Nuclear Science and
Engineering (M&C 2023) [22].
In Section 2 the theory of RL with the motivation behind
the development of Proximal Policy Optimization (PPO)
(Section 2.2) as well as its major hyper-parameters (Section
2.3) are given. Related works are presented in Section 3. In
Section 4, the formulation of the loading pattern optimization
in an RL-compliant setting and the description of the problem which will be used to illustrate the efficacy of this novel
method are presented. The results are given in Section 5 with
a summary of the findings in this work in Section 5.2, and
an application of the method derived is applied to classical
benchmarks in Section 5.3. Lastly, Section 6 will conclude
this work and present guidance for future studies.

2 Reinforcement learning
2.1 Definition
Neuro-Dynamic Programming or Deep Reinforcement
Learning (RL) [23] is a class of Machine Learning algorithm
that emerged from exact dynamic programming methods for
high dimensional problems that suffer from daunting computational requirements. The RL framework is characterized
by a trial and error scheme between the generation of experiences by one or several agents taking decisions (or actions),
and the improvements of these decisions over time, with the
help of a reward signal produced by an emulator for games

