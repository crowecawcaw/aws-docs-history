

# Role Manager availability change
<a name="role-manager-availability-change"></a>

**Note**  
Amazon SageMaker Role Manager is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Role Manager, but we do not plan to introduce new features.

## IAM native tools, IAM Identity Center, and infrastructure-as-code
<a name="role-manager-replacement-overview"></a>

The combination of AWS IAM native role creation, AWS IAM Identity Center, and Infrastructure-as-Code (CloudFormation, CDK) serves as a replacement for Amazon SageMaker Role Manager by covering its core capabilities across persona-based role creation and activity-based permission scoping.

AWS IAM native tools handle execution role creation through the IAM console, CLI, or SDK by providing the standard workflow for creating roles with the `sagemaker.amazonaws.com` service principal trust policy and attaching managed or custom policies.

AWS IAM Identity Center handles workforce identity and centralized access management by providing permission sets that define fine-grained access to SageMaker resources, enabling federated identity from external identity providers (Okta, Azure AD, Ping Identity) and trusted identity propagation with SageMaker Studio.

IAM Access Analyzer provides dynamic policy validation and least-privilege policy generation by analyzing actual CloudTrail access patterns and recommending refined policies, replacing Role Manager's static activity-based templates with usage-based policy recommendations.

For repeatable governance, CloudFormation and CDK templates provide version-controlled, auditable, and repeatable IAM role definitions that integrate with enterprise CI/CD pipelines and security review processes.

## Replacing Role Manager
<a name="role-manager-replacing"></a>

If your workflow includes navigating to the SageMaker AI console (Admin configurations > Role manager > Create a role), or using the "Create role using the role creation wizard" option during domain, notebook, training job, or inference model creation, use an alternative path described in the Configuring Replacements section below.

### No cleanup required for existing roles
<a name="role-manager-no-cleanup"></a>

IAM roles previously created by Role Manager are standard IAM roles. They continue to function independently with no Role Manager-specific runtime dependency. These roles:
+ Appear in the IAM console as standard IAM roles with the `sagemaker-` prefix
+ Can be viewed, modified, or deleted directly from the IAM console
+ Have their trust policies and permission policies intact and operational
+ Require no transformation, migration, or deletion as part of this transition

### Replace CDK Role Manager constructs (if used)
<a name="role-manager-replace-cdk"></a>

If you used the `@aws-cdk/aws-sagemaker-alpha` Role Manager CDK constructs (the `Persona` and `Activity` classes), replace them with standard `aws-cdk-lib/aws-iam` constructs. See the Infrastructure-as-Code section below for replacement patterns.

### Replacing the Studio domain creation flow
<a name="role-manager-studio-domain-flow"></a>

When creating a SageMaker AI domain, Role Manager was offered as an option to create execution roles during the onboarding wizard ("Create role using the role creation wizard"). Follow the alternative below:

#### Custom domain setup with IAM console role creation
<a name="role-manager-custom-domain-iam"></a>

During custom domain creation, you can create an execution role directly from the IAM console rather than using Role Manager.

**Step 1: Create the execution role in IAM**

1. Open the IAM console at https://console.aws.amazon.com/iam/.

1. Choose **Roles**, then choose **Create role**.

1. Keep **AWS service** as the Trusted entity type.

1. Under "Use cases for other AWS services," find and select **SageMaker AI**.

1. Choose **SageMaker AI – Execution**, then choose **Next**.

1. The `AmazonSageMakerFullAccess` managed policy is automatically attached. Choose **Next**.

1. Enter a **Role name** (for example, `AmazonSageMaker-ExecutionRole-CustomDomain`) and **Description**.

1. (Optional) Add tags for governance and tracking.

1. Choose **Create role** and note the role ARN.

**Step 2: Use the role during domain creation**

1. In the SageMaker AI console, choose **Admin configurations** > **Domains** > **Create domain**.

1. Choose **Set up for organizations (Custom setup)**.

1. Under **Execution role**, choose **Enter a custom IAM role ARN** and paste the ARN from Step 1.

1. Complete the remaining domain configuration steps.

Refer to [How to use SageMaker AI execution roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) for detailed instructions.

#### Use AWS managed policies directly
<a name="role-manager-managed-policies"></a>

AWS provides managed policies that cover common SageMaker activities. Attach these directly to your IAM execution role:


| Use case | AWS managed policies to attach | 
| --- | --- | 
| General ML development (Data Scientist equivalent) | AmazonSageMakerFullAccess | 
| Read-only access for monitoring/auditing | AmazonSageMakerReadOnly | 
| Canvas users | AmazonSageMakerCanvasFullAccess \+ AmazonSageMakerCanvasAIServicesAccess | 
| Pipeline operations (MLOps equivalent) | AmazonSageMakerFullAccess \+ AmazonSageMakerPipelinesIntegrations | 
| Feature Store access | AmazonSageMakerFeatureStoreAccess | 
| Model governance | AmazonSageMakerModelGovernanceUseAccess | 
| Model registry | AmazonSageMakerModelRegistryFullAccess | 

Refer to [AWS managed policies for Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol.html) for the complete list.

#### Use IAM Access Analyzer policy generation (for least-privilege)
<a name="role-manager-access-analyzer"></a>

Use IAM Access Analyzer to generate least-privilege policies based on actual CloudTrail access activity. This produces more accurate, usage-based policies than Role Manager's static templates:

1. **Enable CloudTrail** logging for your SageMaker workloads (typically already enabled).

1. **Run workloads** with a broader policy (for example, `AmazonSageMakerFullAccess`) for a representative period (30-90 days recommended).

1. **Generate a policy** from IAM Access Analyzer:
   + Open the IAM console > **Access Analyzer** > **Policy generation**.
   + Select the role to analyze.
   + Specify the CloudTrail trail and time period.
   + Review the generated policy, which contains only the actions actually used.

1. **Apply the generated policy** to replace the broader initial policy.

This approach replaces Role Manager's static templates with dynamic policies that reflect actual usage patterns, achieving true least-privilege without manual curation.

Refer to [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) for detailed steps.

#### Infrastructure-as-Code (CloudFormation)
<a name="role-manager-cloudformation"></a>

Define SageMaker execution roles in CloudFormation for repeatable, version-controlled role management. The following is an example that needs to be modified based on your use case:

```
AWSTemplateFormatVersion: '2010-09-09'
Description: SageMaker execution roles replacing Role Manager personas

Resources:
  # Replaces Role Manager "SageMaker AI Compute" persona
  SageMakerComputeRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: sagemaker-compute-execution-role
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: sagemaker.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AmazonSageMakerFullAccess
      Policies:
        - PolicyName: S3DataAccess
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - s3:GetObject
                  - s3:PutObject
                  - s3:DeleteObject
                  - s3:ListBucket
                Resource:
                  - arn:aws:s3:::my-sagemaker-bucket
                  - arn:aws:s3:::my-sagemaker-bucket/*
      Tags:
        - Key: Purpose
          Value: sagemaker-compute
        - Key: ManagedBy
          Value: cloudformation

  # Replaces Role Manager "Data Scientist" persona
  DataScientistRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: sagemaker-data-scientist-role
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: sagemaker.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AmazonSageMakerFullAccess
        - arn:aws:iam::aws:policy/AmazonSageMakerCanvasFullAccess
        - arn:aws:iam::aws:policy/AmazonSageMakerCanvasAIServicesAccess
      Policies:
        - PolicyName: GlueAccess
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - glue:CreateTable
                  - glue:UpdateTable
                  - glue:DeleteTable
                  - glue:GetTable
                  - glue:GetTables
                  - glue:GetDatabase
                  - glue:GetDatabases
                Resource: '*'
      Tags:
        - Key: Purpose
          Value: sagemaker-data-scientist
        - Key: ManagedBy
          Value: cloudformation

  # Replaces Role Manager "MLOps" persona
  MLOpsRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: sagemaker-mlops-role
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: sagemaker.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AmazonSageMakerFullAccess
        - arn:aws:iam::aws:policy/AmazonSageMakerPipelinesIntegrations
        - arn:aws:iam::aws:policy/AmazonS3FullAccess
      Tags:
        - Key: Purpose
          Value: sagemaker-mlops
        - Key: ManagedBy
          Value: cloudformation

Outputs:
  ComputeRoleArn:
    Description: ARN of the SageMaker Compute execution role
    Value: !GetAtt SageMakerComputeRole.Arn
  DataScientistRoleArn:
    Description: ARN of the Data Scientist execution role
    Value: !GetAtt DataScientistRole.Arn
  MLOpsRoleArn:
    Description: ARN of the MLOps execution role
    Value: !GetAtt MLOpsRole.Arn
```

#### Infrastructure-as-Code (AWS CDK)
<a name="role-manager-cdk"></a>

Replace the Role Manager CDK constructs (`Persona`, `Activity`) with standard IAM constructs. The following is an example that needs to be modified based on your use case:

```
import * as cdk from 'aws-cdk-lib';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class SageMakerRolesStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Replaces Role Manager "SageMaker AI Compute" persona
    const computeRole = new iam.Role(this, 'SageMakerComputeRole', {
      roleName: 'sagemaker-compute-execution-role',
      assumedBy: new iam.ServicePrincipal('sagemaker.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonSageMakerFullAccess'),
      ],
    });

    // Replaces Role Manager "Data Scientist" persona
    const dataScientistRole = new iam.Role(this, 'DataScientistRole', {
      roleName: 'sagemaker-data-scientist-role',
      assumedBy: new iam.ServicePrincipal('sagemaker.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonSageMakerFullAccess'),
        iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonSageMakerCanvasFullAccess'),
        iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonSageMakerCanvasAIServicesAccess'),
      ],
    });

    // Add custom inline policy for Glue access
    // (replaces "Manage Glue Tables" ML activity)
    dataScientistRole.addToPolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        'glue:CreateTable',
        'glue:UpdateTable',
        'glue:DeleteTable',
        'glue:GetTable',
        'glue:GetTables',
        'glue:GetDatabase',
        'glue:GetDatabases',
      ],
      resources: ['*'],
    }));

    // Replaces Role Manager "MLOps" persona
    const mlopsRole = new iam.Role(this, 'MLOpsRole', {
      roleName: 'sagemaker-mlops-role',
      assumedBy: new iam.ServicePrincipal('sagemaker.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonSageMakerFullAccess'),
        iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonSageMakerPipelinesIntegrations'),
        iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonS3FullAccess'),
      ],
    });

    // Example: Scope down with VPC conditions
    // (replaces Role Manager VPC customization)
    computeRole.addToPolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        'ec2:CreateNetworkInterface',
        'ec2:CreateNetworkInterfacePermission',
        'ec2:DeleteNetworkInterface',
        'ec2:DeleteNetworkInterfacePermission',
        'ec2:DescribeNetworkInterfaces',
        'ec2:DescribeVpcs',
        'ec2:DescribeDhcpOptions',
        'ec2:DescribeSubnets',
        'ec2:DescribeSecurityGroups',
      ],
      resources: ['*'],
      conditions: {
        StringEquals: {
          'ec2:Vpc': 'arn:aws:ec2:us-east-1:123456789012:vpc/vpc-xxxxxxxx',
        },
      },
    }));
  }
}
```