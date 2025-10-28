We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Troubleshooting Amazon Redshift Issues

As you create your Amazon Redshift datasource, ML models, and evaluation, Amazon Machine Learning (Amazon ML) reports the
status of your Amazon ML objects in the Amazon ML console. If Amazon ML returns error messages, use the
following information and resources to troubleshoot the issues.

For answers to general questions about Amazon ML, see the [Amazon Machine Learning FAQs](https://aws.amazon.com/machine-learning/faqs/ "https://aws.amazon.com/machine-learning/faqs/"). You can also search for
answers and post questions in the [Amazon Machine Learning
forum](https://forums.aws.amazon.com/forum.jspa?forumID=194 "https://forums.aws.amazon.com/forum.jspa?forumID=194").

###### Topics

- [Troubleshooting Errors](#trouble-errors "#trouble-errors")
- [Contacting AWS Support](#contacting-support "#contacting-support")

## Troubleshooting Errors

### The format of the role is invalid. Provide a valid IAM role. For example,

arn:aws:iam::YourAccountID:role/YourRedshiftRole.

**Cause**

The format of the Amazon Resource Name (ARN) of your IAM role is incorrect.

**Solution**

In the Create Datasource wizard, correct the ARN for your role. For information about
formatting role ARNs, see [IAM ARNs](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns") in the
_IAM User Guide_. The region is optional for IAM role ARNs.

### The role is invalid. Amazon ML can't assume the <role ARN> IAM role. Provide a valid IAM role and

make it accessible to Amazon ML.

**Cause**

Your role isn't set up to allow Amazon ML to assume it.

**Solution**

In the [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), edit your role so that
it has a trust policy that allows Amazon ML to assume the role attached to it.

### This <user ARN> user is not authorized to pass the <role ARN> IAM role.

**Cause**

Your IAM user doesn't have a permissions policy that allows it to pass a role to
Amazon ML.

**Solution**

Attach a permissions policy to your IAM user that allows you to pass roles to Amazon ML. You
can attach a permissions policy to your IAM user in the [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

### Passing an IAM role across accounts isn't allowed. The IAM role must belong to this

account.

**Cause**

You can't pass a role that belongs to another IAM account.

**Solution**

Sign in to the AWS account that you used to create the role. You can see your IAM
roles in your [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

### The specified role doesn't have permissions to perform the operation. Provide a role

that has a policy that provides Amazon ML the required permissions.

**Cause**

Your IAM role doesn't have the permissions to perform the requested operation.

**Solution**

Edit the permission policy attached to your role in the [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") to provide the required permissions.

### Amazon ML can't configure a security group on that Amazon Redshift cluster with the specified IAM

role.

**Cause**

Your IAM role doesn't have the permissions required to configure an Amazon Redshift security
cluster.

**Solution**

Edit the permission policy attached to your role in the [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") to provide the required
permissions.

### An error occurred when Amazon ML attempted to configure a security group on your cluster.

Try again later.

**Cause**

When Amazon ML tried to connect to your Amazon Redshift cluster, it encountered an issue.

**Solution**

Verify that the IAM role that you provided in the Create Datasource wizard has all of
the required permissions.

### The format of the cluster ID is invalid. Cluster IDs must begin with a letter and must

contain only alphanumeric characters and hyphens. They can't contain two consecutive hyphens
or end with a hyphen.

**Cause**

Your Amazon Redshift cluster ID format is incorrect.

**Solution**

In the Create Datasource wizard, correct your cluster ID so that it contains only
alphanumeric characters and hyphens and doesn't contain two consecutive hyphens or end with
a hyphen.

### There is no <Amazon Redshift cluster name> cluster, or the cluster is not in the same region as your Amazon ML

service. Specify a cluster in the same region as this Amazon ML.

**Cause**

Amazon ML can't find your Amazon Redshift cluster because it's not located in the region where you are
creating an Amazon ML datasource.

**Solution**

Verify that your cluster exists on the Amazon Redshift console [Clusters](https://console.aws.amazon.com/redshift/home "https://console.aws.amazon.com/redshift/home") page, that you are creating a
datasource in the same region where your Amazon Redshift cluster is located, and that the cluster ID
specified in the Create Datasource wizard is correct.

### Amazon ML can't read the data in your Amazon Redshift cluster. Provide the correct Amazon Redshift cluster

ID.

**Cause**

Amazon ML can't read the data in the Amazon Redshift cluster that you specified.

**Solution**

In the Create Datasource wizard, specify the correct Amazon Redshift cluster ID, verify that you
are creating a datasource in the same region that has your Amazon Redshift cluster, and that your
cluster is listed on the Amazon Redshift [Clusters](https://console.aws.amazon.com/redshift/home "https://console.aws.amazon.com/redshift/home") page.

### The <Amazon Redshift cluster name> cluster isn't publicly accessible.

**Cause**

Amazon ML can't access your cluster because the cluster is not publicly accessible and does
not have a public IP address.

**Solution**

Make the cluster publicly accessible and give it a public IP address. For information
about making clusters publicly accessible, see [Modifying a
Cluster](../../../redshift/latest/mgmt/managing-clusters-console.md#modify-cluster "../../../redshift/latest/mgmt/managing-clusters-console.md#modify-cluster") in the _Amazon Redshift Management Guide_.

### The <Redshift> cluster status isn't available to Amazon ML. Use the Amazon Redshift

console to view and resolve this cluster status issue. The cluster status must be "available."

**Cause**

Amazon ML can't see the cluster status.

**Solution**

Make sure that your cluster is available. For information on checking the status of your
cluster, see [Getting
an Overview of Cluster Status](../../../redshift/latest/mgmt/managing-clusters-console.md#status-cluster "../../../redshift/latest/mgmt/managing-clusters-console.md#status-cluster") in the _Amazon Redshift Management Guide_. For
information on rebooting the cluster so that it is available, see [Rebooting a
Cluster](../../../redshift/latest/mgmt/managing-clusters-console.md#reboot-cluster "../../../redshift/latest/mgmt/managing-clusters-console.md#reboot-cluster") in the _Amazon Redshift Management Guide_.

### There is no <database name> database in this cluster. Verify

that the database name is correct or specify another cluster and
database.

**Cause**

Amazon ML can't find the specified database in the specified cluster.

**Solution**

Verify that the database name entered in the Create Datasource wizard is correct, or specify the correct cluster and database names.

### Amazon ML couldn't access your database. Provide a valid password for database user

<user name>.

**Cause**

The password you provided in the Create Datasource wizard to allow Amazon ML to access your
Amazon Redshift database is incorrect.

**Solution**

Provide the correct password for your Amazon Redshift database user.

### An error occurred when Amazon ML attempted to validate the query.

**Cause**

There's an issue with your SQL query.

**Solution**

Verify that your query is valid SQL.

### An error occurred when executing your SQL query. Verify the database name and the

provided query. Root cause: {serverMessage}.

**Cause**

Amazon Redshift was unable to run your query.

**Solution**

Verify that you specified the correct database name in the Create Datasource wizard, and
that your query is valid SQL.

### An error occurred when executing your SQL query. Root cause: {serverMessage}.

**Cause**

Amazon Redshift was unable to find the specified table.

**Solution**

Verify that the table you specified in the Create Datasource wizard is present in your
Amazon Redshift cluster database, and that you entered the correct cluster ID, database name, and SQL
query.

## Contacting AWS Support

If you have AWS Premium Support, you can create a technical support case at the [AWS Support Center](https://console.aws.amazon.com/support/home# "https://console.aws.amazon.com/support/home#").
