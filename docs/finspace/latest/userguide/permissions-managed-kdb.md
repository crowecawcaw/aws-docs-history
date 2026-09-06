

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Permissions required for Managed kdb
<a name="permissions-managed-kdb"></a>

You must have certain IAM permissions to use Managed kdb. In addition to the [finspace:\*permissions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfinspace.html), you might need additional permissions to use the resources in your AWS account. FinSpace uses these permissions on your behalf to configure resources in your account where it needs to function. Add these permissions by using the IAM policies to IAM roles that you use to interact with Managed kdb.

The following table shows a list of permissions and what they are needed for.



<table>
<thead>
  <tr><th>Permissions (IAM actions)</th><th>Use for</th><th>Used by</th></tr>
</thead>
<tbody>
  <tr><td>"logs:CreateLogDelivery"</td><td rowspan="9">Creating and deleting CloudWatch logs</td><td rowspan="9">Users who create or delete the clusters</td></tr>
  <tr><td>"logs:GetLogDelivery"</td></tr>
  <tr><td>"logs:UpdateLogDelivery"</td></tr>
  <tr><td>"logs:DeleteLogDelivery"</td></tr>
  <tr><td>"logs:ListLogDeliveries"</td></tr>
  <tr><td>"logs:PutResourcePolicy"</td></tr>
  <tr><td>"logs:DescribeResourcePolicies"</td></tr>
  <tr><td>"logs:DescribeLogGroup"</td></tr>
  <tr><td>"logs:CreateLogGroup"</td></tr>
  <tr><td>"ec2:CreateVpcEndpoint"</td><td rowspan="3">Managing kdb clusters</td><td rowspan="3">Users who create or delete the clusters</td></tr>
  <tr><td>"ec2:DeleteVpcEndpoints"</td></tr>
  <tr><td>"ec2:DescribeSubnets"</td></tr>
  <tr><td>"ec2:AcceptTransitGatewayVpcAttachment"</td><td rowspan="2">Creating a connection between your Managed kdb environment and your transit gateway</td><td rowspan="2">Administrators who configure the transit gateway environment using the <code>UpdateKxEnvironmentNetwork</code> API</td></tr>
  <tr><td>"ec2:DescribeSubnets"</td></tr>
  <tr><td>"ram:CreateResourceShare"</td><td>Creating a resource share on the transit gateway</td><td>Users who update kdb environment</td></tr>
  <tr><td>“ram:GetResourceShareInvitiations”</td><td rowspan="2">Accepting resource share on private certificate authority for cluster TLS connection</td><td rowspan="2">Users who create kdb environment</td></tr>
  <tr><td>"ram:AcceptResourceShareInvitation"</td></tr>
  <tr><td>"iam:CreateServiceLinkedRole"</td><td>Creating the FinSpace service-linked role (SLR) when creating a kdb environment</td><td>Users who create kdb environment</td></tr>
  <tr><td>"ec2:DescribeTags"</td><td rowspan="2">Creating and describing tags on FinSpace managed VPC endpoints</td><td rowspan="2">Users who create and delete clusters</td></tr>
  <tr><td>"ec2:CreateTags"</td></tr>
  <tr><td>"finspace:*"</td><td>Performing actions to manage FinSpace resources</td><td>Users that manage resources in FinSpace</td></tr>
  <tr><td>"kms:CreateGrant"</td><td rowspan="2">Encrypting any customer data at rest</td><td rowspan="2">Users who create kdb environment</td></tr>
  <tr><td>"kms:RetireGrant"</td></tr>
  <tr><td>"ec2:DescribeTransitGateways"</td><td>Checking if the transit gateway exists</td><td>Users who configure the transit gateway environment using the UpdateKxEnvironmentNetwork API</td></tr>
  <tr><td>"s3:GetObject"</td><td rowspan="4">Controlling access for ingesting code and data into the service. </td><td rowspan="4">Users who create clusters, update code on clusters, or create changesets. See the sections below for additional details.</td></tr>
  <tr><td>"s3:GetObjectTagging"</td></tr>
  <tr><td>"s3:GetObjectVersion"</td></tr>
  <tr><td>"s3:ListBucket"</td></tr>
</tbody>
</table>


## Permissions FinSpace needs to resources in your account
<a name="permissions-fs"></a>

You will need to grant permission to FinSpace to access certain resources in your account. To do this, follow steps in the following sections.

### Granting permission to your AWS KMS key to encrypt data and code stored in Managed kdb
<a name="kdb-enviroment-kms-policy"></a>

You must grant the FinSpace service access by using the AWS KMS key policy to create Managed kdb changesets and load code onto a cluster. The following is an example of such a policy.

In the following example, replace each {{*user input placeholder*}} with your own values.

#### Sample AWS KMS key policy
<a name="collapsible-sample-kms-key-policy"></a>

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "FinSpaceServiceAccess",
    "Statement": [{
            "Sid": "FinSpace Permissions",
            "Effect": "Allow",
            "Principal": {
                "Service": "finspace.amazonaws.com"
            },
            "Action": [
                "kms:Decrypt",
                "kms:DescribeKey",
                "kms:Encrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*"
            ],
            "Resource": "arn:aws:kms:{{us-east-1}}:{{555555555555}}:key/f935d84c-d365-4753-875Y-1c014ab4f61Z",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{555555555555}}"
                }
            }
        }

    ]
}
```

------

### Granting permission to your Amazon S3 code bucket to load code onto your Managed kdb cluster
<a name="permissions-s3-code"></a>

To load code onto your cluster you must first grant the FinSpace service access to the Amazon S3 bucket that stores the code you want to load. The following is an example of the policy that you can use to grant access to code location.

#### Example policy to grant access to the code location
<a name="collapsible-policy-to-grant-principal-access"></a>

In the following example, replace each {{*user input placeholder*}} with your own values.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "FinSpaceServiceAccess",
    "Statement": [{
            "Effect": "Allow",
            "Principal": {
                "Service": "finspace.amazonaws.com"
            },
            "Action": [
                "s3:GetObject",
                "s3:GetObjectTagging",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::{{managed-kdb-code/*}}",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{555555555555}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:finspace:us-east-1:{{555555555555}}:kxEnvironment/<EnvironmentID>/*"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "finspace.amazonaws.com"
            },
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::{{managed-kdb-code}}",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{555555555555}}"
                },
                  "ArnLike": {
                    "aws:SourceArn": "arn:aws:finspace:us-east-1:{{555555555555}}:kxEnvironment/<EnvironmentID>/*"
                }
            }
        }
    ]
}
```

------

After you grant the FinSpace service access to the S3 bucket , you must ensure that the IAM role that you use when you [create a cluster](create-kdb-clusters.md) or when you [update the code on a cluster](update-cluster-code.md) has permission to access the files on the Amazon S3 bucket. The following is an example of the policy that you can use to grant access to the role.

In the following example, replace each {{*user input placeholder*}} with your own values.

#### Example policy for granting calling role access to the code location
<a name="collapsible-sample-iam-role-policy"></a>

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "FinSpaceServiceAccess",
    "Statement": [{
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectTagging",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::{{managed-kdb-code/}}*"
        },
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::{{managed-kdb-code}}"
        }
    ]
}
```

------

When you set permissions on the role, you can control which Amazon S3 locations a user can access. You can also set {{*Deny*}} policies on this role to prevent access to resources. For example, you can use the {{*Deny*}} policy to prevent access to resources in another account.

### Granting permission to your Amazon S3 data staging bucket to ingest data into Managed kdb
<a name="permissions-s3-bucket"></a>

To ingest data from Amazon S3 into your database through a changeset, you must first grant FinSpace access to the S3 bucket that stores the data you want to import as Managed kdb changesets. The following is an example of such a policy.

In the following example, replace each {{*user input placeholder*}} with your own values.

#### Example policy to grant the FinSpace service principal access to the code location
<a name="collapsible-permission-changesets"></a>

In the following example, replace each {{*user input placeholder*}} with your own values.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "FinSpaceServiceAccess",
    "Statement": [{
            "Effect": "Allow",
            "Principal": {
                "Service": "finspace.amazonaws.com"
            },
            "Action": [
                "s3:GetObject",
                "s3:GetObjectTagging",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::{{managed-kdb-data/*}}",

            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{555555555555}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:finspace:us-east-1:{{555555555555}}:kxEnvironment/<EnvironmentID>/*"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "finspace.amazonaws.com"
            },
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::{{managed-kdb-data}}",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{555555555555}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:finspace:us-east-1:{{555555555555}}:kxEnvironment/<EnvironmentID>/*"
                }
            }
        }
    ]
}
```

------

After you grant FinSpace access to the Amazon S3 bucket, you must ensure that the IAM role you use when you [create a changeset](using-kdb-db.md#kdb-db-changesets) has permission to access the files on the Amazon S3 bucket. The following is an example of such a policy.

In the following example, replace each {{*user input placeholder*}} with your own values.

#### Example policy to grant role access to the changeset location
<a name="collapsible-changeset-iam-role"></a>

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "FinSpaceServiceAccess",
    "Statement": [{
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectTagging",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::{{managed-kdb-data/*}}"
        },
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::{{managed-kdb-data}}"
        }
    ]
}
```

------

When you set permissions on the role, you can control which Amazon S3 locations a user can access. You can also set {{*Deny*}} policies on this role to prevent access to resources. For example, you can use the {{*Deny*}} policy to prevent access to resources in another account.