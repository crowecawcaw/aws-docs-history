# Addressing stale AWS Config items in the

ServiceNow CMDB

###### Note

ServiceNow administrators are the target audience for this section.

In addition to the AWS Config settings, AWS SMC for ServiceNow now exposes a global API
to identify stale config items from the AWS Config integration.

Stale Config items are the existing AWS Config items that did not
update during the most recent sync for the same source (such as account, Region,
and Aggregator name).

###### Note

This feature requires you to enable the creation relationship to sync the
status setting in the AWS Config System Properties in the ServiceNow
scoped app.

The script includes `x_126749_aws_sc.AwsSmc` and exposes a public
API. You can use this script to access any application scope, including
_global_ scope. As an example, run this
script:

```

   x_126749_aws_sc.AwsSmc.asSyncUser().getStaleConfigItems().forAll(function(object)
{
  gs.info(
       object.accountNumber + '/' + object.region + ' '
       + (object.aggregatorName ? 'aggregator: ' + object.aggregatorName + ' ' :
'')
       + 'ci: ' + object.ci.name
       + ' - ' + object.ci.getDisplayValue('install_status')
  );
});
```

As a background script, it would log the following:

```
Info: 11111111/us-east-1 ci: i-1234567fg6j8 - Installed
Info: 11111111/us-west-1 ci: i-9876541fdgfd - Installed
Info: 22222222/eu-west-1 aggregator: all-dev ci: i-1df5235ftt55 - Installed
```

Each _object_ contains the properties below:

| Property         | Type            | Description                                                                         |
| ---------------- | --------------- | ----------------------------------------------------------------------------------- |
| `accountNumber`  | String          | The account number from which the stale config item<br>originates.                  |
| `region`         | String          | The Region from which the stale config item<br>originates.                          |
| `aggregatorName` | String          | The Aggregator name (if applicable) from which the stale<br>config item originates. |
| `lastSynced`     | `GlideDateTime` | The `GlideDateTime` of the when the last<br>synchronization occurred.               |
| `CI`             | `GlideRecord`   | The `GlideRecord` of the stale config item.                                         |

Optionally, you can also pass an `options` object as the second
argument to the `forAll` method that allows you to customize the
search for stale items.

| Property         | Type            | Description                                                                                                                            |
| ---------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `lowerTimeLimit` | `GlideDateTime` | The threshold `GlideDateTime` from when you should<br>search items. Any stale item last updated prior to that date<br>does not return. |
| `upperTimeLimit` | `GlideDateTime` | The threshold `GlideDateTime` until you should<br>search for items. Any item last updated after that date does not<br>return.          |
| `excludeStatus`  | Number          | The `install_status` to filter on.                                                                                                     |

Timestamps of sync resources:

- `LastSyncTimeField`(default `checked_in`): The
  start of the current sync process.
- `first_discovered` (for new records): The current time. We
  set the `LastDiscoveredField` (default
  `last_discovered`) to the
  `configurationItemCaptureTime` of the resource, if it
  exists or is undefined.
  **Additional notes on stale records**

When AWS Service Management Connector reads AWS Config records that
refer to other resources, it often creates a relationship to those resources.

In some cases, the related resource does not have an entry in the ServiceNow
CMDB. In these cases, the Connector creates a record for that relationship, with
an install status of _absent_. When the
Connector reads the AWS Config record for the related resource, that
record populates.

To see active resources, you should filter ServiceNow records synced from
AWS Config by an install status of _not
Absent_.

**Disclaimer**

Because the script compares items linked to stale sync records, it is unable
to identify stale resources synced before the installation of this SMC version.
When switching to sync with an Aggregator or switching from Aggregator sync to
non-Aggregator sync, the script also fails to detect items that became stale
between the last non-Aggregator sync and the first Aggregator sync.
