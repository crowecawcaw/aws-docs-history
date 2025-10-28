# Getting started with schema registry

The following sections provide an overview and walk you through setting up and using Schema Registry.
For information about schema registry concepts and components, see [AWS Glue Schema registry](schema-registry.md "schema-registry.md").

###### Topics

- [Installing SerDe Libraries](schema-registry-gs-serde.md "schema-registry-gs-serde.md")
- [Creating a registry](schema-registry-gs3.md "schema-registry-gs3.md")
- [Creating a schema](schema-registry-gs4.md "schema-registry-gs4.md")
- [Updating a schema or registry](schema-registry-gs5.md "schema-registry-gs5.md")
- [Deleting a schema or registry](schema-registry-gs7.md "schema-registry-gs7.md")
- [IAM examples for serializers](#schema-registry-gs1 "#schema-registry-gs1")
- [IAM examples for deserializers](#schema-registry-gs1b "#schema-registry-gs1b")
- [Private connectivity using AWS PrivateLink](#schema-registry-gs-private "#schema-registry-gs-private")
- [Accessing Amazon CloudWatch metrics](schema-registry-gs-monitoring.md "schema-registry-gs-monitoring.md")
- [Sample AWS CloudFormation template for schema registry](schema-registry-integrations-cfn.md "schema-registry-integrations-cfn.md")

## IAM examples for serializers

###### Note

AWS managed policies grant necessary permissions for common use cases. For information on using managed policies to manage the schema registry, see [AWS managed (predefined) policies for
AWS Glue](security-iam-awsmanpol.md#access-policy-examples-aws-managed "security-iam-awsmanpol.md#access-policy-examples-aws-managed").

For serializers, you should create a minimal policy similar to that below to give you the ability to find the `schemaVersionId` for a given schema definition. Note, you should have read permissions on the registry in order to read the schemas in the registry. You can limit the registries that can be read by using the `Resource` clause.

Code example 13:

```
{
    "Sid" : "GetSchemaByDefinition",
    "Effect" : "Allow",
    "Action" :
	[
        "glue:GetSchemaByDefinition"
    ],
        "Resource" : ["arn:aws:glue:us-east-2:012345678:registry/registryname-1",
                      "arn:aws:glue:us-east-2:012345678:schema/registryname-1/schemaname-1",
                      "arn:aws:glue:us-east-2:012345678:schema/registryname-1/schemaname-2"
                     ]
}
```

Further, you can also allow producers to create new schemas and versions by including the following extra methods. Note, you should be able to inspect the registry in order to add/remove/evolve the schemas inside it. You can limit the registries that can be inspected by using the `Resource` clause.

Code example 14:

```
{
    "Sid" : "RegisterSchemaWithMetadata",
    "Effect" : "Allow",
    "Action" :
	[
        "glue:GetSchemaByDefinition",
        "glue:CreateSchema",
        "glue:RegisterSchemaVersion",
        "glue:PutSchemaVersionMetadata",
    ],
    "Resource" : ["arn:aws:glue:`aws-region`:123456789012:registry/registryname-1",
                  "arn:aws:glue:`aws-region`:123456789012:schema/registryname-1/schemaname-1",
                  "arn:aws:glue:`aws-region`:123456789012:schema/registryname-1/schemaname-2"
                 ]
}
```

## IAM examples for deserializers

For deserializers (consumer side), you should create a policy similar to that below to allow the deserializer to fetch the schema from the Schema Registry for deserialization. Note, you should be able to inspect the registry in order to fetch the schemas inside it.

Code example 15:

```
{
    "Sid" : "GetSchemaVersion",
    "Effect" : "Allow",
    "Action" :
	[
        "glue:GetSchemaVersion"
    ],
    "Resource" : ["*"]
}
```

## Private connectivity using AWS PrivateLink

You can use AWS PrivateLink to connect your data producer’s VPC to AWS Glue by defining an
interface VPC endpoint for AWS Glue. When you use a VPC interface endpoint,
communication between your VPC and AWS Glue is conducted entirely within the AWS
network. For more information, see [Using
AWS Glue with VPC Endpoints](vpc-endpoint.md "vpc-endpoint.md").
