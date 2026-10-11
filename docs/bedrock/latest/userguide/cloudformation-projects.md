

# Managing Projects with AWS CloudFormation
<a name="cloudformation-projects"></a>

Amazon Bedrock is integrated with AWS CloudFormation, allowing you to define and manage Projects as part of your infrastructure templates. You can provision projects consistently and repeatedly across multiple AWS accounts and Regions using JSON or YAML templates.

## AWS::BedrockMantle::Project
<a name="cloudformation-projects-resource"></a>

Use the `AWS::BedrockMantle::Project` resource to create and manage a Bedrock Project in a CloudFormation template. Projects created through CloudFormation support the same capabilities as those created through the API, including IAM policy attachment, tagging, and observability.

### Syntax
<a name="cloudformation-projects-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

**Example CloudFormation Syntax**  

```
{
  "Type": "AWS::BedrockMantle::Project",
  "Properties": {
    "Name": String,
    "Tags": [
      { "Key": String, "Value": String }
    ]
  }
}
```

```
Type: AWS::BedrockMantle::Project
Properties:
  Name: String
  Tags:
    - Key: String
      Value: String
```

### Properties
<a name="cloudformation-projects-properties"></a>

Name  
Required. The name of the project. Must be unique within your AWS account.  
Type: String  
Minimum: 1  
Maximum: 128  
Update requires: No interruption

Tags  
A list of unique key-value pairs to associate with the project for cost allocation and access control.  
Type: Array of Tag  
Minimum: 0  
Maximum: 200  
Update requires: No interruption

**Note on Tag Updates**  
CloudFormation tag updates on `AWS::BedrockMantle::Project` use separate add and remove operations internally. There is no atomic full tag replacement. If a stack update fails mid-operation, the project's tag set may be in a partially updated state. Always verify the final tag state after a stack update that modifies tags.

### Return Values
<a name="cloudformation-projects-return-values"></a>

#### Ref
<a name="cloudformation-projects-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the project ARN (for example, `arn:aws:bedrock-mantle:us-east-1:123456789012:project/proj_abc123`). To retrieve the project ID, use `Fn::GetAtt` with the `Id` attribute.

#### Fn::GetAtt
<a name="cloudformation-projects-getatt"></a>

Arn  
The Amazon Resource Name (ARN) of the project (for example, `arn:aws:bedrock-mantle:us-east-1:123456789012:project/proj_abc123`).

CreatedAt  
The timestamp at which the project was created.

Id  
The unique identifier of the project (for example, `proj_abc123`).

## Examples
<a name="cloudformation-projects-examples"></a>

### Create a Basic Project
<a name="cloudformation-projects-basic"></a>

The following example creates a project for a production chatbot application:

**Example Basic Project**  

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Amazon Bedrock Project for Production Chatbot

Resources:
  CustomerChatbotProject:
    Type: AWS::BedrockMantle::Project
    Properties:
      Name: CustomerChatbot-Production
      Tags:
        - Key: Project
          Value: CustomerChatbot
        - Key: Environment
          Value: Production
        - Key: Owner
          Value: TeamAlpha
        - Key: CostCenter
          Value: "21524"

Outputs:
  ProjectId:
    Description: The ID of the created project
    Value: !GetAtt CustomerChatbotProject.Id

  ProjectArn:
    Description: The ARN of the created project
    Value: !Ref CustomerChatbotProject
```

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "CustomerChatbotProject": {
      "Type": "AWS::BedrockMantle::Project",
      "Properties": {
        "Name": "CustomerChatbot-Production",
        "Tags": [
          { "Key": "Project", "Value": "CustomerChatbot" },
          { "Key": "Environment", "Value": "Production" },
          { "Key": "Owner", "Value": "TeamAlpha" },
          { "Key": "CostCenter", "Value": "21524" }
        ]
      }
    }
  },
  "Outputs": {
    "ProjectId": {
      "Description": "The ID of the created project",
      "Value": { "Fn::GetAtt": ["CustomerChatbotProject", "Id"] }
    },
    "ProjectArn": {
      "Description": "The ARN of the created project",
      "Value": { "Ref": "CustomerChatbotProject" }
    }
  }
}
```

### Create Multiple Projects for Different Environments
<a name="cloudformation-projects-multi-env"></a>

The following example provisions separate projects for development, staging, and production environments in a single stack:

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Amazon Bedrock Projects for Multi-Environment Deployment

Parameters:
  ApplicationName:
    Type: String
    Default: InternalSearch
    Description: Name of the application

  CostCenter:
    Type: String
    Description: Cost center for billing allocation

Resources:
  DevelopmentProject:
    Type: AWS::BedrockMantle::Project
    Properties:
      Name: !Sub "${ApplicationName}-Development"
      Tags:
        - Key: Project
          Value: !Ref ApplicationName
        - Key: Environment
          Value: Development
        - Key: CostCenter
          Value: !Ref CostCenter

  StagingProject:
    Type: AWS::BedrockMantle::Project
    Properties:
      Name: !Sub "${ApplicationName}-Staging"
      Tags:
        - Key: Project
          Value: !Ref ApplicationName
        - Key: Environment
          Value: Staging
        - Key: CostCenter
          Value: !Ref CostCenter

  ProductionProject:
    Type: AWS::BedrockMantle::Project
    Properties:
      Name: !Sub "${ApplicationName}-Production"
      Tags:
        - Key: Project
          Value: !Ref ApplicationName
        - Key: Environment
          Value: Production
        - Key: CostCenter
          Value: !Ref CostCenter

Outputs:
  DevelopmentProjectArn:
    Value: !GetAtt DevelopmentProject.Arn
    Export:
      Name: !Sub "${ApplicationName}-Dev-ProjectArn"

  StagingProjectArn:
    Value: !GetAtt StagingProject.Arn
    Export:
      Name: !Sub "${ApplicationName}-Staging-ProjectArn"

  ProductionProjectArn:
    Value: !GetAtt ProductionProject.Arn
    Export:
      Name: !Sub "${ApplicationName}-Prod-ProjectArn"
```

### Create a Project with IAM Role Access
<a name="cloudformation-projects-iam"></a>

The following example creates a project and attaches an IAM policy granting a specific role access to invoke models:

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Amazon Bedrock Project with IAM Access Control

Resources:
  ProductionProject:
    Type: AWS::BedrockMantle::Project
    Properties:
      Name: CustomerChatbot-Production
      Tags:
        - Key: Environment
          Value: Production
        - Key: CostCenter
          Value: "21524"

  ProductionAppRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: BedrockProjectProductionRole
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: BedrockProjectInvokeAccess
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - bedrock-mantle:CreateInference
                  - bedrock-mantle:GetProject
                Resource: !GetAtt ProductionProject.Arn

Outputs:
  ProjectArn:
    Value: !GetAtt ProductionProject.Arn

  RoleArn:
    Value: !GetAtt ProductionAppRole.Arn
```

## Using CloudFormation Outputs with the Projects API
<a name="cloudformation-projects-using-outputs"></a>

After deploying your CloudFormation stack, you can reference the project ARN and ID in your application code using the stack outputs:

```
import boto3
from openai import OpenAI

# Retrieve project details from CloudFormation stack outputs
cfn = boto3.client('cloudformation', region_name='us-east-1')

response = cfn.describe_stacks(StackName='my-bedrock-projects-stack')
outputs = {o['OutputKey']: o['OutputValue'] for o in response['Stacks'][0]['Outputs']}

production_project_arn = outputs['ProductionProjectArn']

# Extract project ID from ARN
# ARN format: arn:aws:bedrock-mantle:us-east-1:123456789012:project/proj_abc123
project_id = production_project_arn.split('/')[-1]

print(f"Using project: {project_id}")

# Use the project for inference
client = OpenAI(project=project_id)

response = client.responses.create(
    model="openai.gpt-oss-120b",
    input="Hello from a CloudFormation-managed project!"
)

print(response)
```

## Learn More
<a name="cloudformation-projects-learn-more"></a>

For more information about using CloudFormation with Amazon Bedrock resources, see:
+ [Create Amazon Bedrock resources with AWS CloudFormation](creating-resources-with-cloudformation.md)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [Amazon Bedrock resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_Bedrock.html)