

# Billing and pricing for AWS Organizations
<a name="pricing"></a>

AWS Organizations is offered at no additional charge. You are charged only for AWS resources that users and roles in your member accounts use. For example, you are charged the standard fees for Amazon EC2 instances that are used by users or roles in your member accounts. For information about the pricing of other AWS services, see [AWS Pricing](https://aws.amazon.com/pricing/services/).

## Who pays for usage incurred by users under an AWS member account in my organization?
<a name="pricing-payment-responsibility"></a>

The owner of the [management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#management-account) is responsible for paying for all usage, data, and resources used by the accounts in the organization.

## Will my bill reflect the organizational unit structure that I created in my organization?
<a name="pricing-payment-structure"></a>

Your bill will not reflect the structure that you have defined in your organization. You can use [cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in individual AWS accounts to categorize and track your AWS costs, and this allocation will be visible in the consolidated bill for your organization.