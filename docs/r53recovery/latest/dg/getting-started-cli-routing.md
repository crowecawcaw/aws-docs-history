#

Examples of using ARC routing control API operations with the AWS CLI

This section walks through simple application examples of working with routing control,
using the AWS Command Line Interface to work with the routing control capability in Amazon Application Recovery Controller (ARC) using API operations.
The examples are intended to help you develop a basic
understanding of how to work with routing control using the CLI.

With routing control in Amazon Application Recovery Controller (ARC), you can trigger traffic failovers between redundant
application copies, or replicas, that are running in separate AWS Regions or Availability Zones.

You organize routing controls into groups called control panels that are provisioned on a cluster. A
ARC cluster is a Regional set of endpoints that is globally deployed. Cluster endpoints provide a highly
available API that you can use to set and retrieve routing control states. For more information about the
components of the routing control feature, see
[Routing control components](introduction-components-routing.md "introduction-components-routing.md") .

###### Note

ARC is a global service that supports endpoints in multiple AWS Regions. However, you must
specify the US West (Oregon) Region—that is, specify the parameter `--region us-west-2`—
in most ARC CLI commands. For example, use the `region` parameter when you create recovery groups,
control panels, and clusters.

When you create a cluster, ARC provides you with a set of Regional
endpoints. To get or update routing control states, you must specify the Regional endpoint (the AWS Region and
the endpoint URL) in your CLI command.

For more information about using the AWS CLI, see the AWS CLI Command Reference. For a list of routing control API actions,
see [Routing control API operations](actions.md "actions.md") and [Routing control API operations](actions.md "actions.md").

We'll start by creating the components you need to manage failover by using routing controls, beginning
with creating a cluster.
