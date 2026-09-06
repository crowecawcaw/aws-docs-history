

# Actions, resources, and condition keys for AWS Control Catalog
<a name="list_controlcatalog"></a>

AWS Control Catalog (service prefix: `controlcatalog`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/controlcatalog/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/controlcatalog/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/controlcatalog/controlcatalog.json) for this service.

**Topics**
+ [API operations defined by AWS Control Catalog](#list_controlcatalog-operations)
+ [Actions defined by AWS Control Catalog](#list_controlcatalog-actions-as-permissions)
+ [Resource types defined by AWS Control Catalog](#list_controlcatalog-resources-for-iam-policies)
+ [Condition keys for AWS Control Catalog](#list_controlcatalog-policy-keys)

## API operations defined by AWS Control Catalog
<a name="list_controlcatalog-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_controlcatalog-actions-as-permissions).




- **   GetControl  **
  - **IAM action:**  [controlcatalog:GetControl](#list_controlcatalog-action-GetControl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [controltower:DescribeGuardrail](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListCommonControls  **
  - **IAM action:**  [controlcatalog:ListCommonControls](#list_controlcatalog-action-ListCommonControls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListControlMappings  **
  - **IAM action:**  [controlcatalog:ListControlMappings](#list_controlcatalog-action-ListControlMappings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListControls  **
  - **IAM action:**  [controlcatalog:ListControls](#list_controlcatalog-action-ListControls)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [controltower:ListGuardrails](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListDomains  **
  - **IAM action:**  [controlcatalog:ListDomains](#list_controlcatalog-action-ListDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListObjectives  **
  - **IAM action:**  [controlcatalog:ListObjectives](#list_controlcatalog-action-ListObjectives) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List



## Actions defined by AWS Control Catalog
<a name="list_controlcatalog-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [GetControl](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_GetControl.html)  **
  - **Description:** Grants permission to return details about a specific control
  - **Resource types (\*required):** [control\*](#list_controlcatalog-resource-control)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListCommonControls](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListCommonControls.html)  **
  - **Description:** Grants permission to return a paginated list of common controls from the AWS Control Catalog
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListControlMappings](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListControlMappings.html)  **
  - **Description:** Grants permission to return a paginated list of control mappings from the AWS Control Catalog
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListControls](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListControls.html)  **
  - **Description:** Grants permission to return a paginated list of all available controls in the AWS Control Catalog library
  - **Resource types (\*required):** [control\*](#list_controlcatalog-resource-control)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDomains](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html)  **
  - **Description:** Grants permission to return a paginated list of domains from the AWS Control Catalog
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListObjectives](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListObjectives.html)  **
  - **Description:** Grants permission to return a paginated list of objectives from the AWS Control Catalog
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List



## Resource types defined by AWS Control Catalog
<a name="list_controlcatalog-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [common-control](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_CommonControlSummary.html)  | arn:${Partition}:controlcatalog:::common-control/${CommonControlId} |   | 
|  [control](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ControlSummary.html)  | arn:${Partition}:controlcatalog:::control/${ControlId} |   | 
|  [domain](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_DomainSummary.html)  | arn:${Partition}:controlcatalog:::domain/${DomainId} |   | 
|  [objective](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ObjectiveSummary.html)  | arn:${Partition}:controlcatalog:::objective/${ObjectiveId} |   | 

## Condition keys for AWS Control Catalog
<a name="list_controlcatalog-policy-keys"></a>

AWS Control Catalog has no service-specific condition keys that can be used in the `Condition` element of policy statements.