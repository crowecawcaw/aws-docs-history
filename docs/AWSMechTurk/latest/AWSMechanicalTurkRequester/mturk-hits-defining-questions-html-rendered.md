# How Mechanical Turk tasks are rendered

When a worker accepts a task in the Mechanical Turk marketplace, they are directed to a page for
the assignment they've accepted. This page contains an `iframe` HTML element
that has a URL for your task interface. If you define your question using the
`HTMLQuestion` schema, the URL is for a Mechanical Turk location containing the HTML you
provided. If you use the `ExternalQuestion` schema, this is the URL you
provide, which points to your own resources.

Mechanical Turk appends four query parameters to the URL that provide your task interface with
information about the assignment, as shown in the following example.

```

https://tictactoe.amazon.com/gamesurvey.cgi?gameid=01523
  &hitId=123RVWYBAZW00EXAMPLE
  &assignmentId=123RVWYBAZW00EXAMPLE456RVWYBAZW00EXAMPLE
  &turkSubmitTo=https://www.mturk.com/
  &workerId=AZ3456EXAMPLE

```

In this example, the first line is the URL that was provided in an
`ExternalQuestion` definition, and the additional lines contain query
parameters that are appended by Mechanical Turk. These are described below.

- `hitId`: The ID of the HIT
- `assignmentId`: The ID of the assignment that the worker has accepted
  for this HIT
- `turkSubmitTo`: The Mechanical Turk server to which your form should submit a
  response
- `workerId`: The ID of the worker
  In most cases, you won't need to directly interact with these values, but it can be
  useful information in various situations. For example, you can have your question check
  the `assignmentId` value to see if a worker is currently previewing your task
  or if they've accepted it. If the `assignmentId` is
  `ASSIGNMENT_ID_NOT_AVAILABLE,` you can disable input fields so that workers
  don't start working on it before they've accepted it.
