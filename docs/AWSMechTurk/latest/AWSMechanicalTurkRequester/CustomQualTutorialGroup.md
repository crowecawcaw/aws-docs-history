

# Tutorial: Creating a qualification requirement that requires workers be in a group
<a name="CustomQualTutorialGroup"></a>

In the following example, we create a qualification type that describes a group of workers that have demonstrated expertise at a task and add it to our qualification requirements. To start, we use the [`CreateQualificationType`](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateQualificationTypeOperation.html) operation to create the type with which we're working. 

```
{
  Name: 'Experts', 
  Description: 'Demonstrated expertise at my task',
  QualificationTypeStatus: 'Active'
}
 
```

The `CreateQualificationType` operation will return an ID, 3TL87MO8CLOFYXKXNRLM00EXAMPLE, that we can assign to workers. For each worker, we call the [`AssociateQualificationWithWorker`](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_AssociateQualificationWithWorkerOperation.html) operation to add them to our group. 

```
{
  WorkerId: 'AZ3456EXAMPLE',
  QualificationTypeId: '3TL87MO8CLOFYXKXNRLM00EXAMPLE'
}
 
```

Now that we've built our group, we can reference it in the `QualificationRequirements` for our HITs as shown in the following example. 

```
QualificationRequirements: [
  {
    QualificationTypeId: '3TL87MO8CLOFYXKXNRLM00EXAMPLE',
    Comparator: 'Exists',
    ActionsGuarded: 'DiscoverPreviewAndAccept'
  }
]
 
```

Because the `ActionsGuarded` is set to `DiscoverPreviewAndAccept`, it is only visible to workers who've been assigned the qualification type. 