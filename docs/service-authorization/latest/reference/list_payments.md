

# Actions, resources, and condition keys for AWS Payments
<a name="list_payments"></a>

AWS Payments (service prefix: `payments`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/payments/payments.json) for this service.

**Topics**
+ [Actions defined by AWS Payments](#list_payments-actions-as-permissions)
+ [Permission-only actions for AWS Payments](#list_payments-permission-only-actions)
+ [Resource types defined by AWS Payments](#list_payments-resources-for-iam-policies)
+ [Condition keys for AWS Payments](#list_payments-policy-keys)

## Actions defined by AWS Payments
<a name="list_payments-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptFinancingApplicationTerms](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  **
  - **Description:** Grants permission to accept financing application terms provided by a lender
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateFinancingApplication](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  **
  - **Description:** Grants permission to create a financing application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreatePaymentInstrument](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  **
  - **Description:** Grants permission to create a payment instrument
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_payments-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_payments-aws_TagKeys)
  - **Access level:** Write

- **   [GetFinancingApplication](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  **
  - **Description:** Grants permission to get information about a financing application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFinancingLine](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  **
  - **Description:** Grants permission to get information about a financing line
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFinancingLineWithdrawal](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  **
  - **Description:** Grants permission to get information about a financing line withdrawal
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFinancingOption](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  **
  - **Description:** Grants permission to get information about a financing option
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPaymentInstrument](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  **
  - **Description:** Grants permission to get information about a payment instrument
  - **Resource types (\*required):** [payment-instrument](#list_payments-resource-payment-instrument)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payments-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFinancingApplications](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  **
  - **Description:** Grants permission to list financing application metadata
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFinancingLineWithdrawals](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  **
  - **Description:** Grants permission to list financing line withdrawals metadata
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFinancingLines](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  **
  - **Description:** Grants permission to list financing line metadata
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPaymentProgramOptions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  **
  - **Description:** Grants permission to list information about payment options
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPaymentProgramStatus](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  **
  - **Description:** Grants permission to list information about payment program eligibility and enrolment status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  **
  - **Description:** Grants permission to list tags on a payment resource
  - **Resource types (\*required):** [payment-instrument](#list_payments-resource-payment-instrument)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payments-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  **
  - **Description:** Grants permission to tag a payment resource
  - **Resource types (\*required):** [payment-instrument](#list_payments-resource-payment-instrument)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_payments-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_payments-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_payments-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  **
  - **Description:** Grants permission to untag a payment resource
  - **Resource types (\*required):** [payment-instrument](#list_payments-resource-payment-instrument)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_payments-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_payments-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateFinancingApplication](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  **
  - **Description:** Grants permission to update a financing application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for AWS Payments
<a name="list_payments-permission-only-actions"></a>

The following actions are defined by AWS Payments but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [DeletePaymentInstrument](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to delete a payment instrument |  |   | Write | 
|   [GetPaymentStatus](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to get payment status of invoices |  |   | Read | 
|   [ListPaymentInstruments](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to list payment instrument metadata |  |   | List | 
|   [ListPaymentPreferences](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to get payment preferences (preferred payment currency, preferred payment method, etc.) |  |   | List | 
|   [MakePayment](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to make a payment, authenticate a payment, verify a payment method, and generate a funding request document for Advance Pay |  |   | Write | 
|   [UpdatePaymentInstrument](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to update a payment instrument |  |   | Write | 
|   [UpdatePaymentPreferences](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to update payment preferences (preferred payment currency, preferred payment method, etc.) |  |   | Write | 

## Resource types defined by AWS Payments
<a name="list_payments-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [payment-instrument](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  | arn:${Partition}:payments::${Account}:payment-instrument:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_payments-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Payments
<a name="list_payments-policy-keys"></a>

AWS Payments defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 