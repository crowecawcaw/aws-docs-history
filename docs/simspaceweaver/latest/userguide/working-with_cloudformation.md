End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Managing your resources with AWS CloudFormation

You can use AWS CloudFormation to manage your AWS SimSpace Weaver resources. CloudFormation is a separate AWS service
that helps you specify, provision, and manage your AWS infrastructure as code. With CloudFormation you
create a JSON or YAML file, called a _[template](../../../AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.md#cfn-concepts-templates template "../../../AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.md#cfn-concepts-templates template")_. Your template specifies the details of your infrastructure. CloudFormation
uses your template to provision your infrastructure as a single unit, called a _[stack](../../../AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.md#w2ab1b5c15b9 "../../../AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.md#w2ab1b5c15b9")_. When you delete your stack, you can have CloudFormation delete everything in
the stack at the same time. You can manage your template using standard source code management
processes (for example, tracking it in a version control system like
[Git](https://git-scm.com/ "https://git-scm.com/")). For more information about CloudFormation, see the
[_AWS CloudFormation User Guide_](../../../AWSCloudFormation/latest/UserGuide.md "../../../AWSCloudFormation/latest/UserGuide.md").

###### Your simulation resource

In AWS, a _resource_
is an entity that you can work with. Examples include an Amazon EC2 instance, an Amazon S3 bucket, or an
IAM role. Your SimSpace Weaver simulation is a resource.
In configurations, you usually specify an AWS resource in the form
`AWS::`service`::resource`. For SimSpace Weaver, you specify your simulation
resource as `AWS::SimSpaceWeaver::Simulation`. For more
information about your simulation resource in CloudFormation, see the [SimSpace Weaver](../../../AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.md")
section in the _AWS CloudFormation User Guide_.

###### How can I use CloudFormation with SimSpace Weaver?

You can create an CloudFormation template
that specifies the AWS resources that you want to provision. Your template can specify an
entire architecture, part of an architecture, or a small solution. For example, you
could specify an architecture for your SimSpace Weaver solution that includes Amazon S3 buckets,
IAM permissions, a supporting database in Amazon Relational Database Service or Amazon DynamoDB, and
your `Simulation` resource. You can then use CloudFormation to provision all of
those resources as a unit, and at the same time.

###### Example template that creates IAM resources and starts a simulation

The following example template creates an IAM role and permissions that SimSpace Weaver
needs to perform actions in your account. The SimSpace Weaver app SDK scripts create
the role and permissions in a specific AWS Region when you create a project, but
you can use an CloudFormation template to deploy the simulation to another AWS Region
without running the scripts again. For example, you
can do this to set up a backup simulation for disaster recovery purposes.

In this example, the original simulation name is `MySimulation`.
A bucket for the schema already exists in the AWS Region where CloudFormation will build
the stack. The bucket contains a version of the schema that is properly configured
to run the simulation in that AWS Region. Recall that the schema specifies the
location of your app zip files, which is an Amazon S3 bucket in the same AWS Region
as the simulation. The app zips bucket and files must already exist in the
AWS Region when CloudFormation builds the stack, otherwise your simulation won't start.
Note that the bucket name in this example includes the AWS Region, but that
doesn't determine where the bucket is actually located. You must make sure that
the bucket is actually in that AWS Region (you can check the bucket properties
in the Amazon S3 console, with the Amazon S3 APIs, or with the Amazon S3 commands in the AWS CLI).

This example uses some built-in functions and parameters in CloudFormation to perform
variable substitution. For more information, see [Intrinsic function reference](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md") and [Pseudo parameters reference](../../../AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.md "../../../AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.md") in the _AWS CloudFormation User Guide_.

```

AWSTemplateFormatVersion: 2010-09-09
Resources:
  WeaverAppRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: SimSpaceWeaverAppRole
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
        - Effect: Allow
          Principal:
            Service:
              - simspaceweaver.amazonaws.com
          Action:
            - sts:AssumeRole
      Path: /
      Policies:
        - PolicyName: SimSpaceWeaverAppRolePolicy
          PolicyDocument:
            Version: 2012-10-17
            Statement:
            - Effect: Allow
              Action:
                - logs:PutLogEvents
                - logs:DescribeLogGroups
                - logs:DescribeLogStreams
                - logs:CreateLogGroup
                - logs:CreateLogStream
              Resource: *
            - Effect: Allow
              Action:
                - cloudwatch:PutMetricData
              Resource: *
            - Effect: Allow
              Action:
                - s3:ListBucket
                - s3:PutObject
                - s3:GetObject
              Resource: *
  MyBackupSimulation:
    Type: AWS::SimSpaceWeaver::Simulation
    Properties:
      Name: !Sub 'mySimulation-${AWS::Region}'
      RoleArn: !GetAtt WeaverAppRole.Arn
      SchemaS3Location:
        BucketName: !Sub 'weaver-mySimulation-${AWS::AccountId}-schemas-${AWS::Region}'
        ObjectKey: !Sub 'schema/mySimulation-${AWS::Region}-schema.yaml'

```
