

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Permissions to access other AWS Resources
<a name="copy-usage_notes-access-permissions"></a>

 To move data between your cluster and another AWS resource, such as Amazon S3, Amazon DynamoDB, Amazon EMR, or Amazon EC2, your cluster must have permission to access the resource and perform the necessary actions. For example, to load data from Amazon S3, COPY must have LIST access to the bucket and GET access for the bucket objects. For information about minimum permissions, see [IAM permissions for COPY, UNLOAD, and CREATE LIBRARY](#copy-usage_notes-iam-permissions).

To get authorization to access the resource, your cluster must be authenticated using the following authentication method: 
+ [Role-based access control](#copy-usage_notes-access-role-based) – For role-based access control, you specify an AWS Identity and Access Management (IAM) role that your cluster uses for authentication and authorization. To safeguard your AWS credentials and sensitive data, we strongly recommend using role-based authentication.

## Role-based access control
<a name="copy-usage_notes-access-role-based"></a>

With <a name="copy-usage_notes-access-role-based.phrase"></a>role-based access control, your cluster temporarily assumes an IAM role on your behalf. Then, based on the authorizations granted to the role, your cluster can access the required AWS resources.

Creating an IAM *role* is similar to granting permissions to a user, in that it is an AWS identity with permissions policies that determine what the identity can and can't do in AWS. However, instead of being uniquely associated with one user, a role can be assumed by any entity that needs it. Also, a role doesn’t have any credentials (a password or access keys) associated with it. Instead, if a role is associated with a cluster, access keys are created dynamically and provided to the cluster.

We recommend using role-based access control because it provides more secure, fine-grained control of access to AWS resources and sensitive user data, in addition to safeguarding your AWS credentials.

Role-based authentication delivers the following benefits:
+ You can use AWS standard IAM tools to define an IAM role and associate the role with multiple clusters. When you modify the access policy for a role, the changes are applied automatically to all clusters that use the role.
+ You can define fine-grained IAM policies that grant permissions for specific clusters and database users to access specific AWS resources and actions.
+ Your cluster obtains temporary session credentials at run time and refreshes the credentials as needed until the operation completes.
+ Your access key ID and secret access key ID aren't stored or transmitted in your SQL code.

To use role-based access control, you must first create an IAM role using the Amazon Redshift service role type, and then attach the role to your cluster. The role must have, at a minimum, the permissions listed in [IAM permissions for COPY, UNLOAD, and CREATE LIBRARY](#copy-usage_notes-iam-permissions). For steps to create an IAM role and attach it to your cluster, see [Authorizing Amazon Redshift to Access Other AWS Services On Your Behalf](https://docs.aws.amazon.com/redshift/latest/mgmt/authorizing-redshift-service.html) in the *Amazon Redshift Management Guide*.

You can add a role to a cluster or view the roles associated with a cluster by using the Amazon Redshift Management Console, CLI, or API. For more information, see [Associating an IAM Role With a Cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/copy-unload-iam-role.html) in the *Amazon Redshift Management Guide*.

When you create an IAM role, IAM returns an Amazon Resource Name (ARN) for the role. To specify an IAM role, provide the role ARN with the [Using the IAM\_ROLE parameter](copy-parameters-authorization.md#copy-iam-role) parameter. 

For example, suppose the following role is attached to the cluster.

```
"IamRoleArn": "arn:aws:iam::0123456789012:role/MyRedshiftRole"
```

The following COPY command example uses the IAM\_ROLE parameter with the ARN in the previous example for authentication and access to Amazon S3.

```
copy customer from 's3://amzn-s3-demo-bucket/mydata'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole';
```

In addition, a superuser can grant the ASSUMEROLE privilege to database users and groups to provide access to a role for COPY operations. For information, see [GRANT](r_GRANT.md).

## Temporary security credentials
<a name="r_copy-temporary-security-credentials"></a>

When you use role-based access control, Amazon Redshift automatically uses temporary security credentials on your behalf. Temporary security credentials provide enhanced security because they have short lifespans and can't be reused after they expire.

When you authorize using an IAM role, your cluster temporarily assumes the role and obtains temporary session credentials at run time. Your cluster refreshes these credentials as needed until the operation completes, so you don't need to provide or manage them yourself. For more information, see [Role-based access control](#copy-usage_notes-access-role-based).

## IAM permissions for COPY, UNLOAD, and CREATE LIBRARY
<a name="copy-usage_notes-iam-permissions"></a>

The IAM role referenced by the IAM\_ROLE parameter must have, at a minimum, the following permissions:
+ For COPY from Amazon S3, permission to LIST the Amazon S3 bucket and GET the Amazon S3 objects that are being loaded, and the manifest file, if one is used.
+ For COPY from Amazon S3, Amazon EMR, and remote hosts (SSH) with JSON-formatted data, permission to LIST and GET the JSONPaths file on Amazon S3, if one is used. 
+ For COPY from DynamoDB, permission to SCAN and DESCRIBE the DynamoDB table that is being loaded. 
+ For COPY from an Amazon EMR cluster, permission for the `ListInstances` action on the Amazon EMR cluster. 
+ For UNLOAD to Amazon S3, GET, LIST, and PUT permissions for the Amazon S3 bucket to which the data files are being unloaded.
+ For CREATE LIBRARY from Amazon S3, permission to LIST the Amazon S3 bucket and GET the Amazon S3 objects being imported.

**Note**  
If you receive the error message `S3ServiceException: Access Denied`, when running a COPY, UNLOAD, or CREATE LIBRARY command, your cluster doesn’t have proper access permissions for Amazon S3.

You can manage IAM permissions by attaching an IAM policy to an IAM role that is attached to your cluster, to a user, or to the group to which your user belongs. For example, the `AmazonS3ReadOnlyAccess` managed policy grants LIST and GET permissions to Amazon S3 resources. For more information about IAM policies, see [Managing IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html) in the *IAM User Guide*. 