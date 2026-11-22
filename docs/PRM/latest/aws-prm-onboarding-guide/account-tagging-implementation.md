

# Implementation

**Note**  
AWS Revenue Measurement is intended to measure production workloads. Dev/test/staging environments can be used for validating your implementation before rolling out to production.

Account Tagging for SaaS products uses AWS Organizations to apply the `aws-apn-id-{{partner-central-aws-account-id}}` tag to member accounts that host your product. You must perform tagging from the management account or a delegated administrator account in your organization.

## 3-Step Implementation Process
<a name="account-tagging-steps"></a>

1. Get your product code from [AWS Marketplace Management Portal](product-code-retrieval.md).

1. Add the tag to each member account hosting your product:
   + Tag Key: `aws-apn-id-{{partner-central-aws-account-id}}`
   + Example Tag Key: `aws-apn-id-123456789012`
   + Tag Value: `pc:{{product-code}}`
   + Example Tag Value: `pc:5ugbbrmu7ud3u5hsipfzug61p`

1. Verify the tag using the methods described below.

**Note**  
An AWS account can only have one tag with the `aws-apn-id-{{partner-central-aws-account-id}}` key. If you need to attribute consumption from the same account to multiple products, use Resource Tagging or User Agent String instead.

## Tagging via AWS Organizations Console
<a name="account-tagging-console"></a>

You can tag member accounts using the AWS Organizations console.

**To tag a single account**

1. Sign in to the AWS Management Console using your Organizations management account.

1. Open the AWS Organizations console.

1. In the navigation pane, choose AWS accounts.

1. Select the member account that hosts your product.

1. Choose the Tags tab.

1. Choose Manage tags.

1. Choose Add tag.

1. Enter `aws-apn-id-123456789012` as the Key (replace 123456789012 with your Partner Central AWS account ID).

1. Enter `pc:5ugbbrmu7ud3u5hsipfzug61p` as the Value (replace 5ugbbrmu7ud3u5hsipfzug61p with your product code).

1. Choose Save changes.

If your product runs across multiple accounts, repeat the steps above for each account that hosts your product.

## Tagging via AWS CLI
<a name="account-tagging-cli"></a>

You can tag member accounts using the AWS CLI. Run the following commands from your Organizations management account (or delegated administrator account).

**Tag a single account**

**Note**  
Replace 111111111111 with your member account ID, 123456789012 with your Partner Central AWS account ID, and 5ugbbrmu7ud3u5hsipfzug61p with your product code in the following example.

```bash
aws organizations tag-resource \
  --resource-id 111111111111 \
  --tags Key=aws-apn-id-123456789012,Value=pc:5ugbbrmu7ud3u5hsipfzug61p
```

**Tag multiple accounts**

If your product runs across multiple dedicated accounts, tag each account with the same product code.

**Note**  
Replace the member account IDs, 123456789012 with your Partner Central AWS account ID, and 5ugbbrmu7ud3u5hsipfzug61p with your product code in the following example.

```bash
for ACCOUNT_ID in 111111111111 222222222222 333333333333; do
  aws organizations tag-resource \
    --resource-id $ACCOUNT_ID \
    --tags Key=aws-apn-id-123456789012,Value=pc:5ugbbrmu7ud3u5hsipfzug61p
done
```

**Tag all accounts in an organizational unit (OU)**

If all accounts hosting your product are organized under the same OU, you can query the OU membership and tag each account.

**Note**  
Replace ou-xxxx-xxxxxxxx with your OU ID, 123456789012 with your Partner Central AWS account ID, and 5ugbbrmu7ud3u5hsipfzug61p with your product code in the following example.

```bash
for ACCOUNT_ID in $(aws organizations list-accounts-for-parent \
  --parent-id ou-xxxx-xxxxxxxx \
  --query 'Accounts[].Id' --output text); do
  aws organizations tag-resource \
    --resource-id $ACCOUNT_ID \
    --tags Key=aws-apn-id-123456789012,Value=pc:5ugbbrmu7ud3u5hsipfzug61p
done
```

## Verification
<a name="account-tagging-verification"></a>

After applying the tag, verify that the tag is correctly associated with your account.

**Verify via AWS CLI**

Run the following command from your management account to confirm the tag:

```bash
aws organizations list-tags-for-resource \
  --resource-id 111111111111
```

Expected output:

```json
{
    "Tags": [
        {
            "Key": "aws-apn-id-123456789012",
            "Value": "pc:5ugbbrmu7ud3u5hsipfzug61p"
        }
    ]
}
```

## Tag Management
<a name="account-tagging-management"></a>

**Tag Persistence:** Once an account is tagged with a partner's product code, AWS continues to attribute all revenue from that account to the product until the tag is removed.

**Tag Conflicts:** Since an AWS account can only have one tag with the `aws-apn-id-{{partner-central-aws-account-id}}` key, only one partner product identifier is allowed per account. If you need to attribute consumption from the same account to multiple products, use Resource Tagging or User Agent String instead.

**Tag Removal:** Any user with AWS Organizations management account access (or delegated administrator access) can remove account tags. To remove a tag, use the AWS Organizations console or CLI:

```bash
aws organizations untag-resource \
  --resource-id 111111111111 \
  --tag-keys aws-apn-id-123456789012
```