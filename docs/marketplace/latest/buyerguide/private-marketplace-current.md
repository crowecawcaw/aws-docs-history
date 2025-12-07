# Private Marketplace

With Private Marketplace, you control what users in your organization can procure from AWS Marketplace. Administrators can provide customized procurement experiences with curated catalogs of approved products to different audiences in your organization. Private Marketplace integrates with [AWS Organizations](https://aws.amazon.com/organizations "https://aws.amazon.com/organizations"), a service that helps you manage all your AWS accounts in one place.

You can create multiple experiences to govern your entire organization, AWS organizational units (OUs), or AWS accounts and adjust your procurement controls as your business needs change. If you update your organization structure within AWS Organizations, Private Marketplace updates the governance accordingly. You can also add company branding to each experience with a custom name and messaging that gives users more information about their procurement experience.

After you set up governing experiences using Private Marketplace, users in your organization can buy and deploy only vetted products that comply with your organization's policies and standards. They can browse the entire AWS Marketplace catalog and request additional products. Administrators can view user requests and approve or decline these requests. Private Marketplace publishes Amazon EventBridge events when users create requests and when administrators approve or decline these requests. To streamline the approval process and receive timely updates, administrators and users can set up email notifications for these events. For more information, see [Private Marketplace notifications](configuring-notifications.md "configuring-notifications.md").

###### Note

The legacy version of Private Marketplace will be deprecated on March 17, 2026. To use the current version, an administrator in the management account of your AWS Organizations must create an integration for Private Marketplace. To check integration status, see [Viewing Private Marketplace settings](view-private-marketplace-settings.md "view-private-marketplace-settings.md").

## Products governed by Private Marketplace

All products that require AWS Marketplace subscriptions will be governed by Private Marketplace. Keep in mind the following important exceptions and considerations:

- Any Amazon Bedrock model where automatic access has been enabled by Amazon Bedrock will not be governed by Private Marketplace. This currently includes serverless models and models from AWS. Refer to the [Amazon Bedrock User Guide](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md") for latest information.
- As customers are already entitled to products whose EULAs are governed by the AWS Customer Agreement or other agreement with AWS governing use of AWS services, you cannot control subscriptions to such products using Private Marketplace. Hence, such products are not included in the list that you approve within your Private Marketplace experiences.
- If your organization already has subscriptions to products in AWS Marketplace, Private Marketplace will not block usage from these existing subscriptions. Users will not be blocked from launching new instances from existing subscriptions. Private Marketplace will only block new subscriptions or changes to existing subscriptions to products that are not approved in the experience that is governing the user.
- Private Marketplace does not control what can be deployed in AWS accounts. If you want to control what can be deployed including products that are automatically entitled, consider other services such as [AWS Service Catalog](../../../servicecatalog/latest/adminguide/introduction.md "../../../servicecatalog/latest/adminguide/introduction.md").
