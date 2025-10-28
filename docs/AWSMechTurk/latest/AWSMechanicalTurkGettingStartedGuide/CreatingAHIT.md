# Creating a HIT

In the previous section, you set up your AWS account and
installed the programming tools you need to use Amazon Mechanical Turk.
The following topics describe how to write, test, publish,
and manage a Human Intelligence Task (HIT).

###### Topics

- [Workflow](#workflow "#workflow")

## Workflow

The following procedure gives you an overview of creating, testing, publishing, and
managing a HIT.

Workflow for Requesters | 1 | Define your HIT.
Construct your question in one of the
[Question and Answer Data Structure](../AWSMturkAPI/ApiReference_QuestionAnswerDataArticle.md "../AWSMturkAPI/ApiReference_QuestionAnswerDataArticle.md").
The Question paramater accepts a XML string or HTML string.
|
| 2 | Create HIT. Build a new HIT with the [CreateHIT](../AWSMturkAPI/ApiReference_CreateHITOperation.md "../AWSMturkAPI/ApiReference_CreateHITOperation.md") operation or [CreateHITwithHITType](../AWSMturkAPI/ApiReference_CreateHITWithHITTypeOperation.md "../AWSMturkAPI/ApiReference_CreateHITWithHITTypeOperation.md") operation. Provide [Title, Description, Keywords, and Question Details](../AWSMturkAPI/Concepts_HITsArticle.md "../AWSMturkAPI/Concepts_HITsArticle.md") as outlined in the documentation For code samples demonstrating how to use the _Amazon Mechanical Turk Requester API_, go to [AWSLabs on Github.](https://github.com/awslabs/mturk-code-samples "https://github.com/awslabs/mturk-code-samples") For language-specific support about using _Amazon Mechanical Turk Requester API_ go to [AWS SDKs](https://aws.amazon.com/tools/#sdk "https://aws.amazon.com/tools/#sdk") |
| 3 | Test your HIT. Publish your HIT on the _Amazon Mechanical Turk Developer Sandbox_. The _Amazon Mechanical Turk Developer Sandbox_ is a simulated environment that allows you to view your HIT as it would appear to Workers. For more information about the _Amazon Mechanical Turk Developer Sandbox_ and how to use it, go to the [Amazon Mechanical Turk Developer Sandbox](https://requestersandbox.mturk.com/ "https://requestersandbox.mturk.com/"). |
| 4 | Publish your HIT on the Amazon Mechanical Turk production system. This step makes your HIT available to Workers. |
| 5 | Workers accept your HIT and complete the assignment. You can view the status of your HITs with [AWS Shell](https://github.com/awslabs/aws-shell "https://github.com/awslabs/aws-shell") or the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). |
| 6 | Process the assignment results. When a Worker completes an assignment, you can view the results, output the results to a file, and accept or reject the work. Accepting the work means that you agree to pay the Worker. Use [List Assignments for a HIT](../AWSMturkAPI/ApiReference_ListAssignmentsForHITOperation.md "../AWSMturkAPI/ApiReference_ListAssignmentsForHITOperation.md") to get results once Workers have completed the Assignment. Then you can process the results with the [ApproveAssignment](../AWSMturkAPI/ApiReference_ApproveAssignmentOperation.md "../AWSMturkAPI/ApiReference_ApproveAssignmentOperation.md") operation and [RejectAssignment](../AWSMturkAPI/ApiReference_RejectAssignmentOperation.md "../AWSMturkAPI/ApiReference_RejectAssignmentOperation.md") operation. |
| 7 | Manage your HIT. You can extend the completion time for your HIT, expire the HIT early, add additional assignments, modify the HIT properties, or block Workers whose work does not meet your standards. |
