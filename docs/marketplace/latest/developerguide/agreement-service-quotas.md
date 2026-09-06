

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Service quotas for AWS Marketplace Agreement API
<a name="agreement-service-quotas"></a>

Your AWS account has the following quotas related to the AWS Marketplace Agreement Service.


**Request quotas**  

|  **API operation**  | **Request rate (per AWS account)** | 
| --- | --- | 
| AcceptAgreementCancellationRequest | 2 per second | 
| AcceptAgreementPaymentRequest | 5 per second | 
| AcceptAgreementRequest | 3 per second | 
| BatchCreateBillingAdjustmentRequest | 2 per second | 
| CancelAgreement | 3 per second | 
| CancelAgreementCancellationRequest | 2 per second | 
| CancelAgreementPaymentRequest | 5 per second | 
| CreateAgreementRequest | 4 per second | 
| DescribeAgreement | 5 per second | 
| GetAgreementCancellationRequest | 5 per second | 
| GetAgreementEntitlements | 10 per second | 
| GetAgreementPaymentRequest | 5 per second | 
| GetAgreementTerms | 10 per second | 
| GetBillingAdjustmentRequest | 5 per second | 
| ListAgreementCancellationRequests | 5 per second | 
| ListAgreementCharges | 15 per second | 
| ListAgreementInvoiceLineItems | 10 per second | 
| ListAgreementPaymentRequests | 5 per second | 
| ListBillingAdjustmentRequests | 5 per second | 
| RejectAgreementCancellationRequest | 2 per second | 
| RejectAgreementPaymentRequest | 5 per second | 
| SearchAgreements | 5 per second | 
| SendAgreementCancellationRequest | 2 per second | 
| SendAgreementPaymentRequest | 5 per second | 
| UpdatePurchaseOrders | 3 per second | 


**Agreement quotas**  

|  **Description**  | **Quota** | 
| --- | --- | 
| The maximum agreement value (in USD) that you can specify for targeted proposal. | $1B (or equivalent in requested currency) | 
| The maximum agreement value (in USD) that you can specify for general proposal. | $1M (or equivalent in requested currency) | 
| The maximum number of free trials allowed per resource per account. | 1 | 
| The maximum number of active agreements that you can create per resource per account. | 100 | 