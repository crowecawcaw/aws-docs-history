# Create a Braket notebook instance using CloudFormation

###### Tip

**Learn the foundations of quantum computing with AWS!**
Enroll in the [Amazon Braket Digital Learning Plan](https://skillbuilder.aws/learning-plan/EH35DWGU3R/amazon-braket--knowledge-badge-readiness-path-includes-labs "https://skillbuilder.aws/learning-plan/EH35DWGU3R/amazon-braket--knowledge-badge-readiness-path-includes-labs")
and earn your own Digital badge after completing a series of learning courses and a digital assessment.

You can use CloudFormation to manage your Amazon Braket notebook instances. Braket notebook
instances are built on Amazon SageMaker AI. With CloudFormation, you can provision a notebook instance with a
template file that describes the intended configuration. The template file is written in JSON
or YAML format. You can create, update, and delete instances in an orderly and repeatable
fashion. You may find this useful when you manage multiple Braket notebook instances in your
AWS account.

After you create a CloudFormation template for a Braket notebook, you use CloudFormation to deploy the
resource. For more information, see [Creating a stack on
the CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md") in the _CloudFormation user guide_.

To create a Braket notebook instance using CloudFormation, you perform these three
steps:

1. Create a SageMaker AI lifecycle configuration script.
2. Create an AWS Identity and Access Management (IAM) role to be assumed by SageMaker AI.
3. Create a SageMaker AI notebook instance with the prefix
   `amazon-braket-`
   You can reuse the lifecycle configuration for all of the Braket notebooks that you
   create. You can also reuse the IAM role for the Braket notebooks that you assign the same
   execution permissions.

###### In this section:

- [Step 1: Create a SageMaker AI
  lifecycle configuration script](#braket-create-cloudformation-template-step-1 "#braket-create-cloudformation-template-step-1")
- [Step 2: Create the IAM role
  assumed by Amazon SageMaker AI](#braket-create-cloudformation-template-step-2 "#braket-create-cloudformation-template-step-2")
- [Step 3: Create a SageMaker AI
  notebook instance with the prefix amazon-braket-](#braket-create-cloudformation-template-step-3 "#braket-create-cloudformation-template-step-3")

## Step 1: Create a SageMaker AI

lifecycle configuration script

Use the following template to create a [SageMaker AI lifecycle configuration
script](../../../sagemaker/latest/dg/notebook-lifecycle-config.md "../../../sagemaker/latest/dg/notebook-lifecycle-config.md"). The script customizes a SageMaker AI notebook instance for Braket. For
configuration options for the lifecycle CloudFormation resource, see [AWS::SageMaker::NotebookInstanceLifecycleConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.md") in the _CloudFormation user
guide_.

```
BraketNotebookInstanceLifecycleConfig:
    Type: "AWS::SageMaker::NotebookInstanceLifecycleConfig"
    Properties:
      NotebookInstanceLifecycleConfigName: BraketLifecycleConfig-${AWS::StackName}
      OnStart:
      - Content:
          Fn::Base64: |
            #!/usr/bin/env bash
            sudo -u ec2-user -i ≪EOS
            curl -o braket-notebook-lcc.zip https://d3ded4lzb1lnme.cloudfront.net/notebook/braket-notebook-lcc.zip
            unzip braket-notebook-lcc.zip
            ./install.sh
            EOS

            exit 0
```

## Step 2: Create the IAM role

assumed by Amazon SageMaker AI

When you use a Braket notebook instance, SageMaker AI performs operations on your behalf. For
example, suppose you run a Braket notebook using a circuit on a supported device. Within
the notebook instance, SageMaker AI runs the operation on Braket for you. The notebook execution
role defines the exact operations that SageMaker AI is permitted to execute on your behalf. For
more information, see [SageMaker AI roles](../../../sagemaker/latest/dg/sagemaker-roles.md "../../../sagemaker/latest/dg/sagemaker-roles.md") in the
_Amazon SageMaker AI developer guide_.

Use the following example to create a Braket notebook execution role with the required
permissions. You can modify the policies according to your needs.

###### Note

Make sure that the role has permission for the `s3:ListBucket` and
`s3:GetObject`operations on Amazon S3 buckets prefixed with
`braketnotebookcdk-"`. The lifecycle configuration script requires these
permissions to copy the Braket notebook installation script.

```
ExecutionRole:
    Type: "AWS::IAM::Role"
    Properties:
      RoleName: !Sub AmazonBraketNotebookRole-${AWS::StackName}
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
        -
          Effect: "Allow"
          Principal:
            Service:
              - "sagemaker.amazonaws.com"
          Action:
          - "sts:AssumeRole"
      Path: "/service-role/"
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AmazonBraketFullAccess
      Policies:
        -
          PolicyName: "AmazonBraketNotebookPolicy"
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - s3:GetObject
                  - s3:PutObject
                  - s3:ListBucket
                Resource:
                  - arn:aws:s3:::amazon-braket-*
                  - arn:aws:s3:::braketnotebookcdk-*
              - Effect: "Allow"
                Action:
                  - "logs:CreateLogStream"
                  - "logs:PutLogEvents"
                  - "logs:CreateLogGroup"
                  - "logs:DescribeLogStreams"
                Resource:
                  - !Sub "arn:aws:logs:*:${AWS::AccountId}:log-group:/aws/sagemaker/*"
              - Effect: "Allow"
                Action:
                  - braket:*
                Resource: "*"
```

## Step 3: Create a SageMaker AI

notebook instance with the prefix `amazon-braket-`

Use the SageMaker AI lifecycle script and the IAM role created in step 1 and step 2 to create
a SageMaker AI notebook instance. The notebook instance is customized for Braket and can be
accessed with the Amazon Braket console. For more information about configuration options
for this CloudFormation resource, see [AWS::SageMaker::NotebookInstance](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.md") in the _CloudFormation user
guide_.

```
BraketNotebook:
    Type: AWS::SageMaker::NotebookInstance
    Properties:
      InstanceType: ml.t3.medium
      NotebookInstanceName: !Sub amazon-braket-notebook-${AWS::StackName}
      RoleArn: !GetAtt ExecutionRole.Arn
      VolumeSizeInGB: 30
      LifecycleConfigName: !GetAtt BraketNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleConfigName
```
