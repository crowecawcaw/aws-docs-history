

# Plan Management
<a name="plan-management"></a>

Flat-rate plans can be managed in the console or programmatically using the AWS CLI, AWS SDKs, or the PricingPlanManager API. For programmatic management, see Getting started with the PricingPlanManager API.

## New Plan Activation
<a name="new-activation"></a>

Paid plans use a two-phase activation: you first create the plan, then approve it to begin billing. This prevents you from being committed to charges before you confirm. Free plans activate immediately and don’t require approval.

When you create a paid plan:
+ The plan is created in a pending state and is not yet committed
+ No charges are incurred until you approve the plan
+ In the console, the confirmation step serves as your approval as long as you have permission to approve paid plans

When you approve a paid plan (or create a Free plan):
+ Plan activates immediately
+ Pro-rated charge for remaining days in current billing cycle appears on your account and is reflected in your next invoice
+ Full monthly charge begins with next billing cycle
+ Once a paid plan is approved and active, it can’t be canceled or reverted until the end of the current billing period.

**Pro-Ration Example**  
If you activate a $15/month Pro plan on the 16th day of a 30-day month, you’ll see a $7.50 charge on your account. This represents the 15 remaining days in the current billing cycle ($15 ÷ 30 days × 15 days = $7.50). Starting with your next billing cycle, you’ll be charged the full $15/month.

## Upgrading Plans
<a name="upgrading"></a>

When you upgrade to a higher plan tier:
+ Upgrade takes effect immediately
+ Your charge and usage allowances are prorated
+ Pro-rated charge for tier difference for remaining days in current cycle appears on your account and is reflected in your next invoice
+ Usage allowance increases immediately to new tier limits
+ Next billing cycle charges at new tier’s full monthly rate

**Pro-Ration Example**  
If you upgrade from a $15/month Pro plan to a $200/month Business plan on the 16th day of a 30-day month, you’ll see a $92.50 charge on your account. This represents the tier difference for the 15 remaining days in the current billing cycle (($200 - $15) ÷ 30 days × 15 days = $92.50). Starting with your next billing cycle, you’ll be charged the full $200/month Business plan rate.

## Downgrading Plans
<a name="downgrading"></a>

When you downgrade to a lower plan tier:
+ Downgrade takes effect at next billing cycle (not immediate)
+ No mid-cycle pro-ration credits provided
+ Continue paying current tier price through end of billing period
+ Next billing cycle charges at lower tier rate
+ Must ensure current usage fits within target tier allowances to avoid service disruption

## Cancelling Plans
<a name="cancelling"></a>

When you cancel a flat-rate plan:
+ Cancellation takes effect at end of current billing period (not immediate)
+ No refunds provided for remaining days in current period
+ You retain access to flat-rate plan benefits through cancellation date
+ After cancellation date, all usage billed at standard pay-as-you-go rates