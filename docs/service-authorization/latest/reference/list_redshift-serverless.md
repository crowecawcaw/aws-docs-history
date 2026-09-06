

# Actions, resources, and condition keys for Amazon Redshift Serverless
<a name="list_redshift-serverless"></a>

Amazon Redshift Serverless (service prefix: `redshift-serverless`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-serverless.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-authentication-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/redshift-serverless/redshift-serverless.json) for this service.

**Topics**
+ [API operations defined by Amazon Redshift Serverless](#list_redshift-serverless-operations)
+ [Actions defined by Amazon Redshift Serverless](#list_redshift-serverless-actions-as-permissions)
+ [Permission-only actions for Amazon Redshift Serverless](#list_redshift-serverless-permission-only-actions)
+ [Resource types defined by Amazon Redshift Serverless](#list_redshift-serverless-resources-for-iam-policies)
+ [Condition keys for Amazon Redshift Serverless](#list_redshift-serverless-policy-keys)

## API operations defined by Amazon Redshift Serverless
<a name="list_redshift-serverless-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_redshift-serverless-actions-as-permissions).




- **   ConvertRecoveryPointToSnapshot  **
  - **IAM action:**  [redshift-serverless:ConvertRecoveryPointToSnapshot](#list_redshift-serverless-action-ConvertRecoveryPointToSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift-serverless:TagResource](#list_redshift-serverless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCustomDomainAssociation  **
  - **IAM action:**  [redshift-serverless:CreateCustomDomainAssociation](#list_redshift-serverless-action-CreateCustomDomainAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEndpointAccess  **
  - **IAM action:**  [redshift-serverless:CreateEndpointAccess](#list_redshift-serverless-action-CreateEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateNamespace  **
  - **IAM action:**  [redshift-serverless:CreateNamespace](#list_redshift-serverless-action-CreateNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift-serverless:TagResource](#list_redshift-serverless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** redshift-serverless.amazonaws.com / **Access level:** Write

- **   CreateReservation  **
  - **IAM action:**  [redshift-serverless:CreateReservation](#list_redshift-serverless-action-CreateReservation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateScheduledAction  **
  - **IAM action:**  [redshift-serverless:CreateScheduledAction](#list_redshift-serverless-action-CreateScheduledAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift-serverless:CreateSnapshot](#list_redshift-serverless-action-CreateSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** redshift-serverless.amazonaws.com / **Access level:** Write

- **   CreateSnapshot  **
  - **IAM action:**  [redshift-serverless:CreateSnapshot](#list_redshift-serverless-action-CreateSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift-serverless:TagResource](#list_redshift-serverless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSnapshotCopyConfiguration  **
  - **IAM action:**  [redshift-serverless:CreateSnapshotCopyConfiguration](#list_redshift-serverless-action-CreateSnapshotCopyConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateUsageLimit  **
  - **IAM action:**  [redshift-serverless:CreateUsageLimit](#list_redshift-serverless-action-CreateUsageLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWorkgroup  **
  - **IAM action:**  [redshift-serverless:CreateWorkgroup](#list_redshift-serverless-action-CreateWorkgroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift-serverless:TagResource](#list_redshift-serverless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteCustomDomainAssociation  **
  - **IAM action:**  [redshift-serverless:DeleteCustomDomainAssociation](#list_redshift-serverless-action-DeleteCustomDomainAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEndpointAccess  **
  - **IAM action:**  [redshift-serverless:DeleteEndpointAccess](#list_redshift-serverless-action-DeleteEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNamespace  **
  - **IAM action:**  [redshift-serverless:DeleteNamespace](#list_redshift-serverless-action-DeleteNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [redshift-serverless:DeleteResourcePolicy](#list_redshift-serverless-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScheduledAction  **
  - **IAM action:**  [redshift-serverless:DeleteScheduledAction](#list_redshift-serverless-action-DeleteScheduledAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSnapshot  **
  - **IAM action:**  [redshift-serverless:DeleteSnapshot](#list_redshift-serverless-action-DeleteSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSnapshotCopyConfiguration  **
  - **IAM action:**  [redshift-serverless:DeleteSnapshotCopyConfiguration](#list_redshift-serverless-action-DeleteSnapshotCopyConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUsageLimit  **
  - **IAM action:**  [redshift-serverless:DeleteUsageLimit](#list_redshift-serverless-action-DeleteUsageLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkgroup  **
  - **IAM action:**  [redshift-serverless:DeleteWorkgroup](#list_redshift-serverless-action-DeleteWorkgroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCredentials  **
  - **IAM action:**  [redshift-serverless:GetCredentials](#list_redshift-serverless-action-GetCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCustomDomainAssociation  **
  - **IAM action:**  [redshift-serverless:GetCustomDomainAssociation](#list_redshift-serverless-action-GetCustomDomainAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEndpointAccess  **
  - **IAM action:**  [redshift-serverless:GetEndpointAccess](#list_redshift-serverless-action-GetEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdentityCenterAuthToken  **
  - **IAM action:**  [redshift-serverless:GetIdentityCenterAuthToken](#list_redshift-serverless-action-GetIdentityCenterAuthToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNamespace  **
  - **IAM action:**  [redshift-serverless:GetNamespace](#list_redshift-serverless-action-GetNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecoveryPoint  **
  - **IAM action:**  [redshift-serverless:GetRecoveryPoint](#list_redshift-serverless-action-GetRecoveryPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReservation  **
  - **IAM action:**  [redshift-serverless:GetReservation](#list_redshift-serverless-action-GetReservation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReservationOffering  **
  - **IAM action:**  [redshift-serverless:GetReservationOffering](#list_redshift-serverless-action-GetReservationOffering) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [redshift-serverless:GetResourcePolicy](#list_redshift-serverless-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetScheduledAction  **
  - **IAM action:**  [redshift-serverless:GetScheduledAction](#list_redshift-serverless-action-GetScheduledAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSnapshot  **
  - **IAM action:**  [redshift-serverless:GetSnapshot](#list_redshift-serverless-action-GetSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableRestoreStatus  **
  - **IAM action:**  [redshift-serverless:GetTableRestoreStatus](#list_redshift-serverless-action-GetTableRestoreStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTrack  **
  - **IAM action:**  [redshift-serverless:GetTrack](#list_redshift-serverless-action-GetTrack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUsageLimit  **
  - **IAM action:**  [redshift-serverless:GetUsageLimit](#list_redshift-serverless-action-GetUsageLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkgroup  **
  - **IAM action:**  [redshift-serverless:GetWorkgroup](#list_redshift-serverless-action-GetWorkgroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCustomDomainAssociations  **
  - **IAM action:**  [redshift-serverless:ListCustomDomainAssociations](#list_redshift-serverless-action-ListCustomDomainAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEndpointAccess  **
  - **IAM action:**  [redshift-serverless:ListEndpointAccess](#list_redshift-serverless-action-ListEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedWorkgroups  **
  - **IAM action:**  [redshift-serverless:ListManagedWorkgroups](#list_redshift-serverless-action-ListManagedWorkgroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNamespaces  **
  - **IAM action:**  [redshift-serverless:ListNamespaces](#list_redshift-serverless-action-ListNamespaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecoveryPoints  **
  - **IAM action:**  [redshift-serverless:ListRecoveryPoints](#list_redshift-serverless-action-ListRecoveryPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReservationOfferings  **
  - **IAM action:**  [redshift-serverless:ListReservationOfferings](#list_redshift-serverless-action-ListReservationOfferings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReservations  **
  - **IAM action:**  [redshift-serverless:ListReservations](#list_redshift-serverless-action-ListReservations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListScheduledActions  **
  - **IAM action:**  [redshift-serverless:ListScheduledActions](#list_redshift-serverless-action-ListScheduledActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSnapshotCopyConfigurations  **
  - **IAM action:**  [redshift-serverless:ListSnapshotCopyConfigurations](#list_redshift-serverless-action-ListSnapshotCopyConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSnapshots  **
  - **IAM action:**  [redshift-serverless:ListSnapshots](#list_redshift-serverless-action-ListSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTableRestoreStatus  **
  - **IAM action:**  [redshift-serverless:ListTableRestoreStatus](#list_redshift-serverless-action-ListTableRestoreStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [redshift-serverless:ListTagsForResource](#list_redshift-serverless-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTracks  **
  - **IAM action:**  [redshift-serverless:ListTracks](#list_redshift-serverless-action-ListTracks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUsageLimits  **
  - **IAM action:**  [redshift-serverless:ListUsageLimits](#list_redshift-serverless-action-ListUsageLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkgroups  **
  - **IAM action:**  [redshift-serverless:ListWorkgroups](#list_redshift-serverless-action-ListWorkgroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutResourcePolicy  **
  - **IAM action:**  [redshift-serverless:PutResourcePolicy](#list_redshift-serverless-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreFromRecoveryPoint  **
  - **IAM action:**  [redshift-serverless:RestoreFromRecoveryPoint](#list_redshift-serverless-action-RestoreFromRecoveryPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreFromSnapshot  **
  - **IAM action:**  [redshift-serverless:RestoreFromSnapshot](#list_redshift-serverless-action-RestoreFromSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreTableFromRecoveryPoint  **
  - **IAM action:**  [redshift-serverless:RestoreTableFromRecoveryPoint](#list_redshift-serverless-action-RestoreTableFromRecoveryPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreTableFromSnapshot  **
  - **IAM action:**  [redshift-serverless:RestoreTableFromSnapshot](#list_redshift-serverless-action-RestoreTableFromSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [redshift-serverless:TagResource](#list_redshift-serverless-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [redshift-serverless:UntagResource](#list_redshift-serverless-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCustomDomainAssociation  **
  - **IAM action:**  [redshift-serverless:UpdateCustomDomainAssociation](#list_redshift-serverless-action-UpdateCustomDomainAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEndpointAccess  **
  - **IAM action:**  [redshift-serverless:UpdateEndpointAccess](#list_redshift-serverless-action-UpdateEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLakehouseConfiguration  **
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** redshift-serverless.amazonaws.com / **Access level:** Write
  - **IAM action:**  [redshift:AssociateDataShareConsumer](https://docs.aws.amazon.com/redshift/latest/APIReference/API_AssociateDataShareConsumer.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:DeregisterNamespace](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeregisterNamespace.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift:RegisterNamespace](https://docs.aws.amazon.com/redshift/latest/APIReference/API_RegisterNamespace.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateNamespace  **
  - **IAM action:**  [redshift-serverless:UpdateNamespace](#list_redshift-serverless-action-UpdateNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** redshift-serverless.amazonaws.com / **Access level:** Write

- **   UpdateScheduledAction  **
  - **IAM action:**  [redshift-serverless:CreateSnapshot](#list_redshift-serverless-action-CreateSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [redshift-serverless:UpdateScheduledAction](#list_redshift-serverless-action-UpdateScheduledAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** redshift-serverless.amazonaws.com / **Access level:** Write

- **   UpdateSnapshot  **
  - **IAM action:**  [redshift-serverless:UpdateSnapshot](#list_redshift-serverless-action-UpdateSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSnapshotCopyConfiguration  **
  - **IAM action:**  [redshift-serverless:UpdateSnapshotCopyConfiguration](#list_redshift-serverless-action-UpdateSnapshotCopyConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUsageLimit  **
  - **IAM action:**  [redshift-serverless:UpdateUsageLimit](#list_redshift-serverless-action-UpdateUsageLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkgroup  **
  - **IAM action:**  [redshift-serverless:UpdateWorkgroup](#list_redshift-serverless-action-UpdateWorkgroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Redshift Serverless
<a name="list_redshift-serverless-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ConvertRecoveryPointToSnapshot](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ConvertRecoveryPointToSnapshot.html)  **
  - **Description:** Grants permission to convert a recovery point to a snapshot
  - **Resource types (\*required):** [recoveryPoint\*](#list_redshift-serverless-resource-recoveryPoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Resource types (\*required):** [snapshot\*](#list_redshift-serverless-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCustomDomainAssociation](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateCustomDomainAssociation.html)  **
  - **Description:** Grants permission to create a custom domain association in Amazon Redshift Serverless
  - **Resource types (\*required):** [workgroup\*](#list_redshift-serverless-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEndpointAccess](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateEndpointAccess.html)  **
  - **Description:** Grants permission to create an Amazon Redshift Serverless managed VPC endpoint
  - **Resource types (\*required):** [endpointAccess\*](#list_redshift-serverless-resource-endpointAccess)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateNamespace](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateNamespace.html)  **
  - **Description:** Grants permission to create an Amazon Redshift Serverless namespace
  - **Resource types (\*required):** [namespace\*](#list_redshift-serverless-resource-namespace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Access level:** Write

- **   [CreateReservation](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateReservation.html)  **
  - **Description:** Grants permission to purchase a capacity reservation according to a specific reservation offering, for a specified number of RPUs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateScheduledAction](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateScheduledAction.html)  **
  - **Description:** Grants permission to create a scheduled action for a specified Amazon Redshift Serverless namespace
  - **Resource types (\*required):** [namespace\*](#list_redshift-serverless-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSnapshot](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateSnapshot.html)  **
  - **Description:** Grants permission to create a snapshot of all databases in a namespace
  - **Resource types (\*required):** [namespace\*](#list_redshift-serverless-resource-namespace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Resource types (\*required):** [snapshot\*](#list_redshift-serverless-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSnapshotCopyConfiguration](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateSnapshotCopyConfiguration.html)  **
  - **Description:** Grants permission to create a snapshot copy configuration for a specified Amazon Redshift Serverless namespace
  - **Resource types (\*required):** [namespace\*](#list_redshift-serverless-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUsageLimit](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateUsageLimit.html)  **
  - **Description:** Grants permission to create a usage limit for a specified Amazon Redshift Serverless usage type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateWorkgroup](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateWorkgroup.html)  **
  - **Description:** Grants permission to create a workgroup in Amazon Redshift Serverless
  - **Resource types (\*required):** [workgroup\*](#list_redshift-serverless-resource-workgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCustomDomainAssociation](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_DeleteCustomDomainAssociation.html)  **
  - **Description:** Grants permission to delete a custom domain association
  - **Resource types (\*required):** [workgroup\*](#list_redshift-serverless-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEndpointAccess](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_DeleteEndpointAccess.html)  **
  - **Description:** Grants permission to delete an Amazon Redshift Serverless managed VPC endpoint
  - **Resource types (\*required):** [endpointAccess\*](#list_redshift-serverless-resource-endpointAccess)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteNamespace](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_DeleteNamespace.html)  **
  - **Description:** Grants permission to delete a namespace from Amazon Redshift Serverless
  - **Resource types (\*required):** [namespace\*](#list_redshift-serverless-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete the specified resource policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteScheduledAction](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_DeleteScheduledAction.html)  **
  - **Description:** Grants permission to delete a scheduled action from Amazon Redshift Serverless
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSnapshot](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_DeleteSnapshot.html)  **
  - **Description:** Grants permission to delete a snapshot from Amazon Redshift Serverless
  - **Resource types (\*required):** [snapshot\*](#list_redshift-serverless-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSnapshotCopyConfiguration](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_DeleteSnapshotCopyConfiguration.html)  **
  - **Description:** Grants permission to delete a snapshot copy configuration for a Amazon Redshift Serverless namespace
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteUsageLimit](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_DeleteUsageLimit.html)  **
  - **Description:** Grants permission to delete a usage limit from Amazon Redshift Serverless
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteWorkgroup](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_DeleteWorkgroup.html)  **
  - **Description:** Grants permission to delete a workgroup
  - **Resource types (\*required):** [workgroup\*](#list_redshift-serverless-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCredentials](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetCredentials.html)  **
  - **Description:** Grants permission to get a database user name and temporary password with temporary authorization to log on to Amazon Redshift Serverless
  - **Resource types (\*required):** [workgroup\*](#list_redshift-serverless-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCustomDomainAssociation](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetCustomDomainAssociation.html)  **
  - **Description:** Grants permission to get information about a specific custom domain association
  - **Resource types (\*required):** [workgroup\*](#list_redshift-serverless-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEndpointAccess](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetEndpointAccess.html)  **
  - **Description:** Grants permission to create an Amazon Redshift Serverless managed VPC endpoint
  - **Resource types (\*required):** [endpointAccess\*](#list_redshift-serverless-resource-endpointAccess)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIdentityCenterAuthToken](https://docs.aws.amazon.com/redshift/latest/mgmt/identity-center-authentication.html)  **
  - **Description:** Grants permission to get an authorized token for Identity Center users to access Redshift Serverless workgroups
  - **Resource types (\*required):** [workgroup\*](#list_redshift-serverless-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetManagedWorkgroup](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetManagedWorkgroup.html)  **
  - **Description:** Grants permission to create a Amazon Redshift Managed Serverless workgroup with the specified configuration settings
  - **Resource types (\*required):** [managed-workgroup\*](#list_redshift-serverless-resource-managed-workgroup)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNamespace](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetNamespace.html)  **
  - **Description:** Grants permission to get information about a namespace in Amazon Redshift Serverless
  - **Resource types (\*required):** [namespace\*](#list_redshift-serverless-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecoveryPoint](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetRecoveryPoint.html)  **
  - **Description:** Grants permission to get information about a recovery point
  - **Resource types (\*required):** [recoveryPoint\*](#list_redshift-serverless-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReservation](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetReservation.html)  **
  - **Description:** Grants permission to get a particular reservation object
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetReservationOffering](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetReservationOffering.html)  **
  - **Description:** Grants permission to get a particular reservation offering
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get a resource policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetScheduledAction](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetScheduledAction.html)  **
  - **Description:** Grants permission to get information about a specific scheduled action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSnapshot](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetSnapshot.html)  **
  - **Description:** Grants permission to get information about a specific snapshot
  - **Resource types (\*required):** [snapshot\*](#list_redshift-serverless-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTableRestoreStatus](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetTableRestoreStatus.html)  **
  - **Description:** Grants permission to get table restore status about a specific snapshot
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTrack](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetTrack.html)  **
  - **Description:** Grants permission to get information about a track in Amazon Redshift Serverless
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUsageLimit](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetUsageLimit.html)  **
  - **Description:** Grants permission to get information about a usage limit in Amazon Redshift Serverless
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetWorkgroup](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetWorkgroup.html)  **
  - **Description:** Grants permission to get information about a specific workgroup
  - **Resource types (\*required):** [workgroup\*](#list_redshift-serverless-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCustomDomainAssociations](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListCustomDomainAssociations.html)  **
  - **Description:** Grants permission to list custom domain associations in Amazon Redshift Serverless
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEndpointAccess](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListEndpointAccess.html)  **
  - **Description:** Grants permission to list EndpointAccess objects and relevant information
  - **Resource types (\*required):** [endpointAccess\*](#list_redshift-serverless-resource-endpointAccess)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedWorkgroups](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListManagedWorkgroups.html)  **
  - **Description:** Grants permission to list managed workgroups in Amazon Redshift Serverless
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNamespaces](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListNamespaces.html)  **
  - **Description:** Grants permission to list namespaces in Amazon Redshift Serverless
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecoveryPoints](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListRecoveryPoints.html)  **
  - **Description:** Grants permission to list an array of recovery points
  - **Resource types (\*required):** [recoveryPoint\*](#list_redshift-serverless-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReservationOfferings](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListReservationOfferings.html)  **
  - **Description:** Grants permission to list all available capacity reservation offerings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReservations](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListReservations.html)  **
  - **Description:** Grants permission to list all reservations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListScheduledActions](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListScheduledActions.html)  **
  - **Description:** Grants permission to list scheduled actions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSnapshotCopyConfigurations](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListSnapshotCopyConfigurations.html)  **
  - **Description:** Grants permission to list SnapshotCopyConfiguration objects and relevant information
  - **Resource types (\*required):** [namespace](#list_redshift-serverless-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSnapshots](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListSnapshots.html)  **
  - **Description:** Grants permission to list snapshots
  - **Resource types (\*required):** [snapshot\*](#list_redshift-serverless-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTableRestoreStatus](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListTableRestoreStatus.html)  **
  - **Description:** Grants permission to list table restore status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags assigned to a resource
  - **Resource types (\*required):** [namespace](#list_redshift-serverless-resource-namespace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workgroup](#list_redshift-serverless-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTracks](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListTracks.html)  **
  - **Description:** Grants permission to list tracks available in Amazon Redshift Serverless
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListUsageLimits](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListUsageLimits.html)  **
  - **Description:** Grants permission to list all usage limits within Amazon Redshift Serverless
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorkgroups](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListWorkgroups.html)  **
  - **Description:** Grants permission to list workgroups in Amazon Redshift Serverless
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutResourcePolicy](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to create or update a resource policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RestoreFromRecoveryPoint](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_RestoreFromRecoveryPoint.html)  **
  - **Description:** Grants permission to restore the data from a recovery point
  - **Resource types (\*required):** [recoveryPoint\*](#list_redshift-serverless-resource-recoveryPoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreFromSnapshot](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_RestoreFromSnapshot.html)  **
  - **Description:** Grants permission to restore a namespace from a snapshot
  - **Resource types (\*required):** [snapshot\*](#list_redshift-serverless-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreTableFromRecoveryPoint](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_RestoreTableFromRecoveryPoint.html)  **
  - **Description:** Grants permission to restore a table from a recovery point
  - **Resource types (\*required):** [namespace\*](#list_redshift-serverless-resource-namespace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recoveryPoint\*](#list_redshift-serverless-resource-recoveryPoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreTableFromSnapshot](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_RestoreTableFromSnapshot.html)  **
  - **Description:** Grants permission to restore a table from a snapshot
  - **Resource types (\*required):** [namespace\*](#list_redshift-serverless-resource-namespace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [snapshot\*](#list_redshift-serverless-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to assign one or more tags to a resource
  - **Resource types (\*required):** [namespace](#list_redshift-serverless-resource-namespace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Resource types (\*required):** [recoveryPoint](#list_redshift-serverless-resource-recoveryPoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Resource types (\*required):** [snapshot](#list_redshift-serverless-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Resource types (\*required):** [workgroup](#list_redshift-serverless-resource-workgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_redshift-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag or set of tags from a resource
  - **Resource types (\*required):** [namespace](#list_redshift-serverless-resource-namespace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Resource types (\*required):** [recoveryPoint](#list_redshift-serverless-resource-recoveryPoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Resource types (\*required):** [snapshot](#list_redshift-serverless-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Resource types (\*required):** [workgroup](#list_redshift-serverless-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_redshift-serverless-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCustomDomainAssociation](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateCustomDomainAssociation.html)  **
  - **Description:** Grants permission to update a certificate associated with a custom domain
  - **Resource types (\*required):** [workgroup\*](#list_redshift-serverless-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEndpointAccess](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateEndpointAccess.html)  **
  - **Description:** Grants permission to update an Amazon Redshift Serverless managed VPC endpoint
  - **Resource types (\*required):** [endpointAccess\*](#list_redshift-serverless-resource-endpointAccess)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateNamespace](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateNamespace.html)  **
  - **Description:** Grants permission to update a namespace with the specified configuration settings
  - **Resource types (\*required):** [namespace\*](#list_redshift-serverless-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateScheduledAction](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateScheduledAction.html)  **
  - **Description:** Grants permission to update a scheduled action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSnapshot](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateSnapshot.html)  **
  - **Description:** Grants permission to update a snapshot
  - **Resource types (\*required):** [snapshot\*](#list_redshift-serverless-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSnapshotCopyConfiguration](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateSnapshotCopyConfiguration.html)  **
  - **Description:** Grants permission to update a snapshot copy configuration for a Amazon Redshift Serverless namespace
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateUsageLimit](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateUsageLimit.html)  **
  - **Description:** Grants permission to update a usage limit in Amazon Redshift Serverless
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateWorkgroup](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateWorkgroup.html)  **
  - **Description:** Grants permission to update an Amazon Redshift Serverless workgroup with the specified configuration settings
  - **Resource types (\*required):** [workgroup\*](#list_redshift-serverless-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Redshift Serverless
<a name="list_redshift-serverless-permission-only-actions"></a>

The following actions are defined by Amazon Redshift Serverless but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DescribeOneTimeCredit](https://aws.amazon.com/redshift/free-trial/)  **
  - **Description:** Grants permission to see on the Amazon Redshift Serverless console the remaining number of free trial credits and their expiration date
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAutonomicsDenylist](https://docs.aws.amazon.com/redshift/latest/dg/t_Manage_workload_exclusion.html)  **
  - **Description:** Grants permission to list the resources that are denylisted from global autonomics decisions for a specified workgroup
  - **Resource types (\*required):** [workgroup\*](#list_redshift-serverless-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [UpdateAutonomicsDenylist](https://docs.aws.amazon.com/redshift/latest/dg/t_Manage_workload_exclusion.html)  **
  - **Description:** Grants permission to add or remove resources from the global autonomics denylist for a specified workgroup
  - **Resource types (\*required):** [workgroup\*](#list_redshift-serverless-resource-workgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Redshift Serverless
<a name="list_redshift-serverless-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [endpointAccess](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-connecting.html)  | arn:${Partition}:redshift-serverless:${Region}:${Account}:managedvpcendpoint/${EndpointAccessId} |   | 
|  [managed-workgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-managed-workgroup-namespace.html)  | arn:${Partition}:redshift-serverless:${Region}:${Account}:managed-workgroup/${ManagedWorkgroupName} |   | 
|  [namespace](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-workgroup-namespace.html)  | arn:${Partition}:redshift-serverless:${Region}:${Account}:namespace/${NamespaceId} | [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_) | 
|  [recoveryPoint](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery.html)  | arn:${Partition}:redshift-serverless:${Region}:${Account}:recoverypoint/${RecoveryPointId} | [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_) | 
|  [snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery.html)  | arn:${Partition}:redshift-serverless:${Region}:${Account}:snapshot/${SnapshotId} | [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_) | 
|  [workgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-workgroup-namespace.html)  | arn:${Partition}:redshift-serverless:${Region}:${Account}:workgroup/${WorkgroupId} | [aws:ResourceTag/${TagKey}](#list_redshift-serverless-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Redshift Serverless
<a name="list_redshift-serverless-policy-keys"></a>

Amazon Redshift Serverless defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [redshift-serverless:endpointAccessId](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  | Filters access by the endpoint access identifier | String | 
|   [redshift-serverless:managedWorkgroupName](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  | Filters access by the managed workgroup identifier | String | 
|   [redshift-serverless:namespaceId](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  | Filters access by the namespace identifier | String | 
|   [redshift-serverless:recoveryPointId](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  | Filters access by the recovery point identifier | String | 
|   [redshift-serverless:snapshotId](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  | Filters access by the snapshot identifier | String | 
|   [redshift-serverless:tableRestoreRequestId](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  | Filters access by the table restore request identifier | String | 
|   [redshift-serverless:workgroupId](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)  | Filters access by the workgroup identifier | String | 