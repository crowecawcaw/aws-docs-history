# Additional resources and reference info for Amazon SWF

This chapter provides additional resources and reference information that is useful when developing workflows
with Amazon SWF.

###### Topics

- [Amazon SWF Timeout Types](swf-timeout-types.md "swf-timeout-types.md")
- [Amazon Simple Workflow Service Endpoints](#resources-endpoints "#resources-endpoints")
- [Additional Documentation for the Amazon Simple Workflow Service](#resources-docs "#resources-docs")
- [Web Resources for the Amazon Simple Workflow Service](#resources-web "#resources-web")
- [Migration options for Ruby Flow](#RubyFlowOptions "#RubyFlowOptions")

## Amazon Simple Workflow Service Endpoints

A list of the current [Amazon SWF
Regions and Endpoints](../../../general/latest/gr/rande.md#swf_region "../../../general/latest/gr/rande.md#swf_region") are provided in the _Amazon Web Services General Reference_, along with the
endpoints for other services.

Amazon SWF domains and all related workflows and activities must exist within the same region to communicate with
each other. Furthermore, any registered domains, workflows and activities within a region don't exist in other
regions. For example, if you create a domain named "MySampleDomain" in both _us-east-1_ and in
_us-west-2_, they exist as _separate domains_: none of the workflows, task
lists, activities, or data associated with your domains are shared across regions.

If you use other AWS resources in your workflows, such as Amazon EC2 instances, these must also exist in the same
region as your Amazon SWF resources. The only exceptions to this are services that span regions, such as Amazon S3 and IAM.
You can access these services from workflows that exist in any region that supports them.

## Additional Documentation for the Amazon Simple Workflow Service

In addition to this Developer Guide, you may find the following documentation useful.

### Amazon Simple Workflow Service API Reference

The [Amazon Simple Workflow Service API Reference](../apireference.md "../apireference.md") provides detailed information about the Amazon SWF HTTP API, including actions, request and
response structures and error codes.

### AWS Flow Framework Documentation

The [AWS Flow Framework](https://aws.amazon.com/swf/details/flow/ "https://aws.amazon.com/swf/details/flow/") is a programming framework
that simplifies the process of implementing distributed asynchronous applications that use Amazon SWF to manage their
workflows and activities, so you can focus on implementing your workflow logic.

Each AWS Flow Framework is designed to work idiomatically in the language for which it is designed, so you can work
naturally with your language of choice to implement workflows with all of the benefits of Amazon SWF.

There is an AWS Flow Framework for Java. The [AWS Flow Framework for Java Developer Guide](../awsflowguide.md "../awsflowguide.md") provides information about how to obtain, set up and use the AWS Flow Framework for Java.

### AWS SDK Documentation

The AWS Software Development Kits (SDKs) provide access to Amazon SWF in many different programming languages. The SDKs follow the HTTP API
closely, but also provide language-specific programming interfaces for some Amazon SWF features. You can find out more
information about each SDK by visiting the following links.

###### Note

Only SDKs that have support for Amazon SWF at the time of writing are listed here. For a full list of the
available AWS SDKs, visit the [Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/")
page.

**Java**

The AWS SDK for Java provides a Java API for AWS infrastructure services.

To view the available documentation, see the [AWS SDK for Java Documentation](https://aws.amazon.com/documentation/sdkforjava/ "https://aws.amazon.com/documentation/sdkforjava/")
page. You can also go directly to the Amazon SWF sections in the SDK reference by following these links:

- [`Class: AmazonSimpleWorkflowClient`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowClient.md")
- [`Class: AmazonSimpleWorkflowAsyncClient`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowAsyncClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowAsyncClient.md")
- [`Interface: AmazonSimpleWorkflow`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflow.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflow.md")
- [`Interface: AmazonSimpleWorkflowAsync`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowAsync.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowAsync.md")

**JavaScript**

The AWS SDK for JavaScript allows developers to build libraries or applications that make use of AWS
services using a simple and easy-to-use API available both in the browser or inside of Node.js applications
on the server.

To view the available documentation, see the [AWS SDK for JavaScript Documentation](https://aws.amazon.com/documentation/sdkforjavascript/ "https://aws.amazon.com/documentation/sdkforjavascript/")
page. You can also go directly to the Amazon SWF section in the SDK reference by following this link:

- [`Class:
AWS.SimpleWorkflow`](../../../AWSJavaScriptSDK/latest/AWS/SWF.md "../../../AWSJavaScriptSDK/latest/AWS/SWF.md")

**.NET**

The AWS SDK for .NET is a single, downloadable package that includes Visual Studio project templates,
the AWS .NET library, C# code samples, and documentation. The AWS SDK for .NET makes it easier for Windows developers to build
.NET applications for Amazon SWF and other services.

To view the available documentation, see the [AWS SDK for .NET Documentation](https://aws.amazon.com/documentation/sdkfornet/ "https://aws.amazon.com/documentation/sdkfornet/")
page. You can also go directly to the Amazon SWF sections in the SDK reference by following these links:

- [`Namespace: Amazon.SimpleWorkflow`](../../../sdkfornet/v4/apidocs/items/SimpleWorkflow/NSimpleWorkflow.md "../../../sdkfornet/v4/apidocs/items/SimpleWorkflow/NSimpleWorkflow.md")
- [`Namespace: Amazon.SimpleWorkflow.Model`](../../../sdkfornet/v4/apidocs/items/SimpleWorkflow/NSimpleWorkflowModel.md "../../../sdkfornet/v4/apidocs/items/SimpleWorkflow/NSimpleWorkflowModel.md")

**PHP**

The AWS SDK for PHP provides a PHP programming interface to Amazon SWF.

To view the available documentation, see the [AWS SDK for PHP Documentation](https://aws.amazon.com/documentation/sdkforphp/ "https://aws.amazon.com/documentation/sdkforphp/") page. You
can also go directly to the Amazon SWF section in the SDK reference by following this link:

- [`Class:
SwfClient`](../../../sdk-for-php/latest/reference/class-Aws.Swf.md "../../../sdk-for-php/latest/reference/class-Aws.Swf.md")

**Python**

The AWS SDK for Python (Boto) provides a Python programming interface to Amazon SWF.

To view the available documentation, see the
[boto: A Python interface to Amazon Web Services](http://docs.pythonboto.org/en/latest/ "http://docs.pythonboto.org/en/latest/") page.
You can also go directly to the Amazon SWF sections in the documentation by following these links:

- [Amazon SWF Tutorial](http://docs.pythonboto.org/en/latest/swf_tut.html "http://docs.pythonboto.org/en/latest/swf_tut.html")
- [Amazon SWF Reference](http://docs.pythonboto.org/en/latest/ref/swf.html "http://docs.pythonboto.org/en/latest/ref/swf.html")

**Ruby**

The AWS SDK for Ruby provides a Ruby programming interface to Amazon SWF.

To view the available documentation, see the [AWS SDK for Ruby Documentation](https://aws.amazon.com/documentation/sdkforruby/ "https://aws.amazon.com/documentation/sdkforruby/") page. You can
also go directly to the Amazon SWF section in the SDK reference by following this link:

- [Class:
  AWS::SimpleWorkflow](../../../AWSRubySDK/latest/AWS/SimpleWorkflow.md "../../../AWSRubySDK/latest/AWS/SimpleWorkflow.md")

### AWS CLI Documentation

The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services. With just one tool to
download and configure, you can control multiple AWS services from the command line and automate them through
scripts.

For more information about the AWS CLI, see the [AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") page.

For an overview of the available commands for Amazon SWF, see [swf](../../../cli/latest/reference/swf/index.md "../../../cli/latest/reference/swf/index.md") in the _AWS CLI Command Reference_.

## Web Resources for the Amazon Simple Workflow Service

There are a number of Web resources that you can use to learn more about Amazon SWF or to get help with using the
service and developing workflows.

### Amazon SWF Forum

The Amazon SWF forum provides a place for you to communicate with other Amazon SWF developers and members of the Amazon SWF
development team at Amazon to ask questions and to get answers.

You can visit the forum at: [Forum:
Amazon Simple Workflow Service](https://forums.aws.amazon.com/forum.jspa?forumID=133 "https://forums.aws.amazon.com/forum.jspa?forumID=133").

### Amazon SWF FAQ

The Amazon SWF FAQ provide answers to frequently-asked questions about Amazon SWF, including an overview of common
use cases, differences between Amazon SWF and other services, and more.

You can access the FAQ here: [Amazon SWF FAQ](https://aws.amazon.com/swf/faqs/ "https://aws.amazon.com/swf/faqs/").

### Amazon SWF Videos

The [Amazon Web Services](http://www.youtube.com/user/AmazonWebServices "http://www.youtube.com/user/AmazonWebServices") channel on YouTube
provides video training for all of Amazon's Web Services, including Amazon SWF. For a full list of Amazon SWF-related videos, use the following query:
[_Simple
Workflow_ in Amazon Web Services](http://www.youtube.com/user/AmazonWebServices/search?query=simple+workflow "http://www.youtube.com/user/AmazonWebServices/search?query=simple+workflow")

## Migration options for Ruby Flow

The AWS Flow Framework for Ruby is no longer under active development. While existing code will continue
to work indefinitely, there will be no new features or versions. This topic will cover usage and
migration options to continue working with Amazon SWF, and information on how to migrate to
Step Functions.

| Option                                                                                           | Description                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Continue to use the Ruby Flow<br>Framework](#continue-to-use-ruby "#continue-to-use-ruby")      | For now, the Ruby Flow Framework will continue to work. If you do nothing, your<br>code will continue to function as it is. Plan to migrate off of the AWS Flow Framework for Ruby in the near<br>future. |
| [Migrate to the Java Flow<br>Framework](#migrate-to-java-flow "#migrate-to-java-flow")           | The Java Flow Framework remains in active development and will continue to receive<br>new features and updates.                                                                                           |
| [Migrate to Step Functions](#migrate-to-step-functions "#migrate-to-step-functions")             | Step Functions provides a way to coordinate the components of distributed<br>applications using visual workflows controlled by a state machine.                                                           |
| [Use the SWF API directly](#use-api-directly "#use-api-directly"), without the Flow<br>Framework | You can continue to work in Ruby and use the SWF API directly instead of the Ruby<br>Flow Framework.                                                                                                      |

The advantage the Flow Framework provides, for either Ruby or Java, is that it allows you to
focus on your workflow logic. The framework handles much of the details of communication and
coordination, and some of the complexity is abstracted. You can continue to have the same level
of abstraction by migrating to the Java Flow Framework, or you can directly interact with Amazon SWF
SDK directly.

### Continue to use the Ruby Flow Framework

The AWS Flow Framework for Ruby will continue to function as it does now in the short term. If you have
workflows written in the AWS Flow Framework for Ruby, these will continue to work. Without updates,
support, or security fixes, it is best to have a firm plan to migrate off of the
AWS Flow Framework for Ruby in the near future.

### Migrate to the Java Flow Framework

The AWS Flow Framework for Java will remain in active development. Conceptually, the AWS Flow Framework for Java is
similar to AWS Flow Framework for Ruby: you can still focus on your workflow logic, and the framework will
help manage your decider logic, and will make other aspects of Amazon SWF easier to manage.

- [AWS Flow Framework
  for Java](../awsflowguide/welcome.md "../awsflowguide/welcome.md")
- [AWS Flow Framework for Java API Reference](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/package-summary.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/package-summary.md")

### Migrate to Step Functions

AWS Step Functions provides a service that is similar to Amazon SWF, but where your workflow logic is
controlled by a state machine. Step Functions enables you to coordinate the components of distributed
applications and microservices using visual workflows. You build applications from individual
components that each perform a discrete function, or _task_, allowing you
to scale and change applications quickly. Step Functions provides a reliable way to coordinate
components and step through the functions of your application. A graphical console provides a
way to visualize the components of your application as a series of steps. It automatically
triggers and tracks each step, and retries when there are errors, so your application executes
in order and as expected, every time. Step Functions logs the state of each step, so when things do go
wrong, you can diagnose and debug problems quickly.

In Step Functions, you manage the coordination of your tasks using a state machine, written in
declarative JSON, that is defined using the [Amazon States Language](../../../step-functions/latest/dg/concepts-amazon-states-language.md "../../../step-functions/latest/dg/concepts-amazon-states-language.md"). By
using a state machine, you don't have to write and maintain a decider program to control your
application logic. Step Functions provides an intuitive, productive, and agile approach to coordinating
application components using visual workflows. You should consider using AWS Step Functions for all
your new applications, and Step Functions provides an excellent platform to migrate to for the
workflows you currently have implemented in the AWS Flow Framework for Ruby.

To help migrate your tasks to Step Functions, while continuing to leverage your Ruby language
skills, Step Functions provides an example Ruby activity worker. This example uses best practices for
implementing an activity worker, and can be used as a template to migrate your task logic to
Step Functions. For more information, see the [_Example Activity Worker in
Ruby_](../../../step-functions/latest/dg/example-ruby-activity-worker.md "../../../step-functions/latest/dg/example-ruby-activity-worker.md") topic in the [AWS Step Functions Developer Guide](../../../step-functions/latest/dg.md "../../../step-functions/latest/dg.md").

###### Note

For many customers, migrating to Step Functions from the AWS Flow Framework for Ruby is the best option. But,
if you require that signals intervene in your processes, or if you need to launch child
processes that return a result to a parent, consider using the Amazon SWF API directly, or
migrating to the AWS Flow Framework for Java.

For more information on AWS Step Functions, see:

- [AWS Step Functions Developer Guide](../../../step-functions/latest/dg.md "../../../step-functions/latest/dg.md")
- [AWS Step Functions API Reference](../../../step-functions/latest/apireference.md "../../../step-functions/latest/apireference.md")
- [AWS Step Functions Command Line Reference](../../../cli/latest/reference/stepfunctions.md "../../../cli/latest/reference/stepfunctions.md")

### Use the Amazon SWF API directly

While the AWS Flow Framework for Ruby manages some of the complexity of Amazon SWF, you can also use the
Amazon SWF API directly. Using the API directly allows you to build workflows where you have full
control over implementing tasks and coordinating them, without worrying about underlying
complexities such as tracking their progress and maintaining their state.

- [Amazon Simple Workflow Service Developer Guide](../developerguide.md "../developerguide.md")
- [Amazon Simple Workflow Service API Reference](../apireference.md "../apireference.md")
