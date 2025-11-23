# Recording Configurations with AWS Config for Third-Party

Resources using the AWS CLI

Record configurations for third-party resources or custom resource types such as on
premise servers, SAAS monitoring tools, and version control systems (like GitHub).

You can publish the configuration data of third-party resources into AWS Config and view and
monitor the resource inventory and configuration history using the AWS Config console and APIs.
You can use AWS Config to manage all your resources and evaluate resource configuration for
compliance against best practices using AWS Config rules. You can also create AWS Config rules or
conformance packs to evaluate these third-party resources against best practices, internal
policies, and regulatory policies.

###### Note

If you have configured AWS Config to record all resource types, then third-party resources
that are managed (created, updated, or deleted) through CloudFormation are automatically tracked
in AWS Config as configuration items.

**Prerequisite:** The third-party resources or custom resource type must
be registered using CloudFormation.

###### Topics

- [Adding Resources](customresources-adding.md "customresources-adding.md")
- [Recording Configuration Items](add-custom-resource-type-cli.md "add-custom-resource-type-cli.md")
- [Reading Configuration Items](view-custom-resource-type-cli.md "view-custom-resource-type-cli.md")
- [Deleting Resources](delete-custom-resource-type.md "delete-custom-resource-type.md")
