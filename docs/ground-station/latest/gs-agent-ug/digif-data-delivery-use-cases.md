# Receive data via the AWS Ground Station Agent

The diagrams below provide an overview of how data flows through AWS Ground Station during Wideband Digital Intermediate Frequency (DigIF) contacts.

The AWS Ground Station Agent will handle orchestrating the dataplane components for a contact.
Prior to scheduling a contact the agent must be correctly configured, started, and it must be registered (registration is automatic upon agent startup) with AWS Ground Station.
In addition, the data receiving software (such as a software defined radio) must be running and configured to receive data at the [AwsGroundStationAgentEndpoint](../APIReference/API_AwsGroundStationAgentEndpoint.md "../APIReference/API_AwsGroundStationAgentEndpoint.md") egressAddress.

Behind the scenes, the AWS Ground Station Agent will receive tasking from AWS Ground Station and undo the AWS KMS encryption that was applied in transit, before forwarding it to the destination endpoint egressAddress where your Software Defined Radio (SDR) is listening.
The AWS Ground Station Agent and its underlying components will respect the CPU boundaries set in the configuration file to ensure it does not impact performance of other applications running on the instance.

You must have the AWS Ground Station Agent running on the receiver instance involved in the contact. A single AWS Ground Station Agent is able to orchestrate multiple dataflows, as seen below, if you prefer to receive all dataflows on a single receiver instance.

## Multiple dataflows, single receiver

**Example Scenario:**

You would like to receive two antenna downlinks as DigIF dataflows at the same EC2 receiver instance.
The two downlinks will be 200MHz and 100MHz.

**AwsGroundStationAgentEndpoints:**

There will be two `AwsGroundStationAgentEndpoint` resources, one for each dataflow.
Both endpoints will have the same public IP address (`ingressAddress.socketAddress.name`).
The ingress `portRange`’s should not overlap, as the dataflows are being received at the same EC2 instance.
Both `egressAddress.socketAddress.port`'s must be unique.

**CPU Planning:**

- 1 core (2 vCPU) for running the single AWS Ground Station Agent on the instance.
- 6 cores (12 vCPU) to receive DigIF Dataflow 1 (200MHz lookup in [CPU core planning](agent-instance-selection.md#cpu-core-planning "agent-instance-selection.md#cpu-core-planning") table).
- 4 cores (8 vCPU) to receive DigIF Dataflow 2 (100MHz lookup in [CPU core planning](agent-instance-selection.md#cpu-core-planning "agent-instance-selection.md#cpu-core-planning") table).
- Total Dedicated Agent CPU Space = **11 cores** (22 vCPU) on the same socket.

![Two AwsGroundStationAgentEndpoint resources, one for each dataflow. Both endpoints will have the same public IP address (ingressAddress.socketAddress.name). The ingress portRange’s should not overlap, as the dataflows are being received at the same EC2 instance. Both egressAddress.socketAddress.port's must be unique.](images/digif-multi-dataflow-single-receiver.png)

## Multiple dataflows, multiple receivers

**Example Scenario:**

You would like to receive two antenna downlinks as DigIF dataflows at different EC2 receiver instances.
Both downlinks will be 400MHz.

**AwsGroundStationAgentEndpoints:**

There will be two `AwsGroundStationAgentEndpoint` resources, one for each dataflow.
The endpoints will have a different public IP address (`ingressAddress.socketAddress.name`).
There is no restriction on the port values for either `ingressAddress` or `egressAddress` as the dataflows are received on separate infrastructure and will not conflict with each other.

**CPU Planning:**

- Receiver Instance 1
  - 1 core (2 vCPU) for running the single AWS Ground Station Agent on the instance.
  - 9 cores (18 vCPU) to receive DigIF Dataflow 1 (400MHz lookup in [CPU core planning](agent-instance-selection.md#cpu-core-planning "agent-instance-selection.md#cpu-core-planning") table).
  - Total Dedicated Agent CPU Space = **10 cores** (20 vCPU) on the same socket.

- Receiver Instance 2
  - 1 core (2 vCPU) for running the single AWS Ground Station Agent on the instance.
  - 9 cores (18 vCPU) to receive DigIF Dataflow 2 (400MHz lookup in [CPU core planning](agent-instance-selection.md#cpu-core-planning "agent-instance-selection.md#cpu-core-planning") table).
  - Total Dedicated Agent CPU Space = **10 cores** (20 vCPU) on the same socket.

![Two AwsGroundStationAgentEndpoint resources, one for each dataflow. The endpoints will have a different public IP address (ingressAddress.socketAddress.name). There is no restriction on the port values for either ingressAddress or egressAddress as the dataflows are received on separate infrastructure and will not conflict with each other.](images/digif-multi-dataflow-multi-receiver.png)
