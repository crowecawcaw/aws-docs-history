# Adding a source identifier to an Amazon RDS event notification

subscription

You can add a source identifier (the Amazon RDS source generating the event) to an existing subscription.

You can easily add or remove source identifiers using the Amazon RDS console by selecting or deselecting
them when modifying a subscription. For more information, see [Modifying an Amazon RDS event notification subscription](USER_Events.md "USER_Events.md").

To add a source identifier to an Amazon RDS event notification subscription, use the AWS CLI [`add-source-identifier-to-subscription`](../../../index.md "../../../index.md") command. Include
the following required parameters:

- `--subscription-name`
- `--source-identifier`

###### Example

The following example adds the source identifier `mysqldb` to the
`myrdseventsubscription` subscription.

For Linux, macOS, or Unix:

```
aws rds add-source-identifier-to-subscription \
    --subscription-name `myrdseventsubscription` \
    --source-identifier `mysqldb`
```

For Windows:

```
aws rds add-source-identifier-to-subscription ^
    --subscription-name `myrdseventsubscription` ^
    --source-identifier `mysqldb`
```

To add a source identifier to an Amazon RDS event notification subscription, call the Amazon RDS API [`AddSourceIdentifierToSubscription`](../APIReference/API_AddSourceIdentifierToSubscription.md "../APIReference/API_AddSourceIdentifierToSubscription.md"). Include the following required
parameters:

- `SubscriptionName`
- `SourceIdentifier`
