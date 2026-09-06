

# Using endpoint policies to control access with VPC endpoints
<a name="vpc-vpce.policy"></a>

This topic explains how you can attach a policy to VPC endpoints to controls access to your application (your service) and your Elastic Beanstalk environment. 

An endpoint policy is an AWS Identity and Access Management (IAM) resource policy that controls access from the endpoint to the specified service. The endpoint policy is specific to the endpoint. It's separate from any user or instance IAM policies that your environment might have and doesn't override or replace them. 

By default, a VPC endpoint allows full access to the service with which it's associated. When you create or modify an endpoint, you can attach an *endpoint policy* to it to control access to specific resources associated with the service. For details about authoring and using VPC endpoint policies, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

**Note**  
When you create restrictive endpoint policies you may need to add specific permissions to required resources, so that access to these resources isn't blocked by the endpoint policy. Doing so ensures that your environment continues to deploy and function properly.

The following example denies all users the permission to terminate an environment through the VPC endpoint, and allows full access to all other actions.

```
{
    "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": "*"
        },
        {
            "Action": "elasticbeanstalk:TerminateEnvironment",
            "Effect": "Deny",
            "Resource": "*",
            "Principal": "*"
        }
    ]
}
```

## Required Amazon S3 bucket permissions for restrictive VPC endpoint policies
<a name="AWSHowTo.S3.VPCendpoints"></a>

If you add restrictions to your VPC endpoint policies, you must include specific Amazon S3 bucket permissions to ensure that your environment continues to deploy and function properly. This section explains the required S3 buckets and includes example policies.

**Topics**
+ [S3 Buckets that store assets to manage environment platforms](#AWSHowTo.S3.VPCendpoints.required-permissions.assets)
+ [S3 Buckets owned by CloudFormation](#AWSHowTo.S3.VPCendpoints.required-permissions.cloudformation)
+ [S3 Buckets owned by customer accounts to store source code and other items](#AWSHowTo.S3.VPCendpoints.required-permissions.items)
+ [S3 Buckets owned by customer accounts to support Docker registry authentication](#AWSHowTo.S3.VPCendpoints.required-permissions.docker-auth)
+ [Updating your VPC endpoint policy](#AWSHowTo.S3.VPCendpoints.required-permissions.assets.permissions)

### S3 Buckets that store assets to manage environment platforms
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.assets"></a>

The Elastic Beanstalk service owns S3 buckets that store the assets associated with a solution stack (platform version). These assets include configuration files, the sample application, and available instance types. When Elastic Beanstalk creates and manages your environment it retrieves the required information for the specific platform version from the asset bucket for each corresponding AWS Region.

#### S3 Bucket ARN
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.assets.arn"></a>

 `arn:aws:s3:::elasticbeanstalk-samples-{{region}}` 

Amazon Linux 2 and later
+  `arn:aws:s3:::elasticbeanstalk-platform-assets-{{region}}` 
**Note**  
The bucket name follows a different convention for the *BJS *region. The string *public-beta-cn-north-1* is used in place of {{region}}. For example, `arn:aws:s3:::elasticbeanstalk-platform-assets-public-beta-cn-north-1`.

Windows Server, Amazon Linux (AMI), Amazon Linux 2 and later
+  `arn:aws:s3:::elasticbeanstalk-env-resources-{{region}}` 
+  `arn:aws:s3:::elasticbeanstalk-{{region}}` 

**Note**  
The bucket names for platform-assets and env-resources buckets follow different conventions in some regions. See the region-specific bucket naming patterns section below for details.

##### Region-specific bucket ARN patterns
<a name="AWSHowTo.S3.VPCendpoints.region-specific-buckets.collapsed"></a>



- **me-central-1**
  - **Bucket Type:** platform-assets / **Bucket ARN Pattern:** arn:aws:s3:::elasticbeanstalk-platform-assets-me-central-1-f08b818c
  - **Bucket Type:** env-resources / **Bucket ARN Pattern:** arn:aws:s3:::elasticbeanstalk-env-resources-me-central-1-f08b818c



#### Operations
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.assets.operations"></a>

GetObject

#### VPC endpoint policy example
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.assets.example"></a>

The following example illustrates how to provide access to the S3 buckets required for Elastic Beanstalk operations in the US East (Ohio) Region (us-east-2). The example lists all of the buckets for both Amazon Linux and Windows Server platforms. Update your policy to only include the buckets that apply to the operating system of your environment. 

##### Example policy
<a name="aAWSHowTo.S3.VPCendpoints.required-permissions.assets.example.collapsed"></a>

**Important**  
We recommend that you avoid using wildcard characters (\*) in place of specific Regions in this policy. For example, use `arn:aws:s3:::cloudformation-waitcondition-us-east-2/*` and don't use `arn:aws:s3:::cloudformation-waitcondition-*/*`. Using wildcards could provide access to S3 buckets that you don’t intend to grant access to. If you want to use the policy for more than one Region, we recommend repeating the first `Statement` block for each Region.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowRequestsToAWSResources",
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": ["s3:GetObject"],
            "Resource": [
                "arn:aws:s3:::elasticbeanstalk-platform-assets-{{us-east-2}}/*",
                "arn:aws:s3:::elasticbeanstalk-env-resources-{{us-east-2}}/*",
                "arn:aws:s3:::elasticbeanstalk-env-resources-{{us-east-2}}/*",
                "arn:aws:s3:::elasticbeanstalk-samples-{{us-east-2}}/*"
            ]
         }
    ]
}
```

------

### S3 Buckets owned by CloudFormation
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.cloudformation"></a>

Elastic Beanstalk uses CloudFormation to create resources for your environment. CloudFormation owns S3 buckets in each AWS Region to monitor responses to wait conditions.

Services like Elastic Beanstalk communicate with CloudFormation by sending requests to a presigned Amazon S3 URL for the S3 bucket that CloudFormation owns. CloudFormation creates the presigned Amazon S3 URL using the `cloudformation.amazonaws.com` service principal.

For more detailed information, see [Considerations for CloudFormation VPC endpoints](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-vpce-bucketnames.html#cfn-setting-up-vpc-considerations) in the *AWS CloudFormation User Guide*. To learn more about presigned URLs, see [Working with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) in the *Amazon S3 User Guide*.

#### S3 Bucket ARN
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.cloudformation.arn"></a>
+  `arn:aws:s3:::cloudformation-waitcondition-{{region}}` 

  When using wait conditions, region names do contain dashes. For example, *us-west-2*.
+  `arn:aws:s3:::cloudformation-custom-resource-response-{{region}}` 

  When using custom resources, region names don't contain dashes. For example, *uswest2*.

#### Operations
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.cloudformation.operations"></a>

GetObject

#### VPC endpoint policy example
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.cloudformation.example"></a>

The following example illustrates how to provide access to the S3 buckets required for Elastic Beanstalk operations in the US East (Ohio) Region (us-east-2).

##### Example policy
<a name="aAWSHowTo.S3.VPCendpoints.required-permissions.cloudformation.example.collapsed"></a>

**Important**  
We recommend that you avoid using wildcard characters (\*) in place of specific Regions in this policy. For example, use `arn:aws:s3:::cloudformation-waitcondition-us-east-2/*` and don't use `arn:aws:s3:::cloudformation-waitcondition-*/*`. Using wildcards could provide access to S3 buckets that you don’t intend to grant access to. If you want to use the policy for more than one Region, we recommend repeating the first `Statement` block for each Region.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowRequestsToCloudFormation",
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": ["s3:GetObject"],
            "Resource": [
                "arn:aws:s3:::cloudformation-waitcondition-{{us-east-2}}/*",
                "arn:aws:s3:::cloudformation-custom-resource-response-{{us-east-2}}/*"
            ]
         }
    ]
}
```

------

### S3 Buckets owned by customer accounts to store source code and other items
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.items"></a>

This bucket is owned by the AWS customer account that owns the environment. It stores resources that are specific to your environment, such as source code and requested logs.

#### S3 Bucket ARN
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.items.arn"></a>

 `arn:aws:s3:::elasticbeanstalk-{{region}}-{{account-id}}` 

#### Operations
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.items.operations"></a>
+ GetObject
+ GetObjectAcl
+ PutObject
+ PutObjectAcl
+ ListBucket

#### VPC endpoint policy example
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.items.example"></a>

The following example illustrates how to provide access to the S3 buckets required for Elastic Beanstalk operations in the US East (Ohio) Region (us-east-2) and for the example AWS account id 123456789012.

##### Example policy
<a name="aAWSHowTo.S3.VPCendpoints.required-permissions.items.example.collapsed"></a>

**Important**  
We recommend that you avoid using wildcard characters (\*) in place of specific Regions in this policy. For example, use `arn:aws:s3:::cloudformation-waitcondition-us-east-2/*` and don't use `arn:aws:s3:::cloudformation-waitcondition-*/*`. Using wildcards could provide access to S3 buckets that you don’t intend to grant access to. If you want to use the policy for more than one Region, we recommend repeating the first `Statement` block for each Region.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowRequestsToCustomerItems",
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": [
               "s3:GetObject",
               "s3:GetObjectAcl",
               "s3:PutObject",
               "s3:PutObjectAcl",
               "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::elasticbeanstalk-{{us-east-2}}-{{123456789012}}/*"
            ]
         }
    ]
}
```

------

### S3 Buckets owned by customer accounts to support Docker registry authentication
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.docker-auth"></a>

This bucket only applies to environments based on the Docker platform. The bucket stores a file used to authenticate to a private Docker registry that resides on an S3 bucket provisioned by the customer. For more information, see [Using the `Dockerrun.aws.json` v3 file](docker-configuration.remote-repo.md#docker-configuration.remote-repo.dockerrun-aws) in the Docker platform chapter of this guide.

#### S3 Bucket ARN
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.docker-auth.arn"></a>

The ARN varies by customer account.

The S3 bucket ARN has the following format: `arn:aws:s3:::{{bucket-name}}`

#### Operations
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.docker-auth.operations"></a>

GetObject

#### VPC endpoint policy example
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.docker-auth.example"></a>

The following example illustrates how to provide access to an S3 bucket with the name amzn-s3-demo-bucket1.

##### Example policy
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.docker-auth.example.collapsed"></a>

------
#### [ JSON ]

****  

```
  {
  "Version":"2012-10-17",		 	 	 
  "Statement": [
     {
        "Sid": "AllowRequestsToDockerRegistryAuth",
         "Effect": "Allow",
         "Action": [
            "s3:GetObject"
          ],
      "Resource": [
        "arn:aws:s3:::{{amzn-s3-demo-bucket1}}"
      ]
    }
  ]
}
```

------

### Updating your VPC endpoint policy
<a name="AWSHowTo.S3.VPCendpoints.required-permissions.assets.permissions"></a>

Because a VPC endpoint has only one policy attached, you must combine all of the permissions into the one policy. The following example provides all of the previous examples combined into one. 

For details about authoring and using VPC endpoint policies, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

Like the previous examples, the following one illustrates how to provide access to the S3 buckets required for Elastic Beanstalk operations in the US East (Ohio) Region (us-east-2). It also includes buckets with example AWS account id 123456789012 and example bucket name amzn-s3-demo-bucket1.

**Important**  
We recommend that you avoid using wildcard characters (\*) in place of specific Regions in this policy. For example, use `arn:aws:s3:::cloudformation-waitcondition-us-east-2/*` and don't use `arn:aws:s3:::cloudformation-waitcondition-*/*`. Using wildcards could provide access to S3 buckets that you don’t intend to grant access to. If you want to use the policy for more than one Region, we recommend repeating the first `Statement` block for each Region.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowRequestsToAWSResources",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::elasticbeanstalk-platform-assets-{{us-east-2}}/*",
                "arn:aws:s3:::elasticbeanstalk-env-resources-{{us-east-2}}/*",
                "arn:aws:s3:::elasticbeanstalk-samples-{{us-east-2}}/*"
            ]
        },
        {
            "Sid": "AllowRequestsToCloudFormation",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::cloudformation-waitcondition-{{us-east-2}}/*",
                "arn:aws:s3:::cloudformation-custom-resource-response-{{us-east-2}}/*"
            ]
        },
        {
            "Sid": "AllowRequestsToCustomerItems",
            "Effect": "Allow",
            "Action": [
               "s3:GetObject",
               "s3:GetObjectAcl",
              "s3:PutObject",
               "s3:PutObjectAcl",
               "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::elasticbeanstalk-{{us-east-2}}-{{123456789012}}/*"
            ]
        },
        {
            "Sid": "AllowRequestsToDockerRegistryAuth",
            "Effect": "Allow",
            "Action": [
            "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket1}}"
            ]
        }
    ]
}
```

------