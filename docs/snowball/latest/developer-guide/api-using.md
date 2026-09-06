

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/). 

# Using the Job Management API
<a name="api-using"></a>

The [ Job Management API for AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/api-reference/Welcome.html) is a network protocol based on HTTP (RFC 2616). For more information on this RFC, see [HTTP (RFC 2616)](https://www.ietf.org/rfc/rfc2616.txt) on the IETF website. For each call to the job management API, you make an HTTP request to the region-specific job management API endpoint for the AWS Region where you want to manage jobs. The API uses JSON (RFC 4627) documents for HTTP request/response bodies.

**Note**  
API calls made within the US regions for listing jobs or describing addresses return all jobs or addresses within the US for that account.

The job management API for Snowball Edge is an RPC model. In this model, there is a fixed set of operations and the syntax for each operation is known to clients without any previous interaction. Following, you can find a description of each API operation using an abstract RPC notation, with an operation name that does not appear on the wire. For each operation, the topic specifies the mapping to HTTP request elements. 

The specific job management operation to which a given request maps is determined by a combination of the request's method (GET, PUT, POST, or DELETE) and which of the various patterns its Request-URI matches. If the operation is PUT or POST, Snowball Edge extracts call arguments from the Request-URI path segment, query parameters, and the JSON object in the request body.

Although the operation name, such as `CreateJob`, doesn't appear on the wire, these operation names are meaningful in AWS Identity and Access Management (IAM) policies. The operation name is also used to name commands in command-line tools and elements of the AWS SDK APIs. For example, the AWS Command Line Interface (AWS CLI) command `create-job` maps to the `CreateJob` operation. The operation name also appears in CloudTrail logs for Snowball Edge API calls.

For information on installing and setting up the AWS CLI, including specifying what regions you want to make AWS CLI calls against, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).

**Note**  
The job management API provides a programmatic interface to the same functionality available in the [AWS Snowball Management Console](https://console.aws.amazon.com/importexport/home?region=us-west-2), that is to create and manage jobs for Snowball Edge. To transfer data locally with a Snowball appliance, use the Snowball Edge Client or the S3 SDK Adapter for Snowball Edge. For more information, see [Transferring Data with a Snowball](https://docs.aws.amazon.com/snowball/latest/ug/snowball-data-transfer.html) in the *AWS Snowball User Guide*.  
If you use a Snowball Edge, use the Snowball Edge Client to unlock the appliance. For more information, see [Using the Snowball Client](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-client.html) in the *AWS Snowball Developer Guide*.

## API Endpoint
<a name="api-using-endpoint"></a>

The API endpoint is the Domain Name Service (DNS) name used as a host in the HTTP URI for the API calls. These API endpoints are region-specific and take the following form.

```
snowball.{{aws-region}}.amazonaws.com
```

For example, the Snowball Edge API endpoint for the US West (Oregon) Region is the following.

```
snowball.us-west-2.amazonaws.com
```

For a list of AWS Regions that Snowball Edge supports (where you can create and manage jobs), see [AWS Import/Export](https://docs.aws.amazon.com/general/latest/gr/rande.html#ie-region) in the *AWS General Reference*.

The region-specific API endpoint defines the scope of the Snowball Edge resources that are accessible when you make an API call. For example, when you call the `ListJobs` operation using the preceding endpoint, you get a list of jobs in the US West (Oregon) Region that have been created in your account. 

## API Version
<a name="api-using-version"></a>

The version of the API being used for a call is identified by the first path segment of the request URI, and its form is an ISO 8601 date. The documentation describes API version 2016-06-30.

## API Permission Policy Reference
<a name="api-using-policies"></a>

The following policies are needed for creating jobs with the job management API for Snowball Edge.

**Role Trust Policy for Creating Jobs**

Using the job management API to create jobs requires the following trust policy.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "importexport.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "AWSIE"
        }
      }
    }
  ]
}
```

------

**Note**  
To learn more about trust policies, see [Modifying a Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html) in the IAM User Guide.

**Role Policy for Creating Import Jobs**

Creating an import job requires the following role policy.

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
                "s3:GetBucketLocation",
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketPolicy",
                "s3:PutObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts",
                "s3:PutObjectAcl"
            ],
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "snowball:*"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

------

**Role Policy for Creating Export Jobs**

Creating an export job requires the following role policy.

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
        "s3:GetBucketLocation",
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::*"
    },
    {
       "Effect": "Allow",
       "Action": [
         "snowball:*"
       ],
       "Resource": [
         "*"
       ]
    }
  ]
}
```

------

**Amazon S3 Bucket Policy Principal for Creating Jobs**

In some cases, the Amazon S3 buckets that you use with Snowball Edge have bucket policies in place that require listing the role session name of the assumed role. In these cases, you need to specify a principal in those policies that identifies `AWSImportExport-Validation`. The following Amazon S3 bucket policy example demonstrates how to do so. 

**Example**    
****  

```
{
	"Version":"2012-10-17",		 	 	 
	"Statement": {
		"Sid": "AllowAWSSnowballToCreateJobs",
		"Effect": "Allow",
		"Principal": {
			"AWS": [
				"arn:aws:iam::{{111122223333}}:role/rolename",
				"arn:aws:sts::{{111122223333}}:assumed-role/rolename/AWSImportExport-Validation",
				"arn:aws:iam::{{111122223333}}:root"
			]
		},
		"Action": "S3:*",
		"Resource": ["arn:aws:s3:::{{examplebucket}}/*"]
	}
}
```
In this policy example, we deny access to all principals except the one named in the `NotPrincipal` element. For more information on how to use `NotPrincipal`, see [NotPrincipal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#NotPrincipal) in the *IAM User Guide*.

**Note**  
For jobs in AWS GovCloud (US), Snowball Edge uses `AWSIEJob` as the role session name of the assumed role.

## Creating an IAM Role for Snowball Edge and Snowball Edge
<a name="create-iam-role"></a>

An IAM role policy must be created with read and write permissions for your Amazon S3 buckets. The IAM role must also have a trust relationship with Snowball Edge. Having a trust relationship means that AWS can write the data in the Snowball and in your Amazon S3 buckets, depending on whether you're importing or exporting data.

When you create a job in the AWS Snow Family Management Console, creating the necessary IAM role occurs in step 4 in the **Permission** section. This process is automatic. The IAM role that you allow Snowball Edge to assume is only used to write your data to your bucket when the Snowball with your transferred data arrives at AWS. The following procedure outlines that process.

**To create the IAM role for your import job**

1. Sign in to the AWS Management Console and open the AWS Snowball Edge console at [https://console.aws.amazon.com/importexport/](https://console.aws.amazon.com/importexport/). 

1. Choose **Create job**.

1. In the first step, fill out the details for your import job into Amazon S3, and then choose **Next**.

1. In the second step, under **Permission**, choose **Create/Select IAM Role**.

   The IAM Management Console opens, showing the IAM role that AWS uses to copy objects into your specified Amazon S3 buckets.

1. Review the details on this page, and then choose **Allow**.

   You return to the AWS Snow Family Management Console, where **Selected IAM role ARN** contains the Amazon Resource Name (ARN) for the IAM role that you just created.

1. Choose **Next** to finish creating your IAM role.

The preceding procedure creates an IAM role that has write permissions for the Amazon S3 buckets that you plan to import your data into. The IAM role that is created has one of the following structures, depending on whether it's for an import job or export job.

**IAM Role for an Import Job**

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
        "s3:GetBucketLocation",
        "s3:ListBucketMultipartUploads"
      ],
      "Resource": "arn:aws:s3:::*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketPolicy",
        "s3:PutObject",
        "s3:AbortMultipartUpload",
        "s3:ListMultipartUploadParts",
        "s3:PutObjectAcl"
      ],
      "Resource": "arn:aws:s3:::*"
    }
  ]
}
```

------

If you use server-side encryption with AWS KMS–managed keys (SSE-KMS) to encrypt the Amazon S3 buckets associated with your import job, you also need to add the following statement to your IAM role.

```
{
     "Effect": "Allow",
     "Action": [
       "kms:GenerateDataKey"
     ],
     "Resource": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}"
}
```

**IAM Role for an Export Job**

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
        "s3:GetBucketLocation",
        "s3:GetBucketPolicy",
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::*"
    }
  ]
}
```

------

If you use server-side encryption with AWS KMS–managed keys to encrypt the Amazon S3 buckets associated with your export job, you also need to add the following statement to your IAM role.

```
{
     "Effect": "Allow",
     "Action": [
            "kms:Decrypt"
      ],
      "Resource": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}"
}
```