

# Actions, resources, and condition keys for AWS Control Tower
<a name="list_controltower"></a>

AWS Control Tower (service prefix: `controltower`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/controltower/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/controltower/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/controltower/latest/userguide/auth-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/controltower/controltower.json) for this service.

**Topics**
+ [API operations defined by AWS Control Tower](#list_controltower-operations)
+ [Actions defined by AWS Control Tower](#list_controltower-actions-as-permissions)
+ [Permission-only actions for AWS Control Tower](#list_controltower-permission-only-actions)
+ [Resource types defined by AWS Control Tower](#list_controltower-resources-for-iam-policies)
+ [Condition keys for AWS Control Tower](#list_controltower-policy-keys)

## API operations defined by AWS Control Tower
<a name="list_controltower-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_controltower-actions-as-permissions).




- **   CreateLandingZone  **
  - **IAM action:**  [controltower:CreateLandingZone](#list_controltower-action-CreateLandingZone)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [controltower:PerformPreLaunchChecks](#list_controltower-action-PerformPreLaunchChecks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [controltower:SetupLandingZone](#list_controltower-action-SetupLandingZone)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [controltower:TagResource](#list_controltower-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteLandingZone  **
  - **IAM action:**  [controltower:DeleteLandingZone](#list_controltower-action-DeleteLandingZone) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableBaseline  **
  - **IAM action:**  [controltower:DeregisterOrganizationalUnit](#list_controltower-action-DeregisterOrganizationalUnit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [controltower:DisableBaseline](#list_controltower-action-DisableBaseline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DisableControl  **
  - **IAM action:**  [controltower:DisableControl](#list_controltower-action-DisableControl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [controltower:DisableGuardrail](#list_controltower-action-DisableGuardrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   EnableBaseline  **
  - **IAM action:**  [controltower:EnableBaseline](#list_controltower-action-EnableBaseline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [controltower:ManageOrganizationalUnit](#list_controltower-action-ManageOrganizationalUnit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [controltower:TagResource](#list_controltower-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   EnableControl  **
  - **IAM action:**  [controltower:EnableControl](#list_controltower-action-EnableControl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [controltower:EnableGuardrail](#list_controltower-action-EnableGuardrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [controltower:TagResource](#list_controltower-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   GetBaseline  **
  - **IAM action:**  [controltower:GetBaseline](#list_controltower-action-GetBaseline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBaselineOperation  **
  - **IAM action:**  [controltower:DescribeRegisterOrganizationalUnitOperation](#list_controltower-action-DescribeRegisterOrganizationalUnitOperation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [controltower:GetBaselineOperation](#list_controltower-action-GetBaselineOperation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetControlOperation  **
  - **IAM action:**  [controltower:GetControlOperation](#list_controltower-action-GetControlOperation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnabledBaseline  **
  - **IAM action:**  [controltower:DescribeManagedAccount](#list_controltower-action-DescribeManagedAccount)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [controltower:DescribeManagedOrganizationalUnit](#list_controltower-action-DescribeManagedOrganizationalUnit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [controltower:GetEnabledBaseline](#list_controltower-action-GetEnabledBaseline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetEnabledControl  **
  - **IAM action:**  [controltower:DescribeGuardrailForTarget](#list_controltower-action-DescribeGuardrailForTarget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [controltower:GetEnabledControl](#list_controltower-action-GetEnabledControl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetLandingZone  **
  - **IAM action:**  [controltower:DescribeLandingZoneConfiguration](#list_controltower-action-DescribeLandingZoneConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [controltower:GetAvailableUpdates](#list_controltower-action-GetAvailableUpdates)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [controltower:GetLandingZone](#list_controltower-action-GetLandingZone)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [controltower:GetLandingZoneDriftStatus](#list_controltower-action-GetLandingZoneDriftStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [controltower:GetLandingZoneStatus](#list_controltower-action-GetLandingZoneStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetLandingZoneOperation  **
  - **IAM action:**  [controltower:GetLandingZoneOperation](#list_controltower-action-GetLandingZoneOperation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [controltower:GetLandingZoneStatus](#list_controltower-action-GetLandingZoneStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListBaselines  **
  - **IAM action:**  [controltower:ListBaselines](#list_controltower-action-ListBaselines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListControlOperations  **
  - **IAM action:**  [controltower:ListControlOperations](#list_controltower-action-ListControlOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnabledBaselines  **
  - **IAM action:**  [controltower:ListEnabledBaselines](#list_controltower-action-ListEnabledBaselines)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [controltower:ListManagedAccounts](#list_controltower-action-ListManagedAccounts)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [controltower:ListManagedOrganizationalUnits](#list_controltower-action-ListManagedOrganizationalUnits)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListEnabledControls  **
  - **IAM action:**  [controltower:ListEnabledControls](#list_controltower-action-ListEnabledControls)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [controltower:ListGuardrailsForTarget](#list_controltower-action-ListGuardrailsForTarget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListLandingZoneOperations  **
  - **IAM action:**  [controltower:GetLandingZoneStatus](#list_controltower-action-GetLandingZoneStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [controltower:ListLandingZoneOperations](#list_controltower-action-ListLandingZoneOperations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListLandingZones  **
  - **IAM action:**  [controltower:GetHomeRegion](#list_controltower-action-GetHomeRegion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [controltower:ListLandingZones](#list_controltower-action-ListLandingZones)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [controltower:ListTagsForResource](#list_controltower-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ResetEnabledBaseline  **
  - **IAM action:**  [controltower:ManageOrganizationalUnit](#list_controltower-action-ManageOrganizationalUnit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [controltower:ResetEnabledBaseline](#list_controltower-action-ResetEnabledBaseline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   ResetEnabledControl  **
  - **IAM action:**  [controltower:ResetEnabledControl](#list_controltower-action-ResetEnabledControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResetLandingZone  **
  - **IAM action:**  [controltower:ResetLandingZone](#list_controltower-action-ResetLandingZone)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [controltower:SetupLandingZone](#list_controltower-action-SetupLandingZone)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [controltower:TagResource](#list_controltower-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [controltower:UntagResource](#list_controltower-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateEnabledBaseline  **
  - **IAM action:**  [controltower:ManageOrganizationalUnit](#list_controltower-action-ManageOrganizationalUnit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [controltower:UpdateEnabledBaseline](#list_controltower-action-UpdateEnabledBaseline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateEnabledControl  **
  - **IAM action:**  [controltower:UpdateEnabledControl](#list_controltower-action-UpdateEnabledControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLandingZone  **
  - **IAM action:**  [controltower:SetupLandingZone](#list_controltower-action-SetupLandingZone)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [controltower:UpdateLandingZone](#list_controltower-action-UpdateLandingZone)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write



## Actions defined by AWS Control Tower
<a name="list_controltower-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_CreateLandingZone.html)  **
  - **Description:** Grants permission to create a landing zone
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_controltower-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_controltower-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_DeleteLandingZone.html)  **
  - **Description:** Grants permission to delete AWS Control Tower landing zone
  - **Resource types (\*required):** [LandingZone\*](#list_controltower-resource-LandingZone)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_DisableBaseline.html)  **
  - **Description:** Grants permission to disable a Baseline on a target
  - **Resource types (\*required):** [EnabledBaseline\*](#list_controltower-resource-EnabledBaseline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_DisableControl.html)  **
  - **Description:** Grants permission to remove a control from an organizational unit
  - **Resource types (\*required):** [EnabledControl\*](#list_controltower-resource-EnabledControl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableBaseline.html)  **
  - **Description:** Grants permission to enable a Baseline on a target
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_controltower-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_controltower-aws_TagKeys)
  - **Access level:** Write

- **   [EnableControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableControl.html)  **
  - **Description:** Grants permission to activate a control for an organizational unit
  - **Resource types (\*required):** [EnabledControl](#list_controltower-resource-EnabledControl)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_controltower-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_controltower-aws_TagKeys)
  - **Access level:** Write

- **   [GetBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetBaseline.html)  **
  - **Description:** Grants permission to get Baseline details
  - **Resource types (\*required):** [Baseline\*](#list_controltower-resource-Baseline)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetBaselineOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetBaselineOperation.html)  **
  - **Description:** Grants permission to get the current status of a particular Baseline operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetControlOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetControlOperation.html)  **
  - **Description:** Grants permission to get the current status of a particular EnabledControl or DisableControl operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEnabledBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetEnabledBaseline.html)  **
  - **Description:** Grants permission to get an enabled Baseline
  - **Resource types (\*required):** [EnabledBaseline\*](#list_controltower-resource-EnabledBaseline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetEnabledControl.html)  **
  - **Description:** Grants permission to get an enabled control from an organizational unit
  - **Resource types (\*required):** [EnabledControl\*](#list_controltower-resource-EnabledControl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetLandingZone.html)  **
  - **Description:** Grants permission to get the current status of the landing zone setup
  - **Resource types (\*required):** [LandingZone\*](#list_controltower-resource-LandingZone)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLandingZoneDriftStatus](https://docs.aws.amazon.com/controltower/latest/userguide/drift.html)  **
  - **Description:** Grants permission to get the current landing zone drift status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLandingZoneOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetLandingZoneOperation.html)  **
  - **Description:** Grants permission to get the current status of a particular landing zone operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListBaselines](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListBaselines.html)  **
  - **Description:** Grants permission to list Baselines
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListControlOperations](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListControlOperations.html)  **
  - **Description:** Grants permission to list all control operations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDriftDetails](https://docs.aws.amazon.com/controltower/latest/userguide/drift.html)  **
  - **Description:** Grants permission to list occurrences of drift in AWS Control Tower
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEnabledBaselines](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListEnabledBaselines.html)  **
  - **Description:** Grants permission to list enabled Baselines
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEnabledControls](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListEnabledControls.html)  **
  - **Description:** Grants permission to list all enabled controls in a specified organizational unit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListExternalConfigRuleCompliance](https://docs.aws.amazon.com/controltower/latest/userguide/review-compliance.html)  **
  - **Description:** Grants permission to list the compliance of external AWS Config rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListLandingZoneOperations](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListLandingZoneOperations.html)  **
  - **Description:** Grants permission to list all landing zone operations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLandingZones](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListLandingZones.html)  **
  - **Description:** Grants permission to list all landing zones
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** [EnabledBaseline](#list_controltower-resource-EnabledBaseline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [EnabledControl](#list_controltower-resource-EnabledControl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [LandingZone](#list_controltower-resource-LandingZone) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ResetEnabledBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledBaseline.html)  **
  - **Description:** Grants permission to reset an enabled Baseline
  - **Resource types (\*required):** [EnabledBaseline\*](#list_controltower-resource-EnabledBaseline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResetEnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledControl.html)  **
  - **Description:** Grants permission to reset an enabled control for an organizational unit
  - **Resource types (\*required):** [EnabledControl\*](#list_controltower-resource-EnabledControl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResetLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetLandingZone.html)  **
  - **Description:** Grants permission to reset a landing zone
  - **Resource types (\*required):** [LandingZone\*](#list_controltower-resource-LandingZone)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/controltower/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [EnabledBaseline](#list_controltower-resource-EnabledBaseline) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_controltower-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_controltower-aws_TagKeys)
  - **Resource types (\*required):** [EnabledControl](#list_controltower-resource-EnabledControl) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_controltower-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_controltower-aws_TagKeys)
  - **Resource types (\*required):** [LandingZone](#list_controltower-resource-LandingZone) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_controltower-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_controltower-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [EnabledBaseline](#list_controltower-resource-EnabledBaseline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_controltower-aws_TagKeys)
  - **Resource types (\*required):** [EnabledControl](#list_controltower-resource-EnabledControl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_controltower-aws_TagKeys)
  - **Resource types (\*required):** [LandingZone](#list_controltower-resource-LandingZone) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_controltower-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateEnabledBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateEnabledBaseline.html)  **
  - **Description:** Grants permission to update an enabled Baseline
  - **Resource types (\*required):** [EnabledBaseline\*](#list_controltower-resource-EnabledBaseline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateEnabledControl.html)  **
  - **Description:** Grants permission to update an enabled control for an organizational unit
  - **Resource types (\*required):** [EnabledControl\*](#list_controltower-resource-EnabledControl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateLandingZone.html)  **
  - **Description:** Grants permission to update a landing zone
  - **Resource types (\*required):** [LandingZone\*](#list_controltower-resource-LandingZone)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Control Tower
<a name="list_controltower-permission-only-actions"></a>

The following actions are defined by AWS Control Tower but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateManagedAccount](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)  | Grants permission to create an account managed by AWS Control Tower |  |   | Write | 
|   [DeregisterManagedAccount](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)  | Grants permission to deregister an account created through the account factory from AWS Control Tower |  |   | Write | 
|   [DeregisterOrganizationalUnit](https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html)  | Grants permission to deregister an organizational unit from AWS Control Tower management |  |   | Write | 
|   [DescribeAccountFactoryConfig](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)  | Grants permission to describe the current account factory configuration |  |   | Read | 
|   [DescribeCoreService](https://docs.aws.amazon.com/controltower/latest/userguide/how-control-tower-works.html#what-shared)  | Grants permission to describe resources managed by core accounts in AWS Control Tower |  |   | Read | 
|   [DescribeGuardrail](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html)  | Grants permission to describe a guardrail |  |   | Read | 
|   [DescribeGuardrailForTarget](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html)  | Grants permission to describe a guardrail for a organizational unit |  |   | Read | 
|   [DescribeLandingZoneConfiguration](https://docs.aws.amazon.com/controltower/latest/userguide/step-two.html)  | Grants permission to describe the current Landing Zone configuration |  |   | Read | 
|   [DescribeManagedAccount](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)  | Grants permission to describe an account created through account factory |  |   | Read | 
|   [DescribeManagedOrganizationalUnit](https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html)  | Grants permission to describe an AWS Organizations organizational unit managed by AWS Control Tower |  |   | Read | 
|   [DescribeRegisterOrganizationalUnitOperation](https://docs.aws.amazon.com/controltower/latest/userguide/about-extending-governance.html)  | Grants permission to describe a Register Organizational Unit Operation  |  |   | Read | 
|   [DescribeSingleSignOn](https://docs.aws.amazon.com/controltower/latest/userguide/sso.html)  | Grants permission to describe the current AWS Control Tower IAM Identity Center configuration |  |   | Read | 
|   [DisableGuardrail](https://docs.aws.amazon.com/controltower/latest/userguide/enable-controls-on-ou.html)  | Grants permission to disable a guardrail from an organizational unit |  |   | Write | 
|   [EnableGuardrail](https://docs.aws.amazon.com/controltower/latest/userguide/enable-controls-on-ou.html)  | Grants permission to enable a guardrail to an organizational unit |  |   | Write | 
|   [GetAccountInfo](https://docs.aws.amazon.com/controltower/latest/userguide/accounts.html)  | Grants permission to describe an account email and validate that it exists |  |   | Read | 
|   [GetAvailableUpdates](https://docs.aws.amazon.com/controltower/latest/userguide/configuration-updates.html)  | Grants permission to list available updates for the current AWS Control Tower deployment |  |   | Read | 
|   [GetGuardrailComplianceStatus](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html)  | Grants permission to get the current compliance status of a guardrail |  |   | Read | 
|   [GetHomeRegion](https://docs.aws.amazon.com/controltower/latest/userguide/how-control-tower-works.html#region-how)  | Grants permission to get the home region of the AWS Control Tower setup |  |   | Read | 
|   [GetLandingZoneStatus](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html#step-two)  | Grants permission to get the current status of the landing zone setup |  |   | Read | 
|   [ListDirectoryGroups](https://docs.aws.amazon.com/controltower/latest/userguide/sso.html)  | Grants permission to list the current directory groups available through IAM Identity Center |  |   | List | 
|   [ListEnabledGuardrails](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html)  | Grants permission to list currently enabled guardrails |  |   | List | 
|   [ListExtendGovernancePrecheckDetails](https://docs.aws.amazon.com/controltower/latest/userguide/about-extending-governance.html)  | Grants permission to list Precheck details for an Organizational Unit  |  |   | List | 
|   [ListGuardrailViolations](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html)  | Grants permission to list existing guardrail violations |  |   | List | 
|   [ListGuardrails](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html)  | Grants permission to list all available guardrails |  |   | List | 
|   [ListGuardrailsForTarget](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html)  | Grants permission to list guardrails and their current state for a organizational unit |  |   | List | 
|   [ListManagedAccounts](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)  | Grants permission to list accounts managed through AWS Control Tower |  |   | List | 
|   [ListManagedAccountsForGuardrail](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)  | Grants permission to list managed accounts with a specified guardrail applied |  |   | List | 
|   [ListManagedAccountsForParent](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)  | Grants permission to list managed accounts under an organizational unit |  |   | List | 
|   [ListManagedOrganizationalUnits](https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html)  | Grants permission to list organizational units managed by AWS Control Tower |  |   | List | 
|   [ListManagedOrganizationalUnitsForGuardrail](https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html)  | Grants permission to list managed organizational units that have a specified guardrail applied |  |   | List | 
|   [ManageOrganizationalUnit](https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html)  | Grants permission to set up an organizational unit to be managed by AWS Control Tower |  |   | Write | 
|   [PerformPreLaunchChecks](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-prereqs.html)  | Grants permission to perform validations in an account |  |   | Read | 
|   [SetupLandingZone](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html#step-two)  | Grants permission to set up or update AWS Control Tower landing zone |  |   | Write | 
|   [UpdateAccountFactoryConfig](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)  | Grants permission to update the account factory configuration |  |   | Write | 

## Resource types defined by AWS Control Tower
<a name="list_controltower-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Baseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetBaseline.html)  | arn:${Partition}:controltower:${Region}::baseline/${BaselineId} |   | 
|  [EnabledBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableBaseline.html)  | arn:${Partition}:controltower:${Region}:${Account}:enabledbaseline/${EnabledBaselineId} | [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_) | 
|  [EnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableControl.html)  | arn:${Partition}:controltower:${Region}:${Account}:enabledcontrol/${EnabledControlId} | [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_) | 
|  [LandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_CreateLandingZone.html)  | arn:${Partition}:controltower:${Region}:${Account}:landingzone/${LandingZoneId} | [aws:ResourceTag/${TagKey}](#list_controltower-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Control Tower
<a name="list_controltower-policy-keys"></a>

AWS Control Tower defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 