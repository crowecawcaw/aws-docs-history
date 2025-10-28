# Fleet Indexing Troubleshooting

## Troubleshooting aggregation queries for the

fleet indexing service

If you are having type mismatch errors, you can use CloudWatch Logs to troubleshoot the problem.
CloudWatch Logs must be enabled before logs are written by the Fleet Indexing service. For more
information, see [Monitor AWS IoT using CloudWatch Logs](cloud-watch-logs.md "cloud-watch-logs.md").

To make aggregation queries on non-managed fields, you must specify a field you
defined in the `customFields` argument passed to
`UpdateIndexingConfiguration` or
**update-indexing-configuration**. If the field value is inconsistent
with the configured field data type, this value is ignored when you perform an aggregation
query.

If a field cannot be indexed because of a mismatched type, the Fleet Indexing service
sends an error log to CloudWatch Logs. The error log contains the field name, the value that could
not be converted, and the thing name for the device. The following is an example error
log:

```
{
  "timestamp": "2017-02-20 20:31:22.932",
  "logLevel": "ERROR",
  "traceId": "79738924-1025-3a00-a669-7bec69f7f07a",
  "accountId": "000000000000",
  "status": "SucceededWithIssues",
  "eventType": "IndexingCustomFieldFailed",
  "thingName": "thing0",
  "failedCustomFields": [
    {
      "Name": "attributeName1",
      "Value": "apple",
      "ExpectedType": "String"
    },
    {
      "Name": "attributeName2",
      "Value": "2",
      "ExpectedType": "Boolean"
    }
  ]
}
```

If a device has been disconnected for approximately an hour, the connectivity status
`timestamp` value might be missing. For persistent sessions, the value might
be missing after a client has been disconnected longer than the configured time-to-live
(TTL) for the persistent session. The connectivity status data is indexed only for
connections where the client ID has a matching thing name. (The client ID is the value
used to connect a device to AWS IoT Core.)

## Troubleshooting fleet indexing

configuration

**Can't downgrade fleet indexing configuration**

Downgrading fleet indexing configuration is not supported when you want to remove the
data sources that are associated with a fleet metric or a dynamic group.

For example, if your indexing configuration has registry data, shadow data, and
connectivity data, and a fleet metric exists with the query `thingName:TempSensor*
 AND shadow.desired.temperature>80`, updating the indexing configuration to include
only the registry data will result in an error.

Modifying custom fields used by existing fleet metrics is not supported.

**Can't update your indexing configuration due to incompatible
fleet metrics or dynamic groups**

If you can't update your indexing configuration due to incompatible fleet metrics or
dynamic groups, delete the incompatible fleet metrics or dynamic groups before you update
the indexing configuration.

## Troubleshooting location indexing

and geoqueries

To troubleshoot mismatched type errors in location indexing and geoqueries, you can
enable CloudWatch logs. For more information about how to monitor AWS IoT using CloudWatch, follow
[the
step-by-step guide](cloud-watch-logs.md "cloud-watch-logs.md").

When you index location data using geoqueries, the location fields you specify in
`geoLocations` must match the location fields you pass to
`UpdateIndexingConfiguration`. If there's a mismatch, fleet indexing sends a
mismatched type error to CloudWatch. The error log contains the field name, the value that could
not be converted, and the thing name for the device.

The following is an example error log:

```
{
"timestamp": "2023-11-09 01:39:43.466",
    "logLevel": "ERROR",
    "traceId": "79738924-1025-3a00-a669-7bec69f7f07a",
    "accountId": "123456789012",
    "status": "Failure",
    "eventType": "IndexingGeoLocationFieldFailed",
    "thingName": "thing0",
    "failedGeolocationFields": [
        {
"Name": "attributeName1",
            "Value": "apple",
            "ExpectedType": "Geopoint"
        }
    ],
    "reason": "failed to index the field because it could not be converted to one of the expected geoLocation formats."
}
```

For more information, see [Indexing location data](location-indexing-geoquery.md "location-indexing-geoquery.md").

## Troubleshooting fleet metrics

**Can't see data points in CloudWatch**

If you're able to create a fleet metric but you can't see data points in CloudWatch, it's
likely that you don't have a thing that meets the query string criteria.

See this example command of how to create a fleet metric:

```
aws iot create-fleet-metric --metric-name "example_FM" --query-string "thingName:TempSensor* AND attributes.temperature>80" --period 60 --aggregation-field "attributes.temperature" --aggregation-type name=Statistics,values=count

```

If you don't have a thing that meets the query string criteria `--query-string
 "thingName:TempSensor* AND attributes.temperature>80"`:

- With `values=count`, you'll be able to create a fleet metric and
  there'll be data points to show in CloudWatch. The data points of the value
  `count` is always 0.
- With `values` other than `count`, you'll be able to create a
  fleet metric but you won't see the fleet metric in CloudWatch and there'll be no data points
  to show in CloudWatch.
