# Amazon DataZone custom AWS service blueprints

In Amazon DataZone, custom AWS service blueprints enable you optimize resource usage and
costs by configuring Amazon DataZone to use your own existing AWS Identity and Access
Management (IAM) roles and AWS services that you already have set up in your organization.

A blueprint with which a Amazon DataZone environment is created defines what tools and services
members of the project to which the environment belongs can use as they work with assets in
the Amazon DataZone catalog. In the current release of Amazon DataZone, there are the following
built-in blueprints:

- Data lake blueprint
- Data warehouse blueprint
- Amazon SageMaker blueprint
  With Amazon DataZone custom AWS service blueprints, you can create environments and projects
  that are customized to any AWS services that you are currently using in your organization.
  With custom blueprints, you can include Amazon DataZone in your existing data pipelines by
  configuring it to use your existing IAM roles to enhance governance across infrastructure
  setup and collaborate on business initiatives.

###### Important

With Amazon DataZone custom AWS service prints, you can migrate your existing Amazon
SageMaker domain into Amazon DataZone. With this capability, administrators can now set
up Amazon DataZone projects by importing their existing authorized users, security
configurations, and policies from Amazon SageMaker domains. For more information, see
[Set up SageMaker Assets (administrator guide)](../../../sagemaker/latest/dg/sm-assets-set-up.md "../../../sagemaker/latest/dg/sm-assets-set-up.md").

###### Topics

- [Enable a custom AWS service
  blueprint](enable-custom-blueprint.md "enable-custom-blueprint.md")
- [Create an environment using a custom AWS
  service blueprint](create-custom-environment.md "create-custom-environment.md")
- [Create actions in a custom AWS
  service environment](configure-custom-environment-actions.md "configure-custom-environment-actions.md")
- [Add project members to a
  custom AWS service environment](add-project-members-to-custom-environment.md "add-project-members-to-custom-environment.md")
- [Configure a data source in
  an AWS service environment](configure-data-source-in-custom-environment.md "configure-data-source-in-custom-environment.md")
- [Configure a
  subscription target in an AWS service environment](configure-subscription-target-in-custom-environment.md "configure-subscription-target-in-custom-environment.md")
