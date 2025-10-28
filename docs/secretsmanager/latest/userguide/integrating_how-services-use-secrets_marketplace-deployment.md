# AWS Marketplace

When you use AWS Marketplace Quick Launch, AWS Marketplace distributes your software
along with the license key. AWS Marketplace stores the license key in your account as a
Secrets Manager [managed secret](service-linked-secrets.md "service-linked-secrets.md"). The cost of storing the
secret is included with the charges for AWS Marketplace. To update the secret, you must use
AWS Marketplace rather than Secrets Manager. For more information, see [Configure
Quick Launch](../../../marketplace/latest/userguide/saas-product-settings.md#saas-quick-launch "../../../marketplace/latest/userguide/saas-product-settings.md#saas-quick-launch") in the _AWS Marketplace Seller Guide_.
