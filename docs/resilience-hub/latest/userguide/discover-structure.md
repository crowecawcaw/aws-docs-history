# Add resource collections

This section discusses the following options that you can use to form the basis of your
application structure:

- [Add resource collections](#resource-collection "#resource-collection")
- [Add EKS clusters](#add-eks-clusters "#add-eks-clusters")

## Add resource collections

This section discusses the following methods that you use to form the basis of your
application structure:

- [Using AWS CloudFormation stacks](#cloudformation-steps "#cloudformation-steps")
- [Using AWS Resource Groups](#resource-groups-steps "#resource-groups-steps")
- [Using myApplications applications](#myApplications-steps "#myApplications-steps")
- [Using Terraform state files](#terraformstate-steps "#terraformstate-steps")

### Using AWS CloudFormation stacks

Choose the AWS CloudFormation stacks that contain the resources you want to use in the application
you're describing. The stacks can be from the AWS account that you are using to describe the
application, or they can be from different accounts or different Regions.

###### To discover the resources that form the basis of your application structure

1. Select **CloudFormation stack** to discover your stack-based resources.
2. Choose stacks from the **Choose stacks** dropdown list that are
   associated with your AWS account and Region.

To use stacks that are in a different AWS account, different Region, or both, choose
the right arrow adjacent to **Add stack outside of AWS Region** and enter
the Amazon Resource Name (ARN) of the stack in the **Enter a stack ARN** box,
and then choose **Add stack ARN**. For more information about ARNs, see
[Amazon
Resource Names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") in the _AWS General Reference_.

### Using AWS Resource Groups

Choose the AWS Resource Groups that contain the resources that you want to use in the application
that you're describing.

###### To discover the resources that form the basis of your application structure

1. Select **Resource groups** to discover the AWS Resource Groups that contain the
   resources.
2. Choose resources from **Choose a resource group** dropdown list.

To use AWS Resource Groups that are in a different AWS account, different Region, or both, choose
the right arrow adjacent to **Resource Group ARN:** and enter the Amazon
Resource Name (ARN) of the AWS Resource Groups in the **Enter a resource group ARN**
box, and then choose **Add resource Group ARN**. For more information about
ARNs, see [Amazon Resource Names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") in the _AWS General Reference_.

### Using myApplications applications

Choose the myApplications application you want to include in AWS Resilience Hub

###### To include myApplications application in AWS Resilience Hub

1. Select **myApplications**.
2. Choose an application from the **Select application** dropdown
   list.

### Using Terraform state files

Choose the Terraform state file that contains your Amazon S3 bucket resources that you want to use
in the application you're describing. You can navigate to the location of your Terraform state
file or provide a link to a Terraform state file you have access to that’s located in a
different Region.

###### Note

AWS Resilience Hub supports Terraform state file version `0.12` and later.

###### To discover the resources that form the basis of your application structure

1. Select **Terraform state files** to discover your S3 bucket resources.
2. From the **Select state files::** section, choose **Browse S3** to navigate to the location of your Terraform state file.

To use Terraform state files located in a different Region, provide the link to the
location of Terraform state file in the **S3 URI** field, and choose
**Add S3 URL**.

The limit for Terraform state files is 4 megabytes (MB). 3. From **Choose an archive in S3** dialog box, select your Amazon Simple Storage Service bucket from
the **Buckets** section. 4. From the **Objects** section, select a key, and choose **Choose**.

## Add EKS clusters

This section discusses about using Amazon EKS clusters to form the basis of your application
structure.

###### Note

You must have Amazon EKS permissions and additional IAM roles to connect to the Amazon EKS cluster.
For more information about adding single account and cross-account Amazon EKS permissions and
additional IAM roles to connect to the cluster, see the following topics:

- [AWS Resilience Hub access
  permissions reference](security-iam-resilience-hub-permissions.md "security-iam-resilience-hub-permissions.md")
- [Enabling AWS Resilience Hub access to your Amazon Elastic Kubernetes Service
  cluster](enabling-eks-in-arh.md "enabling-eks-in-arh.md")

Choose the Amazon EKS clusters and namespaces that contain the resources you want to use in the
application you're describing. The Amazon EKS clusters can be from the AWS account that you are
using to describe the application, or they can be from different accounts or different
Regions.

###### Note

For AWS Resilience Hub to assess your Amazon EKS clusters, you must manually add the relevant namespaces
to each of the Amazon EKS clusters in **EKS clusters and namespaces** section. The
namespace name must match exactly with the namespace name on your Amazon EKS clusters.

###### To add Amazon EKS clusters

1. In **1. Select EKS clusters** section, choose the Amazon EKS
   clusters from the **Choose EKS clusters** dropdown list that are associated
   with your AWS account and Region.
2. To use Amazon EKS clusters that are in a different AWS account, different Region, or both,
   choose the right arrow adjacent to **Add an EKS cluster within a different account or
   Region** and enter the Amazon Resource Name (ARN) of the Amazon EKS cluster in the
   **Enter an EKS ARN** box, and then choose **Add EKS ARN**.
   For more information about ARNs, see [Amazon Resource Names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") in
   the _AWS General Reference_.

For more information about adding permissions to access cross-Region Amazon Elastic Kubernetes Service clusters,
see [Enabling AWS Resilience Hub access to your Amazon Elastic Kubernetes Service
cluster](enabling-eks-in-arh.md "enabling-eks-in-arh.md").

###### To add namespaces from the selected Amazon EKS clusters

1. In the **Add namespaces** section, from the **EKS clusters and
   namespaces** table, select the radio button located at the left of Amazon EKS cluster
   name, and then choose **Update namespaces**.

You can identify Amazon EKS clusters by the following:

    * **EKS cluster name** – Indicates the name of the selected Amazon EKS
     clusters.
    * **# of Namespaces** – Indicates the number of namespaces
     selected in the Amazon EKS clusters.
    * **Status** – Indicates whether AWS Resilience Hub has included the
     namespaces from the selected Amazon EKS clusters in your application. You can identify the status
     using the following options:




    	+ **Namespace required** – Indicates that you have not included
    	 any namespaces from the Amazon EKS cluster.
    	+ **Namespaces added** – Indicates that you have included one
    	 or more namespaces from the Amazon EKS cluster.

2. To add a namespace, in the **Update namespaces** dialog box, choose
   **Add a new namespace**.

The **Update namespaces** dialog box displays all the namespaces that
you have selected from your Amazon EKS cluster, as an editable option. 3. In the **Update namespaces** dialog box, you have the following edit
options:

    * To add a new namespace, choose **Add a new namespace**, and then enter
     the namespace name in **namespace** box.


    The namespace name must exactly match with the namespace name on your Amazon EKS
     cluster.
    * To remove a namespace, choose **Remove** located next to the
     namespace.
    * To apply the selected namespaces to all the Amazon EKS clusters, choose **Apply
     namespaces to all EKS clusters**.


    If you choose this option, your previous namespace selection in the other Amazon EKS
     clusters will be overridden with the current namespace selection.

4. To include the updated namespaces in your application, choose
   **Update**.

### Next

[Set RTO and RPO](setup-resiliency-policy.md "setup-resiliency-policy.md")
