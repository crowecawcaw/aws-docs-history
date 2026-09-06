

# Data retrieval APIs for Amazon Mechanical Turk
<a name="amazonmechanicalturk"></a>

Amazon Mechanical Turk provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="mechanicalturk-GetAccountBalance"></a>[GetAccountBalance](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetAccountBalanceOperation.html) | The GetAccountBalance operation retrieves the amount of money in your Amazon Mechanical Turk account | Read | 
| <a name="mechanicalturk-GetAssignment"></a>[GetAssignment](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetAssignmentOperation.html) | The GetAssignment retrieves an assignment with an AssignmentStatus value of Submitted, Approved, or Rejected, using the assignment's ID | Read | 
| <a name="mechanicalturk-GetFileUploadURL"></a>[GetFileUploadURL](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetFileUploadURLOperation.html) | The GetFileUploadURL operation generates and returns a temporary URL | Read | 
| <a name="mechanicalturk-GetHIT"></a>[GetHIT](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetHITOperation.html) | The GetHIT operation retrieves the details of the specified HIT | Read | 
| <a name="mechanicalturk-GetQualificationScore"></a>[GetQualificationScore](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetQualificationScoreOperation.html) | The GetQualificationScore operation returns the value of a Worker's Qualification for a given Qualification type | Read | 
| <a name="mechanicalturk-GetQualificationType"></a>[GetQualificationType](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetQualificationTypeOperation.html) | The GetQualificationType operation retrieves information about a Qualification type using its ID | Read | 
| <a name="mechanicalturk-ListAssignmentsForHIT"></a>[ListAssignmentsForHIT](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListAssignmentsForHITOperation.html) | The ListAssignmentsForHIT operation retrieves completed assignments for a HIT | List | 
| <a name="mechanicalturk-ListBonusPayments"></a>[ListBonusPayments](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListBonusPaymentsOperation.html) | The ListBonusPayments operation retrieves the amounts of bonuses you have paid to Workers for a given HIT or assignment | List | 
| <a name="mechanicalturk-ListHITs"></a>[ListHITs](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListHITsOperation.html) | The ListHITs operation returns all of a Requester's HITs | List | 
| <a name="mechanicalturk-ListHITsForQualificationType"></a>[ListHITsForQualificationType](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListHITsForQualificationTypeOperation.html) | The ListHITsForQualificationType operation returns the HITs that use the given QualififcationType for a QualificationRequirement | List | 
| <a name="mechanicalturk-ListQualificationRequests"></a>[ListQualificationRequests](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListQualificationRequestsOperation.html) | The ListQualificationRequests operation retrieves requests for Qualifications of a particular Qualification type | List | 
| <a name="mechanicalturk-ListQualificationTypes"></a>[ListQualificationTypes](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListQualificationTypesOperation.html) | The ListQualificationTypes operation searches for Qualification types using the specified search query, and returns a list of Qualification types | List | 
| <a name="mechanicalturk-ListReviewPolicyResultsForHIT"></a>[ListReviewPolicyResultsForHIT](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListReviewPolicyResultsForHITOperation.html) | The ListReviewPolicyResultsForHIT operation retrieves the computed results and the actions taken in the course of executing your Review Policies during a CreateHIT operation | List | 
| <a name="mechanicalturk-ListReviewableHITs"></a>[ListReviewableHITs](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListReviewableHITsOperation.html) | The ListReviewableHITs operation returns all of a Requester's HITs that have not been approved or rejected | List | 
| <a name="mechanicalturk-ListWorkerBlocks"></a>[ListWorkerBlocks](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListWorkerBlocksOperation.html) | The ListWorkersBlocks operation retrieves a list of Workers who are blocked from working on your HITs | List | 
| <a name="mechanicalturk-ListWorkersWithQualificationType"></a>[ListWorkersWithQualificationType](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListWorkersWithQualificationTypeOperation.html) | The ListWorkersWithQualificationType operation returns all of the Workers with a given Qualification type | List | 