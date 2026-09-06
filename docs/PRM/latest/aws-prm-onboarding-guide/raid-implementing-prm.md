

# Implementing PRM with a Revenue Attribution ID
<a name="raid-implementing-prm"></a>

**Important**  
No implementation rework is required for existing PRM-enabled products. If you already implemented PRM using an AWS Marketplace listing's product code as the tag value or in the user agent string, you do not need to change that implementation to use a Revenue Attribution ID.  
You can leverage this additional capability by creating a Revenue Attribution ID, associating it to the PRM-enabled product in Step 1 of the creation wizard, and providing your monthly deal-level cost allocation percentages in Step 2. Revenue Attribution IDs map product-level revenue to specific AWS Marketplace Offers and/or ACE opportunities — eliminating rework.

PRM implementation requires a unique identifier — either your AWS Marketplace product listing's product code or a Revenue Attribution ID — used as the value in a resource tag or user agent string. The two scenarios are:

**Scenario 1: Product-level implementation (AWS Marketplace listing product code as the unique identifier)**

For product-level implementation details, refer to the [Resource Tagging](manual-tagging.md) or [User Agent String](user-agent-implementation.md) documentation.

**Scenario 2: Deal-level implementation (Revenue Attribution ID as the unique identifier)**

If you implement PRM using a Revenue Attribution ID directly as the tag value or in the user agent string, AWS measures consumption at the deal level from the start. Use this approach for new implementations or when you want deal-level measurement without first establishing product-level PRM.

The Revenue Attribution ID format is `ra-<13 character string>` (for example, `ra-aabbccddee001`).

## Resource Tagging
<a name="raid-resource-tagging"></a>

Add the tag to your resources:
+ Tag Key: `aws-apn-id`
+ Tag Value: `<RA ID>`
+ Example: `ra-aabbccddee001`

See [Resource Tagging](manual-tagging.md) for implementation details.

## User Agent String
<a name="raid-user-agent-string"></a>

Configure the User Agent string format `APN_1.1/pc_<RA ID>$` for AWS services.
+ Example: `APN_1.1/pc_ra-aabbccddee001$`

See [User Agent String](user-agent-implementation.md) for implementation details.

**Note**  
Only use a Revenue Attribution ID in your user agent string if you have not already implemented product-level PRM via user agent string. Multiple user agent identifiers are not supported. If you have already implemented product-level PRM via user agent string, use the deal-level overlay approach (Scenario 1) instead — no changes to your existing user agent string are required.