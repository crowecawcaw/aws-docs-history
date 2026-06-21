# Complete prerequisites

The following prerequisites are completed by the **Alliance
Lead** within Partner Central.

## Ensure Partner Central is linked to an AWS account

Link your Partner Central account to your primary AWS account. Choose your account
carefully from the start. While unlinking and re-linking a different account is
possible, doing so creates data persistence issues and requires manual reconciliation
efforts.

- For more information on linking your accounts, see the [Account Linking](../getting-started/account-linking.md "../getting-started/account-linking.md") section.
- For more information on unlinking, see the [Partner Central support article](https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=AWS-Partner-Central#Unlinking-AWS-Partner-Central-and-AWS-accounts "https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=AWS-Partner-Central#Unlinking-AWS-Partner-Central-and-AWS-accounts").

## Complete Partner Central migration to AWS Console

Migrating to the new Partner Central experience in AWS Console is not required to
upgrade from Amazon S3 to API-based CRM integration. However, migration helps maintain
pipeline fidelity. Without migrating, you may experience degradation in ACE
Opportunity pipeline sync ability. This degradation occurs when Partner Central users take
actions outside your CRM:

- They may interact with API-based functionality within the AWS Console
  that Amazon S3 does not support.
- If you use AWS Marketing Leads, those will no longer sync from Partner Central
  via CRM Integration using the Amazon S3 backend.

For more details on this process, see the [Partner Central migration guide](../getting-started/migrating-to-partner-central.md "../getting-started/migrating-to-partner-central.md").
