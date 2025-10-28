# Working with audit frameworks

A _framework_ is a collection of controls that helps you to evaluate
your backup practices. You can use pre-built, customizable controls to define your policies
and evaluate whether your backup practices comply with your policies. You can also set up
automatic daily reports to gain insights into the compliance status of your frameworks.

Each framework applies to a single account and AWS Region. You can deploy a maximum of
15 frameworks per account per Region. You cannot deploy duplicate frameworks (frameworks that
contain the same controls and parameters).

There are two different types of frameworks:

- The **AWS Backup framework** (recommended) – Use the
  AWS Backup framework to deploy all available controls to monitor your backup activity,
  coverage, and resources against the best practices that we recommend.
- A **custom framework** that you define – Use a
  custom framework to choose one or more specific controls and to customize control
  parameters.

###### Topics

- [Choosing your controls](choosing-controls.md "choosing-controls.md")
- [Turning on resource tracking](turning-on-resource-tracking.md "turning-on-resource-tracking.md")
- [Creating frameworks using the AWS Backup
  console](creating-frameworks-console.md "creating-frameworks-console.md")
- [Creating frameworks using the AWS Backup API](creating-frameworks-api.md "creating-frameworks-api.md")
- [Viewing framework compliance status](viewing-frameworks.md "viewing-frameworks.md")
- [Finding non-compliant resources](finding-non-compliant-resources.md "finding-non-compliant-resources.md")
- [Updating audit frameworks](updating-frameworks.md "updating-frameworks.md")
- [Deleting audit frameworks](deleting-frameworks.md "deleting-frameworks.md")
