# Approving and rejecting work

Before workers can receive payment for tasks you post to Amazon Mechanical Turk (Mechanical Turk), the work
must be approved. You can review a worker's submission prior to transferring funds to
their account.

When you create tasks (HITs) in Mechanical Turk, one of the attributes you can set is the
auto-approval delay. This specifies how long you have to review a task before it's
automatically approved. As a general rule, it's best to keep this delay as short as
possible so that workers don't have to wait overly long to receive payment for the work
they did for you. Being prompt and fair in payment contributes to a positive
relationship with the worker community.

Between the time a task is submitted and when the auto-approval delay is reached, you
can use [`ListAssignmentsForHIT`](../AWSMturkAPI/ApiReference_ListAssignmentsForHITOperation.md "../AWSMturkAPI/ApiReference_ListAssignmentsForHITOperation.md") to review a worker's submission and
validate that they've made a reasonable effort to complete the task successfully. If so,
you can call [`ApproveAssignment`](../AWSMturkAPI/ApiReference_ApproveAssignmentOperation.md "../AWSMturkAPI/ApiReference_ApproveAssignmentOperation.md") to authorize payment to the worker. If
you identify a worker that is putting in no effort at all on your task (spamming), you
can use the [`RejectAssignment`](../AWSMturkAPI/ApiReference_RejectAssignmentOperation.md "../AWSMturkAPI/ApiReference_RejectAssignmentOperation.md") operation to invalidate their submission.

We recommend you only reject work when workers are clearly putting in no effort to
submit an accurate response to your task. It's inappropriate to penalize a worker for
submitting data incorrectly because you provided unclear instructions or they simply
made a mistake in interpreting what you wanted them to do. Most workers zealously guard
their approval rating and avoid doing work for requesters that they believe are in
unfair in how they reject work.

In the event that you reject an assignment but then discover that the issue was not
the worker's fault, you can call [`ApproveAssignment`](../AWSMturkAPI/ApiReference_ApproveAssignmentOperation.md "../AWSMturkAPI/ApiReference_ApproveAssignmentOperation.md") to reverse the rejection, but only for
assignments submitted in the last 30 days that haven't been deleted.
