# Prerequisites to create an interactive endpoint on

Amazon EMR on EKS

This section describes prerequisites to set up an interactive endpoint that EMR Studio
can use to connect to an Amazon EMR on EKS cluster and run interactive workloads.

## AWS CLI

Follow the steps in [Install or update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
to install the latest version of the AWS Command Line Interface (AWS CLI).

## Installing eksctl

Follow the steps in [Install kubectl](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md")
to install the latest version of eksctl. If you are using Kubernetes version 1.22 or
later for your Amazon EKS cluster, use an eksctl version greater than 0.117.0.

## Amazon EKS cluster

Create an Amazon EKS cluster. Register the cluster as a virtual cluster with Amazon EMR on EKS. The
following are requirements and considerations for this cluster:

- The cluster must be in the same Amazon Virtual Private Cloud (VPC) as your EMR Studio.

- The cluster must have at least one private subnet to activate interactive endpoints,
  to link Git-based repositories, and to launch the Application Load Balancer in private mode.
- There must be at least one private subnet in common between your EMR Studio and
  the Amazon EKS cluster that you use to register your virtual cluster. This ensures that your
  interactive endpoint appears as an option in your Studio workspaces, and
  activates connectivity from Studio to the Application Load Balancer.

There are two methods that you can choose from to connect your Studio and
your Amazon EKS cluster:

    + Create an Amazon EKS cluster and associate it with the subnets that belong to your
     EMR Studio.
    + Alternatively, create an EMR Studio and specify the private subnets for your
     Amazon EKS cluster.

- Amazon EKS optimized ARM Amazon Linux AMIs are not supported for Amazon EMR on EKS interactive
  endpoints.
- Interactive endpoints work with Amazon EKS clusters that use Kubernetes versions up to
  1.30.
- Only [Amazon EKS managed node groups](../../../eks/latest/userguide/managed-node-groups.md "../../../eks/latest/userguide/managed-node-groups.md") and Karpenter provisioned nodes are supported.

## Grant Cluster access for Amazon EMR on EKS

Use the the steps in [Grant Cluster
Access for Amazon EMR on EKS](setting-up-cluster-access.md "setting-up-cluster-access.md") to grant Amazon EMR on EKS access to a specific namespace in your
cluster.

## Activate IRSA on the Amazon EKS cluster

To activate IAM roles for Service Accounts (IRSA) on the Amazon EKS cluster, follow the
steps in [Enable IAM Roles
for Service Accounts (IRSA)](setting-up-enable-IAM.md "setting-up-enable-IAM.md").

## Create IAM job execution role

You must create an IAM role to run workloads on Amazon EMR on EKS interactive endpoints. We
refer to this IAM role as the _job execution role_ in this
documentation. This IAM role gets assigned to both the interactive endpoint container and
the actual execution containers that are created when you submit jobs with EMR Studio.
You'll need the Amazon Resource Name (ARN) of your job execution role for Amazon EMR on EKS. There
are two steps required for this:

- [Create a
  IAM role for job execution.](creating-job-execution-role.md "creating-job-execution-role.md")
- [Update the
  trust policy of the job execution role.](setting-up-trust-policy.md "setting-up-trust-policy.md")

## Grant users access to Amazon EMR on EKS

The IAM entity (user or role) that makes the request to create an interactive endpoint
must also have the following Amazon EC2 and `emr-containers` permissions. Follow the steps
described in [Grant users access to Amazon EMR on EKS](setting-up-iam.md "setting-up-iam.md") to grant these
permissions that allow Amazon EMR on EKS to create, manage, and delete the security groups that
limit inbound traffic to the load balancer of your interactive endpoint.

The following `emr-containers` permissions allow the user to perform basic interactive
endpoint operations:

```
"ec2:CreateSecurityGroup",
"ec2:DeleteSecurityGroup",
"ec2:AuthorizeSecurityGroupEgress",
"ec2:AuthorizeSecurityGroupIngress",
"ec2:RevokeSecurityGroupEgress",
"ec2:RevokeSecurityGroupIngress"

"emr-containers:CreateManagedEndpoint",
"emr-containers:ListManagedEndpoints",
"emr-containers:DescribeManagedEndpoint",
"emr-containers:DeleteManagedEndpoint"

```

## Register the Amazon EKS cluster with Amazon EMR

Set up a virtual cluster and map it to the namespace in the Amazon EKS cluster where you want
to run your jobs. For AWS Fargate-only clusters, use the same namespace for both the
Amazon EMR on EKS virtual cluster and Fargate profile.

For information on setting up an Amazon EMR on EKS virtual cluster, see [Register the Amazon EKS cluster with Amazon
EMR](setting-up-registration.md "setting-up-registration.md").

## Deploy AWS Load Balancer Controller to Amazon EKS

cluster

An AWS Application Load Balancer is required for your Amazon EKS cluster. You only need to set up one Application Load Balancer
controller per Amazon EKS cluster. For information on setting up the AWS Application Load Balancer controller, see
[Installing the AWS Load Balancer Controller add-on](../../../eks/latest/userguide/aws-load-balancer-controller.md "../../../eks/latest/userguide/aws-load-balancer-controller.md") in the _Amazon EKS User
Guide_.
