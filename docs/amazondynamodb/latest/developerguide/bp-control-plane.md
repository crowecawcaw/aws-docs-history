# Best practices for managing the control plane in

DynamoDB

###### Note

DynamoDB is introducing a control plane throttle limit of 2,500 requests per second with the
option for a retry. See below for additional details.

DynamoDB control plane operations let you manage DynamoDB tables as well as objects that are
dependent on tables such as indexes. For more information about these operations, see [Control plane](HowItWorks.md#HowItWorks.API.ControlPlane "HowItWorks.md#HowItWorks.API.ControlPlane").

In some circumstances, you may need to take actions and use data returned by control plane
calls as part of your business logic. For example, you might need to know the value of
`ProvisionedThroughput` returned by `DescribeTable`. In these
circumstances, follow these best practices:

- Do not excessively query the DynamoDB control plane.
- Do not mix control plane calls and data plane calls within the same code.
- Handle throttles on control plane requests and retry with a backoff.
- Invoke and track changes to a particular resource from a single client.
- Instead of retrieving data for the same table multiple times at short intervals, cache
  the data for processing.
