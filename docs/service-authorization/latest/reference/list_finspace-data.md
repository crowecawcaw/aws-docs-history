

# Actions, resources, and condition keys for Amazon FinSpace API
<a name="list_finspace-data"></a>

Amazon FinSpace API (service prefix: `finspace-api`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/finspace/latest/data-api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/finspace/latest/userguide/temporary-credentials.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/finspace-api/finspace-api.json) for this service.

**Topics**
+ [API operations defined by Amazon FinSpace API](#list_finspace-data-operations)
+ [Actions defined by Amazon FinSpace API](#list_finspace-data-actions-as-permissions)
+ [Resource types defined by Amazon FinSpace API](#list_finspace-data-resources-for-iam-policies)
+ [Condition keys for Amazon FinSpace API](#list_finspace-data-policy-keys)

## API operations defined by Amazon FinSpace API
<a name="list_finspace-data-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_finspace-data-actions-as-permissions).




- **   GetProgrammaticAccessCredentials  **
  - **IAM action:**  [finspace-api:GetProgrammaticAccessCredentials](#list_finspace-data-action-GetProgrammaticAccessCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon FinSpace API
<a name="list_finspace-data-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [GetProgrammaticAccessCredentials](https://docs.aws.amazon.com/finspace/latest/data-api/API_GetProgrammaticAccessCredentials.html)  **
  - **Description:** Grants permission to retrieve FinSpace programmatic access credentials
  - **Resource types (\*required):** [credential\*](#list_finspace-data-resource-credential)
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by Amazon FinSpace API
<a name="list_finspace-data-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [credential](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html)  | arn:${Partition}:finspace-api:${Region}:${Account}:/credentials/programmatic |   | 

## Condition keys for Amazon FinSpace API
<a name="list_finspace-data-policy-keys"></a>

Amazon FinSpace API has no service-specific condition keys that can be used in the `Condition` element of policy statements.