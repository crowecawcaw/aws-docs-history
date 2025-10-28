# Create a tracker

Create a tracker resource to store and process position updates from your devices.
You can use the Amazon Location Service console, the AWS CLI, or the Amazon Location APIs.

Each position update stored in your tracker resources can include a measure of
position accuracy, and up to three fields of metadata about the position or device
that you want to store. The metadata is stored as key-value pairs, and can store
information such as speed, direction, tire pressure, or engine temperature.

Trackers filter position updates as they are received. This reduces visual noise
in your device paths (called _jitter_), and reduces the number of
false geofence entry and exit events. This also helps manage costs by reducing the
number of geofence evaluations initiated.

Trackers offer three position filtering options to help manage costs and reduce
jitter in your location updates.

- **Accuracy-based** – _Use
  with any device that provides an accuracy measurement. Most mobile
  devices provide this information._ The accuracy of each
  position measurement is affected by many environmental factors, including
  GPS satellite reception, landscape, and the proximity of Wi-Fi and Bluetooth
  devices. Most devices, including most mobile devices, can provide an
  estimate of the accuracy of the measurement along with the measurement. With
  `AccuracyBased` filtering, Amazon Location ignores location updates
  if the device moved less than the measured accuracy. For example, if two
  consecutive updates from a device have an accuracy range of 5 m and 10 m,
  Amazon Location ignores the second update if the device has moved less than 15 m.
  Amazon Location neither evaluates ignored updates against geofences, nor stores
  them.

When accuracy is not provided, it is treated as zero, and the measurement
is considered perfectly accurate.

###### Note

You can also use accuracy-based filtering to remove all filtering. If
you select accuracy-based filtering, but override all accuracy data to
zero, or omit the accuracy entirely, then Amazon Location will not filter out
any updates.

- **Distance-based** – _Use
  when your devices do not provide an accuracy measurement, but you still
  want to take advantage of filtering to reduce jitter and manage
  costs._
  `DistanceBased` filtering ignores location updates in which
  devices have moved less than 30 m (98.4 ft). When you use
  `DistanceBased` position filtering, Amazon Location neither
  evaluates these ignored updates against geofences nor stores the
  updates.

The accuracy of most mobile devices, including the average accuracy of iOS
and Android devices, is within 15 m. In most applications,
`DistanceBased` filtering can reduce the effect of location
inaccuracies when displaying device trajectory on a map, and the bouncing
effect of multiple consecutive entry and exit events when devices are near
the border of a geofence. It can also help reduce the cost of your
application, by making fewer calls to evaluate against linked geofences or
retrieve device positions.

- **Time-based** – (default)
  _Use when your devices send position updates very frequently
  (more than once every 30 seconds), and you want to achieve near
  real-time geofence evaluations without storing every update._ In `TimeBased` filtering, every location update is
  evaluated against linked geofence collections, but not every location update
  is stored. If your update frequency is more often than 30 seconds, only one
  update per 30 seconds is stored for each unique device ID.

###### Note

Be mindful of the costs of your tracking application when deciding your
filtering method and the frequency of position updates. You are billed for every
location update and once for evaluating the position update against each linked
geofence collection. For example, when using time-based filtering, if your
tracker is linked to two geofence collections, every position update will count
as one location update request and two geofence collection evaluations. If you
are reporting position updates every 5 seconds for your devices and using
time-based filtering, you will be billed for 720 location updates and 1,440
geofence evaluations per hour for each device.

Your bill is not affected by the number of geofences in each collection. Since
each geofence collection may contain up to 50,000 geofences, you may want to
combine your geofences into fewer collections, where possible, to reduce your
cost of geofence evaluations.

By default, you will get EventBridge events each time a tracked device enters or
exits a linked geofence. For more information, see
[Link a tracker to a geofence collection](associate-consumer.md "associate-consumer.md").

You can enable events for all filtered position updates for a tracker
resource. For more information, see [Enable update events for a tracker](location-events.md#enable-update-events "location-events.md#enable-update-events").

###### Note

If you wish to encrypt your data using your own AWS KMS customer managed key, then the Bounding
Polygon Queries feature will be disabled by default. This is because by using
this Bounding Polygon Queries feature, a representation of your device positions
will not be encrypted using your AWS KMS managed key. However, the exact device
position is still encrypted using your managed key.

You can choose to opt-in to the Bounding Polygon Queries feature by setting the `KmsKeyEnableGeospatialQueries` parameter to true when creating or updating a Tracker.

Console
**To create a tracker using the Amazon Location
console**

1. Open the Amazon Location Service console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. In the left navigation pane, choose **Trackers**.
3. Choose **Create tracker**.
4. Fill the following fields:
   - **Name** – Enter a unique name.
     For example, `ExampleTracker`.
     Maximum 100 characters. Valid entries include
     alphanumeric characters, hyphens, periods, and
     underscores.
   - **Description**
     – Enter an optional description.

5. Under **Position filtering**, choose the
   option that best fits how you intend to use your tracker
   resource. If you do not set **Position
   filtering**, the default setting is
   `TimeBased`. For more information, see [Amazon Location Service trackers](trackers.md "trackers.md") in this guide, and
   `PositionFiltering` in the Amazon Location Service
   Trackers API Reference.
6. (Optional) Under **Tags**, enter a tag
   **Key** and **Value**.
   This adds a tag your new geofence collection. For more
   information, see [How to use tags](manage-resources.md#manage-resources_how-to "manage-resources.md#manage-resources_how-to").
7. (Optional) Under **Customer managed key
   encryption**, you can choose to **Add a
   customer managed key**. This adds a symmetric
   customer managed key that you create, own, and manage over the
   default AWS owned encryption. For more information, see [Encrypting data at
   rest](encryption-at-rest.md "encryption-at-rest.md").
8. (Optional) Under **KmsKeyEnableGeospatialQueries**, you can choose to enable
   **Geospatial Queries**. This allows you use the Bounding Polygon Queries feature, while encrypting your data using a customer AWS KMS managed key.

###### Note

When you use the Bounding Polygon Queries feature a representation of your device positions is
not be encrypted using your AWS KMS managed key. However, the
exact device position is still encrypted using your managed
key. 9. (Optional) Under **EventBridge configuration**,
you can choose to enable EventBridge events for filtered position
updates. This will send an event each time a position
update for a device in this tracker meets the position
filtering evaluation. 10. Choose **Create tracker**.

API
**To create a tracker by using the Amazon Location
APIs**

Use the `CreateTracker` operation from the Amazon Location
Trackers APIs.

The following example uses an API request to create a tracker called
`ExampleTracker`. The tracker resource is
associated with a [customer managed
AWS KMS key to encrypt customer data](encryption-at-rest.md "encryption-at-rest.md"), and does not [enable position
updates in EventBridge](location-events.md#enable-update-events "location-events.md#enable-update-events").

```
POST /tracking/v0/trackers
Content-type: application/json

{

   "TrackerName": "ExampleTracker",
   "Description": "string",
   "KmsKeyEnableGeospatialQueries": false,
   "EventBridgeEnabled": false,
   "KmsKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
   "PositionFiltering": "AccuracyBased",
   "Tags": {
      "string" : "string"
   }
}
```

**Create a tracker with `KmsKeyEnableGeospatialQueries` enabled**

The following example has the parameter
`KmsKeyEnableGeospatialQueries` set to true.
This allows you use the Bounding Polygon Queries feature,
while encrypting your data using a customer AWS KMS managed key.

For information on using the Bounding Polygon Queries feature, see [List your device positions](list-device-positions.md "list-device-positions.md")

###### Note

When you use the Bounding Polygon Queries feature a representation of your device positions is
not be encrypted using your AWS KMS managed key. However, the exact
device position is still encrypted using your managed key.

```
POST /tracking/v0/trackers
Content-type: application/json

{

   "TrackerName": "`ExampleTracker`",
   "Description": "string",
   "KmsKeyEnableGeospatialQueries": true,
   "EventBridgeEnabled": false,
   "KmsKeyId": "`1234abcd-12ab-34cd-56ef-1234567890ab`",
   "PositionFiltering": "`AccuracyBased`",
   "Tags": {
      "string" : "string"
   }
}
```

AWS CLI
**To create a tracker using AWS CLI
commands**

Use the `create-tracker` command.

The following example uses the AWS CLI to create a tracker called
`ExampleTracker`. The tracker resource is
associated with a [customer managed
AWS KMS key to encrypt customer data](encryption-at-rest.md "encryption-at-rest.md"), and does not [enable position
updates in EventBridge](location-events.md#enable-update-events "location-events.md#enable-update-events").

```
aws location \
  create-tracker \
  --tracker-name "``ExampleTracker``" \
  --position-filtering "`AccuracyBased`" \
  --event-bridge-enabled false \
  --kms-key-enable-geospatial-queries false \
  --kms-key-id "`1234abcd-12ab-34cd-56ef-1234567890ab`"
```

**Create a tracker with `KmsKeyEnableGeospatialQueries` enabled**

The following example has the parameter
`KmsKeyEnableGeospatialQueries` set to true.
This allows you use the Bounding Polygon Queries feature,
while encrypting your data using a customer AWS KMS managed key.

For information on using the Bounding Polygon Queries feature, see [List your device positions](list-device-positions.md "list-device-positions.md")

###### Note

When you use the Bounding Polygon Queries feature a representation of your device positions is
not be encrypted using your AWS KMS managed key. However, the exact
device position is still encrypted using your managed key.

```
aws location \
  create-tracker \
  --tracker-name "``ExampleTracker``" \
  --position-filtering "`AccuracyBased`" \
  --event-bridge-enabled false \
  --kms-key-enable-geospatial-queries true \
  --kms-key-id "`1234abcd-12ab-34cd-56ef-1234567890ab`"
```

###### Note

Billing depends on your usage. You may incur fees for the use of other AWS
services. For more information, see [Amazon Location Service
pricing](https://aws.amazon.com/location/pricing/ "https://aws.amazon.com/location/pricing/").

You can edit the **Description**, **Position
filtering**, and **EventBridge configuration** after the
tracker is created by choosing **Edit tracker**.
