# Implementing Amazon Mechanical Turk

The following topics describe information and additional resources you can use to
implement a project using Amazon Mechanical Turk.

###### Topics

- [Interfaces](#interfaces "#interfaces")
- [Considerations](#considerations "#considerations")
- [Common Use Scenarios](#common-use-scenarios "#common-use-scenarios")
- [Coding Resources](#coding-resources "#coding-resources")
- [Advanced Functionality](#advanced-functionality "#advanced-functionality")
- [Reference Resources](#reference-resources "#reference-resources")
  In the [Creating a HIT](CreatingAHIT.md "CreatingAHIT.md") tutorial you learned
  how to complete basic Amazon Mechanical Turk tasks. If you didn't use the tutorial, you can learn how to
  complete basic and advanced Amazon Mechanical Turk tasks using the _Amazon Mechanical Turk Developer
  Guide_ and by looking at code samples. For more information, go to [Amazon Mechanical Turk Developer
  Guide](../AWSMechanicalTurkRequester.md "../AWSMechanicalTurkRequester.md") and [Amazon Mechanical Turk
  Sample Code and Libraries](https://requester.mturk.com/developer/tools "https://requester.mturk.com/developer/tools"), respectively.

## Interfaces

Amazon Mechanical Turk offers the following interfaces:

- Command line
- API
- Requester user interface

The Amazon Mechanical Turk command line interface (CLI) makes it easy to use most of the Amazon Mechanical Turk
functionality. When you wish to have a hands-on approach to using Amazon Mechanical Turk and have a
relatively small number of assignments and results, the CLI is a good choice. For more
information, go to [Amazon Mechanical Turk Command
Line Tool Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md").

When the number of assignments you have or the number of results you have is large,
the Amazon Mechanical Turk API is a good choice. The API exercises all of Amazon Mechanical Turk's functionality and
enables you to integrate Amazon Mechanical Turk functions programmatically. For more information, go to
[Amazon Mechanical Turk
Developer Guide](../AWSMechanicalTurkRequester.md "../AWSMechanicalTurkRequester.md").

If you have a very large number of similar HITs, consider using the Requester user
interface. It merges one question template with lots of question data to create many
similar HITs. For more information, go to [Amazon Mechanical Turk Requester User
Interface](../RequesterUI.md "../RequesterUI.md").

## Considerations

Creating a successful HIT involves more than programming. There is a certain art
involved, for example, in pricing a HIT correctly, laying out the question correctly,
breaking down the task into HITs, and minimizing the Worker's time spent with the HIT.
For that reason, we created a best practices guide that gives detailed instructions
about creating an effective HIT.

Some of the HITs you create require the Workers to have special skills. You might, for
example, publish a HIT that asks for a translation. Whenever you have a HIT that
requires specialized skills, we recommend that you qualify the Workers. Only those who
pass the test receive the opportunity to work on your HITs. For more information, go to
[CreateHIT](../AWSMturkAPI/ApiReference_CreateHITOperation.md "../AWSMturkAPI/ApiReference_CreateHITOperation.md") and read about the `QualificationRequirement`
parameter.

Once a Worker becomes qualified, you can grant them qualification status so that they
no longer need to complete a qualification test before working on your HITs. For more
information, go to [AssignQualification](../AWSMturkAPI/ApiReference_AssignQualificationOperation.md "../AWSMturkAPI/ApiReference_AssignQualificationOperation.md").

### Considerations for Writing a

HIT

This guide presented a HIT for you to use. When you have to create your own, there
are several things you should consider:

- What is the problem you are trying to solve?

What questions do you want the Workers to answer? What is the best way to
present the task to Workers? You need this information when you write the
description and question for your HIT. You should be familiar with the
format to create your question or task. For more information, go to the
[Amazon Mechanical Turk Developer Guide](../AWSMechanicalTurkRequester.md "../AWSMechanicalTurkRequester.md").

- How much do you want to pay Workers?

You need to specify a reward for your HIT. Setting too low a reward
discourages Workers from working on your HITs. You need to determine what a
fair price is for the work you're asking the Workers to do. The best way is
to look at similar tasks advertised on the Amazon Mechanical Turk website. For more
information, go to the [Amazon Mechanical Turk website](https://www.mturk.com/mturk/welcome "https://www.mturk.com/mturk/welcome").

- How many responses do you want?

This is the number of assignments for your HIT. Sometimes you want only
one answer per HIT. When the answer is controversial, however, you might
like to get multiple answers (and thus use multiple assignments) per HIT and
reach an answer by consensus.

- How much time do you want to allow to complete the task?

Giving a Worker too long a time potentially delays getting results. Making
the duration too short frustrates Workers.

## Common Use Scenarios

This section describes some of the ways you can use Amazon Mechanical Turk.

### Photo and Video

Processing

Amazon Mechanical Turk is well-suited for processing images. In the past, companies have used
Mechanical Turk to:

- Tag objects found in an image for easier searching and advertising
  targeting
- Select from a set of images the best picture to represent a product
- Audit user-uploaded images for inappropriate content
- Classify objects found in satellite imagery

### Data

Verification and Clean-up

Companies with large online catalogs use Amazon Mechanical Turk to identify duplicate entries and
verify item details. Examples include:

- De-duplication of yellow pages directory listings
- Identification of duplicate products in an online product catalog
- Verification of restaurant details, such as the phone number or hours of
  operation

### Information

Gathering

The Amazon Mechanical Turk workforce enables you to gather information, such as:

- Allowing people to ask questions from a computer or mobile device about
  any topic and have Workers return results to those questions
- Filling out survey data on a variety of topics
- Writing reviews, descriptions and blog entries for websites
- Finding specific fields or data elements in large legal and government
  documents

### Data Processing

Use Amazon Mechanical Turk to process data, for example:

- Podcast editing and transcription
- Human powered translation services
- Search engine rating

## Coding Resources

To help you code your applications, we provide the following resources:

- Developer Resources page— Click the
  **Developer** tab on the Requester website located at
  [https://requester.mturk.com/](https://requester.mturk.com/ "https://requester.mturk.com/") to get to the [Developer Resources](https://requester.mturk.com/developer "https://requester.mturk.com/developer")
  page, which has links to sample code, documentation, the sandbox, and other
  helpful information.
- Sample Code and Libraries— You can use
  code samples as a means of understanding how to implement the Amazon Mechanical Turk API. For
  more information, go to [Amazon Mechanical Turk Sample Code and Libraries](https://requester.mturk.com/developer/tools "https://requester.mturk.com/developer/tools").
- Customer Forum—We recommend you look at
  the Amazon Mechanical Turk Forum to get an idea of what other users are doing and to benefit
  from the questions they've asked.

The forum can help you understand what you can and can't do with Amazon Mechanical Turk. The
forum also serves as a place for you to ask questions that other users or Amazon
representatives might answer. You can use the forum to report issues with the
service, the API, or the documentation. For more information, go to [Amazon Mechanical Turk Discussion Forums](https://developer.amazonwebservices.com/connect/forum.jspa?forumID=11 "https://developer.amazonwebservices.com/connect/forum.jspa?forumID=11").

## Advanced Functionality

The tutorial in this guide showed how to accomplish the basic tasks of creating,
testing, and publishing your HITs. The Amazon Mechanical Turk API, however, offers advanced
functionality, which the following table summarizes. For more information, go to the
_[Amazon Mechanical Turk
Developer Guide](../AWSMechanicalTurkRequester.md "../AWSMechanicalTurkRequester.md")_.

| Functionality                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Review the work submitted by Workers                                      | You reward work well done by paying the Worker. If work is not done<br>well, you can elect not to pay the Worker and block them from future<br>assignments.                                                                                                                                                                                                                                                                                                                                                                                     |
| Give bonuses                                                              | You might like to give a bonus to a Worker that does especially good<br>work. This gives the Worker incentive to work on one of your other HITs.<br>By rewarding Workers, you can create a small group of qualified people<br>who you know do good work. They, in turn, will prioritize your HITs over<br>others so that Workers complete your HITs in a timely manner. For more<br>information about awarding bonuses, go to [SendBonus](../AWSMturkAPI/ApiReference_OperationsArticle.md "../AWSMturkAPI/ApiReference_OperationsArticle.md"). |
| Review results programmatically                                           | Reviewing the results manually is an option when the number of<br>assignments is small. As the number of assignments grows, reviewing<br>results programmatically becomes more practical. The Amazon Mechanical Turk API enables<br>you to do that. For more information, go to [ListReviewableHITs](../AWSMturkAPI/ApiReference_OperationsArticle.md "../AWSMturkAPI/ApiReference_OperationsArticle.md")                                                                                                                                       |
| Delete a HIT                                                              | There are times when the results, although accurate, are unexpected<br>and unusable by you. In that case, you have to delete the HIT, revise,<br>and recreate it. For more information, go to [DeleteHIT](../AWSMturkAPI/ApiReference_OperationsArticle.md "../AWSMturkAPI/ApiReference_OperationsArticle.md").                                                                                                                                                                                                                                 |
| Update HIT properties                                                     | You can use API operations and the command line tools to update HIT<br>properties, such as Title, Description, Reward, and Keywords. For more<br>information, go to [UpdateHITTypeOfHIT](../AWSMturkAPI/ApiReference_OperationsArticle.md "../AWSMturkAPI/ApiReference_OperationsArticle.md").                                                                                                                                                                                                                                                  |
| Extend or eliminate HITs                                                  | You can also use the API operations to extend the completion time for<br>a HIT, expire a HIT early, or add additional assignments. For more<br>information, go to [CreateAdditionalAssignmentsForHIT](../AWSMturkAPI/ApiReference_OperationsArticle.md "../AWSMturkAPI/ApiReference_OperationsArticle.md") and [DeleteHIT](../AWSMturkAPI/ApiReference_OperationsArticle.md "../AWSMturkAPI/ApiReference_OperationsArticle.md").                                                                                                                |
| Communicate with Workers                                                  | You can use [NotifyWorkers](../AWSMturkAPI/ApiReference_OperationsArticle.md "../AWSMturkAPI/ApiReference_OperationsArticle.md") to send emails to specified Workers.                                                                                                                                                                                                                                                                                                                                                                           |
| Return the amount of money in your account that you use to pay<br>Workers | If you have not enabled AWS Billing, you must have sufficient Prepaid HITs balance for all assignments before you can publish Amazon Mechanical Turk HITs.<br>You can programmatically access your Prepaid HITs balance using [GetAccountBalance](../AWSMturkAPI/ApiReference_OperationsArticle.md "../AWSMturkAPI/ApiReference_OperationsArticle.md").                                                                                                                                                                                         |
| Create your own qualifications for Workers                                | We recommend that you use qualification tests when completing your<br>HITs requires specialized skills. You can create your own qualification<br>tests using [CreateQualificationType](../AWSMturkAPI/ApiReference_OperationsArticle.md "../AWSMturkAPI/ApiReference_OperationsArticle.md").                                                                                                                                                                                                                                                    |

## Reference Resources

The following list shows additional resources you can use to further your
understanding of Amazon Mechanical Turk.

- Learn the pricing for Amazon Mechanical Turk.

For more information, go to [Amazon Mechanical Turk Pricing](https://requester.mturk.com/pricing "https://requester.mturk.com/pricing").

- When you have questions about developing with Amazon Mechanical Turk visit the customer forum
  to get your questions answered.

A wide variety of questions have already been answered in the forum. If your
question has not been answered, ask it and wait for a fellow developer or Amazon
representative to help. For more information, go to [Amazon Mechanical Turk Developer Forums](https://developer.amazonwebservices.com/connect/forum.jspa?forumID=11 "https://developer.amazonwebservices.com/connect/forum.jspa?forumID=11").

- The Service Health Dashboard shows you the status of the Amazon Mechanical Turk web
  service. The dashboard shows you whether Amazon Mechanical Turk's services are
  functioning properly. For more information, go to the [Amazon Mechanical Turk Service Health Dashboard](https://requester.mturk.com/status/ "https://requester.mturk.com/status/").
- The _Amazon Mechanical Turk Developer Guide_ provides a detailed
  discussion of the service.

For more information, go to [Amazon Mechanical Turk
Developer Guide](../AWSMechanicalTurkRequester.md "../AWSMechanicalTurkRequester.md").

- The HIT page shows the Amazon Mechanical Turk HITs available to work on.

For more information, go to the [HIT
page](https://www.mturk.com/mturk/findhits?match=false "https://www.mturk.com/mturk/findhits?match=false").
