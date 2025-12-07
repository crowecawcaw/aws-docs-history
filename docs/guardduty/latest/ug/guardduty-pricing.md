# Pricing in GuardDuty

This section focuses on the AWS Free Tier model that GuardDuty uses for various protection plans, and how you can
view estimated and actual usage costs. If you
are looking for the pricing details associated with all the protection plans across supported Regions,
see [GuardDuty
pricing](https://aws.amazon.com/guardduty/pricing/ "https://aws.amazon.com/guardduty/pricing/").

**AWS Free Tier**

AWS Free Tier helps you explore and try out AWS services free of charge up to
specified limits for each service. There are three categories – 12 months free,
always free, and short-term free trials. Amazon GuardDuty belongs to the short-term free trial
category and offers a 30-day free trial. When you continue using GuardDuty after this free
trial ends, you start incurring cost based on how you use this service.

\***\*1**Exception to GuardDuty 30-day free trial\*\*

On-demand malware scan (under Malware Protection for EC2) and Malware Protection for S3 don't fall into the GuardDuty 30-day short
term free trial category. Malware Protection for S3 falls into the 12 months free category of the
AWS Free Tier whereas the On-demand malware scan follows a pay-as-you-use cost model. There is no
30-day free trial or a 12-month Free Tier cost model with On-demand malware scan.

## Using GuardDuty 30-day free

trial

When using GuardDuty for the first time in an AWS Region, your AWS account is
automatically enrolled in a 30-day free trial in that Region. Some of the protection
plans will also get enabled automatically and are included in the 30-day free trial.
Because GuardDuty is a regional service, when you enable it for the first time in a
different Region, your account will get a 30-day free trial of GuardDuty in that Region.
When working with multiple accounts in a GuardDuty organization, each account gets its
own 30-day free trial.

Use the following table to review which protection plans are enabled by default with GuardDuty,
and their free trial availability.

| Protection plan                                                                                                                                                                 | Enabled by default with GuardDuty | Separate free trial availability**[2](#protection-plan-separate-enablement-gdu "#protection-plan-separate-enablement-gdu")** |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| [EKS Protection](kubernetes-protection.md "kubernetes-protection.md")                                                                                                           | Yes                               | Yes                                                                                                                          |
| [S3 Protection](s3-protection.md "s3-protection.md")                                                                                                                            | Yes                               | Yes                                                                                                                          |
| [Runtime Monitoring](runtime-monitoring.md "runtime-monitoring.md")                                                                                                             | No                                | Yes                                                                                                                          |
| [Malware Protection for EC2](malware-protection.md "malware-protection.md") – [GuardDuty-initiated malware scan](gdu-initiated-malware-scan.md "gdu-initiated-malware-scan.md") | Yes                               | Yes                                                                                                                          |
| [Malware Protection for EC2](malware-protection.md "malware-protection.md") – [On-demand malware scan in GuardDuty](on-demand-malware-scan.md "on-demand-malware-scan.md")      | No                                | No**[1](#protection-plan-exception-free-trial-gdu "#protection-plan-exception-free-trial-gdu")**                             |
| [GuardDuty Malware Protection for S3](gdu-malware-protection-s3.md "gdu-malware-protection-s3.md")                                                                              | No                                | No**[1](#protection-plan-exception-free-trial-gdu "#protection-plan-exception-free-trial-gdu")**                             |
| [RDS Protection](rds-protection.md "rds-protection.md")                                                                                                                         | Yes                               | Yes                                                                                                                          |
| [Lambda Protection](lambda-protection.md "lambda-protection.md")                                                                                                                | Yes                               | Yes                                                                                                                          |

**2**When you enable
GuardDuty for the first time, protection plans (except Runtime Monitoring) are automatically
enabled and included in the initial 30-day free trial. When an existing GuardDuty account enables
a new protection plan after their initial GuardDuty free trial has expired, then that protection
plan comes with its own 30-day free trial. For
more information about free trials for protection plans, see the document associated
with each protection plan.

**View estimated usage cost during free trial**
– During 30-day free trial of GuardDuty and potentially a protection plan, GuardDuty
provides estimated usage cost for your account. If you're a delegated GuardDuty administrator account, you can view
the total estimated usage cost and account-level breakdown for all the member
accounts that have enabled GuardDuty. For more information, see [Monitoring GuardDuty Usage and Estimating Costs](monitoring_costs.md "monitoring_costs.md").

**Usage cost after free trial ends** – When
you continue using GuardDuty or any of its protection plans after the free trial ends,
you will start incurring associated usage costs. To view your bill, navigate to
**Cost Explorer** in the [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/") console.
For more information about AWS account billing, see the [AWS Billing User Guide](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md").

## Using Malware Protection for S3 with

12-month Free Tier

Malware Protection for S3 uses a Free Tier plan associated with your AWS accounts that are
either new, have an ongoing free tier, or have an expired 12-month free tier. For
more information, see [Pricing and usage cost for
Malware Protection for S3](pricing-malware-protection-for-s3-guardduty.md "pricing-malware-protection-for-s3-guardduty.md").
