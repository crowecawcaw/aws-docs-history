

# Actions, resources, and condition keys for AWS Management Console Mobile App
<a name="list_consoleapp"></a>

AWS Management Console Mobile App (service prefix: `consoleapp`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/what-is-consolemobileapp.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/permissions-policies.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/permissions-policies.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/consoleapp/consoleapp.json) for this service.

**Topics**
+ [Actions defined by AWS Management Console Mobile App](#list_consoleapp-actions-as-permissions)
+ [Resource types defined by AWS Management Console Mobile App](#list_consoleapp-resources-for-iam-policies)
+ [Condition keys for AWS Management Console Mobile App](#list_consoleapp-policy-keys)

## Actions defined by AWS Management Console Mobile App
<a name="list_consoleapp-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [GetDeviceIdentity](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/permissions-policies.html)  **
  - **Description:** Grants permission to retrieve the device identity for a Console Mobile App device
  - **Resource types (\*required):** [DeviceIdentity\*](#list_consoleapp-resource-DeviceIdentity)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDeviceIdentities](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/permissions-policies.html)  **
  - **Description:** Grants permission to retrieve a list of device identities
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List



## Resource types defined by AWS Management Console Mobile App
<a name="list_consoleapp-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [DeviceIdentity](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/permissions-policies.html)  | arn:${Partition}:consoleapp::${Account}:device/${DeviceId}/identity/${IdentityId} |   | 

## Condition keys for AWS Management Console Mobile App
<a name="list_consoleapp-policy-keys"></a>

AWS Management Console Mobile App has no service-specific condition keys that can be used in the `Condition` element of policy statements.