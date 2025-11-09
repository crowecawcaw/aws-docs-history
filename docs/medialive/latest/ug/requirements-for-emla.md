# Requirements for MediaLive Anywhere

Your organization might be deploying MediaLive Anywhere, which lets you run MediaLive channels on
on-premises hardware located in your organization's data center.

You must give your users access to perform MediaLive Anywhere operations:

- Permissions to perform the initial configuration of the MediaLive Anywhere clusters, and to modify the
  configuration as required.
- Permissions to work with MediaLive Anywhere resources when creating channels and running
  workflows

## Configuration actions

Some users in your organization will configure the clusters of on-premises nodes to work
with MediaLive. These users need the following permissions. We recommend that you create separate
policies for the MediaLive permissions and the Amazon Elastic Container Service permissions.

| Permissions                                                            | Service name in IAM              | Actions                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Create, modify, and delete networks, clusters, nodes, and SDI sources. | MediaLive                        | `CreateNetwork``CreateCluster``CreateNode``CreateSdiSource``DeleteNetwork``DeleteCluster``DeleteNode``DeleteSdiSource``UpdateNetwork``UpdateCluster``UpdateNode``UpdateSdiSource`                                                          |
| Create a cluster                                                       | Amazon Elastic Container Service | In addition to `CreateCluster`, users need access to actions in Amazon Elastic Container Service.<br>For more information, see [Create special FAS policies](emla-deploy-users-ecs-permissions.md "emla-deploy-users-ecs-permissions.md"). |
| View networks, clusters, nodes, and SDI sources                        | MediaLive                        | `ListNetworks`<br>`ListClusters`<br>`ListNodes`<br>`ListSdiSources`<br>`DescribeNetwork`<br>`DescribeCluster`<br>`DescribeNode`<br>`DescribeSdiSource`                                                                                     |

## Runtime actions

Some users in your organization will create push inputs and SDI inputs for sources that
originate from your on-premises network. These users need the following permissions. These
permissions are in addition to the permissions listed in [Requirements for AWS Elemental MediaLive
features](requirements-for-medialive.md "requirements-for-medialive.md").

| Permissions                                                   | Service name in IAM | Specific activities that the user can perform                                                                     | Actions          |
| ------------------------------------------------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------- |
| Create push inputs for channels running on MediaLive Anywhere | MediaLive           | Specify the network of a static IP address on a push input. (Using a static IP address<br>is optional.)           | `ListNetworks`   |
| Create push inputs for channels running on MediaLive Anywhere | MediaLive           | Optionally specify the route for a static IP address on a push input. (Using a static<br>IP address is optional.) | `ListNetworks`   |
| Create SDI inputs for channels running on MediaLive Anywhere  | MediaLive           | Select the source for an SDI input                                                                                | `ListSdiSources` |
