

# Actions, resources, and condition keys for AWS IoT
<a name="list_iot"></a>

AWS IoT (service prefix: `iot`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/iot/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/iot/latest/developerguide/authorization.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iot/iot.json) for this service.

**Topics**
+ [API operations defined by AWS IoT](#list_iot-operations)
+ [Actions defined by AWS IoT](#list_iot-actions-as-permissions)
+ [Resource types defined by AWS IoT](#list_iot-resources-for-iam-policies)
+ [Condition keys for AWS IoT](#list_iot-policy-keys)

## API operations defined by AWS IoT
<a name="list_iot-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_iot-actions-as-permissions).




- **   AcceptCertificateTransfer  **
  - **SDK client:** iot
  - **IAM action:**  [iot:AcceptCertificateTransfer](#list_iot-action-AcceptCertificateTransfer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddThingToBillingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:AddThingToBillingGroup](#list_iot-action-AddThingToBillingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddThingToThingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:AddThingToThingGroup](#list_iot-action-AddThingToThingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateSbomWithPackageVersion  **
  - **SDK client:** iot
  - **IAM action:**  [iot:AssociateSbomWithPackageVersion](#list_iot-action-AssociateSbomWithPackageVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateTargetsWithJob  **
  - **SDK client:** iot
  - **IAM action:**  [iot:AssociateTargetsWithJob](#list_iot-action-AssociateTargetsWithJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachPolicy  **
  - **SDK client:** iot
  - **IAM action:**  [iot:AttachPolicy](#list_iot-action-AttachPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AttachPrincipalPolicy  **
  - **SDK client:** iot
  - **IAM action:**  [iot:AttachPrincipalPolicy](#list_iot-action-AttachPrincipalPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AttachSecurityProfile  **
  - **SDK client:** iot
  - **IAM action:**  [iot:AttachSecurityProfile](#list_iot-action-AttachSecurityProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachThingPrincipal  **
  - **SDK client:** iot
  - **IAM action:**  [iot:AttachThingPrincipal](#list_iot-action-AttachThingPrincipal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelAuditMitigationActionsTask  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CancelAuditMitigationActionsTask](#list_iot-action-CancelAuditMitigationActionsTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelAuditTask  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CancelAuditTask](#list_iot-action-CancelAuditTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelCertificateTransfer  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CancelCertificateTransfer](#list_iot-action-CancelCertificateTransfer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelDetectMitigationActionsTask  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CancelDetectMitigationActionsTask](#list_iot-action-CancelDetectMitigationActionsTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelJob  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CancelJob](#list_iot-action-CancelJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelJobExecution  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CancelJobExecution](#list_iot-action-CancelJobExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ClearDefaultAuthorizer  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ClearDefaultAuthorizer](#list_iot-action-ClearDefaultAuthorizer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAuditSuppression  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateAuditSuppression](#list_iot-action-CreateAuditSuppression) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAuthorizer  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateAuthorizer](#list_iot-action-CreateAuthorizer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateBillingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateBillingGroup](#list_iot-action-CreateBillingGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCertificateFromCsr  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateCertificateFromCsr](#list_iot-action-CreateCertificateFromCsr) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCertificateProvider  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateCertificateProvider](#list_iot-action-CreateCertificateProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCommand  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateCommand](#list_iot-action-CreateCommand)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   CreateCustomMetric  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateCustomMetric](#list_iot-action-CreateCustomMetric)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDimension  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateDimension](#list_iot-action-CreateDimension)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDomainConfiguration  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateDomainConfiguration](#list_iot-action-CreateDomainConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDynamicThingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateDynamicThingGroup](#list_iot-action-CreateDynamicThingGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFleetMetric  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateFleetMetric](#list_iot-action-CreateFleetMetric)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateJob  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateJob](#list_iot-action-CreateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   CreateJobTemplate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateJobTemplate](#list_iot-action-CreateJobTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   CreateKeysAndCertificate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateKeysAndCertificate](#list_iot-action-CreateKeysAndCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMitigationAction  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateMitigationAction](#list_iot-action-CreateMitigationAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   CreateOTAUpdate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateOTAUpdate](#list_iot-action-CreateOTAUpdate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   CreatePackage  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreatePackage](#list_iot-action-CreatePackage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePackageVersion  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreatePackageVersion](#list_iot-action-CreatePackageVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePolicy  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreatePolicy](#list_iot-action-CreatePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePolicyVersion  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreatePolicyVersion](#list_iot-action-CreatePolicyVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   CreateProvisioningClaim  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateProvisioningClaim](#list_iot-action-CreateProvisioningClaim) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProvisioningTemplate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateProvisioningTemplate](#list_iot-action-CreateProvisioningTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   CreateProvisioningTemplateVersion  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateProvisioningTemplateVersion](#list_iot-action-CreateProvisioningTemplateVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRoleAlias  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateRoleAlias](#list_iot-action-CreateRoleAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   CreateScheduledAudit  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateScheduledAudit](#list_iot-action-CreateScheduledAudit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSecurityProfile  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateSecurityProfile](#list_iot-action-CreateSecurityProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   CreateStream  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateStream](#list_iot-action-CreateStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   CreateThing  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateThing](#list_iot-action-CreateThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateThingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateThingGroup](#list_iot-action-CreateThingGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateThingType  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateThingType](#list_iot-action-CreateThingType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTopicRule  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateTopicRule](#list_iot-action-CreateTopicRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   CreateTopicRuleDestination  **
  - **SDK client:** iot
  - **IAM action:**  [iot:CreateTopicRuleDestination](#list_iot-action-CreateTopicRuleDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   DeleteAccountAuditConfiguration  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteAccountAuditConfiguration](#list_iot-action-DeleteAccountAuditConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAuditSuppression  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteAuditSuppression](#list_iot-action-DeleteAuditSuppression) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAuthorizer  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteAuthorizer](#list_iot-action-DeleteAuthorizer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBillingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteBillingGroup](#list_iot-action-DeleteBillingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCACertificate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteCACertificate](#list_iot-action-DeleteCACertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCertificate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteCertificate](#list_iot-action-DeleteCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCertificateProvider  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteCertificateProvider](#list_iot-action-DeleteCertificateProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCommand  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteCommand](#list_iot-action-DeleteCommand) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCommandExecution  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteCommandExecution](#list_iot-action-DeleteCommandExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomMetric  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteCustomMetric](#list_iot-action-DeleteCustomMetric) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDimension  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteDimension](#list_iot-action-DeleteDimension) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomainConfiguration  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteDomainConfiguration](#list_iot-action-DeleteDomainConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDynamicThingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteDynamicThingGroup](#list_iot-action-DeleteDynamicThingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFleetMetric  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteFleetMetric](#list_iot-action-DeleteFleetMetric) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteJob  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteJob](#list_iot-action-DeleteJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteJobExecution  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteJobExecution](#list_iot-action-DeleteJobExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteJobTemplate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteJobTemplate](#list_iot-action-DeleteJobTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMitigationAction  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteMitigationAction](#list_iot-action-DeleteMitigationAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOTAUpdate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteOTAUpdate](#list_iot-action-DeleteOTAUpdate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePackage  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeletePackage](#list_iot-action-DeletePackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePackageVersion  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeletePackageVersion](#list_iot-action-DeletePackageVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePolicy  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeletePolicy](#list_iot-action-DeletePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeletePolicyVersion  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeletePolicyVersion](#list_iot-action-DeletePolicyVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteProvisioningTemplate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteProvisioningTemplate](#list_iot-action-DeleteProvisioningTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProvisioningTemplateVersion  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteProvisioningTemplateVersion](#list_iot-action-DeleteProvisioningTemplateVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegistrationCode  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteRegistrationCode](#list_iot-action-DeleteRegistrationCode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRoleAlias  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteRoleAlias](#list_iot-action-DeleteRoleAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScheduledAudit  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteScheduledAudit](#list_iot-action-DeleteScheduledAudit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSecurityProfile  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteSecurityProfile](#list_iot-action-DeleteSecurityProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStream  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteStream](#list_iot-action-DeleteStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteThing  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteThing](#list_iot-action-DeleteThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteThingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteThingGroup](#list_iot-action-DeleteThingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteThingType  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteThingType](#list_iot-action-DeleteThingType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTopicRule  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteTopicRule](#list_iot-action-DeleteTopicRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTopicRuleDestination  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteTopicRuleDestination](#list_iot-action-DeleteTopicRuleDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteV2LoggingLevel  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeleteV2LoggingLevel](#list_iot-action-DeleteV2LoggingLevel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeprecateThingType  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DeprecateThingType](#list_iot-action-DeprecateThingType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountAuditConfiguration  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeAccountAuditConfiguration](#list_iot-action-DescribeAccountAuditConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAuditFinding  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeAuditFinding](#list_iot-action-DescribeAuditFinding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAuditMitigationActionsTask  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeAuditMitigationActionsTask](#list_iot-action-DescribeAuditMitigationActionsTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAuditSuppression  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeAuditSuppression](#list_iot-action-DescribeAuditSuppression) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAuditTask  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeAuditTask](#list_iot-action-DescribeAuditTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAuthorizer  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeAuthorizer](#list_iot-action-DescribeAuthorizer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBillingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeBillingGroup](#list_iot-action-DescribeBillingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCACertificate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeCACertificate](#list_iot-action-DescribeCACertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCertificate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeCertificate](#list_iot-action-DescribeCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCertificateProvider  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeCertificateProvider](#list_iot-action-DescribeCertificateProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCustomMetric  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeCustomMetric](#list_iot-action-DescribeCustomMetric) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDefaultAuthorizer  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeDefaultAuthorizer](#list_iot-action-DescribeDefaultAuthorizer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDetectMitigationActionsTask  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeDetectMitigationActionsTask](#list_iot-action-DescribeDetectMitigationActionsTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDimension  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeDimension](#list_iot-action-DescribeDimension) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDomainConfiguration  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeDomainConfiguration](#list_iot-action-DescribeDomainConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEncryptionConfiguration  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeEncryptionConfiguration](#list_iot-action-DescribeEncryptionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpoint  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeEndpoint](#list_iot-action-DescribeEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventConfigurations  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeEventConfigurations](#list_iot-action-DescribeEventConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetMetric  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeFleetMetric](#list_iot-action-DescribeFleetMetric) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeIndex  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeIndex](#list_iot-action-DescribeIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJob  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeJob](#list_iot-action-DescribeJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJobExecution  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeJobExecution](#list_iot-action-DescribeJobExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJobTemplate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeJobTemplate](#list_iot-action-DescribeJobTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeManagedJobTemplate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeManagedJobTemplate](#list_iot-action-DescribeManagedJobTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMitigationAction  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeMitigationAction](#list_iot-action-DescribeMitigationAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProvisioningTemplate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeProvisioningTemplate](#list_iot-action-DescribeProvisioningTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProvisioningTemplateVersion  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeProvisioningTemplateVersion](#list_iot-action-DescribeProvisioningTemplateVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRoleAlias  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeRoleAlias](#list_iot-action-DescribeRoleAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeScheduledAudit  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeScheduledAudit](#list_iot-action-DescribeScheduledAudit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSecurityProfile  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeSecurityProfile](#list_iot-action-DescribeSecurityProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStream  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeStream](#list_iot-action-DescribeStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeThing  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeThing](#list_iot-action-DescribeThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeThingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeThingGroup](#list_iot-action-DescribeThingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeThingRegistrationTask  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeThingRegistrationTask](#list_iot-action-DescribeThingRegistrationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeThingType  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DescribeThingType](#list_iot-action-DescribeThingType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetachPolicy  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DetachPolicy](#list_iot-action-DetachPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DetachPrincipalPolicy  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DetachPrincipalPolicy](#list_iot-action-DetachPrincipalPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DetachSecurityProfile  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DetachSecurityProfile](#list_iot-action-DetachSecurityProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DetachThingPrincipal  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DetachThingPrincipal](#list_iot-action-DetachThingPrincipal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableTopicRule  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DisableTopicRule](#list_iot-action-DisableTopicRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateSbomFromPackageVersion  **
  - **SDK client:** iot
  - **IAM action:**  [iot:DisassociateSbomFromPackageVersion](#list_iot-action-DisassociateSbomFromPackageVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableTopicRule  **
  - **SDK client:** iot
  - **IAM action:**  [iot:EnableTopicRule](#list_iot-action-EnableTopicRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetBehaviorModelTrainingSummaries  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetBehaviorModelTrainingSummaries](#list_iot-action-GetBehaviorModelTrainingSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetBucketsAggregation  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetBucketsAggregation](#list_iot-action-GetBucketsAggregation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCardinality  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetCardinality](#list_iot-action-GetCardinality) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCommand  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetCommand](#list_iot-action-GetCommand) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCommandExecution  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetCommandExecution](#list_iot-action-GetCommandExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEffectivePolicies  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetEffectivePolicies](#list_iot-action-GetEffectivePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIndexingConfiguration  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetIndexingConfiguration](#list_iot-action-GetIndexingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJobDocument  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetJobDocument](#list_iot-action-GetJobDocument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLoggingOptions  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetLoggingOptions](#list_iot-action-GetLoggingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOTAUpdate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetOTAUpdate](#list_iot-action-GetOTAUpdate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPackage  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetPackage](#list_iot-action-GetPackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPackageConfiguration  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetPackageConfiguration](#list_iot-action-GetPackageConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPackageVersion  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetPackageVersion](#list_iot-action-GetPackageVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPercentiles  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetPercentiles](#list_iot-action-GetPercentiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicy  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetPolicy](#list_iot-action-GetPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicyVersion  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetPolicyVersion](#list_iot-action-GetPolicyVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegistrationCode  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetRegistrationCode](#list_iot-action-GetRegistrationCode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStatistics  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetStatistics](#list_iot-action-GetStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetThingConnectivityData  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetThingConnectivityData](#list_iot-action-GetThingConnectivityData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTopicRule  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetTopicRule](#list_iot-action-GetTopicRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTopicRuleDestination  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetTopicRuleDestination](#list_iot-action-GetTopicRuleDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetV2LoggingOptions  **
  - **SDK client:** iot
  - **IAM action:**  [iot:GetV2LoggingOptions](#list_iot-action-GetV2LoggingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListActiveViolations  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListActiveViolations](#list_iot-action-ListActiveViolations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAttachedPolicies  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListAttachedPolicies](#list_iot-action-ListAttachedPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAuditFindings  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListAuditFindings](#list_iot-action-ListAuditFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAuditMitigationActionsExecutions  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListAuditMitigationActionsExecutions](#list_iot-action-ListAuditMitigationActionsExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAuditMitigationActionsTasks  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListAuditMitigationActionsTasks](#list_iot-action-ListAuditMitigationActionsTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAuditSuppressions  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListAuditSuppressions](#list_iot-action-ListAuditSuppressions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAuditTasks  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListAuditTasks](#list_iot-action-ListAuditTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAuthorizers  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListAuthorizers](#list_iot-action-ListAuthorizers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBillingGroups  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListBillingGroups](#list_iot-action-ListBillingGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCACertificates  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListCACertificates](#list_iot-action-ListCACertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCertificateProviders  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListCertificateProviders](#list_iot-action-ListCertificateProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCertificates  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListCertificates](#list_iot-action-ListCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCertificatesByCA  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListCertificatesByCA](#list_iot-action-ListCertificatesByCA) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCommandExecutions  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListCommandExecutions](#list_iot-action-ListCommandExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCommands  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListCommands](#list_iot-action-ListCommands) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomMetrics  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListCustomMetrics](#list_iot-action-ListCustomMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDetectMitigationActionsExecutions  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListDetectMitigationActionsExecutions](#list_iot-action-ListDetectMitigationActionsExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDetectMitigationActionsTasks  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListDetectMitigationActionsTasks](#list_iot-action-ListDetectMitigationActionsTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDimensions  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListDimensions](#list_iot-action-ListDimensions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainConfigurations  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListDomainConfigurations](#list_iot-action-ListDomainConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFleetMetrics  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListFleetMetrics](#list_iot-action-ListFleetMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIndices  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListIndices](#list_iot-action-ListIndices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobExecutionsForJob  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListJobExecutionsForJob](#list_iot-action-ListJobExecutionsForJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobExecutionsForThing  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListJobExecutionsForThing](#list_iot-action-ListJobExecutionsForThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobTemplates  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListJobTemplates](#list_iot-action-ListJobTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobs  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListJobs](#list_iot-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedJobTemplates  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListManagedJobTemplates](#list_iot-action-ListManagedJobTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMetricValues  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListMetricValues](#list_iot-action-ListMetricValues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMitigationActions  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListMitigationActions](#list_iot-action-ListMitigationActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOTAUpdates  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListOTAUpdates](#list_iot-action-ListOTAUpdates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOutgoingCertificates  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListOutgoingCertificates](#list_iot-action-ListOutgoingCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPackageVersions  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListPackageVersions](#list_iot-action-ListPackageVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPackages  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListPackages](#list_iot-action-ListPackages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicies  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListPolicies](#list_iot-action-ListPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicyPrincipals  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListPolicyPrincipals](#list_iot-action-ListPolicyPrincipals) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicyVersions  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListPolicyVersions](#list_iot-action-ListPolicyVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPrincipalPolicies  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListPrincipalPolicies](#list_iot-action-ListPrincipalPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPrincipalThings  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListPrincipalThings](#list_iot-action-ListPrincipalThings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPrincipalThingsV2  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListPrincipalThingsV2](#list_iot-action-ListPrincipalThingsV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProvisioningTemplateVersions  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListProvisioningTemplateVersions](#list_iot-action-ListProvisioningTemplateVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProvisioningTemplates  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListProvisioningTemplates](#list_iot-action-ListProvisioningTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRelatedResourcesForAuditFinding  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListRelatedResourcesForAuditFinding](#list_iot-action-ListRelatedResourcesForAuditFinding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRoleAliases  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListRoleAliases](#list_iot-action-ListRoleAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSbomValidationResults  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListSbomValidationResults](#list_iot-action-ListSbomValidationResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListScheduledAudits  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListScheduledAudits](#list_iot-action-ListScheduledAudits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSecurityProfiles  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListSecurityProfiles](#list_iot-action-ListSecurityProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSecurityProfilesForTarget  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListSecurityProfilesForTarget](#list_iot-action-ListSecurityProfilesForTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStreams  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListStreams](#list_iot-action-ListStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListTagsForResource](#list_iot-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTargetsForPolicy  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListTargetsForPolicy](#list_iot-action-ListTargetsForPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTargetsForSecurityProfile  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListTargetsForSecurityProfile](#list_iot-action-ListTargetsForSecurityProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThingGroups  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListThingGroups](#list_iot-action-ListThingGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThingGroupsForThing  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListThingGroupsForThing](#list_iot-action-ListThingGroupsForThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThingPrincipals  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListThingPrincipals](#list_iot-action-ListThingPrincipals) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThingPrincipalsV2  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListThingPrincipalsV2](#list_iot-action-ListThingPrincipalsV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThingRegistrationTaskReports  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListThingRegistrationTaskReports](#list_iot-action-ListThingRegistrationTaskReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThingRegistrationTasks  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListThingRegistrationTasks](#list_iot-action-ListThingRegistrationTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThingTypes  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListThingTypes](#list_iot-action-ListThingTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThings  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListThings](#list_iot-action-ListThings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThingsInBillingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListThingsInBillingGroup](#list_iot-action-ListThingsInBillingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThingsInThingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListThingsInThingGroup](#list_iot-action-ListThingsInThingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTopicRuleDestinations  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListTopicRuleDestinations](#list_iot-action-ListTopicRuleDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTopicRules  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListTopicRules](#list_iot-action-ListTopicRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListV2LoggingLevels  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListV2LoggingLevels](#list_iot-action-ListV2LoggingLevels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListViolationEvents  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ListViolationEvents](#list_iot-action-ListViolationEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutVerificationStateOnViolation  **
  - **SDK client:** iot
  - **IAM action:**  [iot:PutVerificationStateOnViolation](#list_iot-action-PutVerificationStateOnViolation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterCACertificate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:RegisterCACertificate](#list_iot-action-RegisterCACertificate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   RegisterCertificate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:RegisterCertificate](#list_iot-action-RegisterCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterCertificateWithoutCA  **
  - **SDK client:** iot
  - **IAM action:**  [iot:RegisterCertificateWithoutCA](#list_iot-action-RegisterCertificateWithoutCA) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterThing  **
  - **SDK client:** iot
  - **IAM action:**  [iot:RegisterThing](#list_iot-action-RegisterThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectCertificateTransfer  **
  - **SDK client:** iot
  - **IAM action:**  [iot:RejectCertificateTransfer](#list_iot-action-RejectCertificateTransfer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveThingFromBillingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:RemoveThingFromBillingGroup](#list_iot-action-RemoveThingFromBillingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveThingFromThingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:RemoveThingFromThingGroup](#list_iot-action-RemoveThingFromThingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ReplaceTopicRule  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ReplaceTopicRule](#list_iot-action-ReplaceTopicRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   SearchIndex  **
  - **SDK client:** iot
  - **IAM action:**  [iot:SearchIndex](#list_iot-action-SearchIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SetDefaultAuthorizer  **
  - **SDK client:** iot
  - **IAM action:**  [iot:SetDefaultAuthorizer](#list_iot-action-SetDefaultAuthorizer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   SetDefaultPolicyVersion  **
  - **SDK client:** iot
  - **IAM action:**  [iot:SetDefaultPolicyVersion](#list_iot-action-SetDefaultPolicyVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   SetLoggingOptions  **
  - **SDK client:** iot
  - **IAM action:**  [iot:SetLoggingOptions](#list_iot-action-SetLoggingOptions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   SetV2LoggingLevel  **
  - **SDK client:** iot
  - **IAM action:**  [iot:SetV2LoggingLevel](#list_iot-action-SetV2LoggingLevel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetV2LoggingOptions  **
  - **SDK client:** iot
  - **IAM action:**  [iot:SetV2LoggingOptions](#list_iot-action-SetV2LoggingOptions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   StartAuditMitigationActionsTask  **
  - **SDK client:** iot
  - **IAM action:**  [iot:StartAuditMitigationActionsTask](#list_iot-action-StartAuditMitigationActionsTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDetectMitigationActionsTask  **
  - **SDK client:** iot
  - **IAM action:**  [iot:StartDetectMitigationActionsTask](#list_iot-action-StartDetectMitigationActionsTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartOnDemandAuditTask  **
  - **SDK client:** iot
  - **IAM action:**  [iot:StartOnDemandAuditTask](#list_iot-action-StartOnDemandAuditTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartThingRegistrationTask  **
  - **SDK client:** iot
  - **IAM action:**  [iot:StartThingRegistrationTask](#list_iot-action-StartThingRegistrationTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   StopThingRegistrationTask  **
  - **SDK client:** iot
  - **IAM action:**  [iot:StopThingRegistrationTask](#list_iot-action-StopThingRegistrationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** iot
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestAuthorization  **
  - **SDK client:** iot
  - **IAM action:**  [iot:TestAuthorization](#list_iot-action-TestAuthorization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TestInvokeAuthorizer  **
  - **SDK client:** iot
  - **IAM action:**  [iot:TestInvokeAuthorizer](#list_iot-action-TestInvokeAuthorizer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TransferCertificate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:TransferCertificate](#list_iot-action-TransferCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UntagResource](#list_iot-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccountAuditConfiguration  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateAccountAuditConfiguration](#list_iot-action-UpdateAccountAuditConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   UpdateAuditSuppression  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateAuditSuppression](#list_iot-action-UpdateAuditSuppression) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAuthorizer  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateAuthorizer](#list_iot-action-UpdateAuthorizer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBillingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateBillingGroup](#list_iot-action-UpdateBillingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCACertificate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateCACertificate](#list_iot-action-UpdateCACertificate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   UpdateCertificate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateCertificate](#list_iot-action-UpdateCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCertificateProvider  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateCertificateProvider](#list_iot-action-UpdateCertificateProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCommand  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateCommand](#list_iot-action-UpdateCommand) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCustomMetric  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateCustomMetric](#list_iot-action-UpdateCustomMetric) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDimension  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateDimension](#list_iot-action-UpdateDimension) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDomainConfiguration  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateDomainConfiguration](#list_iot-action-UpdateDomainConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDynamicThingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateDynamicThingGroup](#list_iot-action-UpdateDynamicThingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEncryptionConfiguration  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateEncryptionConfiguration](#list_iot-action-UpdateEncryptionConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   UpdateEventConfigurations  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateEventConfigurations](#list_iot-action-UpdateEventConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFleetMetric  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateFleetMetric](#list_iot-action-UpdateFleetMetric) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIndexingConfiguration  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateIndexingConfiguration](#list_iot-action-UpdateIndexingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateJob  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateJob](#list_iot-action-UpdateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   UpdateMitigationAction  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateMitigationAction](#list_iot-action-UpdateMitigationAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   UpdatePackage  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdatePackage](#list_iot-action-UpdatePackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePackageConfiguration  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdatePackageConfiguration](#list_iot-action-UpdatePackageConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   UpdatePackageVersion  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdatePackageVersion](#list_iot-action-UpdatePackageVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProvisioningTemplate  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateProvisioningTemplate](#list_iot-action-UpdateProvisioningTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   UpdateRoleAlias  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateRoleAlias](#list_iot-action-UpdateRoleAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   UpdateScheduledAudit  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateScheduledAudit](#list_iot-action-UpdateScheduledAudit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSecurityProfile  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateSecurityProfile](#list_iot-action-UpdateSecurityProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   UpdateStream  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateStream](#list_iot-action-UpdateStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iot.amazonaws.com / **Access level:** Write

- **   UpdateThing  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateThing](#list_iot-action-UpdateThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateThingGroup  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateThingGroup](#list_iot-action-UpdateThingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateThingGroupsForThing  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateThingGroupsForThing](#list_iot-action-UpdateThingGroupsForThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateThingType  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateThingType](#list_iot-action-UpdateThingType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTopicRuleDestination  **
  - **SDK client:** iot
  - **IAM action:**  [iot:UpdateTopicRuleDestination](#list_iot-action-UpdateTopicRuleDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidateSecurityProfileBehaviors  **
  - **SDK client:** iot
  - **IAM action:**  [iot:ValidateSecurityProfileBehaviors](#list_iot-action-ValidateSecurityProfileBehaviors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CloseTunnel  **
  - **SDK client:** iotsecuretunneling
  - **IAM action:**  [iot:CloseTunnel](#list_iot-action-CloseTunnel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeTunnel  **
  - **SDK client:** iotsecuretunneling
  - **IAM action:**  [iot:DescribeTunnel](#list_iot-action-DescribeTunnel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **SDK client:** iotsecuretunneling
  - **IAM action:**  [iot:ListTagsForResource](#list_iot-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTunnels  **
  - **SDK client:** iotsecuretunneling
  - **IAM action:**  [iot:ListTunnels](#list_iot-action-ListTunnels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   OpenTunnel  **
  - **SDK client:** iotsecuretunneling
  - **IAM action:**  [iot:OpenTunnel](#list_iot-action-OpenTunnel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RotateTunnelAccessToken  **
  - **SDK client:** iotsecuretunneling
  - **IAM action:**  [iot:RotateTunnelAccessToken](#list_iot-action-RotateTunnelAccessToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** iotsecuretunneling
  - **IAM action:**  [iot:TagResource](#list_iot-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** iotsecuretunneling
  - **IAM action:**  [iot:UntagResource](#list_iot-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS IoT
<a name="list_iot-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptCertificateTransfer](https://docs.aws.amazon.com/iot/latest/apireference/API_AcceptCertificateTransfer.html)  **
  - **Description:** Grants permission to accept a pending certificate transfer
  - **Resource types (\*required):** [cert\*](#list_iot-resource-cert)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AddThingToBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_AddThingToBillingGroup.html)  **
  - **Description:** Grants permission to add a thing to the specified billing group
  - **Resource types (\*required):** [billinggroup\*](#list_iot-resource-billinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing) / **Condition keys:**  
  - **Access level:** Write

- **   [AddThingToThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_AddThingToThingGroup.html)  **
  - **Description:** Grants permission to add a thing to the specified thing group
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing) / **Condition keys:**  
  - **Resource types (\*required):** [thinggroup\*](#list_iot-resource-thinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateSbomWithPackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_AssociateSbomWithPackageVersion.html)  **
  - **Description:** Grants permission to associate SBOM files to a package version
  - **Resource types (\*required):** [packageversion\*](#list_iot-resource-packageversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateTargetsWithJob](https://docs.aws.amazon.com/iot/latest/apireference/API_AssociateTargetsWithJob.html)  **
  - **Description:** Grants permission to associate a group with a continuous job
  - **Resource types (\*required):** [job\*](#list_iot-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing) / **Condition keys:**  
  - **Resource types (\*required):** [thinggroup\*](#list_iot-resource-thinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AttachPolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_AttachPolicy.html)  **
  - **Description:** Grants permission to attach a policy to the specified target
  - **Resource types (\*required):** [cert](#list_iot-resource-cert) / **Condition keys:**  
  - **Resource types (\*required):** [thinggroup](#list_iot-resource-thinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [AttachPrincipalPolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_AttachPrincipalPolicy.html)  **
  - **Description:** Grants permission to attach the specified policy to the specified principal (certificate or other credential)
  - **Resource types (\*required):** [cert](#list_iot-resource-cert)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [AttachSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_AttachSecurityProfile.html)  **
  - **Description:** Grants permission to associate a Device Defender security profile with a thing group or with this account
  - **Resource types (\*required):** [custommetric](#list_iot-resource-custommetric) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dimension](#list_iot-resource-dimension) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [securityprofile\*](#list_iot-resource-securityprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thinggroup](#list_iot-resource-thinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AttachThingPrincipal](https://docs.aws.amazon.com/iot/latest/apireference/API_AttachThingPrincipal.html)  **
  - **Description:** Grants permission to attach the specified principal to the specified thing
  - **Resource types (\*required):** [cert](#list_iot-resource-cert)
  - **Condition keys:** [iot:thingArn](#list_iot-iot_thingArn)
  - **Access level:** Write

- **   [CancelAuditMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelAuditMitigationActionsTask.html)  **
  - **Description:** Grants permission to cancel a mitigation action task that is in progress
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelAuditTask](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelAuditTask.html)  **
  - **Description:** Grants permission to cancel an audit that is in progress. The audit can be either scheduled or on-demand
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelCertificateTransfer](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelCertificateTransfer.html)  **
  - **Description:** Grants permission to cancel a pending transfer for the specified certificate
  - **Resource types (\*required):** [cert\*](#list_iot-resource-cert)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelDetectMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelDetectMitigationActionsTask.html)  **
  - **Description:** Grants permission to cancel a Device Defender ML Detect mitigation action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelJob](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelJob.html)  **
  - **Description:** Grants permission to cancel a job
  - **Resource types (\*required):** [job\*](#list_iot-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelJobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_CancelJobExecution.html)  **
  - **Description:** Grants permission to cancel a job execution on a particular device
  - **Resource types (\*required):** [job\*](#list_iot-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing) / **Condition keys:**  
  - **Access level:** Write

- **   [ClearDefaultAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_ClearDefaultAuthorizer.html)  **
  - **Description:** Grants permission to clear the default authorizer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CloseTunnel](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_CloseTunnel.html)  **
  - **Description:** Grants permission to close a tunnel
  - **Resource types (\*required):** [tunnel\*](#list_iot-resource-tunnel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[iot:Delete](#list_iot-iot_Delete)
  - **Access level:** Write

- **   [ConfirmTopicRuleDestination](https://docs.aws.amazon.com/iot/latest/apireference/API_ConfirmTopicRuleDestination.html)  **
  - **Description:** Grants permission to confirm a http url TopicRuleDestinationDestination
  - **Resource types (\*required):** [destination\*](#list_iot-resource-destination)
  - **Condition keys:**  
  - **Access level:** Write

- **   [Connect](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to connect as the specified client
  - **Resource types (\*required):** [client\*](#list_iot-resource-client)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAuditSuppression](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateAuditSuppression.html)  **
  - **Description:** Grants permission to create a Device Defender audit suppression
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateAuthorizer.html)  **
  - **Description:** Grants permission to create an authorizer
  - **Resource types (\*required):** [authorizer\*](#list_iot-resource-authorizer)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateBillingGroup.html)  **
  - **Description:** Grants permission to create a billing group
  - **Resource types (\*required):** [billinggroup\*](#list_iot-resource-billinggroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCertificateFromCsr](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html)  **
  - **Description:** Grants permission to create an X.509 certificate using the specified certificate signing request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateCertificateProvider](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateProvider.html)  **
  - **Description:** Grants permission to create a certificate provider
  - **Resource types (\*required):** [certificateprovider\*](#list_iot-resource-certificateprovider)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCommand](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCommand.html)  **
  - **Description:** Grants permission to create a command that can be used to start new executions against a device
  - **Resource types (\*required):** [command\*](#list_iot-resource-command)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCustomMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCustomMetric.html)  **
  - **Description:** Grants permission to create a custom metric for device side metric reporting and monitoring
  - **Resource types (\*required):** [custommetric\*](#list_iot-resource-custommetric)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDimension](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDimension.html)  **
  - **Description:** Grants permission to define a dimension that can be used to to limit the scope of a metric used in a security profile
  - **Resource types (\*required):** [dimension\*](#list_iot-resource-dimension)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDomainConfiguration.html)  **
  - **Description:** Grants permission to create a domain configuration
  - **Resource types (\*required):** [domainconfiguration\*](#list_iot-resource-domainconfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)<br />[iot:DomainName](#list_iot-iot_DomainName)
  - **Access level:** Write

- **   [CreateDynamicThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDynamicThingGroup.html)  **
  - **Description:** Grants permission to create a Dynamic Thing Group
  - **Resource types (\*required):** [dynamicthinggroup\*](#list_iot-resource-dynamicthinggroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFleetMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateFleetMetric.html)  **
  - **Description:** Grants permission to create a fleet metric
  - **Resource types (\*required):** [fleetmetric\*](#list_iot-resource-fleetmetric) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [index\*](#list_iot-resource-index) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateJob](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateJob.html)  **
  - **Description:** Grants permission to create a job
  - **Resource types (\*required):** [job\*](#list_iot-resource-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [jobtemplate](#list_iot-resource-jobtemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [package](#list_iot-resource-package) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [packageversion](#list_iot-resource-packageversion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [thinggroup\*](#list_iot-resource-thinggroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateJobTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateJobTemplate.html)  **
  - **Description:** Grants permission to create a job template
  - **Resource types (\*required):** [job](#list_iot-resource-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [jobtemplate\*](#list_iot-resource-jobtemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [package](#list_iot-resource-package) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [packageversion](#list_iot-resource-packageversion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateKeysAndCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateKeysAndCertificate.html)  **
  - **Description:** Grants permission to create a 2048 bit RSA key pair and issues an X.509 certificate using the issued public key
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateMitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateMitigationAction.html)  **
  - **Description:** Grants permission to define an action that can be applied to audit findings by using StartAuditMitigationActionsTask
  - **Resource types (\*required):** [mitigationaction\*](#list_iot-resource-mitigationaction)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateOTAUpdate](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateOTAUpdate.html)  **
  - **Description:** Grants permission to create an OTA update job
  - **Resource types (\*required):** [otaupdate\*](#list_iot-resource-otaupdate)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePackage](https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePackage.html)  **
  - **Description:** Grants permission to create a software package that you can deploy to your devices
  - **Resource types (\*required):** [package\*](#list_iot-resource-package)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePackageVersion.html)  **
  - **Description:** Grants permission to create a version under the specified package
  - **Resource types (\*required):** [package\*](#list_iot-resource-package) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [packageversion\*](#list_iot-resource-packageversion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePolicy.html)  **
  - **Description:** Grants permission to create an AWS IoT policy
  - **Resource types (\*required):** [policy\*](#list_iot-resource-policy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Permissions management, Write

- **   [CreatePolicyVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePolicyVersion.html)  **
  - **Description:** Grants permission to create a new version of the specified AWS IoT policy
  - **Resource types (\*required):** [policy\*](#list_iot-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [CreateProvisioningClaim](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningClaim.html)  **
  - **Description:** Grants permission to create a provisioning claim
  - **Resource types (\*required):** [provisioningtemplate\*](#list_iot-resource-provisioningtemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateProvisioningTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningTemplate.html)  **
  - **Description:** Grants permission to create a fleet provisioning template
  - **Resource types (\*required):** [provisioningtemplate\*](#list_iot-resource-provisioningtemplate)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProvisioningTemplateVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningTemplateVersion.html)  **
  - **Description:** Grants permission to create a new version of a fleet provisioning template
  - **Resource types (\*required):** [provisioningtemplate\*](#list_iot-resource-provisioningtemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateRoleAlias](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateRoleAlias.html)  **
  - **Description:** Grants permission to create a role alias
  - **Resource types (\*required):** [rolealias\*](#list_iot-resource-rolealias)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateScheduledAudit](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateScheduledAudit.html)  **
  - **Description:** Grants permission to create a scheduled audit that is run at a specified time interval
  - **Resource types (\*required):** [scheduledaudit\*](#list_iot-resource-scheduledaudit)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateSecurityProfile.html)  **
  - **Description:** Grants permission to create a Device Defender security profile
  - **Resource types (\*required):** [custommetric](#list_iot-resource-custommetric) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [dimension](#list_iot-resource-dimension) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [securityprofile\*](#list_iot-resource-securityprofile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStream](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateStream.html)  **
  - **Description:** Grants permission to create a new AWS IoT stream
  - **Resource types (\*required):** [stream\*](#list_iot-resource-stream)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateThing](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateThing.html)  **
  - **Description:** Grants permission to create a thing in the thing registry
  - **Resource types (\*required):** [billinggroup](#list_iot-resource-billinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateThingGroup.html)  **
  - **Description:** Grants permission to create a thing group
  - **Resource types (\*required):** [thinggroup\*](#list_iot-resource-thinggroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateThingType](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateThingType.html)  **
  - **Description:** Grants permission to create a new thing type
  - **Resource types (\*required):** [thingtype\*](#list_iot-resource-thingtype)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateTopicRule.html)  **
  - **Description:** Grants permission to create a rule
  - **Resource types (\*required):** [rule\*](#list_iot-resource-rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTopicRuleDestination](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateTopicRuleDestination.html)  **
  - **Description:** Grants permission to create a TopicRuleDestination
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAccountAuditConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteAccountAuditConfiguration.html)  **
  - **Description:** Grants permission to delete the audit configuration associated with the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAuditSuppression](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteAuditSuppression.html)  **
  - **Description:** Grants permission to delete a Device Defender audit suppression
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteAuthorizer.html)  **
  - **Description:** Grants permission to delete the specified authorizer
  - **Resource types (\*required):** [authorizer\*](#list_iot-resource-authorizer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteBillingGroup.html)  **
  - **Description:** Grants permission to delete the specified billing group
  - **Resource types (\*required):** [billinggroup\*](#list_iot-resource-billinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCACertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCACertificate.html)  **
  - **Description:** Grants permission to delete a registered CA certificate
  - **Resource types (\*required):** [cacert\*](#list_iot-resource-cacert)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCertificate.html)  **
  - **Description:** Grants permission to delete the specified certificate
  - **Resource types (\*required):** [cert\*](#list_iot-resource-cert)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteCertificateProvider](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCertificateProvider.html)  **
  - **Description:** Grants permission to delete a certificate provider
  - **Resource types (\*required):** [certificateprovider\*](#list_iot-resource-certificateprovider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCommand](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCommand.html)  **
  - **Description:** Grants permission to delete a command
  - **Resource types (\*required):** [command\*](#list_iot-resource-command)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCommandExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCommandExecution.html)  **
  - **Description:** Grants permission to delete a command execution
  - **Resource types (\*required):** [client](#list_iot-resource-client) / **Condition keys:**  
  - **Resource types (\*required):** [thing](#list_iot-resource-thing) / **Condition keys:**  
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to disconnect the specified connection
  - **Resource types (\*required):** [client\*](#list_iot-resource-client)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteCustomMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCustomMetric.html)  **
  - **Description:** Grants permission to deletes the specified custom metric from your AWS account
  - **Resource types (\*required):** [custommetric\*](#list_iot-resource-custommetric)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDimension](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteDimension.html)  **
  - **Description:** Grants permission to remove the specified dimension from your AWS account
  - **Resource types (\*required):** [dimension\*](#list_iot-resource-dimension)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteDomainConfiguration.html)  **
  - **Description:** Grants permission to delete a domain configuration
  - **Resource types (\*required):** [domainconfiguration\*](#list_iot-resource-domainconfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDynamicThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteDynamicThingGroup.html)  **
  - **Description:** Grants permission to delete the specified Dynamic Thing Group
  - **Resource types (\*required):** [dynamicthinggroup\*](#list_iot-resource-dynamicthinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFleetMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteFleetMetric.html)  **
  - **Description:** Grants permission to delete the specified fleet metric
  - **Resource types (\*required):** [fleetmetric\*](#list_iot-resource-fleetmetric)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteJob](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteJob.html)  **
  - **Description:** Grants permission to delete a job and its related job executions
  - **Resource types (\*required):** [job\*](#list_iot-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteJobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteJobExecution.html)  **
  - **Description:** Grants permission to delete a job execution
  - **Resource types (\*required):** [job\*](#list_iot-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing) / **Condition keys:**  
  - **Access level:** Write

- **   [DeleteJobTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteJobTemplate.html)  **
  - **Description:** Grants permission to delete a job template
  - **Resource types (\*required):** [jobtemplate\*](#list_iot-resource-jobtemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteMitigationAction.html)  **
  - **Description:** Grants permission to delete a defined mitigation action from your AWS account
  - **Resource types (\*required):** [mitigationaction\*](#list_iot-resource-mitigationaction)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOTAUpdate](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteOTAUpdate.html)  **
  - **Description:** Grants permission to delete an OTA update job
  - **Resource types (\*required):** [otaupdate\*](#list_iot-resource-otaupdate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePackage](https://docs.aws.amazon.com/iot/latest/apireference/API_DeletePackage.html)  **
  - **Description:** Grants permission to delete a package
  - **Resource types (\*required):** [package\*](#list_iot-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_DeletePackageVersion.html)  **
  - **Description:** Grants permission to delete a version of the specified package
  - **Resource types (\*required):** [package\*](#list_iot-resource-package) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [packageversion\*](#list_iot-resource-packageversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_DeletePolicy.html)  **
  - **Description:** Grants permission to delete the specified policy
  - **Resource types (\*required):** [policy\*](#list_iot-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeletePolicyVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_DeletePolicyVersion.html)  **
  - **Description:** Grants permission to Delete the specified version of the specified policy
  - **Resource types (\*required):** [policy\*](#list_iot-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteProvisioningTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteProvisioningTemplate.html)  **
  - **Description:** Grants permission to delete a fleet provisioning template
  - **Resource types (\*required):** [provisioningtemplate\*](#list_iot-resource-provisioningtemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProvisioningTemplateVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteProvisioningTemplateVersion.html)  **
  - **Description:** Grants permission to delete a fleet provisioning template version
  - **Resource types (\*required):** [provisioningtemplate\*](#list_iot-resource-provisioningtemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRegistrationCode](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteRegistrationCode.html)  **
  - **Description:** Grants permission to delete a CA certificate registration code
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRoleAlias](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteRoleAlias.html)  **
  - **Description:** Grants permission to delete the specified role alias
  - **Resource types (\*required):** [rolealias\*](#list_iot-resource-rolealias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteScheduledAudit](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteScheduledAudit.html)  **
  - **Description:** Grants permission to delete a scheduled audit
  - **Resource types (\*required):** [scheduledaudit\*](#list_iot-resource-scheduledaudit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteSecurityProfile.html)  **
  - **Description:** Grants permission to delete a Device Defender security profile
  - **Resource types (\*required):** [custommetric](#list_iot-resource-custommetric) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dimension](#list_iot-resource-dimension) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [securityprofile\*](#list_iot-resource-securityprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStream](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteStream.html)  **
  - **Description:** Grants permission to delete a specified stream
  - **Resource types (\*required):** [stream\*](#list_iot-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteThing](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteThing.html)  **
  - **Description:** Grants permission to delete the specified thing
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteThingGroup.html)  **
  - **Description:** Grants permission to delete the specified thing group
  - **Resource types (\*required):** [thinggroup\*](#list_iot-resource-thinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteThingShadow](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to delete the specified thing shadow
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteThingType](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteThingType.html)  **
  - **Description:** Grants permission to delete the specified thing type
  - **Resource types (\*required):** [thingtype\*](#list_iot-resource-thingtype)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteTopicRule.html)  **
  - **Description:** Grants permission to delete the specified rule
  - **Resource types (\*required):** [rule\*](#list_iot-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTopicRuleDestination](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteTopicRuleDestination.html)  **
  - **Description:** Grants permission to delete a TopicRuleDestination
  - **Resource types (\*required):** [destination\*](#list_iot-resource-destination)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteV2LoggingLevel](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteV2LoggingLevel.html)  **
  - **Description:** Grants permission to delete the specified v2 logging level
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeprecateThingType](https://docs.aws.amazon.com/iot/latest/apireference/API_DeprecateThingType.html)  **
  - **Description:** Grants permission to deprecate the specified thing type
  - **Resource types (\*required):** [thingtype\*](#list_iot-resource-thingtype)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAccountAuditConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAccountAuditConfiguration.html)  **
  - **Description:** Grants permission to get information about audit configurations for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAuditFinding](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditFinding.html)  **
  - **Description:** Grants permission to get information about a single audit finding. Properties include the reason for noncompliance, the severity of the issue, and when the audit that returned the finding was started
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAuditMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditMitigationActionsTask.html)  **
  - **Description:** Grants permission to get information about an audit mitigation task that is used to apply mitigation actions to a set of audit findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAuditSuppression](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditSuppression.html)  **
  - **Description:** Grants permission to get information about a Device Defender audit suppression
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAuditTask](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditTask.html)  **
  - **Description:** Grants permission to get information about a Device Defender audit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuthorizer.html)  **
  - **Description:** Grants permission to describe an authorizer
  - **Resource types (\*required):** [authorizer\*](#list_iot-resource-authorizer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeBillingGroup.html)  **
  - **Description:** Grants permission to get information about the specified billing group
  - **Resource types (\*required):** [billinggroup\*](#list_iot-resource-billinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCACertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeCACertificate.html)  **
  - **Description:** Grants permission to describe a registered CA certificate
  - **Resource types (\*required):** [cacert\*](#list_iot-resource-cacert)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeCertificate.html)  **
  - **Description:** Grants permission to get information about the specified certificate
  - **Resource types (\*required):** [cert\*](#list_iot-resource-cert)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeCertificateProvider](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeCertificateProvider.html)  **
  - **Description:** Grants permission to describe a certificate provider
  - **Resource types (\*required):** [certificateprovider\*](#list_iot-resource-certificateprovider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCustomMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeCustomMetric.html)  **
  - **Description:** Grants permission to describe a custom metric that is defined in your AWS account
  - **Resource types (\*required):** [custommetric\*](#list_iot-resource-custommetric)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDefaultAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeDefaultAuthorizer.html)  **
  - **Description:** Grants permission to describe the default authorizer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDetectMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeDetectMitigationActionsTask.html)  **
  - **Description:** Grants permission to describe a Device Defender ML Detect mitigation action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDimension](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeDimension.html)  **
  - **Description:** Grants permission to get details about a dimension that is defined in your AWS account
  - **Resource types (\*required):** [dimension\*](#list_iot-resource-dimension)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeDomainConfiguration.html)  **
  - **Description:** Grants permission to get information about the domain configuration
  - **Resource types (\*required):** [domainconfiguration\*](#list_iot-resource-domainconfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEncryptionConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeEncryptionConfiguration.html)  **
  - **Description:** Grants permission to describe the encryption configuration for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEndpoint](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeEndpoint.html)  **
  - **Description:** Grants permission to get a unique endpoint specific to the AWS account making the call
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEventConfigurations](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeEventConfigurations.html)  **
  - **Description:** Grants permission to get account event configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFleetMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeFleetMetric.html)  **
  - **Description:** Grants permission to get information about the specified fleet metric
  - **Resource types (\*required):** [fleetmetric\*](#list_iot-resource-fleetmetric)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeIndex](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeIndex.html)  **
  - **Description:** Grants permission to get information about the specified index
  - **Resource types (\*required):** [index\*](#list_iot-resource-index)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeJob](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeJob.html)  **
  - **Description:** Grants permission to describe a job
  - **Resource types (\*required):** [job\*](#list_iot-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeJobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeJobExecution.html)  **
  - **Description:** Grants permission to describe a job execution
  - **Resource types (\*required):** [job](#list_iot-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing](#list_iot-resource-thing) / **Condition keys:**  
  - **Access level:** Read

- **   [DescribeJobTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeJobTemplate.html)  **
  - **Description:** Grants permission to describe a job template
  - **Resource types (\*required):** [jobtemplate\*](#list_iot-resource-jobtemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeManagedJobTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeManagedJobTemplate.html)  **
  - **Description:** Grants permission to describe a managed job template
  - **Resource types (\*required):** [jobtemplate\*](#list_iot-resource-jobtemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeMitigationAction.html)  **
  - **Description:** Grants permission to get information about a mitigation action
  - **Resource types (\*required):** [mitigationaction\*](#list_iot-resource-mitigationaction)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProvisioningTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeProvisioningTemplate.html)  **
  - **Description:** Grants permission to get information about a fleet provisioning template
  - **Resource types (\*required):** [provisioningtemplate\*](#list_iot-resource-provisioningtemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProvisioningTemplateVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeProvisioningTemplateVersion.html)  **
  - **Description:** Grants permission to get information about a fleet provisioning template version
  - **Resource types (\*required):** [provisioningtemplate\*](#list_iot-resource-provisioningtemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRoleAlias](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeRoleAlias.html)  **
  - **Description:** Grants permission to describe a role alias
  - **Resource types (\*required):** [rolealias\*](#list_iot-resource-rolealias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeScheduledAudit](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeScheduledAudit.html)  **
  - **Description:** Grants permission to get information about a scheduled audit
  - **Resource types (\*required):** [scheduledaudit\*](#list_iot-resource-scheduledaudit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeSecurityProfile.html)  **
  - **Description:** Grants permission to get information about a Device Defender security profile
  - **Resource types (\*required):** [securityprofile\*](#list_iot-resource-securityprofile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStream](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeStream.html)  **
  - **Description:** Grants permission to get information about the specified stream
  - **Resource types (\*required):** [stream\*](#list_iot-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeThing](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeThing.html)  **
  - **Description:** Grants permission to get information about the specified thing
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeThingGroup.html)  **
  - **Description:** Grants permission to get information about the specified thing group
  - **Resource types (\*required):** [thinggroup\*](#list_iot-resource-thinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeThingRegistrationTask](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeThingRegistrationTask.html)  **
  - **Description:** Grants permission to get information about the bulk thing registration task
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeThingType](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeThingType.html)  **
  - **Description:** Grants permission to get information about the specified thing type
  - **Resource types (\*required):** [thingtype\*](#list_iot-resource-thingtype)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTunnel](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_DescribeTunnel.html)  **
  - **Description:** Grants permission to describe a tunnel
  - **Resource types (\*required):** [tunnel\*](#list_iot-resource-tunnel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DetachPolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_DetachPolicy.html)  **
  - **Description:** Grants permission to detach a policy from the specified target
  - **Resource types (\*required):** [cert](#list_iot-resource-cert) / **Condition keys:**  
  - **Resource types (\*required):** [thinggroup](#list_iot-resource-thinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DetachPrincipalPolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_DetachPrincipalPolicy.html)  **
  - **Description:** Grants permission to remove the specified policy from the specified certificate
  - **Resource types (\*required):** [cert](#list_iot-resource-cert)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DetachSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_DetachSecurityProfile.html)  **
  - **Description:** Grants permission to disassociate a Device Defender security profile from a thing group or from this account
  - **Resource types (\*required):** [custommetric](#list_iot-resource-custommetric) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dimension](#list_iot-resource-dimension) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [securityprofile\*](#list_iot-resource-securityprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thinggroup](#list_iot-resource-thinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DetachThingPrincipal](https://docs.aws.amazon.com/iot/latest/apireference/API_DetachThingPrincipal.html)  **
  - **Description:** Grants permission to detach the specified principal from the specified thing
  - **Resource types (\*required):** [cert](#list_iot-resource-cert)
  - **Condition keys:** [iot:thingArn](#list_iot-iot_thingArn)
  - **Access level:** Write

- **   [DisableTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_DisableTopicRule.html)  **
  - **Description:** Grants permission to disable the specified rule
  - **Resource types (\*required):** [rule\*](#list_iot-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateSbomFromPackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_DisassociateSbomFromPackageVersion.html)  **
  - **Description:** Grants permission to disassociate SBOM files from a package version
  - **Resource types (\*required):** [packageversion\*](#list_iot-resource-packageversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_EnableTopicRule.html)  **
  - **Description:** Grants permission to enable the specified rule
  - **Resource types (\*required):** [rule\*](#list_iot-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetBehaviorModelTrainingSummaries](https://docs.aws.amazon.com/iot/latest/apireference/API_GetBehaviorModelTrainingSummaries.html)  **
  - **Description:** Grants permission to fetch a Device Defender's ML Detect Security Profile training model's status
  - **Resource types (\*required):** [securityprofile](#list_iot-resource-securityprofile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetBucketsAggregation](https://docs.aws.amazon.com/iot/latest/apireference/API_GetBucketsAggregation.html)  **
  - **Description:** Grants permission to get buckets aggregation for IoT fleet index
  - **Resource types (\*required):** [index\*](#list_iot-resource-index)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCardinality](https://docs.aws.amazon.com/iot/latest/apireference/API_GetCardinality.html)  **
  - **Description:** Grants permission to get cardinality for IoT fleet index
  - **Resource types (\*required):** [index\*](#list_iot-resource-index)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCommand](https://docs.aws.amazon.com/iot/latest/apireference/API_GetCommand.html)  **
  - **Description:** Grants permission to get the information about the command
  - **Resource types (\*required):** [command\*](#list_iot-resource-command)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCommandExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_GetCommandExecution.html)  **
  - **Description:** Grants permission to get the information of a command execution
  - **Resource types (\*required):** [client](#list_iot-resource-client) / **Condition keys:**  
  - **Resource types (\*required):** [thing](#list_iot-resource-thing) / **Condition keys:**  
  - **Access level:** Read

- **   [GetConnection](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to retrieve the specified connection information
  - **Resource types (\*required):** [client\*](#list_iot-resource-client)
  - **Condition keys:** [iot:IncludeSocketInformation](#list_iot-iot_IncludeSocketInformation)
  - **Access level:** Write

- **   [GetEffectivePolicies](https://docs.aws.amazon.com/iot/latest/apireference/API_GetEffectivePolicies.html)  **
  - **Description:** Grants permission to get effective policies
  - **Resource types (\*required):** [cert](#list_iot-resource-cert)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIndexingConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_GetIndexingConfiguration.html)  **
  - **Description:** Grants permission to get current fleet indexing configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetJobDocument](https://docs.aws.amazon.com/iot/latest/apireference/API_GetJobDocument.html)  **
  - **Description:** Grants permission to get a job document
  - **Resource types (\*required):** [job\*](#list_iot-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLoggingOptions](https://docs.aws.amazon.com/iot/latest/apireference/API_GetLoggingOptions.html)  **
  - **Description:** Grants permission to get the logging options
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOTAUpdate](https://docs.aws.amazon.com/iot/latest/apireference/API_GetOTAUpdate.html)  **
  - **Description:** Grants permission to get the information about the OTA update job
  - **Resource types (\*required):** [otaupdate\*](#list_iot-resource-otaupdate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPackage](https://docs.aws.amazon.com/iot/latest/apireference/API_GetPackage.html)  **
  - **Description:** Grants permission to get the information about the package
  - **Resource types (\*required):** [package\*](#list_iot-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPackageConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_GetPackageConfiguration.html)  **
  - **Description:** Grants permission to get the package configuration of the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_GetPackageVersion.html)  **
  - **Description:** Grants permission to get the version of the package
  - **Resource types (\*required):** [package\*](#list_iot-resource-package) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [packageversion\*](#list_iot-resource-packageversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPercentiles](https://docs.aws.amazon.com/iot/latest/apireference/API_GetPercentiles.html)  **
  - **Description:** Grants permission to get percentiles for IoT fleet index
  - **Resource types (\*required):** [index\*](#list_iot-resource-index)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_GetPolicy.html)  **
  - **Description:** Grants permission to get information about the specified policy with the policy document of the default version
  - **Resource types (\*required):** [policy\*](#list_iot-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicyVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_GetPolicyVersion.html)  **
  - **Description:** Grants permission to get information about the specified policy version
  - **Resource types (\*required):** [policy\*](#list_iot-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRegistrationCode](https://docs.aws.amazon.com/iot/latest/apireference/API_GetRegistrationCode.html)  **
  - **Description:** Grants permission to get a registration code used to register a CA certificate with AWS IoT
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRetainedMessage](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to get the retained message on the specified topic
  - **Resource types (\*required):** [topic\*](#list_iot-resource-topic)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetStatistics](https://docs.aws.amazon.com/iot/latest/apireference/API_GetStatistics.html)  **
  - **Description:** Grants permission to get statistics for IoT fleet index
  - **Resource types (\*required):** [index\*](#list_iot-resource-index)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetThingConnectivityData](https://docs.aws.amazon.com/iot/latest/apireference/API_GetThingConnectivityData.html)  **
  - **Description:** Grants permission to get the thing's connectivity data
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing)
  - **Condition keys:** [iot:IncludeSocketInformation](#list_iot-iot_IncludeSocketInformation)
  - **Access level:** Read

- **   [GetThingShadow](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to get the thing shadow
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_GetTopicRule.html)  **
  - **Description:** Grants permission to get information about the specified rule
  - **Resource types (\*required):** [rule\*](#list_iot-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTopicRuleDestination](https://docs.aws.amazon.com/iot/latest/apireference/API_GetTopicRuleDestination.html)  **
  - **Description:** Grants permission to get a TopicRuleDestination
  - **Resource types (\*required):** [destination\*](#list_iot-resource-destination)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetV2LoggingOptions](https://docs.aws.amazon.com/iot/latest/apireference/API_GetV2LoggingOptions.html)  **
  - **Description:** Grants permission to get v2 logging options
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListActiveViolations](https://docs.aws.amazon.com/iot/latest/apireference/API_ListActiveViolations.html)  **
  - **Description:** Grants permission to list the active violations for a given Device Defender security profile or Thing
  - **Resource types (\*required):** [securityprofile](#list_iot-resource-securityprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing](#list_iot-resource-thing) / **Condition keys:**  
  - **Access level:** List

- **   [ListAttachedPolicies](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAttachedPolicies.html)  **
  - **Description:** Grants permission to list the policies attached to the specified thing group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAuditFindings](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditFindings.html)  **
  - **Description:** Grants permission to list the findings (results) of a Device Defender audit or of the audits performed during a specified time period
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAuditMitigationActionsExecutions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditMitigationActionsExecutions.html)  **
  - **Description:** Grants permission to get the status of audit mitigation action tasks that were executed
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAuditMitigationActionsTasks](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditMitigationActionsTasks.html)  **
  - **Description:** Grants permission to get a list of audit mitigation action tasks that match the specified filters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAuditSuppressions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditSuppressions.html)  **
  - **Description:** Grants permission to list your Device Defender audit suppressions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAuditTasks](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuditTasks.html)  **
  - **Description:** Grants permission to list the Device Defender audits that have been performed during a given time period
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAuthorizers](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuthorizers.html)  **
  - **Description:** Grants permission to list the authorizers registered in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBillingGroups](https://docs.aws.amazon.com/iot/latest/apireference/API_ListBillingGroups.html)  **
  - **Description:** Grants permission to list all billing groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCACertificates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCACertificates.html)  **
  - **Description:** Grants permission to list the CA certificates registered for your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCertificateProviders](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCertificateProviders.html)  **
  - **Description:** Grants permission to list certificate providers in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCertificates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCertificates.html)  **
  - **Description:** Grants permission to list your certificates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCertificatesByCA](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCertificatesByCA.html)  **
  - **Description:** Grants permission to list the device certificates signed by the specified CA certificate
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCommandExecutions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCommandExecutions.html)  **
  - **Description:** Grants permission to list commands executions in the account
  - **Resource types (\*required):** [client](#list_iot-resource-client) / **Condition keys:**  
  - **Resource types (\*required):** [command](#list_iot-resource-command) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing](#list_iot-resource-thing) / **Condition keys:**  
  - **Access level:** List

- **   [ListCommands](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCommands.html)  **
  - **Description:** Grants permission to list commands in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCustomMetrics](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCustomMetrics.html)  **
  - **Description:** Grants permission to list the custom metrics in your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDetectMitigationActionsExecutions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListDetectMitigationActionsExecutions.html)  **
  - **Description:** Grants permission to lists mitigation actions executions for a Device Defender ML Detect Security Profile
  - **Resource types (\*required):** [thing](#list_iot-resource-thing)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDetectMitigationActionsTasks](https://docs.aws.amazon.com/iot/latest/apireference/API_ListDetectMitigationActionsTasks.html)  **
  - **Description:** Grants permission to list Device Defender ML Detect mitigation actions tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDimensions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListDimensions.html)  **
  - **Description:** Grants permission to list the dimensions that are defined for your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDomainConfigurations](https://docs.aws.amazon.com/iot/latest/apireference/API_ListDomainConfigurations.html)  **
  - **Description:** Grants permission to list the domain configuration created by your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFleetMetrics](https://docs.aws.amazon.com/iot/latest/apireference/API_ListFleetMetrics.html)  **
  - **Description:** Grants permission to list the fleet metrics in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIndices](https://docs.aws.amazon.com/iot/latest/apireference/API_ListIndices.html)  **
  - **Description:** Grants permission to list all indices for fleet index
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobExecutionsForJob](https://docs.aws.amazon.com/iot/latest/apireference/API_ListJobExecutionsForJob.html)  **
  - **Description:** Grants permission to list the job executions for a job
  - **Resource types (\*required):** [job\*](#list_iot-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListJobExecutionsForThing](https://docs.aws.amazon.com/iot/latest/apireference/API_ListJobExecutionsForThing.html)  **
  - **Description:** Grants permission to list the job executions for the specified thing
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobTemplates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListJobTemplates.html)  **
  - **Description:** Grants permission to list job templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobs](https://docs.aws.amazon.com/iot/latest/apireference/API_ListJobs.html)  **
  - **Description:** Grants permission to list jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedJobTemplates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListManagedJobTemplates.html)  **
  - **Description:** Grants permission to list managed job templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMetricValues](https://docs.aws.amazon.com/iot/latest/apireference/API_ListMetricValues.html)  **
  - **Description:** Grants permissions to list the metric values for a thing based on the metricName, and dimension if specified
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMitigationActions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListMitigationActions.html)  **
  - **Description:** Grants permission to get a list of all mitigation actions that match the specified filter criteria
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNamedShadowsForThing](https://docs.aws.amazon.com/iot/latest/apireference/API_ListNamedShadowsForThing.html)  **
  - **Description:** Grants permission to list all named shadows for a given thing
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOTAUpdates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListOTAUpdates.html)  **
  - **Description:** Grants permission to list OTA update jobs in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOutgoingCertificates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListOutgoingCertificates.html)  **
  - **Description:** Grants permission to list certificates that are being transfered but not yet accepted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPackageVersions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPackageVersions.html)  **
  - **Description:** Grants permission to list versions for a package in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPackages](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPackages.html)  **
  - **Description:** Grants permission to list packages in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPolicies](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPolicies.html)  **
  - **Description:** Grants permission to list your policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPolicyPrincipals](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPolicyPrincipals.html)  **
  - **Description:** Grants permission to list the principals associated with the specified policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPolicyVersions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPolicyVersions.html)  **
  - **Description:** Grants permission to list the versions of the specified policy, and identifies the default version
  - **Resource types (\*required):** [policy\*](#list_iot-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPrincipalPolicies](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPrincipalPolicies.html)  **
  - **Description:** Grants permission to list the policies attached to the specified principal. If you use an Amazon Cognito identity, the ID needs to be in Amazon Cognito Identity format
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPrincipalThings](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPrincipalThings.html)  **
  - **Description:** Grants permission to list the things associated with the specified principal
  - **Resource types (\*required):** [cert](#list_iot-resource-cert)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPrincipalThingsV2](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPrincipalThingsV2.html)  **
  - **Description:** Grants permission to list the things associated with the specified principal
  - **Resource types (\*required):** [cert](#list_iot-resource-cert)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProvisioningTemplateVersions](https://docs.aws.amazon.com/iot/latest/apireference/API_ListProvisioningTemplateVersions.html)  **
  - **Description:** Grants permission to get a list of fleet provisioning template versions
  - **Resource types (\*required):** [provisioningtemplate\*](#list_iot-resource-provisioningtemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProvisioningTemplates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListProvisioningTemplates.html)  **
  - **Description:** Grants permission to list the fleet provisioning templates in your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRelatedResourcesForAuditFinding](https://docs.aws.amazon.com/iot/latest/apireference/API_ListRelatedResourcesForAuditFinding.html)  **
  - **Description:** Grants permission to list related resources for a single audit finding
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRetainedMessages](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to list the retained messages for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRoleAliases](https://docs.aws.amazon.com/iot/latest/apireference/API_ListRoleAliases.html)  **
  - **Description:** Grants permission to list role aliases
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSbomValidationResults](https://docs.aws.amazon.com/iot/latest/apireference/API_ListSbomValidationResults.html)  **
  - **Description:** Grants permission to list SBOM validation results of a package version
  - **Resource types (\*required):** [packageversion\*](#list_iot-resource-packageversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListScheduledAudits](https://docs.aws.amazon.com/iot/latest/apireference/API_ListScheduledAudits.html)  **
  - **Description:** Grants permission to list all of your scheduled audits
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSecurityProfiles](https://docs.aws.amazon.com/iot/latest/apireference/API_ListSecurityProfiles.html)  **
  - **Description:** Grants permission to list the Device Defender security profiles you have created
  - **Resource types (\*required):** [custommetric](#list_iot-resource-custommetric) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dimension](#list_iot-resource-dimension) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSecurityProfilesForTarget](https://docs.aws.amazon.com/iot/latest/apireference/API_ListSecurityProfilesForTarget.html)  **
  - **Description:** Grants permission to list the Device Defender security profiles attached to a target
  - **Resource types (\*required):** [thinggroup](#list_iot-resource-thinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStreams](https://docs.aws.amazon.com/iot/latest/apireference/API_ListStreams.html)  **
  - **Description:** Grants permission to list the streams in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscriptions](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to retrieve the specified connection's subscriptions
  - **Resource types (\*required):** [client\*](#list_iot-resource-client)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListTagsForResource](https://docs.aws.amazon.com/iot/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags for a given resource
  - **Resource types (\*required):** [authorizer](#list_iot-resource-authorizer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [billinggroup](#list_iot-resource-billinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cacert](#list_iot-resource-cacert) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [certificateprovider](#list_iot-resource-certificateprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [command](#list_iot-resource-command) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [custommetric](#list_iot-resource-custommetric) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dimension](#list_iot-resource-dimension) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domainconfiguration](#list_iot-resource-domainconfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dynamicthinggroup](#list_iot-resource-dynamicthinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleetmetric](#list_iot-resource-fleetmetric) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [job](#list_iot-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [jobtemplate](#list_iot-resource-jobtemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [mitigationaction](#list_iot-resource-mitigationaction) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [otaupdate](#list_iot-resource-otaupdate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [policy](#list_iot-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [provisioningtemplate](#list_iot-resource-provisioningtemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rolealias](#list_iot-resource-rolealias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rule](#list_iot-resource-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [scheduledaudit](#list_iot-resource-scheduledaudit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [securityprofile](#list_iot-resource-securityprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stream](#list_iot-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thinggroup](#list_iot-resource-thinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thingtype](#list_iot-resource-thingtype) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTargetsForPolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_ListTargetsForPolicy.html)  **
  - **Description:** Grants permission to list targets for the specified policy
  - **Resource types (\*required):** [policy\*](#list_iot-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTargetsForSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_ListTargetsForSecurityProfile.html)  **
  - **Description:** Grants permission to list the targets associated with a given Device Defender security profile
  - **Resource types (\*required):** [securityprofile\*](#list_iot-resource-securityprofile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListThingGroups](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingGroups.html)  **
  - **Description:** Grants permission to list all thing groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListThingGroupsForThing](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingGroupsForThing.html)  **
  - **Description:** Grants permission to list thing groups to which the specified thing belongs
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListThingPrincipals](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingPrincipals.html)  **
  - **Description:** Grants permission to list the principals associated with the specified thing
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListThingPrincipalsV2](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingPrincipalsV2.html)  **
  - **Description:** Grants permission to list the principals associated with the specified thing
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListThingRegistrationTaskReports](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingRegistrationTaskReports.html)  **
  - **Description:** Grants permission to list information about bulk thing registration tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListThingRegistrationTasks](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingRegistrationTasks.html)  **
  - **Description:** Grants permission to list bulk thing registration tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListThingTypes](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingTypes.html)  **
  - **Description:** Grants permission to list all thing types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListThings](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThings.html)  **
  - **Description:** Grants permission to list all things
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListThingsInBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingsInBillingGroup.html)  **
  - **Description:** Grants permission to list all things in the specified billing group
  - **Resource types (\*required):** [billinggroup\*](#list_iot-resource-billinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListThingsInThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingsInThingGroup.html)  **
  - **Description:** Grants permission to list all things in the specified thing group
  - **Resource types (\*required):** [thinggroup\*](#list_iot-resource-thinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTopicRuleDestinations](https://docs.aws.amazon.com/iot/latest/apireference/API_ListTopicRuleDestinations.html)  **
  - **Description:** Grants permission to list all TopicRuleDestinations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTopicRules](https://docs.aws.amazon.com/iot/latest/apireference/API_ListTopicRules.html)  **
  - **Description:** Grants permission to list the rules for the specific topic
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTunnels](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_ListTunnels.html)  **
  - **Description:** Grants permission to list tunnels
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListV2LoggingLevels](https://docs.aws.amazon.com/iot/latest/apireference/API_ListV2LoggingLevels.html)  **
  - **Description:** Grants permission to list the v2 logging levels
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListViolationEvents](https://docs.aws.amazon.com/iot/latest/apireference/API_ListViolationEvents.html)  **
  - **Description:** Grants permission to list the Device Defender security profile violations discovered during the given time period
  - **Resource types (\*required):** [securityprofile](#list_iot-resource-securityprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing](#list_iot-resource-thing) / **Condition keys:**  
  - **Access level:** List

- **   [OpenTunnel](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_OpenTunnel.html)  **
  - **Description:** Grants permission to open a tunnel
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)<br />[iot:ThingGroupArn](#list_iot-iot_ThingGroupArn)<br />[iot:TunnelDestinationService](#list_iot-iot_TunnelDestinationService)
  - **Access level:** Write

- **   [Publish](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to publish to the specified topic
  - **Resource types (\*required):** [topic\*](#list_iot-resource-topic)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutVerificationStateOnViolation](https://docs.aws.amazon.com/iot/latest/apireference/API_PutVerificationStateOnViolation.html)  **
  - **Description:** Grants permission to put verification state on a violation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [Receive](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to receive from the specified topic
  - **Resource types (\*required):** [topic\*](#list_iot-resource-topic)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterCACertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterCACertificate.html)  **
  - **Description:** Grants permission to register a CA certificate with AWS IoT
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Write

- **   [RegisterCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterCertificate.html)  **
  - **Description:** Grants permission to register a device certificate with AWS IoT
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterCertificateWithoutCA](https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterCertificateWithoutCA.html)  **
  - **Description:** Grants permission to register a device certificate with AWS IoT without a registered CA (certificate authority)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterThing](https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterThing.html)  **
  - **Description:** Grants permission to register your thing
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RejectCertificateTransfer](https://docs.aws.amazon.com/iot/latest/apireference/API_RejectCertificateTransfer.html)  **
  - **Description:** Grants permission to reject a pending certificate transfer
  - **Resource types (\*required):** [cert\*](#list_iot-resource-cert)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveThingFromBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_RemoveThingFromBillingGroup.html)  **
  - **Description:** Grants permission to remove thing from the specified billing group
  - **Resource types (\*required):** [billinggroup\*](#list_iot-resource-billinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing) / **Condition keys:**  
  - **Access level:** Write

- **   [RemoveThingFromThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_RemoveThingFromThingGroup.html)  **
  - **Description:** Grants permission to remove thing from the specified thing group
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing) / **Condition keys:**  
  - **Resource types (\*required):** [thinggroup\*](#list_iot-resource-thinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ReplaceTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_ReplaceTopicRule.html)  **
  - **Description:** Grants permission to replace the specified rule
  - **Resource types (\*required):** [rule\*](#list_iot-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RetainPublish](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to publish a retained message to the specified topic
  - **Resource types (\*required):** [topic\*](#list_iot-resource-topic)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RotateTunnelAccessToken](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_RotateTunnelAccessToken.html)  **
  - **Description:** Grants permission to rotate the access token of a tunnel
  - **Resource types (\*required):** [tunnel\*](#list_iot-resource-tunnel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[iot:ClientMode](#list_iot-iot_ClientMode)<br />[iot:ThingGroupArn](#list_iot-iot_ThingGroupArn)<br />[iot:TunnelDestinationService](#list_iot-iot_TunnelDestinationService)
  - **Access level:** Write

- **   [SearchIndex](https://docs.aws.amazon.com/iot/latest/apireference/API_SearchIndex.html)  **
  - **Description:** Grants permission to search IoT fleet index
  - **Resource types (\*required):** [index\*](#list_iot-resource-index)
  - **Condition keys:**  
  - **Access level:** Read

- **   [SendDirectMessage](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to send a direct message to an IoT client
  - **Resource types (\*required):** [client\*](#list_iot-resource-client)
  - **Condition keys:** [iot:Topic](#list_iot-iot_Topic)
  - **Access level:** Write

- **   [SetDefaultAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_SetDefaultAuthorizer.html)  **
  - **Description:** Grants permission to set the default authorizer. This will be used if a websocket connection is made without specifying an authorizer
  - **Resource types (\*required):** [authorizer\*](#list_iot-resource-authorizer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [SetDefaultPolicyVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_SetDefaultPolicyVersion.html)  **
  - **Description:** Grants permission to set the specified version of the specified policy as the policy's default (operative) version
  - **Resource types (\*required):** [policy\*](#list_iot-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [SetLoggingOptions](https://docs.aws.amazon.com/iot/latest/apireference/API_SetLoggingOptions.html)  **
  - **Description:** Grants permission to set the logging options
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetV2LoggingLevel](https://docs.aws.amazon.com/iot/latest/apireference/API_SetV2LoggingLevel.html)  **
  - **Description:** Grants permission to set the v2 logging level
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetV2LoggingOptions](https://docs.aws.amazon.com/iot/latest/apireference/API_SetV2LoggingOptions.html)  **
  - **Description:** Grants permission to set the v2 logging options
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartAuditMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_StartAuditMitigationActionsTask.html)  **
  - **Description:** Grants permission to start a task that applies a set of mitigation actions to the specified target
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartCommandExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_StartCommandExecution.html)  **
  - **Description:** Grants permission to start a new command execution
  - **Resource types (\*required):** [client](#list_iot-resource-client) / **Condition keys:** [iot:CommandExecutionParameterBoolean/${CommandParameterName}](#list_iot-iot_CommandExecutionParameterBoolean___CommandParameterName_)<br />[iot:CommandExecutionParameterNumber/${CommandParameterName}](#list_iot-iot_CommandExecutionParameterNumber___CommandParameterName_)<br />[iot:CommandExecutionParameterString/${CommandParameterName}](#list_iot-iot_CommandExecutionParameterString___CommandParameterName_)
  - **Resource types (\*required):** [command\*](#list_iot-resource-command) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[iot:CommandExecutionParameterBoolean/${CommandParameterName}](#list_iot-iot_CommandExecutionParameterBoolean___CommandParameterName_)<br />[iot:CommandExecutionParameterNumber/${CommandParameterName}](#list_iot-iot_CommandExecutionParameterNumber___CommandParameterName_)<br />[iot:CommandExecutionParameterString/${CommandParameterName}](#list_iot-iot_CommandExecutionParameterString___CommandParameterName_)
  - **Resource types (\*required):** [thing](#list_iot-resource-thing) / **Condition keys:** [iot:CommandExecutionParameterBoolean/${CommandParameterName}](#list_iot-iot_CommandExecutionParameterBoolean___CommandParameterName_)<br />[iot:CommandExecutionParameterNumber/${CommandParameterName}](#list_iot-iot_CommandExecutionParameterNumber___CommandParameterName_)<br />[iot:CommandExecutionParameterString/${CommandParameterName}](#list_iot-iot_CommandExecutionParameterString___CommandParameterName_)
  - **Access level:** Write

- **   [StartDetectMitigationActionsTask](https://docs.aws.amazon.com/iot/latest/apireference/API_StartDetectMitigationActionsTask.html)  **
  - **Description:** Grants permission to start a Device Defender ML Detect mitigation actions task
  - **Resource types (\*required):** [securityprofile](#list_iot-resource-securityprofile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartOnDemandAuditTask](https://docs.aws.amazon.com/iot/latest/apireference/API_StartOnDemandAuditTask.html)  **
  - **Description:** Grants permission to start an on-demand Device Defender audit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartThingRegistrationTask](https://docs.aws.amazon.com/iot/latest/apireference/API_StartThingRegistrationTask.html)  **
  - **Description:** Grants permission to start a bulk thing registration task
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopThingRegistrationTask](https://docs.aws.amazon.com/iot/latest/apireference/API_StopThingRegistrationTask.html)  **
  - **Description:** Grants permission to stop a bulk thing registration task
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [Subscribe](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to subscribe to the specified TopicFilter
  - **Resource types (\*required):** [topicfilter\*](#list_iot-resource-topicfilter)
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a specified resource
  - **Resource types (\*required):** [authorizer](#list_iot-resource-authorizer) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [billinggroup](#list_iot-resource-billinggroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [cacert](#list_iot-resource-cacert) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [certificateprovider](#list_iot-resource-certificateprovider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [command](#list_iot-resource-command) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [custommetric](#list_iot-resource-custommetric) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [dimension](#list_iot-resource-dimension) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [domainconfiguration](#list_iot-resource-domainconfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [dynamicthinggroup](#list_iot-resource-dynamicthinggroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [fleetmetric](#list_iot-resource-fleetmetric) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [job](#list_iot-resource-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [jobtemplate](#list_iot-resource-jobtemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [mitigationaction](#list_iot-resource-mitigationaction) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [otaupdate](#list_iot-resource-otaupdate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [package](#list_iot-resource-package) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [packageversion](#list_iot-resource-packageversion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [policy](#list_iot-resource-policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [provisioningtemplate](#list_iot-resource-provisioningtemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [rolealias](#list_iot-resource-rolealias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [rule](#list_iot-resource-rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [scheduledaudit](#list_iot-resource-scheduledaudit) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [securityprofile](#list_iot-resource-securityprofile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [stream](#list_iot-resource-stream) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [thinggroup](#list_iot-resource-thinggroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [thingtype](#list_iot-resource-thingtype) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TestAuthorization](https://docs.aws.amazon.com/iot/latest/apireference/API_TestAuthorization.html)  **
  - **Description:** Grants permission to test the policies evaluation for group policies
  - **Resource types (\*required):** [cert](#list_iot-resource-cert)
  - **Condition keys:**  
  - **Access level:** Read

- **   [TestInvokeAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_TestInvokeAuthorizer.html)  **
  - **Description:** Grants permission to test invoke the specified custom authorizer for testing purposes
  - **Resource types (\*required):** [authorizer\*](#list_iot-resource-authorizer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TransferCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_TransferCertificate.html)  **
  - **Description:** Grants permission to transfer the specified certificate to the specified AWS account
  - **Resource types (\*required):** [cert\*](#list_iot-resource-cert)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a specified resource
  - **Resource types (\*required):** [authorizer](#list_iot-resource-authorizer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [billinggroup](#list_iot-resource-billinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [cacert](#list_iot-resource-cacert) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [certificateprovider](#list_iot-resource-certificateprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [command](#list_iot-resource-command) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [custommetric](#list_iot-resource-custommetric) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [dimension](#list_iot-resource-dimension) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [domainconfiguration](#list_iot-resource-domainconfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [dynamicthinggroup](#list_iot-resource-dynamicthinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [fleetmetric](#list_iot-resource-fleetmetric) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [job](#list_iot-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [jobtemplate](#list_iot-resource-jobtemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [mitigationaction](#list_iot-resource-mitigationaction) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [otaupdate](#list_iot-resource-otaupdate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [package](#list_iot-resource-package) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [packageversion](#list_iot-resource-packageversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [policy](#list_iot-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [provisioningtemplate](#list_iot-resource-provisioningtemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [rolealias](#list_iot-resource-rolealias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [rule](#list_iot-resource-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [scheduledaudit](#list_iot-resource-scheduledaudit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [securityprofile](#list_iot-resource-securityprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [stream](#list_iot-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [thinggroup](#list_iot-resource-thinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Resource types (\*required):** [thingtype](#list_iot-resource-thingtype) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountAuditConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateAccountAuditConfiguration.html)  **
  - **Description:** Grants permission to configure or reconfigure the Device Defender audit settings for this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAuditSuppression](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateAuditSuppression.html)  **
  - **Description:** Grants permission to update a Device Defender audit suppression
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateAuthorizer.html)  **
  - **Description:** Grants permission to update an authorizer
  - **Resource types (\*required):** [authorizer\*](#list_iot-resource-authorizer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBillingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateBillingGroup.html)  **
  - **Description:** Grants permission to update information associated with the specified billing group
  - **Resource types (\*required):** [billinggroup\*](#list_iot-resource-billinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCACertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCACertificate.html)  **
  - **Description:** Grants permission to update a registered CA certificate
  - **Resource types (\*required):** [cacert\*](#list_iot-resource-cacert)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCertificate.html)  **
  - **Description:** Grants permission to update the status of the specified certificate. This operation is idempotent
  - **Resource types (\*required):** [cert\*](#list_iot-resource-cert)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateCertificateProvider](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCertificateProvider.html)  **
  - **Description:** Grants permission to update a certificate provider
  - **Resource types (\*required):** [certificateprovider\*](#list_iot-resource-certificateprovider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCommand](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCommand.html)  **
  - **Description:** Grants permission to update a command
  - **Resource types (\*required):** [command\*](#list_iot-resource-command)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCustomMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCustomMetric.html)  **
  - **Description:** Grants permission to update the specified custom metric
  - **Resource types (\*required):** [custommetric\*](#list_iot-resource-custommetric)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDimension](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateDimension.html)  **
  - **Description:** Grants permission to update the definition for a dimension
  - **Resource types (\*required):** [dimension\*](#list_iot-resource-dimension)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateDomainConfiguration.html)  **
  - **Description:** Grants permission to update a domain configuration
  - **Resource types (\*required):** [domainconfiguration\*](#list_iot-resource-domainconfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDynamicThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateDynamicThingGroup.html)  **
  - **Description:** Grants permission to update a Dynamic Thing Group
  - **Resource types (\*required):** [dynamicthinggroup\*](#list_iot-resource-dynamicthinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEncryptionConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateEncryptionConfiguration.html)  **
  - **Description:** Grants permission to update the encryption configuration for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEventConfigurations](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateEventConfigurations.html)  **
  - **Description:** Grants permission to update event configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateFleetMetric](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateFleetMetric.html)  **
  - **Description:** Grants permission to update a fleet metric
  - **Resource types (\*required):** [fleetmetric\*](#list_iot-resource-fleetmetric) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_iot-resource-index) / **Condition keys:**  
  - **Access level:** Write

- **   [UpdateIndexingConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateIndexingConfiguration.html)  **
  - **Description:** Grants permission to update fleet indexing configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateJob](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateJob.html)  **
  - **Description:** Grants permission to update a job
  - **Resource types (\*required):** [job\*](#list_iot-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateMitigationAction.html)  **
  - **Description:** Grants permission to update the definition for the specified mitigation action
  - **Resource types (\*required):** [mitigationaction\*](#list_iot-resource-mitigationaction)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePackage](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackage.html)  **
  - **Description:** Grants permission to update a package
  - **Resource types (\*required):** [package\*](#list_iot-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePackageConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackageConfiguration.html)  **
  - **Description:** Grants permission to update the package configuration of the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdatePackageVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdatePackageVersion.html)  **
  - **Description:** Grants permission to update the version of the specified package
  - **Resource types (\*required):** [package\*](#list_iot-resource-package) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [packageversion\*](#list_iot-resource-packageversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProvisioningTemplate](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateProvisioningTemplate.html)  **
  - **Description:** Grants permission to update a fleet provisioning template
  - **Resource types (\*required):** [provisioningtemplate\*](#list_iot-resource-provisioningtemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRoleAlias](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateRoleAlias.html)  **
  - **Description:** Grants permission to update the role alias
  - **Resource types (\*required):** [rolealias\*](#list_iot-resource-rolealias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateScheduledAudit](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateScheduledAudit.html)  **
  - **Description:** Grants permission to update a scheduled audit, including what checks are performed and how often the audit takes place
  - **Resource types (\*required):** [scheduledaudit\*](#list_iot-resource-scheduledaudit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateSecurityProfile.html)  **
  - **Description:** Grants permission to update a Device Defender security profile
  - **Resource types (\*required):** [custommetric](#list_iot-resource-custommetric) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dimension](#list_iot-resource-dimension) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [securityprofile\*](#list_iot-resource-securityprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStream](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateStream.html)  **
  - **Description:** Grants permission to update the data for a stream
  - **Resource types (\*required):** [stream\*](#list_iot-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateThing](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateThing.html)  **
  - **Description:** Grants permission to update information associated with the specified thing
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateThingGroup](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateThingGroup.html)  **
  - **Description:** Grants permission to update information associated with the specified thing group
  - **Resource types (\*required):** [thinggroup\*](#list_iot-resource-thinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateThingGroupsForThing](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateThingGroupsForThing.html)  **
  - **Description:** Grants permission to update the thing groups to which the thing belongs
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing) / **Condition keys:**  
  - **Resource types (\*required):** [thinggroup](#list_iot-resource-thinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateThingShadow](https://docs.aws.amazon.com/iot/latest/developerguide/policy-actions.html)  **
  - **Description:** Grants permission to update the thing shadow
  - **Resource types (\*required):** [thing\*](#list_iot-resource-thing)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateThingType](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateThingType.html)  **
  - **Description:** Grants permission to update information associated with the specified thing type
  - **Resource types (\*required):** [thingtype\*](#list_iot-resource-thingtype)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTopicRuleDestination](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateTopicRuleDestination.html)  **
  - **Description:** Grants permission to update a TopicRuleDestination
  - **Resource types (\*required):** [destination\*](#list_iot-resource-destination)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ValidateSecurityProfileBehaviors](https://docs.aws.amazon.com/iot/latest/apireference/API_ValidateSecurityProfileBehaviors.html)  **
  - **Description:** Grants permission to validate a Device Defender security profile behaviors specification
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by AWS IoT
<a name="list_iot-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [authorizer](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authorizer.html)  | arn:${Partition}:iot:${Region}:${Account}:authorizer/${AuthorizerName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [billinggroup](https://docs.aws.amazon.com/iot/latest/developerguide/billing-groups.html)  | arn:${Partition}:iot:${Region}:${Account}:billinggroup/${BillingGroupName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [cacert](https://docs.aws.amazon.com/iot/latest/developerguide/x509-certs.html)  | arn:${Partition}:iot:${Region}:${Account}:cacert/${CACertificate} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [cert](https://docs.aws.amazon.com/iot/latest/developerguide/x509-certs.html)  | arn:${Partition}:iot:${Region}:${Account}:cert/${Certificate} |   | 
|  [certificateprovider](https://docs.aws.amazon.com/iot/latest/developerguide/provisioning-cert-provider.html)  | arn:${Partition}:iot:${Region}:${Account}:certificateprovider/${CertificateProviderName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-message-broker.html)  | arn:${Partition}:iot:${Region}:${Account}:client/${ClientId} |   | 
|  [command](https://docs.aws.amazon.com/iot/latest/developerguide/iot-remote-command.html)  | arn:${Partition}:iot:${Region}:${Account}:command/${CommandId} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [custommetric](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html)  | arn:${Partition}:iot:${Region}:${Account}:custommetric/${MetricName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [destination](https://docs.aws.amazon.com/iot/latest/developerguide/rule-destination.html)  | arn:${Partition}:iot:${Region}:${Account}:ruledestination/${DestinationType}/${Uuid} |   | 
|  [dimension](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html)  | arn:${Partition}:iot:${Region}:${Account}:dimension/${DimensionName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [domainconfiguration](https://docs.aws.amazon.com/iot/latest/developerguide/domain-configuration.html)  | arn:${Partition}:iot:${Region}:${Account}:domainconfiguration/${DomainConfigurationName}/${Id} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [dynamicthinggroup](https://docs.aws.amazon.com/iot/latest/developerguide/dynamic-thing-groups.html)  | arn:${Partition}:iot:${Region}:${Account}:thinggroup/${ThingGroupName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [fleetmetric](https://docs.aws.amazon.com/iot/latest/developerguide/iot-indexing.html)  | arn:${Partition}:iot:${Region}:${Account}:fleetmetric/${FleetMetricName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [index](https://docs.aws.amazon.com/iot/latest/developerguide/iot-indexing.html)  | arn:${Partition}:iot:${Region}:${Account}:index/${IndexName} |   | 
|  [job](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html)  | arn:${Partition}:iot:${Region}:${Account}:job/${JobId} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [jobtemplate](https://docs.aws.amazon.com/iot/latest/developerguide/job-templates.html)  | arn:${Partition}:iot:${Region}:${Account}:jobtemplate/${JobTemplateId} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [mitigationaction](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-mitigation-actions.html)  | arn:${Partition}:iot:${Region}:${Account}:mitigationaction/${MitigationActionName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [otaupdate](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ota-dev.html)  | arn:${Partition}:iot:${Region}:${Account}:otaupdate/${OtaUpdateId} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [package](https://docs.aws.amazon.com/iot/latest/developerguide/software-package-catalog.html)  | arn:${Partition}:iot:${Region}:${Account}:package/${PackageName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [packageversion](https://docs.aws.amazon.com/iot/latest/developerguide/software-package-catalog.html)  | arn:${Partition}:iot:${Region}:${Account}:package/${PackageName}/version/${VersionName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [policy](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html)  | arn:${Partition}:iot:${Region}:${Account}:policy/${PolicyName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [provisioningtemplate](https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html)  | arn:${Partition}:iot:${Region}:${Account}:provisioningtemplate/${ProvisioningTemplate} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [rolealias](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html)  | arn:${Partition}:iot:${Region}:${Account}:rolealias/${RoleAlias} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html)  | arn:${Partition}:iot:${Region}:${Account}:rule/${RuleName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [scheduledaudit](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit.html)  | arn:${Partition}:iot:${Region}:${Account}:scheduledaudit/${ScheduleName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [securityprofile](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html)  | arn:${Partition}:iot:${Region}:${Account}:securityprofile/${SecurityProfileName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [stream](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ota-dev.html)  | arn:${Partition}:iot:${Region}:${Account}:stream/${StreamId} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [thing](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html)  | arn:${Partition}:iot:${Region}:${Account}:thing/${ThingName} |   | 
|  [thinggroup](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)  | arn:${Partition}:iot:${Region}:${Account}:thinggroup/${ThingGroupName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [thingtype](https://docs.aws.amazon.com/iot/latest/developerguide/thing-types.html)  | arn:${Partition}:iot:${Region}:${Account}:thingtype/${ThingTypeName} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 
|  [topic](https://docs.aws.amazon.com/iot/latest/developerguide/iot-message-broker.html)  | arn:${Partition}:iot:${Region}:${Account}:topic/${TopicName} |   | 
|  [topicfilter](https://docs.aws.amazon.com/iot/latest/developerguide/topics.html)  | arn:${Partition}:iot:${Region}:${Account}:topicfilter/${TopicFilter} |   | 
|  [tunnel](https://docs.aws.amazon.com/iot/latest/developerguide/iot-tunnels.html)  | arn:${Partition}:iot:${Region}:${Account}:tunnel/${TunnelId} | [aws:ResourceTag/${TagKey}](#list_iot-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS IoT
<a name="list_iot-policy-keys"></a>

AWS IoT defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by a tag key that is present in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by a tag key component of a tag associated to the IoT resource in the request | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by a list of tag keys associated to the IoT resource in the request | ArrayOfString | 
|   [iot:ClientMode](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html)  | Filters access by the mode of the client for IoT Tunnel | String | 
|   [iot:CommandExecutionParameterBoolean/${CommandParameterName}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html)  | Filters access by the command parameter name and boolean value | Bool | 
|   [iot:CommandExecutionParameterNumber/${CommandParameterName}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html)  | Filters access by the command parameter name and numeric value | Numeric | 
|   [iot:CommandExecutionParameterString/${CommandParameterName}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html)  | Filters access by the command parameter name and string value | String | 
|   [iot:Delete](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html)  | Filters access by a flag indicating whether or not to also delete an IoT Tunnel immediately when making iot:CloseTunnel request | Bool | 
|   [iot:DomainName](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html)  | Filters access by based on the domain name of an IoT DomainConfiguration | String | 
|   [iot:IncludeSocketInformation](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html)  | Filters access by GetConnection and GetThingConnectivityData includeSocketInformation request parameter | Bool | 
|   [iot:ThingGroupArn](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html)  | Filters access by a list of IoT Thing Group ARNs that the destination IoT Thing belongs to for an IoT Tunnel | ArrayOfARN | 
|   [iot:Topic](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html)  | Filters access by based on the topic | String | 
|   [iot:TunnelDestinationService](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html)  | Filters access by a list of destination services for an IoT Tunnel | ArrayOfString | 
|   [iot:thingArn](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html)  | Filters access by the ARN of an IoT Thing | ARN | 