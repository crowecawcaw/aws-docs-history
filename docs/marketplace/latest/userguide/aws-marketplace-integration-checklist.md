

# SaaS product integration checklist

Before your software as a service (SaaS) product becomes available to buyers in AWS Marketplace, you must verify that you have completed the required configuration. You can use the following SaaS integration checklist to verify that you have completed the required configurations.

If you list an Agentic Commerce product, the **Registration** rows, the **Billing Solution** rows about `BatchMeterUsage` and entitlements, and the **Subscription** rows about unsubscribe messages and final metering don't apply. Instead, verify the following:
+ You configured the key that signs your quotes, as a JSON Web Key Set (JWKS) URL or an AWS Key Management Service (AWS KMS) key, in the delivery option. For more information, see [Configuring your quote-signing key](agentic-commerce-signing-key.md).
+ A request to each endpoint that carries no payment returns HTTP 402 with an x402 quote that is signed by that key.
+ Before you serve a request, you verify the payment token's signature, `kid`, `iss` and `aud` claims, and expiration time. You also confirm that it carries a quote that you issued, reject your own quote tokens, and reject a token that was already used. For more information, see [Verifying payment tokens](agentic-commerce-verify-payment-tokens.md).
+ You don't send metering records for Agentic Commerce requests.


|  **Category**  |  **Requirements**  | 
| --- | --- | 
| Access  | Submitted a seller registration form with the desired AWS account for AWS Marketplace usage.  | 
| Access  | Completed the seller registration, including terms and conditions, bank account, and W8 or W9 tax form.  | 
| Access  | Configured cross-account roles for the registered AWS Marketplace account.  | 
| Product  | Created the product and completed the Provide product details card.  | 
| Product  | Provided AWS account IDs for testing. You add them in the Allowlisted AWS accounts section of the product's Settings tab. | 
| Product  | Provided the EULA for your product. You upload a .txt or .pdf file on the Configure legal terms and offer documents step of the public offer. To change it later, see [Update the end user license agreement (EULA)](saas-product-settings.md#saas-update-eula). | 
| Product  | Received your product code from AWS Marketplace.  | 
| Product  | Created an Amazon EventBridge rule for AWS Marketplace events with an Amazon SQS queue as the target. If you registered your seller account on or before July 15, 2026, you can instead subscribe an Amazon SQS queue to your Amazon SNS topic.  | 
| Billing Solution  | Validated you can send metering records to the BatchMeterUsage operation each hour for licenses across each customer for SaaS subscriptions products. Can send metering records for additional usage by each customer for SaaS contracts products.  | 
| Billing Solution  | Validated you can verify customer entitlements from the AWS Marketplace Entitlement Service for SaaS contracts products.  | 
| Billing Solution  | Validated that the costs appear as expected on bills generated for test accounts.  | 
| Billing Solution  | Tested for situations such as invalid customer IDs and canceled subscriptions.  | 
| Product  | Submitted the product to AWS Marketplace for review.  | 
| Registration  | Implemented an HTTPS registration page that can accept HTTP POST requests.  | 
| Registration  | Validated you can accept new customer registrations.  | 
| Registration  | Validated you are not storing the registration token in a cookie.  | 
| Registration  | Validated you are using ResolveCustomer to obtain the ProductCode, CustomerAWSAccountId, and LicenseArn from the AWS token.  | 
| Registration  | Validated you can resolve the registration token received from AWS with no delays.  | 
| Registration  | Tested that you aren't blocked from registering with email services addresses such as Gmail.  | 
| Registration  | Tested that you can accept incomplete registrations and multiple registration attempts.  | 
| Subscription  | Test that you can handle unsubscribe-pending and unsubscribe-success messages.  | 
| Subscription  | Validated that you send ﬁnal metering records within an hour of receiving an `unsubscribe-pending` message.  | 
| Security  | Validated the AWS root account doesn't have API keys, has a strong password, and is associated with a hardware multi-factor authentication (MFA) device. All administrative access is through identities created with AWS Identity and Access Management (IAM). No shared accounts.  | 
| Security  | Validated that IAM roles are used for all programmatic Amazon Elastic Compute Cloud (Amazon EC2) access. Credentials aren't hard-coded into scripts, headers, or source code.  | 
| Security  | Validated you maintain comprehensive logging and log consolidation.  | 
| Security  | Verified you have well-deﬁned public and private subnet boundaries that isolate application services and access to database and ﬁle systems. Distinct data class deﬁnitions that demarcate sensitive data and segregate public and private data.  | 
| Security  | Verified you have private data encryption in transit and at rest with scheduled key rotation.  | 
| Security  | Validated you have security incident tools and access in place and routinely scheduled incident response exercises that accommodate timely investigation and recovery.  | 
| Reliability  | Verified the system adapts to changes in demand, scaling up and down as required, and employs load balancing to ensure high performance. The system also provides edge-based caching as required.  | 
| Reliability  | Validated recovery time and point objectives are speciﬁed, and disaster recovery is scheduled at regular intervals. Component failure is self-healing via automated triggers and notiﬁcations.  | 