# Working with reservations

Reservations give you exclusive access to the quantum device of your choice. You can
schedule a reservation at your convenience, so you know exactly when your workload starts and
ends execution. Reservations are available in 1-hour increments for all Braket devices and
can be cancelled up to 48 hours in advance, at no additional charge. You can choose to queue quantum tasks and
hybrid jobs for an upcoming reservation in advance, or submit workloads during your
reservation.

The cost of dedicated device access is based on the duration of your reservation,
regardless of how many quantum tasks and hybrid jobs you run on the quantum processing unit
(QPU).

###### Note

When using a direct reservation with an IonQ device, there is no
[gateshot](braket-terms.md#gateshot-limit-term "braket-terms.md#gateshot-limit-term")
limit, and a minimum of 500 shots for
[Error mitigation](braket-error-mitigation.md "braket-error-mitigation.md") tasks.

**When to use a reservation**

Leveraging dedicated device access with reservations provides you with the convenience
and predictability of knowing exactly when your quantum workload starts and ends execution.
Compared to submitting tasks and hybrid jobs on-demand, you do not have wait in a queue with
other customer tasks. Because you have exclusive access to the device during your reservation,
only your workloads run on the device for the entirety of the reservation.

We recommend using on-demand access for the design and prototyping phase of your
research, enabling quick and cost-efficient iteration of your algorithms. Once you are ready
to produce final experiment results, consider scheduling a device reservation at your
convenience to ensure that you can meet project or publication deadlines. We also recommend
using reservations when you desire task execution during specific times, such as when you're
running a live demo or workshop on a quantum computer.

###### In this section:

- [How to create a reservation](braket-create-a-reservation.md "braket-create-a-reservation.md")
- [Running quantum tasks during a reservation](braket-run-quantum-task-with-reservation.md "braket-run-quantum-task-with-reservation.md")
- [Running hybrid jobs during a reservation](braket-run-hybrid-jobs-with-reservation.md "braket-run-hybrid-jobs-with-reservation.md")
- [What happens at the end of your reservation](braket-end-of-reservation.md "braket-end-of-reservation.md")
- [Cancel or reschedule an existing reservation](braket-cancel-reservation.md "braket-cancel-reservation.md")
