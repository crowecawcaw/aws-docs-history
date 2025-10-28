# Compare Amazon Braket simulators

This section helps you select the Amazon Braket simulator that is best
suited for your quantum task, by describing some concepts, limitations, and use cases.

**Choosing between local simulators and on-demand simulators
(SV1, TN1, DM1)**

The performance of _local simulators_ depends on the hardware that
hosts the local environment, such as a Braket notebook instance, used to run your
simulator. _On-demand simulators_ run in the AWS cloud and are
designed to scale beyond typical local environments. On-demand simulators are optimized for
larger circuits, but add some latency overhead per quantum task or batch of quantum tasks. This can imply a
trade-off if many quantum tasks are involved. Given these general performance characteristics, the
following guidance can help you choose how to run simulations, including ones with
noise.

For **simulations**:

- When employing fewer than 18 qubits, use a local simulator.
- When employing 18–24 qubits, choose a simulator based on the
  workload.
- When employing more than 24 qubits, use an on-demand
  simulator.
  For **noise simulations**:

- When employing fewer than 9 qubits, use a local simulator.
- When employing 9–12 qubits, choose a simulator based on the
  workload.
- When employing more than 12 qubits, use DM1.

**What is a state vector simulator?**

SV1 is a universal state vector simulator. It stores the full wave function
of the quantum state and sequentially applies gate operations to the state. It stores all
possibilities, even the extremely unlikely ones. The SV1 simulator's run
time for a quantum task increases linearly with the number of gates in the circuit.

**What is a density matrix simulator?**

DM1 simulates quantum circuits with noise. It stores the full density matrix
of the system and sequentially applies the gates and noise operations of the circuit. The
final density matrix contains complete information about the quantum state after the
circuit runs. The runtime generally scales linearly with the number of operations and
exponentially with the number of qubits.

**What is a tensor network simulator?**

TN1 encodes quantum circuits into a structured graph.

- The nodes of the graph consist of quantum gates, or qubits.
- The edges of the graph represent connections between gates.
  As a result of this structure, TN1 can find simulated solutions for
  relatively large and complex quantum circuits.

**TN1 requires two phases**

Typically, TN1 operates in a two-phase approach to simulating quantum
computation.

- **The rehearsal phase:** In this phase,
  TN1 comes up with a way to traverse the graph in an efficient
  manner, which involves visiting every node so that you can obtain the measurement you
  desire. As a customer, you do not see this phase because TN1 performs
  both phases together for you. It completes the first phase and determines whether to
  perform the second phase on its own based on practical constraints. You have no input
  into that decision after the simulation has begun.
- **The contraction phase:** This phase is analogous to
  the execution phase of a computation in a classical computer. The phase consists of a
  series of matrix multiplications. The order of these multiplications has a great
  effect on the difficulty of the computation. Therefore, the rehearsal phase is
  accomplished first to find the most effective computation paths across the
  graph. After it finds the contraction path during the rehearsal phase,
  TN1 contracts together the gates of your circuit to produce the
  results of the simulation.

**TN1 graphs are analogous to a map**

Metaphorically, you can compare the underlying TN1 graph to the streets
of a city. In a city with a planned grid, it is easy to find a route to your destination
using a map. In a city with unplanned streets, duplicate street names, and so forth, it can
be difficult to find a route to your destination by looking at a map.

If TN1 did not perform the rehearsal phase, it would be like walking
around the streets of the city to find your destination, instead of looking at a map first.
It can really pay off in terms of walking time to spend more time looking at the map.
Similarly, the rehearsal phase provides valuable information.

You might say that the TN1 has a certain “awareness” of the structure of
the underlying circuit that it traverses. It gains this awareness during the rehearsal
phase.

**Types of problems best suited for each of these types of
simulators**

SV1 is well-suited for any class of problems that rely primarily on having a
certain number of qubits and gates. Generally, the time required grows
linearly with the number of gates, while it does not depend on the number of
shots. SV1 is generally faster than TN1 for
circuits under 28 qubits.

SV1 can be slower for higher qubit numbers because it
actually simulates all possibilities, even the extremely unlikely ones. It has no way to
determine which outcomes are likely. Thus, for a 30-qubit evaluation,
SV1 must calculate 2^30 configurations. The limit of 34
qubits for the Amazon Braket SV1
simulator is a practical constraint due to memory and storage limitations. You can think of
it like this: Each time you add a qubit to SV1, the problem
becomes twice as hard.

For many classes of problems, TN1 can evaluate much larger circuits in
realistic time than SV1 because TN1 takes advantage of the
structure of the graph. It essentially tracks the evolution of solutions from its starting
place and it retains only the configurations that contribute to an efficient traversal. Put
another way, it saves the configurations to create an ordering of matrix multiplication
that results in a simpler evaluation process.

For TN1, the number of qubits and gates matters, but the
structure of the graph matters a lot more. For example, TN1 is very good at
evaluating circuits (graphs) in which the gates are short-range (that is, each
qubit is connected by gates only to its nearest neighbour
qubits), and circuits (graphs) in which the connections (or gates) have
similar range. A typical range for TN1 is having each qubit
talk only to other qubits that are 5 qubits away. If most of
the structure can be decomposed into simpler relationships such as these, which can be
represented in _more_, _smaller_, or _more
uniform_ matrices, TN1 performs the evaluation efficiently.

**Limitations of TN1**

TN1 can be slower than SV1 depending on the graph's
structural complexity. For certain graphs, TN1 terminates the simulation
after the rehearsal stage, and shows a status of `FAILED`, for either of these
two reasons:

- **Cannot find a path** — If the graph is too complex,
  it is too difficult to find a good traversal path and the simulator gives up on the
  computation. TN1 cannot perform the contraction. You may see an error
  message similar to this one: `No viable contraction path found.`
- **Contraction stage is too difficult** — In some
  graphs, TN1 can find a traversal path, but it is very long and
  extremely time-consuming to evaluate. In this case, the contraction is so expensive
  that the cost would be prohibitive and instead, TN1 exits after the
  rehearsal phase. You may see an error message similar to this one: `Predicted
runtime based on best contraction path found exceeds TN1 limit.`

###### Note

You are billed for the rehearsal stage of TN1 even if contraction is
not performed and you see a `FAILED` status.

The predicted runtime also depends on the shot count. In worst-case
scenarios, TN1 contraction time depends linearly on the shot
count. The circuit may be contractable with fewer shots. For example, you
might submit a quantum task with 100 shots, which TN1 decides is
uncontractable, but if you resubmit with only 10, the contraction proceeds. In this
situation, to attain 100 samples, you could submit 10 quantum tasks of 10 shots for
the same circuit and combine the results in the end.

As a best practice, we recommend that you always test your circuit or circuit class with
a few shots (for example, 10) to find out how hard your circuit is for
TN1, before you proceed with a higher number of
shots.

###### Note

The series of multiplications that forms the contraction phase begins with small, NxN
matrices. For example, a 2-qubit gate requires a 4x4 matrix. The
intermediate matrices required during a contraction that is adjudged to be too difficult
are gigantic. Such a computation would require days to complete. That is why
Amazon Braket does not attempt extremely complex contractions.

**Concurrency**

All Braket simulators give you the ability to run multiple circuits concurrently.
Concurrency limits vary by simulator and region. For more information on concurrency
limits, see the [Quotas](braket-quotas.md "braket-quotas.md") page.
