# Channel Management

AWS Partner Central Channel Management provides AWS Solution Providers, Distributors, and Distribution Sellers (Channel Partners) with capabilities to manage their AWS accounts participating in Channel Programs. AWS Partner Central Channel Management is used with [AWS Billing Transfer](https://aws.amazon.com/aws-cost-management/aws-billing-transfer "https://aws.amazon.com/aws-cost-management/aws-billing-transfer") to enable channel partners to resell to end customers while customers retain root access to their own AWS management account.

Key capabilities include:

- Centrally manage AWS accounts used for reselling
- Establish, track, and manage relationships with customers and distribution sellers
- Qualify for partner program benefits and discounts
- Monitor billing transfer relationships across multiple accounts
  Prerequisites:

- Active registration in AWS Channel Programs (Solution Provider, Distribution, or Distribution Seller)
- AWS Partner Central account with linked AWS account
- AWS Partner Central user with mapped Partner Central Channel IAM roles
- [Necessary IAM roles provisioned in the AWS accounts used in channel management](../APIReference/channel-access-control.md "../APIReference/channel-access-control.md")
- [AWS Partner Central user with mapped Partner Central Channel IAM roles](channel-management-user-mapping.md "channel-management-user-mapping.md")
- Active AWS management account used to receive bills and administer channel programs

###### Important

AWS Partner Central channel management features require IAM roles to be configured in both the Partner Central linked AWS account and the AWS management account used to receive bills and administer channel programs. Work with your AWS Partner Central cloud admin to ensure IAM permissions are configured, and work with your alliance lead or cloud admin to map IAM roles to Partner Central users. Learn more about accessing channel management in the [API reference](../APIReference/channel-access-control.md "../APIReference/channel-access-control.md").

## How AWS Partner Central channel management works

The Channel Management workflow follows a structured process to set up and manage your resale business. Here's how the components work together:

1. **Create and activate Program Management Accounts**

Report your AWS management accounts as PMAs to associate them with your channel program authorization. Activate your program management accounts instantly using channel handshakes to verify consent from the AWS management account. 2. **Establish relationships with customers or distribution sellers**

Create relationships to define how you work with each customer or downstream seller AWS management account and qualify for channel program benefits. Select appropriate support models and settings for each relationship. 3. **Set up service periods to manage billing transfer offboarding (optional)**

Add service periods to relationships to enforce minimum notice periods or fixed commitment periods on billing transfer. Partner service periods are added to govern changes to billing transfer, and must be accepted by the customer's AWS management account. 4. **Monitor billing transfer status and relationship list**

Track the status of billing transfers across all program management accounts and relationships from a central location.
