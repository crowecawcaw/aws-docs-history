# Learn how to create custom images with Image Builder tutorials

There are many ways to build custom images and components with EC2 Image Builder. Tutorials
help you learn about key Image Builder concepts. Each tutorial presents a use case with steps
that you can follow for the first time. The instructions use defaults where possible to
assist with learning the overall process. After you use one of the tutorials, you can
explore more ways to customize your own images.

## Build your first image

The following tutorials show you how to build your first image with the Image Builder
console wizard. At the end of the tutorial you'll have created the following set
of Image Builder resources. The final step in the tutorial is to clean up the resources
you created.

- An image recipe for your Amazon Machine Image (AMI) or a container
  recipe for your container image.
- An infrastructure configuration resource with default settings.
- A distribution settings resource with default settings that distributes
  the output to the source Region (your account in the Region that you use
  to run the console wizard).
- An image pipeline that uses the listed resources to build your
  output image with the default image build workflows.
- An output AMI or container image.

###### Console wizard tutorials

- [Pipeline wizard: Create AMI](start-build-image-pipeline.md "start-build-image-pipeline.md")
- [Pipeline wizard: Create container image](start-build-container-pipeline.md "start-build-container-pipeline.md")

## Create a custom component with input parameters

The following tutorial shows you how to create a custom component that defines input
parameters, and then set the values from your Image Builder recipe.

[Custom component with parameters](tutorial-component-parameters.md "tutorial-component-parameters.md")

## Use Systems Manager parameters with Image Builder

The following tutorial shows you how to create an AWS Systems Manager Parameter Store parameter and use
it in an image recipe.

[Use a base image parameter in your recipe](tutorial-ssm-parameters-recipe.md "tutorial-ssm-parameters-recipe.md")

You can also use Parameter Store parameters in AMI distribution settings to store your
output image ID, and in custom components. For more information, see
[Create and update AMI distribution configurations](cr-upd-ami-distribution-settings.md "cr-upd-ami-distribution-settings.md") for distributions, and
[Use Systems Manager Parameter Store parameters](toe-user-defined-variables.md#toe-ssm-parameters "toe-user-defined-variables.md#toe-ssm-parameters") for custom components.
