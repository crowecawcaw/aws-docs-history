# Manage custom image creation in Image Builder through a repeatable pipeline process

Image Builder image pipelines provide an automation framework for creating and
maintaining custom AMIs and container images. Pipelines deliver the
following functionality:

- Assemble the base image, build and test components for image customization,
  infrastructure configuration, and distribution settings.
- Facilitate scheduling for automated maintenance processes using
  the `Schedule builder` in the console wizard, or entering
  cron expressions for recurring updates to your images.
- Enable change detection for the base image and components, to
  automatically skip scheduled builds when there are no changes.
- Enable rule-based automation through Amazon EventBridge.

###### Note

For more information about using the EventBridge API to view or change
rules, see the [Amazon EventBridge API Reference](../../../eventbridge/latest/APIReference.md "../../../eventbridge/latest/APIReference.md"). For more information about using EventBridge
**events** commands in the AWS CLI to view or change
rules, see [events](../../../cli/latest/reference/events.md "../../../cli/latest/reference/events.md")
in the _AWS CLI Command Reference_.

###### Topics

- [Configure pipeline execution settings for image pipelines](schedule-pipeline.md "schedule-pipeline.md")
- [List and view pipeline details](pipeline-details.md "pipeline-details.md")
- [Create and update AMI image pipelines](ami-image-pipelines.md "ami-image-pipelines.md")
- [Create and update container image pipelines](container-image-pipelines.md "container-image-pipelines.md")
- [Configure image pipeline workflows in Image Builder](pipeline-workflows.md "pipeline-workflows.md")
- [Use EventBridge rules with Image Builder pipelines](ev-rules-for-pipeline.md "ev-rules-for-pipeline.md")
