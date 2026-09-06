

# Savings estimation mode
<a name="savings-estimation-mode"></a>

The savings estimation mode preference allows Compute Optimizer to analyze specific pricing discounts when generating the estimated cost savings of rightsizing recommendations. Compute Optimizer offers the savings estimation mode for the following pricing discounts per AWS resource:
+ Amazon EC2 and EC2 Auto Scaling group instances — Savings Plans and Reserved Instances pricing discounts.
+ AWS Lambda functions and Amazon ECS services — Saving Plans pricing discounts.
+ Amazon EBS volumes — other specific pricing discounts.
+ Aurora and RDS databases — Reserved Instances pricing discounts and other specific pricing discounts.

**Note**  
The savings estimation mode preference is only available for accounts within AWS Organizations that enable Cost Optimization Hub in AWS Cost Explorer. For more information, see [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the *AWS Cost Management User Guide*.

**Important**  
When you use Billing Transfer as a bill source account, the `AfterDiscounts` functionality is disabled and you can't enable it. Bill source accounts must validate rightsizing recommendations against their Reserved Instance and Savings Plans inventory to consider any unused commitment before making optimization decisions.

## Default behavior
<a name="sem-default-behavior"></a>

Compute Optimizer applies a default savings estimation mode based on your account type and Cost Optimization Hub enrollment status.

When a management account opts in to Cost Optimization Hub, all member accounts in the organization automatically default to `AfterDiscounts`. This means Compute Optimizer uses your organization's pricing discounts, such as Savings Plans and Reserved Instances, when estimating potential cost savings. If the management account opts out of Cost Optimization Hub or disables savings estimation mode in Cost Optimization Hub, member accounts without an explicit preference revert to `BeforeDiscounts`.

The following table describes the default behavior when no explicit savings estimation mode preference is set.


| Account type | Default savings estimation mode | 
| --- | --- | 
| Management account or Delegated Administrator | AfterDiscounts — Compute Optimizer uses pricing discounts in savings estimates. | 
| Standalone account | AfterDiscounts — Compute Optimizer uses pricing discounts in savings estimates. | 
| Member account (management account opted in to Cost Optimization Hub) | AfterDiscounts — Compute Optimizer uses pricing discounts in savings estimates. | 
| Member account (management account not opted in to Cost Optimization Hub) | BeforeDiscounts — Compute Optimizer uses On-Demand pricing only. | 

**Note**  
If you have Linked account discounts disabled in Cost Explorer, Compute Optimizer will be set to `BeforeDiscounts`.

## Overriding default preferences
<a name="sem-explicit-preferences"></a>

You can override the default behavior by explicitly setting a savings estimation mode preference using the `PutRecommendationPreferences` API or the Compute Optimizer console. An explicit preference always takes precedence over the default behavior described above.

Only the account manager or delegated administrator of your organization can activate member accounts in specific AWS Regions to receive recommendations with pricing discounts. For the account manager and the delegated administrator, the savings estimation mode preference is activated by default.

If the savings estimation mode preference isn't activated and the account doesn't qualify for a default of `AfterDiscounts`, Compute Optimizer uses the default On-Demand pricing information.

## Next steps
<a name="sem-next-steps"></a>

For instructions on how to activate or deactivate the savings estimation mode preference for member accounts, see [Activating savings estimation mode](activate-savings-estimation-mode.md).