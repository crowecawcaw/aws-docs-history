Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Authorization parameters

The COPY command needs authorization to access data in another AWS resource,
including in Amazon S3, Amazon EMR, Amazon DynamoDB, and Amazon EC2. You can provide that authorization by
referencing an [AWS Identity and Access Management (IAM) role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
that is attached to your cluster (_role-based access control_).

You can encrypt your load data on Amazon S3.

The following topics provide more details and examples of authentication
options:

- [IAM permissions for COPY, UNLOAD,
  and CREATE LIBRARY](copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions "copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions")
- [Role-based access
  control](copy-usage_notes-access-permissions.md#copy-usage_notes-access-role-based "copy-usage_notes-access-permissions.md#copy-usage_notes-access-role-based")
- [Key-based access control](copy-usage_notes-access-permissions.md#copy-usage_notes-access-key-based "copy-usage_notes-access-permissions.md#copy-usage_notes-access-key-based")
  Use one of the following to provide authorization for the COPY command:

- [Using the IAM_ROLE parameter](#copy-iam-role "#copy-iam-role") parameter
- [Using the ACCESS_KEY_ID and SECRET_ACCESS_KEY parameters](#copy-access-key-id "#copy-access-key-id") parameters
- [Using the CREDENTIALS parameter](#copy-credentials "#copy-credentials") clause

## Using the IAM_ROLE parameter

### IAM_ROLE

Use the default keyword to have Amazon Redshift use the IAM role that is set as
default and associated with the cluster when the COPY command runs.

Use the Amazon Resource Name (ARN) for an IAM role that your cluster uses for
authentication and authorization. If you specify IAM_ROLE, you can't use
ACCESS_KEY_ID and SECRET_ACCESS_KEY, SESSION_TOKEN, or CREDENTIALS.

The following shows the syntax for the IAM_ROLE parameter.

```
IAM_ROLE { default | 'arn:aws:iam::`<AWS account-id>`:role/`<role-name>`' }
```

For more information, see [Role-based access
control](copy-usage_notes-access-permissions.md#copy-usage_notes-access-role-based "copy-usage_notes-access-permissions.md#copy-usage_notes-access-role-based").

## Using the ACCESS_KEY_ID and SECRET_ACCESS_KEY parameters

### ACCESS_KEY_ID, SECRET_ACCESS_KEY

This authorization method is not recommended.

###### Note

Instead of providing access credentials as plain text, we strongly
recommend using role-based authentication by specifying the IAM_ROLE
parameter. For more information, see [Role-based access
control](copy-usage_notes-access-permissions.md#copy-usage_notes-access-role-based "copy-usage_notes-access-permissions.md#copy-usage_notes-access-role-based").

### SESSION_TOKEN

The session token for use with temporary access credentials. When
SESSION_TOKEN is specified, you must also use ACCESS_KEY_ID and
SECRET_ACCESS_KEY to provide temporary access key credentials. If you specify
SESSION_TOKEN you can't use IAM_ROLE or CREDENTIALS. For more information, see
[Temporary security
credentials](copy-usage_notes-access-permissions.md#r_copy-temporary-security-credentials "copy-usage_notes-access-permissions.md#r_copy-temporary-security-credentials") in the
IAM User Guide.

###### Note

Instead of creating temporary security credentials, we strongly recommend
using role-based authentication. When you authorize using an IAM role, Amazon Redshift
automatically creates temporary user credentials for each session. For more
information, see [Role-based access
control](copy-usage_notes-access-permissions.md#copy-usage_notes-access-role-based "copy-usage_notes-access-permissions.md#copy-usage_notes-access-role-based").

The following shows the syntax for the SESSION_TOKEN parameter with the
ACCESS_KEY_ID and SECRET_ACCESS_KEY parameters.

```
ACCESS_KEY_ID '`<access-key-id>`'
SECRET_ACCESS_KEY '`<secret-access-key>`'
SESSION_TOKEN '`<temporary-token>`';
```

If you specify SESSION_TOKEN you can't use CREDENTIALS or IAM_ROLE.

## Using the CREDENTIALS parameter

### CREDENTIALS

A clause that indicates the method your cluster will use when accessing
other AWS resources that contain data files or manifest files. You can't use
the CREDENTIALS parameter with IAM_ROLE or ACCESS_KEY_ID and
SECRET_ACCESS_KEY.

The following shows the syntax for the CREDENTIALS parameter.

```
[WITH] CREDENTIALS [AS] 'credentials-args'
```

###### Note

For increased flexibility, we recommend using the [IAM_ROLE](#copy-iam-role-iam "#copy-iam-role-iam")
parameter instead of the CREDENTIALS parameter.

Optionally, if the [ENCRYPTED](copy-parameters-data-source-s3.md#copy-encrypted "copy-parameters-data-source-s3.md#copy-encrypted") parameter is used, the
_credentials-args_ string also provides the encryption
key.

The _credentials-args_ string is case-sensitive and must
not contain spaces.

The keywords WITH and AS are optional and are ignored.

You can specify either [role-based access control](copy-usage_notes-access-permissions.md#copy-usage_notes-access-role-based.phrase "copy-usage_notes-access-permissions.md#copy-usage_notes-access-role-based.phrase") or [key-based access control](copy-usage_notes-access-permissions.md#copy-usage_notes-access-key-based.phrase "copy-usage_notes-access-permissions.md#copy-usage_notes-access-key-based.phrase"). In either case, the
IAM role or user must have the permissions required to access the specified
AWS resources. For more information, see [IAM permissions for COPY, UNLOAD,
and CREATE LIBRARY](copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions "copy-usage_notes-access-permissions.md#copy-usage_notes-iam-permissions").

###### Note

To safeguard your AWS credentials and protect sensitive data, we strongly
recommend using role-based access control.

To specify role-based access control, provide the
_credentials-args_ string in the following format.

```
'aws_iam_role=arn:aws:iam::`<aws-account-id>`:role/`<role-name>`'
```

To use temporary token credentials, you must provide the temporary access
key ID, the temporary secret access key, and the temporary token. The
_credentials-args_ string is in the following format.

```
CREDENTIALS
'aws_access_key_id=`<temporary-access-key-id>`;aws_secret_access_key=`<temporary-secret-access-key>`;token=`<temporary-token>`'
```

A COPY command using role-based access control with temporary credentials would resemble the following sample statement:

```
COPY customer FROM 's3://amzn-s3-demo-bucket/mydata'
CREDENTIALS
'aws_access_key_id=`<temporary-access-key-id>`;aws_secret_access_key=`<temporary-secret-access-key-id>`;token=`<temporary-token>`'
```

For more information, see [Temporary security
credentials](copy-usage_notes-access-permissions.md#r_copy-temporary-security-credentials "copy-usage_notes-access-permissions.md#r_copy-temporary-security-credentials").

If the [ENCRYPTED](copy-parameters-data-source-s3.md#copy-encrypted "copy-parameters-data-source-s3.md#copy-encrypted") parameter is used, the
_credentials-args_ string is in the following format,
where `<root-key>` is the value of the root
key that was used to encrypt the files.

```
CREDENTIALS
'`<credentials-args>`;master_symmetric_key=`<root-key>`'
```

A COPY command using role-based access control with an encryption key would resemble the following sample statement:

```
COPY customer FROM 's3://amzn-s3-demo-bucket/mydata'
CREDENTIALS
'aws_iam_role=arn:aws:iam::`<account-id>`:role/`<role-name>`;master_symmetric_key=`<root-key>`'
```
