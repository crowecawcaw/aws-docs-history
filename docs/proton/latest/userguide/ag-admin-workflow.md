End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Getting started workflow

Learn to create template bundles, create and register templates, and create environments and services by following the example steps and links.

Before starting, verify that you created an [AWS Proton service role](ag-setting-up-iam.md#setting-up-cicd "ag-setting-up-iam.md#setting-up-cicd").

If your service template includes an AWS Proton service pipeline, verify that you created an [AWS CodeStar
connection](setting-up-for-service.md#setting-up-vcontrol "setting-up-for-service.md#setting-up-vcontrol") and a [AWS Proton pipeline service role](ag-setting-up-iam.md#setting-up-cicd "ag-setting-up-iam.md#setting-up-cicd").

For more information, see [The AWS Proton service API
Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

###### Example: Getting started workflow

1. Refer to the diagram in [How AWS Proton works](ag-works.md "ag-works.md") for a high-level view of AWS Proton inputs and outputs.
2. [Create an environment bundle and a service template bundle](ag-template-authoring.md#ag-template-bundles "ag-template-authoring.md#ag-template-bundles").
   1. Identify [input parameters](parameters.md "parameters.md").
   2. Create a [schema file](ag-schema.md "ag-schema.md").
   3. Create [infrastructure as code (IaC) files](ag-infrastructure-tmp-files.md "ag-infrastructure-tmp-files.md").
   4. To [wrap up your template bundle](ag-wrap-up.md "ag-wrap-up.md"), create a manifest file and organize your IaC files, manifest files, and
      schema file in directories.
   5. Make your [template bundle](ag-wrap-up.md "ag-wrap-up.md") accessible to AWS Proton.

3. [Create and register an environment template version](template-create.md "template-create.md") with AWS Proton.

When you use the console to create and register a template, a template version is automatically created.

When you use the AWS CLI to create and register a template:

    1. Create an environment template.
    2. Create an environment template version.For more information, see [CreateEnvironmentTemplate](../APIReference/API_CreateEnvironmentTemplate.md "../APIReference/API_CreateEnvironmentTemplate.md") and [CreateEnvironmentTemplateVersion](../APIReference/API_CreateEnvironmentTemplateVersion.md "../APIReference/API_CreateEnvironmentTemplateVersion.md") in the *AWS Proton API reference*.

4. [Publish your environment template](template-update.md "template-update.md") to make it available for use.

For more information, see [UpdateEnvironmentTemplateVersion](../APIReference/API_UpdateEnvironmentTemplateVersion.md "../APIReference/API_UpdateEnvironmentTemplateVersion.md") in the _AWS Proton API reference_. 5. To [create an environment](ag-create-env.md "ag-create-env.md"), select a published environment template version and provide values for required
inputs.

For more information, see [CreateEnvironment](../APIReference/API_CreateEnvironment.md "../APIReference/API_CreateEnvironment.md")
in the _AWS Proton API reference_. 6. [Create and register a service template version](template-create.md "template-create.md") with AWS Proton.

When you use the console to create and register a template, a template version is automatically created.

When you use the AWS CLI to create and register a template:

    1. Create a service template.
    2. Create a service template version.For more information, see [CreateServiceTemplate](../APIReference/API_CreateServiceTemplate.md "../APIReference/API_CreateServiceTemplate.md") and [CreateServiceTemplateVersion](../APIReference/API_CreateServiceTemplateVersion.md "../APIReference/API_CreateServiceTemplateVersion.md") in the *AWS Proton API reference*.

7. [Publish your service template](template-update.md "template-update.md") to make it available for use.

For more information, see [UpdateServiceTemplateVersion](../APIReference/API_UpdateServiceTemplateVersion.md "../APIReference/API_UpdateServiceTemplateVersion.md") in the _AWS Proton API reference_. 8. To [create a service](ag-create-svc.md "ag-create-svc.md"), select a published service template version and provide values for required
inputs.

For more information, see [CreateService](../APIReference/API_CreateService.md "../APIReference/API_CreateService.md") in the
_AWS Proton API reference_.
