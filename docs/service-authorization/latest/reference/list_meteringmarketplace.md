

# Actions, resources, and condition keys for AWS Marketplace Metering Service
<a name="list_meteringmarketplace"></a>

AWS Marketplace Metering Service (service prefix: `aws-marketplace`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/marketplace/latest/APIReference/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/marketplace/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/marketplace/latest/userguide/iam-user-policy-for-aws-marketplace-actions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json) for this service.

**Topics**
+ [API operations defined by AWS Marketplace Metering Service](#list_meteringmarketplace-operations)
+ [Actions defined by AWS Marketplace Metering Service](#list_meteringmarketplace-actions-as-permissions)
+ [Resource types defined by AWS Marketplace Metering Service](#list_meteringmarketplace-resources-for-iam-policies)
+ [Condition keys for AWS Marketplace Metering Service](#list_meteringmarketplace-policy-keys)

## API operations defined by AWS Marketplace Metering Service
<a name="list_meteringmarketplace-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_meteringmarketplace-actions-as-permissions).




- **   BatchMeterUsage  **
  - **IAM action:**  [aws-marketplace:BatchMeterUsage](#list_meteringmarketplace-action-BatchMeterUsage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   MeterUsage  **
  - **IAM action:**  [aws-marketplace:MeterUsage](#list_meteringmarketplace-action-MeterUsage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterUsage  **
  - **IAM action:**  [aws-marketplace:RegisterUsage](#list_meteringmarketplace-action-RegisterUsage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResolveCustomer  **
  - **IAM action:**  [aws-marketplace:ResolveCustomer](#list_meteringmarketplace-action-ResolveCustomer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Marketplace Metering Service
<a name="list_meteringmarketplace-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [BatchMeterUsage](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_BatchMeterUsage.html)  | Grants permission to post metering records for a set of customers for SaaS applications |  |   | Write | 
|   [MeterUsage](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_MeterUsage.html)  | Grants permission to emit metering records |  |   | Write | 
|   [RegisterUsage](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_RegisterUsage.html)  | Grants permission to to verify that the customer running your paid software is subscribed to your product on AWS Marketplace, enabling you to guard against unauthorized use. Meters software use per ECS task, per hour, with usage prorated to the second |  |   | Write | 
|   [ResolveCustomer](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_ResolveCustomer.html)  | Grants permission to resolve a registration token to obtain a CustomerIdentifier and product code |  |   | Write | 

## Resource types defined by AWS Marketplace Metering Service
<a name="list_meteringmarketplace-resources-for-iam-policies"></a>

AWS Marketplace Metering Service does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Marketplace Metering Service
<a name="list_meteringmarketplace-policy-keys"></a>

AWS Marketplace Metering Service has no service-specific condition keys that can be used in the `Condition` element of policy statements.