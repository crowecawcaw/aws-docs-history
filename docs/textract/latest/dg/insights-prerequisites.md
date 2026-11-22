

# Prerequisites and setup

Before you run an analysis job, set up the AWS account, AWS Regions, input files, IAM permissions, and AWS Command Line Interface (AWS CLI) that Amazon Textract Insights requires.

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).

## AWS Regions
<a name="insights-prerequisites-regions"></a>

Amazon Textract Insights is available in the following AWS Regions:
+ US East (N. Virginia) — us-east-1
+ US West (Oregon) — us-west-2

Your Amazon S3 input and output buckets must be in the same AWS Region as the request.

## Supported input file types
<a name="insights-prerequisites-input-types"></a>

Amazon Textract Insights accepts PDF, PNG, JPEG, and TIFF files. DOCX files are not supported. For input size limits, such as the maximum pages per document insights job, see [Limits and quotas](insights-quotas.md). For the languages that Amazon Textract Insights supports, see [Supported languages](supported-languages.md).

## IAM permissions
<a name="insights-prerequisites-iam"></a>

Attach a policy to the IAM identity that calls Amazon Textract Insights. The identity needs permissions for the Amazon Textract Insights actions it uses, plus `s3:GetObject` on the input location and `s3:PutObject` on the output location.

The following policy grants the actions needed for the full workflow — managing projects and blueprints, starting and monitoring jobs, and reading and writing the Amazon S3 objects. Scope the resources to your own account and buckets.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "TextractInsightsActions",
      "Effect": "Allow",
      "Action": [
        "textract:CreateProject",
        "textract:GetProject",
        "textract:UpdateProject",
        "textract:DeleteProject",
        "textract:ListProjects",
        "textract:CreateBlueprint",
        "textract:CreateBlueprintVersion",
        "textract:GetBlueprint",
        "textract:UpdateBlueprint",
        "textract:DeleteBlueprint",
        "textract:ListBlueprints",
        "textract:StartDocumentInsights",
        "textract:GetDocumentInsights",
        "textract:TagResource",
        "textract:UntagResource",
        "textract:ListTagsForResource"
      ],
      "Resource": "*"
    },
    { "Sid": "ReadInputDocuments", "Effect": "Allow", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*" },
    { "Sid": "WriteOutputResults", "Effect": "Allow", "Action": "s3:PutObject", "Resource": "arn:aws:s3:::amzn-s3-demo-destination-bucket/*" },
    { "Sid": "TutorialUploadInput", "Effect": "Allow", "Action": "s3:PutObject", "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*" },
    { "Sid": "TutorialReadOutput", "Effect": "Allow", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::amzn-s3-demo-destination-bucket/*" },
    { "Sid": "TutorialListOutput", "Effect": "Allow", "Action": "s3:ListBucket", "Resource": "arn:aws:s3:::amzn-s3-demo-destination-bucket" }
  ]
}
```

The three Tutorial\* statements are needed for the tutorial, where the same identity uploads the input document and downloads the results. If your application uses a different identity to upload documents or read results, you can remove them.

If you call only part of the workflow, you can remove the actions you do not use. For example, if you do not create custom blueprints, you can omit the `CreateBlueprint`, `CreateBlueprintVersion`, and `UpdateBlueprint` actions.

If you encrypt your data with a customer managed AWS KMS key, your identity also needs `kms:DescribeKey`, `kms:GenerateDataKey`, and `kms:Decrypt` on that key. See [Data protection and encryption](insights-data-protection.md).

If you do not tag resources, you can omit the `TagResource`, `UntagResource`, and `ListTagsForResource` actions. See [Tagging Amazon Textract Insights resources](insights-tagging.md).

## Set up the AWS CLI
<a name="insights-prerequisites-cli"></a>

Amazon Textract Insights is available through the AWS CLI under the `aws textract` namespace. Install the AWS CLI and configure credentials for the IAM identity you set up above:

```
aws configure
```

Provide the access key, secret key, and a default AWS Region (us-east-1 or us-west-2). You can override the AWS Region per command with `--region`.

Verify your setup by listing your projects:

```
aws textract list-projects --region us-east-1
```

An empty list (or a list of your existing projects) confirms that your credentials and permissions are working.

## Next steps
<a name="insights-prerequisites-next-steps"></a>
+ To run an end-to-end job, see [Tutorial: Process your first document](insights-tutorial.md).
+ To understand projects and the operations you use to manage them, see [Working with projects](insights-working-with-projects.md).