

# Channel Management
<a name="channel-management"></a>

AWS Partner Central Channel Management provides AWS Solution Providers, Distributors, and Distribution Sellers (Channel Partners) with capabilities to manage their AWS accounts participating in Channel Programs. AWS Partner Central Channel Management is used with [AWS Billing Transfer](https://aws.amazon.com/aws-cost-management/aws-billing-transfer) to enable channel partners to resell to end customers while customers retain root access to their own AWS management account.

To learn more about Channel Program Management, see the [Solution Provider Program User Guide](https://partnercentral.awspartner.com/partnercentral2/s/article?category=AWS_Solution_Provider_Program&article=AWS-Solution-Provider-Program-User-Guide) or the [Distribution Program User Guide](https://partnercentral.awspartner.com/partnercentral2/s/article?category=AWS_Distribution_Program&article=AWS-Distribution-Program-User-Guide). These guides provide step-by-step setup instructions covering activation, relationship reporting, and post-setup configuration.

For more information on AWS Billing Conductor pricing, see [AWS Billing Conductor Pricing](https://aws.amazon.com/aws-cost-management/aws-billing-conductor/pricing/).

Key capabilities include:
+ Centrally manage AWS accounts used for reselling
+ Establish, track, and manage relationships with customers and distribution sellers
+ Qualify for partner program benefits and discounts
+ Monitor billing transfer relationships across multiple accounts

Prerequisites:
+ Active registration in AWS Channel Programs (Solution Provider, Distribution, or Distribution Seller)
+ AWS Partner Central account with linked AWS account
+ AWS Partner Central user with mapped Partner Central Channel IAM roles
+ [Necessary IAM roles provisioned in the AWS accounts used in channel management](https://docs.aws.amazon.com/partner-central/latest/APIReference/channel-access-control.html)
+ [AWS Partner Central user with mapped Partner Central Channel IAM roles](https://docs.aws.amazon.com/partner-central/latest/getting-started/channel-management-user-mapping.html)
+ Active AWS management account used to receive bills and administer channel programs

**Important**  
AWS Partner Central channel management features require IAM roles to be configured in both the Partner Central linked AWS account and the AWS management account used to receive bills and administer channel programs. Work with your AWS Partner Central cloud admin to ensure IAM permissions are configured, and work with your alliance lead or cloud admin to map IAM roles to Partner Central users. Learn more about accessing channel management in the [API reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/channel-access-control.html).

## How AWS Partner Central channel management works
<a name="channel-management-works"></a>

The Channel Management workflow follows a structured process to set up and manage your resale business. Here's how the components work together:

1. **Create and activate Program Management Accounts**

   Report your AWS management accounts as PMAs to associate them with your channel program authorization. Activate your program management accounts instantly using channel handshakes to verify consent from the AWS management account.

1. **Establish relationships with customers or distribution sellers**

   Create relationships to define how you work with each customer or downstream seller AWS management account and qualify for channel program benefits. Select appropriate support models and settings for each relationship.

1. **Set up service periods to manage billing transfer offboarding (optional)**

   Add service periods to relationships to enforce minimum notice periods or fixed commitment periods on billing transfer. Partner service periods are added to govern changes to billing transfer, and must be accepted by the customer's AWS management account.

1. **Monitor billing transfer status and relationship list**

   Track the status of billing transfers across all program management accounts and relationships from a central location.