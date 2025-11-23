# Enable Lake Formation with Amazon EMR

With Amazon EMR 6.15.0 and higher, when you run Spark jobs on Amazon EMR on EC2 clusters
that access data in the AWS Glue Data Catalog, you can use AWS Lake Formation to apply table, row,
column, and cell level permissions on Hudi, Iceberg, or Delta Lake based
tables.

In this section, we cover how to create a security configuration and set up Lake Formation
to work with Amazon EMR. We also go over how to launch a cluster with the security
configuration that you created for Lake Formation.

## Step 1: Set up a runtime role for your

EMR cluster

To use a runtime role for your EMR cluster, you must create a security
configuration. With a security configuration, you can apply consistent security,
authorization, and authentication options across your clusters.

1. Create a file called
   `lf-runtime-roles-sec-cfg.json` with the
   following security configuration.

```
{
    "AuthorizationConfiguration": {
        "IAMConfiguration": {
            "EnableApplicationScopedIAMRole": true,
            "ApplicationScopedIAMRoleConfiguration": {
                "PropagateSourceIdentity": true
            }
        },
        "LakeFormationConfiguration": {
            "AuthorizedSessionTagValue": "Amazon EMR"
        }
    },
    "EncryptionConfiguration": {
	    "EnableAtRestEncryption": false,
            "EnableInTransitEncryption": true,
            "InTransitEncryptionConfiguration": {
            "TLSCertificateConfiguration": {<certificate-configuration>}
        }
    }
}
```

The example below illustrates how to use a zip file with certificates
in Amazon S3 for certificate configuration:

    * A zip file with certificates in Amazon S3 is used as the key
     provider. (See [Providing certificates for
     encrypting data in transit with Amazon EMR encryption](emr-encryption-enable.md#emr-encryption-certificates "emr-encryption-enable.md#emr-encryption-certificates") for
     certificate requirements.)

```
"TLSCertificateConfiguration": {
	"CertificateProviderType": "PEM",
	"S3Object": "s3://MyConfigStore/artifacts/MyCerts.zip"
 }
```

The example below illustrates how to use a custom key provider for
certificate configuration:

    * A custom key provider is used. (See [Providing certificates for
     encrypting data in transit with Amazon EMR encryption](emr-encryption-enable.md#emr-encryption-certificates "emr-encryption-enable.md#emr-encryption-certificates") for
     certificate requirements.)

```
"TLSCertificateConfiguration": {
	"CertificateProviderType": "Custom",
	"S3Object": "s3://MyConfig/artifacts/MyCerts.jar",
	"CertificateProviderClass": "com.mycompany.MyCertProvider"
    }
```

2. Next, to ensure that the session tag can authorize Lake Formation, set the
   `LakeFormationConfiguration/AuthorizedSessionTagValue`
   property to `Amazon EMR`.
3. Use the following command to create the Amazon EMR security
   configuration.

```
aws emr create-security-configuration \
--name 'iamconfig-with-iam-lf' \
--security-configuration file://lf-runtime-roles-sec-cfg.json
```

Alternatively, you can use the [Amazon EMR
console](https://console.aws.amazon.com//emr "https://console.aws.amazon.com//emr") to create a security configuration with custom
settings.

## Step 2: Launch an Amazon EMR cluster

Now you’re ready to launch an EMR cluster with the security configuration
that you created in the previous step. For more information on security
configurations, see [Use security configurations to set up Amazon EMR cluster security](emr-security-configurations.md "emr-security-configurations.md") and [Runtime roles for Amazon EMR steps](emr-steps-runtime-roles.md "emr-steps-runtime-roles.md").

## Step 3: Set up Lake Formation-based column, row, or

cell-level permissions with Amazon EMR runtime roles

To apply fine-grained access control at the column, row, or cell level with
Lake Formation, the data lake administrator for Lake Formation must set `Amazon EMR` as the
value for the session tag configuration, `AuthorizedSessionTagValue`.
Lake Formation uses this session tag to authorize callers and provide access to the data
lake. You can set this session tag in the **Application integration
settings** section of the Lake Formation console. Replace
`123456789012` with your own AWS account
ID.

## Step 4: Configure AWS Glue and Lake Formation grants

for Amazon EMR runtime roles

To continue with your setup of Lake Formation based access control with Amazon EMR runtime
roles, you must configure AWS Glue and Lake Formation grants for Amazon EMR runtime roles. To
allow your IAM runtime roles to interact with Lake Formation, grant them access with
`lakeformation:GetDataAccess` and `glue:Get*`.

Lake Formation permissions control access to AWS Glue Data Catalog resources, Amazon S3 locations, and
the underlying data at those locations. IAM permissions control access to the
Lake Formation and AWS Glue APIs and resources. Although you might have the Lake Formation permission
to access a table in the data catalog (SELECT), your operation fails if you
don’t have the IAM permission on the `glue:Get*` API. For more
details about Lake Formation access control, see [Lake Formation access
control overview](../../../lake-formation/latest/dg/lf-permissions-overview.md "../../../lake-formation/latest/dg/lf-permissions-overview.md").

1. Create the
   `emr-runtime-roles-lake-formation-policy.json`
   file with the following content.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LakeFormationManagedAccess",
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess",
 "glue:Get*",
 "glue:Create*",
 "glue:Update*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

2. Create the related IAM policy.

```
aws iam create-policy \
--policy-name emr-runtime-roles-lake-formation-policy \
--policy-document file://emr-runtime-roles-lake-formation-policy.json
```

3. To assign this policy to your IAM runtime roles, follow the steps in
   [Managing
   AWS Lake Formation permissions](../../../lake-formation/latest/dg/managing-permissions.md "../../../lake-formation/latest/dg/managing-permissions.md").

You can now use runtime roles and Lake Formation to apply table and column level
permissions. You can also use a source identity to control actions and monitor

operations with AWS CloudTrail.

For each IAM role that you plan to use as a runtime role, set the following
trust policy, replacing `EMR_EC2_DefaultRole` with your instance
profile role. To modify the trust policy of an IAM role, see [Modifying a role trust policy](../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md "../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md").

```
{
   "Sid":"AllowAssumeRole",
   "Effect":"Allow",
   "Principal":{
     "AWS":"arn:aws:iam::`<AWS_ACCOUNT_ID>`:role/EMR_EC2_DefaultRole"
   },
   "Action":[
        "sts:AssumeRole",
        "sts:TagSession"
       ]
 }
```

For a detailed, end-to-end example, see [Introducing runtime roles for Amazon EMR steps](https://aws.amazon.com/blogs/big-data/introducing-runtime-roles-for-amazon-emr-steps-use-iam-roles-and-aws-lake-formation-for-access-control-with-amazon-emr/ "https://aws.amazon.com/blogs/big-data/introducing-runtime-roles-for-amazon-emr-steps-use-iam-roles-and-aws-lake-formation-for-access-control-with-amazon-emr/").

For information about how to integrate with Iceberg and AWS Glue Data Catalog for a
multi-catalog hierarchy, see [Configure Spark to access a multi-catalog hierarchy in
AWS Glue Data Catalog](../ReleaseGuide/emr-multi-catalog.md#emr-lakehouse-using-spark-access "../ReleaseGuide/emr-multi-catalog.md#emr-lakehouse-using-spark-access").
