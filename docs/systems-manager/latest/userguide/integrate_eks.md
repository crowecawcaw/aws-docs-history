

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use Parameter Store parameters in Amazon Elastic Kubernetes Service
<a name="integrate_eks"></a>

To show parameters from Parameter Store, a tool of AWS Systems Manager, as files mounted in Amazon EKS Pods, you can use the AWS Secrets and Configuration Provider for the Kubernetes Secrets Store CSI Driver. The ASCP works with Amazon Elastic Kubernetes Service 1.17\+ running an Amazon EC2 node group. AWS Fargate node groups are not supported. 

With the ASCP, you can store and manage your parameter in Parameter Store and then retrieve them through your workloads running on Amazon EKS. If your parameter contains multiple key-value pairs in JSON format, you can choose which ones to mount in Amazon EKS. The ASCP uses JMESPath syntax to query the key-value pairs in your secret. The ASCP also works with AWS Secrets Manager secrets.

The ASCP offers two methods of authentication with Amazon EKS The first approach uses IAM Roles for Service Accounts (IRSA). The second approach uses Pod Identities. Each approach has its benefits and use cases.

## ASCP with IAM Roles for Service Accounts (IRSA)
<a name="csi_driver_overview"></a>

The ASCP with IAM Roles for Service Accounts (IRSA) lets you mount parameters from Parameter Store as files in your Amazon EKS Pods. This approach is suitable when:
+ You need to mount parameters as files in your Pods.
+ You're using Amazon EKS version 1.17 or later with Amazon EC2 node groups.
+ You want to retrieve specific key-value pairs from JSON-formatted parameters.

For more information, see [Use AWS Secrets and Configuration Provider CSI with IAM Roles for Service Accounts (IRSA)](integrating_ascp_irsa.md).

## ASCP with Pod Identity
<a name="pod_identity_overview"></a>

The ASCP with Pod Identity method enhances security and simplifies configuration for accessing parameters in Parameter Store. This approach is beneficial when:
+ You need more granular permission management at the Pod level.
+ You're using Amazon EKS version 1.24 or later.
+ You want improved performance and scalability.

For more information, see [Use AWS Secrets and Configuration Provider CSI with Pod Identity for Amazon EKS](ascp-pod-identity-integration.md).

## Choosing the right approach
<a name="comparison"></a>

Consider the following factors when deciding between ASCP with IRSA and ASCP with Pod Identity:
+ Amazon EKSversion: Pod Identity requires Amazon EKS 1.24\+, while CSI driver works with Amazon EKS 1.17\+.
+ Security requirements: Pod Identity offers more granular control at the Pod level.
+ Performance: Pod Identity generally performs better in high-scale environments.
+ Complexity: Pod Identity simplifies setup by eliminating the need for separate service accounts.

Choose the method that best aligns with your specific requirements and Amazon EKS environment.