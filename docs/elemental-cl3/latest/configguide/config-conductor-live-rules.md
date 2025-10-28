# Rules and limits

The following table provides a summary of the configuration rules and constraints that
apply to an AWS Elemental Conductor Live cluster.

| Feature or topic                                                                                   | Rule or limit                                                                                         |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Hardware in a cluster                                                                              | A Conductor Live cluster can include a maximum of 50 worker nodes.                                    |
| Physical location of nodes in a cluster                                                            | Within a cluster, the Conductor Live and encoder nodes must be located in the same physical location. |
| Within a cluster, the communications among cluster members shouldn't traverse the public internet. |
