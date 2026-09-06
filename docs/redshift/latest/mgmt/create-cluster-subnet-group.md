

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Creating a cluster subnet group
<a name="create-cluster-subnet-group"></a>

The following procedure walks you through how to create a subnet group for a provisioned cluster. You must have at least one cluster subnet group defined to provision a cluster in a VPC.

**To create a cluster subnet group for a provisioned cluster**

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Configurations**, then choose **Subnet groups**. The list of subnet groups is displayed. 

1. Choose **Create cluster subnet group** to display the create page. 

1. Enter information for the subnet group, including which subnets to add. 

1. Choose **Create cluster subnet group** to create the group with the subnets that you chose. 

**Note**  
For information about how to create an Amazon Redshift Serverless workgroup with a collection of subnets, see [Creating a workgroup with a namespace](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console-workgroups-create-workgroup-wizard.html) or [Create a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/create-subnets.html) in the Amazon VPC User Guide.