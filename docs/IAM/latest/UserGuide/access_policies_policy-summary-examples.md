

# Examples of policy summaries
<a name="access_policies_policy-summary-examples"></a>

The following examples include JSON policies with their associated [policy summaries](access_policies_understand-policy-summary.md), the [service summaries](access_policies_understand-service-summary.md), and the [action summaries](access_policies_understand-action-summary.md) to help you understand the permissions given through a policy.

## Policy 1: DenyCustomerBucket
<a name="example1"></a>

This policy demonstrates an allow and a deny for the same service.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "FullAccess",
            "Effect": "Allow",
            "Action": ["s3:*"],
            "Resource": ["*"]
        },
        {
            "Sid": "DenyCustomerBucket",
            "Action": ["s3:*"],
            "Effect": "Deny",
            "Resource": ["arn:aws:s3:::customer", "arn:aws:s3:::customer/*" ]
        }
    ]
}
```

------

***DenyCustomerBucket** Policy Summary:*

![Policy summary for DenyCustomerBucket showing S3 service with explicit deny access level.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-example1-dialog.png)


***DenyCustomerBucket S3 (Explicit deny)** Service Summary:*

![Service summary for DenyCustomerBucket S3 showing explicitly denied actions.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-action-example1-dialog.png)


***GetObject (Read)** Action Summary:*

![Action summary for GetObject showing denied resources in the DenyCustomerBucket policy.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-resource-example1-dialog.png)


## Policy 2: DynamoDbRowCognitoID
<a name="policy_example2"></a>

This policy provides row-level access to Amazon DynamoDB based on the user's Amazon Cognito ID.

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
                "dynamodb:DeleteItem",
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:UpdateItem"
            ],
            "Resource": [
                "arn:aws:dynamodb:us-west-1:123456789012:table/myDynamoTable"
            ],
            "Condition": {
                "ForAllValues:StringEquals": {
                    "dynamodb:LeadingKeys": [
                        "${cognito-identity.amazonaws.com:sub}"
                    ]
                }
            }
        }
    ]
}
```

------

***DynamoDbRowCognitoID** Policy Summary:*

![Policy summary for DynamoDbRowCognitoID showing DynamoDB service with allowed access level.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-example2-dialog.png)


***DynamoDbRowCognitoID DynamoDB (Allow)** Service Summary:*

![Service summary for DynamoDbRowCognitoID DynamoDB showing allowed actions.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-action-example2-dialog.png)


***GetItem (List)** Action Summary:*

![Action summary for GetItem showing allowed resources with conditions in the DynamoDbRowCognitoID policy.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-resource-example2-dialog.png)


## Policy 3: MultipleResourceCondition
<a name="policy_example3"></a>

This policy includes multiple resources and conditions.

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
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Resource": ["arn:aws:s3:::Apple_bucket/*"],
            "Condition": {"StringEquals": {"s3:x-amz-acl": ["public-read"]}}
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Resource": ["arn:aws:s3:::Orange_bucket/*"],
            "Condition": {"StringEquals": {
                "s3:x-amz-acl": ["custom"],
                "s3:x-amz-grant-full-control": ["1234"]
            }}
        }
    ]
}
```

------

***MultipleResourceCondition** Policy Summary:*

![Policy summary for MultipleResourceCondition showing S3 service with allowed access level.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-example3-dialog.png)


***MultipleResourceCondition S3 (Allow)** Service Summary:*

![Service summary for MultipleResourceCondition S3 showing allowed actions.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-action-example3-dialog.png)


***PutObject (Write)** Action Summary:*

![Action summary for PutObject showing allowed resources with conditions in the MultipleResourceCondition policy.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-resource-example3-dialog.png)


## Policy 4: EC2\_troubleshoot
<a name="policy_example4"></a>

The following policy allows users to get a screenshot of a running Amazon EC2 instance, which can help with EC2 troubleshooting. This policy also permits viewing information about the items in the Amazon S3 developer bucket. 

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
                "ec2:GetConsoleScreenshot"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::developer"
            ]
        }
    ]
}
```

------

***EC2\_Troubleshoot** Policy Summary:*

![Policy summary for EC2_Troubleshoot showing EC2 and S3 services with allowed access levels.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-example4-dialog.png)


***EC2\_Troubleshoot S3 (Allow)** Service Summary:*

![Service summary for EC2_Troubleshoot S3 showing allowed actions.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-action-example4-dialog.png)


***ListBucket (List)** Action Summary:*

![Action summary for ListBucket showing allowed resources in the EC2_Troubleshoot policy.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-resource-example4-dialog.png)


## Policy 5: CodeBuild\_CodeCommit\_CodeDeploy
<a name="example6"></a>

This policy provides access to specific CodeBuild, CodeCommit, and CodeDeploy resources. Because these resources are specific to each service, they appear only with the matching service. If you include a resource that does not match any services in the `Action` element, then the resource appears in all action summaries.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Stmt1487980617000",
            "Effect": "Allow",
            "Action": [
                "codebuild:*",
                "codecommit:*",
                "codedeploy:*"
            ],
            "Resource": [
                "arn:aws:codebuild:us-east-2:123456789012:project/my-demo-project",
                "arn:aws:codecommit:us-east-2:123456789012:MyDemoRepo",
                "arn:aws:codedeploy:us-east-2:123456789012:application:WordPress_App",
                "arn:aws:codedeploy:us-east-2:123456789012:instance/AssetTag*"
            ]
        }
    ]
}
```

------

***CodeBuild\_CodeCommit\_CodeDeploy** Policy Summary:*

![Policy summary for CodeBuild_CodeCommit_CodeDeploy showing multiple services with allowed access levels.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-example6-dialog.png)


***CodeBuild\_CodeCommit\_CodeDeploy CodeBuild (Allow)** Service Summary:*

![Service summary for CodeBuild_CodeCommit_CodeDeploy CodeBuild showing allowed actions.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-action-example6-dialog.png)


***CodeBuild\_CodeCommit\_CodeDeploy StartBuild (Write)** Action Summary:*

![Action summary for StartBuild showing allowed resources in the CodeBuild_CodeCommit_CodeDeploy policy.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policies-summary-resource-example6-dialog.png)
