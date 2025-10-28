# Creating HITs

A human intelligence task, or HIT, is a question your application asks and a worker
answers. There are two primary ways to create tasks (HITs) in Amazon Mechanical Turk (Mechanical Turk): directly or
using a HIT Type ID. In both cases, you need to provide a valid question and attributes for
your HIT.

###### Topics

- [Create a HIT Directly](#mturk-creating-hits-directly "#mturk-creating-hits-directly")
- [Create a HIT using a HIT Type](#mturk-creating-hits-using-type "#mturk-creating-hits-using-type")

## Create a HIT Directly

The most common way to create HITs in Mechanical Turk is via the [`CreateHIT`](../AWSMturkAPI/ApiReference_CreateHITOperation.md "../AWSMturkAPI/ApiReference_CreateHITOperation.md") operation. This API can be called with a JSON object
containing the following values.

```

{
  "Title": String,
  "Description": String,
  "Question": String,
  "HITLayoutId": String,
  "HITLayoutParameters": HITLayoutParameterList,
  "Reward": String,
  "AssignmentDurationInSeconds": Integer,
  "LifetimeInSeconds": Integer,
  "Keywords": String,
  "MaxAssignments": Integer,
  "AutoApprovalDelayInSeconds": Integer,
  "QualificationRequirements": QualificationRequirementList,
  "AssignmentReviewPolicy": ReviewPolicy,
  "HITReviewPolicy": ReviewPolicy,
  "RequesterAnnotation": String,
  "UniqueRequestToken": String
 }

```

The response includes the `HITId` that was generated for the task as well as
the `HITTypeId` that has been assigned to the HIT.  It also includes all of the
attributes of the HIT that were provided in the `CreateHIT` call.

## Create a HIT using a HIT Type

Creating a HIT with a HIT Type allows you to be explicit about which HITs ought to be
the same type and is a best practice for customers creating large numbers of HITs.  It is
also valuable when connecting notifications to your HITs as described in [Use Mechanical Turk notifications](Concepts_NotificationsArticle.md "Concepts_NotificationsArticle.md").

When creating a HIT using a HIT Type, you can use a HIT Type ID generated via a
previous [`CreateHIT`](../AWSMturkAPI/ApiReference_CreateHITOperation.md "../AWSMturkAPI/ApiReference_CreateHITOperation.md") call or generate one by calling the [`CreateHITType`](../AWSMturkAPI/ApiReference_CreateHITTypeOperation.md "../AWSMturkAPI/ApiReference_CreateHITTypeOperation.md") operation. This API can be called with a JSON object
containing the following values.

```

{
  "Title": String,
  "Description": String,
  "Reward": String,
  "AssignmentDurationInSeconds": Integer,
  "Keywords": String,
  "AutoApprovalDelayInSeconds": Integer,
  "QualificationRequirements": QualificationRequirementList
}
 

```

The response includes a generated `HITTypeId`, or the ID of an existing HIT
Type in your account that has the same attributes. The `HITTypeId` can then be
used to call [`CreateHITWithHITType`](../AWSMturkAPI/ApiReference_CreateHITWithHITTypeOperation.md "../AWSMturkAPI/ApiReference_CreateHITWithHITTypeOperation.md") with a JSON object containing the following
values.

```

{
  "HITTypeId": String,
  "Question": String,
  "HITLayoutId": String,
  "HITLayoutParameters": HITLayoutParameterList,
  "LifetimeInSeconds": Integer,
  "MaxAssignments": Integer,
  "AssignmentReviewPolicy": ReviewPolicy,
  "HITReviewPolicy": ReviewPolicy,
  "RequesterAnnotation": String,
  "UniqueRequestToken": String
 }
 

```

The response includes the `HITId` that was generated for the HIT and all of
the attributes of the HIT.
