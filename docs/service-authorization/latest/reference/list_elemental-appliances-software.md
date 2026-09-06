

# Actions, resources, and condition keys for AWS Elemental Appliances and Software
<a name="list_elemental-appliances-software"></a>

AWS Elemental Appliances and Software (service prefix: `elemental-appliances-software`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/elemental-appliances-software/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/elemental-appliances-software/latest/ug/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/elemental-appliances-software/latest/ug/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/elemental-appliances-software/elemental-appliances-software.json) for this service.

**Topics**
+ [Actions defined by AWS Elemental Appliances and Software](#list_elemental-appliances-software-actions-as-permissions)
+ [Permission-only actions for AWS Elemental Appliances and Software](#list_elemental-appliances-software-permission-only-actions)
+ [Resource types defined by AWS Elemental Appliances and Software](#list_elemental-appliances-software-resources-for-iam-policies)
+ [Condition keys for AWS Elemental Appliances and Software](#list_elemental-appliances-software-policy-keys)

## Actions defined by AWS Elemental Appliances and Software
<a name="list_elemental-appliances-software-actions-as-permissions"></a>

AWS Elemental Appliances and Software has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS Elemental Appliances and Software
<a name="list_elemental-appliances-software-permission-only-actions"></a>

The following actions are defined by AWS Elemental Appliances and Software but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CompleteUpload](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to complete an upload of an attachment for a quote or order
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateOrderV1](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to create an order
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateQuote](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to create a quote
  - **Resource types (\*required):** [quote\*](#list_elemental-appliances-software-resource-quote)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAvsCorrectAddress](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to validate an address
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetBillingAddresses](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to list the billing addresses in the AWS Account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDeliveryAddressesV2](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to list the delivery addresses in the AWS Account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOrder](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to describe an order
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOrdersV2](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to list the orders in the AWS Account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetQuote](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to describe a quote
  - **Resource types (\*required):** [quote\*](#list_elemental-appliances-software-resource-quote)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTaxes](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to calculate taxes for an order
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListQuotes](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to list the quotes in the AWS Account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartUpload](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to start an upload of an attachment for a quote or order
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SubmitOrderV1](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to submit an order
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateQuote](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to modify a quote
  - **Resource types (\*required):** [quote\*](#list_elemental-appliances-software-resource-quote)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Elemental Appliances and Software
<a name="list_elemental-appliances-software-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [quote](https://docs.aws.amazon.com/elemental-appliances-software)  | arn:${Partition}:elemental-appliances-software:${Region}:${Account}:quote/${ResourceId} |   | 

## Condition keys for AWS Elemental Appliances and Software
<a name="list_elemental-appliances-software-policy-keys"></a>

AWS Elemental Appliances and Software has no service-specific condition keys that can be used in the `Condition` element of policy statements.