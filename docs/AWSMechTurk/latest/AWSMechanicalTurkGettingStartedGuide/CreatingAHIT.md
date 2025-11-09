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

Workflow for Requesters | 1 | Define your HIT.<br>Construct your question in one of the<br>[Question and Answer Data Structure](../AWSMturkAPI/ApiReference_QuestionAnswerDataArticle.md "../AWSMturkAPI/ApiReference_QuestionAnswerDataArticle.md").<br>The Question paramater accepts a XML string or HTML string. |
| 2 | Create HIT.<br>Build a new HIT with the<br>[CreateHIT](../AWSMturkAPI/ApiReference_CreateHITOperation.md "../AWSMturkAPI/ApiReference_CreateHITOperation.md")<br>operation or [CreateHITwithHITType](../AWSMturkAPI/ApiReference_CreateHITWithHITTypeOperation.md "../AWSMturkAPI/ApiReference_CreateHITWithHITTypeOperation.md")<br>operation.<br>Provide [Title,<br>Description, Keywords, and Question Details](../AWSMturkAPI/Concepts_HITsArticle.md "../AWSMturkAPI/Concepts_HITsArticle.md") as outlined in the<br>documentation<br>For code samples demonstrating how to use the _Amazon Mechanical Turk<br>Requester API_, go to [AWSLabs on<br>Github.](https://github.com/awslabs/mturk-code-samples "https://github.com/awslabs/mturk-code-samples")<br>For language-specific support about using *Amazon Mechanical Turk Requester API<br>• go to [AWS SDKs](https://aws.amazon.com/tools/#sdk "https://aws.amazon.com/tools/#sdk") |
| 3 | Test your HIT.<br>Publish your HIT on the *Amazon Mechanical Turk Developer<br>Sandbox*. The *Amazon Mechanical Turk<br>Developer Sandbox<br>• is a simulated environment that<br>allows you to view your HIT as it would appear to Workers.<br>For more information about the \*Amazon Mechanical<br>Turk Developer Sandbox<br>• and how to use it, go to the<br>[Amazon Mechanical<br>Turk Developer Sandbox](https://requestersandbox.mturk.com/ "https://requestersandbox.mturk.com/"). |
| 4 | Publish your HIT on the Amazon Mechanical Turk production system.<br>This step makes your HIT available to Workers. |
| 5 | Workers accept your HIT and complete the assignment.<br>You can view the status of your HITs with [AWS Shell](https://github.com/awslabs/aws-shell "https://github.com/awslabs/aws-shell")<br>or the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). |
| 6 | Process the assignment results.<br>When a Worker completes an assignment, you can view the<br>results, output the results to a file, and accept or reject the<br>work. Accepting the work means that you agree to pay the<br>Worker.<br>Use [List Assignments for a HIT](../AWSMturkAPI/ApiReference_ListAssignmentsForHITOperation.md "../AWSMturkAPI/ApiReference_ListAssignmentsForHITOperation.md") to get results<br>once<br>Workers have completed the Assignment. Then you can process the<br>results with the [ApproveAssignment](../AWSMturkAPI/ApiReference_ApproveAssignmentOperation.md "../AWSMturkAPI/ApiReference_ApproveAssignmentOperation.md") operation and [RejectAssignment](../AWSMturkAPI/ApiReference_RejectAssignmentOperation.md "../AWSMturkAPI/ApiReference_RejectAssignmentOperation.md") operation. |
| 7 | Manage your HIT.<br>You can extend the completion time for your HIT, expire the HIT<br>early, add additional assignments, modify the HIT properties, or<br>block Workers whose work does not meet your standards. |
