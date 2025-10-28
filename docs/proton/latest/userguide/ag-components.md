End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# AWS Proton components

Components are a type of AWS Proton resource. They add flexibility to service templates. Components provide platform teams with a mechanism to extend
core infrastructure patterns, and define safeguards that empower developers to manage aspects of their application infrastructure.

In AWS Proton administrators define standard infrastructure that is used across development teams and applications. However, development teams might need to
include additional resources for their specific use cases, like Amazon Simple Queue Service (Amazon SQS) queues or Amazon DynamoDB tables. These application-specific resources might
change frequently, particularly during early application development. Maintaining these frequent changes in administrator authored templates might be hard
to manage and scale—administrators would need to maintain many more templates without real administrator added value. The alternative—letting
application developers author templates for their applications—isn't ideal either, because it takes away administrators' ability to standardize the
main architecture components, like AWS Fargate tasks. This is where components come in.

With a component, a developer can add supplemental resources to their application, above and beyond what administrators defined in environment and
service templates. The developer then attaches the component to a service instance. AWS Proton provisions infrastructure resources defined by the component just
like it provisions resources for environments and service instances.

A component can read service instance inputs and provide outputs to the service instance, for a fully integrated experience. For example, if the
component adds an Amazon Simple Storage Service (Amazon S3) bucket for use by a service instance, the component template can take the environment and service instance names into
account for naming the bucket. When AWS Proton renders the service template to provision a service instance, the service instance can refer to the bucket and use
it.

The components that AWS Proton currently supports are _directly defined components_. You pass the Infrastructure as Code (IaC) file that
defines the component's infrastructure directly to the AWS Proton API or console. This is different than an environment or service, where you define IaC in a
template bundle and register the bundle as a template resource, then use a template resource to create the environment or service.

###### Note

Directly defined components allow developers to define extra infrastructure and provision it. AWS Proton provisions all directly defined components running
in the same environment using the same AWS Identity and Access Management (IAM) role.

An administrator can control what developers can do with components in two ways:

- _Supported component sources_ – An administrator can allow the attachment of components to service instances based on a
  property of AWS Proton service template versions. By default, developers can't attach components to service instances.

For more information about this property, see the [supportedComponentSources](../APIReference/API_CreateServiceTemplateVersion.md#proton-CreateServiceTemplateVersion-request-supportedComponentSources "../APIReference/API_CreateServiceTemplateVersion.md#proton-CreateServiceTemplateVersion-request-supportedComponentSources") parameter of the [CreateServiceTemplateVersion](../APIReference/API_CreateServiceTemplateVersion.md "../APIReference/API_CreateServiceTemplateVersion.md") API action in the _AWS Proton API Reference_.

###### Note

When you use template sync, AWS Proton creates service template versions implicitly when you commit changes to a service template bundle in a
repository. In this case, instead of specifying supported component sources during service template version creation, you specify this property in a
file associated with each service template major version. For more information, see [Syncing service templates](create-template-sync.md#create-template-sync-service-templates "create-template-sync.md#create-template-sync-service-templates").

- _Component roles_ – An administrator can assign a component role to an environment. AWS Proton assumes this role when it
  provisions infrastructure defined by directly defined component in the environment. Therefore, the component role scopes down the infrastructure that
  developers can add using directly defined components in the environment. In the absence of the component role, developers can't create directly defined
  components in the environment.

For more information about assigning a component role, see the [componentRoleArn](../APIReference/API_CreateEnvironment.md#proton-CreateEnvironment-request-componentRoleArn "../APIReference/API_CreateEnvironment.md#proton-CreateEnvironment-request-componentRoleArn") parameter of
the [CreateEnvironment](../APIReference/API_CreateEnvironment.md "../APIReference/API_CreateEnvironment.md") API action in the
_AWS Proton API Reference_.

###### Note

Component roles aren't used in [Self-managed provisioning](ag-works-prov-methods.md#ag-works-prov-methods-self "ag-works-prov-methods.md#ag-works-prov-methods-self") environments.

###### Topics

- [How do components compare to other AWS Proton resources?](#ag-components.compare "#ag-components.compare")
- [Components in the AWS Proton console](#ag-components.console "#ag-components.console")
- [Components in the AWS Proton API and AWS CLI](#ag-components.api "#ag-components.api")
- [Component frequently asked questions](#ag-components.faq "#ag-components.faq")
- [Component states](ag-components-states.md "ag-components-states.md")
- [Component infrastructure as code files](ag-components-iac.md "ag-components-iac.md")
- [Component AWS CloudFormation example](ag-components-example-cfn.md "ag-components-example-cfn.md")

## How do components compare to other AWS Proton resources?

In many ways, components are similar to other AWS Proton resources. Their infrastructure is defined in an [IaC template file](ag-components-iac.md "ag-components-iac.md"), authored in either AWS CloudFormation YAML or Terraform HCL format. AWS Proton can provision component infrastructure using either
[AWS-managed provisioning](ag-works-prov-methods.md#ag-works-prov-methods-direct "ag-works-prov-methods.md#ag-works-prov-methods-direct") or [self-managed
provisioning](ag-works-prov-methods.md#ag-works-prov-methods-self "ag-works-prov-methods.md#ag-works-prov-methods-self").

Components are, however, different from other AWS Proton resources in a few ways:

- _Detached state_ – Components are designed to be attached to service instances and to extend their infrastructure, but
  can also be in a _detached_ state, in which they aren't attached to any service instance. For more information about component
  states, see [Component states](ag-components-states.md "ag-components-states.md").
- _No schema_ – Components don't have an associated schema like [template bundles](ag-template-authoring.md#ag-template-bundles "ag-template-authoring.md#ag-template-bundles")
  have. Component inputs are defined by a service. A component can consume inputs when it is attached to a service instance.
- _No customer-managed components_ – AWS Proton always provisions component infrastructure for you. There isn't a
  _bring your own resources_ version of components. For more information about customer-managed environments, see [Create an environment](ag-create-env.md "ag-create-env.md").
- _No template resource_ – Directly defined components don't have an associated template resource similar to environment
  and service templates. You provide an IaC template file directly to the component. Similarly, you directly provide a manifest that defines the
  template language and rendering engine for provisioning the component's infrastructure. You author the template file and the manifest in a way similar
  to authoring a [template bundle](ag-template-authoring.md#ag-template-bundles "ag-template-authoring.md#ag-template-bundles"). However, with directly defined components, there's no requirement to store
  IaC files as bundles in particular locations, and you don't create a template resource in AWS Proton out of IaC files.
- _No CodeBuild-based provisioning_ – You can't provision directly defined components using your own custom provisioning
  script, known as _CodeBuild-based provisioning_. For more information, see [How CodeBuild provisioning works](ag-works-prov-methods.md#ag-works-prov-methods-codebuild "ag-works-prov-methods.md#ag-works-prov-methods-codebuild").

## Components in the AWS Proton console

Use the AWS Proton console to create, update, view, and use AWS Proton components.

The following console pages are related to components. We include direct links to top level console pages.

- [Components](https://console.aws.amazon.com/proton/#/components "https://console.aws.amazon.com/proton/#/components") – View the list of components in your AWS account. You can create
  new components, and update or delete existing components. Choose a component name on the list to view its details page.

Similar lists exist also on the **Environment details** and **Service instance details** pages. These lists show
only the components associated with the resource that is being viewed. When you create a component from one of these lists, AWS Proton pre-selects the
associated environment on the **Create component** page.

- **Component details** – To view the component details page, choose a component name on the [Components](https://console.aws.amazon.com/proton/#/components "https://console.aws.amazon.com/proton/#/components") list.

On the details page, view the component details and status, and update or delete the component. View and manage lists of outputs (for example,
provisioned resource ARNs), provisioned AWS CloudFormation stacks, and assigned tags.

- [Create component](https://console.aws.amazon.com/proton/#/components/create "https://console.aws.amazon.com/proton/#/components/create") – Create a component. Enter the component name and
  description, choose the associated resources, specify the component source IaC file, and assign tags.
- **Update component** – To update a component, select the component on the [Components](https://console.aws.amazon.com/proton/#/components "https://console.aws.amazon.com/proton/#/components") list, and then, on the **Actions** menu, choose **Update
  component**. Alternatively, on the **Component details** pages, choose **Update**.

You can update most of the component's details. You can't update the component name. And you can choose whether or not to redeploy the component
after a successful update.

- **Configure environment** – When you create or update an environment, you can specify a **Component
  role**. This role controls the ability to run directly defined components in the environment and provides permissions for provisioning
  them.
- **Create new service template version** – When you create a service template version, you can specify **Supported
  component sources** for the template version. This controls the ability to attach components to service instances of services based on this
  template version.

## Components in the AWS Proton API and AWS CLI

Use the AWS Proton API or the AWS CLI to create, update, view, and use AWS Proton components.

The following API actions directly manage AWS Proton component resources.

- [CreateComponent](../APIReference/API_CreateComponent.md "../APIReference/API_CreateComponent.md") – Create an AWS Proton
  component.
- [DeleteComponent](../APIReference/API_DeleteComponent.md "../APIReference/API_DeleteComponent.md") – Delete an AWS Proton
  component.
- [GetComponent](../APIReference/API_GetComponent.md "../APIReference/API_GetComponent.md") – Get detailed data for a
  component.
- [ListComponentOutputs](../APIReference/API_ListComponentOutputs.md "../APIReference/API_ListComponentOutputs.md") – Get a list of
  component Infrastructure as Code (IaC) outputs.
- [ListComponentProvisionedResources](../APIReference/API_ListComponentProvisionedResources.md "../APIReference/API_ListComponentProvisionedResources.md")
  – List provisioned resources for a component with details.
- [ListComponents](../APIReference/API_ListComponents.md "../APIReference/API_ListComponents.md") – List components with summary
  data. You can filter the result list by environment, service, or a single service instance.

The following API actions of other AWS Proton resources have some functionality related to components.

- [CreateEnvironment](../APIReference/API_CreateEnvironment.md "../APIReference/API_CreateEnvironment.md"), [UpdateEnvironment](../APIReference/API_UpdateEnvironment.md "../APIReference/API_UpdateEnvironment.md") – Use `componentRoleArn` to specify the
  Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in this environment. It determines
  the scope of infrastructure that a directly defined component can provision.
- [CreateServiceTemplateVersion](../APIReference/API_CreateServiceTemplateVersion.md "../APIReference/API_CreateServiceTemplateVersion.md") –
  Use `supportedComponentSources` to specify supported component sources. Components with supported sources can be attached to service
  instances based on this service template version.

## Component frequently asked questions

What is the lifecycle of a component?

Components can be in an _attached_ or _detached_ state. They are designed to be attached to a service instance
and enhance its infrastructure most of the time. Detached components are in a transitional state that enables you to delete a component or attach it to
another service instance in a controlled and safe way. For more information, see [Component states](ag-components-states.md "ag-components-states.md").

Why can't I delete my attached components?

_Solution:_ To delete an attached component, update the component to detach it from the service instance, validate service instance
stability, and then delete the component.

_Why is this required?_ Attached components provide extra infrastructure that your application needs to perform its runtime
functions. The service instance might be using component outputs to detect and use resources of this infrastructure. Deleting the component, thereby
removing its infrastructure resources, could be disruptive to the attached service instance.

As an added safety measure, AWS Proton requires that you update the component and detach it from its service instance before you can delete it. You can
then validate your service instance to ensure that it continues to deploy and function properly. If you detect an issue, you can quickly reattach the
component to the service instance, then work to fix the issue. When you're confident that your service instance is clear of any dependency on the
component, you can safely delete the component.

Why can't I change a component's attached service instance directly?

_Solution:_ To change attachment, update the component to detach it from the service instance, validate component and service
instance stability, then attach the component to the new service instance.

_Why is this required?_ A component is designed to be attached to a service instance. Your component might use service instance
inputs for infrastructure resource naming and configuration. Changing the attached service instance could be disruptive to the component (in addition to
possible disruption to the service instance, as described in the previous FAQ, [Why can't I delete my attached
components?](#ag-components.faq.delete "#ag-components.faq.delete")). For example, it might cause renaming, and possibly even replacement, of resources defined in the component's IaC template.

As an added safety measure, AWS Proton requires that you update the component and detach it from its service instance before you can attach it to another
service instance. You can then validate the stability of both the component and the service instance before attaching the component to the new service
instance.
