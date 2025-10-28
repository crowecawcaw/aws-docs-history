# Amazon Location Service API and CLI

Amazon Location Service provides API and CLI operations access to the location functionality. See the lists below for more information.

## Amazon Location Service API

This includes the following APIs:

- [Places](../APIReference/API_Operations_Amazon_Location_Service_Places_V2.md "../APIReference/API_Operations_Amazon_Location_Service_Places_V2.md")
- [Routes](../APIReference/API_Operations_Amazon_Location_Service_Routes_V2.md "../APIReference/API_Operations_Amazon_Location_Service_Routes_V2.md")
- [Authentication](../../previous/APIReference/API_Operations-Keys.md "../../previous/APIReference/API_Operations-Keys.md")
- [Maps](../APIReference/API_Operations_Amazon_Location_Service_Maps_V2.md "../APIReference/API_Operations_Amazon_Location_Service_Maps_V2.md")
- [Geofences](../../previous/APIReference/API_Operations-Geofences.md "../../previous/APIReference/API_Operations-Geofences.md")
- [Trackers](../APIReference/API_Operations-Trackers.md "../APIReference/API_Operations-Trackers.md")
- [Tags](../../previous/APIReference/API_Operations-Tags.md "../../previous/APIReference/API_Operations-Tags.md")

## Amazon Location Service CLI

This includes the following CLIs:

### AWS CLI Operations for Amazon Location Service

Amazon Location Service provides AWS CLI (Command-line interface) operations to access location functionality, including the following APIs:

Places

- [autocomplete](../../../cli/latest/reference/geo-places/autocomplete.md "../../../cli/latest/reference/geo-places/autocomplete.md")
- [geocode](../../../cli/latest/reference/geo-places/geocode.md "../../../cli/latest/reference/geo-places/geocode.md")
- [get-place](../../../cli/latest/reference/geo-places/get-place.md "../../../cli/latest/reference/geo-places/get-place.md")
- [reverse-geocode](../../../cli/latest/reference/geo-places/reverse-geocode.md "../../../cli/latest/reference/geo-places/reverse-geocode.md")
- [search-nearby](../../../cli/latest/reference/geo-places/search-nearby.md "../../../cli/latest/reference/geo-places/search-nearby.md")
- [search-text](../../../cli/latest/reference/geo-places/search-text.md "../../../cli/latest/reference/geo-places/search-text.md")
- [Learn More](../../../cli/latest/reference/geo-places.md "../../../cli/latest/reference/geo-places.md")

Routes

- [calculate-isolines](../../../cli/latest/reference/geo-routes/calculate-isolines.md "../../../cli/latest/reference/geo-routes/calculate-isolines.md")
- [calculate-route-matrix](../../../cli/latest/reference/geo-routes/calculate-route-matrix.md "../../../cli/latest/reference/geo-routes/calculate-route-matrix.md")
- [calculate-routes](../../../cli/latest/reference/geo-routes/calculate-routes.md "../../../cli/latest/reference/geo-routes/calculate-routes.md")
- [optimize-waypoints](../../../cli/latest/reference/geo-routes/optimize-waypoints.md "../../../cli/latest/reference/geo-routes/optimize-waypoints.md")
- [snap-to-roads](../../../cli/latest/reference/geo-routes/snap-to-roads.md "../../../cli/latest/reference/geo-routes/snap-to-roads.md")
- [Learn More](../../../cli/latest/reference/geo-routes.md "../../../cli/latest/reference/geo-routes.md")

Authentication

- [create-key](../../../cli/latest/reference/location/create-key.md "../../../cli/latest/reference/location/create-key.md")
- [delete-key](../../../cli/latest/reference/location/delete-key.md "../../../cli/latest/reference/location/delete-key.md")
- [describe-key](../../../cli/latest/reference/location/describe-key.md "../../../cli/latest/reference/location/describe-key.md")
- [list-keys](../../../cli/latest/reference/location/list-keys.md "../../../cli/latest/reference/location/list-keys.md")
- [update-key](../../../cli/latest/reference/location/update-key.md "../../../cli/latest/reference/location/update-key.md")
- [Learn More](../../../cli/latest/reference/location.md "../../../cli/latest/reference/location.md")

Maps

- [get-glyphs](../../../cli/latest/reference/geo-maps/get-glyphs.md "../../../cli/latest/reference/geo-maps/get-glyphs.md")
- [get-sprites](../../../cli/latest/reference/geo-maps/get-sprites.md "../../../cli/latest/reference/geo-maps/get-sprites.md")
- [get-static-map](../../../cli/latest/reference/geo-maps/get-static-map.md "../../../cli/latest/reference/geo-maps/get-static-map.md")
- [get-style-descriptor](../../../cli/latest/reference/geo-maps/get-style-descriptor.md "../../../cli/latest/reference/geo-maps/get-style-descriptor.md")
- [get-tile](../../../cli/latest/reference/geo-maps/get-tile.md "../../../cli/latest/reference/geo-maps/get-tile.md")
- [Learn More](../../../cli/latest/reference/geo-maps.md "../../../cli/latest/reference/geo-maps.md")

Geofences

- [batch-delete-geofence](../../../cli/latest/reference/location/batch-delete-geofence.md "../../../cli/latest/reference/location/batch-delete-geofence.md")
- [batch-evaluate-geofences](../../../cli/latest/reference/location/batch-evaluate-geofences.md "../../../cli/latest/reference/location/batch-evaluate-geofences.md")
- [batch-put-geofence](../../../cli/latest/reference/location/batch-put-geofence.md "../../../cli/latest/reference/location/batch-put-geofence.md")
- [forecast-geofence-events](../../../cli/latest/reference/location/forecast-geofence-events.md "../../../cli/latest/reference/location/forecast-geofence-events.md")
- [create-geofence-collection](../../../cli/latest/reference/location/create-geofence-collection.md "../../../cli/latest/reference/location/create-geofence-collection.md")
- [delete-geofence-collection](../../../cli/latest/reference/location/delete-geofence-collection.md "../../../cli/latest/reference/location/delete-geofence-collection.md")
- [describe-geofence-collection](../../../cli/latest/reference/location/describe-geofence-collection.md "../../../cli/latest/reference/location/describe-geofence-collection.md")
- [list-geofence-collections](../../../cli/latest/reference/location/list-geofence-collections.md "../../../cli/latest/reference/location/list-geofence-collections.md")
- [update-geofence-collection](../../../cli/latest/reference/location/update-geofence-collection.md "../../../cli/latest/reference/location/update-geofence-collection.md")
- [get-geofence](../../../cli/latest/reference/location/get-geofence.md "../../../cli/latest/reference/location/get-geofence.md")
- [list-geofences](../../../cli/latest/reference/location/list-geofences.md "../../../cli/latest/reference/location/list-geofences.md")
- [put-geofence](../../../cli/latest/reference/location/put-geofence.md "../../../cli/latest/reference/location/put-geofence.md")
- [Learn More](../../../cli/latest/reference/location.md "../../../cli/latest/reference/location.md")

Trackers

- [batch-get-device-position](../../../cli/latest/reference/location/batch-get-device-position.md "../../../cli/latest/reference/location/batch-get-device-position.md")
- [batch-update-device-position](../../../cli/latest/reference/location/batch-update-device-position.md "../../../cli/latest/reference/location/batch-update-device-position.md")
- [batch-delete-device-position-history](../../../cli/latest/reference/location/batch-delete-device-position-history.md "../../../cli/latest/reference/location/batch-delete-device-position-history.md")
- [get-device-position](../../../cli/latest/reference/location/get-device-position.md "../../../cli/latest/reference/location/get-device-position.md")
- [get-device-position-history](../../../cli/latest/reference/location/get-device-position-history.md "../../../cli/latest/reference/location/get-device-position-history.md")
- [associate-tracker-consumer](../../../cli/latest/reference/location/associate-tracker-consumer.md "../../../cli/latest/reference/location/associate-tracker-consumer.md")
- [disassociate-tracker-consumer](../../../cli/latest/reference/location/disassociate-tracker-consumer.md "../../../cli/latest/reference/location/disassociate-tracker-consumer.md")
- [create-tracker](../../../cli/latest/reference/location/create-tracker.md "../../../cli/latest/reference/location/create-tracker.md")
- [delete-tracker](../../../cli/latest/reference/location/delete-tracker.md "../../../cli/latest/reference/location/delete-tracker.md")
- [describe-tracker](../../../cli/latest/reference/location/describe-tracker.md "../../../cli/latest/reference/location/describe-tracker.md")
- [list-trackers](../../../cli/latest/reference/location/list-trackers.md "../../../cli/latest/reference/location/list-trackers.md")
- [update-tracker](../../../cli/latest/reference/location/update-tracker.md "../../../cli/latest/reference/location/update-tracker.md")
- [list-tracker-consumers](../../../cli/latest/reference/location/list-tracker-consumers.md "../../../cli/latest/reference/location/list-tracker-consumers.md")
- [verify-device-position](../../../cli/latest/reference/location/verify-device-position.md "../../../cli/latest/reference/location/verify-device-position.md")
- [Learn More](../../../cli/latest/reference/location.md "../../../cli/latest/reference/location.md")

Tags

- [list-tags-for-resource](../../../cli/latest/reference/location/list-tags-for-resource.md "../../../cli/latest/reference/location/list-tags-for-resource.md")
- [tag-resource](../../../cli/latest/reference/location/tag-resource.md "../../../cli/latest/reference/location/tag-resource.md")
- [untag-resource](../../../cli/latest/reference/location/untag-resource.md "../../../cli/latest/reference/location/untag-resource.md")
- [Learn More](../../../cli/latest/reference/location.md "../../../cli/latest/reference/location.md")
