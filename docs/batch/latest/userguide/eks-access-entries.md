

# Amazon EKS access entry authentication
<a name="eks-access-entries"></a>

Amazon EKS supports two mechanisms for granting an IAM principal permission to call the cluster's Kubernetes API: the legacy `aws-auth` ConfigMap and the newer [access entry API](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html). An access entry grants Kubernetes API access to an IAM principal without requiring you to edit a ConfigMap. AWS Batch can authenticate to your cluster through either mechanism.

When you set `eksConfiguration.accessEntry.desiredState` to `ENABLED` on a compute environment, AWS Batch can manage the access entry for that compute environment on the cluster. You no longer need to manually edit the `aws-auth` ConfigMap.

Whether AWS Batch provisions an access entry depends on your AWS Batch compute environment and your Amazon EKS cluster configuration. See [Interaction with the cluster's `authenticationMode`](#eks-access-entries-matrix) for details.

## Values for `accessEntry.desiredState`
<a name="eks-access-entries-desired-state"></a>

The `desiredState` field on `EksAccessEntry` declares the desired access entry state for the compute environment. Valid values are:

`ENABLED`  
AWS Batch creates an AWS Batch-managed access entry on the cluster for the compute environment. AWS Batch will only create an AWS Batch-managed access entry if all compute environments on the cluster have set `desiredState` to `ENABLED` (see [How AWS Batch reconciles `desiredState` across compute environments](#eks-access-entries-reconciliation) for details).

`DISABLED`  
AWS Batch deletes the AWS Batch-managed access entry for the cluster. AWS Batch will only delete an AWS Batch-managed access entry if all compute environments on the cluster have set `desiredState` to `DISABLED` (see [How AWS Batch reconciles `desiredState` across compute environments](#eks-access-entries-reconciliation) for details). Access to the cluster must be configured through the `aws-auth` ConfigMap.

`INHERIT_FROM_CLUSTER`  
AWS Batch defers to the cluster's current access entry `status`. On an Amazon EKS cluster whose authentication mode is `API`, AWS Batch creates and manages an access entry because the cluster has no `aws-auth` ConfigMap to fall back to. On a cluster whose authentication mode is `CONFIG_MAP` or `API_AND_CONFIG_MAP`, AWS Batch neither adds nor removes an access entry.

The compute environment also exposes a read-only `accessEntry.status` field in [DescribeComputeEnvironments](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeComputeEnvironments.html) responses. `ACTIVE` means that an AWS Batch-managed access entry for the compute environment exists on the cluster and takes precedence over the `aws-auth` ConfigMap. `INACTIVE` means that no AWS Batch-managed access entry is present. This can be because `desiredState` is `DISABLED`, because the compute environments targeting the cluster don't yet agree on `desiredState`, or because the entry hasn't been provisioned yet. If `accessEntry.status` is `INACTIVE`, Batch uses `aws-auth` ConfigMap for cluster access.

**Note**  
An access entry reports `ACTIVE` as soon as it exists on the cluster, even if AWS Batch hasn't finished associating the access policy that makes it usable. If the compute environment status changes to `INVALID` while `accessEntry.status` is `ACTIVE`, see [Amazon EKS access entry setup is incomplete](batch_eks_invalid_compute_environment.md#batch_eks_access_entry_incomplete).

**Note**  
If you omit the `accessEntry` field, AWS Batch doesn't record a `desiredState` for the compute environment, and `DescribeComputeEnvironments` doesn't return one. For the purpose of provisioning the access entry, AWS Batch behaves as it does for `INHERIT_FROM_CLUSTER`.

## Interaction with the cluster's `authenticationMode`
<a name="eks-access-entries-matrix"></a>

How AWS Batch behaves for a given `desiredState` depends on the cluster's authentication mode. The following table applies to both `CreateComputeEnvironment` and `UpdateComputeEnvironment`.


<table>
<thead>
  <tr><th>Cluster <code>authenticationMode</code></th><th>Compute environment <code>accessEntry.desiredState=ENABLED</code></th><th>Compute environment <code>accessEntry.desiredState=DISABLED</code></th><th>Compute environment <code>accessEntry.desiredState=INHERIT_FROM_CLUSTER</code></th></tr>
</thead>
<tbody>
  <tr><td><code>CONFIG_MAP</code></td><td colspan="3">Access entries aren't available on the cluster, so AWS Batch doesn't create or remove one. AWS Batch still records the value that you specify. After you change the cluster's authentication mode, that recorded value takes effect on your next <code>CreateComputeEnvironment</code> or <code>UpdateComputeEnvironment</code> call that specifies <code>desiredState</code>.</td></tr>
  <tr><td><code>API_AND_CONFIG_MAP</code></td><td colspan="2">AWS Batch compares the recorded values across the compute environments that share the cluster — see <a href="#eks-access-entries-reconciliation">How AWS Batch reconciles `desiredState` across compute environments</a>.</td><td>Existing access mode is retained. AWS Batch does not add or remove an access entry.</td></tr>
  <tr><td><code>API</code></td><td>Access entry is created and maintained on the cluster.</td><td>The request is rejected. A cluster in this mode doesn't support the <code>aws-auth</code> ConfigMap, and the ConfigMap method can't be enabled after cluster creation, so <code>DISABLED</code> would leave the compute environment with no way to authenticate.</td><td>Access entry is created and maintained on the cluster. When the cluster is <code>API</code>-only, inheriting is equivalent to <code>ENABLED</code>.</td></tr>
</tbody>
</table>


## How AWS Batch reconciles `desiredState` across compute environments
<a name="eks-access-entries-reconciliation"></a>

Because a single Amazon EKS cluster can back multiple AWS Batch compute environments, a cluster's access configuration is a shared resource. AWS Batch therefore reconciles, or compares and resolves, the `desiredState` values recorded across those compute environments.

When the cluster's `authenticationMode` is `API_AND_CONFIG_MAP`, AWS Batch compares the `desiredState` recorded for every compute environment in the same AWS account and AWS Region that targets the cluster. AWS Batch uses this comparison to determine whether to add or remove the access entry on each `CreateComputeEnvironment` or `UpdateComputeEnvironment` operation that specifies `desiredState`.

Every compute environment has `desiredState=ENABLED`  
AWS Batch creates the access entry on the cluster.

Every compute environment has `desiredState=DISABLED`  
AWS Batch deletes the access entry from the cluster if one exists.

The recorded `desiredState` values don't all match  
AWS Batch retains the existing access mode. The access entry is neither added nor removed. This includes any mix of `ENABLED`, `DISABLED`, and `INHERIT_FROM_CLUSTER`, and it also includes any compute environment that has no `desiredState` recorded.

**Note**  
To transition a cluster whose authentication mode is `API_AND_CONFIG_MAP` from `aws-auth` ConfigMap to access entry authentication, set `desiredState=ENABLED` on every AWS Batch compute environment that targets the cluster. To transition back, set `desiredState=DISABLED` on every one of them.

## What AWS Batch creates on your cluster
<a name="eks-access-entries-what-batch-creates"></a>

AWS Batch creates one access entry per cluster that meets the above conditions, then associates the `AWSBatchClusterPolicy` Amazon EKS access policy with that access entry. The access entry is per cluster rather than per compute environment, so all AWS Batch compute environments that target the same cluster share it.

**Note**  
Deleting a compute environment doesn't remove the access entry, even if it's the last AWS Batch compute environment on the cluster. To remove an AWS Batch-managed access entry, call `UpdateComputeEnvironment` with `desiredState=DISABLED` on every AWS Batch compute environment that targets the cluster before you delete them.

An access entry isn't sufficient on its own to run jobs on the cluster. For the Kubernetes permissions and node access that you must configure yourself, see [Cluster configuration that you must still provide](#eks-access-entries-additional-configuration).

## Required permissions
<a name="eks-access-entries-permissions"></a>

AWS Batch manages the access entry using the credentials of the IAM identity that calls the `CreateComputeEnvironment` or `UpdateComputeEnvironment` operation. That identity must be allowed to perform the following Amazon EKS actions:
+ `eks:DescribeCluster`
+ `eks:DescribeAccessEntry`
+ `eks:CreateAccessEntry`
+ `eks:AssociateAccessPolicy`
+ `eks:DeleteAccessEntry`

## Configure the access entry
<a name="eks-access-entries-configure"></a>

You can configure the access entry on a compute environment through the `eksConfiguration.accessEntry` field of the [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html) or [UpdateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html) API.

------
#### [ AWS CLI ]

**Enable an AWS Batch-managed access entry when creating a compute environment**

```
$ aws batch create-compute-environment \
    --compute-environment-name {{my-eks-ce}} \
    --type MANAGED \
    --eks-configuration 'eksClusterArn={{arn:aws:eks:us-east-1:123456789012:cluster/my-cluster}},kubernetesNamespace={{my-aws-batch-namespace}},accessEntry={desiredState=ENABLED}' \
    --compute-resources 'type=EC2,maxvCpus=128,subnets={{subnet-a123456b}},securityGroupIds={{sg-a12b3456}},instanceRole={{arn:aws:iam::123456789012:instance-profile/my-node-instance-profile}}'
```

**Enable an AWS Batch-managed access entry on an existing compute environment**

```
$ aws batch update-compute-environment \
    --compute-environment {{my-eks-ce}} \
    --eks-configuration 'accessEntry={desiredState=ENABLED}'
```

**Check the status**

```
$ aws batch describe-compute-environments \
    --compute-environments {{my-eks-ce}} \
    --query "computeEnvironments[0].eksConfiguration.accessEntry"
```

The response includes both the `desiredState` that you specified and the observed `status`:

```
{
    "desiredState": "ENABLED",
    "status": "ACTIVE"
}
```

**Note**  
AWS Batch returns `accessEntry.status` for all Amazon EKS compute environments, and returns `desiredState` only if you have set it. A compute environment where you never specified `accessEntry` returns `status` alone.

To stop AWS Batch from managing the access entry, set `desiredState` to `DISABLED` instead. Before you do, review [Interaction with the cluster's `authenticationMode`](#eks-access-entries-matrix): `DISABLED` is rejected on a cluster whose authentication mode is `API`, and on a cluster whose authentication mode is `API_AND_CONFIG_MAP` the access entry is removed only after every AWS Batch compute environment that targets the cluster is set to `DISABLED`.

------
#### [ API ]

Use the `eksConfiguration.accessEntry` object in your [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html) or [UpdateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html) request.

**Create a compute environment with an AWS Batch-managed access entry**

Include `accessEntry` in the request body:

```
{
    "computeEnvironmentName": "{{my-eks-ce}}",
    "type": "MANAGED",
    "state": "ENABLED",
    "eksConfiguration": {
        "eksClusterArn": "{{arn:aws:eks:us-east-1:123456789012:cluster/my-cluster}}",
        "kubernetesNamespace": "{{my-aws-batch-namespace}}",
        "accessEntry": {
            "desiredState": "ENABLED"
        }
    },
    "computeResources": {
        "type": "EC2",
        "maxvCpus": 128,
        "subnets": ["{{subnet-a123456b}}"],
        "securityGroupIds": ["{{sg-a12b3456}}"],
        "instanceRole": "{{arn:aws:iam::123456789012:instance-profile/my-node-instance-profile}}"
    }
}
```

**Update the access entry on an existing compute environment**

```
{
    "computeEnvironment": "{{my-eks-ce}}",
    "eksConfiguration": {
        "accessEntry": {
            "desiredState": "ENABLED"
        }
    }
}
```

For more information, see [`EksAccessEntry`](https://docs.aws.amazon.com/batch/latest/APIReference/API_EksAccessEntry.html), [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html), and [UpdateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html) in the *AWS Batch API Reference*.

------

## Cluster configuration that you must still provide
<a name="eks-access-entries-additional-configuration"></a>

An access entry controls only how AWS Batch authenticates to your cluster. It doesn't grant AWS Batch the Kubernetes permissions that it needs to run your jobs, and it doesn't let the instances that AWS Batch launches join the cluster. Regardless of which authentication mechanism you use, you must still configure both of the following.

**Important**  
Once an AWS Batch-managed access entry is created for the AWS Batch service-linked role on a cluster (`accessEntry.status=ACTIVE`), it takes precedence over the `aws-auth` ConfigMap configuration for the role. The ConfigMap entries for the AWS Batch service-linked role are unused, and AWS Batch authenticates using the access entry instead. To return to ConfigMap authentication, set `desiredState=DISABLED` on all compute environments that target the cluster. This removes the AWS Batch-managed access entry.

Kubernetes permissions for the AWS Batch namespace  
AWS Batch needs Kubernetes permissions to create and manage pods in the namespace that you specify in `eksConfiguration.kubernetesNamespace`. Create the namespace, then configure those permissions using one of the following methods depending on your authentication approach:  
+ **Access policy association (required when access entry `status=ACTIVE`)** — When you set `desiredState=ENABLED` on all compute environments targeting a cluster, AWS Batch creates an access entry with the cluster-level `AWSBatchClusterPolicy`. You must then associate the namespace-scoped `AWSBatchNamespacePolicy` to grant AWS Batch permission to create and manage pods.

  After the access entry reaches `status=ACTIVE`, associate the namespace policy using the AWS CLI:

  ```
  $ aws eks associate-access-policy \
      --cluster-name {{my-cluster}} \
      --principal-arn {{arn:aws:iam::123456789012:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch}} \
      --policy-arn arn:aws:eks::aws:cluster-access-policy/AWSBatchNamespacePolicy \
      --access-scope type=namespace,namespaces={{my-aws-batch-namespace}}
  ```

  Replace {{my-aws-batch-namespace}} with the value you specified in `eksConfiguration.kubernetesNamespace`.
**Important**  
Without the namespace-scoped policy association, jobs will remain stuck in `RUNNABLE` status. The cluster-level policy alone does not grant pod management permissions.
+ **Kubernetes roles and role bindings (when access entry `status=INACTIVE`)** — If the AWS Batch-managed access entry is not active, create the Kubernetes roles and role bindings that grant those permissions, as described in [Step 2: Prepare your Amazon EKS cluster for AWS Batch](getting-started-eks.md#getting-started-eks-step-1). You do this once for each cluster.
**Note**  
When an AWS Batch-managed access entry is active (`status=ACTIVE`), the Kubernetes RBAC roles are bypassed. You must use the access policy association method instead.
AWS Batch doesn't create these resources for you, and an AWS Batch-managed access entry doesn't substitute for them. If they're missing, the compute environment can still become `VALID` while your jobs fail to start.

Cluster access for the node instance role  
Instances that AWS Batch launches join the cluster using the instance profile that you specify in `computeResources.instanceRole`. That role needs its own access to the cluster, which is separate from the AWS Batch-managed access entry and which AWS Batch doesn't configure.  
The configuration method depends on your cluster's `authenticationMode`:  
+ **On clusters whose `authenticationMode` is `CONFIG_MAP`** — You must use the `aws-auth` ConfigMap. Access entries are not supported on these clusters.
+ **On clusters whose `authenticationMode` is `API_AND_CONFIG_MAP`** — The node instance role can authenticate using either the `aws-auth` ConfigMap or an access entry. If the instance role is already mapped in the ConfigMap, nodes will join successfully without creating an access entry for the role.
+ **On clusters whose `authenticationMode` is `API`** — You must create an access entry for the node instance role. The `aws-auth` ConfigMap is not used for authentication on these clusters.
To create an access entry for the node instance role, use the AWS CLI:  

```
$ aws eks create-access-entry \
    --cluster-name {{my-cluster}} \
    --principal-arn {{arn:aws:iam::123456789012:role/my-node-instance-role}} \
    --type EC2_LINUX
```

```
$ aws eks associate-access-policy \
    --cluster-name {{my-cluster}} \
    --principal-arn {{arn:aws:iam::123456789012:role/my-node-instance-role}} \
    --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSWorkerNodePolicy \
    --access-scope type=cluster
```
For more information, see [Creating access entries](https://docs.aws.amazon.com/eks/latest/userguide/creating-access-entries.html) in the **Amazon EKS User Guide**.  
Without proper cluster access for the node instance role, EC2 instances cannot join the cluster. Jobs will remain in the `RUNNABLE` state because no capacity registers with the cluster.

## Choosing between the `aws-auth` ConfigMap and access entries
<a name="eks-access-entries-choosing"></a>

Access entry authentication is the recommended path for new AWS Batch on Amazon EKS compute environments, and it offers the following advantages:
+ Eliminates the need to manually edit the `aws-auth` ConfigMap to grant AWS Batch access to the cluster.
+ Provides an auditable, API-driven record of the principals that have access to the cluster.
+ Is required for clusters whose `authenticationMode` is `API`, which do not support the `aws-auth` ConfigMap.

If your cluster's `authenticationMode` is `CONFIG_MAP`, access entries aren't available and AWS Batch authenticates through the `aws-auth` ConfigMap. For instructions, see [Verify that the `aws-auth ConfigMap` is configured correctly](verify-configmap-config.md).