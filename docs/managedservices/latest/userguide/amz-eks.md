# Use AMS SSP to provision Amazon EKS on AWS Fargate in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon EKS on AWS Fargate capabilities directly in your AMS managed account. AWS Fargate is a technology that provides on-demand, right-sized compute capacity for containers (to understand containers, see
[What are Containers?](https://aws.amazon.com/what-are-containers "https://aws.amazon.com/what-are-containers")).
With AWS Fargate, you no longer have to provision, configure, or scale groups of
virtual machines to run containers. This removes the need to choose server types,
decide when to scale your node groups, or optimize cluster packing.

Amazon Elastic Kubernetes Service (Amazon EKS) integrates Kubernetes with AWS Fargate by using controllers that
are built by AWS using the upstream, extensible model provided by Kubernetes. These
controllers run as part of the Amazon EKS-managed Kubernetes control plane and are
responsible for scheduling native Kubernetes pods onto Fargate. The Fargate
controllers include a new scheduler that runs alongside the default Kubernetes scheduler
in addition to several mutating and validating admission controllers. When you start a
pod that meets the criteria for running on Fargate, the Fargate controllers running
in the cluster recognize, update, and schedule the pod onto Fargate.

To learn more, see
[Amazon EKS on AWS Fargate Now Generally Available](https://aws.amazon.com/blogs/aws/amazon-eks-on-aws-fargate-now-generally-available/ "https://aws.amazon.com/blogs/aws/amazon-eks-on-aws-fargate-now-generally-available/") and
[Amazon EKS Best Practices Guide for Security](https://aws.github.io/aws-eks-best-practices/security/docs/ "https://aws.github.io/aws-eks-best-practices/security/docs/") (includes "Recommendations"
such as "Review and revoke unnecessary anonymous access" and more).

###### Tip

AMS has a change type, Deployment | Advanced stack components | Identity and Access Managment (IAM) | Create OpenID Connect provider (ct-30ecvfi3tq4k3),
that you can use with Amazon EKS. For an example, see
[Identity and Access Management (IAM) | Create OpenID Connect Provider](../ctref/deployment-advanced-identity-and-access-management-iam-create-openid-connect-provider.md "../ctref/deployment-advanced-identity-and-access-management-iam-create-openid-connect-provider.md").

## Amazon EKS on AWS Fargate in AWS Managed Services FAQ

**Q: How do I request access to Amazon EKS on Fargate in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account.

- `customer_eks_fargate_console_role`.

After it's provisioned in your account, you must onboard the role in your federation solution.

- These service roles give Amazon EKS on Fargate permission to call other AWS services on your behalf:
  - `customer_eks_pod_execution_role`
  - `customer_eks_cluster_service_role`

**Q: What are the restrictions to using Amazon EKS on Fargate in my AMS account?**

- Creating
  [managed](../../../eks/latest/userguide/managed-node-groups.md "../../../eks/latest/userguide/managed-node-groups.md") or
  [self-managed](../../../eks/latest/userguide/worker.md "../../../eks/latest/userguide/worker.md")
  EC2 nodegroups is not supported in AMS. If you have a requirement for using EC2 worker nodes, reach out to your AMS
  Cloud Service Delivery Manager(CSDM) or Cloud Architect(CA).
- AMS does not include Trend Micro or preconfigured network security components for container images. You are expected to manage
  your own image scanning services to detect malicious container images prior to deployment.
- EKSCTL is not supported due to CloudFormation interdependencies.
- During cluster creation, you have permissions to disable
  cluster control plane logging. For more information, see
  [Amazon EKS control plane logging](../../../eks/latest/userguide/control-plane-logs.md "../../../eks/latest/userguide/control-plane-logs.md").
  We advise that you enable all important API, Authentication, and Audit logging on cluster creation.
- During cluster creation, cluster endpoint access for Amazon EKS clusters are defaulted to public; for
  more information, see [Amazon EKS cluster endpoint access control](../../../eks/latest/userguide/cluster-endpoint.md "../../../eks/latest/userguide/cluster-endpoint.md").
  We recommend that Amazon EKS endpoints be set to private. If endpoints are required for public access, then it's a best practice to set them to public
  only for specific CIDR ranges.
- AMS doesn't have a method to force and restrict images used to deploy to containers on Amazon EKS
  Fargate. You can deploy images from Amazon ECR, Docker Hub, or any other private image repository. Therefore, there is a
  risk of deploying a public image that might perform malicious activity on the account.
- Deploying EKS clusters through the cloud development kit (CDK) or CloudFormation Ingest isn't supported in AMS.
- You must create the required security group using [ct-3pc215bnwb6p7 Deployment | Advanced stack components | Security group | Create](../ctref/deployment-advanced-security-group-create.md "../ctref/deployment-advanced-security-group-create.md") and reference in the manifest file for ingress creation. This is because the role `customer-eks-alb-ingress-controller-role` isn't authorized to create security groups.

**Q: What are the prerequisites or dependencies to using Amazon EKS on Fargate in my AMS account?**

In order to use the service, the following dependencies must be configured:

- For authenticating against the service, both KUBECTL and aws-iam-authenticator must be installed; for more information, see
  [Managing cluster authentication](../../../eks/latest/userguide/managing-auth.md "../../../eks/latest/userguide/managing-auth.md").
- Kubernetes rely on a concept called "service accounts." In order to utilize the service accounts functionality inside of
  a kubernetes cluster on EKS, a Management | Other | Other | Update RFC is required with the following inputs:
  - [Required] Amazon EKS Cluster name
  - [Required] Amazon EKS Cluster namespace where service account (SA) will be deployed.
  - [Required] Amazon EKS Cluster SA name.
  - [Required] IAM Policy name and permissions/document to be associated.
  - [Required] IAM Role name being requested.
  - [Optional] OpenID Connect provider URL. For more information, see
    - [Enabling IAM roles for service accounts on your cluster](../../../eks/latest/userguide/enable-iam-roles-for-service-accounts.md "../../../eks/latest/userguide/enable-iam-roles-for-service-accounts.md")
    - [Introducing fine-grained IAM roles for service accounts](https://aws.amazon.com/blogs/opensource/introducing-fine-grained-iam-roles-service-accounts/ "https://aws.amazon.com/blogs/opensource/introducing-fine-grained-iam-roles-service-accounts/")

- We recommend that Config rules be configured and monitored for
  - Public cluster endpoints
  - Disabled API loggingIt is your responsibility to monitor and remediate these Config rules.

If you want to deploy an
[ALB Ingress controller](../../../eks/latest/userguide/alb-ingress.md "../../../eks/latest/userguide/alb-ingress.md"), submit a
Management | Other | Other Update RFC to provision the necessary IAM role to be used with the
ALB Ingress Controller pod. The following inputs are required for creating IAM resources
to be associated with ALB Ingress Controller (include these with your RFC):

- [Required] Amazon EKS Cluster name
- [Optional] OpenID Connect provider URL
- [Optional] Amazon EKS Cluster namespace where the application load balancer (ALB)
  ingress controller service will be deployed. [default: kube-system]
- [Optional] Amazon EKS Cluster service account (SA) name.
  [default: aws-load-balancer-controller]

If you want to enable envelope secrets encryption in your cluster (which we recommend),
provide the KMS key IDs you intend to use, in the description field of the RFC to add the service
(Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct). To learn more about envelope encryption, see
[Amazon EKS adds envelope encryption for secrets with AWS KMS](https://aws.amazon.com/about-aws/whats-new/2020/03/amazon-eks-adds-envelope-encryption-for-secrets-with-aws-kms/ "https://aws.amazon.com/about-aws/whats-new/2020/03/amazon-eks-adds-envelope-encryption-for-secrets-with-aws-kms/").
