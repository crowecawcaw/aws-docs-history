# Calculating security scores

On the AWS Security Hub CSPM console, the **Summary** page and the
**Controls** page display a summary security score across all of your
enabled standards. On the **Security standards** page, Security Hub CSPM also displays
a security score from 0–100 percent for each enabled standard.

When you first enable Security Hub CSPM, Security Hub CSPM calculates the summary security score and standard
security scores within 30 minutes of your first visit to the **Summary** or
**Security standards** page on the console. Scores are generated only
for standards that are enabled when you visit those pages on the console. In addition, AWS Config
resource recording must be configured for the scores to appear. The summary security score
is the average of the standard security scores. To review a list of standards that are
currently enabled, you can use the [GetEnabledStandards](../../1.0/APIReference/API_GetEnabledStandards.md "../../1.0/APIReference/API_GetEnabledStandards.md") operation of the Security Hub CSPM API.

After first-time score generation, Security Hub CSPM updates security scores every 24 hours. Security Hub CSPM
displays a timestamp to indicate when a security score was last updated. Note that it can
take up to 24 hours for first-time security scores to be generated in the China Regions and
AWS GovCloud (US) Regions.

If you turn on [consolidated control
findings](controls-findings-create-update.md#consolidated-control-findings "controls-findings-create-update.md#consolidated-control-findings"), it can take up to 24 hours for your security scores to update. In
addition, enabling a new aggregation Region or updating linked Regions resets existing
security scores. It can take up to 24 hours for Security Hub CSPM to generate new security scores that
include data from the updated Regions.

## Method of calculating security scores

Security scores represent the proportion of **Passed**
controls to enabled controls. The score is displayed as a percentage rounded up or down to the nearest whole number.

Security Hub CSPM calculates a summary security score across all of your enabled standards. Security Hub CSPM also
calculates a security score for each enabled standard. For purposes of score calculation, enabled controls
include controls with a status of **Passed**, **Failed**, and **Unknown**.
Controls with a status of **No data** are excluded from the score calculation.

Security Hub CSPM ignores archived and suppressed findings when calculating control status. This can impact security scores. For example,
if you suppress all failed findings for a control, its status becomes **Passed**, which can in turn
improve your security scores. For more information about control status, see [Evaluating compliance status and control
status](controls-overall-status.md "controls-overall-status.md").

**Scoring example:**

| Standard                                        | Passed controls | Failed controls | Unknown controls | Standard score |
| ----------------------------------------------- | --------------- | --------------- | ---------------- | -------------- |
| AWS Foundational Security Best Practices v1.0.0 | 168             | 22              | 0                | 88%            |
| CIS AWS Foundations Benchmark v1.4.0            | 8               | 29              | 0                | 22%            |
| CIS AWS Foundations Benchmark v1.2.0            | 6               | 35              | 0                | 15%            |
| NIST Special Publication 800-53 Revision 5      | 159             | 56              | 0                | 74%            |
| PCI DSS v3.2.1                                  | 28              | 17              | 0                | 62%            |

When calculating the summary security score, Security Hub CSPM counts each control only
once across standards. For example, if you have enabled a control that applies to three enabled standards, it only
counts as one enabled control for scoring purposes.

In this example, although the total number of enabled controls across enabled standards is 528, Security Hub CSPM counts each
unique control only once for scoring purposes. The number of unique enabled controls is likely lower than 528. If we assume the number of unique enabled controls
is 515, and the number of unique passed controls is 357, the summary score is 69%. This score is calculated by dividing
the number of unique passed controls by the number of unique enabled controls.

You might have a summary score that differs from the standard security score, even if you've
enabled only one standard in your account in the current Region. This can occur if
you're signed in to an administrator account and member accounts have additional
standards or different standards enabled. This can also occur if you're viewing the
score from the aggregation Region and additional standards or different standards are
enabled in linked Regions.

## Security scores for administrator

accounts

If you're signed in to an administrator account, the summary security score and
standard scores account for control statuses in the administrator account and all of the
member accounts.

If the status of a control is **Failed** in even one member account,
its status is **Failed** in the administrator account and impacts the
administrator account scores.

If you're signed in to an administrator account and are viewing scores in an
aggregation Region, security scores account for control statuses in all member accounts
_and_ all linked Regions.

## Security scores if you have set

an aggregation Region

If you have set an aggregation AWS Region, the summary security score and standard
scores account for control statuses in all  linked Regions.

If the status of a control is **Failed** in even one linked Region,
its status is **Failed** in the aggregation Region and impacts the
aggregation Region scores.

If you're signed in to an administrator account and are viewing scores in an
aggregation Region, security scores account for control statuses in all member accounts
_and_ all linked Regions.
