# Cloud Control API resource operations

Use AWS Cloud Control API to do or other command verb construction create, read, update, remove, and list (-L) operations
 on resources in your AWS account.

###### Contents

* [Prerequisites](#resource-operations-prerequisites "#resource-operations-prerequisites")
* [Specifying credentials](#resource-operations-permissions "#resource-operations-permissions")
* [Ensuring requests are unique](#resource-operations-idempotency "#resource-operations-idempotency")
* [Considerations](#resource-operations-considerations "#resource-operations-considerations")
* [Creating a resource](resource-operations-create.md "resource-operations-create.md")
* [Updating a resource](resource-operations-update.md "resource-operations-update.md")
* [Deleting a resource](resource-operations-delete.md "resource-operations-delete.md")
* [Discovering resources](resource-operations-list.md "resource-operations-list.md")
* [Reading a resource](resource-operations-read.md "resource-operations-read.md")
* [Managing resource requests](resource-operations-manage-requests.md "resource-operations-manage-requests.md")
* [Identifying resources with AWS Cloud Control API](resource-identifier.md "resource-identifier.md")

## Prerequisites for using resources with Cloud Control API


To provision a specific resource using Cloud Control API, that resource type must support Cloud Control API and be available for use
 in your AWS account.



* **Resources available for use in your AWS account**


To be available for use in your account, public resource types must be activated, and private resource types
 must be registered. Supported AWS resource types are public and always activated. For more information, see [Using Cloud Control API resource types](resource-types.md "resource-types.md").
* **Resources that support Cloud Control API**


For a list of AWS resource types that support Cloud Control API, see [Resource types that support Cloud Control API](supported-resources.md "supported-resources.md").


Third-party resource types, both public and private, support Cloud Control API.


For details about how to determine if a specific resource type supports Cloud Control API, see [Determining if a resource type
 supports Cloud Control API](resource-types.md#resource-types-determine-support "resource-types.md#resource-types-determine-support").

For information about using resource types, see [Using Cloud Control API resource types](resource-types.md "resource-types.md").


## Specifying credentials for Cloud Control API


As part of performing operations on AWS resources on your behalf, Cloud Control API must make calls to the underlying
 AWS services that actually provision those resources. To do so, Cloud Control API requires the necessary credentials to
 access those services. There are two ways for you to enable Cloud Control API to acquire those credentials:



* **User credentials**


By default, Cloud Control API creates a temporary session using your AWS user
 credentials, and uses that to make any necessary calls to downstream AWS
 services. This session lasts up to 24 hours, after which any remaining calls to
 AWS by Cloud Control API will fail.
* **Service role credentials**


You can also specify a service role for Cloud Control API to assume during a resource operation, when you make
 the resource request. Among other advantages, specifying a service role enables Cloud Control API to make calls to underlying
 AWS services for up to 36 hours.


To use a service role, specify the `RoleArn` parameter of the resource operation
 request.


Because the Cloud Control API actions are part of the AWS CloudFormation service, the service role you specify is assumed by
 the CloudFormation service (`cloudformation.amazonaws.com`). For more information, see [AWS CloudFormation service
 role](../../../AWSCloudFormation/latest/UserGuide/using-iam-servicerole.md "../../../AWSCloudFormation/latest/UserGuide/using-iam-servicerole.md") in the *AWS CloudFormation User Guide*.

The permissions required for each resource handler are defined in the `handlers` section of that
 resource type's schema. For more information about viewing the resource schema, see .[Viewing resource type schemas](resource-types.md#resource-types-schemas "resource-types.md#resource-types-schemas") The `handlers` section is
 defined in the [resource type
 definition schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers").


## Ensuring resource operation requests
 are unique when using Cloud Control API


As a best practice, we strongly recommend you specify an idempotency token with create, delete, and update
 resource operation requests. Preferably, specify a token that will be unique for every request, such as an
 universally unique identifier (UUID). Such a token ensures requests can be disambiguated in cases where a request
 must be retried.


The `create-resource`, `delete-resource`, and `update-resource` operations
 all take a `client-token` parameter, which can be set to an idempotency token.


## Considerations when using
 Cloud Control API


We recommend that you take the following service behavior into account when performing resource operations
 using Cloud Control API:



* Cloud Control API performs each resource operation individually and independently of any other resource
 operations.
* A single resource operation request to Cloud Control API might actually consist of multiple calls to the
 underlying service that provisions the resource. Because of this, a resource request might fail when only partially
 completed, resulting in only some of the requested changes being applied to the resource.
* If a resource operation fails at any point, Cloud Control API doesn't roll back the resource to its previous
 state.
* You can only perform one resource operation at a time on a given resource using Cloud Control API. However, the
 resource can still be operated on directly, through the underlying service that provisioned it. We strongly
 recommend against this approach because it may lead to unpredictable behavior.
