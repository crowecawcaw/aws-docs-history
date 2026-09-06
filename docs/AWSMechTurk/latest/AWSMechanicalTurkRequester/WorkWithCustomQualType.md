

# Working with custom qualification types
<a name="WorkWithCustomQualType"></a>

When using Amazon Mechanical Turk (Mechanical Turk), you can create qualification types that you can then assign to workers as qualifications. Qualifications can be used for a range of worker management approaches, such as identifying workers that have met certain criteria in past tasks (HITs) or assigning a score based on performance over time. The following discusses how to create and assign qualification types to workers, as well as how to modify or revoke them. 

Mechanical Turk also provides the option to create qualification tests that allow workers to take a test to be assigned aqualification automatically. That topic isn't addressed here, but more information can be found in the [API Documentation](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateQualificationTypeOperation.html).

**Topics**
+ [Create a qualification type](#CreateCustomQualType)
+ [Assign or remove a worker qualification](#AssignRemoveQualWorker)
+ [Qualification requests](#QualRequest)
+ [Tutorial: Creating a qualification requirement that requires workers be in a group](CustomQualTutorialGroup.md)
+ [Tutorial: Create a qualification requirement that workers have achieved at least 80% accuracy on previous tasks](CustomQualTutorialAccuracy.md)
+ [Tutorial: Creating a qualification type to exclude workers from selected tasks](CustomQualTutorialExclude.md)

## Create a qualification type
<a name="CreateCustomQualType"></a>

The [`CreateQualificationType`](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateQualificationTypeOperation.html) operation can be used to register a new qualification type in your account. Simply specify the name, provide a brief description, and specify `Active` as the status. Note that the qualification type name and description are visible to workers. You can update these values using the [`UpdateQualificationType`](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_UpdateQualificationTypeOperation.html) operation.

## Assign or remove a worker qualification
<a name="AssignRemoveQualWorker"></a>

To assign a qualification type to a worker, use the [`AssociateQualificationWithWorker`](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_AssociateQualificationWithWorkerOperation.html) operation, specifying the ID of the qualification type and the worker it should be applied to. You can also assign an integer value such as a score. To modify the integer value, call the `AssociateQualificationWithWorker` operation again with the new value. 

You can remove a qualification using the [`DisassociateQualificationFromWorker`](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_DisassociateQualificationFromWorkerOperation.html) operation. 

## Qualification requests
<a name="QualRequest"></a>

When workers don't have one of the custom qualification types required to do your task, they have the option to request it from the Mechanical Turk marketplace. This is most commonly associated with tasks that have qualification tests but all custom qualification types can be requested. 

These requests can be queried using the `[ListQualificationRequests](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListQualificationRequestsOperation.html)` operation and can be approved or rejected using the `[AcceptQualificationRequest](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_AcceptQualificationRequestOperation.html)` or `[RejectQualificationRequest](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_RejectQualificationRequestOperation.html)` operations respectively. 

### Additional operations
<a name="CustomQualAdditionalOps"></a>

The following operations can be used when working with qualifications. 

**Additional Operations**
+  [`ListQualificationTypes`](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListQualificationTypesOperation.html): Retrieves a list of your existing qualification types. 
+  [`GetQualificationType`](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetQualificationTypeOperation.html): Retrieves the details of a qualification type. 
+  [`ListWorkersWithQualificationType`](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListWorkersWithQualificationTypeOperation.html): Retrieves a list of workers that have been assigned a qualification type. 
+  [`ListHITsForQualificationType`](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListHITsForQualificationTypeOperation.html): Retrieves a list of HITs that include a qualification type in their requirements. 
+  [`GetQualificationScore`](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetQualificationScoreOperation.html): Retrieves the qualification assigned to a worker for a qualification type. 