# Replicate IAM Identity Center to an

additional Region

If your environment meets the [prerequisites](multi-region-iam-identity-center.md#multi-region-prerequisites "multi-region-iam-identity-center.md#multi-region-prerequisites"), follow the steps below to
replicate your IAM Identity Center instance to an additional Region:

## Step 1: Create a replica key in the additional Region

Before replicating IAM Identity Center to a Region, you must first create a replica key of your
customer managed KMS key in that Region and configure the replica key with the permissions
required for the operations of IAM Identity Center. For instructions on creating multi-Region replica
keys, see [Create multi-Region
replica keys](../../../kms/latest/developerguide/multi-region-keys-replicate.md "../../../kms/latest/developerguide/multi-region-keys-replicate.md").

The recommended approach for the KMS key permissions is to copy the key policy from the
primary key, which grants the same permissions already established for IAM Identity Center in the primary
Region.
Alternatively, you can define Region-specific key policies, though this approach increases
the complexity of managing permissions across Regions and may require additional
coordination when updating policies in the future.

###### Note

AWS KMS doesn't synchronize your KMS key policy across the Regions of your multi-Region
KMS key.
To keep the KMS key policy in sync across the KMS key Regions, you will need to apply
changes in each Region individually.

## Step 2: Add the Region in IAM Identity Center

Adding a Region in IAM Identity Center triggers automatic and asynchronous replication of IAM Identity Center data to that Region.
Below are instructions for doing this in the AWS Management Console and AWS CLI

Console

**To add a Region**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. In the navigation pane, choose **Settings**.
3. Choose the **Management** tab.
4. In the **Regions for IAM Identity Center** section, choose **Add
   Region**.
5. In the **AWS Regions available for replication** section,
   choose your preferred AWS Region. If the Region doesn't appear in the list, it's
   not available for replication because the KMS key hasn't been replicated there.
   For more information, see _Implementing customer managed KMS keys in
   IAM Identity Center_.
6. Choose **Add Region**.
7. In the **Regions for IAM Identity Center** section, monitor
   the Region status. Use the **Refresh** button (circular arrow) to
   check the latest Region status as needed. After the replication completes, proceed
   to Step 2.

AWS CLI

**To add a Region**

```
aws sso-admin add-region \
    --instance-arn arn:aws:sso:::instance/ssoins-1234567890abcdef \
    --region-name eu-west-1

```

**To check the current Region status**

```
aws sso-admin describe-region \
    --instance-arn arn:aws:sso:::instance/ssoins-1234567890abcdef \
    --region-name eu-west-1
```

When the Region status is ACTIVE, you can proceed to Step 2.

The duration of the initial replication to an additional Region depends on the amount of
data in your IAM Identity Center instance. Subsequent incremental changes are replicated within seconds
in most cases.

## Step 3: Update external IdP setup

Follow the tutorial for your external IdP in [IAM Identity Center identity source tutorials](tutorials.md "tutorials.md") for the
following steps:

**Step 3.a: Add the Assertion Consumer Service (ACS) URLs to your
external IdP**

This step enables direct sign-in to each additional Region and is required to enable
sign-in to AWS managed applications deployed in those Regions and for access to
AWS accounts through those Regions. To learn where to find the ACS URLs, see [ACS endpoints in the primary and additional AWS Regions](multi-region-workforce-access.md#acs-endpoints "multi-region-workforce-access.md#acs-endpoints").

**Step 3.b (Optional): Make the AWS access portal available in the
external IdP portal**

Make the AWS access portal in the additional Region available as a bookmark app in the
external IdP portal. Bookmark apps contain only a link (URL) to the desired destination and
are similar to a browser bookmark. You can find the AWS access portal URLs in the console by
choosing **View all AWS access portal URLs** in the **Regions for IAM
Identity
Center** section. For more information, see [AWS access portal endpoints in the primary and additional AWS Regions](multi-region-workforce-access.md#portal-endpoints "multi-region-workforce-access.md#portal-endpoints").

IAM Identity Center supports IdP-initiated SAML SSO in each additional Region, but external IdPs
typically support this with only a single ACS URL. For continuity, we recommend keeping
the primary Region's ACS URL in use for IdP-initiated SAML SSO and relying on bookmark
apps and browser bookmarks for access to additional Regions.

## Step 4: Confirm firewall and gateway allow-lists

Review your domain allow-lists in firewalls or gateways, and update them based on the [documented allow-lists](enable-identity-center-portal-access.md "enable-identity-center-portal-access.md").

## Step 5: Provide information to your users

Provide your users with information about the new setup, including the AWS access portal URL
in the additional Region and how to use the additional Regions. Review the following
sections for relevant details:

- [Workforce access through an additional Region](multi-region-workforce-access.md "multi-region-workforce-access.md")
- [Failover to an additional Region for AWS account access](multi-region-failover.md "multi-region-failover.md")
- [Deploying and managing applications across multiple AWS
  Regions](multi-region-application-use.md "multi-region-application-use.md")

## Region changes beyond adding the first Region

You can add and remove additional Regions. The primary Region cannot be removed other
than by deleting the entire IAM Identity Center instance. For more information on removing a Region, see [Remove a Region from IAM Identity Center](remove-region.md "remove-region.md").

You cannot promote an additional Region to be the primary or demote the primary Region
to be additional.

## What data is replicated?

IAM Identity Center replicates the following data:

| Data                                                                 | Replication source and target                                                           |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Workforce identities (users, groups, group memberships)              | From the primary Region to the additional Regions                                       |
| Permission sets and their assignments to users and groups            | From the primary Region to the additional Regions                                       |
| Configuration (such as external IdP SAML settings)                   | From the primary Region to the additional Regions                                       |
| Application metadata and application assignments to users and groups | From an application's connected IAM Identity Center Region to the other enabled Regions |
| Trusted token issuers                                                | From the primary Region to the additional Regions                                       |
| Sessions                                                             | From the session's originating Region to the other enabled Regions                      |

###### Note

IAM Identity Center doesn't replicate data stored in AWS managed applications. Also, it doesn't change the regional footprint of an application deployment.
For example, if your IAM Identity Center instance in in US East (N. Virginia), and you have Amazon Redshift deployed in the same Region, replicating IAM Identity Center to
US West (Oregon) doesn't affect the deployment Region of Amazon Redshift and the data it stores.

**Considerations:**

- **Global resource identifiers across enabled Regions** -
  Users, groups, permission sets, and other resources have the same identifiers across the
  enabled Regions.
- **Replication doesn't affect provisioned IAM roles** -
  Existing IAM roles provisioned from permission set assignments are used during account
  sign-in from any enabled Region.
- **Replication doesn't incur KMS usage charges** -
  Replication of data to an additional Region doesn't lead to KMS usage charge.
