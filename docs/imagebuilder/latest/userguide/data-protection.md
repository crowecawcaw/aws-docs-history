

# Data protection and the AWS shared responsibility model in Image Builder
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in EC2 Image Builder. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Image Builder or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

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

```
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

```
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

```
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

```
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