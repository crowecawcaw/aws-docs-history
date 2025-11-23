End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Component CloudFormation IaC file parameter details and examples

You can define and reference parameters in your component infrastructure as code (IaC) files. For a detailed description of AWS Proton parameters,
parameter types, the parameter namespace, and how to use parameters in your IaC files, see [AWS Proton parameters](parameters.md "parameters.md"). For more information about
components, see [AWS Proton components](ag-components.md "ag-components.md").

## Define component output parameters

You can define output parameters in your component IaC files. You can then refer to these outputs in service IaC files.

###### Note

You can't define inputs for component IaC files. Attached components can get inputs from the service instance that they are attached to.
Detached components don't have inputs.

## Read parameter values in component IaC files

You can read parameters related to the component and to other resources in component IaC files. You read a parameter value by referencing the
parameter's name in the AWS Proton parameter namespace.

- Input parameters – Read an attached service instance input value by referencing
  `service_instance.inputs.`input-name``.
- Resource parameters – Read AWS Proton resource parameters by referencing names such as
  `component.name`, `service.name`, `service_instance.name`, and `environment.name`.
- Output parameters – Read environment outputs by referencing
  `environment.outputs.`output-name``.

## Example component and service IaC files with parameters

The following example shows a component that provisions an Amazon Simple Storage Service (Amazon S3) bucket and related access policy and exposes the Amazon Resource Names
(ARNs) of both resources as component outputs. A service IaC template adds the component outputs as container environment variables of an Amazon Elastic Container Service
(Amazon ECS) task to make the outputs available to code running in the container, and adds the bucket access policy to the task's role. The bucket name is
based on the names of the environment, service, service instance, and component, meaning that the bucket is coupled with a specific instance of the
component template extending a specific service instance. Developers can create multiple custom components based on this component template, to
provision Amazon S3 buckets for different service instances and functional needs.

The example shows how you use Jinja `{{ ... }}` syntax to refer to component and other resource parameters in your service IaC file.
You can use `{% if ... %}` statements to add blocks of statements only when a component is attached to the service instance. The
`proton_cfn_*` keywords are _filters_ that you can use to sanitize and format output parameter values. For more
information about filters, see [Parameter filters for CloudFormation IaC files](parameter-filters.md "parameter-filters.md").

As an administrator, you author the service IaC template file.

###### Example service CloudFormation IaC file using a component

```
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
 | proton\_cfn\_iam\_policy\_arns }}**

  # Basic permissions for the task
  BaseTaskRoleManagedPolicy:
    Type: AWS::IAM::ManagedPolicy
    Properties:
      # ...
```

As a developer, you author the component IaC template file.

###### Example component CloudFormation IaC file

```
# cloudformation.yaml

# A component that defines an S3 bucket and a policy for accessing the bucket.
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: **'{{environment.name}}-{{service.name}}-{{service\_instance.name}}-{{component.name}}'**
  S3BucketAccessPolicy:
    Type: AWS::IAM::ManagedPolicy
    Properties:
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Action:
              - 's3:Get*'
              - 's3:List*'
              - 's3:PutObject'
            Resource: !GetAtt S3Bucket.Arn
**Outputs:
 BucketName:
 Description: "Bucket to access"
 Value: !GetAtt S3Bucket.Arn
 BucketAccessPolicyArn:
 Value: !Ref S3BucketAccessPolicy**
```

When AWS Proton renders an CloudFormation template for your service instance and replaces all parameters with actual values, the template might look like the
following file.

###### Example service instance CloudFormation rendered IaC file

```
Resources:
  TaskDefinition:
    Type: AWS::ECS::TaskDefinition
    Properties:
      TaskRoleArn: !Ref TaskRole
      ContainerDefinitions:
        - Name: '{{service_instance.name}}'
          # ...
          Environment:
            - Name: **BucketName**
              Value: arn:aws:s3:us-east-1:123456789012:`environment_name`-`service_name`-`service_instance_name`-`component_name`
            - Name: **BucketAccessPolicyArn**
              Value: arn:aws:iam::123456789012:policy/`cfn-generated-policy-name`
  # ...

  TaskRole:
    Type: AWS::IAM::Role
    Properties:
      # ...
      ManagedPolicyArns:
        - !Ref BaseTaskRoleManagedPolicy
        - arn:aws:iam::123456789012:policy/`cfn-generated-policy-name`

  # Basic permissions for the task
  BaseTaskRoleManagedPolicy:
    Type: AWS::IAM::ManagedPolicy
    Properties:
      # ...
```
