# Excluding resources from recording with

AWS Config

AWS Config allows you to exclude specific types of AWS resources from inventory tracking and
compliance monitoring while still tracking all other supported resource types currently
available in AWS Config, including those that will be added in the future. You can use this feature
to concentrate on critical resources that are subject to your compliance and governance
standards.

Excluding resources (Console)
If you do not want to record an AWS resource type, use one of the following
recording strategies for the AWS Config console:

- **Record all resource types with customizable overrides**,
  choose the resource type you want to exclude, and choose the override "Exclude from
  recording"
- **Record specific resource types**.

For more detailed steps, see [Recording resources
(Console)](select-resources-console.md "select-resources-console.md").

Excluding resources (AWS CLI)
If you do not want to record an AWS resource type, use one of the following
recording strategies for the API/CLI:

- **Record all current and future resource types with
  exclusions** (`EXCLUSION_BY_RESOURCE_TYPES`)
- **Record specific resource types**
  (`INCLUSION_BY_RESOURCE_TYPES`).

For more detailed steps, see [Recording Resources
(AWS CLI)](select-resources-cli.md "select-resources-cli.md").
