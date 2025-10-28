# AWS Service Management Connector for ServiceNow prerequisites

Make sure you have AWS and ServiceNow prerequisites configured before you get started.

- **AWS Service Catalog with the Connector** — You must have an AWS account to configure your AWS portfolios and
  products. For details, refer to [Setting up for
  Service Catalog](../../../servicecatalog/latest/adminguide/setup.md "../../../servicecatalog/latest/adminguide/setup.md") and [Using
  AppRegistry.](../../../servicecatalog/latest/arguide/intro-app-registry.md "../../../servicecatalog/latest/arguide/intro-app-registry.md")
- **AWS Config details** — Configure the service settings to record data for the resource types of
  interest. We recommend you include provisioned products and AWS CloudFormation stacks, in
  addition to the major resource types that your team uses. For more
  information, see [Setting up AWS Config with
  the console](../../../config/latest/developerguide/gs-console.md "../../../config/latest/developerguide/gs-console.md"). This version of the Connector enables the import of
  aggregated Config data in a single AWS account from more than
  one AWS Region or account. To use this feature, you must
  configure an aggregator in AWS. For more information, see
  [Setting up an aggregator using the console](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md").
- **AWS Systems Manager Automation with the
  Connector** — This feature requires no AWS-side set up. As standard,
  AWS provides a number of automation documents (runbooks).
  If you want additional automation documents (runbook), retrieve them in the
  Connector. For more information, see [Working
  with Automation Runbooks](../../../systems-manager/latest/userguide/automation-documents.md "../../../systems-manager/latest/userguide/automation-documents.md").
- **AWS Systems Manager OpsCenter with the Connector** — You must enable the service in all Regions and accounts where you want to
  sync OpsItems. For more information, see [Getting started with OpsCenter](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md")
- **AWS Security Hub with the Connector** — You must enable the service in all Regions and accounts where you want to
  sync Findings. For details, see [Setting up Security Hub](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md"). We recommend you connect ServiceNow
  with the primary (main) AWS account for AWS Security Hub. For
  more information, see [Managing administrator and member accounts](../../../securityhub/latest/userguide/securityhub-accounts.md "../../../securityhub/latest/userguide/securityhub-accounts.md").
- **Support with the Connector** — Your account must have a [Business](https://aws.amazon.com/premiumsupport/plans/business/ "https://aws.amazon.com/premiumsupport/plans/business/") or [Enterprise](https://aws.amazon.com/premiumsupport/plans/enterprise/ "https://aws.amazon.com/premiumsupport/plans/enterprise/") Support plan to use support integration with the
  Connector.
- **AWS Systems Manager Change Manager with the Connector** — You must enable the service in all Regions and accounts where you want to
  sync change templates. The AWS Systems Manager Change Manager integration of
  AWS Service Management Connector introduces a curated version of the
  integration. It allows customers to execute pre-approved change templates
  that contain at least one Automation Runbook and does not require approvals
  during execution from ServiceNow. For more information, see [Setting up Change
  Manager.](../../../systems-manager/latest/userguide/change-manager-setting-up.md "../../../systems-manager/latest/userguide/change-manager-setting-up.md")
- **AWS Systems Manager Incident Manager with the Connector** — You must enable Incident Manager in all AWS Regions and accounts from where
  you want to sync the incidents. For details, see [Setting up for AWS Systems Manager Incident Manager.](../../../incident-manager/latest/userguide/setting-up.md "../../../incident-manager/latest/userguide/setting-up.md")
- **AWS Health with the Connector** — Your account must have a [Business](https://aws.amazon.com/premiumsupport/plans/business/ "https://aws.amazon.com/premiumsupport/plans/business/")
  or [Enterprise](https://aws.amazon.com/premiumsupport/plans/enterprise/ "https://aws.amazon.com/premiumsupport/plans/enterprise/") Support plan to use AWS Health integration with the
  Connector.
- **ServiceNow instance** — You need a ServiceNow instance to
  install the ServiceNow Connector scoped application. The initial installation should
  occur in either an enterprise sandbox or a [ServiceNow Personal Developer Instance](https://developer.servicenow.com/app.do#!/document/content/app_store_doc_getting_started_newyork_topic_lyf_bf2_3r?v=newyork "https://developer.servicenow.com/app.do#!/document/content/app_store_doc_getting_started_newyork_topic_lyf_bf2_3r?v=newyork") (PDI), depending on your
  organization’s technology governance requirements. The ServiceNow administrator needs the admin role to install the Connector for
  ServiceNow scoped application.
