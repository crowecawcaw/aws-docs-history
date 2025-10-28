# Policy configurations for quorum queues for Amazon MQ for RabbitMQ

You can add specific policy configurations to quorum queues for your RabbitMQ broker on Amazon MQ.

When you create a policy for quorum queues, you must do the following:

- Remove all policy attributes that start with `ha`,
  such as `ha-mode`, `ha-params`, `ha-sync-mode`,
  `ha-sync-batch-size`, `ha-promote-on-shutdown`,
  and `ha-promote-on-failure`.
- Remove `queue-mode`.
- Change overflow when it is set to `reject-publish-dlx`

###### Important

Amazon MQ for RabbitMQ applies all or none of the attributes within a policy.
You cannot create a policy that applies to both classic mirrored queues and quorum queues.
If you want your policy to only apply to quorum queues,
you must set `--apply-to` to `quorum_queues`.
If you are using classic mirrored queues and quorum queues,
you must create a separate policy with `--apply-to`:`classic_queues`
as well as a quorum queues policy.

You do not need to modify `AWS-DEFAULT` policies
because they automatically adopt the new queue type in the “applies to” parameter.
For more information on default policies for Amazon MQ for RabbitMQ, see
[RabbitMQ configuration policies](rabbitmq-configuration-policies.md "rabbitmq-configuration-policies.md").
