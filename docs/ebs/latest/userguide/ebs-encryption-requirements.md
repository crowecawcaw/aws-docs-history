

# Requirements for Amazon EBS encryption
<a name="ebs-encryption-requirements"></a>

Before you begin, verify that the following requirements are met.

**Topics**
+ [Supported volume types](#ebs-encryption-volume-types)
+ [Supported instance types](#ebs-encryption_supported_instances)
+ [Permissions for users](#ebs-encryption-permissions)
+ [Permissions for instances](#ebs-encryption-instance-permissions)

## Supported volume types
<a name="ebs-encryption-volume-types"></a>

Encryption is supported by all EBS volume types. You can expect the same IOPS performance on encrypted volumes as on unencrypted volumes, with a minimal effect on latency. You can access encrypted volumes the same way that you access unencrypted volumes. Encryption and decryption are handled transparently, and they require no additional action from you or your applications.

## Supported instance types
<a name="ebs-encryption_supported_instances"></a>

Amazon EBS encryption is available on all [ current generation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#current-gen-instances) and [ previous generation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#previous-gen-instances) instance types.

## Permissions for users
<a name="ebs-encryption-permissions"></a>

When you use a KMS key for EBS encryption, the KMS key policy allows any user with access to the required AWS KMS actions to use this KMS key to encrypt or decrypt EBS resources. You must grant users permission to call the following actions in order to use EBS encryption:
+ `kms:CreateGrant`
+ `kms:Decrypt`
+ `kms:DescribeKey`
+ `kms:GenerateDataKeyWithoutPlaintext`
+ `kms:ReEncrypt`

**Tip**  
To follow the principle of least privilege, do not allow full access to `kms:CreateGrant`. Instead, use the `kms:GrantIsForAWSResource` condition key to allow the user to create grants on the KMS key only when the grant is created on the user's behalf by an AWS service, as shown in the following example.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "kms:CreateGrant",
            "Resource": [
                "arn:aws:kms:us-east-2:123456789012:key/abcd1234-a123-456d-a12b-a123b4cd56ef"
            ],
            "Condition": {
                "Bool": {
                    "kms:GrantIsForAWSResource": true
                }
            }
        }
    ]
}
```

------

For more information, see [Allows access to the AWS account and enables IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam) in the **Default key policy** section in the *AWS Key Management Service Developer Guide*.

## Permissions for instances
<a name="ebs-encryption-instance-permissions"></a>

When an instance attempts to interact with an encrypted AMI, volume, or snapshot, a KMS key grant is issued to the instance's identity-only role. The identity-only role is an IAM role that is used by the instance to interact with encrypted AMIs, volumes, or snapshots on your behalf. 

Identity-only roles do not need to be manually created or deleted, and they have no policies associated with them. Additionally, you can't access the identity-only role credentials.

**Note**  
Identity-only roles are not used by applications on your instance to access other AWS KMS encrypted resources, such as Amazon S3 objects or Dynamo DB tables. These operations are done using the credentials of an Amazon EC2 instance role, or other AWS credentials that you have configured on your instance.

Identity-only roles are subject to [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCPs), and [KMS key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html). If an SCP or KMS key denies the identity-only role access to a KMS key, you may fail to launch EC2 instances with encrypted volumes, or using encrypted AMIs or snapshots.

If you are creating an SCP or key policy that denies access based on network location using the `aws:SourceIp`, `aws:VpcSourceIp`, `aws:SourceVpc`, or `aws:SourceVpce` AWS global condition keys, then you must make sure that these policy statements do not apply to instance-only roles. For example policies, see [Data Perimeter Policy Examples](https://github.com/aws-samples/data-perimeter-policy-examples/tree/main).

Identity-only role ARNs use the following format:

```
arn:{{aws-partition}}:iam::{{account_id}}:role/aws:ec2-infrastructure/{{instance_id}}
```

When a key grant is issued to an instance, the key grant is issued to the assumed-role session specific to that instance. The grantee principal ARN uses the following format:

```
arn:{{aws-partition}}:sts::{{account_id}}:assumed-role/aws:ec2-infrastructure/{{instance_id}}
```