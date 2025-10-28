# Tutorial: Create a qualification

requirement that workers have achieved at least 80% accuracy on previous
tasks

In the following example, we create a qualification type that we can use to record
how well workers did on a previous set of tasks and then build a qualification
requirement that requires them to have achieved at least 80% accuracy. In this
approach, we start by posting a set of HITs to which we already know the answer.
When workers respond to these HITs, we can track their responses against the known
answers and assign them a score as a qualification.

To start, we use the [`CreateQualificationType`](../AWSMturkAPI/ApiReference_CreateQualificationTypeOperation.md "../AWSMturkAPI/ApiReference_CreateQualificationTypeOperation.md") operation to create the type
with which we want to work.

```

{
  Name: 'Task Scores',
  Description: 'Score on previous tasks,
  QualificationTypeStatus: 'Active'
}
 
```

The `CreateQualificationType` operation returns an ID,
3TL87MO8CLOFYXKXNRLM00EXAMPLE, that we can assign to workers. For each worker, we
call the [`AssociateQualificationWithWorker`](../AWSMturkAPI/ApiReference_AssociateQualificationWithWorkerOperation.md "../AWSMturkAPI/ApiReference_AssociateQualificationWithWorkerOperation.md") operation to record
the score they achieved on the earlier tasks. In the example below, we record that
the worker was 93% accurate on the test HITs.

```

{
  WorkerId: 'AZ3456EXAMPLE',
  QualificationTypeId: '3TL87MO8CLOFYXKXNRLM00EXAMPLE',
  IntegerValue: 93
}

```

Now that we've built our group, we can reference it in the
`QualificationRequirements` for our HITs as shown below.

```

QualificationRequirements: [
  {
    QualificationTypeId: '3TL87MO8CLOFYXKXNRLM00EXAMPLE',
    Comparator: 'GreaterThanOrEqual',
    IntegerValues: [80]
  }
]

```
