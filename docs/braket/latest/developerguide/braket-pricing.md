# Cost tracking and saving

###### Tip

**Learn the foundations of quantum computing with AWS!**
Enroll in the [Amazon Braket Digital Learning Plan](https://skillbuilder.aws/learning-plan/EH35DWGU3R/amazon-braket--knowledge-badge-readiness-path-includes-labs "https://skillbuilder.aws/learning-plan/EH35DWGU3R/amazon-braket--knowledge-badge-readiness-path-includes-labs")
and earn your own Digital badge after completing a series of learning courses and a digital assessment.

With Amazon Braket, you have access to quantum computing resources on demand without upfront
commitment. You pay only for what you use. To learn more about pricing, visit our
[pricing page](https://aws.amazon.com/braket/pricing/ "https://aws.amazon.com/braket/pricing/").

###### In this section:

- [Near real-time cost tracking](#real-time-cost-tracking "#real-time-cost-tracking")
- [Best practices for cost savings](#best-practices "#best-practices")

## Near real-time cost tracking

The Braket SDK offers you the option to add a near real-time cost tracking to your quantum workloads. Each of our example notebooks includes cost tracking code to provide you with a maximum cost estimate on Braket's quantum processing units (QPUs) and on-demand simulators. Maximum cost estimates will be shown in USD and are not inclusive of any credits or discounts.

###### Note

Charges shown are estimates based on your Amazon Braket simulator and quantum processing unit (QPU) task usage. Estimated charges shown may differ from your actual charges. Estimated charges do not factor in any discounts or credits and you may experience additional charges based on your use of other services such as Amazon Elastic Compute Cloud (Amazon EC2).

**Cost tracking for SV1**

In order to demonstrate how the cost tracking function can be used, we will be constructing a Bell State circuit and running it on our SV1 simulator. Begin by importing the Braket SDK modules, defining a Bell State and adding the `Tracker()` function to our circuit:

```
#import any required modules
from braket.aws import AwsDevice
from braket.circuits import Circuit
from braket.tracking import Tracker

#create our bell circuit
circ = Circuit().h(0).cnot(0,1)
device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
with Tracker() as tracker:
    task = device.run(circ, shots=1000).result()

#Your results
print(task.measurement_counts)
```

```
Counter({'00': 500, '11': 500})
```

When you run your Notebook, you can expect the following output for your Bell State simulation. The tracker function will show you the number of shots sent, quantum tasks completed, the execution duration, the billed execution duration, and your maximum cost in USD. Your execution time may vary for each simulation.

```
import datetime

tracker.quantum_tasks_statistics()
{'arn:aws:braket:::device/quantum-simulator/amazon/sv1':
 {'shots': 1000,
  'tasks': {'COMPLETED': 1},
  'execution_duration': datetime.timedelta(microseconds=4000),
  'billed_execution_duration': datetime.timedelta(seconds=3)}}

tracker.simulator_tasks_cost()
```

```
Decimal('0.0037500000')
```

**Using the cost tracker to set maximum costs**

You can use the cost tracker to set maximum costs on a program.
You may have a maximum threshold for how much you want to spend on a
given program. In this way, you can use the cost tracker to build out
cost control logic in your execution code. The following example takes
the same circuit on a Rigetti QPU and limits the cost to
1 USD. The cost to run one iteration of the circuit in our code is 0.30
USD. We have set the logic to repeat the iterations until the total cost
exceeds 1 USD; hence, the code snippet will run three times until the next
iteration exceeds 1 USD. Generally, a program would continue to iterate
until it reaches your desired maximum cost, in this case - three iterations.

```
device = AwsDevice("arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3")
with Tracker() as tracker:
    while tracker.qpu_tasks_cost() < 1:
        result = device.run(circ, shots=200).result()
print(tracker.quantum_tasks_statistics())
print(tracker.qpu_tasks_cost(), "USD")
```

```
{'arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3': {'shots': 600, 'tasks': {'COMPLETED': 3}}}
1.4400000000 USD
```

###### Note

The cost tracker will not track duration for failed TN1 quantum tasks. During a TN1 simulation, if your rehearsal completes, but the contraction step fails, your rehearsal charge will not be shown in the cost tracker.

## Best practices for cost savings

Consider the following best practices for using Amazon Braket. Save time, minimize costs, and avoid common errors.

**Verify with simulators**

- Verify your circuits using a simulator before you run it on a QPU, so you can fine-tune your circuit without incurring charges for QPU usage.
- Although the results from running the circuit on a simulator may not be identical to the results from running the circuit on a QPU, you can identify coding errors or configuration issues using a simulator.

**Restrict user access to certain devices**

- You can set up restrictions that keep unauthorized users from submitting quantum tasks on certain devices. The recommended method for restricting access is with AWS IAM. For more information about how to do that, see [Restrict access](braket-manage-access.md#restrict-access "braket-manage-access.md#restrict-access").
- We recommend that you do **not** use your **admin** account as a way to give or restrict user access to Amazon Braket devices.

**Set billing alarms**

- You can set a billing alarm to notify you when your bill reaches a preset limit.
  The recommended way to set up an alarm is through AWS Budgets. You can set custom
  budgets and receive alerts when your costs or usage may exceed your budgeted amount.
  Information is available at [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/ "https://aws.amazon.com/aws-cost-management/aws-budgets/").

**Test TN1 quantum tasks with low shot counts**

- Simulators cost less than QPUs, but certain simulators can be expensive if quantum tasks are run with high shot counts. We recommend that you test your TN1 tasks with a low shot count. Shot count does not affect the cost for SV1 and local simulator tasks.

**Check all Regions for quantum tasks**

- The console displays quantum tasks only for your current AWS Region. When looking for billable quantum tasks that have been submitted, be sure to check all Regions.
- You can view a list of devices and their associated Regions on the [Supported Devices](braket-devices.md "braket-devices.md") documentation page.
