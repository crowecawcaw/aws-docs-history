

# Troubleshooting SaaS products

The following topics explain how to troubleshoot common SaaS product issues and error messages in AWS Marketplace. 

## Common SaaS error messages
<a name="common-saas-error-messages"></a>

The following table lists the most common SaaS error messages and their solutions.


| Error Message | Solution | 
| --- | --- | 
| Agreement creation failed due to seller compliance issues or an unsupported offer currency in your region. Contact the seller to ensure the correct offer is extended to you. | By design, AWS Marketplace prevents sellers from buying their own products. Please use a different account and allow list that account to your product for testing purposes.<br />For more information, see [Configuring SaaS product settings in AWS Marketplace](saas-product-settings.md). | 
| UsageBasedPricingTerm can't be updated until xxx-xx-xxT00:00:00Z because you have requested a price increase in the past 120 days. | Your product might have active subscriptions. Due to these active subscriptions, you need to wait for the effective change date to pass before modifying your listing. This is a standard procedure to ensure service continuity for your current subscribers.<br />If you have questions or need more help, contact the AWS Marketplace support team on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1) in the AWS Partner Central console. | 
| INVALID\_FULFILLMENT\_URL<br />Provide the correct format for the fulfillment URL. Begin with 'https://' | Make sure that the URL starts with `https://`.<br />Use 8 to 2,048 characters for the URL of a SaaS delivery option, and up to 500 characters for the fulfillment URL of an API-based agents and tools delivery option.<br />Validate URL format and accessibility<br />Test fulfillment endpoint before submission<br />Correct format: [https://your-saas-app.com/fulfillment](https://your-saas-app.com/fulfillment)<br />For more information, refer to [Configuring SaaS product settings in AWS Marketplace](saas-product-settings.md). | 
| You do not have sufficient permissions to access this page. | If you get this error when you choose the **Offers** tab in AWS Partner Central, make sure that you meet the [prerequisites for the tab](private-offer-faq.md#resolve-offers-tab-errors) in the [Private offer FAQ](private-offer-faq.md), earlier in this guide. | 
| INVALID\_MEDIA\_LOCATION | Ensure Amazon S3 URLs are accessible and properly formatted<br />https://s3.amazonaws.com/your-bucket/your-logo.png<br />Logo requirements:+ Format: PNG or JPG<br />+ Size: Up to 5 MB<br />+ Publicly accessible Amazon S3 location | 
| Remove unsupported characters | `¦`, `§`, `'`, `—`, `–`, `•`<br />Use standard ASCII characters in product descriptions<br />For more information, see [Providing metadata for AWS Marketplace products](categories-and-metadata.md) earlier in this guide. | 
| DUPLICATE\_SELLER\_ENTITY<br />A seller entity already exists for this account. | Check existing seller registration status<br />Use `UpdateSeller` instead of `CreateSeller` for modifications<br />Contact AWS Marketplace support if duplicate registration persists<br />For more information, refer to [Registration process](registration-process.md) earlier in this guide. | 
| SELLER\_ENTITLEMENT\_EXISTS<br />This principal already has entitlements to be a seller in AWS Marketplace. | Verify current seller status in AWS Partner Central<br />Use appropriate update operations instead of creation<br />Review IAM permissions and roles<br />For more information, refer to [Registration process](registration-process.md) earlier in this guide. | 
| UNSUPPORTED\_DELIVERY\_OPTION<br />The existing default URL-based SaaS products cannot be updated to use API delivery options. | Create new product for API-based delivery<br />Cannot convert between URL-based and API-based SaaS products<br />Plan product architecture before initial creation<br />You choose the delivery method when you add the product's first delivery option. On the **Add delivery option** page, for **Delivery method**, choose **SaaS** or **API-based agents and tools**. | 
| INCOMPATIBLE\_DELIVERY\_OPTION\_TYPES<br />You provided an `ApiDeliveryOption` for a product that already contains `SaaSUrlDeliveryOptions`. | Create separate products for different delivery types<br />Choose either API or URL-based delivery for **Delivery method** when you add the product's first delivery option.<br />Review product requirements before setup | 