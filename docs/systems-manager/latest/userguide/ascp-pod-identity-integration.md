• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use AWS Secrets and Configuration Provider CSI with Pod

Identity for Amazon EKS

The AWS Secrets and Configuration Provider integration with the Pod Identity Agent for Amazon Elastic Kubernetes Service provides
enhanced security, simplified configuration, and improved performance for
applications running on Amazon EKS. Pod Identity simplifies AWS Identity and Access Management (IAM)
authentication for Amazon EKS when retrieving parameters from AWS Systems Manager Parameter Store or
secrets from Secrets Manager.

Amazon EKS Pod Identity streamlines the process of configuring IAM permissions
for Kubernetes applications by allowing permissions to be set up directly
through Amazon EKS interfaces, reducing the number of steps and eliminating the need
to switch between Amazon EKS and IAM services. Pod Identity enables the use of a
single IAM role across multiple clusters without updating trust policies and
supports [role session
tags](../../../eks/latest/userguide/pod-id-abac.md#pod-id-abac-tags "../../../eks/latest/userguide/pod-id-abac.md#pod-id-abac-tags") for more granular access control. This approach not only
simplifies policy management by allowing reuse of permission policies across
roles but also enhances security by enabling access to AWS resources based on
matching tags.

## How it works

1. Pod Identity assigns an IAM role to the Pod.
2. ASCP uses this role to authenticate with AWS services.
3. If authorized, ASCP retrieves the requested parameters and makes
   them available to the Pod.

For more information, see [Understand how Amazon EKS
Pod Identity works](../../../eks/latest/userguide/pod-id-how-it-works.md "../../../eks/latest/userguide/pod-id-how-it-works.md") in the _Amazon EKS User Guide_.

## Prerequisites

###### Important

Pod Identity is supported only for Amazon EKS in the cloud. It is not
supported for [Amazon EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere/ "https://aws.amazon.com/eks/eks-anywhere/"), [Red Hat OpenShift Service on AWS](https://aws.amazon.com/rosa/ "https://aws.amazon.com/rosa/"), or self-managed Kubernetes clusters on Amazon EC2
instances.

- Amazon EKS cluster (version 1.24 or later)
- Access to AWS CLI and Amazon EKS cluster via `kubectl`
- (Optional) Access to two AWS accounts for cross-account
  access

## Install the Amazon EKS Pod Identity

Agent

To use Pod Identity with your cluster, you must install the Amazon EKS Pod
Identity Agent add-on.

###### To install the Pod Identity Agent

- Install the Pod Identity Agent add-on on your cluster.

Replace the `default placeholder text` with your own values:

```
eksctl create addon \
  --name eks-pod-identity-agent \
  --cluster `clusterName` \
  --region `region`
```

## Set up ASCP with Pod Identity

1. Create a permissions policy that grants
   `ssm:GetParameters` and
   `ssm:DescribeParameters` permission to the parameters
   that the Pod needs to access.
2. Create an IAM role that can be assumed by the Amazon EKS service
   principal for Pod Identity:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "pods.eks.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRole",
 "sts:TagSession"
 ]
 }
 ]
 }`

```

Attach the IAM policy to the role.

Replace the `default placeholder text` with your own values:

```
aws iam attach-role-policy \
  --role-name `MY_ROLE` \
  --policy-arn `POLICY_ARN`
```

3. Create a Pod Identity association. For an example, see [Create a Pod Identity association](../../../eks/latest/userguide/pod-id-association.md#pod-id-association-create "../../../eks/latest/userguide/pod-id-association.md#pod-id-association-create") in the
   _Amazon EKS User Guide_
4. Create the `SecretProviderClass` that specifies which
   parameters or secrets to mount in the Pod:

```
kubectl apply -f kubectl apply -f https://raw.githubusercontent.com/aws/secrets-store-csi-driver-provider-aws/main/examples/ExampleSecretProviderClass-PodIdentity.yaml
```

The key difference in `SecretProviderClass` between
IRSA and Pod Identity is the optional parameter
`usePodIdentity`. It is an optional field that
determines the authentication approach. When not specified, it
defaults to using IAM Roles for Service Accounts (IRSA).

    * To use EKS Pod Identity, use any of these values:
     `"true", "True", "TRUE", "t", "T"`.
    * To explicitly use IRSA, set to any of these values:
     `"false", "False", "FALSE", "f", or
     "F"`.

5. Deploy the Pod that mounts the parameters or secrets under
   `/mnt/secrets-store`:

```
kubectl apply -f kubectl apply -f https://raw.githubusercontent.com/aws/secrets-store-csi-driver-provider-aws/main/examples/ExampleDeployment-PodIdentity.yaml
```

6. If you use a private Amazon EKS cluster, make sure that the VPC that
   the cluster is in has an AWS STS endpoint. For information about
   creating an endpoint, see [Interface VPC endpoints](../../../IAM/latest/UserGuide/reference_interface_vpc_endpoints.md "../../../IAM/latest/UserGuide/reference_interface_vpc_endpoints.md") in the _AWS Identity and Access Management User
   Guide_.

### Verify the secret mount

To verify that the parameter or secret is mounted properly, run the
following command.

Replace the `default placeholder text` with
your own values:

```
kubectl exec -it $(kubectl get pods | awk '/`pod-identity-deployment`/{print $1}' | head -1) -- cat /mnt/secrets-store/MyParameter
```

###### To set up Amazon EKS Pod Identity to access to parameters in Parameter Store

1. Create a permissions policy that grants `ssm:GetParameters`
   and `ssm:DescribeParameters` permission to the parameters
   that the Pod needs to access.
2. Create a parameter in Parameter Store, if you do not already have one. For
   information, see [Creating Parameter Store parameters in
   Systems Manager](sysman-paramstore-su-create.md "sysman-paramstore-su-create.md").

## Troubleshoot

You can view most errors by describing the Pod deployment.

###### To see error messages for your container

1. Get a list of Pod names with the following command. If you aren't
   using the default namespace, use `-n
`namespace``.

```
kubectl get pods
```

2. To describe the Pod, in the following command, for
   `pod-id` use the Pod ID from the Pods
   you found in the previous step. If you aren't using the default
   namespace, use `-n
`NAMESPACE``.

```
kubectl describe pod/`pod-id`
```

###### To see errors for the ASCP

- To find more information in the provider logs, in the following
  command, for `PODID` use the ID of the
  _csi-secrets-store-provider-aws_ Pod.

```
kubectl -n kube-system get pods
kubectl -n kube-system logs pod/`pod-id`
```
