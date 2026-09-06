

# Security Hub Extended plan
<a name="securityhub-extended-plan"></a>

 With the Security Hub Extended plan, you can protect your entire enterprise estate across cloud, endpoint, network, identity, data, email, and browser. Use AWS Security Hub as the center of an integrated security operations experience. With the Security Hub Extended plan, you can select partner solutions that address your security needs and sign up for flexible pay-as-you-go pricing with no upfront investments or long-term commitments required. You can add or remove partner solutions as your business needs evolve. 

 The Security Hub Extended plan is available to all customers who have enabled the Security Hub Essentials plan. Charges for Security Hub Extended plan appear on your monthly AWS bill with AWS as the seller of record. 

 Security Hub Extended plan pricing for all solutions is available on the Extended plan tab of the [Security Hub pricing details page](https://aws.amazon.com/security-hub/pricing/#pricing_details). 

## Permissions for the Security Hub Extended plan
<a name="securityhub-extended-plan-access"></a>

 To subscribe to a partner product from the Security Hub Extended plan, you need the following permissions, in addition to your Security Hub permissions: 
+ `aws-marketplace:ViewSubscriptions`
+ `aws-marketplace:Subscribe`

 To unsubscribe from a partner product in the Security Hub Extended plan, you need the following permissions, in addition to your Security Hub permissions: 
+ `license-manager:ListReceivedLicenses`
+ `aws-marketplace:ListAgreementCharges`
+ `aws-marketplace:Unsubscribe`

 For more information on AWS Marketplace permissions, see [Controlling access to AWS Marketplace subscriptions](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html) in the *AWS Marketplace Buyer Guide*. 

## Reviewing and signing up for Extended plan partners
<a name="securityhub-extended-plan-subscribe"></a>

 The Security Hub Extended plan is accessible through the Security Hub delegated administrator account or standalone accounts. On the Security Hub Extended plan page, you can view details about each partner, initiate a subscription to a partner solution, and begin the onboarding process to each partner's solution through the partner's onboarding page. 

**To access the Security Hub Extended plan and sign up for a partner's product**

1. Sign in to the AWS Management Console using your delegated administrator or standalone account credentials.

1. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home).

1. In the navigation pane, choose **Management**, and then choose **Extended plan**.

1. For each partner solution that you want to sign up for, choose **View product**.

1. Review the product pricing details, and then choose **Subscribe** when you are ready to start the process of onboarding to the partner product.

1. After the subscription process completes, choose **Set up your account** to be redirected to the partner's sign-up page.

1. Provide the necessary information for the partner sign-up page, and follow the next steps, provided by the partner, for completing the onboarding steps.

**Important**  
You are not billed for the partner solution until you complete the onboarding process for the partner product.

## Unsubscribing from an Extended plan partner
<a name="securityhub-extended-plan-unsubscribe"></a>

 If you no longer want to use an Extended plan partner solution, you can unsubscribe from the partner listing. 

 To unsubscribe from a partner solution, follow the guidance at [Canceling your SaaS subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-subscription.html#cancel-saas-subscription) in the *AWS Marketplace Buyer Guide*. 

**Important**  
In addition to canceling your subscription, follow any additional offboarding steps that are required for the partner solution, based on how you configured the solution for your company.