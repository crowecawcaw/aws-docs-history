

# Actions, resources, and condition keys for Amazon Simple Email Service - Mail Manager
<a name="list_mailmanager"></a>

Amazon Simple Email Service - Mail Manager (service prefix: `ses`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/ses/latest/dg/eb.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/ses/latest/dg/control-user-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ses/ses.json) for this service.

**Topics**
+ [API operations defined by Amazon Simple Email Service - Mail Manager](#list_mailmanager-operations)
+ [Actions defined by Amazon Simple Email Service - Mail Manager](#list_mailmanager-actions-as-permissions)
+ [Permission-only actions for Amazon Simple Email Service - Mail Manager](#list_mailmanager-permission-only-actions)
+ [Resource types defined by Amazon Simple Email Service - Mail Manager](#list_mailmanager-resources-for-iam-policies)
+ [Condition keys for Amazon Simple Email Service - Mail Manager](#list_mailmanager-policy-keys)

## API operations defined by Amazon Simple Email Service - Mail Manager
<a name="list_mailmanager-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mailmanager-actions-as-permissions).




- **   CreateAddonInstance  **
  - **IAM action:**  [ses:CreateAddonInstance](#list_mailmanager-action-CreateAddonInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_mailmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAddonSubscription  **
  - **IAM action:**  [ses:CreateAddonSubscription](#list_mailmanager-action-CreateAddonSubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_mailmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAddressList  **
  - **IAM action:**  [ses:CreateAddressList](#list_mailmanager-action-CreateAddressList)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_mailmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAddressListImportJob  **
  - **IAM action:**  [ses:CreateAddressListImportJob](#list_mailmanager-action-CreateAddressListImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateArchive  **
  - **IAM action:**  [ses:CreateArchive](#list_mailmanager-action-CreateArchive)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_mailmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIngressPoint  **
  - **IAM action:**  [ses:CreateIngressPoint](#list_mailmanager-action-CreateIngressPoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_mailmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRelay  **
  - **IAM action:**  [ses:CreateRelay](#list_mailmanager-action-CreateRelay)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_mailmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRuleSet  **
  - **IAM action:**  [ses:CreateRuleSet](#list_mailmanager-action-CreateRuleSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_mailmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ses.amazonaws.com / **Access level:** Write

- **   CreateTrafficPolicy  **
  - **IAM action:**  [ses:CreateTrafficPolicy](#list_mailmanager-action-CreateTrafficPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ses:TagResource](#list_mailmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAddonInstance  **
  - **IAM action:**  [ses:DeleteAddonInstance](#list_mailmanager-action-DeleteAddonInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAddonSubscription  **
  - **IAM action:**  [ses:DeleteAddonSubscription](#list_mailmanager-action-DeleteAddonSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAddressList  **
  - **IAM action:**  [ses:DeleteAddressList](#list_mailmanager-action-DeleteAddressList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteArchive  **
  - **IAM action:**  [ses:DeleteArchive](#list_mailmanager-action-DeleteArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIngressPoint  **
  - **IAM action:**  [ses:DeleteIngressPoint](#list_mailmanager-action-DeleteIngressPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRelay  **
  - **IAM action:**  [ses:DeleteRelay](#list_mailmanager-action-DeleteRelay) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRuleSet  **
  - **IAM action:**  [ses:DeleteRuleSet](#list_mailmanager-action-DeleteRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTrafficPolicy  **
  - **IAM action:**  [ses:DeleteTrafficPolicy](#list_mailmanager-action-DeleteTrafficPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterMemberFromAddressList  **
  - **IAM action:**  [ses:DeregisterMemberFromAddressList](#list_mailmanager-action-DeregisterMemberFromAddressList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAddonInstance  **
  - **IAM action:**  [ses:GetAddonInstance](#list_mailmanager-action-GetAddonInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAddonSubscription  **
  - **IAM action:**  [ses:GetAddonSubscription](#list_mailmanager-action-GetAddonSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAddressList  **
  - **IAM action:**  [ses:GetAddressList](#list_mailmanager-action-GetAddressList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAddressListImportJob  **
  - **IAM action:**  [ses:GetAddressListImportJob](#list_mailmanager-action-GetAddressListImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetArchive  **
  - **IAM action:**  [ses:GetArchive](#list_mailmanager-action-GetArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetArchiveExport  **
  - **IAM action:**  [ses:GetArchiveExport](#list_mailmanager-action-GetArchiveExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetArchiveMessage  **
  - **IAM action:**  [ses:GetArchiveMessage](#list_mailmanager-action-GetArchiveMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetArchiveMessageContent  **
  - **IAM action:**  [ses:GetArchiveMessageContent](#list_mailmanager-action-GetArchiveMessageContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetArchiveSearch  **
  - **IAM action:**  [ses:GetArchiveSearch](#list_mailmanager-action-GetArchiveSearch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetArchiveSearchResults  **
  - **IAM action:**  [ses:GetArchiveSearchResults](#list_mailmanager-action-GetArchiveSearchResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIngressPoint  **
  - **IAM action:**  [ses:GetIngressPoint](#list_mailmanager-action-GetIngressPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMemberOfAddressList  **
  - **IAM action:**  [ses:GetMemberOfAddressList](#list_mailmanager-action-GetMemberOfAddressList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRelay  **
  - **IAM action:**  [ses:GetRelay](#list_mailmanager-action-GetRelay) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRuleSet  **
  - **IAM action:**  [ses:GetRuleSet](#list_mailmanager-action-GetRuleSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTrafficPolicy  **
  - **IAM action:**  [ses:GetTrafficPolicy](#list_mailmanager-action-GetTrafficPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAddonInstances  **
  - **IAM action:**  [ses:ListAddonInstances](#list_mailmanager-action-ListAddonInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAddonSubscriptions  **
  - **IAM action:**  [ses:ListAddonSubscriptions](#list_mailmanager-action-ListAddonSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAddressListImportJobs  **
  - **IAM action:**  [ses:ListAddressListImportJobs](#list_mailmanager-action-ListAddressListImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAddressLists  **
  - **IAM action:**  [ses:ListAddressLists](#list_mailmanager-action-ListAddressLists) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListArchiveExports  **
  - **IAM action:**  [ses:ListArchiveExports](#list_mailmanager-action-ListArchiveExports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListArchiveSearches  **
  - **IAM action:**  [ses:ListArchiveSearches](#list_mailmanager-action-ListArchiveSearches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListArchives  **
  - **IAM action:**  [ses:ListArchives](#list_mailmanager-action-ListArchives) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIngressPoints  **
  - **IAM action:**  [ses:ListIngressPoints](#list_mailmanager-action-ListIngressPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMembersOfAddressList  **
  - **IAM action:**  [ses:ListMembersOfAddressList](#list_mailmanager-action-ListMembersOfAddressList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRelays  **
  - **IAM action:**  [ses:ListRelays](#list_mailmanager-action-ListRelays) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRuleSets  **
  - **IAM action:**  [ses:ListRuleSets](#list_mailmanager-action-ListRuleSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [ses:ListTagsForResource](#list_mailmanager-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTrafficPolicies  **
  - **IAM action:**  [ses:ListTrafficPolicies](#list_mailmanager-action-ListTrafficPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RegisterMemberToAddressList  **
  - **IAM action:**  [ses:RegisterMemberToAddressList](#list_mailmanager-action-RegisterMemberToAddressList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAddressListImportJob  **
  - **IAM action:**  [ses:StartAddressListImportJob](#list_mailmanager-action-StartAddressListImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartArchiveExport  **
  - **IAM action:**  [ses:StartArchiveExport](#list_mailmanager-action-StartArchiveExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartArchiveSearch  **
  - **IAM action:**  [ses:StartArchiveSearch](#list_mailmanager-action-StartArchiveSearch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopAddressListImportJob  **
  - **IAM action:**  [ses:StopAddressListImportJob](#list_mailmanager-action-StopAddressListImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopArchiveExport  **
  - **IAM action:**  [ses:StopArchiveExport](#list_mailmanager-action-StopArchiveExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopArchiveSearch  **
  - **IAM action:**  [ses:StopArchiveSearch](#list_mailmanager-action-StopArchiveSearch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [ses:TagResource](#list_mailmanager-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [ses:UntagResource](#list_mailmanager-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateArchive  **
  - **IAM action:**  [ses:UpdateArchive](#list_mailmanager-action-UpdateArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIngressPoint  **
  - **IAM action:**  [ses:UpdateIngressPoint](#list_mailmanager-action-UpdateIngressPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRelay  **
  - **IAM action:**  [ses:UpdateRelay](#list_mailmanager-action-UpdateRelay) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRuleSet  **
  - **IAM action:**  [ses:UpdateRuleSet](#list_mailmanager-action-UpdateRuleSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ses.amazonaws.com / **Access level:** Write

- **   UpdateTrafficPolicy  **
  - **IAM action:**  [ses:UpdateTrafficPolicy](#list_mailmanager-action-UpdateTrafficPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Simple Email Service - Mail Manager
<a name="list_mailmanager-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateAddonInstance](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateAddonInstance.html)  **
  - **Description:** Grants permission to create an addon instance
  - **Resource types (\*required):** [addon-instance\*](#list_mailmanager-resource-addon-instance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)<br />[ses:AddonSubscriptionArn](#list_mailmanager-ses_AddonSubscriptionArn)
  - **Access level:** Write

- **   [CreateAddonSubscription](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateAddonSubscription.html)  **
  - **Description:** Grants permission to create an addon subscription
  - **Resource types (\*required):** [addon-subscription\*](#list_mailmanager-resource-addon-subscription)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAddressList](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateAddressList.html)  **
  - **Description:** Grants permission to create an address list
  - **Resource types (\*required):** [mailmanager-address-list\*](#list_mailmanager-resource-mailmanager-address-list)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAddressListImportJob](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateAddressListImportJob.html)  **
  - **Description:** Grants permission to create an import job on an address list
  - **Resource types (\*required):** [mailmanager-address-list\*](#list_mailmanager-resource-mailmanager-address-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateArchive](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateArchive.html)  **
  - **Description:** Grants permission to create an archive
  - **Resource types (\*required):** [mailmanager-archive\*](#list_mailmanager-resource-mailmanager-archive)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIngressPoint](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateIngressPoint.html)  **
  - **Description:** Grants permission to create an ingress point
  - **Resource types (\*required):** [mailmanager-ingress-point\*](#list_mailmanager-resource-mailmanager-ingress-point)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)<br />[ses:MailManagerIngressPointType](#list_mailmanager-ses_MailManagerIngressPointType)<br />[ses:MailManagerRuleSetArn](#list_mailmanager-ses_MailManagerRuleSetArn)<br />[ses:MailManagerTrafficPolicyArn](#list_mailmanager-ses_MailManagerTrafficPolicyArn)
  - **Access level:** Write

- **   [CreateRelay](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateRelay.html)  **
  - **Description:** Grants permission to create a SMTP relay
  - **Resource types (\*required):** [mailmanager-smtp-relay\*](#list_mailmanager-resource-mailmanager-smtp-relay)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRuleSet](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateRuleSet.html)  **
  - **Description:** Grants permission to create a rule set
  - **Resource types (\*required):** [mailmanager-rule-set\*](#list_mailmanager-resource-mailmanager-rule-set)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTrafficPolicy](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateTrafficPolicy.html)  **
  - **Description:** Grants permission to create a traffic policy
  - **Resource types (\*required):** [mailmanager-traffic-policy\*](#list_mailmanager-resource-mailmanager-traffic-policy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAddonInstance](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeleteAddonInstance.html)  **
  - **Description:** Grants permission to delete an addon instance
  - **Resource types (\*required):** [addon-instance\*](#list_mailmanager-resource-addon-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAddonSubscription](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeleteAddonSubscription.html)  **
  - **Description:** Grants permission to delete an addon subscription
  - **Resource types (\*required):** [addon-subscription\*](#list_mailmanager-resource-addon-subscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAddressList](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeleteAddressList.html)  **
  - **Description:** Grants permission to delete an address list
  - **Resource types (\*required):** [mailmanager-address-list\*](#list_mailmanager-resource-mailmanager-address-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteArchive](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeleteArchive.html)  **
  - **Description:** Grants permission to delete an archive
  - **Resource types (\*required):** [mailmanager-archive\*](#list_mailmanager-resource-mailmanager-archive)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIngressPoint](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeleteIngressPoint.html)  **
  - **Description:** Grants permission to delete an ingress point
  - **Resource types (\*required):** [mailmanager-ingress-point\*](#list_mailmanager-resource-mailmanager-ingress-point)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[ses:MailManagerIngressPointType](#list_mailmanager-ses_MailManagerIngressPointType)
  - **Access level:** Write

- **   [DeleteRelay](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeleteRelay.html)  **
  - **Description:** Grants permission to delete a SMTP relay
  - **Resource types (\*required):** [mailmanager-smtp-relay\*](#list_mailmanager-resource-mailmanager-smtp-relay)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRuleSet](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeleteRuleSet.html)  **
  - **Description:** Grants permission to delete a rule set
  - **Resource types (\*required):** [mailmanager-rule-set\*](#list_mailmanager-resource-mailmanager-rule-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTrafficPolicy](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeleteTrafficPolicy.html)  **
  - **Description:** Grants permission to delete a traffic point
  - **Resource types (\*required):** [mailmanager-traffic-policy\*](#list_mailmanager-resource-mailmanager-traffic-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterMemberFromAddressList](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeregisterMemberFromAddressList.html)  **
  - **Description:** Grants permission to remove a member from an address list
  - **Resource types (\*required):** [mailmanager-address-list\*](#list_mailmanager-resource-mailmanager-address-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAddonInstance](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetAddonInstance.html)  **
  - **Description:** Grants permission to get information about an addon instance
  - **Resource types (\*required):** [addon-instance\*](#list_mailmanager-resource-addon-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAddonSubscription](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetAddonSubscription.html)  **
  - **Description:** Grants permission to get information about an addon subscription
  - **Resource types (\*required):** [addon-subscription\*](#list_mailmanager-resource-addon-subscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAddressList](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetAddressList.html)  **
  - **Description:** Grants permission to get information about an address list
  - **Resource types (\*required):** [mailmanager-address-list\*](#list_mailmanager-resource-mailmanager-address-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAddressListImportJob](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetAddressListImportJob.html)  **
  - **Description:** Grants permission to get information about an import job on an address list
  - **Resource types (\*required):** [mailmanager-address-list\*](#list_mailmanager-resource-mailmanager-address-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetArchive](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchive.html)  **
  - **Description:** Grants permission to get information about an archive
  - **Resource types (\*required):** [mailmanager-archive\*](#list_mailmanager-resource-mailmanager-archive)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetArchiveExport](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveExport.html)  **
  - **Description:** Grants permission to get information about an archive export
  - **Resource types (\*required):** [mailmanager-archive\*](#list_mailmanager-resource-mailmanager-archive)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetArchiveMessage](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveMessage.html)  **
  - **Description:** Grants permission to retrieve archived message
  - **Resource types (\*required):** [mailmanager-archive\*](#list_mailmanager-resource-mailmanager-archive)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetArchiveMessageContent](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveMessageContent.html)  **
  - **Description:** Grants permission to retrieve archived message content
  - **Resource types (\*required):** [mailmanager-archive\*](#list_mailmanager-resource-mailmanager-archive)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetArchiveSearch](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveSearch.html)  **
  - **Description:** Grants permission to get information about a search
  - **Resource types (\*required):** [mailmanager-archive\*](#list_mailmanager-resource-mailmanager-archive)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetArchiveSearchResults](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveSearchResults.html)  **
  - **Description:** Grants permission to get information about search results
  - **Resource types (\*required):** [mailmanager-archive\*](#list_mailmanager-resource-mailmanager-archive)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIngressPoint](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetIngressPoint.html)  **
  - **Description:** Grants permission to get information about an ingress point
  - **Resource types (\*required):** [mailmanager-ingress-point\*](#list_mailmanager-resource-mailmanager-ingress-point)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[ses:MailManagerIngressPointType](#list_mailmanager-ses_MailManagerIngressPointType)
  - **Access level:** Read

- **   [GetMemberOfAddressList](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetMemberOfAddressList.html)  **
  - **Description:** Grants permission to get information about a member in an address list
  - **Resource types (\*required):** [mailmanager-address-list\*](#list_mailmanager-resource-mailmanager-address-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRelay](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetRelay.html)  **
  - **Description:** Grants permission to get information about a SMTP relay
  - **Resource types (\*required):** [mailmanager-smtp-relay\*](#list_mailmanager-resource-mailmanager-smtp-relay)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRuleSet](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetRuleSet.html)  **
  - **Description:** Grants permission to get information about a rule set
  - **Resource types (\*required):** [mailmanager-rule-set\*](#list_mailmanager-resource-mailmanager-rule-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTrafficPolicy](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetTrafficPolicy.html)  **
  - **Description:** Grants permission to get information about a traffic policy
  - **Resource types (\*required):** [mailmanager-traffic-policy\*](#list_mailmanager-resource-mailmanager-traffic-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAddonInstances](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListAddonInstances.html)  **
  - **Description:** Grants permission to list all of the addon instances associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAddonSubscriptions](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListAddonSubscriptions.html)  **
  - **Description:** Grants permission to list all of the addon subscriptions associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAddressListImportJobs](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListAddressListImportJobs.html)  **
  - **Description:** Grants permission to list all of the import jobs associated with an address list
  - **Resource types (\*required):** [mailmanager-address-list\*](#list_mailmanager-resource-mailmanager-address-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAddressLists](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListAddressLists.html)  **
  - **Description:** Grants permission to list all of the address lists associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListArchiveExports](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListArchiveExports.html)  **
  - **Description:** Grants permission to list all of the archive exports associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListArchiveSearches](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListArchiveSearches.html)  **
  - **Description:** Grants permission to list all of the archive searches associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListArchives](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListArchives.html)  **
  - **Description:** Grants permission to list all of the archives associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIngressPoints](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListIngressPoints.html)  **
  - **Description:** Grants permission to list all of the ingress points associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMembersOfAddressList](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListMembersOfAddressList.html)  **
  - **Description:** Grants permission to list all of the members associated with an address list
  - **Resource types (\*required):** [mailmanager-address-list\*](#list_mailmanager-resource-mailmanager-address-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRelays](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListRelays.html)  **
  - **Description:** Grants permission to list all of the SMTP relays associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRuleSets](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListRuleSets.html)  **
  - **Description:** Grants permission to list all of the rule sets associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all of the tags associated with the resource
  - **Resource types (\*required):** [addon-instance](#list_mailmanager-resource-addon-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [addon-subscription](#list_mailmanager-resource-addon-subscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [mailmanager-archive](#list_mailmanager-resource-mailmanager-archive) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [mailmanager-ingress-point](#list_mailmanager-resource-mailmanager-ingress-point) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[ses:MailManagerIngressPointType](#list_mailmanager-ses_MailManagerIngressPointType)
  - **Resource types (\*required):** [mailmanager-rule-set](#list_mailmanager-resource-mailmanager-rule-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [mailmanager-smtp-relay](#list_mailmanager-resource-mailmanager-smtp-relay) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [mailmanager-traffic-policy](#list_mailmanager-resource-mailmanager-traffic-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTrafficPolicies](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListTrafficPolicies.html)  **
  - **Description:** Grants permission to list all of the traffic policies associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [RegisterMemberToAddressList](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RegisterMemberToAddressList.html)  **
  - **Description:** Grants permission to add a member to an address list
  - **Resource types (\*required):** [mailmanager-address-list\*](#list_mailmanager-resource-mailmanager-address-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAddressListImportJob](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_StartAddressListImportJob.html)  **
  - **Description:** Grants permission to start an import job on an address list
  - **Resource types (\*required):** [mailmanager-address-list\*](#list_mailmanager-resource-mailmanager-address-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartArchiveExport](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_StartArchiveExport.html)  **
  - **Description:** Grants permission to start an archive export
  - **Resource types (\*required):** [mailmanager-archive\*](#list_mailmanager-resource-mailmanager-archive)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartArchiveSearch](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_StartArchiveSearch.html)  **
  - **Description:** Grants permission to start an archive search
  - **Resource types (\*required):** [mailmanager-archive\*](#list_mailmanager-resource-mailmanager-archive)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopAddressListImportJob](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_StopAddressListImportJob.html)  **
  - **Description:** Grants permission to stop an ongoing import job on an address list
  - **Resource types (\*required):** [mailmanager-address-list\*](#list_mailmanager-resource-mailmanager-address-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopArchiveExport](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_StopArchiveExport.html)  **
  - **Description:** Grants permission to stop archive export
  - **Resource types (\*required):** [mailmanager-archive\*](#list_mailmanager-resource-mailmanager-archive)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopArchiveSearch](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_StopArchiveSearch.html)  **
  - **Description:** Grants permission to stop archive search
  - **Resource types (\*required):** [mailmanager-archive\*](#list_mailmanager-resource-mailmanager-archive)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags (keys and values) to a specified resource
  - **Resource types (\*required):** [addon-instance](#list_mailmanager-resource-addon-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Resource types (\*required):** [addon-subscription](#list_mailmanager-resource-addon-subscription) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Resource types (\*required):** [mailmanager-address-list](#list_mailmanager-resource-mailmanager-address-list) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Resource types (\*required):** [mailmanager-archive](#list_mailmanager-resource-mailmanager-archive) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Resource types (\*required):** [mailmanager-ingress-point](#list_mailmanager-resource-mailmanager-ingress-point) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)<br />[ses:MailManagerIngressPointType](#list_mailmanager-ses_MailManagerIngressPointType)
  - **Resource types (\*required):** [mailmanager-rule-set](#list_mailmanager-resource-mailmanager-rule-set) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Resource types (\*required):** [mailmanager-smtp-relay](#list_mailmanager-resource-mailmanager-smtp-relay) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Resource types (\*required):** [mailmanager-traffic-policy](#list_mailmanager-resource-mailmanager-traffic-policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mailmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags (keys and values) from a specified resource
  - **Resource types (\*required):** [addon-instance](#list_mailmanager-resource-addon-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Resource types (\*required):** [addon-subscription](#list_mailmanager-resource-addon-subscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Resource types (\*required):** [mailmanager-address-list](#list_mailmanager-resource-mailmanager-address-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Resource types (\*required):** [mailmanager-archive](#list_mailmanager-resource-mailmanager-archive) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Resource types (\*required):** [mailmanager-ingress-point](#list_mailmanager-resource-mailmanager-ingress-point) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)<br />[ses:MailManagerIngressPointType](#list_mailmanager-ses_MailManagerIngressPointType)
  - **Resource types (\*required):** [mailmanager-rule-set](#list_mailmanager-resource-mailmanager-rule-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Resource types (\*required):** [mailmanager-smtp-relay](#list_mailmanager-resource-mailmanager-smtp-relay) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Resource types (\*required):** [mailmanager-traffic-policy](#list_mailmanager-resource-mailmanager-traffic-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mailmanager-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateArchive](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_UpdateArchive.html)  **
  - **Description:** Grants permission to update an archive
  - **Resource types (\*required):** [mailmanager-archive\*](#list_mailmanager-resource-mailmanager-archive)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIngressPoint](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_UpdateIngressPoint.html)  **
  - **Description:** Grants permission to update an ingress point
  - **Resource types (\*required):** [mailmanager-ingress-point\*](#list_mailmanager-resource-mailmanager-ingress-point)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[ses:MailManagerIngressPointType](#list_mailmanager-ses_MailManagerIngressPointType)<br />[ses:MailManagerRuleSetArn](#list_mailmanager-ses_MailManagerRuleSetArn)<br />[ses:MailManagerTrafficPolicyArn](#list_mailmanager-ses_MailManagerTrafficPolicyArn)
  - **Access level:** Write

- **   [UpdateRelay](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_UpdateRelay.html)  **
  - **Description:** Grants permission to update a SMTP relay
  - **Resource types (\*required):** [mailmanager-smtp-relay\*](#list_mailmanager-resource-mailmanager-smtp-relay)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRuleSet](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_UpdateRuleSet.html)  **
  - **Description:** Grants permission to update a rule set
  - **Resource types (\*required):** [mailmanager-rule-set\*](#list_mailmanager-resource-mailmanager-rule-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTrafficPolicy](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_UpdateTrafficPolicy.html)  **
  - **Description:** Grants permission to update a traffic policy
  - **Resource types (\*required):** [mailmanager-traffic-policy\*](#list_mailmanager-resource-mailmanager-traffic-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Simple Email Service - Mail Manager
<a name="list_mailmanager-permission-only-actions"></a>

The following actions are defined by Amazon Simple Email Service - Mail Manager but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/ses/latest/dg/eb-policies.html)  **
  - **Description:** Grants permission to configure vended log delivery for Mail Manager resources
  - **Resource types (\*required):** [mailmanager-ingress-point](#list_mailmanager-resource-mailmanager-ingress-point) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[ses:MailManagerIngressPointType](#list_mailmanager-ses_MailManagerIngressPointType)
  - **Resource types (\*required):** [mailmanager-rule-set](#list_mailmanager-resource-mailmanager-rule-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write



## Resource types defined by Amazon Simple Email Service - Mail Manager
<a name="list_mailmanager-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [addon-instance](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_AddonInstance.html)  | arn:${Partition}:ses:${Region}:${Account}:addon-instance/${AddonInstanceId} | [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_) | 
|  [addon-subscription](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_AddonSubscription.html)  | arn:${Partition}:ses:${Region}:${Account}:addon-subscription/${AddonSubscriptionId} | [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_) | 
|  [mailmanager-address-list](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_AddressList.html)  | arn:${Partition}:ses:${Region}:${Account}:mailmanager-address-list/${AddressListId} | [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_) | 
|  [mailmanager-archive](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_Archive.html)  | arn:${Partition}:ses:${Region}:${Account}:mailmanager-archive/${ArchiveId} | [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_) | 
|  [mailmanager-ingress-point](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressPoint.html)  | arn:${Partition}:ses:${Region}:${Account}:mailmanager-ingress-point/${IngressPointId} | [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_)<br />[ses:MailManagerIngressPointType](#list_mailmanager-ses_MailManagerIngressPointType) | 
|  [mailmanager-rule-set](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleSet.html)  | arn:${Partition}:ses:${Region}:${Account}:mailmanager-rule-set/${RuleSetId} | [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_) | 
|  [mailmanager-smtp-relay](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_Relay.html)  | arn:${Partition}:ses:${Region}:${Account}:mailmanager-smtp-relay/${RelayId} | [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_) | 
|  [mailmanager-traffic-policy](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_TrafficPolicy.html)  | arn:${Partition}:ses:${Region}:${Account}:mailmanager-traffic-policy/${TrafficPolicyId} | [aws:ResourceTag/${TagKey}](#list_mailmanager-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Simple Email Service - Mail Manager
<a name="list_mailmanager-policy-keys"></a>

Amazon Simple Email Service - Mail Manager defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [ses:AddonSubscriptionArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsesmailmanager.html#amazonsesmailmanager-policy-keys)  | Filters access by SES Addon Subscription ARN | ARN | 
|   [ses:MailManagerIngressPointType](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsesmailmanager.html#amazonsesmailmanager-policy-keys)  | Filters access by SES Mail Manager ingress point type, for example OPEN or AUTH | String | 
|   [ses:MailManagerRuleSetArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsesmailmanager.html#amazonsesmailmanager-policy-keys)  | Filters access by SES Mail Manager rule set ARN | ARN | 
|   [ses:MailManagerTrafficPolicyArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsesmailmanager.html#amazonsesmailmanager-policy-keys)  | Filters access by SES Mail Manager traffic policy ARN | ARN | 