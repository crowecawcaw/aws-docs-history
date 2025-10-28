This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Kubernetes cluster autoscaler (optional)

Kubernetes Cluster Autoscaler is an optional configuration value for the Wickr Enterprise
installation. It will aid in scaling your Kubernetes node groups in the event of increased
traffic or other resource restrictions that could lead to poor performance.

The Wickr Enterprise installation supports 3 Cloud provider integrations: AWS, Google
Cloud, and Azure. **Each Cloud provider has different requirements for this
integration.** Please follow the instructions for your specific cloud provider below to
enable this feature.

## AWS

If you did not use the WickrEnterpriseCDK to install your Wickr Environment on AWS,
you will need to take some additional steps to enable the Cluster Autoscaler.

1. Add the following tags to your Node Groups. This allows the Cluster Autoscaler to
   autodiscover the appropriate nodes.
   1. `k8s.io/cluster-autoscaler/**clusterName** = owned` where
      **clusterName** is the name of your Kubernetes Cluster
   2. `k8s.io/cluster-autoscaler-enabled = true`

2. Add a Kubernetes Service Account, in the kube-system namespace and associate it with an
   IAM policy that allows autoscaling and ec2 actions. For more information and detailed
   instructions, see [Configuring a Kubernetes
   service account to assume an IAM role](../../../eks/latest/userguide/associate-service-account-role.md "../../../eks/latest/userguide/associate-service-account-role.md") in the _Amazon EKS User
   Guide_.
   1. You’ll need to use the ‘kube-system’ namespace when setting up the Service
      Account
   2. The following policy can be used for the Service Account:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Action": [
    "autoscaling:DescribeAutoScalingGroups",
    "autoscaling:DescribeAutoScalingInstances",
    "autoscaling:DescribeLaunchConfigurations",
    "autoscaling:DescribeTags",
    "autoscaling:SetDesiredCapacity",
    "autoscaling:TerminateInstanceInAutoScalingGroup",
    "ec2:DescribeInstanceTypes",
    "ec2:DescribeInstances",
    "ec2:DescribeLaunchTemplateVersions"
    ],
    "Resource": "*",
    "Effect": "Allow"
    }
    ]
   }`

   ```

In the Replicated UI when configuring the Cluster Autoscaler, select
**AWS** as your cloud provider and provide the name of the Service Account
you created above to instruct the Cluster Autoscaler to utilize that service account.

## Google cloud

It is highly recommended to use the built-in Autoscaling capabilities from GKE for both
Autopilot and standard clusters. However, if you wish to proceed with this integration, the
following requirements must be met before proceeding.

**Requirements:**

1. The Managed Instance Groups (MIG) must be created with Security Scope including at a
   minimum 'Read/Write' to Compute Engine Resources. This cannot be added to the MIG later
   currently.
2. Cluster must have Workload Identity Federation enabled. You can enable this on an
   existing cluster by running: `gcloud container clusters update ${CLUSTER_NAME}
--workload-pool=${PROJECT_ID}.svc.id.goog`
3. A Google Cloud Platform (GCP) Service Account with access to the role
   `roles/compute.instanceAdmin.v1`. This can be created using these instructions:

```
# Create GCP Service Account
gcloud iam service-accounts create k8s-cluster-autoscaler

# Add role to GCP Service Account
gcloud projects add-iam-policy-binding ${PROJECT_ID} \
--member "serviceAccount:k8s-cluster-autoscaler@${PROJECT_ID}.iam.gserviceaccount.com" \
--role "roles/compute.instanceAdmin.v1"

# Link GCP Service Account to Kubernetes Service Account
gcloud iam service-accounts add-iam-policy-binding k8s-cluster-autoscaler@${PROJECT_ID}.iam.gserviceaccount.com \
--role roles/iam.workloadIdentityUser \
--member "serviceAccount:${PROJECT_ID}.svc.id.goog[kube-system/cluster-autoscaler-gce-cluster-autoscaler]"
```

## Azure

Azure Kubernetes Service (AKS) provides integrated cluster autoscaling for most deployments
and it is highly recommended to utilize those methods for cluster autoscaling. However, if your
requirements are such that those methods do not work, we have provided a Kubernetes Cluster
Autoscaler integration for Azure Kubernetes Service. To utilize this integration you will need
to gather the following information and put them in the configuration of the KOTS admin panel
under **Cluster Autoscaler** after selecting **Azure** as your
cloud provider.

**Azure Authentication**

**Subscription Id**: The subscription ID can be obtained via the Azure
portal by following the official documentation. For more information, see [Get
subscription and tenant IDs in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id "https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id").

The following parameters can be obtained by creating an AD Service Principal using the az
command line utility.

```
az ad sp create-for-rbac —role="Contributor" —scopes="/subscriptions/subscription-id" —output json
```

App ID:

Client Password:

Tenant ID:

**Azure Cluster Autoscaler Configuration**

In addition to the authentication requirements, the following fields are necessary for
proper functioning of the cluster autoscaler. Commands for obtaining this information has been
provided for convenience, however, they may require some modifications depending on your
specific AKS configuration.

**Azure Managed Node Resource Group**: This value is the Managed Resource
Group created by Azure when you established the AKS Cluster and not the Resource Group you
defined. To obtain this value, you need the CLUSTER_NAME and RESOURCE_GROUP from when you
created the cluster. Once you have those values, you can obtain this by running:

```
az aks show —resource-group ${RESOURCE_GROUP} —name ${CLUSTER_NAME} —query nodeResourceGroup -o tsv
```

**Application Node Pool VMSS Name**: This is the name of the Virtual
Machine Scaling Set (VMSS) associated with your AKS Nodepool for the Wickr Application. This
is the resource that will be scaling up or down based on the needs of your cluster. To obtain
this value you can run the following **az** command:

```
CLUSTER_NODEPOOL_NAME="(Your-NodePool-Name)"
CLUSTER_RESOURCE_GROUP="(Your-Managed-Node-Resource-Group-As-Defined-Above>)"
az vmss list -g ${CLUSTER_RESOURCE_GROUP} --query '[?tags."aks-managed-poolName"==`'''${CLUSTER_NODEPOOL_NAME}'''`].{VMSS_name:name}' -o tsv
```

**ACalling Node Pool VMSS Name (optional)**: This is the name of the VMSS
associated with your calling Nodepool if you have one. To obtain this value, you can run a
modified version of the command for Application Node Pool VMSS Name switching out the
CLUSTER_NODEPOOL_NAME value for the name of the nodepool for your calling nodepool.
