

# Identify your resources referencing specified AMIs
<a name="ec2-ami-references"></a>

You can identify your AWS resources that reference specified Amazon Machine Images (AMIs), regardless of whether the AMIs are public or private, or who owns them. This visibility helps you ensure your resources use the latest compliant AMIs.

**Key benefits**

Checking AMI references helps you:
+ Audit the use of AMIs in your account.
+ Check where specific AMIs are being referenced.
+ Maintain compliance by updating your resources to reference the latest AMIs.

 

**Topics**
+ [Supported resources](#ec2-ami-references-supported-resources)
+ [How AMI reference checks work](#how-ami-references-works)
+ [Required IAM permissions](#ami-references-required-permissions)
+ [Steps for checking AMI references](#ami-reference-procedures)

## Supported resources
<a name="ec2-ami-references-supported-resources"></a>

AMI references can be checked in:
+ EC2 instances
+ Launch templates
+ SSM parameters
+ Image Builder image recipes
+ Image Builder container recipes

## How AMI reference checks work
<a name="how-ami-references-works"></a>

**Basic operation**

When you run an AMI reference check, you:
+ Specify which AMIs to check.
+ Choose which resource types to scan.
+ Receive a list of your resources that reference the specified AMIs.

**Resource type selection**

In the console, you select the resource types to scan.

In the CLI, you specify resource types to scan using one or both of the following CLI parameters:
+ `IncludeAllResourceTypes`: Scans all supported resource types.
+ `ResourceTypes`: Scans your specified resource types.

**Response scoping**

You can scope the response for EC2 instances and launch templates by customizing the `ResourceTypeOptions` values using the `ResourceTypes` parameter. The console and `IncludeAllResourceTypes` parameter both use default option values. When `ResourceTypes` and `IncludeAllResourceTypes` are used together, the `ResourceTypes` option values take precedence over the defaults.

The following are the default values:


| Resource type | Scoping option (`OptionName`) | Purpose | Default values for `OptionValue` and console | 
| --- | --- | --- | --- | 
| EC2 instances | state-name | Filter by instance state | pending, running, shutting-down, terminated, stopping, stopped (all states) | 
| Launch templates | version-depth | Specify the number of launch template versions to check (starting from the most recent version) | 10 (most recent versions) | 

## Required IAM permissions
<a name="ami-references-required-permissions"></a>

To use the DescribeImageReferences API to identify your resources that are referencing specified AMIs, you need the following IAM permissions to describe the resources:
+ `ec2:DescribeInstances`
+ `ec2:DescribeLaunchTemplates`
+ `ec2:DescribeLaunchTemplateVersions`
+ `ssm:DescribeParameters`
+ `ssm:GetParameters`
+ `imagebuilder:ListImageRecipes`
+ `imagebuilder:ListContainerRecipes`
+ `imagebuilder:GetContainerRecipe`

**Example IAM policy for using the DescribeImageReferences API**  
The following example policy grants you the permissions to use the DescribeImageReferences API, which includes the permissions to describe EC2 instances, launch templates, Systems Manager parameters, Image Builder image recipes, and Image Builder container recipes.

------
#### [ JSON ]

****  

```
{
	"Version":"2012-10-17",		 	 	 
	"Statement": [
		{
			"Effect": "Allow",
			"Action": "ec2:DescribeImageReferences",
			"Resource": "*"
		},
		{
			"Effect": "Allow",
			"Action": [
				"ec2:DescribeInstances",
				"ec2:DescribeLaunchTemplates",
				"ec2:DescribeLaunchTemplateVersions",
				"ssm:DescribeParameters",
				"ssm:GetParameters",
				"imagebuilder:ListImageRecipes",
				"imagebuilder:ListContainerRecipes",
				"imagebuilder:GetContainerRecipe"
			],
			"Resource": "*",
			"Condition": {
				"ForAnyValue:StringEquals": {
					"aws:CalledVia": [
						"ec2-images.amazonaws.com"
					]
				}
			}
		}
	]
}
```

------

**Important**  
We strongly recommend using the AWS managed policy [`AmazonEC2ImageReferencesAccessPolicy`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ImageReferencesAccessPolicy.html) instead of creating the policy yourself. Creating a custom IAM policy that provides only the required permissions requires time and expertise, and will require updates as new resource types become available.  
The `AmazonEC2ImageReferencesAccessPolicy` managed policy:  
Grants all the permissions needed to use the DescribeImageReferences API (these include the permissions to describe EC2 instances, launch templates, Systems Manager parameters, and Image Builder container and image recipes).
Automatically supports new resource types as they become available (especially important when using the `IncludeAllResourceTypes` parameter).
You can attach the `AmazonEC2ImageReferencesAccessPolicy` policy to your IAM identities (users, groups, and roles).   
To view the permissions included in this policy, see [AmazonEC2ImageReferencesAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ImageReferencesAccessPolicy.html) in the *AWS Managed Policy Reference*.

## Steps for checking AMI references
<a name="ami-reference-procedures"></a>

Use the following procedures to identify which of your AWS resources are referencing specified AMIs.

------
#### [ Console ]

**To identify resources referencing specified AMIs**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select one or more AMIs to check for references.

1. Choose **Actions**, **AMI usage**, **View referenced resources**.

1. On the **View resources referencing selected AMIs** page:

   1. For **Resource types**, select one or more resource types.

   1. Choose **View resources**.

1. The **Resources referencing selected AMIs** section appears. The list displays the resources referencing the specified AMIs. Each row provides the following information:
   + **AMI ID** – The ID of the referenced AMI.
   + **Resource type** – The resource type of the resource referencing the AMI.
   + **Resource ID** – The ID of the resource referencing the AMI.

------
#### [ AWS CLI ]

**To check AMI references for specific resource types**  
Use the [describe-image-references](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-image-references.html) command with the `--resource-types` parameter. The following example checks EC2 instances (scoping by instance state), launch templates (scoping to the 20 most recent launch template versions), and other specific resource types.

```
aws ec2 describe-image-references \
    --image-ids {{ami-0abcdef1234567890}} {{ami-1234567890abcdef0}} \
    --resource-types \
        'ResourceType=ec2:Instance,ResourceTypeOptions=[{OptionName=state-name,OptionValues=[{{running}},{{pending}}]}]' \
        'ResourceType=ec2:LaunchTemplate,ResourceTypeOptions=[{OptionName=version-depth,OptionValues=[{{20}}]}]' \
        'ResourceType=ssm:Parameter' \
        'ResourceType=imagebuilder:ImageRecipe' \
        'ResourceType=imagebuilder:ContainerRecipe'
```

The following is example output.

```
{
    "ImageReferences": [
        {
            "ImageId": "ami-0abcdef1234567890",
            "ResourceType": "ec2:Instance",
            "Arn": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
        },
        {
            "ImageId": "ami-1234567890abcdef0",
            "ResourceType": "ec2:LaunchTemplate",
            "Arn": "arn:aws:ec2:us-east-1:123456789012:launch-template/lt-1234567890abcdef0"
        }
    ]
}
```

**To check AMI references for all the supported resource types**  
Use the [describe-image-references](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-image-references.html) command with the `--include-all-resource-types` parameter.

```
aws ec2 describe-image-references \
    --image-ids {{ami-0abcdef1234567890}} {{ami-1234567890abcdef0}} \
    --include-all-resource-types
```

**To check AMI references for all supported resource types and specific options**  
Use the [describe-image-references](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-image-references.html) command with both the `--include-all-resource-types` and `--resource-types` parameters. This example checks all resource types while scoping the response for EC2 instances to running or pending instances.

```
aws ec2 describe-image-references \
    --image-ids {{ami-0abcdef1234567890}} {{ami-1234567890abcdef0}} \
    --include-all-resource-types \
    --resource-types 'ResourceType=ec2:Instance,ResourceTypeOptions=[{OptionName=state-name,OptionValues=[{{running}},{{pending}}]}]'
```

------
#### [ PowerShell ]

**To check AMI references for specific resource types**  
Use the [Get-EC2ImageReference](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2ImageReference.html) cmdlet with the `-ResourceType` parameter. The following example checks EC2 instances (scoping by instance state), launch templates (scoping to the 20 most recent launch template versions), and other specific resource types.

```
Get-EC2ImageReference `
    -ImageId '{{ami-0abcdef1234567890}}', '{{ami-1234567890abcdef0}}' `
    -ResourceType @(
        @{
            ResourceType = 'ec2:Instance'
            ResourceTypeOptions = @(
                @{
                    OptionName = 'state-name'
                    OptionValues = @('{{running}}', '{{pending}}')
                }
            )
        },
        @{
            ResourceType = 'ec2:LaunchTemplate'
            ResourceTypeOptions = @(
                @{
                    OptionName = 'version-depth'
                    OptionValues = @('{{20}}')
                }
            )
        },
        @{
            ResourceType = 'ssm:Parameter'
        },
        @{
            ResourceType = 'imagebuilder:ImageRecipe'
        },
        @{
            ResourceType = 'imagebuilder:ContainerRecipe'
        }
    )
```

**To check AMI references for all the supported resource types**  
Use the [Get-EC2ImageReference](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2ImageReference.html) cmdlet with the `-IncludeAllResourceTypes` parameter.

```
Get-EC2ImageReference `
    -ImageId '{{ami-0abcdef1234567890}}', '{{ami-1234567890abcdef0}}' `
    -IncludeAllResourceTypes
```

**To check AMI references for all supported resource types and specific options**  
Use the [Get-EC2ImageReference](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2ImageReference.html) cmdlet with both the `-IncludeAllResourceTypes` and `-ResourceType` parameters. This example checks all resource types while scoping the response for EC2 instances to running or pending instances.

```
Get-EC2ImageReference `
    -ImageId '{{ami-0abcdef1234567890}}', '{{ami-1234567890abcdef0}}' `
    -IncludeAllResourceTypes `
    -ResourceType @(
        @{
            ResourceType = 'ec2:Instance'
            ResourceTypeOptions = @(
                @{
                    OptionName = 'state-name'
                    OptionValues = @({{'running'}}, '{{pending'}})
                }
            )
        }
    )
```

------