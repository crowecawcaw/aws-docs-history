

# Implementation

**Note**  
AWS Revenue Measurement is about customer-related consumption, not a particular environment. Apply Identity Tagging in any environment connected to customer workloads or consumption (production, dev, test, UAT, and so on), paid or unpaid. Internal or non-customer-specific environments you run for your own business are not in scope.

## 3-Step Implementation Process
<a name="identity-tagging-steps"></a>

1. Get your product code from the AWS Marketplace Management Portal. For step-by-step instructions, see [Product Code Retrieval](product-code-retrieval.md).

1. Add the tag to each IAM principal (role or user) your organization operates in the customer environment:
   + Tag Key: `aws-apn-id-{{partner-central-aws-account-id}}`
   + Example Tag Key: `aws-apn-id-123456789012`
   + Tag Value: `pc:{{product-code}}`
   + Example Tag Value: `pc:5ugbbrmu7ud3u5hsipfzug61p`

   For how to construct your key and value, see [Constructing Your Tag Key and Value](manual-tagging.md#tag-key-construction).

1. Verify the tag using the methods described below.

**Note**  
An IAM principal can have only one tag per partner-scoped key (`aws-apn-id-{{partner-central-aws-account-id}}`). If you need to attribute the same identity's consumption to multiple products, operate separate identities, one per product, or use Resource Tagging or User Agent String instead.

## Tagging an IAM Role via the IAM Console
<a name="identity-tagging-console"></a>

You can tag the IAM role your organization assumes using the IAM console.

1. Sign into the AWS Management Console with permissions to manage the IAM role.

1. Open the IAM console.

1. In the navigation pane, choose Roles.

1. Choose the role your organization operates in the customer environment.

1. Choose the Tags tab.

1. Choose Add tags.

1. Enter `aws-apn-id-123456789012` as the Key (replace 123456789012 with your Partner Central AWS account ID).

1. Enter `pc:5ugbbrmu7ud3u5hsipfzug61p` as the Value (replace 5ugbbrmu7ud3u5hsipfzug61p with your product code).

1. Choose Save changes.

1. Verify the tag landed by staying on the Tags tab and confirming the key/value appear.

For IAM users, follow the same steps under Users instead of Roles. For more information, see [Managing tags on IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags_roles.html) in the IAM User Guide.

## Tagging via AWS CLI
<a name="identity-tagging-cli"></a>

You can tag IAM principals using the AWS CLI. Run the following commands with permissions to manage the principal.

**Tag a single IAM role**

**Note**  
Replace MyPartnerRole with your IAM role name, 123456789012 with your Partner Central AWS account ID, and 5ugbbrmu7ud3u5hsipfzug61p with your product code in the following example.

```bash
aws iam tag-role \
  --role-name MyPartnerRole \
  --tags Key=aws-apn-id-123456789012,Value=pc:5ugbbrmu7ud3u5hsipfzug61p
```

**Tag a single IAM user**

**Note**  
Replace MyPartnerUser with your IAM username, 123456789012 with your Partner Central AWS account ID, and 5ugbbrmu7ud3u5hsipfzug61p with your product code in the following example.

```bash
aws iam tag-user \
  --user-name MyPartnerUser \
  --tags Key=aws-apn-id-123456789012,Value=pc:5ugbbrmu7ud3u5hsipfzug61p
```

**Tag multiple roles**

If your organization operates multiple roles across customer engagements, tag each role with the same product code.

**Note**  
Replace the role names, 123456789012 with your Partner Central AWS account ID, and 5ugbbrmu7ud3u5hsipfzug61p with your product code in the following example.

```bash
for ROLE_NAME in MyPartnerRole-A MyPartnerRole-B MyPartnerRole-C; do
  aws iam tag-role \
    --role-name $ROLE_NAME \
    --tags Key=aws-apn-id-123456789012,Value=pc:5ugbbrmu7ud3u5hsipfzug61p
done
```

## Tag Verification
<a name="identity-tagging-verification"></a>

After applying the tag, verify that it is correctly associated with your IAM principal. Run the following command to confirm the tag on a role:

```bash
aws iam list-role-tags \
  --role-name MyPartnerRole
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

For IAM users, use `list-user-tags` with the `--user-name` parameter.

## Tag Management
<a name="identity-tagging-management"></a>

**Tag Persistence:** Once an IAM principal is tagged with a partner's product code, AWS continues to attribute activity from that identity to the product until the tag is removed.

**Tag Removal and Billing Month:** When an Identity Tagging tag is removed from a principal, or the principal is deleted, attribution is retained for the billing month in which the removal occurred and stops from the following billing month.

**Tag Removal:** Any user with permission to manage the IAM principal can remove its tags. To remove a tag, use the IAM console or CLI:

```bash
aws iam untag-role \
  --role-name MyPartnerRole \
  --tag-keys aws-apn-id-123456789012
```