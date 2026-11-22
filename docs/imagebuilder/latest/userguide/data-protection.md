

# Data protection and the AWS shared responsibility model in Image Builder

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in EC2 Image Builder. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Image Builder or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

## Your responsibility for base images and other source content
<a name="source-image-trust"></a>

The base image that you specify in a recipe provides the operating system and the starting software for your output image. Components, resources that other accounts share with you, and imported virtual machine images also affect what the output image contains. Under the shared responsibility model, verifying that this content is authentic and comes from a source that you trust is your responsibility.

The build runs in your own AWS account. For an AMI, Image Builder launches a build instance from the base AMI that you specify. Components run on the build and test instances under the instance profile role from your infrastructure configuration. They run with root privileges on Linux and macOS, and with SYSTEM privileges on Windows. For a container image, Image Builder builds on the container base image that you specify and runs components inside the container.

When you create a recipe, Image Builder checks that you can access the base image and the components that the recipe references, and that they're compatible with the recipe. These checks confirm access, not origin. Image Builder doesn't check whether a base image or component comes from an owner that you trust, and it doesn't verify signatures or otherwise confirm that content is authentic.

A base image or component from an untrusted source can affect the output image and any instances or containers that you launch from it. To reduce this risk, do the following:
+ Use base images from trusted sources, such as Image Builder managed images, AMIs from Amazon or a verified provider, and images that you build yourself. For more information, see [Verified provider](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharing-amis.html#verified-ami-provider) in the *Amazon EC2 User Guide*.
+ Use Allowed AMIs to limit the public and shared AMIs that your account can discover and launch instances from. The settings also apply to the base images of your builds. If a base image isn't allowed, Image Builder can't find it, and the recipe or build fails. If you use Image Builder managed images, make sure that your criteria allow the AMIs behind them. Most match the `amazon` image provider, and images based on AWS Marketplace products match `aws-marketplace`. The Allowed AMIs feature doesn't restrict the AMIs that your account owns, so it doesn't affect the images that you build or their test instances. To see which AMIs your criteria affect before you restrict access, start in audit mode. For more information, see [Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html) in the *Amazon EC2 User Guide*.
+ Know which references can change between builds. For each build, Image Builder reads the current value of a base image parameter in AWS Systems Manager Parameter Store. It also resolves version wildcards, such as `x.x.x`, to the latest version, including new versions from the owner of a shared image or component. An image version without a build number, such as `1.0.0`, resolves to its latest build. A container image tag can also point to a different image at build time. To use a fixed base image, specify an AMI ID or an Image Builder build version ARN that ends with the build number, such as `.../1.0.0/1`. Otherwise, restrict who can change what these references point to.
+ Use container base images from registries and publishers that you trust. Image Builder doesn't verify image signatures, and it pulls a tagged base image again for each build. Verify the signatures of signed base images. For your own Amazon ECR repositories, turn on tag immutability or restrict who can push images. For more information, see [Signature verification](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-signing-verification.html) in the *Amazon Elastic Container Registry User Guide*.
+ Review any component that you didn't create before you add it to a recipe, including shared, third-party, and AWS Marketplace components. Check what the component does and who publishes it. Image Builder runs these components the same way as your own, with the same privileges and instance profile role.
+ Verify each file that a component downloads before the component uses it. For example, provide both the `checksum` and `algorithm` inputs to the `WebDownload` action. For more information, see [WebDownload (Linux, Windows, macOS)](toe-action-modules.md#action-modules-webdownload).
+ Test your images and scan them with Amazon Inspector. Tests check the conditions that you define, and scans look for known software vulnerabilities. Neither confirms where your source content came from. For more information, see [Amazon Inspector integration in Image Builder](integ-inspector.md).

For ISO disk images, see [Your responsibility for imported ISO disk images](#iso-import-media-trust).

## Your responsibility for build and test instances
<a name="build-instance-trust"></a>

Image Builder launches build and test instances in your own AWS account. The instances use the instance profile role, subnet, and security groups from your infrastructure configuration. Under the shared responsibility model, securing these instances is your responsibility. This includes the permissions of the instance profile role, the network settings, and who can start builds with that configuration.

All software on an instance, including software from the base image and every component, can use the permissions of the instance profile role. Any permission that you grant to the role is available to that software. To help secure your build environment, do the following:
+ Grant the instance profile role only the permissions that your builds need. Start with AmazonSSMManagedInstanceCore and the Image Builder managed policies for instance profiles, such as EC2InstanceProfileForImageBuilder. Add only the permissions that your components use, because all software on the instance can use them. For more information, see [Use AWS managed policies for EC2 Image Builder](security-iam-awsmanpol.md).
+ Limit who can create or update infrastructure configurations, and who can create images and pipelines that use them. Grant these permissions only to principals that you trust with the instance profile role. To limit which roles a principal can pass to Amazon EC2, scope its `iam:PassRole` permission. For more information, see [Grant a user permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) in the *IAM User Guide*.
+ Require Instance Metadata Service Version 2 (IMDSv2) on build and test instances. To do this, set `httpTokens` to `required` in the instance metadata settings of your infrastructure configuration. To enforce the setting, use the `imagebuilder:Ec2MetadataHttpTokens` condition key in policies for principals that create or update infrastructure configurations. For container image builds that require IMDSv2, set `httpPutResponseHopLimit` to at least 2. For more information, see [imagebuilder:Ec2MetadataHttpTokens](security_iam_service-with-iam.md#image-builder-security-ec2metadatatokens).
+ Use a subnet and security groups that allow only the network access that your builds need. For more information, see [Create an infrastructure configuration](create-infra-config.md).
+ Restrict access to any instances that you keep running after a build, for example to troubleshoot a failure. Terminate these instances when you finish, because they continue to run with the instance profile role.
+ If you build on an instance from an Auto Scaling group, treat the instance like a base image. Build only from Auto Scaling groups that you control. Image Builder creates the output AMI from that instance's own volumes. The instance keeps its own instance profile, instance metadata options, and network settings, instead of the settings in your infrastructure configuration. For more information, see [Build on an instance from an Auto Scaling group](infra-config-parent-instance.md).
+ Use a custom execution role for your pipelines and images. Image Builder uses the execution role to launch build and test instances. A custom role keeps your service control policies (SCPs) and resource control policies (RCPs) in effect for operations that Image Builder performs on your behalf. Builds that don't specify an execution role use the Image Builder service-linked role, whose permissions you can't edit. For more information, see [Service access](manage-image-workflows.md#wf-service-access).
+ Scope the `ec2:RunInstances` permission of your execution role to limit the AMIs that your builds launch from. Use a customer managed policy, or a `Deny` statement, with condition keys such as `ec2:Owner` or `ec2:ImageID`. Also allow the AMIs that your builds create, because Image Builder launches test instances from them.

## Control access with IAM policies and tags
<a name="access-control-trust"></a>

IAM policies, and the tags that they reference, control who can create, change, and use your Image Builder resources. Under the shared responsibility model, configuring this access is your responsibility. When you configure this access, do the following:
+ Use resource-level permissions to limit which Image Builder images and components each principal can use in recipes. Also limit which recipes, infrastructure configurations, and workflows each principal can build with, and who can start builds. To limit the AMIs that your builds launch from, use Allowed AMIs and the permissions of your execution role. For more information, see [Your responsibility for base images and other source content](#source-image-trust) and [Your responsibility for build and test instances](#build-instance-trust).
+ If you use tags for attribute-based access control, use the `aws:ResourceTag`, `aws:RequestTag`, and `aws:TagKeys` condition keys. Restrict who can add, change, or remove those tags on your Image Builder and Amazon EC2 resources. For more information, see [Authorization based on Image Builder tags](security_iam_service-with-iam.md#security-iam-service-with-ib-tags) and [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *IAM User Guide*.
+ Don't use tags as evidence of where an image came from. Any principal with tagging permissions can add or change tags. To track the lineage of your AMIs, use AMI watermarks, which only the owner of an AMI can attach. For more information, see [Track AMI lineage with watermarks](ami-watermarks.md).
+ Restrict who has `ssm:PutParameter` permission for any Systems Manager Parameter Store parameter that your recipes use as a base image. Image Builder reads the parameter value each time that it builds an image. For more information, see [Use a base image parameter in your recipe](tutorial-ssm-parameters-recipe.md).

## Your responsibility for imported ISO disk images
<a name="iso-import-media-trust"></a>

When you import a Windows ISO disk image, the ISO that you supply provides the operating system for the output AMI. Under the shared responsibility model, verifying that the media is authentic is your responsibility.

The import runs in your own AWS account, on a build instance that uses the instance profile role from your infrastructure configuration. During the import, Image Builder runs executables from the ISO and the applied Windows image with SYSTEM privileges under that role.

An ISO from an untrusted source can affect the output AMI and any instances that you launch from it. Obtain ISO files from Microsoft or an authorized reseller. For more information, see [Import verified Windows ISO disk images with Image Builder](import-iso-disk.md).

## Encryption and key management in Image Builder
<a name="ib-encryption"></a>

Image Builder encrypts the data that it stores at rest by default.

### Encryption at rest
<a name="ib-encryption-at-rest"></a>

Image Builder encrypts the following resources with a KMS key that Image Builder owns, unless you specify your own customer managed key when you create the resource:
+ **Components** – Image Builder encrypts the component document.
+ **Container recipes** – Image Builder encrypts the Dockerfile template.
+ **Image workflows** – Image Builder encrypts the workflow document.

### Key management
<a name="ib-key-management"></a>

You can manage your own keys through AWS KMS. However, you can't manage the KMS keys that Image Builder owns.

**Encryption context**  
As an additional integrity and authenticity check, Image Builder uses the Amazon Resource Name (ARN) of the resource as the [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) when it encrypts a component, container recipe, or workflow. For the inputs and outputs of `RunCommand` steps that Image Builder encrypts during a workflow run, Image Builder uses the ARN of the workflow build version. The encryption context also includes an `aws-crypto-public-key` key-value pair that the AWS Encryption SDK adds. AWS KMS decrypts the data key only when the request includes an exact, case-sensitive match of the encryption context. Image Builder supplies the encryption context, so you don't provide it.

### Encrypt image workflows with a customer managed key
<a name="ib-workflow-encrypt-cmk"></a>

To add a layer of protection, you can encrypt your Image Builder workflow resources with your own customer managed key. If you encrypt your Image Builder workflows with your customer managed key, two principals need permission to use the key: the principal that creates the workflow and your workflow execution role. You can revoke access at any time. If you revoke the access of your workflow execution role to the key, builds that use workflows encrypted with the key fail, because Image Builder can't decrypt the workflow document.

The process to grant Image Builder access to use your customer managed key has two steps, as follows:

**Step 1: Add key policy permissions for Image Builder workflows**  
When Image Builder runs your workflows, your workflow execution role decrypts the workflow document and encrypts and decrypts the inputs and outputs of `RunCommand` steps.

This example key policy grants access to your workflow execution role and grants your AWS account full access to the key. The encryption context condition uses wildcards to match the ARN of any workflow in your account, in any Region.

As a prerequisite for using image workflows, you created an IAM workflow execution role that grants permission for Image Builder to run workflow actions. The principal for the first statement shown in the key policy example here must specify your IAM workflow execution role.

**CreateWorkflow** encrypts the workflow document with the caller's credentials. The caller therefore needs `kms:GenerateDataKey`. To view the workflow document with **GetWorkflow**, or the inputs and outputs of `RunCommand` steps with **GetWorkflowStepExecution** or **ListWorkflowStepExecutions**, the caller needs `kms:Decrypt`.

For more information about customer managed keys, see [KMS key access and permissions](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html) in the *AWS Key Management Service Developer Guide*.

------
#### [ JSON ]

****  

```json
{
	"Version":"2012-10-17",		 	 	 
	"Statement": [
		{
			"Sid": "Allow access to build images with encrypted workflow",
			"Effect": "Allow",
			"Principal": {
				"AWS": "arn:aws:iam::{{111122223333}}:role/{{YourImageBuilderExecutionRole}}"
			},
			"Action": [
				"kms:Decrypt",
				"kms:GenerateDataKey"
			],
			"Resource": "*",
			"Condition": {
				"StringLike": {
					"kms:EncryptionContext:aws:imagebuilder:arn": "arn:aws:imagebuilder:*:{{111122223333}}:workflow/*"
				}
			}
		},
		{
			"Sid": "Allow access for key administrators",
			"Effect": "Allow",
			"Principal": {
				"AWS": "arn:aws:iam::{{111122223333}}:root"
			},
			"Action": [
				"kms:*"
			],
			"Resource": "arn:aws:kms:*:{{111122223333}}:key/*"
		}
	]
}
```

------

**Step 2: Grant key access to your workflow execution role**  
The IAM role that Image Builder assumes to run your workflows needs permission to use your customer managed key. Without access to your key, Image Builder won't be able to encrypt or decrypt your workflow resources with it.

Edit the policy for your workflow execution role to add the following policy statement.

------
#### [ JSON ]

****  

```json
{
	"Version":"2012-10-17",		 	 	 
	"Statement": [
		{
			"Sid": "AllowAccessToWorkflowKey",
			"Effect": "Allow",
			"Action": [
				"kms:Decrypt",
				"kms:GenerateDataKey"
			],
			"Resource": "arn:aws:kms:{{us-west-2}}:{{111122223333}}:key/key_ID",
			"Condition": {
				"StringLike": {
					"kms:EncryptionContext:aws:imagebuilder:arn": "arn:aws:imagebuilder:*:{{111122223333}}:workflow/*"
				}
			}
		}
	]
}
```

------

### AWS CloudTrail events for image workflows
<a name="ib-workflow-cloudtrail-examples"></a>

The following examples show typical AWS CloudTrail entries for encrypting and decrypting image workflows that are stored with a customer managed key.

**Example: GenerateDataKey**  
This example shows what a CloudTrail event might look like when Image Builder invokes the AWS KMS **GenerateDataKey** API action from the Image Builder **CreateWorkflow** API action. Image Builder must encrypt a new workflow before it creates the workflow resource.

```json
{
	"eventVersion": "1.08",
	"userIdentity": {
		"type": "AssumedRole",
		"principalId": "PRINCIPALID1234567890:workflow-role-name",
		"arn": "arn:aws:sts::111122223333:assumed-role/Admin/workflow-role-name",
		"accountId": "111122223333",
		"accessKeyId": "AKIAIOSFODNN7EXAMPLE",
		"sessionContext": {
			"sessionIssuer": {
				"type": "Role",
				"principalId": "PRINCIPALID1234567890",
				"arn": "arn:aws:iam::111122223333:role/Admin",
				"accountId": "111122223333",
				"userName": "Admin"
			},
			"webIdFederationData": {},
			"attributes": {
				"creationDate": "2023-11-21T20:29:31Z",
				"mfaAuthenticated": "false"
			}
		},
		"invokedBy": "imagebuilder.amazonaws.com"
	},
	"eventTime": "2023-11-21T20:31:03Z",
	"eventSource": "kms.amazonaws.com",
	"eventName": "GenerateDataKey",
	"awsRegion": "us-west-2",
	"sourceIPAddress": "imagebuilder.amazonaws.com",
	"userAgent": "imagebuilder.amazonaws.com",
	"requestParameters": {
		"encryptionContext": {
			"aws:imagebuilder:arn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/sample-encrypted-workflow/1.0.0/*",
			"aws-crypto-public-key": "{{key value}}"
		},
		"keyId": "arn:aws:kms:us-west-2:111122223333:alias/ExampleKMSKey",
		"numberOfBytes": 32
	},
	"responseElements": null,
	"requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
	"eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
	"readOnly": true,
	"resources": [
		{
			"accountId": "111122223333",
			"type": "AWS::KMS::Key",
			"ARN": "arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLEzzzzz"
		}
	],
	"eventType": "AwsApiCall",
	"managementEvent": true,
	"recipientAccountId": "111122223333",
	"eventCategory": "Management"
}
```

**Example: Decrypt**  
This example shows what a CloudTrail event might look like when Image Builder invokes the AWS KMS **Decrypt** API action from the Image Builder **GetWorkflow** API action. Image Builder pipelines need to decrypt a workflow resource before they can use it.

```json
{
	"eventVersion": "1.08",
	"userIdentity": {
		"type": "AssumedRole",
		"principalId": "PRINCIPALID1234567890:workflow-role-name",
		"arn": "arn:aws:sts::111122223333:assumed-role/Admin/workflow-role-name",
		"accountId": "111122223333",
		"accessKeyId": "AKIAIOSFODNN7EXAMPLE",
		"sessionContext": {
			"sessionIssuer": {
				"type": "Role",
				"principalId": "PRINCIPALID1234567890",
				"arn": "arn:aws:iam::111122223333:role/Admin",
				"accountId": "111122223333",
				"userName": "Admin"
			},
			"webIdFederationData": {},
			"attributes": {
				"creationDate": "2023-11-21T20:29:31Z",
				"mfaAuthenticated": "false"
			}
		},
		"invokedBy": "imagebuilder.amazonaws.com"
	},
	"eventTime": "2023-11-21T20:34:25Z",
	"eventSource": "kms.amazonaws.com",
	"eventName": "Decrypt",
	"awsRegion": "us-west-2",
	"sourceIPAddress": "imagebuilder.amazonaws.com",
	"userAgent": "imagebuilder.amazonaws.com",
	"requestParameters": {
		"keyId": "arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLEzzzzz",
		"encryptionAlgorithm": "SYMMETRIC_DEFAULT",
		"encryptionContext": {
			"aws:imagebuilder:arn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/sample-encrypted-workflow/1.0.0/*",
			"aws-crypto-public-key": "ABC123def4567890abc12345678/90dE/F123abcDEF+4567890abc123D+ef1=="
		}
	},
	"responseElements": null,
	"requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
	"eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
	"readOnly": true,
	"resources": [
		{
			"accountId": "111122223333",
			"type": "AWS::KMS::Key",
			"ARN": "arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLEzzzzz"
		}
	],
	"eventType": "AwsApiCall",
	"managementEvent": true,
	"recipientAccountId": "111122223333",
	"eventCategory": "Management"
}
```

## Data storage in Image Builder
<a name="ib-data-storage"></a>

Image Builder doesn't store any of your logs in the service. All logs are saved on your Amazon EC2 instance that is used to build the image, or in your Systems Manager automation logs.

## Inter-network Traffic Privacy in Image Builder
<a name="image-builder-internetwork"></a>

Connections are secured between Image Builder and on-premises locations, between AZs within an AWS Region, and between AWS Regions through HTTPS. There are no direct connections between accounts.