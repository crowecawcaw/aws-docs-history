# Amazon Mechanical Turk core concepts

The following are the core concepts of Amazon Mechanical Turk (Mechanical Turk) that you need to understand to use it
effectively.

## Requesters and workers

A _requester_ is a company, organization, or person that posts tasks
(HITs) to Mechanical Turk for workers to perform. A _worker_ is a person who
performs the tasks specified by a tequester in a HIT.

## Marketplace

The [Mechanical Turk marketplace](https://worker.mturk.com "https://worker.mturk.com") is where workers can go
to find and accept tasks. In addition to the _production_
marketplace, there is a second [_sandbox_ marketplace](https://workersandbox.mturk.com "https://workersandbox.mturk.com") where requesters can post
development tasks without money changing hands.

More information can be found in Amazon Mechanical Turk marketplace.

## Task or HIT

The base unit of work in Mechanical Turk is called a _Human Intelligence Task_,
which is typically designated as a _HIT_ or
_task_. A HIT represents a single, self-contained task, such
as _Identify the color of the car in the photo_,
that a requester submits to Mechanical Turk for workers to complete.

Mechanical Turk is built around the concept of _microtasks,_ which are small,
atomic tasks that workers can complete in their web browser. When you submit work to
Mechanical Turk, you typically start by breaking it into smaller tasks on which workers can
work independently. In this way, a project involving categorizing 10,000 images
becomes 10,000 individual microtasks that workers can complete. Hundreds of workers
can work on portions of your project at the same time, which increases how quickly
the work can be completed. In addition, you can specify that each task be completed
by multiple workers to allow you to check for quality or identify biases in
subjective questions.

## Assignment

When creating a HIT, you can specify how many workers can accept and complete each task.
Doing so allows you to collect multiple responses for each item and then compare
them. This additional information can be valuable in managing quality, as well as in
collecting multiple data points when responses are subjective.

When a worker accepts a HIT, Mechanical Turk creates an _assignment_, which belongs
exclusively to the worker. The worker can submit results up until the expiration of
the HIT. When retrieving results for a HIT, requesters retrieve all of the submitted
assignments.

## Reward and bonus

A _reward_ is the money you, as a requester, pay workers for
satisfactory work they do on your HITs. A _bonus_ is the amount
you award workers for high-quality performance. Rewards are transmitted to workers
when assignment submissions are approved, either by approving the assignment or when
the auto-approval threshold is reached. Bonuses can be sent to workers who have
recently completed an assignment for you.

## Qualifications

You can use _qualifications_ to specify attributes of the workers
eligible to work on your HITs. Qualifications can be either system-generated, such
as qualifications based on location, or managed by you, based on past performance on
your tasks.

To learn more, see [Selecting eligible workers](SelectingEligibleWorkers.md "SelectingEligibleWorkers.md").
