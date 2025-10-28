# Use components to customize your Image Builder image

Image Builder uses the AWS Task Orchestrator and Executor (AWSTOE) component management application to
orchestrate complex workflows. Build and test components that work with the
AWSTOE application are based on YAML documents that define the scripts to customize
or test your image. For AMI images, Image Builder installs components and the AWSTOE component
management application on its Amazon EC2 build and test instances. For container images, the
components and AWSTOE component management application are installed inside of the
running container.

Image Builder uses AWSTOE to perform all on-instance activities. There is no additional
setup required to interact with AWSTOE when you run Image Builder commands or use the
Image Builder console.

###### Note

When a component that is managed by Amazon reaches the end of its support lifespan,
it is no longer maintained. About four weeks before this occurs, any accounts that are
using the component receive notification, and a list of the affected recipes in their
account from their AWS Health Dashboard. To learn more about AWS Health, see
[AWS Health User Guide](../../../health/latest/ug.md "../../../health/latest/ug.md").

###### Workflow stages for building a new image

The Image Builder workflow for building new images includes the following two
distinct stages.

1. Build stage (pre-snapshot) –
   During the build stage, you make changes to the Amazon EC2 build instance
   that's running your base image, to create the baseline for your new
   image. For example, your recipe can include components
   that install an application or modify the operating system firewall settings.

The following phases from your component document run during the build stage:

    * build
    * validate

After this stage completes successfully, Image Builder creates a snapshot or
container image that it uses for the test stage and beyond. 2. Test stage (post-snapshot) – During the
test stage, there are some differences between images that create AMIs and container images. For
AMI workflows, Image Builder launches an EC2 instance from the snapshot that it created
as the final step of the build stage. Tests run on the new instance to validate
settings and ensure that the instance is functioning as expected. For container workflows, the
tests run on the same instance that was used for building.

The following phase from your component document runs for every component that
is included in the recipe during the image build test stage:

    * test

This component phase applies to both Build and Test component types. After this stage
completes successfully, Image Builder can create and distribute your final image from the snapshot or
the container image.

###### Note

While the AWSTOE application framework allows you to define many phases in a
component document, Image Builder has strict rules about what phases it runs, and during which
stages it runs them. For a component to run during the image build stage, the
component document must define at least one of these phases: `build`
or `validate`. For a component to run during the image test stage,
the component document must define the `test` phase, and no
other phases.

Since Image Builder runs the stages independently, chaining references in component
documents cannot cross stage boundaries. You cannot chain a value from
a phase that runs in the build stage to a phase that runs in the test
stage. You can, however, define input parameters to the intended target,
and pass in values through the command line. For more information about
setting component parameters in your Image Builder recipes, see
[Tutorial: Create a custom component with input parameters](tutorial-component-parameters.md "tutorial-component-parameters.md").

To assist with troubleshooting on your build or test instance AWSTOE creates a
log folder that contains the input document and log files to track what's happening
each time a component runs. If you configured an Amazon S3 bucket in your pipeline
configuration, the logs are also written there. For more information about YAML
documents and log output, see [Use the AWSTOE component document framework for custom components](toe-use-documents.md "toe-use-documents.md").

###### Tip

When you have many components to keep track of, tagging helps you to
identify a specific component or version based on the tags you've assigned to it.
For more information about tagging your resources using Image Builder commands
in the AWS CLI, see the [Tag resources](tag-resources.md "tag-resources.md")
section of this guide.

This section covers how to list, view, create, and import components, using
the Image Builder console or commands in the AWS CLI.

###### Topics

- [List and view component details](component-details.md "component-details.md")
- [Use AWS Marketplace components to customize your image](use-marketplace-components.md "use-marketplace-components.md")
- [Use managed components to customize your Image Builder image](use-managed-components.md "use-managed-components.md")
- [Develop custom components for your Image Builder image](create-custom-components.md "create-custom-components.md")
- [How Image Builder uses the AWS Task Orchestrator and Executor application to manage components](toe-component-manager.md "toe-component-manager.md")
