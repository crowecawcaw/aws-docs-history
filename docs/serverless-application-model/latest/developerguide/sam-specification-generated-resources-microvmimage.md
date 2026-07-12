# CloudFormation resources generated when AWS::Serverless::MicrovmImage is specified

When you specify an `AWS::Serverless::MicrovmImage`, AWS Serverless Application Model
(AWS SAM) generates an `AWS::Lambda::MicrovmImage` base CloudFormation
resource.

**`AWS::Lambda::MicrovmImage`**

_`LogicalId`:_ `<microvmimage‑LogicalId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this CloudFormation resource)

In addition to this CloudFormation resource, when `AWS::Serverless::MicrovmImage` is
specified, AWS SAM also generates CloudFormation resources for the following scenarios:

###### Scenarios

- [BuildRoleArn property is not specified](#sam-specification-generated-resources-microvmimage-iam-role "#sam-specification-generated-resources-microvmimage-iam-role")

## BuildRoleArn property is not specified

When you don't specify the `BuildRoleArn` property of an `AWS::Serverless::MicrovmImage`,
AWS SAM generates an `AWS::IAM::Role`
CloudFormation resource with an inline policy granting the following permissions:

- `s3:GetObject` — scoped to the Amazon S3 bucket from `CodeUri`
- `logs:CreateLogGroup`, `logs:CreateLogStream`, `logs:PutLogEvents` — for build logs

The role trust policy allows the `lambda.amazonaws.com` service principal to assume the role.

**`AWS::IAM::Role`**

_`LogicalId`:_ ``<microvmimage‑LogicalId>`BuildRole`
