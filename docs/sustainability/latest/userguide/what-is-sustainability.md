# What is AWS Sustainability?

Welcome to the AWS Sustainability user guide.

The AWS Sustainability service provides a suite of features to help you understand your environmental impact from using AWS services. The vast majority of accounts with AWS usage can see their environmental impact. If data isn't available for your account, your account may be too new to show data (data is published the month after the usage occurs) or your impact may be immaterial (under 0.5 grams of carbon dioxide equivalent or .5 milliliters of water withdrawn).

###### Topics

- [Features of AWS Sustainability](#sustainability-features "#sustainability-features")
- [Calculation methodology](#calculation-methodology-overview "#calculation-methodology-overview")
- [Related services](#related-services "#related-services")
- [Key concepts](key-concepts.md "key-concepts.md")
- [Resources](resources.md "resources.md")

## Features of AWS Sustainability

The AWS Sustainability service includes the following features:

- **Carbon emissions** — Visualize your carbon emissions over time. Deep dive into your emissions by scope, AWS Region, service, and more.
- **Water allocation** — Visualize your water allocation over time. Deep dive into your water withdrawals by AWS Region, service, and more.
- **Reports** — Access your sustainability data in bulk. Create .csv reports to quickly see your data, integrate with the AWS Sustainability API, or create an ongoing data export (in [Data Exports](../../../cur/latest/userguide.md "../../../cur/latest/userguide.md")).
- **Release notes** — Learn about new features, methodology updates, bug fixes, and more.

## Calculation methodology

The calculation methodology behind all the figures shown in the AWS Sustainability service is explained in the [Calculation methodology](methodology.md "methodology.md") section of this user guide.

## Related services

AWS Organizations

If you're signed in as a management account of AWS Organizations, the AWS Sustainability service will report the consolidated environmental impact of all the member accounts within that management account, for the duration that those member accounts were a part of your organization.

If you're signed in as a member account, the AWS Sustainability service will report emission data for the member account only.

For more information, see the [AWS Organizations User Guide](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md").

Data Exports

AWS Data Exports enables you to create billing and cost management data exports and carbon emissions data exports using basic SQL, and visualize data by integrating with Amazon QuickSight.

For more information, see [What is AWS Data Exports?](../../../cur/latest/userguide/what-is-data-exports.md "../../../cur/latest/userguide/what-is-data-exports.md")
