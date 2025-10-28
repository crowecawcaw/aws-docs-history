# Retrieving HIT status

At any point after a HIT is created in Amazon Mechanical Turk (Mechanical Turk) up until it is disposed, you can
retrieve the status of a HIT using the `GetHIT` operation. In addition, you can call `ListHITs,`
`ListHITsForQualificationType`, or `ListReviewableHITs` to retrieve HIT information. The [HIT data structure](../AWSMturkAPI/ApiReference_HITDataStructureArticle.md "../AWSMturkAPI/ApiReference_HITDataStructureArticle.md") returned by these operations includes the attributes and
question used to create the HIT, as well as attributes that describe the current status of
the HIT.

The most useful attribute to monitor is the `HITStatus` value, which can be
used to evaluate if a HIT is complete. When a HIT is created, its `HITStatus`
initially has a value of `Assignable`, which indicates that it's possible for a
worker to accept it and begin working on it. After the maximum number of assignments have
been accepted, the HIT moves to a status of `Unassignable` because no additional
workers can accept it. Finally, a HIT moves to the `Reviewable` state when all of
the assignments have been submitted or the HIT has expired. Keep in mind that you can
retrieve interim results at any time, regardless of whether or not all of the HITs have been
submitted.

You can use the values `NumberOfAssignmentsAvailable` and
`NumberOfAssignmentsPending` to monitor assignment acceptance and submission.
When a HIT is first created, the number of assignments available is equal to the
`MaxAssignments` value. As HITs are accepted by workers, this number is
reduced and the number of assignments pending increases. When workers submit assignments,
they are no longer reflected in `NumberOfAssignmentsPending`. Similarly, if
workers _return_ an assignment or the assignment duration elapses, the
assignment is no longer reflected in pending but returns to available. When all of the
available assignments have been submitted or the HIT expires, the number of pending and
available are both 0.

**HIT Lifecycle**

The following example shows the HIT status values through the lifecycle of a HIT with
`MaxAssignments` set to 5.

| Step                                                  | `HITStatus`    | Number Of assignments available | Number Of assignments pending |
| ----------------------------------------------------- | -------------- | ------------------------------- | ----------------------------- |
| Initial state                                         | `Assignable`   | 5                               | 0                             |
| Three assignments have been accepted                  | `Assignable`   | 2                               | 3                             |
| All assignments accepted and two submitted            | `Unassignable` | 0                               | 3                             |
| One assignment is returned                            | `Assignable`   | 1                               | 2                             |
| All assignments submitted                             | `Reviewable`   | 0                               | 0                             |
| Three of the submitted assignments have been approved | `Reviewable`   | 0                               | 0                             |
| All of the assignments have been approved             | `Reviewable`   | 0                               | 0                             |
