# Designing mappings for node interfaces

This section is intended for the video engineer who is responsible for designing the
MediaLive Anywhere workflows.

In each cluster, you must design a collection of mappings. You must design these mappings
after you have [identified the networks](emla-deploy-identify-network-requirements.md#emla-identify-networks "emla-deploy-identify-network-requirements.md#emla-identify-networks") and
designed the clusters. You must decision a mapping for each network that handles encoder
traffic. You don't need to create a mapping for the management network.

## About interface mappings

Each mapping connects one network to the node network interface that handles the traffic
for that network. For example, there might be a mapping to connect the input network to the
node network interface for input traffic.

![Diagram showing a Network box connected to a Node box, each with a single component.](images/anywhere_nwork_nodeinterface.png)

The mapping works as illustrated in the diagram that follows. The mapping (the blue box)
consists of two pieces of information — the network ID and a logical interface name that you
assign. The mapping connects the network (the pink box) to the physical interface (the
yellow box).

![Diagram showing network, mapping, and node components connected in a linear flow.](images/anywhere_nwork_full.png)

You must design one mapping for each network in a cluster. You don't create one mapping
for each node. Instead, the similar physical interfaces in all the nodes share the same
mapping. For example, the physical interfaces for input traffic all share the same mapping.

## Procedure to design mappings

You will create the mappings in the cluster (the blue box in diagrams above). Then in
each node (each green box), you will create a second mapping that assigns each logical
interface name to the appropriate node interface.

1. Assign names to the networks (the pink boxes above).
2. Assign names to the logical interface for each network (the gray boxes
   above).

Keep in mind that name fields are case sensitive. Make a list of these names, and
make sure that you use these exact names when you later create the networks and the
logical interface names. 3. Match up the network to the corresponding physical interface in each node. The names
might be old style (for example, Eth1) or new style (for example, eno5555).

Typically, the interface position is the same on all your nodes. But they could be
different. In the example below, in CL-A, node 3 uses Eth2 and Eth3. 4. Repeat these steps for every cluster.

You should end up with a list like the following. This list uses the clusters and nodes
that are illustrated in [Organize groups into clusters](emla-deploy-design-cluster.md#emla-deploy-design-organize-cluster "emla-deploy-design-cluster.md#emla-deploy-design-organize-cluster"). Note the
following:

- In this example, cluster CL-A and cluster CL-B share the same two networks. In your
  deployment, clusters might not share networks.

- In this example, you assign the same names to the logical interfaces in both
  clusters. But you could assign different names.

| Cluster name   | Network name         | Logical interface name | Corresponding physical interface for Node 1 | Node 2 | Node 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Node 4 |
| -------------- | -------------------- | ---------------------- | ------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------ | ------------- | ---------------------- | ------------------------------------------- | ------ | ------ |
|                |                      |                        |                                             |        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |        |
| CL-A           | input-network        | my-Inputs-Interface    | Eth1                                        | Eth1   | Eth2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Eth1   |
| output-network | my-Outputs-Interface | Eth2                   | Eth2                                        | Eth3   | Eth2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |        | Cluster name | Network name  | Logical interface name | Corresponding physical interface for Node 1 | Node 2 | Node 3 |
| ---            | ---                  | ---                    | ---                                         | ---    | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |        | CL-B         | input-network | my-Inputs-Interface    | Eth1                                        | Eth1   | Eth2   |
| output-network | my-Outputs-Interface | Eth2                   | Eth2                                        | Eth3   | You will use this information as follows: <br>• Network name: Assign this name when you [create each network](emla-setup-cl-networks.md "emla-setup-cl-networks.md"). <br>• Cluster name: Assign this name when you [create each cluster](emla-setup-cluster.md "emla-setup-cluster.md"). <br>• Logical interface name: Assign this name to complete the **Interface mappings** fields when you [create each cluster](emla-setup-cluster.md "emla-setup-cluster.md"). <br>• Physical interface: You will enter this information to complete the **Node interface mapping** fields when you [create the nodes](emla-setup-cl-nodes-create.md "emla-setup-cl-nodes-create.md"). |
