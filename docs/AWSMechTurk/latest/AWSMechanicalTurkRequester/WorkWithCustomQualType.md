# Working with custom qualification types

When using Amazon Mechanical Turk (Mechanical Turk), you can create qualification types that you
can then assign to workers as qualifications. Qualifications can be used for a range of
worker management approaches, such as identifying workers that have met certain criteria
in past tasks (HITs) or assigning a score based on performance over time. The following
discusses how to create and assign qualification types to workers, as well as how to
modify or revoke them.

Mechanical Turk also provides the option to create qualification tests that allow workers to take
a test to be assigned aqualification automatically. That topic isn't addressed here, but
more information can be found in the [API Documentation](../AWSMturkAPI/ApiReference_CreateQualificationTypeOperation.md "../AWSMturkAPI/ApiReference_CreateQualificationTypeOperation.md").

###### Topics

- [Create a qualification type](#CreateCustomQualType "#CreateCustomQualType")
- [Assign or remove a worker qualification](#AssignRemoveQualWorker "#AssignRemoveQualWorker")
- [Qualification requests](#QualRequest "#QualRequest")
- [Tutorial: Creating a qualification
  requirement that requires workers be in a group](CustomQualTutorialGroup.md "CustomQualTutorialGroup.md")
- [Tutorial: Create a qualification
  requirement that workers have achieved at least 80% accuracy on previous
  tasks](CustomQualTutorialAccuracy.md "CustomQualTutorialAccuracy.md")
- [Tutorial: Creating a qualification type
  to exclude workers from selected tasks](CustomQualTutorialExclude.md "CustomQualTutorialExclude.md")

## Create a qualification type

The [`CreateQualificationType`](../AWSMturkAPI/ApiReference_CreateQualificationTypeOperation.md "../AWSMturkAPI/ApiReference_CreateQualificationTypeOperation.md") operation can be used to
register a new qualification type in your account. Simply specify the name, provide
a brief description, and specify `Active` as the status. Note that the
qualification type name and description are visible to workers. You can update these
values using the [`UpdateQualificationType`](../AWSMturkAPI/ApiReference_UpdateQualificationTypeOperation.md "../AWSMturkAPI/ApiReference_UpdateQualificationTypeOperation.md") operation.

## Assign or remove a worker qualification

To assign a qualification type to a worker, use the [`AssociateQualificationWithWorker`](../AWSMturkAPI/ApiReference_AssociateQualificationWithWorkerOperation.md "../AWSMturkAPI/ApiReference_AssociateQualificationWithWorkerOperation.md") operation, specifying
the ID of the qualification type and the worker it should be applied to. You can
also assign an integer value such as a score. To modify the integer value, call the
`AssociateQualificationWithWorker` operation again with the new
value.

You can remove a qualification using the [`DisassociateQualificationFromWorker`](../AWSMturkAPI/ApiReference_DisassociateQualificationFromWorkerOperation.md "../AWSMturkAPI/ApiReference_DisassociateQualificationFromWorkerOperation.md") operation.

## Qualification requests

When workers don't have one of the custom qualification types required to do your
task, they have the option to request it from the Mechanical Turk marketplace. This is most
commonly associated with tasks that have qualification tests but all custom
qualification types can be requested.

These requests can be queried using the `ListQualificationRequests` operation and can be approved or
rejected using the `AcceptQualificationRequest` or `RejectQualificationRequest` operations respectively.

### Additional operations

The following operations can be used when working with qualifications.

**Additional Operations**

- [`ListQualificationTypes`](../AWSMturkAPI/ApiReference_ListQualificationTypesOperation.md "../AWSMturkAPI/ApiReference_ListQualificationTypesOperation.md"): Retrieves a list
  of your existing qualification types.
- [`GetQualificationType`](../AWSMturkAPI/ApiReference_GetQualificationTypeOperation.md "../AWSMturkAPI/ApiReference_GetQualificationTypeOperation.md"): Retrieves the
  details of a qualification type.
- [`ListWorkersWithQualificationType`](../AWSMturkAPI/ApiReference_ListWorkersWithQualificationTypeOperation.md "../AWSMturkAPI/ApiReference_ListWorkersWithQualificationTypeOperation.md"):
  Retrieves a list of workers that have been assigned a qualification
  type.
- [`ListHITsForQualificationType`](../AWSMturkAPI/ApiReference_ListHITsForQualificationTypeOperation.md "../AWSMturkAPI/ApiReference_ListHITsForQualificationTypeOperation.md"): Retrieves a
  list of HITs that include a qualification type in their requirements.
- [`GetQualificationScore`](../AWSMturkAPI/ApiReference_GetQualificationScoreOperation.md "../AWSMturkAPI/ApiReference_GetQualificationScoreOperation.md"): Retrieves the
  qualification assigned to a worker for a qualification type.
