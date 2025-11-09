# Billing report (monthly)

## Billing charges details

This report provides details about AMS billing charges with linked accounts and respective AWS services.

**This report provides:**

- Data on AMS service-level charges, uplift percentages, account-level AMS service tiers and AMS fees.
- Data on linked accounts and AWS usage charges.

###### Important

The Monthly Billing report is only available in your Management Payer Account (MPA) or your defined Charge Account. These are the accounts where your AMS monthly bill is sent. If you're unable to locate these accounts, then contact your Cloud Service Delivery Manager (CSDM) for assistance.

| **Field Name**                              | **Dataset Field Name**              | **Definition**                                                                                                |
| ------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Billing Date                                | date                                | The month and year of the service billed                                                                      |
| Payer Account Id                            | payer_account_id                    | The 12 digit ID identifying the account responsible for paying the AMS charges                                |
| Linked Account Id                           | linked_account_id                   | The 12 digit ID identifying the AMS account that consumes services that generates expanses                    |
| AWS Service Name                            | product_name                        | The AWS service that was used                                                                                 |
| AWS Charges                                 | aws_charges                         | The AWS charges for the AWS service name in AWS Service Name                                                  |
| Pricing Plan                                | pricing_plan                        | The pricing plan associated with the linked account                                                           |
| AMS Service Group                           | tier_uplifting_groups               | AMS service group code that determines uplift percentage                                                      |
| Uplift Proportion                           | uplift_percent                      | The uplift percentage (as a decimal V.WXYZ) based on pricing_plan, SLA, and AWS service                       |
| Adjusted AWS Charges                        | adjusted_aws_usage                  | AWS usage adjusted for AMS                                                                                    |
| Uplifted AWS Charges                        | uplifted_aws_charges                | The percentage of AWS charges to be charged for AMS; adjusted_aws_charges \<br>• uplift_percent               |
| Instances EC2 RDS Spend                     | instances_ec2_rds_spend             | Spend on EC2 and RDS instances                                                                                |
| Reserved Instance Charges                   | ris_charges                         | Reserved instance charges                                                                                     |
| Uplifted Reserved Instance Charges          | uplifted_ris                        | The percentage of reserved instance charges to becharged for AMS; ris_charges \<br>• uplift_percent           |
| Savings Plan Charges                        | sp_charges                          | SavingsPlan usage charges                                                                                     |
| Uplifted Savings Plan Charges               | uplifted_sp                         | The percentage of savings plans charges to be chargedfor AMS; sp_charges \<br>• uplift_percent                |
| AMS Charges                                 | ams_charges                         | Total ams charges for the product; uplifted_aws_charges + instance_ec2_rds_spend + uplifted_ris + uplifted_sp |
| Prorated Minimum Fee                        | prorated_minimum                    | The amount we charge to meet the contractual minimum                                                          |
| Linked Account Total AMS Charges            | linked_account_total<br>ams_charges | Sum of all charges for the linked_account                                                                     |
| Payer Account Total AMS Charges             | payer_account_total<br>ams_charges  | Sum of all charges for payer account                                                                          |
| Minimum Fee                                 | minimum_fees                        | AMS Minimum Fees (if applicable)                                                                              |
| Reserved Instance and Savings Plan discount | adj_ri_sp_charges                   | RI/SP discount to be applied against RI/SP charges (applicable under certain circumstances)                   |
