# Spot Fleet request states

A Spot Fleet request can be one of various states, with each state indicating a different
stage of the request's lifecycle and its management of instances.

A Spot Fleet request can be in one of the following states:

`submitted`

The Spot Fleet request is being evaluated and Amazon EC2 is preparing to launch the
target number of instances. If a request would exceed your Spot Fleet quotas, it
is canceled immediately.

`active`

The Spot Fleet has been validated and Amazon EC2 is attempting to maintain the target
number of running Spot Instances. The request remains in this state until it is
modified or canceled.

`modifying`

The Spot Fleet request is being modified. The request remains in this state
until the modification is fully processed or the request is canceled. Only a
`maintain` fleet type can be modified. This state does not
apply to a one-time `request` fleet type.

`cancelled_running`

The Spot Fleet is canceled (deleted) and does not launch additional Spot Instances. Its
existing instances continue to run until they are interrupted or terminated
manually. The request remains in this state until all instances are
interrupted or terminated.

`cancelled_terminating`

The Spot Fleet is canceled (deleted) and its instances are terminating. The
request remains in this state until all instances are terminated.

`cancelled`

The Spot Fleet is canceled (deleted) and has no running instances. The request
is deleted two days after its instances are terminated.
