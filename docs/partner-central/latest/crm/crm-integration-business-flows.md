# Working with referrals, leads, and

opportunities

The following topics describe how sales referrals become leads and opportunities. The
topics also explain the differences between opportunities originated by AWS and those
originated by partners.

###### Note

The approval process for [partner-originated referrals](#what-is-a-partner-originated-opportunity-referral "#what-is-a-partner-originated-opportunity-referral") assumes that you use Salesforce and the CRM connector.

###### Topics

- [What is a referral?](#what-is-a-lead-referral "#what-is-a-lead-referral")
- [What is an AWS originated
  opportunity referral?](#what-is-an-aws-originated-opportunity-referral "#what-is-an-aws-originated-opportunity-referral")
- [What is a partner-originated opportunity referral?](#what-is-a-partner-originated-opportunity-referral "#what-is-a-partner-originated-opportunity-referral")
- [Closing a referral](#closing-a-referral "#closing-a-referral")

## What is a referral?

The term _referral_ serves as a general descriptor for leads and
opportunities. A _lead_ refers to a contact who expresses interest in an
AWS product or partner solution. During the initial stages of the sales process, a sales
representative determines whether the interested individual has the potential to become an
AWS customer. This assessment and validation phase is referred to as
_qualification_. If a lead is deemed qualified and has a higher
probability of converting to a customer, it becomes an
_opportunity_.

## What is an AWS originated

opportunity referral?

AWS Sales creates an AWS-originated opportunity referral by sharing the referral
with you. The AWS Sales team receives recommendations to attach a partner to an AWS
sales opportunity based on multiple factors, such as the quality of information in the
solution listing, past opportunities, progress in the partnership journey, and past
performance.

You receive referrals with
the customer contact details—contact name, title, email, and phone—masked. However, the referral
contains AWS contact details, including the customer name and project title, that you use to decide whether to pursue the referral.
To accept or reject the referral, you send an `Accepted` or
`Rejected` value for the `partnerAcceptanceStatus` field. You must do that before the `acceptBy` date and
time specified in the payload. If you reject a referral, you must provide a `rejectionReason`.

When you accept or reject an AWS-originated referral, don't update
any other values in the referral. Every update on a referral, from you or AWS, can
take up to one hour to sync with your CRM system. When you accept a referral, AWS sends a new payload with
the unmasked customer contact details. You then engage with the
opportunity and provide regular updates to AWS.

## What is a partner-originated opportunity referral?

You create a partner-originated opportunity referral when you share a referral with
AWS Sales for coselling or visibility. By default, all partner-originated opportunity
referrals go through a validation (review) process, and they have a status of **Submitted**.
When the review starts, the status changes to
**In-review** and you can't update the opportunity until validation
completes.

If the validation succeeds, the opportunity status changes to
**Approved**, and you can update to the opportunity. If the
validation fails, the status becomes **Action required**, and the
validator’s comments appear in the **apnReviewerComments**
field in Salesforce. Fix any issues and resubmit the referral.

After you update and resubmit the opportunity, it moves back to the
**Submitted** state and the validation process starts again. When the
opportunity passes, the referral state becomes **Approved**, and partners
and AWS can share regular updates about the opportunity. The validation process can take
up to five business days.

For more information about the fields in partner-originated leads and opportunities, see
[Leads-Fields](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Leads-Fields.csv "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Leads-Fields.csv") and
[Opportunity-Fields](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Fields.csv "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Fields.csv") on GitHub

###### Note

AWS doesn’t support the "Partner Shares Lead with AWS" scenario. Partners who
receive a lead through an external source typically pursue it themselves. After the lead
becomes an approved opportunity, partners can submit it to AWS as a partner originated
opportunity referral.

## Closing a referral

When partners close referrals as **Launched**, they must attach an
AWS account associated with the customer. To close a referral as **Closed
Lost**, partners must provide a **closedLostReason**. For a
referral that relates to a sale on AWS Marketplace, partners must attach an AWS Marketplace offer to the
opportunity.

To see an opportunity's status, partners can check the **awsStage** field in Salesforce.

###### Note

The **awsStage** field differs from the **stage** field. The **awsStage** field
displays a referral's current stage as a read-only value. The `stage` field
displays regular updates about a referral.
