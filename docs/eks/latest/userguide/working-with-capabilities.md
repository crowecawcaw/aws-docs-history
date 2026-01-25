**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Working with capability resources

This topic describes common operations for managing capability resources across all capability types.

## EKS capability resources

EKS capabilities are AWS resources that enable managed functionality on your Amazon EKS cluster.
Capabilities run in EKS, eliminating the need to install and maintain controllers and other operational components on your worker nodes.
Capabilities are created for a specific EKS cluster, and remain affiliated with that cluster for their entire lifecycle.

Each capability resource has:

- A unique name within your cluster
- A capability type (ACK, ARGOCD, or KRO)
- An Amazon Resource Name (ARN), specifying both name and type
- A capability IAM role
- A status that indicates its current state
- Configuration, both generic and specific to the capability type

## Understanding capability status

Capability resources have a status that indicates their current state.
You can view capability status and health in the EKS console or using the AWS CLI.

**Console**:

1. Open the Amazon EKS console at https://console.aws.amazon.com/eks/home#/clusters.
2. Select your cluster name.
3. Choose the **Capabilities** tab to view status for all capabilities.
4. For detailed health information, choose the **Observability** tab, then **Monitor cluster**, then the **Capabilities** tab.

**AWS CLI**:

```
aws eks describe-capability \
  --region region-code \
  --cluster-name my-cluster \
  --capability-name my-capability-name
```

### Capability statuses

**CREATING**: Capability is being set up.
You can navigate away from the console—the capability will continue creating in the background.

**ACTIVE**: Capability is running and ready to use.
If resources aren’t working as expected, check resource status and IAM permissions.
See [Troubleshooting EKS Capabilities](capabilities-troubleshooting.md "capabilities-troubleshooting.md") for guidance.

**UPDATING**: Configuration changes are being applied.
Wait for the status to return to `ACTIVE`.

**DELETING**: Capability is being removed from the cluster.

**CREATE_FAILED**: Setup encountered an error.
Common causes include:

- IAM role trust policy incorrect or missing
- IAM role doesn’t exist or isn’t accessible
- Cluster access issues
- Invalid configuration parameters

Check the capability health section for specific error details.

**UPDATE_FAILED**: Configuration update failed.
Check the capability health section for details and verify IAM permissions.

###### Tip

For detailed troubleshooting guidance, see:

- [Troubleshooting EKS Capabilities](capabilities-troubleshooting.md "capabilities-troubleshooting.md") - General capability troubleshooting
- [Troubleshoot issues with ACK capabilities](ack-troubleshooting.md "ack-troubleshooting.md") - ACK-specific issues
- [Troubleshoot issues with Argo CD capabilities](argocd-troubleshooting.md "argocd-troubleshooting.md") - Argo CD-specific issues
- [Troubleshoot issues with kro capabilities](kro-troubleshooting.md "kro-troubleshooting.md") - kro-specific issues

## Create capabilities

To create a capability on your cluster, see the following topics:

- [Create an ACK capability](create-ack-capability.md "create-ack-capability.md") – Create an ACK capability to manage AWS resources using Kubernetes APIs
- [Create an Argo CD capability](create-argocd-capability.md "create-argocd-capability.md") – Create an Argo CD capability for GitOps continuous delivery
- [Create a kro capability](create-kro-capability.md "create-kro-capability.md") – Create a kro capability for resource composition and orchestration

## List capabilities

You can list all capability resources on a cluster.

### Console

1. Open the Amazon EKS console at https://console.aws.amazon.com/eks/home#/clusters.
2. Select your cluster name to open the cluster detail page.
3. Choose the **Capabilities** tab.
4. View capability resources under **Managed capabilities**.

### AWS CLI

Use the `list-capabilities` command to view all capabilities on your cluster. Replace `region-code` with the AWS Region that your cluster is in and replace `my-cluster` with the name of your cluster.

```
aws eks list-capabilities \
  --region `region-code` \
  --cluster-name `my-cluster`

```

```
{
    "capabilities": [
        {
            "capabilityName": "my-ack",
            "arn": "arn:aws:eks:us-west-2:111122223333:capability/my-cluster/ack/my-ack/abc123",
            "type": "ACK",
            "status": "ACTIVE",
            "createdAt": "2025-11-02T10:30:00.000000-07:00",
            "modifiedAt": "2025-11-02T10:32:15.000000-07:00",
        },
        {
            "capabilityName": "my-kro",
            "arn": "arn:aws:eks:us-west-2:111122223333:capability/my-cluster/kro/my-kro/abc123",
            "type": "KRO",
            "status": "ACTIVE",
            "version": "v0.6.3",
            "createdAt": "2025-11-02T10:30:00.000000-07:00",
            "modifiedAt": "2025-11-02T10:32:15.000000-07:00",
        },
        {
            "capabilityName": "my-argocd",
            "arn": "arn:aws:eks:us-west-2:111122223333:capability/my-cluster/argocd/my-argocd/abc123",
            "type": "ARGOCD",
            "status": "ACTIVE",
            "version": "3.1.8-eks-1",
            "createdAt": "2025-11-21T08:22:28.486000-05:00",
            "modifiedAt": "2025-11-21T08:22:28.486000-05:00"
        }
    ]
}
```

## Describe a capability

Get detailed information about a specific capability, including its configuration and status.

### Console

1. Open the Amazon EKS console at https://console.aws.amazon.com/eks/home#/clusters.
2. Select your cluster name to open the cluster detail page.
3. Choose the **Capabilities** tab.
4. Choose the capability you want to view from **Managed capabilities**.
5. View the capability details, including status, configuration, and creation time.

### AWS CLI

Use the `describe-capability` command to view detailed information. Replace `region-code` with the AWS Region that your cluster is in, replace `my-cluster` with the name of your cluster, and replace `capability-name` with the capability name (ack, argocd, or kro).

```
aws eks describe-capability \
  --region `region-code` \
  --cluster-name `my-cluster` \
  --capability-name `capability-name`

```

**Example output:**

```
{
  "capability": {
    "capabilityName": "my-ack",
    "capabilityArn": "arn:aws:eks:us-west-2:111122223333:capability/my-cluster/ack/my-ack/abc123",
    "clusterName": "my-cluster",
    "type": "ACK",
    "roleArn": "arn:aws:iam::111122223333:role/AmazonEKSCapabilityACKRole",
    "status": "ACTIVE",
    "configuration": {},
    "tags": {},
    "health": {
      "issues": []
    },
    "createdAt": "2025-11-19T17:11:30.242000-05:00",
    "modifiedAt": "2025-11-19T17:11:30.242000-05:00",
    "deletePropagationPolicy": "RETAIN"
  }
}
```

## Update the configuration of a capability

You can update certain aspects of a capability’s configuration after creation.
The specific configuration options vary by capability type.

###### Note

EKS capability resources are fully managed, including patching and version updates.
Updating a capability will update resource configuration and will not result in version updates of the managed capability components.

### AWS CLI

Use the `update-capability` command to modify a capability:

```
aws eks update-capability \
  --region `region-code` \
  --cluster-name `my-cluster` \
  --capability-name `capability-name` \
  --role-arn arn:aws:iam::[.replaceable]`111122223333`:role/`NewCapabilityRole`

```

###### Note

Not all capability properties can be updated after creation.
Refer to the capability-specific documentation for details on what can be modified.

## Delete a capability

When you no longer need a capability on your cluster, you can delete the capability resource.

###### Important

**Delete cluster resources before deleting the capability.**

Deleting a capability resource does not automatically delete resources created through that capability:

- All Kubernetes Custom Resource Definitions (CRDs) remain installed in your cluster.
- ACK resources remain in your cluster, and corresponding AWS resources remain in your account
- Argo CD Applications and their Kubernetes resources remain in your cluster
- kro ResourceGraphDefinitions and instances remain in your cluster
  You should delete these resources before deleting the capability to avoid orphaned resources.

You may optionally choose to retain AWS resources associated with ACK Kubernetes resources. See [ACK considerations](ack-considerations.md "ack-considerations.md")

### Console

1. Open the Amazon EKS console at https://console.aws.amazon.com/eks/home#/clusters.
2. Select your cluster name to open the cluster detail page.
3. Choose the **Capabilities** tab.
4. Select the capability you want to delete from the list of **Managed capabilities**.
5. Choose **Delete capability**.
6. In the confirmation dialog, type the name of the capability to confirm deletion.
7. Choose **Delete**.

### AWS CLI

Use the `delete-capability` command to delete a capability resource:

Replace `region-code` with the AWS Region that your cluster is in, replace `my-cluster` with the name of your cluster, and replace `capability-name` with the capability name to delete.

```
aws eks delete-capability \
  --region `region-code` \
  --cluster-name `my-cluster` \
  --capability-name `capability-name`

```

## Next steps

- [Capability Kubernetes resources](capability-kubernetes-resources.md "capability-kubernetes-resources.md") – Learn about the Kubernetes resources provided by each capability type
- [ACK concepts](ack-concepts.md "ack-concepts.md") – Understand ACK concepts and resource lifecycle
- [Working with Argo CD](working-with-argocd.md "working-with-argocd.md") – Working with Argo CD capabilities for GitOps workflows
- [kro concepts](kro-concepts.md "kro-concepts.md") – Understand kro concepts and resource composition
