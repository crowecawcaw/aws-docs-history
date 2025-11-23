# Geofences pricing

For pricing information for tracking and geofencing APIs, see the [Amazon Location Service pricing page](https://aws.amazon.com//location/pricing/ "https://aws.amazon.com//location/pricing/").

**Position Evaluation**

You can use `BatchEvaluateGeofences` to evaluate device positions
against the geofence geometries from a given geofence collection. One request will
evaluate up to ten device positions against all geofences in a single geofence
collection. Price is based on the number of device positions in your API requests.
Unit price per device position evaluated is based on the total monthly usage volume.
See the [Amazon Location Service pricing
page](https://aws.amazon.com//location/pricing/ "https://aws.amazon.com//location/pricing/") for details on unit price and volume tiers.

You can optimize your Position Evaluation cost by configuring the device position
update frequency (also known as ping rate) from your tracking devices, and
leveraging the filtering feature on Trackers to only evaluate relevant position
updates.

**Geofence Management and Storage**

You can use `GetGeofence`, `PutGeofence`,
`BatchPutGeofence`, and `BatchDeleteGeofence` to manage
your geofences in a geofence collection. The price for these APIs is based on the
number of geofences in your API requests.

The storage for geofences will be charged monthly (only for geofences you store
for more than one month). You can also manage your Geofence Collection using the
following APIs: `CreateGeofenceCollection`,
`DeleteGeofenceCollection`, `DescribeGeofenceCollection`,
`ListGeofenceCollections`, `UpdateGeofenceCollection`, and
`ListGeofences`. The price for these APIs is based on the number of
API requests.

**Geofence Event Forecast**

You can use `ForecastGeofenceEvents` to forecast future geofence events
that are likely to occur within a specified time horizon if a device continues
moving at its current speed. The price is based on number of API requests.
