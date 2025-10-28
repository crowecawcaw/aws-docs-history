# Frequently asked questions

Use the following sections to get answers to frequently asked questions. If you need
additional support, use the following link to contact Amazon Mechanical Turk: [www.mturk.com/contact-us](http://www.mturk.com/contact-us "http://www.mturk.com/contact-us").

## Why aren't my tasks being

completed?

There are a number of reasons why the tasks you post to Mechanical Turk aren't being completed. The
most common reason is that the reward amount you specified isn't adequate to compensate
workers for the time and effort they need to commit to your task to complete it. If you
suspect this is the case, remove the HITs from Mechanical Turk by expiring them and experiment with
reposting some of them at a higher reward amount.

Other common reasons include the following.

- The qualification requirements for the task are so narrow that few, if any, workers meet
  the criteria to be eligible for the task.
- The task interface has a technical issue that prevents workers from submitting it.
- The assignment duration is set too short for workers to successfully complete the task in
  the time allowed.

## How do I pull down HITs I created by

mistake?

Use the [UpdateExpirationForHIT](../AWSMturkAPI/ApiReference_UpdateExpirationForHITOperation.md "../AWSMturkAPI/ApiReference_UpdateExpirationForHITOperation.md") operation and set the `ExpireAt` time
to `0` to tell Mechanical Turk to immediately expire a HIT. Note that this won't
prevent workers that have already accepted your HIT from completing and submitting
it.

## I expired my HITs. Why am I still getting submissions from

workers?

If a worker accepts a HIT before it expires, they are still allowed to complete and submit
the task until the assignment duration elapses. This protects the worker experience
by letting them submit work on which they may have already spent a lot of time, even
if you opt to take the HIT down.

## Why are some of my task fields missing from my

results?

A common mistake in building task interfaces is using the same _name_
attribute for multiple form inputs. In those cases, only one of the input field
values is returned. You should check your HTML to ensure that each input has a
unique name.

## Can I make some fields in my task interface

required?

You can use HTML, JavaScript, or both to specify required fields and minimum or maximum
values or perform other validations that prevent workers from submitting the task if
it doesn't meet the requirements. To learn more about the types of form validation
you can apply, see [Client-side form validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation "https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation") on the Mozilla developer site.

## How can I test my task interface?

The easiest way to test your task interface is to save it to an HTML file and open it in a
browser. From the browser, you can go through all of the steps that a worker would
perform in completing the task. If your task interface is built around a standard
form element, you can't test submitting it, but you can test to ensure it works as
you expect. If you use the crowd-form element from Crowd HTML Elements, you can test
it by selecting **Submit**. When you submit from outside of Mechanical Turk,
the results are displayed at the top of the window.

To fully test a task interface and the creation and retrieval of HITs, you can use the
sandbox environment.

## What is the difference between a HIT and an

assignment?

A _HIT_ is a single task that you create in Mechanical Turk. When workers accept a
HIT, they get an _assignment_ that gives them the right to submit
their response. When you create a HIT, you can specify the maximum number of
assignments that can be created for each HIT, which allows you to get multiple
different worker responses for each task. For more information on HITs and
assignments, see [Amazon Mechanical Turk core concepts](IntroCoreConcepts.md "IntroCoreConcepts.md").

## Can I view the HITs I create with the API in the requester

website?

No, the requester website only displays HITs that are created from the requester website.

## I published HITs in the sandbox environment. Why they aren't

being completed?

The sandbox environment is a great way to test HITs without spending any money. However,
because no money changes hands, there isn't any incentive for workers to complete
your tasks. To complete your testing, create an account in the [worker sandbox environment](https://workersandbox.mturk.com "https://workersandbox.mturk.com") to
complete the tasks yourself. Then, publish them in the
_production_ environment.

## I incorrectly rejected some assignments. Can I reverse

the rejection?

In the event that you reject an assignment but then discover that the issue was not the
worker's fault, you can call [ApproveAssignment](../AWSMturkAPI/ApiReference_ApproveAssignmentOperation.md "../AWSMturkAPI/ApiReference_ApproveAssignmentOperation.md") to reverse the rejection, but only for assignments
submitted in the last 30 days that haven't been deleted.

## How do I filter the workers eligible to work on my

task?

Mechanical Turk provides a qualifications system that allows you to use system-managed or custom
criteria to limit the workers that can work on a task. For more information, see
[Selecting eligible workers](SelectingEligibleWorkers.md "SelectingEligibleWorkers.md").

## How do I create a custom qualification?

You can create custom qualification types that allow you to filter workers eligible to work
on your tasks using criteria based on their past performance on your tasks. For more
information, see [Working with custom qualification types](WorkWithCustomQualType.md "WorkWithCustomQualType.md").

## Can I restrict how many HITs a worker can complete for

my project?

Mechanical Turk doesn't provide a native capability to limit the number of HITs that a worker can
contribute to a project or batch. To learn how to accomplish this using custom
qualification types, see [Working with custom qualification types](WorkWithCustomQualType.md "WorkWithCustomQualType.md"). Before starting your project or batch,
create a custom qualification type with a label such as **Completed Enough
of Project A** and pecify that this type doesn't exist
(**DoesNotExist**) in your qualification requirements for each
HIT. When a worker reaches your threshold of HITs they can submit, you can assign
this qualification type to them, after which they can't accept any HITs for the
project.

## Can I post HITs in languages other than

English?

You can post HITs using any language, provided you note the required language in the title
of your task. However, the number of available workers who are fluent in a given
language varies greatly. It may take longer for your task to be completed or you may
need to increase your reward amount if not enough workers are available.

## Additional Mechanical Turk Resources

- The [Mechanical Turk API Reference](../AWSMturkAPI/index.md "../AWSMturkAPI/index.md") describes all the API operations for
  Mechanical Turk in detail.
- The [Mechanical Turk Requester User Interface Documentation](../RequesterUI/index.md "../RequesterUI/index.md") describes how to create
  Mechanical Turk tasks using a graphical user interface.
- Posts on the [Mechanical Turk Happenings Blog](https://blog.mturk.com/ "https://blog.mturk.com/") address
  updates to the Mechanical Turk marketplace.
- [Blog Tutorials](https://blog.mturk.com/tutorials/home "https://blog.mturk.com/tutorials/home") provide
  instruction on using Mechanical Turk for a variety of tasks.
- The [Amazon Mechanical Turk Developer Forums](https://developer.amazonwebservices.com/connect/forum.jspa?forumID=11 "https://developer.amazonwebservices.com/connect/forum.jspa?forumID=11") provide questions and
  answers about Mechanical Turk.
- [Mechanical Turk on Github](https://github.com/awslabs/mturk-api-samples "https://github.com/awslabs/mturk-api-samples") offers
  sample code and tutorials.
