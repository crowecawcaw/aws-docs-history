

# Deploy on-demand blueprints

In Amazon SageMaker Unified Studio, project members can use resource blueprints to deploy analytics and machine learning resources on demand from a project, instead of predefining every resource in a project profile. Members see the blueprints that their role in the project authorizes them to deploy, and they deploy those blueprints on demand. The deployed resources appear in the project's resource list.

As an administrator, you govern resource blueprints with three independent controls:
+ **Blueprint authorization grants** – the grants dictate which designations in a project can deploy the blueprint, and apply to projects under specific domain units. For more information, see [Grant members access to deploy resource blueprints](grant-deploy-resource-blueprints.md).
+ **Designations** – the project member's role in a project that dictates which blueprints the member can deploy. For more information, see [Designations](designations.md).
+ **Provisioning role** – the dedicated IAM role used to deploy the resources from the blueprint. This role is separate from the execution role that members use for their daily work. For more information, see [Configure a provisioning role for resource blueprints](resource-blueprint-provisioning-role.md).

## How resource blueprints work
<a name="how-resource-blueprints-work"></a>

With resource blueprints, administrators control which resources project members can deploy and how those resources are provisioned, and members deploy the resources they are authorized to use. The following sections describe how administrators set up resource blueprints, how projects are set up, and how members deploy resources within a project.

### Set up resource blueprints as an administrator
<a name="manage-resource-blueprints"></a>

As an administrator, you set up resource blueprints by completing the following steps:

1. Set the provisioning role – the dedicated IAM role that Amazon SageMaker Unified Studio uses to deploy blueprint resources, kept separate from the execution role that members use for their daily work. For more information, see [Configure a provisioning role for resource blueprints](resource-blueprint-provisioning-role.md).

1. Create blueprint authorization grants that link designations to blueprints, which determine who can deploy which blueprints. For more information, see [Grant members access to deploy resource blueprints](grant-deploy-resource-blueprints.md).

**Note**  
You configure a provisioning role and blueprint authorization grants for the domain account, and you can configure both for any associated accounts.

### Set up projects
<a name="resource-blueprints-project-options"></a>

You can deploy blueprint resources within projects in two main ways, depending on whether the project uses a project profile:
+ **A project that uses a project profile** – the profile defines which blueprints can be deployed, parameter defaults and locked parameters, deployment order, account and AWS Region placement, and project tags. If a blueprint environment in the project profile has its deployment mode set to **On-demand**, project members can deploy it through resource blueprints. These projects can be created either from the Amazon SageMaker Unified Studio domain management portal or from the Amazon SageMaker Unified Studio portal.
+ **A project without a project profile** – the project starts with a single Tooling-category environment that sets the project's account and AWS Region. Project members then deploy additional resources on demand through resource blueprints, governed by blueprint authorization grants rather than by a profile. Projects without a project profile can only be created from the Amazon SageMaker Unified Studio domain management portal.

**Note**  
Projects created before November 19, 2026 from IAM-based and Identity Center-based domains use a managed project profile named "Default Project Profile". This profile can only deploy S3Bucket and S3TableCatalog blueprints from resource blueprints. To let members deploy other blueprints, disassociate the project profile from the project. For more information, see [Disassociate a project profile from a project](remove-project-profile.md).

The following image shows the project creation workflow, without a project profile, from the Amazon SageMaker Unified Studio domain management portal.

![The project creation workflow without a project profile, in the Amazon SageMaker Unified Studio domain management portal.](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/resource-blueprints/resource-blueprints-project.png)


### Deploy resource blueprints in a project
<a name="deploy-resource-blueprints-in-project"></a>

Within a project, if your designation has a grant for a blueprint, you can deploy that blueprint yourself from **Resource blueprints** in the project. To deploy a blueprint, your designation must include the **Manage Environments** permission. The deployed resource then appears in the project's resource list.

The following image shows which blueprints a project member can deploy in the project.

![Deploying a blueprint from the resource blueprints page in a project in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/resource-blueprints/resource-blueprints-gallery.png)


**Topics**
+ [How resource blueprints work](#how-resource-blueprints-work)
+ [Configure a provisioning role for resource blueprints](resource-blueprint-provisioning-role.md)
+ [Grant members access to deploy resource blueprints](grant-deploy-resource-blueprints.md)
+ [Disassociate a project profile from a project](remove-project-profile.md)
+ [Available resource blueprints](available-resource-blueprints.md)