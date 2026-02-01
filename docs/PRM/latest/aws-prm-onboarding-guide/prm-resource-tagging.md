# Resource Tagging

Partner product resource tagging enables AWS Partners to demonstrate how their products drive
service consumption and AWS revenue by tagging resources with partner product identifiers.

This self-service capability allows partners to tag resources in their own account or customer's
account to track AWS revenue driven by the partner's product.

## Prerequisites

Before implementing resource tagging, ensure you meet all requirements listed in the [Resource Tagging Prerequisites](resource-tagging-prerequisites.md "resource-tagging-prerequisites.md") section.

## 3-Step Implementation Process

1. [Get your product code from AWS Marketplace Management Portal](product-code-retrieval.md "product-code-retrieval.md")
2. Add the tag to your resources:
   - Tag Key: `aws-apn-id`
   - Tag Value: `pc:<product-code>`
   - Example: `pc:5ugbbrmu7ud3u5hsipfzug61p`

3. Apply via automated or manual methods listed below

## Tagging Methods

### Automated Tagging

For low-touch approach at scale, refer to the [Automated Tagging](automated-tagging.md "automated-tagging.md") section.

### Manual Tagging

You can manually tag your resources using the AWS Management Console.

###### To get started

1. Go to your AWS Management Console.
2. Go to the resources you want to tag. Example: Amazon RDS.
3. Choose **Add tags**.
4. Enter `aws-apn-id` as the **Tag key**.
5. Enter `pc:5ugbbrmu7ud3u5hsipfzug61p` as the **Tag value** (replace `5ugbbrmu7ud3u5hsipfzug61p` with your product code).
6. Choose **Save**.

Repeat the steps above for all associated resources such as Snapshots. For more information about tagging resources, see the [Tag your Amazon EC2 resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md") in the Amazon Elastic Compute Cloud user guide for Linux instances.

## Best Practices

- Always use lowercase 'aws-apn-id' key
- Ensure 'pc:' prefix in value
- Validate product code format
- Document all tagged resources
- Monitor tag compliance and revenue attribution

###### Note

Once a resource is tagged with a partner's product code, AWS will continue to attribute
revenue to the product until the tag is removed or the resource is shut down.

## Tag Management

**Tag Conflicts:** Since an AWS resource can only have one tag
with the 'aws-apn-id' key, if another partner's tag exists, you must remove it and add your own.

**Tag Removal:** Any user with account access can remove tags.
Both customers and partners (with account access) can remove tags.
