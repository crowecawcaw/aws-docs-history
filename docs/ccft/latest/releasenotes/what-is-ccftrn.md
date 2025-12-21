# Customer Carbon Footprint Tool Release Notes

The Customer Carbon Footprint Tool (CCFT) release notes provide details about Customer Carbon Footprint Tool releases. This includes new features, updates, fixes related to the service, console, and calculation. When we release any updates to the Customer Carbon Footprint Tool service, release notes are published describing the content of the release.

## Additional resources

Use the following resources to learn more about the Customer Carbon Footprint Tool.

- [Customer Carbon Footprint Tool chapter](../../../awsaccountbilling/latest/aboutv2/what-is-ccft.md "../../../awsaccountbilling/latest/aboutv2/what-is-ccft.md") in the _AWS Billing User Guide_ - Concepts, tool guidance, set up, and estimation reference materials.
- [Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/ "https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/") - Marketing overview of the Customer Carbon Footprint Tool.
- [AWS Sustainability](https://sustainability.aboutamazon.com/products-services/aws-cloud "https://sustainability.aboutamazon.com/products-services/aws-cloud") - AWS initiatives, goals, and progress in addressing environmental issues and promoting sustainable practices across its global operations.

## Release notes

###### Topics

- [Customer Carbon Footprint Tool release notes for 2025](#ccft-releasecotes-2025 "#ccft-releasecotes-2025")
- [Customer Carbon Footprint Tool release notes for 2023](#ccft-releasecotes-2023 "#ccft-releasecotes-2023")
- [Customer Carbon Footprint Tool release notes for 2022](#ccft-releasecotes-2022 "#ccft-releasecotes-2022")

### Customer Carbon Footprint Tool release notes for 2025

This section documents the updates made to Customer Carbon Footprint Tool. This page lists announcements about new or updated features, bug fixes, improvements, and deprecated functionality for the year 2025.

#### December 15, 2025

##### Customer Carbon Footprint Tool data lag reduced by 2 months

The Customer Carbon Footprint Tool and AWS Data Exports now publish carbon emission estimates between the 15 and 21st of the month following the usage (e.g. December data is published by January 21st). To support the faster data delivery, we’re using more estimates to calculate Scope 2 and Scope 3.3 (Fuel- and Energy- Related Activities, FERA). These categories rely on utility invoices that aren’t received until later in the month. Starting in 2026, AWS will recalculate previous year’s emissions using the actual data from utility invoices by June of the following year, and we will also take this opportunity to update any other data sources that have a more recent version. For example, 2025 data will be republished by June 2026 using the latest and greatest inputs.

#### October 22, 2025

##### Added scope 3 emissions category

We've added new emissions categories to the Customer Carbon Footprint Tool and Data Exports, including Scope 3.2
(IT Hardware, Buildings, Equipment), Scope 3.3 (Fuel- and Energy- Related Activities, FERA), and
Scope 3.4 (Upstream Transportation and Distribution). We've also added Scope 1 refrigerants and
natural gas. These new emissions categories have been backfilled back to January 2022.

###### Note

To see your historical data leading up to January 2022, you must create a new Data
Export.

Data Exports now includes new columns that break down emissions by Scope (1, 2, 3).

##### Updated methodology to version 3.0.0

We've released a new methodology that incorporates new emissions categories (select Scope
3, Scope 1 refrigerants, and natural gas categories), and improves carbon allocation for
non-foundational services for internal teams by moving to cost allocation from the previous
proxy logic. Historical emissions are recalculated back to January 2022 using this latest
version. As part of this update, the carbon estimates will use the latest available snapshots
from data sources. This includes using assured carbon datasets from 2022, 2023, and 2024 to
recalculate each year's data.

You can find detailed information about the updated methodology in our [methodology document](https://sustainability.aboutamazon.com/aws-customer-carbon-footprint-tool-methodology.pdf "https://sustainability.aboutamazon.com/aws-customer-carbon-footprint-tool-methodology.pdf"). The methodology has been [third-party assured](https://sustainability.aboutamazon.com/aws-customer-carbon-footprint-tool-methodology-assurance.pdf "https://sustainability.aboutamazon.com/aws-customer-carbon-footprint-tool-methodology-assurance.pdf").

#### August 15, 2025

##### Updates to market-based emissions calculations in multiple

AWS Regions

Customers with usage in Canada West (Calgary), Canada (Central), US West (N. California), Asia Pacific (Jakarta), and edge locations in North America will see a decrease in their market-based emissions in their May 2025 data. Customers with usage in Asia Pacific (Osaka) and Asia Pacific (Tokyo) will see an increase in their market-based emissions in their May 2025 data.

These changes reflect Amazon's continued commitment to expand our use of carbon-free energy and progress toward meeting net-zero carbon by 2040 while also continuing to wind down our use of unbundled renewable energy credits (uRECs). These adjustments affect emissions calculations starting January 2025. We will implement these updates on historical data by Q1 2026 to ensure consistent reporting.

#### July 23, 2025

##### Energy consumption calculation page is now available

Added a new page that explains how to calculate the estimated energy consumption of your AWS cloud carbon footprint using CCFT. For more information, see [Calculating your energy usage](../../../awsaccountbilling/latest/aboutv2/ccft-energy.md "../../../awsaccountbilling/latest/aboutv2/ccft-energy.md").

#### July 17, 2025

##### Emissions data correction for Frankfurt and Paris regions

Customers with usage in Europe (Frankfurt) and Europe (Paris) will see a one-time decrease in location-based emissions in the April 2025 data. The unique structure of these two regions required new logic to correct over-estimation by ~29% (Frankfurt) and ~6% (Paris). This over-estimation affected Customer Carbon Footprint Tool and Data Exports data displayed for these locations between January 2024 and March 2025.

#### June 24, 2025

##### Location-based method (LBM) emission calculation is

launched

The Customer Carbon Footprint Tool and AWS Data Exports now include emissions calculated using the location-based method (LBM), in addition to the existing market-based method (MBM) calculations. LBM calculates emissions based on the average carbon intensity of electricity grids where energy consumption occurs. Electricity grids worldwide vary in their power sources. Some rely more heavily on carbon-intensive fuels like coal, while others use a higher percentage of low-carbon sources such as hydro or other renewables. To learn more about LBM, see the [GHG Protocol Scope 2 Guidance](https://ghgprotocol.org/sites/default/files/2023-03/Scope%202%20Guidance.pdf "https://ghgprotocol.org/sites/default/files/2023-03/Scope%202%20Guidance.pdf").

###### Note

If you have an existing data export, you will need to update to include the newly released columns. Previously exported data remains unchanged and does not include location-based method (LBM) calculations. To add LBM data to your historical records, create a new export including the LBM columns. For more information, see [Editing export details](../../../cur/latest/userguide/dataexports-edit-export-details.md "../../../cur/latest/userguide/dataexports-edit-export-details.md") in the _AWS Data Exports User Guide_.

##### Data granularity for Amazon CloudFront emissions is now available

The CCFT now displays Amazon CloudFront emissions separately in the service breakdown, located in the CCFT console, CSV download, and AWS Data Exports. This aligns with the existing breakdown available for Amazon EC2 and Amazon S3.

###### Note

If you have an existing data export, you will need to recreate the data to see CloudFront data for historical months. Previously exported data remains unchanged. To backfill all of your data, you must create a new export.

##### Emissions threshold updated for granularity and expanded

historical data

The CCFT now shows emissions data at a more granular level with expanded historical coverage. Previously, data was not visible if estimated emissions for the AWS account didn't exceed 0.05 MTCO2e over a 36 month period. Now, estimated emissions is visible in the CCFT console and CSV download as long as emissions for any period rounds to 1 kg (0.001 MTCO2e). CCFT console or CSV download will show `0 emissions` for the selected time period if the estimated emissions are below 0.0005 MTCO2e. With this update, the CCFT console and CSV download contains 38 months of data instead of the previous 36 months.

###### Note

Data Export continues to display emissions at gram (0.000001 MTCO2e) resolution.

##### Improvements made to service allocation logic

An issue was found in a previous CCFT allocation logic that incorrectly assigned
emissions to some AWS services (for example, CloudWatch, Amazon Redshift, and Sagemaker) as `overhead` rather than basing data on usage or
revenue. The new methodology 2.0.1
addresses this issue, starting from March 2025. This update might cause some changes to your
carbon emissions.

#### April 24, 2025

##### CCFT supports region granularity

The Customer Carbon Footprint Tool displays emissions by AWS Region, for example `Asia Pacific (Tokyo)`, `US East (Ohio)`. Emissions by AWS Regions shows your detailed carbon footprint, allowing you to see how your usage in different AWS Regions contributes to your carbon impact. You can also use this information to develop targeted reduction strategies.

##### Carbon emission estimates are available in AWS Data Exports

Carbon Data Exports for carbon emissions estimates is available through the Billing and Cost Management Data Exports. When customers use AWS Organizations, the carbon emissions data export delivers carbon emissions estimates for all the member accounts linked to management accounts. The exports are delivered regularly to a designated Amazon S3 bucket. From there, you can use the data with your business intelligence and reporting systems. This feature streamlines the consolidation and delivery of carbon emissions data from multiple AWS accounts to be used by sustainability teams and business analysts to monitor environmental impact across complex AWS environments.

Carbon Data Exports is available in all commercial AWS Regions. You can configure automated monthly exports to an Amazon S3 bucket in CSV or Parquet format. The data provides both account-level and Regional-level details. Organizations can access up to 38 months of historical data within 24 hours of setup. This enables baseline analysis and trend reporting without the need for manual data gathering. To set up your first carbon export, see [AWS Data Exports](../../../cur/latest/userguide/what-is-data-exports.md "../../../cur/latest/userguide/what-is-data-exports.md").

##### CCFT methodology updated to version 2.0

The Customer Carbon Footprint Tool is using an updated methodology with the release of your January 2025 data. This methodology is assured by Apex, a third-party consultant. To see the full third-party verification letter, see the [AWS Customer Carbon Footprint Tool methodology assurance letter](https://sustainability.aboutamazon.com/aws-customer-carbon-footprint-tool-methodology-assurance.pdf "https://sustainability.aboutamazon.com/aws-customer-carbon-footprint-tool-methodology-assurance.pdf").

Your reported estimated emissions figures might have changed as a result of this methodology update. The new method provides a more precise attribution of carbon emissions based on your actual AWS service usage. Your Customer Carbon Footprint Tool data before December 2024 will continue to use the previous methodology (version 1.0).

To learn how the Customer Carbon Footprint Tool values are calculated, see [Customer Carbon Footprint Tool (CCFT) Methodology.](https://sustainability.aboutamazon.com/aws-customer-carbon-footprint-tool-methodology.pdf "https://sustainability.aboutamazon.com/aws-customer-carbon-footprint-tool-methodology.pdf")

#### January 15, 2025

##### CCFT moved to a new dedicated console page

The Customer Carbon Footprint Tool moved to a dedicated page in the AWS Billing and Cost Management console. You can find the page under **Cost and Usage Analysis** in the navigation pane. The previous location under AWS Cost and Usage Report has been deprecated.

### Customer Carbon Footprint Tool release notes for 2023

This section documents the updates made to Customer Carbon Footprint Tool. This page lists announcements about new or updated features, bug fixes, improvements, and deprecated functionality for the year 2023.

#### April 19, 2023

##### CSV download feature enabled for improved granularity

The Customer Carbon Footprint Tool supports a CSV download option. This allows you to review detailed carbon footprint data and use the data in other reporting systems for further analysis and information sharing.

### Customer Carbon Footprint Tool release notes for 2022

This section documents the updates made to Customer Carbon Footprint Tool. This page lists announcements about new or updated features, bug fixes, improvements, and deprecated functionality for the year 2022.

#### March 01, 2022

##### AWS Customer Carbon Footprint Tool goes live

You can now use the Customer Carbon Footprint Tool to calculate the environmental impact of your AWS workload. This new tool uses intuitive data visualizations for multiple purposes. It provides your historical carbon emissions and evaluates emission trends as your AWS use evolves. The tool also approximates the estimated carbon emissions customers have avoided by using AWS instead of an on-premises data center. Finally, it reviews forecasted emissions based on current use. These emissions show how your carbon footprint changes as Amazon continues towards our goal of powering operations with 100% renewable energy by 2025. This is five years ahead of the original target of 2030, and drives towards net-zero carbon by 2040 as a part of The Climate Pledge.

You can use the Customer Carbon Footprint Tool in the AWS Billing and Cost Management console to help support your sustainability journey. After signing in, you can view your carbon emissions data by geographical location as well as by AWS services (for example, Amazon EC2 and Amazon S3). You can also measure changes to your carbon footprint over time as you deploy new resources to the cloud. Customer Carbon Footprint Tool uses data that meets the Greenhouse Gas Protocol, the international standard for greenhouse gas reporting.
