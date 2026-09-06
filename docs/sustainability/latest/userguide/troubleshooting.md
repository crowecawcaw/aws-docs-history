

# Troubleshooting
<a name="troubleshooting"></a>

The following topics provide troubleshooting advice for errors and issues that you could encounter when using the AWS Sustainability service. If you find an issue that isn't listed here, you can use the feedback button on this page to report it.

For more troubleshooting advice and answers to common support questions, visit the [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/).

## Why do I get an Access Denied error when I access the console?
<a name="troubleshooting-access-denied"></a>

You need to set up IAM permissions to see data in the AWS Sustainability service. See [Prerequisites](setting-up.md) to learn how.

## Why are all the numbers zero in the AWS Sustainability console?
<a name="troubleshooting-numbers-zero"></a>

 In order to see data in the AWS Sustainability console, you need to have usage of AWS services, otherwise your environmental impact will be zero. For carbon, the console shows data at the 0.000001 metric tons of carbon dioxide equivalent (MTCO2e), or 1 gram, resolution. For water, the console shows data at the 0.000001 m3, or 1 milliliter, resolution. If you have AWS usage but the console shows zero, it means your impact is lower than 0.5 grams of CO2e for carbon or 0.5 milliliters for water. 

## Why can't I see data for 2021?
<a name="troubleshooting-data-2021"></a>

You can see your carbon data back to January 2022 and your water data back to January 2023, or whenever your usage started, whichever happened later.

## Why did my data change?
<a name="troubleshooting-data-change"></a>

The calculation methodology is updated over time based on evolving data, climate science, and more. We will also update your data to fix any bugs we identify. All updates are documented in the **Release notes** page in the AWS Sustainability console.

## What's the difference between LBM and MBM?
<a name="troubleshooting-lbm-mbm"></a>

LBM and MBM are GHG Protocol methods used in Scope 2 and Scope 3 fuel- and energy- related activities (FERA) carbon emissions. Location-based emissions (LBM) reflect the average emissions intensity of the grid where energy consumption occurs. Market-based emissions (MBM) reflect supplier-specific emissions intensity after account for Energy Attribute Certificates (EACs), such as AWS' carbon-free energy purchases.

## Why is carbon intensity different depending on the AWS Region?
<a name="troubleshooting-carbon-intensity"></a>

Electricity grids in different parts of the world use various sources of power. Some use carbon-intense fuels (for example, coal), and some are primarily low-carbon hydro or other renewables. The locations of Amazon's carbon-free energy projects also play a role, because the energy produced by these projects is accounted against our emissions from Regions on the same grid. As a result, not all AWS Regions have the same carbon intensity.

## Why can’t I see data from older methodology versions?
<a name="troubleshooting-methodology"></a>

We publish data using the latest methodology version to ensure your estimated emissions are as accurate as possible. If you create a carbon emissions export on [Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html), you will be able to preserve historical data calculated with all methodology versions from that point on. Data Exports publishes your data into an S3 bucket, with each methodology version having its own prefix. When a new version is released, historical data calculated using previous versions will remain in your bucket unless you delete it. Water data is not available in Data Exports at this time. 

**Note**  
 We do not maintain previous methodology versions. To access your data from historical versions, you must create a Data Export *before* a new version is released. If this is important to you, create a data export *now*. 

## Why can't I see water data for 2022?
<a name="troubleshooting-water-data-2022"></a>

 We provide water withdrawals data beginning in 2023, reflecting the point at which we established a standardized reporting baseline that meets our bar for consistent, customer-facing insights. That baseline ensures customers have a dependable foundation for year-over-year reporting. 

## Why don't I see monthly water data?
<a name="troubleshooting-monthly-water"></a>

Water withdrawals data is available on an annual basis at this time.

## Why can't I configure fiscal year for water data?
<a name="troubleshooting-fiscal-year-water"></a>

Water withdrawals data is available on an annual basis at this time. Without monthly granularity, we can't group your withdrawals by fiscal year.