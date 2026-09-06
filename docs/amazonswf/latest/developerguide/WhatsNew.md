

# Document history
<a name="WhatsNew"></a>

The following table describes the important changes to the documentation since the last release of the *Amazon Simple Workflow Service Developer Guide*.



| Change | Description | Date Changed | 
| --- | --- | --- | 
| Documentation-only update | Amazon SWF now includes a section about AWS User Notifications, an AWS service that acts as a central location for your AWS notifications in the AWS Management Console. For more information, see [Using AWS User Notifications with Amazon Simple Workflow Service](using-user-notifications-swf.md). | May 4, 2023 | 
| Update | Amazon SWF now provides a new console experience to manage SWF workflows and their execution-related actions. For more information, see [Amazon SWF console tutorials](swf-dg-using-console.md). | September 12, 2022 | 
| Update | Updated the [Quotas on Task Executions](swf-dg-limits.md#swf-dg-limits-tasks) section to include `Maximum tasks scheduled per second`, and the [Amazon SWF Metrics for CloudWatch](cw-metrics.md) page to include information about [using non-ASCII resource names](cw-metrics.md#cloudwatch-swf-non-ascii) with CloudWatch. | May 12, 2021 | 
| New feature | Amazon Simple Workflow Service now supports Amazon EventBridge. For more information, see: +  [EventBridge for Amazon SWF](ev-events.md) <br />+  [EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/)   | December 18, 2020 | 
| New feature | Amazon Simple Workflow Service supports IAM permissions using tags. For more information, see the following.+  [Tags in Amazon SWF](swf-dev-adv-tags.md)   [Manage tags](swf-dev-adv-tags.md#manage-tags)   [Tag workflow executions](swf-dev-adv-tags.md#swf-dg-tagging)   [Control access to domains with tags](swf-dev-adv-tags.md#swf-dg-tagging-iam)   <br />+  [`TagResource`](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TagResource.html) <br />+  [`UntagResource`](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_UntagResource.html) <br />+  [`ListTagsForResource`](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListTagsForResource.html) <br />+  [`RegisterDomain`](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterDomain.html)  | June 20, 2019 | 
| New feature | Amazon Simple Workflow Service is now available the Europe (Stockholm) region.  | December 12, 2018 | 
| Update | Improved the Amazon Simple Workflow Service topic on CloudTrail integration. See [Recording API calls with AWS CloudTrail](ct-logging.md). | August 7, 2018 | 
| Update | Added information on the new PendingTasks metric for CloudWatch. For more information, see [Amazon SWF Metrics](cw-metrics.md#cloudwatch-swf-metrics). | June 18, 2018 | 
| Update | Improved syntax highlighting in code samples. | March 29, 2018 | 
| Update | Added a topic describing options for Ruby Flow users to migrate off of that platform. For more information, see [Migration options for Ruby Flow](resources.md#RubyFlowOptions). | March 9, 2018 | 
| Update | Improved navigation on advanced concepts topic. See [Advanced workflow concepts in Amazon SWF](swf-dg-adv.md). | February 19, 2018 | 
| Update | Improved CloudWatch metrics documentation by adding valid statistics information. See [Amazon SWF Metrics for CloudWatch](cw-metrics.md). | December 4, 2017 | 
| Update | Changed the TOC to improve the document structure. Added new information on [API and Decision Event Metrics](cw-metrics.md#swf-throttling-metrics). | November 9, 2017 | 
| Update | Updated the [Amazon SWF Quotas](swf-dg-limits.md) section to include throttling limits for all regions. | October 18, 2017 | 
| Update | Changed `task_list` to `workflowId` in the [Getting started with Amazon SWF](swf-sns-tutorial.md) to avoid confusion with `activity_list`. | July 25, 2017 | 
| Update | Cleaned up the code examples throughout this guide. | June 5, 2017 | 
| Update | Simplified and improved the organization and contents of this guide. | May 19, 2017 | 
| Update | Updates and link fixes. | May 16, 2017 | 
| Update | Updates and link fixes. | October 1, 2016 | 
| Lambda task support | You can specify Lambda tasks in addition to traditional Activity tasks in your workflows. For more information, see [AWS Lambda tasks in Amazon SWF](lambda-task.md). | July 21, 2015 | 
| Support for setting task priority | Amazon SWF now includes support for setting the priority of tasks on a task list, and will attempt to deliver those with higher priority before tasks with lower priority. Information about how to set the task priority for workflows and for activities is provided in [Setting task priority in Amazon SWF](programming-priority.md). | December 17, 2014 | 
| Update | Added a new topic that describes how to log Amazon SWF API calls using CloudTrail: [Recording API calls with AWS CloudTrail](ct-logging.md). | May 8, 2014 | 
| Update | Two new topics related to CloudWatch metrics for Amazon SWF have been added: [Amazon SWF Metrics for CloudWatch](cw-metrics.md), which provides a list and descriptions of the supported metrics, and [Viewing Amazon SWF Metrics for CloudWatch using the AWS Management Console](cw-metrics-console.md), which provides information about how to view metrics and set alarms with the AWS Management Console. | April 28, 2014 | 
| Update | Added a new section: [Additional resources and reference info for Amazon SWF](resources.md). This section provides some service reference information and provides information about additional documentation, samples, code and other web resources for Amazon SWF developers. | March 19, 2014 | 
| Update | Added a workflow tutorial. See [Getting started with Amazon SWF](swf-sns-tutorial.md). | October 25, 2013 | 
| Update | Added [AWS CLI information and example](using-cli.md). | August 26, 2013 | 
| Update | Updates and fixes. | August 1, 2013 | 
| Update | Updated the document to describe how to use IAM for access control. | February 22, 2013 | 
| Initial Release | This is the first release of the *Amazon Simple Workflow Service Developer Guide*. | October 16, 2012 | 