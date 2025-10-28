# Modifying HITs

Once a HIT has been created in the Amazon Mechanical Turk (Mechanical Turk) marketplace, it's possible to modify
it; however, there is an important caveat. Because your HIT is now available to workers, Mechanical Turk
will not allow you to make changes that will negatively impact them. For example, Mechanical Turk won't
let you delete a HIT on which a worker is actively working. The following are the common
operations you can perform to modify HITs.

###### Topics

- [Modify expiration time](#mturk-creating-hits-modify-expiration "#mturk-creating-hits-modify-expiration")
- [Add additional
  assignments](#mturk-creating-hits-modify-add-assignments "#mturk-creating-hits-modify-add-assignments")
- [Modify the HIT Type](#mturk-creating-hits-modify-type "#mturk-creating-hits-modify-type")
- [Delete](#mturk-creating-hits-modify-delete "#mturk-creating-hits-modify-delete")

## Modify expiration time

When a HIT is created, the `LifetimeInSeconds` is used to calculate an
`ExpiresAt` value that tells Mechanical Turk when to remove a HIT from the marketplace if
it hasn't been completed yet. You can use the [`UpdateExpirationForHIT`](../AWSMturkAPI/ApiReference_UpdateExpirationForHITOperation.md "../AWSMturkAPI/ApiReference_UpdateExpirationForHITOperation.md") operation to either extend this time
further into the future to allow workers more time to complete it or shorten the time if
responses are no longer valuable.

A common use of `UpdateExpirationForHIT` is to call it with a value of 0 or a
time in the past to tell Mechanical Turk to immediately expire a HIT. This is useful when you make a
mistake in your HIT definition and immediately need to remove the task from the marketplace.
Note that this won't prevent workers who have already accepted your HIT from completing and
submitting it.

## Add additional

assignments

When a HIT is created, the `MaxAssignments` value is provided and informs
Mechanical Turk of how many workers can submit responses for the task. If you need to allow additional
workers to provide responses, you can call [`CreateAdditionalAssignmentsForHIT`](../AWSMturkAPI/ApiReference_CreateAdditionalAssignmentsForHITOperation.md "../AWSMturkAPI/ApiReference_CreateAdditionalAssignmentsForHITOperation.md") to add additional available
assignments.

A common pattern for managing quality in Mechanical Turk is to ask multiple workers to provide
responses for a given task and then compare the results. One approach for doing this is to
start with a minimal number of assignments and then add additional assignments if there is
disagreement among workers. You can use this approach to limit the number of assignments
needed for tasks where there is general agreement, while gathering additional data points
for tasks that are more ambiguous.

Note that HITs created with fewer than 10 assignments cannot be extended to have 10 or
more assignments.

## Modify the HIT Type

The HIT Type attributes of a HIT, such as the reward amount, title, or assignment
duration, can be modified by changing the HIT Type assigned using the `UpdateHITTypeOfHIT` operation. While this can allow you to modify any of
the HIT Type attribute values on an active HIT, Mechanical Turk prevents you from changing the HIT Type
on HITs with assignments that have been accepted or submitted by workers.

## Delete

The `DeleteHIT` operation disposes of HITs that are no longer needed. Calling
this operation deletes your HIT from Mechanical Turk. Once deleted, it is no longer available if you
call `ListHITs`, `GetHIT`, or `ListAssignmentsForHIT`. HITs must be in a `Reviewable` state
to be disposed and all of the completed assignments must be either approved or rejected. As
a result, this operation isn't a solution for removing HITs that you published by mistake,
you should instead use the `UpdateExpirationForHIT` operation to immediately expire your task. HITs
are automatically disposed after 120 days.
