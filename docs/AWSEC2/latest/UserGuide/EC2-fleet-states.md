# EC2 Fleet request states

An EC2 Fleet request can be one of various states, with each state indicating a different
stage of the request's lifecycle and its management of instances.

An EC2 Fleet request can be in one of the following states:

`submitted`

The EC2 Fleet request is being evaluated and Amazon EC2 is preparing to launch the target number of
instances. If a request would exceed your fleet limits, it is deleted
immediately.

`active`

The EC2 Fleet request has been validated and Amazon EC2 is attempting to maintain
the target number of running instances. The request remains in this state
until it is modified or deleted.

`modifying`

The EC2 Fleet request is being modified. The request remains in this state
until the modification is fully processed or the request is deleted. Only a
`maintain` fleet type can be modified. This state does not
apply to other request types.

`deleted_running`

The EC2 Fleet request is deleted and does not launch additional Spot Instances. Its existing instances
continue to run until they are interrupted or terminated manually. The
request remains in this state until all instances are interrupted or
terminated. Only an EC2 Fleet of type `maintain` or
`request` can have running instances after the EC2 Fleet request
is deleted. A deleted `instant` fleet with running instances is
not supported. This state does not apply to `instant`
fleets.

`deleted_terminating`

The EC2 Fleet request is deleted and its instances are terminating. The request
remains in this state until all instances are terminated.

`deleted`

The EC2 Fleet request is deleted and has no running instances. The request is deleted two days
after its instances are terminated.
