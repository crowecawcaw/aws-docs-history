

# Actions, resources, and condition keys for AWS Sustainability
<a name="list_sustainability"></a>

AWS Sustainability (service prefix: `sustainability`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/sustainability/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/sustainability/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sustainability/sustainability.json) for this service.

**Topics**
+ [API operations defined by AWS Sustainability](#list_sustainability-operations)
+ [Actions defined by AWS Sustainability](#list_sustainability-actions-as-permissions)
+ [Resource types defined by AWS Sustainability](#list_sustainability-resources-for-iam-policies)
+ [Condition keys for AWS Sustainability](#list_sustainability-policy-keys)

## API operations defined by AWS Sustainability
<a name="list_sustainability-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_sustainability-actions-as-permissions).




- **   GetEstimatedCarbonEmissions  **
  - **IAM action:**  [sustainability:GetEstimatedCarbonEmissions](#list_sustainability-action-GetEstimatedCarbonEmissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEstimatedCarbonEmissionsDimensionValues  **
  - **IAM action:**  [sustainability:GetEstimatedCarbonEmissionsDimensionValues](#list_sustainability-action-GetEstimatedCarbonEmissionsDimensionValues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEstimatedWaterAllocation  **
  - **IAM action:**  [sustainability:GetEstimatedWaterAllocation](#list_sustainability-action-GetEstimatedWaterAllocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEstimatedWaterAllocationDimensionValues  **
  - **IAM action:**  [sustainability:GetEstimatedWaterAllocationDimensionValues](#list_sustainability-action-GetEstimatedWaterAllocationDimensionValues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS Sustainability
<a name="list_sustainability-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetCarbonFootprintSummary](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create-standard.html)  | Grants permission to access carbon footprint data from AWS Data Exports |  |   | Read | 
|   [GetEstimatedCarbonEmissions](https://docs.aws.amazon.com/sustainability/latest/APIReference/API_GetEstimatedCarbonEmissions.html)  | Grants permission to view estimated carbon emission values based on customer grouping and filtering parameters |  |   | Read | 
|   [GetEstimatedCarbonEmissionsDimensionValues](https://docs.aws.amazon.com/sustainability/latest/APIReference/API_GetEstimatedCarbonEmissionsDimensionValues.html)  | Grants permission to view the possible dimension values available for the estimated carbon emission values |  |   | Read | 
|   [GetEstimatedWaterAllocation](https://docs.aws.amazon.com/sustainability/latest/APIReference/API_GetEstimatedWaterAllocation.html)  | Grants permission to view estimated water allocation values based on customer grouping and filtering parameters |  |   | Read | 
|   [GetEstimatedWaterAllocationDimensionValues](https://docs.aws.amazon.com/sustainability/latest/APIReference/API_GetEstimatedWaterAllocationDimensionValues.html)  | Grants permission to view the possible dimension values available for the estimated water allocation values |  |   | Read | 

## Resource types defined by AWS Sustainability
<a name="list_sustainability-resources-for-iam-policies"></a>

AWS Sustainability does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Sustainability
<a name="list_sustainability-policy-keys"></a>

AWS Sustainability has no service-specific condition keys that can be used in the `Condition` element of policy statements.