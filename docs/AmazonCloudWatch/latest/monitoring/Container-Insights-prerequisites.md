# Verifying prerequisites for Container Insights in CloudWatch

Before you install Container Insights on Amazon EKS or Kubernetes, verify the following.
These prerequisites apply whether you are using the CloudWatch agent or AWS Distro for
OpenTelemetry to set up Container Insights on Amazon EKS clusters.

- You have a functional Amazon EKS or Kubernetes cluster with nodes attached in one of
  the Regions that supports the Container Insights for Amazon EKS and Kubernetes. For the
  list of supported Regions, see [Container Insights](ContainerInsights.md "ContainerInsights.md").
- You have `kubectl` installed and running. For more information, see
  [Installing
  `kubectl`](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md") in the _Amazon EKS User Guide_.
- If you're using Kubernetes running on AWS instead of using Amazon EKS, the following
  prerequisites are also necessary:

      + Be sure that your Kubernetes cluster has enabled role-based access control
       (RBAC). For more information, see [Using RBAC
       Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/ "https://kubernetes.io/docs/reference/access-authn-authz/rbac/") in the Kubernetes Reference.
      + Your kubelet has enabled Webhook authorization mode. For more information, see
       [Kubelet authentication/authorization](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/ "https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/") in the Kubernetes
       Reference.

  You must also grant IAM permissions to enable your Amazon EKS worker nodes to send
  metrics and logs to CloudWatch. There are two ways to do this:

- Attach a policy to the IAM role of your worker nodes. This works for both Amazon EKS
  clusters and other Kubernetes clusters.
- Use an IAM role for service accounts for the cluster, and attach the policy to
  this role. This works only for Amazon EKS clusters.
  The first option grants permissions to CloudWatch for the entire node, while using an IAM
  role for the service account gives CloudWatch access to only the appropriate daemonset
  pods.

**Attaching a policy to the IAM role of your worker
nodes**

Follow these steps to attach the policy to the IAM role of your worker nodes. This
works for both Amazon EKS clusters and Kubernetes clusters outside of Amazon EKS.

###### To attach the necessary policy to the IAM role for your worker nodes

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Select one of the worker node instances and choose the IAM role in the
   description.
3. On the IAM role page, choose **Attach policies**.
4. In the list of policies, select the check box next to
   **CloudWatchAgentServerPolicy**. If necessary, use the search box
   to find this policy.
5. Choose **Attach policies**.
   If you're running a Kubernetes cluster outside Amazon EKS, you might not already have an
   IAM role attached to your worker nodes. If not, you must first attach an IAM role to
   the instance and then add the policy as explained in the previous steps. For more
   information on attaching a role to an instance, see [Attaching an IAM
   Role to an Instance](../../../AWSEC2/latest/WindowsGuide/iam-roles-for-amazon-ec2.md#attach-iam-role "../../../AWSEC2/latest/WindowsGuide/iam-roles-for-amazon-ec2.md#attach-iam-role") in the _Amazon EC2 User Guide_.

If you're running a Kubernetes cluster outside Amazon EKS and you want to collect EBS
volume IDs in the metrics, you must add another policy to the IAM role attached to the
instance. Add the following as an inline policy. For more information, see [Adding and Removing IAM
Identity Permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ec2:DescribeVolumes"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`

```

**Using an IAM service account role**

This method works only on Amazon EKS clusters.

###### To grant permission to CloudWatch using an IAM service account role

1. If you haven't already, enable IAM roles for service accounts on your cluster.
   For more information, see [Enabling IAM
   roles for service accounts on your cluster](../../../eks/latest/userguide/enable-iam-roles-for-service-accounts.md "../../../eks/latest/userguide/enable-iam-roles-for-service-accounts.md") .
2. If you haven't already, configure the service account to use an IAM role. For
   more information, see [Configuring a
   Kubernetes service account to assume an IAM role](../../../eks/latest/userguide/associate-service-account-role.md "../../../eks/latest/userguide/associate-service-account-role.md").

When you create the role, attach the
**CloudWatchAgentServerPolicy** IAM policy to the role in
addition to the policy that you create for the role. Also, the associated Kubernetes
Service Account that is linked to this role should be created in the
`amazon-cloudwatch` namespace, where the CloudWatch and Fluent Bit daemonsets
will be deployed in the upcoming steps 3. If you haven't already, associate the IAM role with a service account in your
cluster. For more information, see [Configuring a
Kubernetes service account to assume an IAM role](../../../eks/latest/userguide/associate-service-account-role.md "../../../eks/latest/userguide/associate-service-account-role.md").
