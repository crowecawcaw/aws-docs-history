# Tutorial: Creating a qualification type

to exclude workers from selected tasks

In the following example, we create a qualification type that describes a group of
workers that have demonstrated they don't perform well at our tasks and excludes
them in our qualification requirements. To start, we use the [`CreateQualificationType`](../AWSMturkAPI/ApiReference_CreateQualificationTypeOperation.md "../AWSMturkAPI/ApiReference_CreateQualificationTypeOperation.md") operation to create the type
with which we want to work.

```

{
  Name: 'Excluded',
  Description: 'Excluded from this task',
  QualificationTypeStatus: 'Active'
}
 
```

The `CreateQualificationType` operation returns an ID,
3TL87MO8CLOFYXKXNRLM00EXAMPLE, that we can assign to workers. For each worker, we
call the [AssociateQualificationWithWorker](../AWSMturkAPI/ApiReference_AssociateQualificationWithWorkerOperation.md "../AWSMturkAPI/ApiReference_AssociateQualificationWithWorkerOperation.md") operation to add them to the excluded
group.

```

{
  WorkerId: 'AZ3456EXAMPLE',
  QualificationTypeId: '3TL87MO8CLOFYXKXNRLM00EXAMPLE'
}
 
```

Now that we've built our group, we can reference it in the
`QualificationRequirements` for our HITs as shown in the following
example.

```

QualificationRequirements: [
  {
    QualificationTypeId: '3TL87MO8CLOFYXKXNRLM00EXAMPLE',
    Comparator: 'DoesNotExist',
    ActionsGuarded: 'DiscoverPreviewAndAccept'
  }
]

```

Because the `ActionsGuarded` has been set to
`DiscoverPreviewAndAccept`, it is not visible to workers who've been
assigned the qualification type.
