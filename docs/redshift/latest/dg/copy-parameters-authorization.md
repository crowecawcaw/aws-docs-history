

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Authorization parameters
<a name="copy-parameters-authorization"></a>

The COPY command needs authorization to access data in another AWS resource, including in Amazon S3, Amazon EMR, Amazon DynamoDB, and Amazon EC2. You can provide that authorization by referencing an [AWS Identity and Access Management (IAM) role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that is attached to your cluster (*role-based access control*). You can encrypt your load data on Amazon S3. 

The following topics provide more details and examples of authentication options:
+ [IAM permissions for COPY, UNLOAD, and CREATE LIBRARY](copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions)
+ [Role-based access control](copy-usage_notes-access-permissions.md#copy-usage_notes-access-role-based)

Use the following to provide authorization for the COPY command: 
+ [Using the IAM\_ROLE parameter](#copy-iam-role) parameter

## Using the IAM\_ROLE parameter
<a name="copy-iam-role"></a>

### IAM\_ROLE
<a name="copy-iam-role-iam"></a>

Use the default keyword to have Amazon Redshift use the IAM role that is set as default and associated with the cluster when the COPY command runs. 

Use the Amazon Resource Name (ARN) for an IAM role that your cluster uses for authentication and authorization.

The following shows the syntax for the IAM\_ROLE parameter. 

```
IAM_ROLE { default | 'SESSION' | 'arn:aws:iam::{{<AWS account-id>}}:role/{{<role-name>}}' }
```

For more information, see [Role-based access control](copy-usage_notes-access-permissions.md#copy-usage_notes-access-role-based). 

### SESSION
<a name="copy-iam-role-session"></a>

Use the `SESSION` keyword to load data using the credentials of your current IAM-federated session. This option is available only when you connect to Amazon Redshift with an IAM-federated identity.

With `SESSION`, Amazon Redshift uses the same Amazon S3 permissions that your federated identity already has. Amazon Redshift doesn't assume a cluster IAM role, so you don't need to attach one to the cluster or workgroup for this access.

When you specify `SESSION`, you can't combine it with any other authorization method.

To load with `SESSION`, you must have the permissions listed in [IAM permissions for COPY, UNLOAD, and CREATE LIBRARY](copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions).

**Note**  
`SESSION` isn't supported for auto-copy jobs. An auto-copy job runs asynchronously and can't access your federated session credentials, so it requires an IAM role. For more information, see [COPY JOB](r_COPY-JOB.md).

For an example of configuring a federated identity, see [Using a federated identity to manage Amazon Redshift access to local resources and Amazon Redshift Spectrum external tables](https://docs.aws.amazon.com/redshift/latest/mgmt/authorization-fas-spectrum.html).