AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Prerequisites for using the network diagram in

AWS Migration Hub

The following are the prerequisites for using the network diagram in AWS Migration Hub:

- AWS Application Discovery Service Discovery Agent must be running on all of the on-premises servers that you want
  mapped in the diagram. For more information, see [Setting up Agent Based
  Discovery](../../../application-discovery/latest/userguide/setting-up-agents.md "../../../application-discovery/latest/userguide/setting-up-agents.md") in the _Application Discovery Service User Guide_.
- AWS recommends that server and network connection data be collected for two to six weeks
  to capture important connection patterns, such as month-end or year-end business cycles.
- To grant access to the network diagram when creating an identity-based policy that allows
  or denies access to AWS Application Discovery Service or Migration Hub, you might need to add the
  `discovery:GetNetworkConnectionGraph` action to the policy. For more information,
  see [Granting permissions to use the network diagram](../../../application-discovery/latest/userguide/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-network-connection-graph "../../../application-discovery/latest/userguide/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-network-connection-graph") in the
  _Application Discovery Service User Guide_.
  The network diagram has the following limits:

- Currently, data ingestion stops after 180 days.
- The network diagram can visualize up to 1,500 server nodes.
