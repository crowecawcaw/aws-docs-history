# View all phone pools in AWS End User Messaging SMS

You can use the [describe-pools](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-pools.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-pools.md")
CLI to view information about existing pools.

This operation can provide a complete list of all of the pools in your AWS End User Messaging SMS account,
information about a specific pool, or a list of pools that is filtered based on criteria that
you define.

###### To retrieve a list of all of your pools using the AWS CLI

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 describe-pools
```

To find information about specific pools, use the `PoolId` parameter.

###### To get information about specific pools using the AWS CLI

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 describe-pools \
`>` --pool-id `poolId`
```

In the preceding command, replace `poolId` with the ID or Amazon
Resource Name (ARN) of the pool.

To see a filtered list of pools, use the `Filters` parameter. You can use the
following filter values:

- `status` – The current status of the pool, such as
  `ACTIVE`.
- `message-type` – The type of messages that the pool is used to send.
  Possible values are `TRANSACTIONAL` or `PROMOTIONAL`.
- `two-way-enabled` – A boolean that indicates whether two-way SMS
  messaging is enabled for numbers in the pool.
- `self-managed-opt-outs-enabled` – A boolean that indicates whether
  self-managed SMS opt-outs are enabled for numbers in the pool.
- `opt-out-list-name` – The name of the opt-out list associated with the
  pool.
- `shared-routes-enabled` – A boolean that indicates whether shared
  routes are enabled for the pool.
- `deletion-protection-enabled` – A boolean that indicates whether or not
  the phone number can be deleted using the `DeletePhoneNumber` operation.
  For example, if you want to view a list of pools for transactional messages that support
  two-way messaging, enter the following command at the command line:

```
`$` aws pinpoint-sms-voice-v2 describe-pools \
`>` --filters Name=message-type,Values=TRANSACTIONAL \
`>` --filters Name=two-way-enabled,Values=true
```
