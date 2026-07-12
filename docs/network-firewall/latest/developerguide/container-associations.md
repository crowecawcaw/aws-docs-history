# Container associations in AWS Network Firewall

AWS Network Firewall container associations collect the IP addresses of running containers in your Amazon Elastic Container Service and
Amazon Elastic Kubernetes Service clusters. They maintain these addresses as a dynamic IP set. Reference this IP set in your Network Firewall
rule groups. Write rules that match traffic by container source or destination IP without hardcoding addresses.

Container associations subscribe to container lifecycle events (task start and stop for Amazon ECS, pod start and stop
for Amazon EKS) to learn which IPs are currently active. They have no direct interaction with cluster traffic or
networking. Your Network Firewall endpoints in your VPC inspect all traffic, using the resolved IP set to evaluate
rules.

## How container associations work

A container association links monitoring configurations to a named Network Firewall resource. Each monitoring
configuration targets one Amazon ECS or Amazon EKS cluster ARN. You can add optional attribute filters to narrow which
containers are tracked.

When you create a container association, Network Firewall:

- Validates that you have access to the specified clusters.
- Creates a service-linked role in your account (if one doesn't already exist).
- Subscribes to container lifecycle events for the specified clusters to learn which container IPs are active.
- Builds and maintains a dynamic IP set from the resolved container addresses.

As containers start and stop, Network Firewall updates the IP set automatically. Network Firewall collects only
IP information from lifecycle events and has no interaction with the cluster's data path. Your Network Firewall
endpoints reference the container association's IP set to match packets by source or destination address.

## Container types

Container associations support two container types:

- **Amazon ECS** – Monitors Amazon Elastic Container Service clusters. Network Firewall creates an
  Managed Rule in your account to receive Amazon ECS task state change events.
- **Amazon EKS** – Monitors Amazon Elastic Kubernetes Service clusters. Network Firewall subscribes
  to pod lifecycle events through the Amazon EKS Pulse Event Service.

You set the container type at creation and cannot change it afterward.

## Monitoring configurations

Each container association can have up to 5 monitoring configurations. A monitoring configuration includes:

- **ClusterArn** (required) – The ARN of the Amazon ECS or Amazon EKS cluster
  to monitor. The cluster must be in the same Region and account as the container association.
- **AttributeFilters** (optional) – Key-value pairs that filter which
  containers are tracked. For Amazon EKS, you can filter by namespace and Kubernetes labels. For Amazon ECS, you can
  filter by container instance attributes.

## Networking requirements and limitations

Container associations have the following networking requirements and limitations:

- **Disable SNAT (Amazon EKS)** – For Amazon EKS pods, disable source NAT (SNAT)
  so that the firewall sees the pod's original IP address. If SNAT is enabled, traffic arrives at the
  firewall with the node IP, not the pod IP, and rules referencing the container association do not
  match.
- **Network mode (Amazon ECS)** – Network Firewall supports only `awsvpc`
  network mode for Amazon ECS tasks. It does not support bridge or host network modes.
- **Fargate and attribute filters (Amazon ECS)** – Attribute filters for Amazon ECS
  container associations only match containers running on Amazon EC2 launch type (container instances). Fargate
  tasks do not have container instance attributes and are not filtered. To get IPs from Fargate tasks,
  do not attach any attributes to the container association.
- **IPSet reference exclusivity** – A rule group's IPSet references
  are either all regular IPSets (prefix lists, static IP sets) or all container associations. You cannot
  mix both types in the same rule group. Attempting to reference both types returns an
  `InvalidRequestException`.

## Prerequisites for container associations

Before you create a container association, make sure that:

- Your IAM identity has the following permissions:

  - `network-firewall:CreateContainerAssociation` on the container association resource
    and on each cluster ARN referenced in the monitoring configurations.
  - `ecs:DescribeClusters` (for Amazon ECS clusters) or `eks:DescribeCluster`
    (for Amazon EKS clusters).
  - `iam:CreateServiceLinkedRole` for the Network Firewall service-linked role (only needed
    the first time).

- For Amazon EKS clusters, SNAT is disabled on the VPC CNI plugin.
- For Amazon ECS clusters, tasks use `awsvpc` network mode.

## Using container associations in firewall rules

After you create a container association, reference it in stateful rule groups as a dynamic IP set. Use the
container association's resolved IP addresses as an IPSet reference variable in your Suricata compatible rules.

### Referencing a container association in a rule group

When you create or update a stateful rule group, add the container association ARN to the rule group's
`ReferenceSets` configuration. This creates a named variable you can use in Suricata rules.

```
aws network-firewall create-rule-group \
    --rule-group-name my-container-rules \
    --type STATEFUL \
    --capacity 100 \
    --rule-group '{
        "RulesSource": {
            "RulesString": "alert tcp @CONTAINER_IPS any -> any any (sid:1; rev:1;)"
        },
        "ReferenceSets": {
            "IPSetReferences": {
                "CONTAINER_IPS": {
                    "ReferenceArn": "arn:aws:network-firewall:us-east-1:123456789012:container-association/my-ecs-monitor"
                }
            }
        }
    }'
```

### Delete protection for container associations

After a rule group references a container association, you cannot delete the container association until you
remove all references to it. If you attempt to delete a referenced container association, the API returns an
`InvalidOperationException` with the message: "Unable to delete the object because it is still
in use."

To delete a container association that is in use:

1. Update or delete the rule groups that reference it.
2. Wait for the references to be fully removed.
3. Delete the container association.

## Creating a container association

You can create a container association using the AWS Command Line Interface, AWS SDKs, or the Network Firewall console.

```
aws network-firewall create-container-association \
    --container-association-name my-ecs-monitor \
    --type ECS \
    --container-monitoring-configurations '[
        {
            "ClusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster",
            "AttributeFilters": [
                {"Key": "ecs.instance-type", "Value": "c5.xlarge"}
            ]
        }
    ]'
```

## Updating a container association

You can update the monitoring configurations and description of a container association. The container type
is fixed at creation and cannot be changed. Use the update token from the most recent describe response for
optimistic concurrency.

- If you pass a `null` or omit the description, the existing description remains unchanged.
  If you pass an empty string, the description is cleared.
- If you update monitoring configurations, Network Firewall automatically manages rules (Amazon ECS) or
  cluster subscriptions (Amazon EKS) for added and removed clusters.

```
aws network-firewall update-container-association \
    --container-association-arn arn:aws:network-firewall:us-east-1:123456789012:container-association/my-ecs-monitor \
    --type ECS \
    --update-token "`your-update-token`" \
    --container-monitoring-configurations '[...]'
```

## Deleting a container association

When you delete a container association, Network Firewall:

- Unsubscribes from container lifecycle events for orphaned clusters (clusters not referenced by other
  associations).
- Removes Managed Rules (for Amazon ECS).
- Transitions the resource to a `DELETING` state.

Network Firewall deletes the container association asynchronously. The API returns immediately with
`DELETING` status while cleanup proceeds in the background.

```
aws network-firewall delete-container-association \
    --container-association-arn arn:aws:network-firewall:us-east-1:123456789012:container-association/my-ecs-monitor
```

## Tagging container associations

Container associations support AWS resource tagging. You can add tags at creation or manage them later using the
`TagResource`, `UntagResource`, and `ListTagsForResource` APIs.

## Managed Rules (Amazon ECS)

For Amazon ECS-type container associations, Network Firewall creates an Managed Rule in your account to receive
Amazon ECS task state change events. Network Firewall names these rules with the pattern
`NetworkFirewallManagedRule-cluster-name-hash`
and tags them as service-managed.

###### Do not modify service-managed rules

Do not delete or modify these Managed Rules manually. Network Firewall manages their lifecycle automatically.
Managed Rules are created when a container association is created or updated to add a new cluster.
They are removed when a container association is deleted or updated to remove a cluster (only if no other
container association references the same cluster).

## Service-linked role for container associations

Container associations require the AWS Network Firewall service-linked role
(`AWSServiceRoleForNetworkFirewall`) in your account. This role grants Network Firewall permission to
monitor container lifecycle events on your behalf.

- Network Firewall automatically creates the service-linked role the first time you create a container
  association, if it doesn't already exist.
- Your IAM identity must have `iam:CreateServiceLinkedRole` permission for the first
  creation.
- All Network Firewall resources in your account share the service-linked role — it is not specific to
  container associations.

For more information, see [Using service-linked roles for Network Firewall](using-service-linked-roles.md "using-service-linked-roles.md").

## Container association status transitions

The following table describes each container association status value.

| Status     | Description                                                                                                                   |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `CREATING` | The container association is being created. Network Firewall has not yet started IP resolution.                               |
| `ACTIVE`   | The container association is operational and actively tracking container IPs.                                                 |
| `UPDATING` | The monitoring configurations are being updated. The previous configuration continues to operate.                             |
| `DELETING` | Network Firewall is deleting this container association and cleaning up event subscriptions and Managed Rules asynchronously. |

You cannot update a container association in `DELETING` state.

## Container association quotas

The following table lists the quotas for container associations.

| Resource                                            | Default quota | Adjustable |
| --------------------------------------------------- | ------------- | ---------- |
| Container associations per account per Region       | 100           | Yes        |
| Monitoring configurations per container association | 5             | No         |
| Container association references per rule group     | 30            | No         |

For the most current quota values, see [AWS Network Firewall quotas](quotas.md "quotas.md").

## Container association error reference

The following table describes the errors that container association API operations can return.

| Error                       | HTTP code | Common causes                                                                                            |
| --------------------------- | --------- | -------------------------------------------------------------------------------------------------------- |
| `AccessDeniedException`     | 400       | Missing `ecs:DescribeClusters`, `eks:DescribeCluster`,<br>`iam:CreateServiceLinkedRole`, or permissions. |
| `InternalServerError`       | 500       | System problem. Retry your request.                                                                      |
| `InvalidRequestException`   | 400       | Invalid parameters, inaccessible cluster, Region mismatch, exceeding config limits.                      |
| `InvalidOperationException` | 400       | Attempting to delete a container association still referenced by a rule group.                           |
| `InvalidTokenException`     | 400       | Stale update token. Re-describe and retry.                                                               |
| `LimitExceededException`    | 400       | Account limit reached.                                                                                   |
| `ResourceNotFoundException` | 400       | Container association with given ARN or name does not exist.                                             |
| `ThrottlingException`       | 400       | Rate limit exceeded.                                                                                     |
