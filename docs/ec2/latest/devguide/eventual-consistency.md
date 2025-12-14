# Eventual consistency in the Amazon EC2 API

The Amazon EC2 API follows an eventual consistency model, due to the distributed nature
of the system supporting the API. This means that the result of an API command you
run that affects your Amazon EC2 resources might not be immediately visible to all
subsequent commands you run. You should keep this in mind when you carry out an API
command that immediately follows a previous API command.

Eventual consistency can affect the way you manage your resources. For example, if
you run a command to create a resource, it will eventually be visible to other
commands. This means that if you run a command to modify or describe the resource
that you just created, its ID might not have propagated throughout the system, and
you will get an error responding that the resource does not exist.

To manage eventual consistency, you can do the following:

- Confirm the state of the resource before you run a command to modify it.
  Run the appropriate `Describe` command using an
  exponential backoff algorithm to ensure that you allow enough time for the
  previous command to propagate through the system. To do this, run the
  `Describe` command repeatedly, starting with a couple
  of seconds of wait time, and increasing gradually up to a few minutes of wait
  time.
- Add wait time between subsequent commands, even if a
  `Describe` command returns an accurate response.
  Apply an exponential backoff algorithm starting with a couple of seconds of
  wait time, and increase gradually up to a few minutes of wait
  time.

###### Eventual consistency error examples

The following are examples of error codes you may encounter as a result of
eventual consistency.

- `InvalidInstanceID.NotFound`

If you successfully run the `RunInstances` command, and
then immediately run another command using the instance ID that was provided
in the response of `RunInstances`, it may return an
`InvalidInstanceID.NotFound` error. This does not mean the
instance does not exist.

Some specific commands that may be affected are:

    + `DescribeInstances`: To confirm the actual
     state of the instance, run this command using an exponential
     backoff algorithm.
    + `TerminateInstances`: To confirm the state of
     the instance, first run the `DescribeInstances`
     command using an exponential backoff algorithm.


    ###### Important

    If you get an `InvalidInstanceID.NotFound` error
     after running `TerminateInstances`, this does
     not mean that the instance is or will be terminated. Your
     instance could still be running. This is why it is important to
     first confirm the instance’s state using
     `DescribeInstances`.

- `InvalidGroup.NotFound`

If you successfully run the `CreateSecurityGroup` command, and then
immediately run another command using the security group ID that was
provided in the response of `CreateSecurityGroup`, it may return
an `InvalidGroup.NotFound` error. To confirm the state of the
security group, run the `DescribeSecurityGroups` command using an
exponential backoff algorithm.

- `InstanceLimitExceeded`

You have requested more instances than your current instance limit allows
for the specified instance type. You could reach this limit unexpectedly if you
are launching and terminating instances rapidly, as terminated instances
count toward your instance limit for a while after they've been terminated.
