# Removing a source identifier from an Amazon RDS event notification subscription

You can remove a source identifier (the Amazon RDS source generating the event) from a subscription if you no longer
want to be notified of events for that source.

You can easily add or remove source identifiers using the Amazon RDS console by selecting or deselecting
them when modifying a subscription. For more information, see [Modifying an Amazon RDS event notification subscription](USER_Events.Modifying.md "USER_Events.Modifying.md").

To remove a source identifier from an Amazon RDS event notification subscription, use the AWS CLI [`remove-source-identifier-from-subscription`](../../../cli/latest/reference/rds/remove-source-identifier-from-subscription.md "../../../cli/latest/reference/rds/remove-source-identifier-from-subscription.md") command. Include the following
required parameters:

- `--subscription-name`
- `--source-identifier`

###### Example

The following example removes the source identifier `mysqldb` from the
`myrdseventsubscription` subscription.

For Linux, macOS, or Unix:

```
aws rds remove-source-identifier-from-subscription \
    --subscription-name `myrdseventsubscription` \
    --source-identifier `mysqldb`
```

For Windows:

```
aws rds remove-source-identifier-from-subscription ^
    --subscription-name `myrdseventsubscription` ^
    --source-identifier `mysqldb`
```

To remove a source identifier from an Amazon RDS event notification subscription, use the Amazon RDS API [`RemoveSourceIdentifierFromSubscription`](../APIReference/API_RemoveSourceIdentifierFromSubscription.md "../APIReference/API_RemoveSourceIdentifierFromSubscription.md") command. Include the following
required parameters:

- `SubscriptionName`
- `SourceIdentifier`
