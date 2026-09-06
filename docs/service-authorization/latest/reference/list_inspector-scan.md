

# Actions, resources, and condition keys for Amazon InspectorScan
<a name="list_inspector-scan"></a>

Amazon InspectorScan (service prefix: `inspector-scan`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/inspector/v2/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/inspector/latest/user/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/inspector-scan/inspector-scan.json) for this service.

**Topics**
+ [API operations defined by Amazon InspectorScan](#list_inspector-scan-operations)
+ [Actions defined by Amazon InspectorScan](#list_inspector-scan-actions-as-permissions)
+ [Resource types defined by Amazon InspectorScan](#list_inspector-scan-resources-for-iam-policies)
+ [Condition keys for Amazon InspectorScan](#list_inspector-scan-policy-keys)

## API operations defined by Amazon InspectorScan
<a name="list_inspector-scan-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_inspector-scan-actions-as-permissions).




- **   ScanSbom  **
  - **IAM action:**  [inspector-scan:ScanSbom](#list_inspector-scan-action-ScanSbom) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon InspectorScan
<a name="list_inspector-scan-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [ScanSbom](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ScanSbom.html)  | Grants permission to scan the customer provided SBOM and return vulnerabilities detected within |  |   | Read | 

## Resource types defined by Amazon InspectorScan
<a name="list_inspector-scan-resources-for-iam-policies"></a>

Amazon InspectorScan does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon InspectorScan
<a name="list_inspector-scan-policy-keys"></a>

Amazon InspectorScan has no service-specific condition keys that can be used in the `Condition` element of policy statements.