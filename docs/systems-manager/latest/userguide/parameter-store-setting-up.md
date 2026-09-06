

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Setting up Parameter Store
<a name="parameter-store-setting-up"></a>

Before setting up parameters in Parameter Store, configure AWS Identity and Access Management (IAM) policies that provide principals in your account with permission to perform the actions you specify. 

In this section, you learn how to manually configure these policies using the IAM console, and how to assign them to users and user groups. You can also create and assign policies to control which parameter actions can be run on a managed node. 

This section also explains how to create Amazon EventBridge rules that let you receive notifications about changes to Systems Manager parameters. You can use EventBridge rules to invoke other actions in AWS based on changes in Parameter Store.

**Topics**
+ [Managing access to Parameter Store parameters using IAM policies](#sysman-paramstore-access)
+ [Choosing parameter tiers in Parameter Store](parameter-store-advanced-parameters.md)
+ [Managing Parameter Store throughput](parameter-store-throughput.md)
+ [Setting up notifications or triggering actions based on Parameter Store events](sysman-paramstore-cwe.md)

## Managing access to Parameter Store parameters using IAM policies
<a name="sysman-paramstore-access"></a>

 The IAM principal that accesses AWS Systems Manager parameters must have permission to perform the required SSM actions. The principal can be an IAM user, IAM role, Amazon EC2 instance profile, Lambda execution role, Amazon ECS task role, CodeBuild service role, or another AWS service role. 

 The following table describes the IAM permissions required for different Parameter Store actions. 



| Action | Required IAM privilege | Reference information | 
| --- | --- | --- | 
| Create or update a parameter | ssm:PutParameter | [PutParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutParameter.html) | 
| Retrieve one parameter | ssm:GetParameter | [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html) | 
| Retrieve multiple named parameters | ssm:GetParameters | [GetParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameters.html) | 
| Retrieve parameters under a path | ssm:GetParametersByPath | [GetParametersByPath](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParametersByPath.html) | 
| View parameter metadata | ssm:DescribeParameters | [DescribeParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeParameters.html) | 
| View parameter version history | ssm:GetParameterHistory | [GetParameterHistory](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameterHistory.html) | 
| Delete one parameter | ssm:DeleteParameter | [DeleteParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteParameter.html) | 
| Delete multiple parameters | ssm:DeleteParameters | [DeleteParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteParameters.html) | 

When using IAM policies to grant access to Systems Manager parameters, we recommend that you create and use *restrictive* IAM policies. For example, the following policy allows a principal to call the `DescribeParameters` and `GetParameters` API operations for a limited set of resources. The principal can get information about and use all parameters that begin with `prod-*`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeParameters"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:GetParameters"
            ],
            "Resource": "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:parameter/prod-*"
        }
    ]
}
```

------

**Important**  
If a user has access to a path, then the user can access all levels of that path. For example, if a user has permission to access path `/a`, then the user can also access `/a/b`. Even if a principal has explicitly been denied access in IAM for parameter `/a/b`, they can still call the `GetParametersByPath` API operation recursively for `/a` and view `/a/b`.

For trusted administrators, you can provide access to all Systems Manager parameter API operations by using a policy similar to the following example. This policy gives the user full access to all production parameters that begin with `dbserver-prod-*`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:PutParameter",
                "ssm:DeleteParameter",
                "ssm:GetParameterHistory",
                "ssm:GetParametersByPath",
                "ssm:GetParameters",
                "ssm:GetParameter",
                "ssm:DeleteParameters"
            ],
            "Resource": "arn:aws:ssm:{{us-east-1}}:111122223333:parameter/dbserver-prod-*"
        },
        {
            "Effect": "Allow",
            "Action": "ssm:DescribeParameters",
            "Resource": "*"
        }
    ]
}
```

------

### Denying permissions
<a name="sysman-paramstore-deny-permissions"></a>

Each API is unique and has distinct operations and permissions that you can allow or deny individually. An explicit deny in any policy overrides the allow.

**Note**  
The default AWS Key Management Service (AWS KMS) key has `Decrypt` permission for all IAM principals within the AWS account. If you want different access levels to `SecureString` parameters in your account, we don't recommend that you use the default key.

If you want all API operations retrieving parameter values to have the same behavior, then you can use a pattern like `GetParameter*` in a policy. The following example shows how to deny `GetParameter`, `GetParameters`, `GetParameterHistory`, and `GetParametersByPath` for all parameters beginning with `prod-*`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "ssm:GetParameter*"
            ],
            "Resource": "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:parameter/prod-*"
        }
    ]
}
```

------

The following example shows how to deny some commands while allowing the user to perform other commands on all parameters that begin with `prod-*`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "ssm:PutParameter",
                "ssm:DeleteParameter",
                "ssm:DeleteParameters",
                "ssm:DescribeParameters"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:GetParametersByPath",
                "ssm:GetParameters",
                "ssm:GetParameter",
                "ssm:GetParameterHistory"
            ],
            "Resource": "arn:aws:ssm:{{us-east-1}}:111122223333:parameter/prod-*"
        }
    ]
}
```

------

**Note**  
The parameter history includes all parameter versions, including the current one. Therefore, if a user is denied permission for `GetParameter`, `GetParameters`, and `GetParameterByPath` but is allowed permission for `GetParameterHistory`, they can see the current parameter, including `SecureString` parameters, using `GetParameterHistory`.

### Encrypting and decrypting parameters using AWS KMS keys
<a name="ps-kms-permissions"></a>

Parameter Store `SecureString` parameters use AWS KMS keys for encryption. AWS KMS encrypts the value by using either an AWS managed key or a customer managed key. For more information about AWS KMS and AWS KMS key, see the *[AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/)*.

All users within the customer account have access to the default AWS managed key. You can locate the Amazon Resource Name (ARN) of the default key in the AWS KMS console on the [AWS managed keys](https://console.aws.amazon.com/kms/home#/kms/defaultKeys) page. The default key is identified with `aws/ssm` in the **Alias** column. You might want to use the default key to encrypt `SecureString` parameters while preventing users from working with `SecureString` parameters. In this case, the IAM policies must explicitly deny access to the default key, as demonstrated in the following policy example.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": [
                "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/abcd1234-ab12-cd34-ef56-abcdeEXAMPLE"
            ]
        }
    ]
}
```

------

When using a customer managed key, the IAM policy that grants a principal access to a parameter or parameter path must provide explicit `kms:Encrypt` permissions for the key. For example, the following policy allows a principal to create, update, and view `SecureString` parameters that begin with `prod-` in the specified AWS Region and AWS account.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:PutParameter",
                "ssm:GetParameter",
                "ssm:GetParameters"
            ],
            "Resource": [
                "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:parameter/prod-*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:Encrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": [
                "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/1234abcd-12ab-34cd-56ef-12345EXAMPLE"
            ]
        }
    ]
}
```

------

**Note**  
The `kms:GenerateDataKey` permission is required for creating encrypted advanced parameters using the specified customer managed key. 

If you require fine-grained access control over the `SecureString` parameters in your account, use a customer managed key to protect and restrict access to these parameters. We also recommend using AWS CloudTrail to monitor `SecureString` parameter activities.

For more information, see the following topics:
+ [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) in the *IAM User Guide*
+ [Using key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *AWS Key Management Service Developer Guide*
+ [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*

### Allowing managed nodes to access specific parameters
<a name="sysman-paramstore-access-inst"></a>

To control which Parameter Store parameters a managed node can retrieve, you can attach an IAM policy to the instance role. If you choose the `SecureString` parameter type when you create your parameter, Systems Manager uses AWS KMS to encrypt the parameter value. You can view the AWS managed key by running the following command from the AWS CLI.

```
aws kms describe-key --key-id alias/aws/ssm
```

The following example allows nodes to get a parameter value only for parameters that begin with `prod-`. If the parameter is a `SecureString` parameter, then the node decrypts the string using AWS KMS.

**Note**  
Instance policies, like in the following example, are assigned to the instance role in IAM. For more information about configuring access to Systems Manager features, including how to assign policies to users and instances, see [Managing EC2 instances with Systems Manager](systems-manager-setting-up-ec2.md).

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:GetParameters"
            ],
            "Resource": [
                "arn:aws:ssm:{{us-east-1}}:111122223333:parameter/prod-*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": [
                "arn:aws:kms:{{us-east-1}}:111122223333:key/4914ec06-e888-4ea5-a371-5b88eEXAMPLE"
            ]
        }
    ]
}
```

------