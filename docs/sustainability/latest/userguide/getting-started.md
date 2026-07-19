# Getting started with AWS Sustainability

This section provides information that you need to get started with using the AWS Sustainability console. Make sure you've met the [prerequisites](setting-up.md "setting-up.md") before you start. You can also customize your AWS Sustainability preferences.

###### Topics

- [Step 1: Review your environmental impact](#getting-started-step1 "#getting-started-step1")
- [Step 2: Programmatically access your sustainability data](#getting-started-step2 "#getting-started-step2")
- [Step 3: (Optional) Configure your fiscal year](#getting-started-step3 "#getting-started-step3")
- [Next steps](#getting-started-next-steps "#getting-started-next-steps")

## Step 1: Review your environmental impact

Use features in the AWS Sustainability console to view your estimated environmental impact.
The AWS Sustainability service publishes carbon emissions data monthly for the previous usage month (for example, data for October usage is published in November).
Carbon emissions data is published by the 21st day of the month.
Water withdrawals data is published annually for the previous usage year (for example, data for 2025 is published in Q2 of 2026).

###### To open the AWS Sustainability console and view your environmental impact

1. Sign into the AWS Management Console and open the AWS Sustainability console at [https://console.aws.amazon.com/sustainability/](https://console.aws.amazon.com/sustainability/ "https://console.aws.amazon.com/sustainability/").
2. Choose **Carbon emissions** to see details about your estimated carbon emissions from using AWS.
3. Choose **Water allocation** to see details about your estimated water withdrawals from using AWS.
4. Choose **Reports** to download csv reports with your environmental impact.
5. Choose **Release notes** to see the history of feature releases, bug fixes, methodology updates, and more.

For more information about the calculation methodology behind the numbers shown in the AWS Sustainability service, see [Calculation methodology](methodology.md "methodology.md").

## Step 2: Programmatically access your sustainability data

In addition to using the dashboards in the AWS Sustainability console to see your environmental impact, you have two ways to get your sustainability data programmatically. We recommend you use one of these options if you want to see your data with the maximum granularity available. For example, if you need data broken out by month, usage account, and AWS Region, for several years, getting your data programmatically is the best solution.

1. Call the AWS Sustainability API. See the [AWS Sustainability API Reference](../APIReference.md "../APIReference.md") to learn how.
2. Create a data export to send your monthly data to the S3 bucket of your choice. See [Get your data in bulk](bulk-data.md "bulk-data.md") to learn how.

## Step 3: (Optional) Configure your fiscal year

By default, the AWS Sustainability service shows yearly visualizations using the calendar year (January to December).
You can configure a different fiscal year to use for carbon emissions data in the **Settings** page within the console if you want to see your carbon emissions data aggregated differently (for example, you can set up your fiscal year to be March to February).

## Next steps

Learn more about AWS Sustainability:

- Key concepts: [Key concepts](key-concepts.md "key-concepts.md")
- Use the console visualizations: [Use the console visualizations](console-visualizations.md "console-visualizations.md")
- Reports: [Get your data in bulk](bulk-data.md "bulk-data.md")
- Calculation methodology: [Calculation methodology](methodology.md "methodology.md")
- Calculate your energy usage: [Calculate your energy usage](energy-calculation.md "energy-calculation.md")
