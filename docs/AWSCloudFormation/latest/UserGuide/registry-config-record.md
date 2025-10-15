# Record resource types in AWS Config

You can specify that AWS Config automatically track your private resource types and record
 changes to those resources as *configuration items*. This enables you
 to view configuration history for these private resource types, in addition to write
 AWS Config Rules rules to verify configuration best practices. AWS Config is required for the Hook
 extension.

To have AWS Config automatically track your private resource types:


* Manage the resources through CloudFormation. This includes performing all resource
 create, updated, and delete operations through CloudFormation.


###### Note

If you use an IAM role to perform your stack operations, that IAM role
 must have permission to call the following AWS Config actions:



	+ [PutResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_PutResourceConfig.html "https://docs.aws.amazon.com/config/latest/APIReference/API_PutResourceConfig.html")
	+ [DeleteResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteResourceConfig.html "https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteResourceConfig.html")
* Configure AWS Config to record all resource types. For more information, see [Recording Configurations for Third-Party Resources using the AWS CLI](https://docs.aws.amazon.com/config/latest/developerguide/customresources.html "https://docs.aws.amazon.com/config/latest/developerguide/customresources.html")
 in the *AWS Config Developer Guide*.


###### Note

AWS Config doesn't support recording of private resources containing properties
 defined as both required *and* write-only.

By design, resource properties defined as write-only aren't returned in
 the schema used to create AWS Config configuration item. Because of this,
 including a property that's defined as both write-only and required will
 cause the configuration item creation to fail, as a required property will
 not be present. To view the schema that will be used to create the
 configuration item, you can review the `schema` property of the
 [DescribeType](../APIReference/API_DescribeType.md "../APIReference/API_DescribeType.md") action.
For more information about configuration items, see [Configuration
 items](https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#config-items "https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#config-items") in the *AWS Config Developer Guide*.


## Preventing sensitive properties
 being recorded in a configuration item


Your resource type may contain properties that you consider sensitive information,
 such as passwords, secrets, or other sensitive data, that you don't want recorded as
 part of the configuration item. To prevent a property from being recorded in the
 configuration item, you can include that property in the
 `writeOnlyproperties` list in your resource type schema. Resource
 properties listed as `writeOnlyproperties` can be specified by the user,
 but won't be returned by a `read` or `list` request.


For more information, see [writeOnlyProperties](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-writeonlyproperties "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-writeonlyproperties") in the *CloudFormation CLI
 User Guide*.
