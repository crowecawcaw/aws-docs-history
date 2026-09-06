

# Actions, resources, and condition keys for Amazon Route 53 Domains
<a name="list_route53domains"></a>

Amazon Route 53 Domains (service prefix: `route53domains`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/Route53/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/route53domains/route53domains.json) for this service.

**Topics**
+ [API operations defined by Amazon Route 53 Domains](#list_route53domains-operations)
+ [Actions defined by Amazon Route 53 Domains](#list_route53domains-actions-as-permissions)
+ [Resource types defined by Amazon Route 53 Domains](#list_route53domains-resources-for-iam-policies)
+ [Condition keys for Amazon Route 53 Domains](#list_route53domains-policy-keys)

## API operations defined by Amazon Route 53 Domains
<a name="list_route53domains-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_route53domains-actions-as-permissions).




- **   AcceptDomainTransferFromAnotherAwsAccount  **
  - **IAM action:**  [route53domains:AcceptDomainTransferFromAnotherAwsAccount](#list_route53domains-action-AcceptDomainTransferFromAnotherAwsAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateDelegationSignerToDomain  **
  - **IAM action:**  [route53domains:AssociateDelegationSignerToDomain](#list_route53domains-action-AssociateDelegationSignerToDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelDomainTransferToAnotherAwsAccount  **
  - **IAM action:**  [route53domains:CancelDomainTransferToAnotherAwsAccount](#list_route53domains-action-CancelDomainTransferToAnotherAwsAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CheckDomainAvailability  **
  - **IAM action:**  [route53domains:CheckDomainAvailability](#list_route53domains-action-CheckDomainAvailability) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CheckDomainTransferability  **
  - **IAM action:**  [route53domains:CheckDomainTransferability](#list_route53domains-action-CheckDomainTransferability) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DeleteDomain  **
  - **IAM action:**  [route53domains:DeleteDomain](#list_route53domains-action-DeleteDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTagsForDomain  **
  - **IAM action:**  [route53domains:DeleteTagsForDomain](#list_route53domains-action-DeleteTagsForDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DisableDomainAutoRenew  **
  - **IAM action:**  [route53domains:DisableDomainAutoRenew](#list_route53domains-action-DisableDomainAutoRenew) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableDomainTransferLock  **
  - **IAM action:**  [route53domains:DisableDomainTransferLock](#list_route53domains-action-DisableDomainTransferLock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateDelegationSignerFromDomain  **
  - **IAM action:**  [route53domains:DisassociateDelegationSignerFromDomain](#list_route53domains-action-DisassociateDelegationSignerFromDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableDomainAutoRenew  **
  - **IAM action:**  [route53domains:EnableDomainAutoRenew](#list_route53domains-action-EnableDomainAutoRenew) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableDomainTransferLock  **
  - **IAM action:**  [route53domains:EnableDomainTransferLock](#list_route53domains-action-EnableDomainTransferLock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetContactReachabilityStatus  **
  - **IAM action:**  [route53domains:GetContactReachabilityStatus](#list_route53domains-action-GetContactReachabilityStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainDetail  **
  - **IAM action:**  [route53domains:GetDomainDetail](#list_route53domains-action-GetDomainDetail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainSuggestions  **
  - **IAM action:**  [route53domains:GetDomainSuggestions](#list_route53domains-action-GetDomainSuggestions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOperationDetail  **
  - **IAM action:**  [route53domains:GetOperationDetail](#list_route53domains-action-GetOperationDetail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDomains  **
  - **IAM action:**  [route53domains:ListDomains](#list_route53domains-action-ListDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOperations  **
  - **IAM action:**  [route53domains:ListOperations](#list_route53domains-action-ListOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPrices  **
  - **IAM action:**  [route53domains:ListPrices](#list_route53domains-action-ListPrices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForDomain  **
  - **IAM action:**  [route53domains:ListTagsForDomain](#list_route53domains-action-ListTagsForDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PushDomain  **
  - **IAM action:**  [route53domains:PushDomain](#list_route53domains-action-PushDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterDomain  **
  - **IAM action:**  [route53domains:RegisterDomain](#list_route53domains-action-RegisterDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53:CreateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RejectDomainTransferFromAnotherAwsAccount  **
  - **IAM action:**  [route53domains:RejectDomainTransferFromAnotherAwsAccount](#list_route53domains-action-RejectDomainTransferFromAnotherAwsAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RenewDomain  **
  - **IAM action:**  [route53domains:RenewDomain](#list_route53domains-action-RenewDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResendContactReachabilityEmail  **
  - **IAM action:**  [route53domains:ResendContactReachabilityEmail](#list_route53domains-action-ResendContactReachabilityEmail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResendOperationAuthorization  **
  - **IAM action:**  [route53domains:ResendOperationAuthorization](#list_route53domains-action-ResendOperationAuthorization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RetrieveDomainAuthCode  **
  - **IAM action:**  [route53domains:RetrieveDomainAuthCode](#list_route53domains-action-RetrieveDomainAuthCode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TransferDomain  **
  - **IAM action:**  [route53domains:TransferDomain](#list_route53domains-action-TransferDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TransferDomainToAnotherAwsAccount  **
  - **IAM action:**  [route53domains:TransferDomainToAnotherAwsAccount](#list_route53domains-action-TransferDomainToAnotherAwsAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDomainContact  **
  - **IAM action:**  [route53domains:UpdateDomainContact](#list_route53domains-action-UpdateDomainContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDomainContactPrivacy  **
  - **IAM action:**  [route53domains:UpdateDomainContactPrivacy](#list_route53domains-action-UpdateDomainContactPrivacy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDomainNameservers  **
  - **IAM action:**  [route53domains:UpdateDomainNameservers](#list_route53domains-action-UpdateDomainNameservers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTagsForDomain  **
  - **IAM action:**  [route53domains:UpdateTagsForDomain](#list_route53domains-action-UpdateTagsForDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ViewBilling  **
  - **IAM action:**  [route53domains:ViewBilling](#list_route53domains-action-ViewBilling) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon Route 53 Domains
<a name="list_route53domains-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AcceptDomainTransferFromAnotherAwsAccount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AcceptDomainTransferFromAnotherAwsAccount.html)  | Grants permission to accept the transfer of a domain from another AWS account to the current AWS account |  |   | Write | 
|   [AssociateDelegationSignerToDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AssociateDelegationSignerToDomain.html)  | Grants permission to associate a new delegation signer to a domain |  |   | Write | 
|   [CancelDomainTransferToAnotherAwsAccount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_CancelDomainTransferToAnotherAwsAccount.html)  | Grants permission to cancel the transfer of a domain from the current AWS account to another AWS account |  |   | Write | 
|   [CheckDomainAvailability](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_CheckDomainAvailability.html)  | Grants permission to check the availability of one domain name |  |   | Read | 
|   [CheckDomainTransferability](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_CheckDomainTransferability.html)  | Grants permission to check whether a domain name can be transferred to Amazon Route 53 |  |   | Read | 
|   [DeleteDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DeleteDomain.html)  | Grants permission to delete domains |  |   | Write | 
|   [DeleteTagsForDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DeleteTagsForDomain.html)  | Grants permission to delete the specified tags for a domain |  |   | Tagging, Write | 
|   [DisableDomainAutoRenew](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DisableDomainAutoRenew.html)  | Grants permission to configure Amazon Route 53 to automatically renew the specified domain before the domain registration expires |  |   | Write | 
|   [DisableDomainTransferLock](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DisableDomainTransferLock.html)  | Grants permission to remove the transfer lock on the domain (specifically the clientTransferProhibited status) to allow domain transfers |  |   | Write | 
|   [DisassociateDelegationSignerFromDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DisassociateDelegationSignerFromDomain.html)  | Grants permission to disassociate an existing delegation signer from a domain |  |   | Write | 
|   [EnableDomainAutoRenew](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DisableDomainAutoRenew.html)  | Grants permission to configure Amazon Route 53 to automatically renew the specified domain before the domain registration expires |  |   | Write | 
|   [EnableDomainTransferLock](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_EnableDomainTransferLock.html)  | Grants permission to set the transfer lock on the domain (specifically the clientTransferProhibited status) to prevent domain transfers |  |   | Write | 
|   [GetContactReachabilityStatus](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetContactReachabilityStatus.html)  | Grants permission to get information about whether the registrant contact has responded for operations that require confirmation that the email address for the registrant contact is valid, such as registering a new domain |  |   | Read | 
|   [GetDomainDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetDomainDetail.html)  | Grants permission to get detailed information about a domain |  |   | Read | 
|   [GetDomainSuggestions](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetDomainSuggestions.html)  | Grants permission to get a list of suggested domain names given a string, which can either be a domain name or simply a word or phrase (without spaces) |  |   | Read | 
|   [GetOperationDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html)  | Grants permission to get the current status of an operation that is not completed |  |   | Read | 
|   [ListDomains](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListDomains.html)  | Grants permission to list all the domain names registered with Amazon Route 53 for the current AWS account |  |   | List | 
|   [ListOperations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListOperations.html)  | Grants permission to list the operation IDs of operations that are not yet complete |  |   | List | 
|   [ListPrices](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListPrices.html)  | Grants permission to list the prices of operations for TLDs |  |   | List | 
|   [ListTagsForDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListTagsForDomain.html)  | Grants permission to list all the tags that are associated with the specified domain |  |   | Read | 
|   [PushDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_PushDomain.html)  | Grants permission to change the IPS tag of .uk domain to initiate a transfer process from Route 53 to another registrar |  |   | Write | 
|   [RegisterDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RegisterDomain.html)  | Grants permission to register domains |  |   | Write | 
|   [RejectDomainTransferFromAnotherAwsAccount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RejectDomainTransferFromAnotherAwsAccount.html)  | Grants permission to reject the transfer of a domain from another AWS account to the current AWS account |  |   | Write | 
|   [RenewDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RenewDomain.html)  | Grants permission to renew domains for the specified number of years |  |   | Write | 
|   [ResendContactReachabilityEmail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ResendContactReachabilityEmail.html)  | Grants permission to resend the confirmation email to the current email address for the registrant contact for operations that require confirmation that the email address for the registrant contact is valid, such as registering a new domain |  |   | Write | 
|   [ResendOperationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ResendOperationAuthorization.html)  | Grants permission to resend the operation authorization |  |   | Write | 
|   [RetrieveDomainAuthCode](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RetrieveDomainAuthCode.html)  | Grants permission to get the AuthCode for the domain |  |   | Write | 
|   [TransferDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomain.html)  | Grants permission to transfer a domain from another registrar to Amazon Route 53 |  |   | Write | 
|   [TransferDomainToAnotherAwsAccount](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html)  | Grants permission to transfer a domain from the current AWS account to another AWS account |  |   | Write | 
|   [UpdateDomainContact](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainContact.html)  | Grants permission to update the contact information for domain |  |   | Write | 
|   [UpdateDomainContactPrivacy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainContactPrivacy.html)  | Grants permission to update the domain contact privacy setting |  |   | Write | 
|   [UpdateDomainNameservers](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainNameservers.html)  | Grants permission to replace the current set of name servers for a domain with the specified set of name servers |  |   | Write | 
|   [UpdateTagsForDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateTagsForDomain.html)  | Grants permission to add or update tags for a specified domain |  |   | Tagging, Write | 
|   [ViewBilling](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ViewBilling.html)  | Grants permission to get all the domain-related billing records for the current AWS account for a specified period |  |   | Read | 

## Resource types defined by Amazon Route 53 Domains
<a name="list_route53domains-resources-for-iam-policies"></a>

Amazon Route 53 Domains does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon Route 53 Domains
<a name="list_route53domains-policy-keys"></a>

Amazon Route 53 Domains has no service-specific condition keys that can be used in the `Condition` element of policy statements.