

# Actions, resources, and condition keys for Amazon Connect Voice ID
<a name="list_voice-id"></a>

Amazon Connect Voice ID (service prefix: `voiceid`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/connect/latest/adminguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/voiceid/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/console/connect/security/access-control/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/voiceid/voiceid.json) for this service.

**Topics**
+ [API operations defined by Amazon Connect Voice ID](#list_voice-id-operations)
+ [Actions defined by Amazon Connect Voice ID](#list_voice-id-actions-as-permissions)
+ [Permission-only actions for Amazon Connect Voice ID](#list_voice-id-permission-only-actions)
+ [Resource types defined by Amazon Connect Voice ID](#list_voice-id-resources-for-iam-policies)
+ [Condition keys for Amazon Connect Voice ID](#list_voice-id-policy-keys)

## API operations defined by Amazon Connect Voice ID
<a name="list_voice-id-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_voice-id-actions-as-permissions).




- **   AssociateFraudster  **
  - **IAM action:**  [voiceid:AssociateFraudster](#list_voice-id-action-AssociateFraudster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDomain  **
  - **IAM action:**  [voiceid:CreateDomain](#list_voice-id-action-CreateDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [voiceid:TagResource](#list_voice-id-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateWatchlist  **
  - **IAM action:**  [voiceid:CreateWatchlist](#list_voice-id-action-CreateWatchlist) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomain  **
  - **IAM action:**  [voiceid:DeleteDomain](#list_voice-id-action-DeleteDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFraudster  **
  - **IAM action:**  [voiceid:DeleteFraudster](#list_voice-id-action-DeleteFraudster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSpeaker  **
  - **IAM action:**  [voiceid:DeleteSpeaker](#list_voice-id-action-DeleteSpeaker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWatchlist  **
  - **IAM action:**  [voiceid:DeleteWatchlist](#list_voice-id-action-DeleteWatchlist) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeDomain  **
  - **IAM action:**  [voiceid:DescribeDomain](#list_voice-id-action-DescribeDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFraudster  **
  - **IAM action:**  [voiceid:DescribeFraudster](#list_voice-id-action-DescribeFraudster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFraudsterRegistrationJob  **
  - **IAM action:**  [voiceid:DescribeFraudsterRegistrationJob](#list_voice-id-action-DescribeFraudsterRegistrationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSpeaker  **
  - **IAM action:**  [voiceid:DescribeSpeaker](#list_voice-id-action-DescribeSpeaker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSpeakerEnrollmentJob  **
  - **IAM action:**  [voiceid:DescribeSpeakerEnrollmentJob](#list_voice-id-action-DescribeSpeakerEnrollmentJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWatchlist  **
  - **IAM action:**  [voiceid:DescribeWatchlist](#list_voice-id-action-DescribeWatchlist) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateFraudster  **
  - **IAM action:**  [voiceid:DisassociateFraudster](#list_voice-id-action-DisassociateFraudster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EvaluateSession  **
  - **IAM action:**  [voiceid:EvaluateSession](#list_voice-id-action-EvaluateSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListDomains  **
  - **IAM action:**  [voiceid:ListDomains](#list_voice-id-action-ListDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFraudsterRegistrationJobs  **
  - **IAM action:**  [voiceid:ListFraudsterRegistrationJobs](#list_voice-id-action-ListFraudsterRegistrationJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFraudsters  **
  - **IAM action:**  [voiceid:ListFraudsters](#list_voice-id-action-ListFraudsters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSpeakerEnrollmentJobs  **
  - **IAM action:**  [voiceid:ListSpeakerEnrollmentJobs](#list_voice-id-action-ListSpeakerEnrollmentJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSpeakers  **
  - **IAM action:**  [voiceid:ListSpeakers](#list_voice-id-action-ListSpeakers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [voiceid:ListTagsForResource](#list_voice-id-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWatchlists  **
  - **IAM action:**  [voiceid:ListWatchlists](#list_voice-id-action-ListWatchlists) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   OptOutSpeaker  **
  - **IAM action:**  [voiceid:OptOutSpeaker](#list_voice-id-action-OptOutSpeaker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartFraudsterRegistrationJob  **
  - **IAM action:**  [voiceid:StartFraudsterRegistrationJob](#list_voice-id-action-StartFraudsterRegistrationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** voiceid.amazonaws.com / **Access level:** Write

- **   StartSpeakerEnrollmentJob  **
  - **IAM action:**  [voiceid:StartSpeakerEnrollmentJob](#list_voice-id-action-StartSpeakerEnrollmentJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** voiceid.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [voiceid:TagResource](#list_voice-id-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [voiceid:UntagResource](#list_voice-id-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDomain  **
  - **IAM action:**  [voiceid:UpdateDomain](#list_voice-id-action-UpdateDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWatchlist  **
  - **IAM action:**  [voiceid:UpdateWatchlist](#list_voice-id-action-UpdateWatchlist) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Connect Voice ID
<a name="list_voice-id-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateFraudster](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_AssociateFraudster.html)  **
  - **Description:** Grants permission to associate a fraudster with a watchlist
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDomain](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_CreateDomain.html)  **
  - **Description:** Grants permission to create a domain
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_voice-id-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_voice-id-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWatchlist](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_CreateWatchlist.html)  **
  - **Description:** Grants permission to create a watchlist
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomain](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_DeleteDomain.html)  **
  - **Description:** Grants permission to delete a domain
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFraudster](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_DeleteFraudster.html)  **
  - **Description:** Grants permission to delete a fraudster
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSpeaker](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_DeleteSpeaker.html)  **
  - **Description:** Grants permission to delete a speaker
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWatchlist](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_DeleteWatchlist.html)  **
  - **Description:** Grants permission to delete a watchlist
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeDomain](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_DescribeDomain.html)  **
  - **Description:** Grants permission to describe a domain
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFraudster](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_DescribeFraudster.html)  **
  - **Description:** Grants permission to describe a fraudster
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFraudsterRegistrationJob](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_DescribeFraudsterRegistrationJob.html)  **
  - **Description:** Grants permission to describe a fraudster registration job
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSpeaker](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_DescribeSpeaker.html)  **
  - **Description:** Grants permission to describe a speaker
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSpeakerEnrollmentJob](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_DescribeSpeakerEnrollmentJob.html)  **
  - **Description:** Grants permission to describe a speaker enrollment job
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWatchlist](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_DescribeWatchlist.html)  **
  - **Description:** Grants permission to describe a watchlist
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateFraudster](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_DisassociateFraudster.html)  **
  - **Description:** Grants permission to disassociate a fraudster from a watchlist
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EvaluateSession](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_EvaluateSession.html)  **
  - **Description:** Grants permission to evaluate a session
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListDomains](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_ListDomains.html)  **
  - **Description:** Grants permission to list domains for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFraudsterRegistrationJobs](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_ListFraudsterRegistrationJobs.html)  **
  - **Description:** Grants permission to list fraudster registration jobs for a domain
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFraudsters](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_ListFraudsters.html)  **
  - **Description:** Grants permission to list fraudsters for a domain or watchlist
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSpeakerEnrollmentJobs](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_ListSpeakerEnrollmentJobs.html)  **
  - **Description:** Grants permission to list speaker enrollment jobs for a domain
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSpeakers](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_ListSpeakers.html)  **
  - **Description:** Grants permission to list speakers for a domain
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a Voice ID resource
  - **Resource types (\*required):** [domain](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWatchlists](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_ListWatchlists.html)  **
  - **Description:** Grants permission to list watchlists for a domain
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [OptOutSpeaker](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_OptOutSpeaker.html)  **
  - **Description:** Grants permission to opt out a speaker
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFraudsterRegistrationJob](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_StartFraudsterRegistrationJob.html)  **
  - **Description:** Grants permission to start a fraudster registration job
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartSpeakerEnrollmentJob](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_StartSpeakerEnrollmentJob.html)  **
  - **Description:** Grants permission to start a speaker enrollment job
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a Voice ID resource
  - **Resource types (\*required):** [domain](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_voice-id-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_voice-id-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from a Voice ID resource
  - **Resource types (\*required):** [domain](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_voice-id-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDomain](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_UpdateDomain.html)  **
  - **Description:** Grants permission to update a domain
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWatchlist](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_UpdateWatchlist.html)  **
  - **Description:** Grants permission to update a watchlist
  - **Resource types (\*required):** [domain\*](#list_voice-id-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Connect Voice ID
<a name="list_voice-id-permission-only-actions"></a>

The following actions are defined by Amazon Connect Voice ID but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [DescribeComplianceConsent](https://docs.aws.amazon.com/connect/latest/adminguide/enable-voiceid.html#enable-voiceid-step1)  | Grants permission to describe compliance consent |  |   | Read | 
|   [RegisterComplianceConsent](https://docs.aws.amazon.com/connect/latest/adminguide/enable-voiceid.html#enable-voiceid-step1)  | Grants permission to register compliance consent |  |   | Write | 

## Resource types defined by Amazon Connect Voice ID
<a name="list_voice-id-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [domain](https://docs.aws.amazon.com/connect/latest/adminguide/enable-voiceid.html#voiceid-domain)  | arn:${Partition}:voiceid:${Region}:${Account}:domain/${DomainId} | [aws:ResourceTag/${TagKey}](#list_voice-id-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Connect Voice ID
<a name="list_voice-id-policy-keys"></a>

Amazon Connect Voice ID defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 