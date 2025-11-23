End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Customer-managed environments

With customer-managed environments, you can use existing infrastructure, like a VPC, that
you already have deployed as your AWS Proton environment. While using customer-managed
environments, you can provision your own shared resources outside of AWS Proton. However, you can
still allow AWS Proton to consume relevant provisioning outputs as inputs for AWS Proton services when
they are deployed. If the outputs can change, AWS Proton is able to accept updates. AWS Proton is unable
to change the environment directly, though, since the provisioning is managed outside of
AWS Proton.

After the environment is created, you're responsible for providing the same outputs to
AWS Proton that would have been created if AWS Proton had made the environment, such as Amazon ECS cluster
names or Amazon VPC IDs.

With this functionality, you can deploy and update AWS Proton service resources from an AWS Proton
service template to this environment. However, the environment itself isn't modified through
template updates in AWS Proton. You're responsible for executing updates to the environment and
updating those outputs in AWS Proton.

You can have multiple environments in a single account that are a mix of AWS Proton managed and
customer-managed environments. You can also link a second account and use an AWS Proton template in
the primary account to execute deployments and updates to environments and services in that
second, linked account.

## How to use customer-managed

environments

The first thing administrators need to do is register an imported, customer-managed
environment template. Don't supply manifests or infrastructure files in the template bundle.
Only supply the schema.

The schema below outlines a list of outputs using the open API format and replicates the
outputs from an CloudFormation template.

###### Important

Only string inputs are allowed for the outputs.

The following example is a snippet of the output sections of an CloudFormation template for a
corresponding Fargate template.

```
Outputs:
  ClusterName:
    Description: The name of the ECS cluster
    Value: !Ref 'ECSCluster'
  ECSTaskExecutionRole:
    Description: The ARN of the ECS role
    Value: !GetAtt 'ECSTaskExecutionRole.Arn'
  VpcId:
    Description: The ID of the VPC that this stack is deployed in
    Value: !Ref 'VPC'
[...]
```

The schema for the corresponding AWS Proton imported environment is similar to the following.
Don't supply default values in the schema.

```
schema:
  format:
    openapi: "3.0.0"
  environment_input_type: "EnvironmentOutput"
  types:
    EnvironmentOutput:
      type: object
      description: "Outputs of the environment"
      properties:
        ClusterName:
          type: string
          description: "The name of the ECS cluster"
        ECSTaskExecutionRole:
          type: string
          description: "The ARN of the ECS role"
        VpcId:
          type: string
          description: "The ID of the VPC that this stack is deployed in"
[...]
```

At the time of registering the template, you indicate that this template is imported and
provides the Amazon S3 bucket location for the bundle. AWS Proton validates that the schema only
contains `environment_input_type` and no CloudFormation template parameters before putting
the template in draft.

You provide the following to create an imported environment.

- An IAM role to use when making deployments.
- A specification with the values for the required outputs.

You can provide both of these through either the console or the AWS CLI using a process
similar to the deployment of a regular environment.
