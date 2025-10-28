# Analyzing Savings Plans, reservation coverage, and utilization reports

You can analyze Savings Plans, reservation coverage, and utilization reports for AWS accounts in
Billing Conductor billing groups. Reports are generated for each billing group. The primary billing group
account can view coverage and utilization data, based on pro forma costs for all accounts in the
group. In pro forma domain, Savings Plans and reservations are shared only within billing groups, despite
preferences in the billable domain. This means that your pro forma coverage and utilization reports are computed based on your pro forma Reservations and Savings Plans sharing configuration at the billing group level, which is enabled for all accounts in the billing group by default.

Billing group managed accounts, or billing group members, can view coverage and utilization
data based on pro forma costs if there are Savings Plans purchases or reservations in that account. You
can't view historical billable coverage and utilization
data. Pro forma data can only
be backfilled up to February of 2024.

The following graphs are available for analysis:

**Savings Plans utilization graph**
This shows pro forma costs under On-Demand spend equivalent, and total net savings.

**Savings Plans coverage graph**
This shows the pro forma cost under On-Demand spend not covered, and potential monthly savings compared to On-Demand.

**Reservation utilization graph**
This shows the pro forma cost under effective reservation costs, On-Demand cost equivalent, total net savings, and total potential savings.

**Reservation coverage graph**
This shows the pro forma costs under total On-Demand costs and annual potential savings.

###### Note

- If you're using AWS Organizations, management accounts can't analyze, forecast, or report pro forma costs in Cost Explorer. This feature is only available to accounts in the billing group.
- Total commitment values are not affected by the pro forma domain.
- Pro forma utilization reports and coverage reports must not be used as a reference to make optimization decisions. For example, changes in workloads, Savings Plans, or reservations purchases. See the billable utilization reports and coverage reports for any optimization decisions.
- We recommend you discuss with the billing administrator or your organization before making reservations and Savings Plans purchases based on pro forma data. Savings Plans and reservations purchase recommendations offer accurate recommendations based on the billable sharing preferences, billable On-Demand spend, and on the performance of any existing Savings Plans and/or reservations in the billable domain. Savings Plans and reservation recommendations reflect the insights reported in the billable utilization and coverage report for primary accounts and linked accounts in billing groups. See the Savings Plans and reservation purchase recommendations page as an account within the billing group, and your recommended commitment value will accurately reflect the billable utilization and coverage report. This is the source of truth for your organization optimization decisions.

## Understanding the effects of billing group configuration and Savings Plans sharing preferences

Discount benefits are shared within the billing group within Billing Conductor. For this reason, Savings Plans coverage and utilization metrics might change based on billing group configuration or Savings Plans sharing preference in the billable domain.

###### Examples

- If Savings Plans sharing is enabled across all accounts in the organization in the billable domain and there is one single billing group that contains all accounts in the organization in the pro forma domain, then there will be no variance between the coverage and utilization metrics between the billable and pro forma domain.
- If Savings Plans sharing is enabled across all accounts in the organization in the billable domain but Billing Conductor pro forma domain is configured so there is either one billing group that contains a subset of accounts in the organization or there are multiple billing groups with subsets of accounts each, then there will be variance between the coverage and utilization metrics in pro forma domain and billable domain. The nature of the variance depends on your billing groups configuration and whether the Savings Plans reside in an account in or outside of the billing group. However, utilization metrics might be lower in the pro forma domain compared to the billable domain while the coverage might be higher in the pro forma domain compared to the billable domain.
- If Savings Plans sharing is restricted to a specific linked account in the billable domain and the billing group contains the account that purchased the Savings Plans, the utilization and coverage metrics might be higher in pro forma compared to the chargeable domain. This is because the pro forma Savings Plans sharing behavior overrides the restrictive billable sharing preference enabling more accounts (if they are in a billing group) to benefit from the Savings Plans.

For more information about Savings Plans and reservation reports, see [Monitoring your Savings Plans](../../../savingsplans/latest/userguide/sp-monitoring.md "../../../savingsplans/latest/userguide/sp-monitoring.md") in the _Savings Plans User Guide_, and [Understanding your reservations with Cost Explorer](../../../cost-management/latest/userguide/ce-ris.md "../../../cost-management/latest/userguide/ce-ris.md") in the _AWS Cost Management User Guide_.
