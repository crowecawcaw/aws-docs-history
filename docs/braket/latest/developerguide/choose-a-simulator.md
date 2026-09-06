

# Compare Amazon Braket simulators
<a name="choose-a-simulator"></a>

This section helps you select the Amazon Braket simulator that is best suited for your quantum task, by describing some concepts, limitations, and use cases.

 **Choosing between local simulators and on-demand simulators (SV1, DM1)** 

The performance of *local simulators* depends on the hardware that hosts the local environment, such as a Braket notebook instance, used to run your simulator. *On-demand simulators* run in the AWS cloud and are designed to scale beyond typical local environments. On-demand simulators are optimized for larger circuits, but add some latency overhead per quantum task or batch of quantum tasks. This can imply a trade-off if many quantum tasks are involved. Given these general performance characteristics, the following guidance can help you choose how to run simulations, including ones with noise.

For **simulations**:
+ When employing fewer than 18 qubits, use a local simulator.
+ When employing 18–24 qubits, choose a simulator based on the workload.
+ When employing more than 24 qubits, use an on-demand simulator.

For **noise simulations**:
+ When employing fewer than 9 qubits, use a local simulator.
+ When employing 9–12 qubits, choose a simulator based on the workload.
+ When employing more than 12 qubits, use DM1.

 **What is a state vector simulator?** 

 SV1 is a universal state vector simulator. It stores the full wave function of the quantum state and sequentially applies gate operations to the state. It stores all possibilities, even the extremely unlikely ones. The SV1 simulator's run time for a quantum task increases linearly with the number of gates in the circuit.

 **What is a density matrix simulator?** 

 DM1 simulates quantum circuits with noise. It stores the full density matrix of the system and sequentially applies the gates and noise operations of the circuit. The final density matrix contains complete information about the quantum state after the circuit runs. The runtime generally scales linearly with the number of operations and exponentially with the number of qubits.

 **Types of problems best suited for each simulator** 

 SV1 is well-suited for any class of problems that rely primarily on having a certain number of qubits and gates. Generally, the time required grows linearly with the number of gates, while it does not depend on the number of shots.

 SV1 can be slower for higher qubit numbers because it actually simulates all possibilities, even the extremely unlikely ones. It has no way to determine which outcomes are likely. Thus, for a 30-qubit evaluation, SV1 must calculate 2^30 configurations. The limit of 34 qubits for the Amazon Braket SV1 simulator is a practical constraint due to memory and storage limitations. You can think of it like this: Each time you add a qubit to SV1, the problem becomes twice as hard.

 DM1 is best suited for simulating circuits with noise. Use DM1 when you need to study the effects of noise on your circuit or when your algorithm requires density matrix operations. The runtime scales linearly with the number of operations but exponentially with the number of qubits, limiting DM1 to circuits of up to 17 qubits.

 **Concurrency** 

All Braket simulators give you the ability to run multiple circuits concurrently. Concurrency limits vary by simulator and region. For more information on concurrency limits, see the [Quotas](https://docs.aws.amazon.com/braket/latest/developerguide/braket-quotas.html) page.