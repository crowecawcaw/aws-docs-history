# Manage your Amazon Location Service tracker

You can manage your trackers using the Amazon Location console, the AWS CLI, or the Amazon Location
APIs.

## List your trackers

You can view your trackers list using the Amazon Location console, the AWS CLI, or the
Amazon Location APIs:

Console
**To view a list of existing trackers using the
Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. Choose **Trackers** from the left
   navigation.
3. View a list of your tracker resources under **My trackers**.

API
Use the `ListTrackers` operation from the Amazon Location
Trackers APIs.

The following example is an API request to get a list of trackers in
your AWS account.

```
POST /tracking/v0/list-trackers
```

The following is an example response for `ListTrackers`:

```
{
   "Entries": [
      {
         "CreateTime": 2020-10-02T19:09:07.327Z,
         "Description": "string",
         "TrackerName": "`ExampleTracker`",
         "UpdateTime": 2020-10-02T19:10:07.327Z
      }
   ],
   "NextToken": "1234-5678-9012"
}
```

CLI
Use the `list-trackers` command.

The following example is an AWS CLI to get a list of trackers in your
AWS account.

```
aws location list-trackers
```

## Disconnecting a tracker from a geofence

collection

You can disconnect a tracker from a geofence collection using the Amazon Location
console, the AWS CLI, or the Amazon Location APIs:

Console
**To disassociate a tracker from an associated
geofence collection using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. Choose **Trackers** from the left
   navigation pane.
3. Under **My trackers**, select the
   name link of the target tracker.
4. Under **Linked Geofence
   Collections**, select a geofence collection with a
   **Linked** status.
5. Choose **Unlink**.

API
Use the `DisassociateTrackerConsumer` operation from the
Amazon Location Trackers APIs.

The following example is an API request to disassociate a tracker from
an associated geofence collection.

```
DELETE /tracking/v0/trackers/`ExampleTracker`/consumers/arn:aws:geo:us-west-2:123456789012:geofence-collection/ExampleCollection
```

The following is an example response for `DisassociateTrackerConsumer`:

```
HTTP/1.1 200
```

CLI
Use the `disassociate-tracker-consumer` command.

The following example is an AWS CLI command to disassociate a tracker
from an associated geofence collection.

```
aws location disassociate-tracker-consumer \
    --consumer-arn "arn:aws:geo:us-west-2:123456789012:geofence-collection/ExampleCollection" \
    --tracker-name "`ExampleTracker`"
```

## Get tracker details

You can get details about any tracker in your AWS account by using the Amazon Location
console, the AWS CLI, or the Amazon Location APIs.

Console
**To view tracker details by using the Amazon Location
console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. Choose **Trackers** from the left
   navigation.
3. Under **My trackers**, select the
   name link of the target tracker.
4. View the tracker details under
   **Information**.

API
Use the `DescribeTracker` operation from the Amazon Location
Tracker APIs.

The following example is an API request to get the tracker details for
`ExampleTracker`.

```
GET /tracking/v0/trackers/`ExampleTracker`
```

The following is an example response for `DescribeTracker`:

```
{
   "CreateTime": 2020-10-02T19:09:07.327Z,
   "Description": "string",
   "EventBridgeEnabled": false,
   "KmsKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
   "PositionFiltering": "TimeBased",
   "Tags": {
      "Tag1" : "Value1"
   },
   "TrackerArn": "arn:aws:geo:us-west-2:123456789012:tracker/ExampleTracker",
   "TrackerName": "`ExampleTracker`",
   "UpdateTime": 2020-10-02T19:10:07.327Z
}
```

CLI
Use the `describe-tracker` command.

The following example is an AWS CLI command to get tracker details for
`ExampleTracker`.

```
aws location describe-tracker \
    --tracker-name "`ExampleTracker`"
```

## Delete a tracker

You can delete a tracker from your AWS account using the Amazon Location console, the
AWS CLI, or the Amazon Location APIs:

Console
**To delete an existing map resource using the
Amazon Location console**

###### Warning

This operation deletes the resource permanently. If the tracker
resource is in use, you may encounter an error. Make sure that the
target resource isn't a dependency for your applications.

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. Choose **Trackers** from the left navigation
   pane.
3. Under **My trackers**, select the target
   tracker.
4. Choose **Delete tracker**.

API
Use the `DeleteTracker` operation from the Amazon Location
Tracker APIs.

The following example is an API request to delete the tracker
`ExampleTracker`.

```
DELETE /tracking/v0/trackers/`ExampleTracker`
```

The following is an example response for `DeleteTracker`:

```
HTTP/1.1 200
```

CLI
Use the `delete-tracker` command.

The following example is an AWS CLI command to delete the tracker
`ExampleTracker`.

```
aws location delete-tracker \
    --tracker-name "`ExampleTracker`"
```
