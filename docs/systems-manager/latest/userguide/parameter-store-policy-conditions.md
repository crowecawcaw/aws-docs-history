

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Preventing access to Parameter Store API operations
<a name="parameter-store-policy-conditions"></a>

Using service-specific *[conditions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html)* supported by Systems Manager for AWS Identity and Access Management (IAM) policies, you can explicity allow or deny access to Parameter Store API operations and content. By using these conditions, you can allow only certain IAM Entities (users and roles) in your organization to call certain API actions, or prevent certain IAM Entities from running them. This includes actions run through the Parameter Store console, the AWS Command Line Interface (AWS CLI), and SDKs. 

Before you write a policy that denies access to particular parameters, review [How Parameter Store authorizes parameter retrieval](ps-retrieval-authorization.md). Parameter Store authorizes each retrieval operation independently, so a policy that denies only one action might not produce the result you intend.

**Topics**
+ [How Parameter Store authorizes parameter retrieval](ps-retrieval-authorization.md)
+ [Restricting access to specific parameters and paths](ps-restrict-parameter-access.md)
+ [Restricting decryption of `SecureString` parameter values](ps-restrict-decryption.md)
+ [Condition keys specific to Parameter Store](#ps-condition-keys)
+ [Preventing changes to existing parameters using `ssm:Overwrite`](#overwrite-condition)
+ [Preventing creation or updates to parameters that use a parameter policy using `ssm:Policies`](#parameter-policies-condition)

## Condition keys specific to Parameter Store
<a name="ps-condition-keys"></a>

Systems Manager supports two condition keys that are specific to Parameter Store. Both apply to the `PutParameter` operation and control how parameters can be created and updated.

`ssm:Overwrite`  
Controls whether a principal can update an existing parameter. See [Preventing changes to existing parameters using `ssm:Overwrite`](#overwrite-condition).

`ssm:Policies`  
Controls whether a principal can create or update a parameter that includes a parameter policy. See [Preventing creation or updates to parameters that use a parameter policy using `ssm:Policies`](#parameter-policies-condition).

To restrict which parameters a principal can *read*, use resource-level and action-level controls as described in [Restricting access to specific parameters and paths](ps-restrict-parameter-access.md) rather than condition keys.

## Preventing changes to existing parameters using `ssm:Overwrite`
<a name="overwrite-condition"></a>

Use the `ssm:Overwrite` condition to control whether IAM Entities can update existing parameters.

In the following sample policy, the `"Allow"` statement grants permission to create parameters by running the `PutParameter` API operation in the AWS account 123456789012 in the US East (Ohio) Region (us-east-2). 

However, the `"Deny"` statement prevents Entities from changing values of *existing* parameters because the `Overwrite` option is explicitly denied for the `PutParameter` operation. Therefore, Entities that are assigned this policy can create parameters, but not make changes to existing parameters.

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
                "ssm:PutParameter"
            ],
            "Resource": "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:parameter/*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "ssm:PutParameter"
            ],
            "Condition": {
                "StringEquals": {
                    "ssm:Overwrite": [
                        "true"
                    ]
                }
            },
            "Resource": "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:parameter/*"
        }
    ]
}
```

------

## Preventing creation or updates to parameters that use a parameter policy using `ssm:Policies`
<a name="parameter-policies-condition"></a>

User the `ssm:Policies` condition to control whether Entities can create parameters that include a parameter policy and update existing parameters that include a parameter policy.

In the following policy example, the `"Allow"` statement grants general permission to create parameters, but the `"Deny"` statement prevents Entities from creating or updating parameters that include a parameter policy in the the AWS account 123456789012 in the US East (Ohio) Region (us-east-2). Entities can still create or update parameters that aren't assigned a parameter policy.

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
                "ssm:PutParameter"
            ],
            "Resource": "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:parameter/*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "ssm:PutParameter"
            ],
            "Condition": {
                "StringEquals": {
                    "ssm:Policies": [
                        "true"
                    ]
                }
            },
            "Resource": "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:parameter/*"
        }
    ]
}
```

------