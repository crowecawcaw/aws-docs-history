

# Using Cloud Control API resource types
<a name="resource-types"></a>

To use a resource type with AWS Cloud Control API, that resource type must be present and activated in your AWS account. Supported AWS resource types are public and always activated. You can choose to activate public resource types offered by third-party publishers as well through the AWS CloudFormation extension registry.

The *extension registry* is a feature of AWS CloudFormation that contains detailed information about the resource types available for use in your account. These can include resource types published by third-parties, in addition to those published by AWS. Using the registry, you can manage the resource types in your account, including:
+ View the available and activated resource types.
+ Register private resource types for use in your account.
+ Activate public third-party resource types.
+ Manage the resource type *versions*, including setting the default version of a resource type in your account.
+ Set account-level configuration properties of a resource type, if it has any.

You can also use the CloudFormation registry to view a resource type's schema, which contains important information about how to use the resource with Cloud Control API, such as property definitions and permission requirements. For more information, see [Viewing resource type schemas](#resource-types-schemas).

The registry is available through the CloudFormation console, in addition to the CloudFormation API.

**Note**  
Not all resource types listed in the CloudFormation registry currently support Cloud Control API. For more information, see [Determining if a resource type supports Cloud Control API](#resource-types-determine-support).

For more information about resource type management options, see [Using the CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) in the *AWS CloudFormation User Guide*.

## Managing resource types using the CloudFormation API
<a name="resource-types-manage-APIs"></a>

In addition to accessing the extension registry through the CloudFormation console, you can use operations included in the CloudFormation API to identify and manage the resource types in your account. The table below lists the API operations that you can use to discover, activate, and configure the resource types available in your account.


| CloudFormation API operation | AWS CLI command | Description | 
| --- | --- | --- | 
| [`DescribeType`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html) | [`describe-type`](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html) | Returns detailed information about a resource type. | 
| [`ListTypes`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListTypes.html) | [`list-types`](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-types.html) | Returns summary information about a resource type. | 
| [`ActivateType`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html) | [`activate-type`](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/activate-type.html) | Activates a public third-party resource type, making it available for use in your account. | 
| [`DeactivateType`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeactivateType.html) | [`deactivate-type`](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deactivate-type.html) | Deactivates a public third-party resource type in your account. | 
| [`ListTypeVersions`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListTypeVersions.html) | [`list-type-versions`](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-type-versions.html) | Returns summary information about the versions of a resource type. | 
| [`SetTypeDefaultVersion`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeDefaultVersion.html) | [`set-type-default-version`](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-default-version.html) | Specifies the default version of a resource type. | 
| [`BatchDescribeTypeConfigurations`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_BatchDescribeTypeConfigurations.html) | [`batch-describe-type-configurations`](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/batch-describe-type-configurations.html) | Returns configuration data for the specified resource types. | 
| [`SetTypeConfiguration`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html) | [`set-type-configuration`](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html) | Specifies the configuration data for a resource type in your account. | 
| [`RegisterType`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html) | [`register-type`](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/register-type.html) | Registers a private third-party resource, making it available for use in your account. | 
| [`DeregisterType`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeregisterType.html) | [`deregister-type`](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deregister-type.html) | Deregisters a private third-party resource, removing it from active use in your account. | 

## Determining if a resource type supports Cloud Control API
<a name="resource-types-determine-support"></a>

By default, resource types published in the CloudFormation registry automatically support Cloud Control API resource operations. This includes private resource types, in addition to public third-party resource types. However, the AWS CloudFormation registry also contains legacy resource types, classified as *non-provisionable*. These resource types don't currently support Cloud Control API, and you can't use them in resource operations.

For a list of the AWS public resource types that currently support Cloud Control API resource operations, see [Resource types that support Cloud Control API](supported-resources.md).

You can also use the AWS Command Line Interface (AWS CLI) to generate a list of supported resource types or to determine if a specific resource type supports Cloud Control API.

**Generating a list of supported resources using the AWS CLI**
+ Use the `list-types` command, with the following parameters:
  + `type` – Specify `RESOURCE` to select only resource types.
  + `visibility` – Specify `PUBLIC` to select public resources or `PRIVATE` for private resources.
  + `provisioning-type` – Specify `FULLY_MUTABLE` or `IMMUTABLE` to select only those resource types that are provisionable.

  For example, the following command selects the first 100 public resource types that are fully mutable from the CloudFormation registry.

  ```
  $ aws cloudformation list-types \
      --type RESOURCE --visibility PUBLIC \
      --provisioning-type FULLY_MUTABLE --max-results 100
  ```

**Determining if a specific resource type supports Cloud Control API using the AWS CLI**
+ Use the `describe-type` command to return details of the resource type.

  Resource types with a `ProvisioningType` of either `FULLY_MUTABLE` or `IMMUTABLE` support Cloud Control API resource operations.

  The following example returns details of the `AWS::Logs::LogGroup` resource type.

  ```
  $ aws cloudformation describe-type \
      --type RESOURCE --type-name AWS::Logs::LogGroup
  ```

## Viewing resource type schemas
<a name="resource-types-schemas"></a>

During resource create and update operations, you specify which resource properties to set and their values. The properties of a resource are defined in its *resource type schema*. This includes data type, whether the property is required, valid values, and other property constraints.

You can view a resource type's schema using the CloudFormation console or the AWS CLI. In addition, the *AWS CloudFormation User Guide* contains reference topics for each available resource type that AWS publishes. For detailed information about resource type properties, in addition to usage examples, see the corresponding topics in the [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) section.

**Note**  
Not all resource types listed in the *AWS CloudFormation User Guide* are available for use with Cloud Control API. To determine if a resource type is available, see [Resource types that support Cloud Control API](supported-resources.md).

For detailed information about the resource type definition schema, which defines how resource type schema can be authored, see [Resource type definition schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html) in the *CloudFormation CLI User Guide for Extension Development*.

For information about how to view an existing resource's current state, which includes its current property values, see [Reading a resource with AWS Cloud Control API](resource-operations-read.md).<a name="resource-operations-create-view-schema-console"></a>

## Viewing a resource type schema using the CloudFormation console
<a name="resource-operations-create-view-schema-console"></a>

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. In the **CloudFormation** navigation pane, under **Registry**, select **Activated extensions**.

1. On the **Resource types** tab, select the resource type that you want to view the resource schema of.

   CloudFormation displays the resource type details page. The resource schema is displayed on the **Schema** tab.<a name="resource-operations-create-view-schema-cli"></a>

## Viewing a resource type schema using the AWS CLI
<a name="resource-operations-create-view-schema-cli"></a>
+ Run `[describe-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html)`.

  In the returned output, the `Schema` structure contains the resource type schema.

  For example, the following command returns information about the `AWS::Logs::LogGroup` resource type.

  ```
  $ aws cloudformation describe-type \
      --type RESOURCE --type-name AWS::Logs::LogGroup
  ```

### Viewing resource property attributes
<a name="resource-types-schemas-properties"></a>

Resource type properties are defined in the `properties` section of the resource type schema. This includes the property data type, whether the property is required, and any constraints such as allowable values or required patterns.

In addition, certain attributes set at the resource level govern when or if a property can be specified. This includes: 
+ Properties defined as `required` must be specified in the desired state during resource creation.
+ Properties defined as `createOnlyProperties` can be set by users, but only during resource creation.
+ Properties defined as `readOnlyProperties` can't be set by users.
+ Properties defined as `writeOnlyProperties` can be specified by users when creating or updating a resource but can't be returned during a read or list request.

### Viewing supported resource operations
<a name="resource-types-schemas-events"></a>

You can determine which operations a resource type supports by referring to the `handlers` section of its resource type schema. If the resource type supports an operation, it's listed in the `handlers` section, and it contains a `permissions` element that lists the permissions that the handler requires.

For example, below is the `handlers` section of the resource type schema for the `AWS::Logs::LogGroup` resource type. This section shows that this resource type supports all five resource operations, and lists the permissions that each handler requires.

```
  "handlers": {
    "create": {
      "permissions": [
        "logs:DescribeLogGroups",
        "logs:CreateLogGroup",
        "logs:PutRetentionPolicy"
      ]
    },
    "read": {
      "permissions": [
        "logs:DescribeLogGroups"
      ]
    },
    "update": {
      "permissions": [
        "logs:DescribeLogGroups",
        "logs:AssociateKmsKey",
        "logs:DisassociateKmsKey",
        "logs:PutRetentionPolicy",
        "logs:DeleteRetentionPolicy"
      ]
    },
    "delete": {
      "permissions": [
        "logs:DescribeLogGroups",
        "logs:DeleteLogGroup"
      ]
    },
    "list": {
      "permissions": [
        "logs:DescribeLogGroups"
      ]
    }
  }
```