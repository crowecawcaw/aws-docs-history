# External Engines for AWS Service Catalog

In AWS Service Catalog, _external engines_ are represented through an `EXTERNAL` product type.
The `EXTERNAL` product type allows for the integration of third-party provisioning engines, such as Terraform.
You can use external engines to extend the capabilities of Service Catalog beyond the native AWS CloudFormation templates, enabling the use of other instructure as code (IaC) tools.

The `EXTERNAL` product type allows you to manage and deploy resources using the familiar interface of Service Catalog while leveraging the specific features and syntax of your chosen IaC tool.

To enable `EXTERNAL` product types in Service Catalog, you must define a set of standard resources in your account.
These resources are known as the _engine_.
Service Catalog delegate tasks to the engine at specific points in the artifact-parsing and provisioning operations.

A _provisioning artifact_ represents the specific version of a product within Service Catalog, allowing you to manage and deploy consistent resources.

When you call AWS Service Catalog's [DescribeProvisioningArtifact](../dg/API_DescribeProvisioningArtifact.md "../dg/API_DescribeProvisioningArtifact.md")
or [DescribeProvisioningParameters](../dg/API_DescribeProvisioningParameters.md "../dg/API_DescribeProvisioningParameters.md") operations
for a provisioning artifact for an `EXTERNAL` product type,
Service Catalog invokes an AWS Lambda function in the engine. This is required to extract the list of parameters from the provided provisioning artifact
and return them to AWS Service Catalog. These parameters will be used later as part of the provisioning process.

When you provision an `EXTERNAL` provisioning artifact by calling
[ProvisionProduct](../dg/API_ProvisionProduct.md "../dg/API_ProvisionProduct.md"),
Service Catalog first performs some actions internally, then send a message to an Amazon SQS queue in the engine.
Next, the engine assumes the provided _launch role_ (the IAM role that you assign to a product as a launch constraint),
provisions the resources based on the provided provisioning artifact,
and invokes the [NotifyProvisionProductEngineWorkflowResult](../dg/API_NotifyProvisionProductEngineWorkflowResult.md "../dg/API_NotifyProvisionProductEngineWorkflowResult.md")
API to report success or failure.

Calls to
[UpdateProvisionedProduct](../dg/API_UpdateProvisionedProduct.md "../dg/API_UpdateProvisionedProduct.md")
and [TerminateProvisionedProduct](../dg/API_TerminateProvisionedProduct.md "../dg/API_TerminateProvisionedProduct.md")
are handled similarly, with each having a distinct queue and Notify APIs:

- [NotifyProvisionProductEngineWorkflowResult](../dg/API_NotifyProvisionProductEngineWorkflowResult.md "../dg/API_NotifyProvisionProductEngineWorkflowResult.md")
- [NotifyUpdateProvisionedProductEngineWorkflowResult](../dg/API_NotifyUpdateProvisionedProductEngineWorkflowResult.md "../dg/API_NotifyUpdateProvisionedProductEngineWorkflowResult.md")
- [NotifyTerminateProvisionedProductEngineWorkflowResult](../dg/API_NotifyTerminateProvisionedProductEngineWorkflowResult.md "../dg/API_NotifyTerminateProvisionedProductEngineWorkflowResult.md").

###### Topics

- [Considerations](#external-engine-considerations "#external-engine-considerations")
- [Parameter Parsing](#external-engine-parameters "#external-engine-parameters")
- [Provisioning](#external-engine-provisioning "#external-engine-provisioning")
- [Updating](#external-engine-updating "#external-engine-updating")
- [Terminating](#external-engine-terminating "#external-engine-terminating")
- [Tagging](#external-engine-tagging "#external-engine-tagging")

## Considerations

**Limit of one external engine per hub account**

You can only use one `EXTERNAL` provisioning engine per Service Catalog hub account. The Service Catalog _hub-and-spoke_
model allows the hub account to create baseline products and share the portfolio while the spoke accounts import portfolios and leverage the products.

This limit is because `EXTERNAL` can only be routed to one engine in an account. If
an administrator wants to have multiple external engines, the administrator must set up the external engines (along with the portfolios and products) in different hub accounts.

**External engines only support launch roles with launch contraints**

`EXTERNAL` provisioning artifacts only support provisioning with launch roles which are specified using _launch constraints_.
A launch constraint specifies the IAM role that Service Catalog assumes when an end user launches, updates, or terminates a product.
For more information on launch constraints, see [AWS Service Catalog Launch Constraints](constraints-launch.md "constraints-launch.md").

## Parameter Parsing

`EXTERNAL` provisioning artifacts can be of any format. This means that when creating an `EXTERNAL` product type,
the engine is required to extract the list of parameters from the provided provisioning artifact and return them to Service Catalog.
This is done by creating a Lambda function in your account that can accept the following request format, process the provisioning artifact,
and return the following response format.

###### Important

The Lambda function must be named `ServiceCatalogExternalParameterParser`.

**Request syntax:**

```
{
    "artifact": {
        "path": "`string`",
        "type": "`string`"
    },
    "launchRoleArn": "`string`"
}
```

| **Field**       | **Type** | **Required** | **Description**                                                                                                                                                   |
| --------------- | -------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| artifact        | object   | Yes          | Details for the artifact to be parsed.                                                                                                                            |
| artifact / path | string   | Yes          | Location from where the parser downloads the artifact. For example, for `AWS_S3`, this is the Amazon S3 URI.                                                      |
| artifact / type | string   | Yes          | Type of artifact. Allowed value: `AWS_S3`.                                                                                                                        |
| launchRole      | string   | No           | The Amazon Resource Name (ARN) of the launch role to assume when downloading the artifact.<br>If no launch role is provided, the Lambda's execution role is used. |

**Response syntax:**

```
{
    "parameters": [
        {
            "key": "`string`"
            "`defaultValue`": "`string`",
            "type": "`string`",
            "description": "`string`",
            "isNoEcho": boolean
        },
    ]
}
```

| **Field**    | **Type** | **Required** | **Description**                                                                                                                                                                                                            |
| ------------ | -------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| parameters   | list     | Yes          | The list of parameters that Service Catalog asks the end user to provide when provisioning a product or updating a provisioned product.<br>If no parameters are defined in the artifact, an empty list is returned.        |
| key          | string   | Yes          | The parameter key.                                                                                                                                                                                                         |
| defaultValue | string   | No           | The default value of the parameter if the end user does not provide a value.                                                                                                                                               |
| type         | string   | Yes          | The expected type of the parameter value for the engine. For example, a string, boolean, or map.<br>The allowed values are specific to each engine. Service Catalog passes each parameter value to the engine as a string. |
| description  | string   | No           | Description for the parameter. It is recommended that this is user-friendly.                                                                                                                                               |
| isNoEcho     | boolean  | no           | Determines if the parameter value is not echoed in logs. Default value is false (parameter values are echoed).                                                                                                             |

## Provisioning

For the [ProvisionProduct](../dg/API_ProvisionProduct.md "../dg/API_ProvisionProduct.md") operation,
Service Catalog delegates the actual provisioning of resources to the engine.
The engine is responsible for interfacing with your IaC solution of choice (such as Terraform) to provision resources as defined in the artifact.
The engine is also responsible for notifying Service Catalog of the result.

Service Catalog sends all Provision requests to an Amazon SQS queue in your account named `ServiceCatalogExternalProvisionOperationQueue`.

**Request syntax:**

```
{
    "token": "`string`",
    "operation": "`string`",
    "provisionedProductId": "`string`",
    "provisionedProductName": "`string`",
    "productId": "`string`",
    "provisioningArtifactId": "`string`",
    "recordId": "`string`",
    "launchRoleArn": "`string`",
    "artifact": {
        "path": "`string`",
        "type": "`string`"
    },
    "identity": {
        "principal": "`string`",
        "awsAccountId": "`string`",
        "organizationId": "`string`"
    },
    "parameters": [
        {
            "key": "`string`",
            "value": "`string`"
        }
    ],
    "tags": [
        {
            "key": "`string`",
            "value": "`string`"
        }
    ]
}
```

| **Field**              | **Type** | **Required** | **Description**                                                                                                         |
| ---------------------- | -------- | ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| token                  | string   | Yes          | The token that identifies this operation. The token must be returned to Service Catalog to notify of execution results. |
| operation              | string   | Yes          | This field must be `PROVISION_PRODUCT` for this operation.                                                              |
| provisionedProductId   | string   | Yes          | ID of the provisioned product.                                                                                          |
| provisionedProductName | string   | Yes          | Name of the provisioned product.                                                                                        |
| productId              | string   | Yes          | ID of the product.                                                                                                      |
| provisioningArtifactId | string   | Yes          | ID of the provisioning artifact.                                                                                        |
| recordId               | string   | Yes          | ID of the Service Catalog record for this operation.                                                                    |
| launchRoleArn          | string   | Yes          | Amazon Resource Name (ARN) for the IAM role to use for provisioning resources.                                          |
| artifact               | object   | Yes          | Details for the artifact that defines how the resources are provisioned.                                                |
| artifact / path        | string   | Yes          | Location from where the engine downloads the artifact. For example, for `AWS_S3`, this is the Amazon S3 URI.            |
| artifact / type        | string   | Yes          | Type of artifact. Allowed value: `AWS_S3`.                                                                              |
| identity               | string   | No           | The field is currently not used.                                                                                        |
| parameters             | list     | Yes          | List of parameter key-value pairs the user entered to Service Catalog as inputs for this operation.                     |
| tags                   | list     | Yes          | List of key-value-pairs the user entered to Service Catalog as tags to apply to the provisioned resources.              |

**Workflow Result Notification:**

Invoke the
[NotifyProvisionProductEngineWorkflowResult](../dg/API_NotifyProvisionProductEngineWorkflowResult .md "../dg/API_NotifyProvisionProductEngineWorkflowResult .md")
API with the response object specified on the API details page.

## Updating

For the [UpdateProvisionedProduct](../dg/API_UpdateProvisionedProduct.md "../dg/API_UpdateProvisionedProduct.md") operation,
Service Catalog delegates the actual updating of resources to the engine.
The engine is responsible for interfacing with your IaC solution of choice (such as Terraform) to updating resources as defined in the artifact.
The engine is also responsible for notifying Service Catalog of the result.

Service Catalog sends all Update requests to an Amazon SQS queue in your account named `ServiceCatalogExternalUpdateOperationQueue`.

**Request syntax:**

```
{
    "token": "`string`",
    "operation": "`string`",
    "provisionedProductId": "`string`",
    "provisionedProductName": "`string`",
    "productId": "string",
    "provisioningArtifactId": "`string`",
    "recordId": "`string`",
    "launchRoleArn": "`string`",
    "artifact": {
        "path": "`string`",
        "type": "`string`"
    },
    "identity": {
        "principal": "`string`",
        "awsAccountId": "`string`",
        "organizationId": "`string`"
    },
    "parameters": [
        {
            "key": "`string`",
            "value": "`string`"
        }
    ],
    "tags": [
        {
            "key": "`string`",
            "value": "`string`"
        }
    ]
}
```

| **Field**              | **Type** | **Required** | **Description**                                                                                                         |
| ---------------------- | -------- | ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| token                  | string   | Yes          | The token that identifies this operation. The token must be returned to Service Catalog to notify of execution results. |
| operation              | string   | Yes          | This field must be `UPDATE_PROVISION_PRODUCT` for this operation.                                                       |
| provisionedProductId   | string   | Yes          | ID of the provisioned product.                                                                                          |
| provisionedProductName | string   | Yes          | Name of the provisioned product.                                                                                        |
| productId              | string   | Yes          | ID of the product.                                                                                                      |
| provisioningArtifactId | string   | Yes          | ID of the provisioning artifact.                                                                                        |
| recordId               | string   | Yes          | ID of the Service Catalog record for this operation.                                                                    |
| launchRoleArn          | string   | Yes          | Amazon Resource Name (ARN) for the IAM role to use for provisioning resources.                                          |
| artifact               | object   | Yes          | Details for the artifact that defines how the resources are provisioned.                                                |
| artifact / path        | string   | Yes          | Location from where the engine downloads the artifact. For example, for `AWS_S3`, this is the Amazon S3 URI.            |
| artifact / type        | string   | Yes          | Type of artifact. Allowed value: `AWS_S3`.                                                                              |
| identity               | string   | No           | The field is currently not used.                                                                                        |
| parameters             | list     | Yes          | List of parameter key-value pairs the user entered to Service Catalog as inputs for this operation.                     |
| tags                   | list     | Yes          | List of key-value-pairs the user entered to Service Catalog as tags to apply to the provisioned resources.              |

**Workflow Result Notification:**

Invoke the
[NotifyUpdateProvisionedProductEngineWorkflowResult](../dg/API_NotifyUpdateProvisionedProductEngineWorkflowResult.md "../dg/API_NotifyUpdateProvisionedProductEngineWorkflowResult.md")
API with the response object specified on the API details page.

## Terminating

For the [TerminateProvisionedProduct](../dg/API_TerminateProvisionedProduct.md "../dg/API_TerminateProvisionedProduct.md") operation,
Service Catalog delegates the actual terminating of resources to the engine.
The engine is responsible for interfacing with your IaC solution of choice (such as Terraform) to terminate resources as defined in the artifact.
The engine is also responsible for notifying Service Catalog of the result.

Service Catalog sends all Terminate requests to an Amazon SQS queue in your account named `ServiceCatalogExternalTerminateOperationQueue`.

**Request syntax:**

```
{
    "token": "`string`",
    "operation": "`string`",
    "provisionedProductId": "`string`",
    "provisionedProductName": "`string`",
    "recordId": "`string`",
    "launchRoleArn": "`string`",
    "identity": {
        "principal": "`string`",
        "awsAccountId": "`string`",
        "organizationId": "`string`"
    }
}
```

| **Field**              | **Type** | **Required** | **Description**                                                                                                         |
| ---------------------- | -------- | ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| token                  | string   | Yes          | The token that identifies this operation. The token must be returned to Service Catalog to notify of execution results. |
| operation              | string   | Yes          | This field must be `TERMINATE_PROVISION_PRODUCT` for this operation.                                                    |
| provisionedProductId   | string   | Yes          | ID of the provisioned product.                                                                                          |
| provisionedProductName | string   | Yes          | Name of the provisioned product.                                                                                        |
| recordId               | string   | Yes          | ID of the Service Catalog record for this operation.                                                                    |
| launchRoleArn          | string   | Yes          | Amazon Resource Name (ARN) for the IAM role to use for provisioning resources.                                          |
| identity               | string   | No           | The field is currently not used.                                                                                        |

**Workflow Result Notification:**

Invoke the
[NotifyTerminateProvisionedProductEngineWorkflowResult](../dg/API_NotifyTerminateProvisionedProductEngineWorkflowResult.md "../dg/API_NotifyTerminateProvisionedProductEngineWorkflowResult.md")
API with the response object specified on the API details page.

## Tagging

For managing tags through Resource Groups, your launch role need the following additional permission statements:

```
{
    "Effect": "Allow",
    "Action": [
        "resource-groups:CreateGroup",
        "resource-groups:ListGroupResources"
    ],
    "Resource": "*"
},
{
    "Effect": "Allow",
    "Action": [
        "tag:GetResources",
        "tag:GetTagKeys",
        "tag:GetTagValues",
        "tag:TagResources",
        "tag:UntagResources"
    ],
    "Resource": "*"
}
```

###### Note

The launch role also needs tagging permissions on the specific resources in the artifact, such
as `ec2:CreateTags`.
