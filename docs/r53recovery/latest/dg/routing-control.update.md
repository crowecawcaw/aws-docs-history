#

Getting and updating routing control states using the ARC API (recommended)

We recommend that you use Amazon Application Recovery Controller (ARC) API operations to get or update routing control states,
by using an AWS CLI command or by using code that you have developed to use ARC API operations with
one of the AWS SDKs. We recommend using API operations, with the CLI or in code, for working with
routing control states, rather than using the AWS Management Console.

ARC offers extreme reliability for failing over across cells (AWS Regions) by updating routing
control states using the API because routing controls are stored in a highly available cluster.
ARC ensures that at least three out of the five Regional cluster endpoints are
always accessible to you to make routing control state changes. To get or change
a routing control state using the API, you connect to one of your Regional cluster
endpoints. If the endpoint is unavailable, you can try connecting to another one of your cluster
endpoints.

You can view the list of Regional cluster endpoints for your cluster in the Route 53 console,
or by using an API action, [DescribeCluster](../../../recovery-cluster/latest/api/cluster-clusterarn.md "../../../recovery-cluster/latest/api/cluster-clusterarn.md"). Your process for getting and changing routing control
states should try each endpoint in rotation, as needed, since cluster endpoints are
cycled through available and unavailable states for regular maintenance and updates.

We provide detailed information and code examples for using ARC API operations to get and update routing
control states, and work with Regional cluster endpoints. For more information, see the following :

- For code examples that explain how to rotate through Regional cluster endpoints to get and set
  routing control states, see [Actions for Application Recovery Controller using AWS SDKs](service_code_examples_actions.md "service_code_examples_actions.md") .
- For information about using the AWS CLI to get and update routing control states, see [List and update routing controls and states with the AWS CLI](getting-started-cli-routing.md "getting-started-cli-routing.md").
