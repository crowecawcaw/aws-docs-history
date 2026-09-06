

# Creating a HIT
<a name="CreatingAHIT"></a>

In the previous section, you set up your AWS account and installed the programming tools you need to use Amazon Mechanical Turk. The following topics describe how to write, test, publish, and manage a Human Intelligence Task (HIT).

**Topics**
+ [Workflow for Requesters](#workflow)

## Workflow
<a name="workflow"></a>

 The following procedure gives you an overview of creating, testing, publishing, and managing a HIT.


**Workflow for Requesters**  

|  |  | 
| --- |--- |
| 1 |  Define your HIT. <br /> Construct your question in one of the [Question and Answer Data Structure](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QuestionAnswerDataArticle.html). The Question paramater accepts a XML string or HTML string. <br />  | 
| 2 |  Create HIT. <br /> Build a new HIT with the [CreateHIT](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateHITOperation.html) operation or [CreateHITwithHITType](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateHITWithHITTypeOperation.html) operation. <br /> Provide [Title, Description, Keywords, and Question Details](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Concepts_HITsArticle.html) as outlined in the documentation<br /> For code samples demonstrating how to use the *Amazon Mechanical Turk Requester API*, go to [AWSLabs on Github.](https://github.com/awslabs/mturk-code-samples) <br /> For language-specific support about using *Amazon Mechanical Turk Requester API* go to [AWS SDKs](https://aws.amazon.com/tools/#sdk) | 
| 3 |  Test your HIT. <br /> Publish your HIT on the * Amazon Mechanical Turk Developer Sandbox*. The *Amazon Mechanical Turk Developer Sandbox* is a simulated environment that allows you to view your HIT as it would appear to Workers. <br /> For more information about the *Amazon Mechanical Turk Developer Sandbox* and how to use it, go to the [ Amazon Mechanical Turk Developer Sandbox](https://requestersandbox.mturk.com/).  | 
| 4 |  Publish your HIT on the Amazon Mechanical Turk production system. <br /> This step makes your HIT available to Workers.  | 
| 5 | Workers accept your HIT and complete the assignment. <br /> You can view the status of your HITs with [AWS Shell](https://github.com/awslabs/aws-shell) or the [AWS CLI](https://aws.amazon.com/cli/). | 
| 6 |  Process the assignment results. <br /> When a Worker completes an assignment, you can view the results, output the results to a file, and accept or reject the work. Accepting the work means that you agree to pay the Worker.<br />Use [List Assignments for a HIT](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListAssignmentsForHITOperation.html) to get results once Workers have completed the Assignment. Then you can process the results with the [ApproveAssignment](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ApproveAssignmentOperation.html) operation and [RejectAssignment](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_RejectAssignmentOperation.html) operation. | 
| 7 |  Manage your HIT. <br />You can extend the completion time for your HIT, expire the HIT early, add additional assignments, modify the HIT properties, or block Workers whose work does not meet your standards.  | 