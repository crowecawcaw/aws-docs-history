#

Creating an Amazon VPC endpoint policy for Neptune Analytics data plane

###### Note

AWS PrivateLink for Neptune Analytics does not support VPC endpoint policies for the control plane service
`neptune-graph`. VPC endpoint policies are only supported for the Neptune Analytics data plane
service `neptune-graph-data`.

You can attach an endpoint policy to your Amazon VPC endpoint that controls access to a Neptune Analytics graph. The policy
specifies the following information:

- The AWS Identity and Access Management (IAM) principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

**Restricting access to a specific Neptune Analytics graph from an Amazon VPC endpoint.**

You can create an endpoint policy that restricts access to only specific Neptune Analytics graphs. This type of policy
is useful if you have other AWS services in your Amazon VPC that use graphs. The following policy only
provides access to the `GetGraphSummary` action/API from the VPC endpoint.
