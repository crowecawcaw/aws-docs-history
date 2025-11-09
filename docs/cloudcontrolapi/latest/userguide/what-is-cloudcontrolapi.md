# What is AWS Cloud Control API?

Use AWS Cloud Control API to create, read, update, delete, and list (CRUD-L) your cloud resources that
belong to AWS and third-party services. With the Cloud Control API standardized set of application programming interfaces
(APIs), you can perform CRUD-L operations on any supported resources in your AWS account. Using Cloud Control API, you won't
have to generate code or scripts specific to each individual service responsible for those resources.

###### Topics

- [Are you a first-time Cloud Control API user?](#first-time-user "#first-time-user")
- [Features of Cloud Control API](#cloudcontrolapi-feature-overview "#cloudcontrolapi-feature-overview")
- [Related services](#related-services "#related-services")
- [Accessing Cloud Control API](#accessing-cloudcontrolapi "#accessing-cloudcontrolapi")
- [How Cloud Control API works](how-it-works.md "how-it-works.md")

## Are you a first-time Cloud Control API user?

If you're a first-time user of Cloud Control API, we recommend that you begin by reading the
following sections:

- [Setting up AWS Cloud Control API](setting-up.md "setting-up.md")
- [Getting started with Cloud Control API](getting-started.md "getting-started.md")

## Features of Cloud Control API

Cloud Control API provides you with consistent control over the resources in your AWS account by
offering a standardized way of accessing and provisioning those resources. It provides a
uniform programmatic interface for making calls directly to the various resource types
available in your AWS account, without having to be familiarized with the APIs of the
underlying web services.

## Related services

Similar to Cloud Control API, AWS CloudFormation also uses resource types to call underlying web services
APIs to provision those resources when you place such a request in your account. However,
CloudFormation focuses on providing resource management, by treating infrastructure as code. Using
CloudFormation, you can author declarative templates that include multiple resources and their
dependencies, and then provision those resources as a _stack_. A stack is a
single unit that you then manage through AWS CloudFormation. You can also centrally manage and provision
stacks across multiple AWS accounts and AWS Regions. To be managed through CloudFormation, a
resource must be created as part of a stack or imported into a stack. For more information,
see the _[AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")_.

## Accessing Cloud Control API

Cloud Control API provides API operations for generating create, read, update, delete, and list
(CRUD-L) resource requests in addition to tracking and managing those requests. You use the
AWS Command Line Interface (AWS CLI) for Cloud Control API operations.

The following table shows the Cloud Control API operations you can use to generate CRUD-L resource
requests.

| API operation                                                                                   | AWS CLI command                                                                                                                                    |
| ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CreateResource](../APIReference/API_CreateResource.md "../APIReference/API_CreateResource.md") | [`create-resource`](../../../cli/latest/reference/cloudcontrol/create-resource.md "../../../cli/latest/reference/cloudcontrol/create-resource.md") |
| [DeleteResource](../APIReference/API_DeleteResource.md "../APIReference/API_DeleteResource.md") | [`delete-resource`](../../../cli/latest/reference/cloudcontrol/delete-resource.md "../../../cli/latest/reference/cloudcontrol/delete-resource.md") |
| [GetResource](../APIReference/API_GetResource.md "../APIReference/API_GetResource.md")          | [`get-resource`](../../../cli/latest/reference/cloudcontrol/get-resource.md "../../../cli/latest/reference/cloudcontrol/get-resource.md")          |
| [ListResources](../APIReference/API_ListResources.md "../APIReference/API_ListResources.md")    | [`list-resources`](../../../cli/latest/reference/cloudcontrol/list-resources.md "../../../cli/latest/reference/cloudcontrol/list-resources.md")    |
| [UpdateResource](../APIReference/API_UpdateResource.md "../APIReference/API_UpdateResource.md") | [`update-resource`](../../../cli/latest/reference/cloudcontrol/update-resource.md "../../../cli/latest/reference/cloudcontrol/update-resource.md") |

The following table shows the Cloud Control API operations that you can use to track and manage
resource requests while they're in process.

| API operation                                                                                                                 | AWS CLI command                                                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CancelResourceRequest](../APIReference/API_CancelResourceRequest.md "../APIReference/API_CancelResourceRequest.md")          | [`cancel-resource-request`](../../../cli/latest/reference/cloudcontrol/cancel-resource-request.md "../../../cli/latest/reference/cloudcontrol/cancel-resource-request.md")             |
| [GetResourceRequestStatus](../APIReference/API_GetResourceRequestStatus.md "../APIReference/API_GetResourceRequestStatus.md") | [`get-resource-request-status`](../../../cli/latest/reference/cloudcontrol/get-resource-request-status.md "../../../cli/latest/reference/cloudcontrol/get-resource-request-status.md") |
| [ListResourceRequests](../APIReference/API_ListResourceRequests.md "../APIReference/API_ListResourceRequests.md")             | [`list-resource-requests`](../../../cli/latest/reference/cloudcontrol/list-resource-requests.md "../../../cli/latest/reference/cloudcontrol/list-resource-requests.md")                |
