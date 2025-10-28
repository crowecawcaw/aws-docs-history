# Trackers pricing

For pricing information for tracking and geofencing APIs, see the [Amazon Location Service pricing page](https://aws.amazon.com/location/pricing/ "https://aws.amazon.com/location/pricing/").

**Position Written**

You can use `BatchUpdateDevicePosition` to upload position update data
for one or more devices to a tracker resource (up to ten devices per batch). Price
is based on the number of device positions in your API request. Unit price per
device position update is based on the total monthly usage volume. See the [Amazon Location Service pricing page](https://aws.amazon.com/location/pricing/ "https://aws.amazon.com/location/pricing/") for
details on unit price and volume tiers.

You can optimize your Position Written cost by configuring the device position
update frequency (also known as ping rate) from your tracking devices, and
optionally use a local filter to only upload relevant device position updates to
Amazon Location Service.

**Position Read**

You can use `BatchGetDevicePosition` to lists the latest device
positions for requested devices, up to 100 devices per request. You can also use
`GetDevicePosition` to retrieve a device's most recent position
according to its sample time.

Price is based on the number of API requests.

**Position Delete**

You can use `BatchDeleteDevicePositionHistory` to delete the position
history of one or more devices from a tracker resource, up to 100 devices per
request.

Price is based on the number of devices in your API request.

**Position Integrity Evaluation**

You can use `VerifyDevicePosition` to verify the integrity of the
device's position by determining if it was reported behind a proxy, and by comparing
it to an inferred position estimated based on the device's state.

Price is based on the number of API requests.
