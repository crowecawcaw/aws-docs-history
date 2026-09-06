

# Actions, resources, and condition keys for AWS Marketplace
<a name="list_marketplace-agreement"></a>

AWS Marketplace (service prefix: `aws-marketplace`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/marketplace/latest/buyerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/marketplace/latest/buyerguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json) for this service.

**Topics**
+ [API operations defined by AWS Marketplace](#list_marketplace-agreement-operations)
+ [Actions defined by AWS Marketplace](#list_marketplace-agreement-actions-as-permissions)
+ [Resource types defined by AWS Marketplace](#list_marketplace-agreement-resources-for-iam-policies)
+ [Condition keys for AWS Marketplace](#list_marketplace-agreement-policy-keys)

## API operations defined by AWS Marketplace
<a name="list_marketplace-agreement-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_marketplace-agreement-actions-as-permissions).




- **   AcceptAgreementCancellationRequest  **
  - **IAM action:**  [aws-marketplace:AcceptAgreementCancellationRequest](#list_marketplace-agreement-action-AcceptAgreementCancellationRequest)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-marketplace:CancelAgreement](#list_marketplace-agreement-action-CancelAgreement)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   AcceptAgreementPaymentRequest  **
  - **IAM action:**  [aws-marketplace:AcceptAgreementPaymentRequest](#list_marketplace-agreement-action-AcceptAgreementPaymentRequest)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-marketplace:UpdatePurchaseOrders](#list_marketplace-agreement-action-UpdatePurchaseOrders)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   AcceptAgreementRequest  **
  - **IAM action:**  [aws-marketplace:AcceptAgreementRequest](#list_marketplace-agreement-action-AcceptAgreementRequest)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-marketplace:Subscribe](#list_marketplace-agreement-action-Subscribe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-marketplace:UpdatePurchaseOrders](#list_marketplace-agreement-action-UpdatePurchaseOrders)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   BatchCreateBillingAdjustmentRequest  **
  - **IAM action:**  [aws-marketplace:BatchCreateBillingAdjustmentRequest](#list_marketplace-agreement-action-BatchCreateBillingAdjustmentRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelAgreement  **
  - **IAM action:**  [aws-marketplace:CancelAgreement](#list_marketplace-agreement-action-CancelAgreement)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-marketplace:Unsubscribe](#list_marketplace-agreement-action-Unsubscribe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CancelAgreementCancellationRequest  **
  - **IAM action:**  [aws-marketplace:CancelAgreementCancellationRequest](#list_marketplace-agreement-action-CancelAgreementCancellationRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelAgreementPaymentRequest  **
  - **IAM action:**  [aws-marketplace:CancelAgreementPaymentRequest](#list_marketplace-agreement-action-CancelAgreementPaymentRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAgreementRequest  **
  - **IAM action:**  [aws-marketplace:CreateAgreementRequest](#list_marketplace-agreement-action-CreateAgreementRequest)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-marketplace:Subscribe](#list_marketplace-agreement-action-Subscribe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DescribeAgreement  **
  - **IAM action:**  [aws-marketplace:DescribeAgreement](#list_marketplace-agreement-action-DescribeAgreement)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-marketplace:ViewSubscriptions](#list_marketplace-agreement-action-ViewSubscriptions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetAgreementCancellationRequest  **
  - **IAM action:**  [aws-marketplace:GetAgreementCancellationRequest](#list_marketplace-agreement-action-GetAgreementCancellationRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgreementEntitlements  **
  - **IAM action:**  [aws-marketplace:GetAgreementEntitlements](#list_marketplace-agreement-action-GetAgreementEntitlements)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-marketplace:ViewSubscriptions](#list_marketplace-agreement-action-ViewSubscriptions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetAgreementPaymentRequest  **
  - **IAM action:**  [aws-marketplace:GetAgreementPaymentRequest](#list_marketplace-agreement-action-GetAgreementPaymentRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgreementTerms  **
  - **IAM action:**  [aws-marketplace:GetAgreementTerms](#list_marketplace-agreement-action-GetAgreementTerms)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [aws-marketplace:ViewSubscriptions](#list_marketplace-agreement-action-ViewSubscriptions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetBillingAdjustmentRequest  **
  - **IAM action:**  [aws-marketplace:GetBillingAdjustmentRequest](#list_marketplace-agreement-action-GetBillingAdjustmentRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAgreementCancellationRequests  **
  - **IAM action:**  [aws-marketplace:ListAgreementCancellationRequests](#list_marketplace-agreement-action-ListAgreementCancellationRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAgreementCharges  **
  - **IAM action:**  [aws-marketplace:ListAgreementCharges](#list_marketplace-agreement-action-ListAgreementCharges) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAgreementInvoiceLineItems  **
  - **IAM action:**  [aws-marketplace:ListAgreementInvoiceLineItems](#list_marketplace-agreement-action-ListAgreementInvoiceLineItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAgreementPaymentRequests  **
  - **IAM action:**  [aws-marketplace:ListAgreementPaymentRequests](#list_marketplace-agreement-action-ListAgreementPaymentRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBillingAdjustmentRequests  **
  - **IAM action:**  [aws-marketplace:ListBillingAdjustmentRequests](#list_marketplace-agreement-action-ListBillingAdjustmentRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RejectAgreementCancellationRequest  **
  - **IAM action:**  [aws-marketplace:RejectAgreementCancellationRequest](#list_marketplace-agreement-action-RejectAgreementCancellationRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectAgreementPaymentRequest  **
  - **IAM action:**  [aws-marketplace:RejectAgreementPaymentRequest](#list_marketplace-agreement-action-RejectAgreementPaymentRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchAgreements  **
  - **IAM action:**  [aws-marketplace:SearchAgreements](#list_marketplace-agreement-action-SearchAgreements)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [aws-marketplace:ViewSubscriptions](#list_marketplace-agreement-action-ViewSubscriptions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   SendAgreementCancellationRequest  **
  - **IAM action:**  [aws-marketplace:SendAgreementCancellationRequest](#list_marketplace-agreement-action-SendAgreementCancellationRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendAgreementPaymentRequest  **
  - **IAM action:**  [aws-marketplace:SendAgreementPaymentRequest](#list_marketplace-agreement-action-SendAgreementPaymentRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePurchaseOrders  **
  - **IAM action:**  [aws-marketplace:UpdatePurchaseOrders](#list_marketplace-agreement-action-UpdatePurchaseOrders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Marketplace
<a name="list_marketplace-agreement-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AcceptAgreementApprovalRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to approve an incoming subscription request (for providers who provide products that require subscription verification) |  |   | Write | 
|   [AcceptAgreementCancellationRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to accept an agreement cancellation request |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | Write | 
|   [AcceptAgreementPaymentRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to accept a payment request |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | Write | 
|   [AcceptAgreementRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to accept an agreement request |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:ProductId](#list_marketplace-agreement-aws-marketplace_ProductId) | Write | 
|   [BatchCreateBillingAdjustmentRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to create a billing adjustment request against an agreement |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | Write | 
|   [CancelAgreement](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to cancel agreements |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType) | Write | 
|   [CancelAgreementCancellationRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to cancel a pending agreement cancellation request |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | Write | 
|   [CancelAgreementPaymentRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to cancel a payment request |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | Write | 
|   [CancelAgreementRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to cancel pending subscription requests for products that require subscription verification |  |   | Write | 
|   [CreateAgreementRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to create an agreement request |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:ProductId](#list_marketplace-agreement-aws-marketplace_ProductId) | Write | 
|   [DescribeAgreement](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to describe the metadata about the agreement |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | Read | 
|   [GetAgreementApprovalRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to view the details of incoming subscription requests (for providers who provide products that require subscription verification) |  |   | Read | 
|   [GetAgreementCancellationRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to view the details of an agreement cancellation request |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | Read | 
|   [GetAgreementEntitlements](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to get the entitlements associated with an agreement |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType) | Read | 
|   [GetAgreementPaymentRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to view details for a payment request |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | Read | 
|   [GetAgreementRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to view the details of subscription requests for data products that require subscription verification |  |   | Read | 
|   [GetAgreementTerms](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to get a list of terms for an agreement |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | List | 
|   [GetBillingAdjustmentRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to view the details of a billing adjustment request |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | Read | 
|   [ListAgreementApprovalRequests](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to list incoming subscription requests (for providers who provide products that require subscription verification) |  |   | List | 
|   [ListAgreementCancellationRequests](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to list agreement cancellation requests |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | List | 
|   [ListAgreementCharges](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to list charges associated with an agreement |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType) | List | 
|   [ListAgreementInvoiceLineItems](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to list invoice line items for an agreement |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | List | 
|   [ListAgreementPaymentRequests](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to list payment requests for an agreement |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | List | 
|   [ListAgreementRequests](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to list subscription requests for products that require subscription verification |  |   | List | 
|   [ListBillingAdjustmentRequests](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to list billing adjustment requests |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | List | 
|   [ListEntitlementDetails](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to list details of the entitlements associated with an agreement. Note that this action is not applicable to Marketplace purchases |  |   | Read | 
|   [RejectAgreementApprovalRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to decline an incoming subscription requests (for providers who provide products that require subscription verification) |  |   | Write | 
|   [RejectAgreementCancellationRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to reject an agreement cancellation request |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | Write | 
|   [RejectAgreementPaymentRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to reject a payment request |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | Write | 
|   [SearchAgreements](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to search agreements |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | List | 
|   [SendAgreementCancellationRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to send an agreement cancellation request |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | Write | 
|   [SendAgreementPaymentRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to send a payment request |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType)<br />[aws-marketplace:PartyType](#list_marketplace-agreement-aws-marketplace_PartyType) | Write | 
|   [Subscribe](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to subscribe to AWS Marketplace products. Includes the ability to send a subscription request for products that require subscription verification. Includes the ability to enable auto-renewal for an existing subscription |  |   | Write | 
|   [Unsubscribe](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to unsubscribe from AWS Marketplace products. Includes the ability to disable auto-renewal for an existing subscription |  |   | Write | 
|   [UpdateAgreementApprovalRequest](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to make changes to an incoming subscription request, including the ability to delete the prospective subscriber's information (for providers who provide products that require subscription verification) |  |   | Write | 
|   [UpdatePurchaseOrders](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to update purchase orders for charges associated with an agreement |  | [aws-marketplace:AgreementType](#list_marketplace-agreement-aws-marketplace_AgreementType) | Write | 
|   [ViewSubscriptions](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Grants permission to view account's subscriptions |  |   | List | 

## Resource types defined by AWS Marketplace
<a name="list_marketplace-agreement-resources-for-iam-policies"></a>

AWS Marketplace does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Marketplace
<a name="list_marketplace-agreement-policy-keys"></a>

AWS Marketplace defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws-marketplace:AgreementType](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Filters access by the type of the agreement | ArrayOfString | 
|   [aws-marketplace:PartyType](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Filters access by the party type of the agreement | String | 
|   [aws-marketplace:ProductId](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html)  | Filters access by product id for AWS Marketplace purchases | ArrayOfString | 