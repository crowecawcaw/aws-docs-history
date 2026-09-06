

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Troubleshooting Amazon Redshift Issues
<a name="troubleshooting"></a>

As you create your Amazon Redshift datasource, ML models, and evaluation, Amazon Machine Learning (Amazon ML) reports the status of your Amazon ML objects in the Amazon ML console. If Amazon ML returns error messages, use the following information and resources to troubleshoot the issues. 

For answers to general questions about Amazon ML, see the [Amazon Machine Learning FAQs](https://aws.amazon.com/machine-learning/faqs/). You can also search for answers and post questions in the [Amazon Machine Learning forum](https://forums.aws.amazon.com/forum.jspa?forumID=194). 



**Topics**
+ [Troubleshooting Errors](#trouble-errors)
+ [Contacting AWS Support](#contacting-support)

## Troubleshooting Errors
<a name="trouble-errors"></a>

### The format of the role is invalid. Provide a valid IAM role. For example, arn:aws:iam::YourAccountID:role/YourRedshiftRole.
<a name="w2aac16c28c13c16b2"></a>

**Cause**

The format of the Amazon Resource Name (ARN) of your IAM role is incorrect. 

**Solution**

In the Create Datasource wizard, correct the ARN for your role. For information about formatting role ARNs, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) in the *IAM User Guide*. The region is optional for IAM role ARNs.

### The role is invalid. Amazon ML can't assume the <role ARN> IAM role. Provide a valid IAM role and make it accessible to Amazon ML.
<a name="w2aac16c28c13c16b4"></a>

**Cause**

Your role isn't set up to allow Amazon ML to assume it.

**Solution**

In the [IAM console](https://console.aws.amazon.com/iam/), edit your role so that it has a trust policy that allows Amazon ML to assume the role attached to it. 

### This <user ARN> user is not authorized to pass the <role ARN> IAM role.
<a name="w2aac16c28c13c16b6"></a>

**Cause**

Your IAM user doesn't have a permissions policy that allows it to pass a role to Amazon ML.

**Solution**

Attach a permissions policy to your IAM user that allows you to pass roles to Amazon ML. You can attach a permissions policy to your IAM user in the [IAM console](https://console.aws.amazon.com/iam/).

### Passing an IAM role across accounts isn't allowed. The IAM role must belong to this account.
<a name="w2aac16c28c13c16b8"></a>

**Cause**

You can't pass a role that belongs to another IAM account.

**Solution**

Sign in to the AWS account that you used to create the role. You can see your IAM roles in your [IAM console](https://console.aws.amazon.com/iam/).

### The specified role doesn't have permissions to perform the operation. Provide a role that has a policy that provides Amazon ML the required permissions.
<a name="w2aac16c28c13c16c10"></a>

**Cause**

Your IAM role doesn't have the permissions to perform the requested operation. 

**Solution**

Edit the permission policy attached to your role in the [IAM console](https://console.aws.amazon.com/iam/) to provide the required permissions. 

### Amazon ML can't configure a security group on that Amazon Redshift cluster with the specified IAM role.
<a name="w2aac16c28c13c16c12"></a>

**Cause**

Your IAM role doesn't have the permissions required to configure an Amazon Redshift security cluster. 

**Solution**

Edit the permission policy attached to your role in the [IAM console](https://console.aws.amazon.com/iam/) to provide the required permissions.

### An error occurred when Amazon ML attempted to configure a security group on your cluster. Try again later.
<a name="w2aac16c28c13c16c14"></a>

**Cause**

When Amazon ML tried to connect to your Amazon Redshift cluster, it encountered an issue.

**Solution**

Verify that the IAM role that you provided in the Create Datasource wizard has all of the required permissions.

### The format of the cluster ID is invalid. Cluster IDs must begin with a letter and must contain only alphanumeric characters and hyphens. They can't contain two consecutive hyphens or end with a hyphen.
<a name="w2aac16c28c13c16c16"></a>

**Cause**

Your Amazon Redshift cluster ID format is incorrect. 

**Solution**

In the Create Datasource wizard, correct your cluster ID so that it contains only alphanumeric characters and hyphens and doesn't contain two consecutive hyphens or end with a hyphen.

### There is no <Amazon Redshift cluster name> cluster, or the cluster is not in the same region as your Amazon ML service. Specify a cluster in the same region as this Amazon ML.
<a name="w2aac16c28c13c16c18"></a>

**Cause**

Amazon ML can't find your Amazon Redshift cluster because it's not located in the region where you are creating an Amazon ML datasource.

**Solution**

Verify that your cluster exists on the Amazon Redshift console [Clusters](https://console.aws.amazon.com/redshift/home) page, that you are creating a datasource in the same region where your Amazon Redshift cluster is located, and that the cluster ID specified in the Create Datasource wizard is correct.

### Amazon ML can't read the data in your Amazon Redshift cluster. Provide the correct Amazon Redshift cluster ID.
<a name="w2aac16c28c13c16c20"></a>

**Cause**

Amazon ML can't read the data in the Amazon Redshift cluster that you specified.

**Solution**

In the Create Datasource wizard, specify the correct Amazon Redshift cluster ID, verify that you are creating a datasource in the same region that has your Amazon Redshift cluster, and that your cluster is listed on the Amazon Redshift [Clusters](https://console.aws.amazon.com/redshift/home) page.

### The <Amazon Redshift cluster name> cluster isn't publicly accessible.
<a name="w2aac16c28c13c16c22"></a>

**Cause**

Amazon ML can't access your cluster because the cluster is not publicly accessible and does not have a public IP address.

**Solution**

Make the cluster publicly accessible and give it a public IP address. For information about making clusters publicly accessible, see [Modifying a Cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-console.html#modify-cluster) in the *Amazon Redshift Management Guide*.

### The <Redshift> cluster status isn't available to Amazon ML. Use the Amazon Redshift console to view and resolve this cluster status issue. The cluster status must be "available."
<a name="w2aac16c28c13c16c24"></a>

**Cause**

Amazon ML can't see the cluster status.

**Solution**

Make sure that your cluster is available. For information on checking the status of your cluster, see [Getting an Overview of Cluster Status](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-console.html#status-cluster) in the *Amazon Redshift Management Guide*. For information on rebooting the cluster so that it is available, see [Rebooting a Cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-console.html#reboot-cluster) in the *Amazon Redshift Management Guide*.

### There is no <database name> database in this cluster. Verify that the database name is correct or specify another cluster and database.
<a name="w2aac16c28c13c16c26"></a>

**Cause**

Amazon ML can't find the specified database in the specified cluster.

**Solution**

Verify that the database name entered in the Create Datasource wizard is correct, or specify the correct cluster and database names. 

### Amazon ML couldn't access your database. Provide a valid password for database user <user name>.
<a name="w2aac16c28c13c16c28"></a>

**Cause**

The password you provided in the Create Datasource wizard to allow Amazon ML to access your Amazon Redshift database is incorrect.

**Solution**

Provide the correct password for your Amazon Redshift database user. 

### An error occurred when Amazon ML attempted to validate the query.
<a name="w2aac16c28c13c16c30"></a>

**Cause**

There's an issue with your SQL query.

**Solution**

Verify that your query is valid SQL.

### An error occurred when executing your SQL query. Verify the database name and the provided query. Root cause: {serverMessage}.
<a name="w2aac16c28c13c16c32"></a>

**Cause**

Amazon Redshift was unable to run your query.

**Solution**

Verify that you specified the correct database name in the Create Datasource wizard, and that your query is valid SQL. 

### An error occurred when executing your SQL query. Root cause: {serverMessage}.
<a name="w2aac16c28c13c16c34"></a>

**Cause**

Amazon Redshift was unable to find the specified table.

**Solution**

Verify that the table you specified in the Create Datasource wizard is present in your Amazon Redshift cluster database, and that you entered the correct cluster ID, database name, and SQL query.

## Contacting AWS Support
<a name="contacting-support"></a>

If you have AWS Premium Support, you can create a technical support case at the [AWS Support Center](https://console.aws.amazon.com/support/home#). 