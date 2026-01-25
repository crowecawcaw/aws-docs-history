**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create a kro capability using the AWS CLI

This topic describes how to create a kro (Kube Resource Orchestrator) capability using the AWS CLI.

## Prerequisites

- **AWS CLI** – Version `2.12.3` or later. To check your version, run `aws --version`. For more information, see [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") in the AWS Command Line Interface User Guide.
- **`kubectl`** – A command line tool for working with Kubernetes clusters. For more information, see [Set up kubectl and eksctl](install-kubectl.md "install-kubectl.md").

## Step 1: Create an IAM Capability Role

Create a trust policy file:

```
cat > kro-trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "capabilities.eks.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:TagSession"
      ]
    }
  ]
}
EOF
```

Create the IAM role:

```
aws iam create-role \
  --role-name KROCapabilityRole \
  --assume-role-policy-document file://kro-trust-policy.json
```

###### Note

Unlike ACK and Argo CD, kro does not require additional IAM permissions.
kro operates entirely within your cluster and does not make AWS API calls.
The role is only needed to establish the trust relationship with the EKS capabilities service.

## Step 2: Create the kro capability

Create the kro capability resource on your cluster. Replace `region-code` with the AWS Region where your cluster is located (such as `us-west-2`) and `my-cluster` with your cluster name.

```
aws eks create-capability \
  --region `region-code` \
  --cluster-name `my-cluster` \
  --capability-name my-kro \
  --type KRO \
  --role-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/KROCapabilityRole \
  --delete-propagation-policy RETAIN
```

The command returns immediately, but the capability takes some time to become active as EKS creates the required capability infrastructure and components.
EKS will install the Kubernetes Custom Resource Definitions related to this capability in your cluster as it is being created.

###### Note

If you receive an error that the cluster doesn’t exist or you don’t have permissions, verify:

- The cluster name is correct
- Your AWS CLI is configured for the correct region
- You have the required IAM permissions

## Step 3: Verify the capability is active

Wait for the capability to become active. Replace `region-code` with the AWS Region that your cluster is in and replace `my-cluster` with the name of your cluster.

```
aws eks describe-capability \
  --region `region-code` \
  --cluster-name `my-cluster` \
  --capability-name my-kro \
  --query 'capability.status' \
  --output text
```

The capability is ready when the status shows `ACTIVE`.

You can also view the full capability details:

```
aws eks describe-capability \
  --region `region-code` \
  --cluster-name `my-cluster` \
  --capability-name my-kro
```

## Step 4: Grant permissions to manage Kubernetes resources

When you create a kro capability, an EKS Access Entry is automatically created with the `AmazonEKSKROPolicy`, which allows kro to manage ResourceGraphDefinitions and their instances.
However, no permissions are granted by default to create the underlying Kubernetes resources (like Deployments, Services, ConfigMaps, etc.) defined in your ResourceGraphDefinitions.

This intentional design follows the principle of least privilege—different ResourceGraphDefinitions require different permissions.
For example: \* A ResourceGraphDefinition that creates only ConfigMaps and Secrets needs different permissions than one that creates Deployments and Services \* A ResourceGraphDefinition that creates ACK resources needs permissions for those specific custom resources \* Some ResourceGraphDefinitions might only read existing resources without creating new ones

You must explicitly configure the permissions kro needs based on the resources your ResourceGraphDefinitions will manage.

### Quick setup

For getting started quickly, testing, or development environments, use `AmazonEKSClusterAdminPolicy`:

Get the capability role ARN:

```
CAPABILITY_ROLE_ARN=$(aws eks describe-capability \
  --region `region-code` \
  --cluster-name `my-cluster` \
  --capability-name my-kro \
  --query 'capability.roleArn' \
  --output text)
```

Associate the cluster admin policy:

```
aws eks associate-access-policy \
  --region `region-code` \
  --cluster-name `my-cluster` \
  --principal-arn $CAPABILITY_ROLE_ARN \
  --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy \
  --access-scope type=cluster
```

###### Important

The `AmazonEKSClusterAdminPolicy` grants broad permissions to create and manage all Kubernetes resources, including the ability to create any resource type across all namespaces.
This is convenient for development and POCs but should not be used in production.
For production, create custom RBAC policies that grant only the permissions needed for the specific resources your ResourceGraphDefinitions will manage.
For guidance on configuring least-privilege permissions, see [Configure kro permissions](kro-permissions.md "kro-permissions.md") and [Security considerations for EKS Capabilities](capabilities-security.md "capabilities-security.md").

## Step 5: Verify custom resources are available

After the capability is active, verify that kro custom resources are available in your cluster:

```
kubectl api-resources | grep kro.run
```

You should see the `ResourceGraphDefinition` resource type listed.

## Next steps

- [kro concepts](kro-concepts.md "kro-concepts.md") - Understand kro concepts and resource composition
- [kro concepts](kro-concepts.md "kro-concepts.md") - Learn about SimpleSchema, CEL expressions, and composition patterns
- [Working with capability resources](working-with-capabilities.md "working-with-capabilities.md") - Manage your kro capability resource
