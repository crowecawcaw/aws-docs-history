End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Component AWS CloudFormation example

Here is a complete example of an AWS Proton directly defined component and how you can use it in an AWS Proton service. The component provisions an Amazon Simple Storage Service
(Amazon S3) bucket and related access policy. The service instance can refer to this bucket and use it. The bucket name is based on the names of the
environment, service, service instance, and component, meaning that the bucket is coupled with a specific instance of the component template extending a
specific service instance. Developers can create multiple components based on this component template, to provision Amazon S3 buckets for different service
instances and functional needs.

The example covers authoring the various required AWS CloudFormation infrastructure as code (IaC) files and creating a required AWS Identity and Access Management (IAM) role. The example
groups steps by the owning people roles.

## Administrator steps

###### To enable developers to use components with a service

1. Create an AWS Identity and Access Management (IAM) role that scopes down the resources that directly defined components running in your environment can provision.
   AWS Proton assumes this role later to provision directly defined components in the environment.

For this example, use the following policy:

###### Example directly defined component role

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:CancelUpdateStack",
 "cloudformation:CreateChangeSet",
 "cloudformation:DeleteChangeSet",
 "cloudformation:DescribeStacks",
 "cloudformation:ContinueUpdateRollback",
 "cloudformation:DetectStackResourceDrift",
 "cloudformation:DescribeStackResourceDrifts",
 "cloudformation:DescribeStackEvents",
 "cloudformation:CreateStack",
 "cloudformation:DeleteStack",
 "cloudformation:UpdateStack",
 "cloudformation:DescribeChangeSet",
 "cloudformation:ExecuteChangeSet",
 "cloudformation:ListChangeSets",
 "cloudformation:ListStackResources"
 ],
 "Resource": "arn:aws:cloudformation:*:`123456789012`:stack/AWSProton-*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:DeleteBucket",
 "s3:GetBucket*",
 "iam:CreatePolicy",
 "iam:DeletePolicy",
 "iam:GetPolicy",
 "iam:ListPolicyVersions",
 "iam:DeletePolicyVersion"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "cloudformation.amazonaws.com"
 }
 }
 }
 ]
}`

```

2. Provide the role you created in the previous step when you create or update the environment. In the AWS Proton console, specify a **Component
   role** on the **Configure environment** page. If you're using the AWS Proton API or AWS CLI, specify the
   `componentRoleArn` of the [CreateEnvironment](../APIReference/API_CreateEnvironment.md "../APIReference/API_CreateEnvironment.md") or [UpdateEnvironment](../APIReference/API_UpdateEnvironment.md "../APIReference/API_UpdateEnvironment.md")
   API actions.
3. Create a service template that refers to a directly defined component attached to the service instance.

The example shows how to write a robust service template that doesn't break if a component isn't attached to the service instance.

###### Example service CloudFormation IaC file using a component

````
# service/instance_infrastructure/cloudformation.yaml

Resources:
  TaskDefinition:
    Type: AWS::ECS::TaskDefinition
    Properties:
      TaskRoleArn: !Ref TaskRole
      ContainerDefinitions:
        - Name: '{{service_instance.name}}'
          # ...
          **{% if service\_instance.components.default.outputs | length > 0 %}
 Environment:
 {{ service\_instance.components.default.outputs |
 proton\_cfn\_ecs\_task\_definition\_formatted\_env\_vars }}
 {% endif %}**

  # ...

  TaskRole:
    Type: AWS::IAM::Role
    Properties:
      # ...
      ManagedPolicyArns:
        - !Ref BaseTaskRoleManagedPolicy
        **{{ service\_instance.components.default.outputs
| proton\_cfn\_iam\_policy\_arns }}** # Basic permissions for the task BaseTaskRoleManagedPolicy: Type: AWS::IAM::ManagedPolicy Properties: # ... ``` 4. Create a new service template minor version that declares directly defined components as supported. <br>• Template bundle in Amazon S3 – In the AWS Proton console, when you create a service template version, for **Supported component sources**, choose **Directly defined**. If you're using the AWS Proton API or AWS CLI, specify `DIRECTLY_DEFINED` in the `supportedComponentSources` parameter of the [CreateServiceTemplateVersion](../APIReference/API_CreateServiceTemplateVersion.md "../APIReference/API_CreateServiceTemplateVersion.md") or [UpdateServiceTemplateVersion](../APIReference/API_UpdateServiceTemplateVersion.md "../APIReference/API_UpdateServiceTemplateVersion.md") API actions. <br>• Template sync – Commit a change to your service template bundle repository, where you specify `DIRECTLY_DEFINED` as an item of `supported_component_sources:` in the `.template-registration.yaml` file in the major version directory. For more information about this file, see [Syncing service templates](create-template-sync.md#create-template-sync-service-templates "create-template-sync.md#create-template-sync-service-templates"). 5. Publish the new service template minor version. For more information, see [Register and publish templates](template-create.md "template-create.md"). 6. Be sure to allow the `proton:CreateComponent` in the IAM role of developers that use this service template. ## Developer steps ###### To use a directly defined component with a service instance 1. Create a service that uses the service template version that the administrator created with component support. Alternatively, update one of your existing service instances to use the latest template version. 2. Write a component IaC template file that provisions an Amazon S3 bucket and a related access policy and exposes these resources as outputs. ###### Example component CloudFormation IaC file ``` # cloudformation.yaml # A component that defines an S3 bucket and a policy for accessing the bucket. Resources: S3Bucket: Type: AWS::S3::Bucket Properties: BucketName: **'{{environment.name}}-{{service.name}}-{{service\_instance.name}}-{{component.name}}'** S3BucketAccessPolicy: Type: AWS::IAM::ManagedPolicy Properties: PolicyDocument: Version: "2012-10-17" Statement: <br>• Effect: Allow Action: <br>• 's3:Get*' <br>• 's3:List*' <br>• 's3:PutObject' Resource: !GetAtt S3Bucket.Arn **Outputs: BucketName: Description: "Bucket to access" Value: !GetAtt S3Bucket.Arn BucketAccessPolicyArn: Value: !Ref S3BucketAccessPolicy** ``` 3. If you're using the AWS Proton API or AWS CLI, write a manifest file for the component. ###### Example directly defined component manifest ``` infrastructure: templates: <br>• file: "cloudformation.yaml" rendering_engine: jinja template_language: cloudformation ``` 4. Create a directly defined component. AWS Proton assumes the component role that the administrator defined to provision the component. In the AWS Proton console, on the [Components](https://console.aws.amazon.com/proton/#/components "https://console.aws.amazon.com/proton/#/components") page, choose **Create component**. For **Component settings**, enter a **Component name** and an optional **Component description**. For **Component attachment**, choose **Attach the component to a service instance.** Select your environment, service, and service instance. For **Component source**, choose **AWS CloudFormation**, and then choose the component IaC file. ###### Note You don't need to provide a manifest—the console creates one for you. If you're using the AWS Proton API or AWS CLI, use the [CreateComponent](../APIReference/API_CreateComponent.md "../APIReference/API_CreateComponent.md") API action. Set a component `name` and optional `description`. Set `environmentName`, `serviceName`, and `serviceInstanceName`. Set `templateSource` and `manifest` to the paths of the files you created. ###### Note Specifying an environment name is optional when you specify service and service instance names. The combination of these two is unique in your AWS account, and AWS Proton can determine the environment from the service instance. 5. Update your service instance to redeploy it. AWS Proton uses outputs from your component in the rendered service instance template, to enable your application to use the Amazon S3 bucket that the component provisioned.
````
