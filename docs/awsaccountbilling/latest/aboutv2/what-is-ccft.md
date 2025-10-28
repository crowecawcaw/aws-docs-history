# Viewing your carbon footprint

You can use the Customer Carbon Footprint Tool (CCFT) to view estimates of the carbon emissions associated with your AWS products and services.

###### Topics

- [Getting started with the Customer Carbon Footprint Tool (CCFT)](#ccft-gettingstarted "#ccft-gettingstarted")
- [Understanding the Customer Carbon Footprint Tool (CCFT)](ccft-overview.md "ccft-overview.md")
- [Calculating your energy usage](ccft-energy.md "ccft-energy.md")
- [Understanding your carbon emission estimations](ccft-estimation.md "ccft-estimation.md")

## Getting started with the Customer Carbon Footprint Tool (CCFT)

The Customer Carbon Footprint Tool is available for all accounts. Your data is updated monthly with a delay of three months while AWS processes the data required to calculate your carbon emission estimates.

###### Note

If a report isn't available for your account, your account might be too new to show data, or
your carbon footprint is under 0.5 kgCO2e in the reporting month. For more
information, see [Understanding the Customer Carbon Footprint Tool (CCFT)](ccft-overview.md "ccft-overview.md").

###### To use the Customer Carbon Footprint Tool

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the navigation pane, choose **Customer Carbon Footprint Tool** under
   **Cost and Usage Analysis**.
3. Under **Customer Carbon Footprint Tool**, choose your **Start
   month** and **End month**.

### IAM policies

You must have the IAM permission `sustainability:GetCarbonFootprintSummary` to access the Customer Carbon Footprint Tool and data. For more information regarding IAM permissions, see [Identity and Access Management for AWS Billing](security-iam.md "security-iam.md").

### AWS Organizations users

If you're signed in as a management account of AWS Organizations, the Customer Carbon Footprint Tool dashboard and
spreadsheet download report the consolidated member account data for the duration
that those member accounts were a part of your organization.

If you're a member account, the Customer Carbon Footprint Tool reports emission data for all the periods.
This is regardless of any changes that might have occurred to your account's
associated membership in an organization.
