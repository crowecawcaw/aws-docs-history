# Savings estimation mode

The savings estimation mode preference allows Compute Optimizer to analyze specific pricing discounts
when generating the estimated cost savings of rightsizing recommendations. Compute Optimizer offers the
savings estimation mode for the following pricing discounts per AWS resource:

- Amazon EC2 and EC2 Amazon EC2 Auto Scaling group instances — Savings Plans and Reserved Instances pricing discounts.
- AWS Lambda functions and Amazon ECS services — Saving Plans pricing discounts.
- Amazon EBS volumes — other specific pricing discounts.
- Aurora and RDS databases — Reserved Instances pricing discounts and other specific pricing discounts.

###### Note

The savings estimation mode preference is only available for accounts within AWS Organizations that enable
Cost Optimization Hub in AWS Cost Explorer. For more information, see [Cost Optimization Hub](../../../cost-management/latest/userguide/cost-optimization-hub.md "../../../cost-management/latest/userguide/cost-optimization-hub.md")
in the _AWS Cost Management User Guide_.

Only the account manager or delegated administrator of your organization can activate member accounts in
specific AWS Regions to receive recommendations with pricing discounts. For the account manager and the
delegated administrator, the savings estimation mode preference is activated by default.

If the savings estimation mode preference isn’t activated, Compute Optimizer only uses the default On-Demand pricing
information.

## Next steps

For instructions on how to activate or deactivate the savings estimation mode preference for member
accounts, see [Activating savings estimation mode](activate-savings-estimation-mode.md "activate-savings-estimation-mode.md").
