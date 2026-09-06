

# Actions, resources, and condition keys for Amazon Mechanical Turk
<a name="list_mturk"></a>

Amazon Mechanical Turk (service prefix: `mechanicalturk`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/SetUp.html#create-iam-user-or-role) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mechanicalturk/mechanicalturk.json) for this service.

**Topics**
+ [API operations defined by Amazon Mechanical Turk](#list_mturk-operations)
+ [Actions defined by Amazon Mechanical Turk](#list_mturk-actions-as-permissions)
+ [Resource types defined by Amazon Mechanical Turk](#list_mturk-resources-for-iam-policies)
+ [Condition keys for Amazon Mechanical Turk](#list_mturk-policy-keys)

## API operations defined by Amazon Mechanical Turk
<a name="list_mturk-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mturk-actions-as-permissions).




- **   AcceptQualificationRequest  **
  - **IAM action:**  [mechanicalturk:AcceptQualificationRequest](#list_mturk-action-AcceptQualificationRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ApproveAssignment  **
  - **IAM action:**  [mechanicalturk:ApproveAssignment](#list_mturk-action-ApproveAssignment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateQualificationWithWorker  **
  - **IAM action:**  [mechanicalturk:AssociateQualificationWithWorker](#list_mturk-action-AssociateQualificationWithWorker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAdditionalAssignmentsForHIT  **
  - **IAM action:**  [mechanicalturk:CreateAdditionalAssignmentsForHIT](#list_mturk-action-CreateAdditionalAssignmentsForHIT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateHIT  **
  - **IAM action:**  [mechanicalturk:CreateHIT](#list_mturk-action-CreateHIT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateHITType  **
  - **IAM action:**  [mechanicalturk:CreateHITType](#list_mturk-action-CreateHITType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateHITWithHITType  **
  - **IAM action:**  [mechanicalturk:CreateHITWithHITType](#list_mturk-action-CreateHITWithHITType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateQualificationType  **
  - **IAM action:**  [mechanicalturk:CreateQualificationType](#list_mturk-action-CreateQualificationType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWorkerBlock  **
  - **IAM action:**  [mechanicalturk:CreateWorkerBlock](#list_mturk-action-CreateWorkerBlock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHIT  **
  - **IAM action:**  [mechanicalturk:DeleteHIT](#list_mturk-action-DeleteHIT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQualificationType  **
  - **IAM action:**  [mechanicalturk:DeleteQualificationType](#list_mturk-action-DeleteQualificationType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkerBlock  **
  - **IAM action:**  [mechanicalturk:DeleteWorkerBlock](#list_mturk-action-DeleteWorkerBlock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateQualificationFromWorker  **
  - **IAM action:**  [mechanicalturk:DisassociateQualificationFromWorker](#list_mturk-action-DisassociateQualificationFromWorker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountBalance  **
  - **IAM action:**  [mechanicalturk:GetAccountBalance](#list_mturk-action-GetAccountBalance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssignment  **
  - **IAM action:**  [mechanicalturk:GetAssignment](#list_mturk-action-GetAssignment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFileUploadURL  **
  - **IAM action:**  [mechanicalturk:GetFileUploadURL](#list_mturk-action-GetFileUploadURL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetHIT  **
  - **IAM action:**  [mechanicalturk:GetHIT](#list_mturk-action-GetHIT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQualificationScore  **
  - **IAM action:**  [mechanicalturk:GetQualificationScore](#list_mturk-action-GetQualificationScore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQualificationType  **
  - **IAM action:**  [mechanicalturk:GetQualificationType](#list_mturk-action-GetQualificationType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAssignmentsForHIT  **
  - **IAM action:**  [mechanicalturk:ListAssignmentsForHIT](#list_mturk-action-ListAssignmentsForHIT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBonusPayments  **
  - **IAM action:**  [mechanicalturk:ListBonusPayments](#list_mturk-action-ListBonusPayments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHITs  **
  - **IAM action:**  [mechanicalturk:ListHITs](#list_mturk-action-ListHITs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHITsForQualificationType  **
  - **IAM action:**  [mechanicalturk:ListHITsForQualificationType](#list_mturk-action-ListHITsForQualificationType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQualificationRequests  **
  - **IAM action:**  [mechanicalturk:ListQualificationRequests](#list_mturk-action-ListQualificationRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQualificationTypes  **
  - **IAM action:**  [mechanicalturk:ListQualificationTypes](#list_mturk-action-ListQualificationTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReviewPolicyResultsForHIT  **
  - **IAM action:**  [mechanicalturk:ListReviewPolicyResultsForHIT](#list_mturk-action-ListReviewPolicyResultsForHIT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReviewableHITs  **
  - **IAM action:**  [mechanicalturk:ListReviewableHITs](#list_mturk-action-ListReviewableHITs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkerBlocks  **
  - **IAM action:**  [mechanicalturk:ListWorkerBlocks](#list_mturk-action-ListWorkerBlocks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkersWithQualificationType  **
  - **IAM action:**  [mechanicalturk:ListWorkersWithQualificationType](#list_mturk-action-ListWorkersWithQualificationType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   NotifyWorkers  **
  - **IAM action:**  [mechanicalturk:NotifyWorkers](#list_mturk-action-NotifyWorkers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectAssignment  **
  - **IAM action:**  [mechanicalturk:RejectAssignment](#list_mturk-action-RejectAssignment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectQualificationRequest  **
  - **IAM action:**  [mechanicalturk:RejectQualificationRequest](#list_mturk-action-RejectQualificationRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendBonus  **
  - **IAM action:**  [mechanicalturk:SendBonus](#list_mturk-action-SendBonus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendTestEventNotification  **
  - **IAM action:**  [mechanicalturk:SendTestEventNotification](#list_mturk-action-SendTestEventNotification) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateExpirationForHIT  **
  - **IAM action:**  [mechanicalturk:UpdateExpirationForHIT](#list_mturk-action-UpdateExpirationForHIT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateHITReviewStatus  **
  - **IAM action:**  [mechanicalturk:UpdateHITReviewStatus](#list_mturk-action-UpdateHITReviewStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateHITTypeOfHIT  **
  - **IAM action:**  [mechanicalturk:UpdateHITTypeOfHIT](#list_mturk-action-UpdateHITTypeOfHIT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNotificationSettings  **
  - **IAM action:**  [mechanicalturk:UpdateNotificationSettings](#list_mturk-action-UpdateNotificationSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQualificationType  **
  - **IAM action:**  [mechanicalturk:UpdateQualificationType](#list_mturk-action-UpdateQualificationType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Mechanical Turk
<a name="list_mturk-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AcceptQualificationRequest](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_AcceptQualificationRequestOperation.html)  | The AcceptQualificationRequest operation grants a Worker's request for a Qualification |  |   | Write | 
|   [ApproveAssignment](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ApproveAssignmentOperation.html)  | The ApproveAssignment operation approves the results of a completed assignment |  |   | Write | 
|   [AssociateQualificationWithWorker](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_AssociateQualificationWithWorkerOperation.html)  | The AssociateQualificationWithWorker operation gives a Worker a Qualification |  |   | Write | 
|   [CreateAdditionalAssignmentsForHIT](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateAdditionalAssignmentsForHITOperation.html)  | The CreateAdditionalAssignmentsForHIT operation increases the maximum number of assignments of an existing HIT |  |   | Write | 
|   [CreateHIT](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateHITOperation.html)  | The CreateHIT operation creates a new HIT (Human Intelligence Task) |  |   | Write | 
|   [CreateHITType](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateHITTypeOperation.html)  | The CreateHITType operation creates a new HIT type |  |   | Write | 
|   [CreateHITWithHITType](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateHITWithHITTypeOperation.html)  | The CreateHITWithHITType operation creates a new Human Intelligence Task (HIT) using an existing HITTypeID generated by the CreateHITType operation |  |   | Write | 
|   [CreateQualificationType](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateQualificationTypeOperation.html)  | The CreateQualificationType operation creates a new Qualification type, which is represented by a QualificationType data structure |  |   | Write | 
|   [CreateWorkerBlock](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateWorkerBlockOperation.html)  | The CreateWorkerBlock operation allows you to prevent a Worker from working on your HITs |  |   | Write | 
|   [DeleteHIT](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_DeleteHITOperation.html)  | The DeleteHIT operation disposes of a HIT that is no longer needed |  |   | Write | 
|   [DeleteQualificationType](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_DeleteQualificationTypeOperation.html)  | The DeleteQualificationType disposes a Qualification type and disposes any HIT types that are associated with the Qualification type |  |   | Write | 
|   [DeleteWorkerBlock](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_DeleteWorkerBlockOperation.html)  | The DeleteWorkerBlock operation allows you to reinstate a blocked Worker to work on your HITs |  |   | Write | 
|   [DisassociateQualificationFromWorker](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_DisassociateQualificationFromWorkerOperation.html)  | The DisassociateQualificationFromWorker revokes a previously granted Qualification from a user |  |   | Write | 
|   [GetAccountBalance](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetAccountBalanceOperation.html)  | The GetAccountBalance operation retrieves the amount of money in your Amazon Mechanical Turk account |  |   | Read | 
|   [GetAssignment](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetAssignmentOperation.html)  | The GetAssignment retrieves an assignment with an AssignmentStatus value of Submitted, Approved, or Rejected, using the assignment's ID |  |   | Read | 
|   [GetFileUploadURL](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetFileUploadURLOperation.html)  | The GetFileUploadURL operation generates and returns a temporary URL |  |   | Read | 
|   [GetHIT](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetHITOperation.html)  | The GetHIT operation retrieves the details of the specified HIT |  |   | Read | 
|   [GetQualificationScore](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetQualificationScoreOperation.html)  | The GetQualificationScore operation returns the value of a Worker's Qualification for a given Qualification type |  |   | Read | 
|   [GetQualificationType](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetQualificationTypeOperation.html)  | The GetQualificationType operation retrieves information about a Qualification type using its ID |  |   | Read | 
|   [ListAssignmentsForHIT](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListAssignmentsForHITOperation.html)  | The ListAssignmentsForHIT operation retrieves completed assignments for a HIT |  |   | List | 
|   [ListBonusPayments](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListBonusPaymentsOperation.html)  | The ListBonusPayments operation retrieves the amounts of bonuses you have paid to Workers for a given HIT or assignment |  |   | List | 
|   [ListHITs](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListHITsOperation.html)  | The ListHITs operation returns all of a Requester's HITs |  |   | List | 
|   [ListHITsForQualificationType](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListHITsForQualificationTypeOperation.html)  | The ListHITsForQualificationType operation returns the HITs that use the given QualififcationType for a QualificationRequirement |  |   | List | 
|   [ListQualificationRequests](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListQualificationRequestsOperation.html)  | The ListQualificationRequests operation retrieves requests for Qualifications of a particular Qualification type |  |   | List | 
|   [ListQualificationTypes](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListQualificationTypesOperation.html)  | The ListQualificationTypes operation searches for Qualification types using the specified search query, and returns a list of Qualification types |  |   | List | 
|   [ListReviewPolicyResultsForHIT](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListReviewPolicyResultsForHITOperation.html)  | The ListReviewPolicyResultsForHIT operation retrieves the computed results and the actions taken in the course of executing your Review Policies during a CreateHIT operation |  |   | List | 
|   [ListReviewableHITs](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListReviewableHITsOperation.html)  | The ListReviewableHITs operation returns all of a Requester's HITs that have not been approved or rejected |  |   | List | 
|   [ListWorkerBlocks](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListWorkerBlocksOperation.html)  | The ListWorkersBlocks operation retrieves a list of Workers who are blocked from working on your HITs |  |   | List | 
|   [ListWorkersWithQualificationType](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListWorkersWithQualificationTypeOperation.html)  | The ListWorkersWithQualificationType operation returns all of the Workers with a given Qualification type |  |   | List | 
|   [NotifyWorkers](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_NotifyWorkersOperation.html)  | The NotifyWorkers operation sends an email to one or more Workers that you specify with the Worker ID |  |   | Write | 
|   [RejectAssignment](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_RejectAssignmentOperation.html)  | The RejectAssignment operation rejects the results of a completed assignment |  |   | Write | 
|   [RejectQualificationRequest](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_RejectQualificationRequestOperation.html)  | The RejectQualificationRequest operation rejects a user's request for a Qualification |  |   | Write | 
|   [SendBonus](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_SendBonusOperation.html)  | The SendBonus operation issues a payment of money from your account to a Worker |  |   | Write | 
|   [SendTestEventNotification](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_SendTestEventNotificationOperation.html)  | The SendTestEventNotification operation causes Amazon Mechanical Turk to send a notification message as if a HIT event occurred, according to the provided notification specification |  |   | Write | 
|   [UpdateExpirationForHIT](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_UpdateExpirationForHITOperation.html)  | The UpdateExpirationForHIT operation allows you extend the expiration time of a HIT beyond is current expiration or expire a HIT immediately |  |   | Write | 
|   [UpdateHITReviewStatus](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_UpdateHITReviewStatusOperation.html)  | The UpdateHITReviewStatus operation toggles the status of a HIT |  |   | Write | 
|   [UpdateHITTypeOfHIT](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_UpdateHITTypeOfHITOperation.html)  | The UpdateHITTypeOfHIT operation allows you to change the HITType properties of a HIT |  |   | Write | 
|   [UpdateNotificationSettings](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_UpdateNotificationSettingsOperation.html)  | The UpdateNotificationSettings operation creates, updates, disables or re-enables notifications for a HIT type |  |   | Write | 
|   [UpdateQualificationType](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_UpdateQualificationTypeOperation.html)  | The UpdateQualificationType operation modifies the attributes of an existing Qualification type, which is represented by a QualificationType data structure |  |   | Write | 

## Resource types defined by Amazon Mechanical Turk
<a name="list_mturk-resources-for-iam-policies"></a>

Amazon Mechanical Turk does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon Mechanical Turk
<a name="list_mturk-policy-keys"></a>

Amazon Mechanical Turk has no service-specific condition keys that can be used in the `Condition` element of policy statements.