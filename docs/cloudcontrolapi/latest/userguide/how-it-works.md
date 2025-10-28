# How Cloud Control API works

Cloud Control API provides you with centralized control over the resources in your AWS account and
a consistent way of accessing and provisioning those resources. It provides a uniform
programmatic interface for making calls directly to the various resource types available in
your AWS account.

A _resource type_ represents an artifact that can be provisioned
through a web service: an Amazon Elastic Compute Cloud (Amazon EC2) instance, an Amazon Relational Database Service (Amazon RDS) database instance,
an AWS Identity and Access Management (IAM) policy, or even an entire web application. Each resource type uses a
standardized syntax to support some or all the following lifecycle events: create, read,
update, delete, and list (CRUD-L). You can directly invoke these CRUD-L event handlers using
Cloud Control API as a consistent set of APIs.

Amazon has published several hundred resource types representing offerings across AWS
web services. Now, third-party publishers can make their own resource types available for use
as well. Any resource type developed using the [AWS CloudFormation
CLI](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md") open-source tool is automatically supported by Cloud Control API.

Each resource type is defined by its _resource type schema_. This
document is compliant with the [JSON schema](https://json-schema.org/ "https://json-schema.org/") open
standard, and includes:

- A complete list of each resource property and its associated metadata, including
  whether the property is required, data type, and value constraints.
- The CRUD-L events that the resource type supports, and the permissions necessary for
  Cloud Control API to invoke each supported event handler.
  When you create or update a resource, you specify JSON that represents the properties and
  property values you want to set for the resource. Cloud Control API handles the actual calls to the
  underlying web services to perform the requested changes. For read requests, Cloud Control API returns
  JSON that represents the current state of the specified resource. For list requests, Cloud Control API
  returns either the resource identifier or JSON that represents the current state of the
  specified resources.

You can use Cloud Control API to perform operations on existing resources, even if those resources
weren't created using Cloud Control API. For example, you could use Cloud Control API to return property information
about each AWS Lambda function in your AWS account.

For a brief tutorial on how to use Cloud Control API to perform resource operations, see [Getting started with Cloud Control API](getting-started.md "getting-started.md").

For more information about resource types and how to use them with Cloud Control API, see [Using Cloud Control API resource types](resource-types.md "resource-types.md").
