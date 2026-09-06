

# Performing ad hoc analysis on pro forma costs in AWS Cost Explorer
<a name="ad-hoc-cost-explorer-analysis"></a>

## Using Billing Conductor as a standalone service
<a name="ad-hoc-cost-explorer-analysis-standalone"></a>

AWS accounts in Billing Conductor billing groups can analyze, forecast, and report pro forma costs in Cost Explorer. The primary account in a billing group can perform these activities for all accounts within the group. If you're using AWS Organizations, management accounts can't analyze, forecast, or report pro forma costs in Cost Explorer. 

Billing group managed accounts (billing group members) can see cost and usage data for the billing periods they were members of the billing group, and pro forma data is available. They cannot see historical billable cost and usage data. If you need historical data, the payer account can request a backfill by contacting [Support Center](http://aws.amazon.com/support). The data is presented in a pro forma format, aligned with the billing group settings.

**Notes**  
Billing Conductor managed accounts (billing group members) can see pro forma costs in Cost Explorer.
To learn more about core workflows that Cost Explorer supports, see [Exploring your data using Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-exploring-data.html) in the *AWS Cost Management User Guide*.

## Using Billing Conductor with billing transfer
<a name="ad-hoc-cost-explorer-analysis-tandem"></a>

An AWS Organizations in a billing transfer billing group can analyze, forecast, and report pro forma costs in Cost Explorer. By default, their cost data in the primary view shows only pro forma data.

For a list of AWS services that support pro forma costs, see [AWS services that support pro forma-based billing view costs](service-integrations-support-proforma.md).