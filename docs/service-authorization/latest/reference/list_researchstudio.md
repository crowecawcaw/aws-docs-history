

# Actions, resources, and condition keys for Amazon Bio Discovery

Amazon Bio Discovery (service prefix: `researchstudio`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/researchstudio/latest/userguide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/researchstudio/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/researchstudio/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/researchstudio/researchstudio.json) for this service.

**Topics**
+ [Actions defined by Amazon Bio Discovery](#list_researchstudio-actions-as-permissions)
+ [Resource types defined by Amazon Bio Discovery](#list_researchstudio-resources-for-iam-policies)
+ [Condition keys for Amazon Bio Discovery](#list_researchstudio-policy-keys)

## Actions defined by Amazon Bio Discovery
<a name="list_researchstudio-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. For each action, the table lists the resource types and condition keys supported by that action. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AssignPrincipal](https://docs.aws.amazon.com/researchstudio/latest/APIReference/API_AssignPrincipal.html)  | Grants permission to assign a principal to a Bio Discovery application |  |   | Write | 
|   [CreateApplication](https://docs.aws.amazon.com/researchstudio/latest/APIReference/API_CreateApplication.html)  | Grants permission to create a Bio Discovery application |  |   | Write | 
|   [DeleteApplication](https://docs.aws.amazon.com/researchstudio/latest/APIReference/API_DeleteApplication.html)  | Grants permission to delete a Bio Discovery application |  |   | Write | 
|   [DeletePrincipal](https://docs.aws.amazon.com/researchstudio/latest/APIReference/API_DeletePrincipal.html)  | Grants permission to remove a principal from a Bio Discovery application |  |   | Write | 
|   [GetApplication](https://docs.aws.amazon.com/researchstudio/latest/APIReference/API_GetApplication.html)  | Grants permission to retrieve the details of a Bio Discovery application |  |   | Read | 
|   [ListApplications](https://docs.aws.amazon.com/researchstudio/latest/APIReference/API_ListApplications.html)  | Grants permission to list the Bio Discovery applications in an account |  |   | List | 
|   [UpdateApplication](https://docs.aws.amazon.com/researchstudio/latest/APIReference/API_UpdateApplication.html)  | Grants permission to update a Bio Discovery application |  |   | Write | 

## Resource types defined by Amazon Bio Discovery
<a name="list_researchstudio-resources-for-iam-policies"></a>

Amazon Bio Discovery does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon Bio Discovery
<a name="list_researchstudio-policy-keys"></a>

Amazon Bio Discovery has no service-specific condition keys that can be used in the `Condition` element of policy statements.