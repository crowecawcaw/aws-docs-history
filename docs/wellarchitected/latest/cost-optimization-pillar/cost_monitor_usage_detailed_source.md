# COST03-BP01 Configure detailed information sources

Set up cost management and reporting tools for enhanced analysis and transparency of cost and usage data. Configure your workload to create log entries that facilitate the tracking and segregation of costs and usage.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Detailed billing information such as hourly granularity in cost management tools allow organizations to track their consumptions with further details and help them to identify some of the cost increase reasons. These data sources provide the most accurate view of cost and usage across your entire organization.

You can use AWS Data Exports to create exports of the AWS Cost and Usage Report (CUR) 2.0. This is the new and recommended way to receive your detailed cost and usage data from AWS. It provides daily or hourly usage granularity, rates, costs, and usage attributes for all chargeable AWS services (the same information as CUR), along with some improvements. All possible dimensions are in the CUR such as tagging, location, resource attributes, and account IDs.

There are three export types based on the type of export you want to create: a standard data export, an export to a cost and usage dashboard with Quick Suite integration, or a legacy data export.

- **Standard data export:** A customized export of a table that delivers to Amazon S3 on a recurring basis.
- **Cost and usage dashboard:** An export and integration to Quick Suite to deploy a pre-built cost and usage dashboard.
- **Legacy data export:** An export of the legacy AWS Cost and Usage Report (CUR).

You can create data exports with the following customizations:

- Include resource IDs
- Split cost allocation data
- Hourly granularity
- Versioning
- Compression type and file format

For your workloads that run containers on Amazon ECS or Amazon EKS, enable split cost allocation data so that you can allocate your container costs to individual business units and teams, based on how your container workloads consume shared compute and memory resources. Split cost allocation data introduces cost and usage data for new container-level resources to AWS Cost and Usage Report. Split cost allocation data is calculated by computing the cost of individual ECS services and tasks running on the cluster.

A cost and usage dashboard exports the cost and usage dashboard table to an S3 bucket on a recurring basis and deploys a prebuilt cost and usage dashboard to Quick Suite. Use this option if you want to quickly deploy a dashboard of your cost and usage data without the ability for customization.

If desired, you can still export CUR in legacy mode, where you can integrate other processing services such as [AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/") to prepare the data for analysis and perform data analysis with [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/") using SQL to query the data.

### Implementation steps

- **Create data exports:** Create customized exports with the data you want and control the schema of your exports. Create billing and cost management data exports using basic SQL, and visualize your billing and cost management data by integrating with Quick Suite. You can also export your data in standard mode to analyze your data with other processing tools like Amazon Athena.
- **Configure the cost and usage
  report:** Using the billing console, configure at
  least one cost and usage report. Configure a report with
  hourly granularity that includes all identifiers and
  resource IDs. You can also create other reports with
  different granularities to provide higher-level summary
  information.
- **Configure hourly granularity in Cost Explorer:** To access cost and usage data with hourly granularity for the past 14 days, consider enabling hourly and resource level data in the billing console.
- **Configure application
  logging:** Verify that your application logs each
  business outcome that it delivers so it can be tracked and
  measured. Ensure that the granularity of this data is at
  least hourly so it matches with the cost and usage data. For
  more details on logging and monitoring,
  see [Well-Architected
  Operational Excellence Pillar](../operational-excellence-pillar/welcome.md "../operational-excellence-pillar/welcome.md").

## Resources

**Related documents:**

- [AWS Data Exports](../../../cur/latest/userguide/what-is-data-exports.md "../../../cur/latest/userguide/what-is-data-exports.md")
- [AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/")
- [Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/")
- [AWS Cost Management Pricing](https://aws.amazon.com/aws-cost-management/pricing/ "https://aws.amazon.com/aws-cost-management/pricing/")
- [Tagging
  AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md")
- [Analyzing
  your costs with Cost Explorer](../../../awsaccountbilling/latest/aboutv2/cost-explorer-what-is.md "../../../awsaccountbilling/latest/aboutv2/cost-explorer-what-is.md")
- [Managing
  AWS Cost and Usage Reports](../../../awsaccountbilling/latest/aboutv2/billing-reports-costusage-managing.md "../../../awsaccountbilling/latest/aboutv2/billing-reports-costusage-managing.md")

**Related examples:**

- [AWS Account Setup](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_1_AWS_Account_Setup/README.html "https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_1_AWS_Account_Setup/README.html")
- [Data Exports for AWS Billing and Cost Management](https://aws.amazon.com/blogs/aws-cloud-financial-management/introducing-data-exports-for-billing-and-cost-management/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/introducing-data-exports-for-billing-and-cost-management/")
- [AWS Cost Explorer Common Use Cases](https://aws.amazon.com/blogs/aws-cloud-financial-management/aws-cost-explorers-new-ui-and-common-use-cases/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/aws-cost-explorers-new-ui-and-common-use-cases/")
