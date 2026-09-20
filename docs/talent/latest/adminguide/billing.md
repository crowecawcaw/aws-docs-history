

# Billing
<a name="billing"></a>

Amazon Connect Talent charges a single flat price for each completed candidate evaluation. Track your usage and charges through your AWS account in the AWS Billing and Cost Management console.

**Topics**
+ [What you are charged for](#billing-what-charged)
+ [Flat per-evaluation charge](#billing-flat-charge)
+ [When an evaluation is billable](#billing-billable)
+ [When an evaluation is not billable](#billing-not-billable)
+ [Each evaluation is charged independently](#billing-independent)
+ [Billing scenarios](#billing-scenarios)
+ [Other AWS service charges](#billing-other-charges)

## What you are charged for
<a name="billing-what-charged"></a>

Amazon Connect Talent charges a single flat price for each completed candidate evaluation. For current pricing, see the [Amazon Connect Talent pricing page](https://aws.amazon.com/products/connect/talent/pricing/).

## Flat per-evaluation charge
<a name="billing-flat-charge"></a>

You pay one charge for each billable evaluation. There is no separate price for each assessment or AI-led interview. When a candidate opts out of some parts of an evaluation, you still pay the full price. There is no reduction.

## When an evaluation is billable
<a name="billing-billable"></a>

An evaluation is billable when any of the following are true:
+ The candidate completes the evaluation.
+ The candidate completes a portion of the evaluation and opts out of the rest.

An assessment or AI-led interview is billable even when the candidate scored poorly. A low score does not change whether the evaluation is billed.

## When an evaluation is not billable
<a name="billing-not-billable"></a>

An evaluation is not billable in the following cases:
+ The candidate opted out of the entire evaluation and completed nothing. Amazon Connect Talent treats this as though the candidate was never invited.
+ A part of the evaluation could not be delivered because of a system or technical issue, or it timed out. This does not mean that the candidate scored poorly or closed their browser.
+ The evaluation has not finished. Amazon Connect Talent assesses charges only after every assessment and AI-led interview in the evaluation reaches a final outcome. When a candidate stops partway through and never returns, the evaluation is never charged.

## Each evaluation is charged independently
<a name="billing-independent"></a>

Each evaluation is a separate charge. When a recruiter sends a new evaluation and the candidate completes it, for example to re-evaluate a candidate after a weak result, that is a separate billable evaluation and a separate charge. Amazon Connect Talent charges the earlier completed evaluation and the new one separately.

## Billing scenarios
<a name="billing-scenarios"></a>

The following table shows common outcomes and whether Amazon Connect Talent charges for each one.


| Outcome | Charged? | Why | 
| --- | --- | --- | 
| The candidate completed all parts of the evaluation. | Yes | The candidate completed the evaluation. | 
| The candidate completed some parts and opted out of the rest. | Yes, full price | The candidate completed at least one part and opted out of every remaining part. There is no reduction. | 
| One part could not be delivered because of a technical failure. | No | A part could not be delivered because of a system or technical issue. | 
| The candidate opted out of the entire evaluation. | No | The candidate completed nothing. Amazon Connect Talent treats this as though the candidate was never invited. | 
| The recruiter re-sent the evaluation, and the candidate completed a second evaluation. | Yes, twice | Each completed evaluation is charged independently. | 
| The candidate stopped partway through and never returned. | No | The evaluation never reached a final outcome. | 

## Other AWS service charges
<a name="billing-other-charges"></a>

In addition to the per-evaluation charge, the following AWS services might appear on your bill when you use Amazon Connect Talent:
+ **Amazon Simple Email Service (Amazon SES)** – Amazon Connect Talent uses Amazon SES to send evaluation invitation emails to candidates. Amazon SES charges apply at standard Amazon SES rates. For more information, see [Amazon SES pricing](https://aws.amazon.com/ses/pricing/).
+ **Amazon Simple Storage Service (Amazon S3)** – Amazon Connect Talent uses Amazon S3 to store interview recordings and transcripts. Amazon S3 charges apply at standard Amazon S3 rates, consistent with Amazon Connect storage charges. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).