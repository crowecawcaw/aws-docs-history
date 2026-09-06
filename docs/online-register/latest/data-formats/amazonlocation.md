

# Data retrieval APIs for Amazon Location
<a name="amazonlocation"></a>

Amazon Location provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="geo-BatchGetDevicePosition"></a>[BatchGetDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchGetDevicePosition.html) | Send a batch request to retrieve device positions | Read | 
| <a name="geo-CalculateRoute"></a>[CalculateRoute](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRoute.html) | Calculate routes using a given route calculator resource | Read | 
| <a name="geo-CalculateRouteMatrix"></a>[CalculateRouteMatrix](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRouteMatrix.html) | Calculate a route matrix using a given route calculator resource | Read | 
| <a name="geo-DescribeGeofenceCollection"></a>[DescribeGeofenceCollection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_DescribeGeofenceCollection.html) | Retrieve geofence collection details | Read | 
| <a name="geo-DescribeKey"></a>[DescribeKey](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_DescribeKey.html) | Retrieve API key resource details and secret | Read | 
| <a name="geo-DescribeMap"></a>[DescribeMap](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeMap.html) | Retrieve map resource details | Read | 
| <a name="geo-DescribePlaceIndex"></a>[DescribePlaceIndex](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribePlaceIndex.html) | Retrieve place-index resource details | Read | 
| <a name="geo-DescribeRouteCalculator"></a>[DescribeRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeRouteCalculator.html) | Retrieve route calculator resource details | Read | 
| <a name="geo-DescribeTracker"></a>[DescribeTracker](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DescribeTracker.html) | Retrieve a tracker resource details | Read | 
| <a name="geo-ForecastGeofenceEvents"></a>[ForecastGeofenceEvents](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ForecastGeofenceEvents.html) | Forecast events for geofences stored in a given geofence collection | Read | 
| <a name="geo-GetDevicePosition"></a>[GetDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_GetDevicePosition.html) | Retrieve the latest device position | Read | 
| <a name="geo-GetDevicePositionHistory"></a>[GetDevicePositionHistory](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_GetDevicePositionHistory.html) | Retrieve the device position history | Read | 
| <a name="geo-GetGeofence"></a>[GetGeofence](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_GetGeofence.html) | Retrieve the geofence details from a geofence-collection | Read | 
| <a name="geo-GetJob"></a>[GetJob](https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_GetJob.html) | Retrieve job details | Read | 
| <a name="geo-GetMapGlyphs"></a>[GetMapGlyphs](https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapGlyphs.html) | Retrieve the glyph file for a map resource | Read | 
| <a name="geo-GetMapSprites"></a>[GetMapSprites](https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapSprites.html) | Retrieve the sprite file for a map resource | Read | 
| <a name="geo-GetMapStyleDescriptor"></a>[GetMapStyleDescriptor](https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapStyleDescriptor.html) | Retrieve the map style descriptor from a map resource | Read | 
| <a name="geo-GetMapTile"></a>[GetMapTile](https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapTile.html) | Retrieve the map tile from the map resource | Read | 
| <a name="geo-GetPlace"></a>[GetPlace](https://docs.aws.amazon.com/location/previous/APIReference/API_GetPlace.html) | Find a place by its unique ID | Read | 
| <a name="geo-ListDevicePositions"></a>[ListDevicePositions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListDevicePositions.html) | Retrieve a list of devices and their latest positions from the given tracker resource | Read | 
| <a name="geo-ListGeofenceCollections"></a>[ListGeofenceCollections](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ListGeofenceCollections.html) | Lists geofence-collections | List | 
| <a name="geo-ListGeofences"></a>[ListGeofences](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ListGeofences.html) | List geofences stored in a given geofence collection | Read | 
| <a name="geo-ListJobs"></a>[ListJobs](https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_ListJobs.html) | List jobs | List | 
| <a name="geo-ListKeys"></a>[ListKeys](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_ListKeys.html) | List API key resources | List | 
| <a name="geo-ListMaps"></a>[ListMaps](https://docs.aws.amazon.com/location/previous/APIReference/API_ListMaps.html) | List map resources | List | 
| <a name="geo-ListPlaceIndexes"></a>[ListPlaceIndexes](https://docs.aws.amazon.com/location/previous/APIReference/API_ListPlaceIndexes.html) | Return a list of place index resources | List | 
| <a name="geo-ListRouteCalculators"></a>[ListRouteCalculators](https://docs.aws.amazon.com/location/previous/APIReference/API_ListRouteCalculators.html) | Return a list of route calculator resources | List | 
| <a name="geo-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_ListTagsForResource.html) | List the tags (metadata) which you have assigned to the resource | Read | 
| <a name="geo-ListTrackerConsumers"></a>[ListTrackerConsumers](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListTrackerConsumers.html) | Retrieve a list of geofence collections currently associated to the given tracker resource | Read | 
| <a name="geo-ListTrackers"></a>[ListTrackers](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListTrackers.html) | Return a list of tracker resources | List | 
| <a name="geo-SearchPlaceIndexForPosition"></a>[SearchPlaceIndexForPosition](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForPosition.html) | Reverse geocodes a given coordinate | Read | 
| <a name="geo-SearchPlaceIndexForSuggestions"></a>[SearchPlaceIndexForSuggestions](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForSuggestions.html) | Generate suggestions for addresses and points of interest based on partial or misspelled free-form text | Read | 
| <a name="geo-SearchPlaceIndexForText"></a>[SearchPlaceIndexForText](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForText.html) | Geocode free-form text, such as an address, name, city or region | Read | 
| <a name="geo-VerifyDevicePosition"></a>[VerifyDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_VerifyDevicePosition.html) | Verify a device position | Read | 