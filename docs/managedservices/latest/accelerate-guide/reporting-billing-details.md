# Billing Charges Details report

AWS Managed Services (AMS) Billing Charges Details report provides details about AMS billing charges with linked accounts and respective AWS services, including:

- AMS service-level charges, uplift percentages, account-level AMS service tiers and AMS fees.
- Linked accounts and AWS usage charges

| **Field Name**                   | **Definition**                                                                                                |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Billing Month                    | The month and year of the service billed                                                                      |
| Payer Account ID                 | The 12 digit ID identifying the account that will be responsible for paying the AMS charges                   |
| Linked Account ID                | The 12 digit ID identifying the AMS account that<br>consumes services that generates expenses                 |
| AWS Service Name                 | The AWS service that was used                                                                                 |
| AWS Charges                      | The AWS charges for the AWS service name listed in AWS Service Name                                           |
| Pricing Plan                     | The name of the pricing plan associated with the linked account                                               |
| Uplift Proportion                | The uplift percentage (as a decimal V.WXYZ) based on pricing_plan, SLA, and AWS service                       |
| Adjusted AWS Charges             | AWS usage adjusted for AMS                                                                                    |
| Uplifted AWS Charges             | The percentage of AWS charges to be charged for AMS; adjusted_aws_charges \<br>• uplift_percent               |
| Instances EC2 RDS Spend          | Spend on EC2 and RDS instances                                                                                |
| AMS Charges                      | Total AMS charges for the product; uplifted_aws_charges + instance_ec2_rds_spend + uplifted_ris + uplifted_sp |
| Prorated Minimum Fee             | The amount we charge to meet the contractual minimum                                                          |
| Minimum Fee                      | AMS Minimum Fees (if applicable)                                                                              |
| Linked Account Total AMS Charges | Sum of all charges for the linked_account                                                                     |
| Payer Account Total AMS Charges  | Sum of all charges for payer account                                                                          |
