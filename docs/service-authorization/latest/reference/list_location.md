

# Actions, resources, and condition keys for Amazon Location
<a name="list_location"></a>

Amazon Location (service prefix: `geo`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/location/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/location/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/location/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/geo/geo.json) for this service.

**Topics**
+ [API operations defined by Amazon Location](#list_location-operations)
+ [Actions defined by Amazon Location](#list_location-actions-as-permissions)
+ [Resource types defined by Amazon Location](#list_location-resources-for-iam-policies)
+ [Condition keys for Amazon Location](#list_location-policy-keys)

## API operations defined by Amazon Location
<a name="list_location-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_location-actions-as-permissions).




- **   AssociateTrackerConsumer  **
  - **IAM action:**  [geo:AssociateTrackerConsumer](#list_location-action-AssociateTrackerConsumer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteDevicePositionHistory  **
  - **IAM action:**  [geo:BatchDeleteDevicePositionHistory](#list_location-action-BatchDeleteDevicePositionHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteGeofence  **
  - **IAM action:**  [geo:BatchDeleteGeofence](#list_location-action-BatchDeleteGeofence) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchEvaluateGeofences  **
  - **IAM action:**  [geo:BatchEvaluateGeofences](#list_location-action-BatchEvaluateGeofences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetDevicePosition  **
  - **IAM action:**  [geo:BatchGetDevicePosition](#list_location-action-BatchGetDevicePosition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchPutGeofence  **
  - **IAM action:**  [geo:BatchPutGeofence](#list_location-action-BatchPutGeofence) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchUpdateDevicePosition  **
  - **IAM action:**  [geo:BatchUpdateDevicePosition](#list_location-action-BatchUpdateDevicePosition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CalculateRoute  **
  - **IAM action:**  [geo:CalculateRoute](#list_location-action-CalculateRoute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CalculateRouteMatrix  **
  - **IAM action:**  [geo:CalculateRouteMatrix](#list_location-action-CalculateRouteMatrix) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CancelJob  **
  - **IAM action:**  [geo:CancelJob](#list_location-action-CancelJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGeofenceCollection  **
  - **IAM action:**  [geo:CreateGeofenceCollection](#list_location-action-CreateGeofenceCollection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [geo:TagResource](#list_location-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateKey  **
  - **IAM action:**  [geo:CalculateRoute](#list_location-action-CalculateRoute)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:CalculateRouteMatrix](#list_location-action-CalculateRouteMatrix)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:CreateKey](#list_location-action-CreateKey)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [geo:GetMapGlyphs](#list_location-action-GetMapGlyphs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:GetMapSprites](#list_location-action-GetMapSprites)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:GetMapStyleDescriptor](#list_location-action-GetMapStyleDescriptor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:GetMapTile](#list_location-action-GetMapTile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:GetPlace](#list_location-action-GetPlace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:SearchPlaceIndexForPosition](#list_location-action-SearchPlaceIndexForPosition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:SearchPlaceIndexForSuggestions](#list_location-action-SearchPlaceIndexForSuggestions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:SearchPlaceIndexForText](#list_location-action-SearchPlaceIndexForText)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:TagResource](#list_location-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [geo-maps:GetStaticMap](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStaticMap.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-maps:GetTile](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetTile.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:Autocomplete](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Autocomplete.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:Geocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Geocode.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:GetPlace](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GetPlace.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:ReverseGeocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ReverseGeocode.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:SearchNearby](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchNearby.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:SearchText](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchText.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:Suggest](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Suggest.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-routes:CalculateIsolines](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateIsolines.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-routes:CalculateRouteMatrix](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRouteMatrix.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-routes:CalculateRoutes](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRoutes.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-routes:OptimizeWaypoints](https://docs.aws.amazon.com/location/latest/APIReference/API_OptimizeWaypoints.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-routes:SnapToRoads](https://docs.aws.amazon.com/location/latest/APIReference/API_SnapToRoads.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateMap  **
  - **IAM action:**  [geo:CreateMap](#list_location-action-CreateMap)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [geo:TagResource](#list_location-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePlaceIndex  **
  - **IAM action:**  [geo:CreatePlaceIndex](#list_location-action-CreatePlaceIndex)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [geo:TagResource](#list_location-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRouteCalculator  **
  - **IAM action:**  [geo:CreateRouteCalculator](#list_location-action-CreateRouteCalculator)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [geo:TagResource](#list_location-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTracker  **
  - **IAM action:**  [geo:CreateTracker](#list_location-action-CreateTracker)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [geo:TagResource](#list_location-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteGeofenceCollection  **
  - **IAM action:**  [geo:DeleteGeofenceCollection](#list_location-action-DeleteGeofenceCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteKey  **
  - **IAM action:**  [geo:DeleteKey](#list_location-action-DeleteKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMap  **
  - **IAM action:**  [geo:DeleteMap](#list_location-action-DeleteMap) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePlaceIndex  **
  - **IAM action:**  [geo:DeletePlaceIndex](#list_location-action-DeletePlaceIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRouteCalculator  **
  - **IAM action:**  [geo:DeleteRouteCalculator](#list_location-action-DeleteRouteCalculator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTracker  **
  - **IAM action:**  [geo:DeleteTracker](#list_location-action-DeleteTracker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeGeofenceCollection  **
  - **IAM action:**  [geo:DescribeGeofenceCollection](#list_location-action-DescribeGeofenceCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeKey  **
  - **IAM action:**  [geo:DescribeKey](#list_location-action-DescribeKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMap  **
  - **IAM action:**  [geo:DescribeMap](#list_location-action-DescribeMap) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePlaceIndex  **
  - **IAM action:**  [geo:DescribePlaceIndex](#list_location-action-DescribePlaceIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRouteCalculator  **
  - **IAM action:**  [geo:DescribeRouteCalculator](#list_location-action-DescribeRouteCalculator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTracker  **
  - **IAM action:**  [geo:DescribeTracker](#list_location-action-DescribeTracker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateTrackerConsumer  **
  - **IAM action:**  [geo:DisassociateTrackerConsumer](#list_location-action-DisassociateTrackerConsumer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ForecastGeofenceEvents  **
  - **IAM action:**  [geo:ForecastGeofenceEvents](#list_location-action-ForecastGeofenceEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDevicePosition  **
  - **IAM action:**  [geo:GetDevicePosition](#list_location-action-GetDevicePosition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDevicePositionHistory  **
  - **IAM action:**  [geo:GetDevicePositionHistory](#list_location-action-GetDevicePositionHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGeofence  **
  - **IAM action:**  [geo:GetGeofence](#list_location-action-GetGeofence) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJob  **
  - **IAM action:**  [geo:GetJob](#list_location-action-GetJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMapGlyphs  **
  - **IAM action:**  [geo:GetMapGlyphs](#list_location-action-GetMapGlyphs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMapSprites  **
  - **IAM action:**  [geo:GetMapSprites](#list_location-action-GetMapSprites) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMapStyleDescriptor  **
  - **IAM action:**  [geo:GetMapStyleDescriptor](#list_location-action-GetMapStyleDescriptor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMapTile  **
  - **IAM action:**  [geo:GetMapTile](#list_location-action-GetMapTile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPlace  **
  - **IAM action:**  [geo:GetPlace](#list_location-action-GetPlace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDevicePositions  **
  - **IAM action:**  [geo:ListDevicePositions](#list_location-action-ListDevicePositions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListGeofenceCollections  **
  - **IAM action:**  [geo:ListGeofenceCollections](#list_location-action-ListGeofenceCollections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGeofences  **
  - **IAM action:**  [geo:ListGeofences](#list_location-action-ListGeofences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListJobs  **
  - **IAM action:**  [geo:ListJobs](#list_location-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKeys  **
  - **IAM action:**  [geo:ListKeys](#list_location-action-ListKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMaps  **
  - **IAM action:**  [geo:ListMaps](#list_location-action-ListMaps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPlaceIndexes  **
  - **IAM action:**  [geo:ListPlaceIndexes](#list_location-action-ListPlaceIndexes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRouteCalculators  **
  - **IAM action:**  [geo:ListRouteCalculators](#list_location-action-ListRouteCalculators) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [geo:ListTagsForResource](#list_location-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTrackerConsumers  **
  - **IAM action:**  [geo:ListTrackerConsumers](#list_location-action-ListTrackerConsumers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTrackers  **
  - **IAM action:**  [geo:ListTrackers](#list_location-action-ListTrackers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutGeofence  **
  - **IAM action:**  [geo:PutGeofence](#list_location-action-PutGeofence) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchPlaceIndexForPosition  **
  - **IAM action:**  [geo:SearchPlaceIndexForPosition](#list_location-action-SearchPlaceIndexForPosition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchPlaceIndexForSuggestions  **
  - **IAM action:**  [geo:SearchPlaceIndexForSuggestions](#list_location-action-SearchPlaceIndexForSuggestions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchPlaceIndexForText  **
  - **IAM action:**  [geo:SearchPlaceIndexForText](#list_location-action-SearchPlaceIndexForText) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartJob  **
  - **IAM action:**  [geo:StartJob](#list_location-action-StartJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [geo:TagResource](#list_location-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** geo.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [geo:TagResource](#list_location-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [geo:UntagResource](#list_location-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateGeofenceCollection  **
  - **IAM action:**  [geo:UpdateGeofenceCollection](#list_location-action-UpdateGeofenceCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateKey  **
  - **IAM action:**  [geo:CalculateRoute](#list_location-action-CalculateRoute)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:CalculateRouteMatrix](#list_location-action-CalculateRouteMatrix)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:GetMapGlyphs](#list_location-action-GetMapGlyphs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:GetMapSprites](#list_location-action-GetMapSprites)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:GetMapStyleDescriptor](#list_location-action-GetMapStyleDescriptor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:GetMapTile](#list_location-action-GetMapTile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:GetPlace](#list_location-action-GetPlace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:SearchPlaceIndexForPosition](#list_location-action-SearchPlaceIndexForPosition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:SearchPlaceIndexForSuggestions](#list_location-action-SearchPlaceIndexForSuggestions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:SearchPlaceIndexForText](#list_location-action-SearchPlaceIndexForText)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo:UpdateKey](#list_location-action-UpdateKey)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [geo-maps:GetStaticMap](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStaticMap.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-maps:GetTile](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetTile.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:Autocomplete](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Autocomplete.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:Geocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Geocode.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:GetPlace](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GetPlace.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:ReverseGeocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ReverseGeocode.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:SearchNearby](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchNearby.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:SearchText](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchText.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-places:Suggest](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Suggest.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-routes:CalculateIsolines](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateIsolines.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-routes:CalculateRouteMatrix](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRouteMatrix.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-routes:CalculateRoutes](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRoutes.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-routes:OptimizeWaypoints](https://docs.aws.amazon.com/location/latest/APIReference/API_OptimizeWaypoints.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [geo-routes:SnapToRoads](https://docs.aws.amazon.com/location/latest/APIReference/API_SnapToRoads.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   UpdateMap  **
  - **IAM action:**  [geo:UpdateMap](#list_location-action-UpdateMap) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePlaceIndex  **
  - **IAM action:**  [geo:UpdatePlaceIndex](#list_location-action-UpdatePlaceIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRouteCalculator  **
  - **IAM action:**  [geo:UpdateRouteCalculator](#list_location-action-UpdateRouteCalculator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTracker  **
  - **IAM action:**  [geo:UpdateTracker](#list_location-action-UpdateTracker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VerifyDevicePosition  **
  - **IAM action:**  [geo:VerifyDevicePosition](#list_location-action-VerifyDevicePosition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon Location
<a name="list_location-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateTrackerConsumer](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_AssociateTrackerConsumer.html)  **
  - **Description:** Grants permission to create an association between a geofence-collection and a tracker resource
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Write

- **   [BatchDeleteDevicePositionHistory](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchDeleteDevicePositionHistory.html)  **
  - **Description:** Grants permission to delete a batch of device position histories from a tracker resource
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Write

- **   [BatchDeleteGeofence](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchDeleteGeofence.html)  **
  - **Description:** Grants permission to delete a batch of geofences from a geofence collection
  - **Resource types (\*required):** [geofence-collection\*](#list_location-resource-geofence-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Access level:** Write

- **   [BatchEvaluateGeofences](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchEvaluateGeofences.html)  **
  - **Description:** Grants permission to evaluate device positions against the position of geofences in a given geofence collection
  - **Resource types (\*required):** [geofence-collection\*](#list_location-resource-geofence-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Access level:** Write

- **   [BatchGetDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchGetDevicePosition.html)  **
  - **Description:** Grants permission to send a batch request to retrieve device positions
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Read

- **   [BatchPutGeofence](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchPutGeofence.html)  **
  - **Description:** Grants permission to send a batch request for adding geofences into a given geofence collection
  - **Resource types (\*required):** [geofence-collection\*](#list_location-resource-geofence-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Access level:** Write

- **   [BatchUpdateDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchUpdateDevicePosition.html)  **
  - **Description:** Grants permission to upload a position update for one or more devices to a tracker resource
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Write

- **   [CalculateRoute](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRoute.html)  **
  - **Description:** Grants permission to calculate routes using a given route calculator resource
  - **Resource types (\*required):** [route-calculator\*](#list_location-resource-route-calculator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CalculateRouteMatrix](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRouteMatrix.html)  **
  - **Description:** Grants permission to calculate a route matrix using a given route calculator resource
  - **Resource types (\*required):** [route-calculator\*](#list_location-resource-route-calculator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CancelJob](https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_CancelJob.html)  **
  - **Description:** Grants permission to cancel a job
  - **Resource types (\*required):** [job\*](#list_location-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGeofenceCollection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_CreateGeofenceCollection.html)  **
  - **Description:** Grants permission to create a geofence-collection
  - **Resource types (\*required):** [geofence-collection\*](#list_location-resource-geofence-collection)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Access level:** Write

- **   [CreateKey](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_CreateKey.html)  **
  - **Description:** Grants permission to create an API key resource
  - **Resource types (\*required):** [api-key\*](#list_location-resource-api-key)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMap](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateMap.html)  **
  - **Description:** Grants permission to create a map resource
  - **Resource types (\*required):** [map\*](#list_location-resource-map)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePlaceIndex](https://docs.aws.amazon.com/location/previous/APIReference/API_CreatePlaceIndex.html)  **
  - **Description:** Grants permission to create a place index resource
  - **Resource types (\*required):** [place-index\*](#list_location-resource-place-index)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateRouteCalculator.html)  **
  - **Description:** Grants permission to create a route calculator resource
  - **Resource types (\*required):** [route-calculator\*](#list_location-resource-route-calculator)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTracker](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_CreateTracker.html)  **
  - **Description:** Grants permission to create a tracker resource
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Write

- **   [DeleteGeofenceCollection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_DeleteGeofenceCollection.html)  **
  - **Description:** Grants permission to delete a geofence-collection
  - **Resource types (\*required):** [geofence-collection\*](#list_location-resource-geofence-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Access level:** Write

- **   [DeleteKey](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_DeleteKey.html)  **
  - **Description:** Grants permission to delete an API key resource
  - **Resource types (\*required):** [api-key\*](#list_location-resource-api-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMap](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteMap.html)  **
  - **Description:** Grants permission to delete a map resource
  - **Resource types (\*required):** [map\*](#list_location-resource-map)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePlaceIndex](https://docs.aws.amazon.com/location/previous/APIReference/API_DeletePlaceIndex.html)  **
  - **Description:** Grants permission to delete a place index resource
  - **Resource types (\*required):** [place-index\*](#list_location-resource-place-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteRouteCalculator.html)  **
  - **Description:** Grants permission to delete a route calculator resource
  - **Resource types (\*required):** [route-calculator\*](#list_location-resource-route-calculator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTracker](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DeleteTracker.html)  **
  - **Description:** Grants permission to delete a tracker resource
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Write

- **   [DescribeGeofenceCollection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_DescribeGeofenceCollection.html)  **
  - **Description:** Grants permission to retrieve geofence collection details
  - **Resource types (\*required):** [geofence-collection\*](#list_location-resource-geofence-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Access level:** Read

- **   [DescribeKey](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_DescribeKey.html)  **
  - **Description:** Grants permission to retrieve API key resource details and secret
  - **Resource types (\*required):** [api-key\*](#list_location-resource-api-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMap](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeMap.html)  **
  - **Description:** Grants permission to retrieve map resource details
  - **Resource types (\*required):** [map\*](#list_location-resource-map)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePlaceIndex](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribePlaceIndex.html)  **
  - **Description:** Grants permission to retrieve place-index resource details
  - **Resource types (\*required):** [place-index\*](#list_location-resource-place-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeRouteCalculator.html)  **
  - **Description:** Grants permission to retrieve route calculator resource details
  - **Resource types (\*required):** [route-calculator\*](#list_location-resource-route-calculator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTracker](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DescribeTracker.html)  **
  - **Description:** Grants permission to retrieve a tracker resource details
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Read

- **   [DisassociateTrackerConsumer](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DisassociateTrackerConsumer.html)  **
  - **Description:** Grants permission to remove the association between a tracker resource and a geofence-collection
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Write

- **   [ForecastGeofenceEvents](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ForecastGeofenceEvents.html)  **
  - **Description:** Grants permission to forecast events for geofences stored in a given geofence collection
  - **Resource types (\*required):** [geofence-collection\*](#list_location-resource-geofence-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Access level:** Read

- **   [GetDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_GetDevicePosition.html)  **
  - **Description:** Grants permission to retrieve the latest device position
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Read

- **   [GetDevicePositionHistory](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_GetDevicePositionHistory.html)  **
  - **Description:** Grants permission to retrieve the device position history
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Read

- **   [GetGeofence](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_GetGeofence.html)  **
  - **Description:** Grants permission to retrieve the geofence details from a geofence-collection
  - **Resource types (\*required):** [geofence-collection\*](#list_location-resource-geofence-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Access level:** Read

- **   [GetJob](https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_GetJob.html)  **
  - **Description:** Grants permission to retrieve job details
  - **Resource types (\*required):** [job\*](#list_location-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMapGlyphs](https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapGlyphs.html)  **
  - **Description:** Grants permission to retrieve the glyph file for a map resource
  - **Resource types (\*required):** [map\*](#list_location-resource-map)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMapSprites](https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapSprites.html)  **
  - **Description:** Grants permission to retrieve the sprite file for a map resource
  - **Resource types (\*required):** [map\*](#list_location-resource-map)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMapStyleDescriptor](https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapStyleDescriptor.html)  **
  - **Description:** Grants permission to retrieve the map style descriptor from a map resource
  - **Resource types (\*required):** [map\*](#list_location-resource-map)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMapTile](https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapTile.html)  **
  - **Description:** Grants permission to retrieve the map tile from the map resource
  - **Resource types (\*required):** [map\*](#list_location-resource-map)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPlace](https://docs.aws.amazon.com/location/previous/APIReference/API_GetPlace.html)  **
  - **Description:** Grants permission to find a place by its unique ID
  - **Resource types (\*required):** [place-index\*](#list_location-resource-place-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDevicePositions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListDevicePositions.html)  **
  - **Description:** Grants permission to retrieve a list of devices and their latest positions from the given tracker resource
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Read

- **   [ListGeofenceCollections](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ListGeofenceCollections.html)  **
  - **Description:** Grants permission to lists geofence-collections
  - **Resource types (\*required):** [geofence-collection\*](#list_location-resource-geofence-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Access level:** List

- **   [ListGeofences](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ListGeofences.html)  **
  - **Description:** Grants permission to list geofences stored in a given geofence collection
  - **Resource types (\*required):** [geofence-collection\*](#list_location-resource-geofence-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Access level:** Read

- **   [ListJobs](https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_ListJobs.html)  **
  - **Description:** Grants permission to list jobs
  - **Resource types (\*required):** [job\*](#list_location-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKeys](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_ListKeys.html)  **
  - **Description:** Grants permission to list API key resources
  - **Resource types (\*required):** [api-key\*](#list_location-resource-api-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMaps](https://docs.aws.amazon.com/location/previous/APIReference/API_ListMaps.html)  **
  - **Description:** Grants permission to list map resources
  - **Resource types (\*required):** [map\*](#list_location-resource-map)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPlaceIndexes](https://docs.aws.amazon.com/location/previous/APIReference/API_ListPlaceIndexes.html)  **
  - **Description:** Grants permission to return a list of place index resources
  - **Resource types (\*required):** [place-index\*](#list_location-resource-place-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRouteCalculators](https://docs.aws.amazon.com/location/previous/APIReference/API_ListRouteCalculators.html)  **
  - **Description:** Grants permission to return a list of route calculator resources
  - **Resource types (\*required):** [route-calculator\*](#list_location-resource-route-calculator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags (metadata) which you have assigned to the resource
  - **Resource types (\*required):** [api-key](#list_location-resource-api-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [geofence-collection](#list_location-resource-geofence-collection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Resource types (\*required):** [job](#list_location-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [map](#list_location-resource-map) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [place-index](#list_location-resource-place-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [route-calculator](#list_location-resource-route-calculator) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [tracker](#list_location-resource-tracker) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Read

- **   [ListTrackerConsumers](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListTrackerConsumers.html)  **
  - **Description:** Grants permission to retrieve a list of geofence collections currently associated to the given tracker resource
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Read

- **   [ListTrackers](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListTrackers.html)  **
  - **Description:** Grants permission to return a list of tracker resources
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** List

- **   [PutGeofence](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_PutGeofence.html)  **
  - **Description:** Grants permission to add a new geofence or update an existing geofence to a given geofence-collection
  - **Resource types (\*required):** [geofence-collection\*](#list_location-resource-geofence-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Access level:** Write

- **   [SearchPlaceIndexForPosition](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForPosition.html)  **
  - **Description:** Grants permission to reverse geocodes a given coordinate
  - **Resource types (\*required):** [place-index\*](#list_location-resource-place-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchPlaceIndexForSuggestions](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForSuggestions.html)  **
  - **Description:** Grants permission to generate suggestions for addresses and points of interest based on partial or misspelled free-form text
  - **Resource types (\*required):** [place-index\*](#list_location-resource-place-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchPlaceIndexForText](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForText.html)  **
  - **Description:** Grants permission to geocode free-form text, such as an address, name, city or region
  - **Resource types (\*required):** [place-index\*](#list_location-resource-place-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartJob](https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_StartJob.html)  **
  - **Description:** Grants permission to start a job
  - **Resource types (\*required):** [job\*](#list_location-resource-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_TagResource.html)  **
  - **Description:** Grants permission to adds to or modifies the tags of the given resource. Tags are metadata which can be used to manage a resource
  - **Resource types (\*required):** [api-key](#list_location-resource-api-key) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Resource types (\*required):** [geofence-collection](#list_location-resource-geofence-collection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Resource types (\*required):** [job](#list_location-resource-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Resource types (\*required):** [map](#list_location-resource-map) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Resource types (\*required):** [place-index](#list_location-resource-place-index) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Resource types (\*required):** [route-calculator](#list_location-resource-route-calculator) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Resource types (\*required):** [tracker](#list_location-resource-tracker) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_location-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_UntagResource.html)  **
  - **Description:** Grants permission to remove the given tags (metadata) from the resource
  - **Resource types (\*required):** [api-key](#list_location-resource-api-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Resource types (\*required):** [geofence-collection](#list_location-resource-geofence-collection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Resource types (\*required):** [job](#list_location-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Resource types (\*required):** [map](#list_location-resource-map) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Resource types (\*required):** [place-index](#list_location-resource-place-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Resource types (\*required):** [route-calculator](#list_location-resource-route-calculator) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)
  - **Resource types (\*required):** [tracker](#list_location-resource-tracker) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_location-aws_TagKeys)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Tagging, Write

- **   [UpdateGeofenceCollection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_UpdateGeofenceCollection.html)  **
  - **Description:** Grants permission to update a geofence collection
  - **Resource types (\*required):** [geofence-collection\*](#list_location-resource-geofence-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds)
  - **Access level:** Write

- **   [UpdateKey](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_UpdateKey.html)  **
  - **Description:** Grants permission to update an API key resource
  - **Resource types (\*required):** [api-key\*](#list_location-resource-api-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMap](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateMap.html)  **
  - **Description:** Grants permission to update a map resource
  - **Resource types (\*required):** [map\*](#list_location-resource-map)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePlaceIndex](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdatePlaceIndex.html)  **
  - **Description:** Grants permission to update a place index resource
  - **Resource types (\*required):** [place-index\*](#list_location-resource-place-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateRouteCalculator.html)  **
  - **Description:** Grants permission to update a route calculator resource
  - **Resource types (\*required):** [route-calculator\*](#list_location-resource-route-calculator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTracker](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_UpdateTracker.html)  **
  - **Description:** Grants permission to update a tracker resource
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Write

- **   [VerifyDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_VerifyDevicePosition.html)  **
  - **Description:** Grants permission to verify a device position
  - **Resource types (\*required):** [tracker\*](#list_location-resource-tracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds)
  - **Access level:** Read



## Resource types defined by Amazon Location
<a name="list_location-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [api-key](https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html)  | arn:${Partition}:geo:${Region}:${Account}:api-key/${KeyName} | [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_) | 
|  [geofence-collection](https://docs.aws.amazon.com/location/latest/developerguide/geofence-components.html)  | arn:${Partition}:geo:${Region}:${Account}:geofence-collection/${GeofenceCollectionName} | [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:GeofenceIds](#list_location-geo_GeofenceIds) | 
|  [job](https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html)  | arn:${Partition}:geo:${Region}:${Account}:job/${JobId} | [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_) | 
|  [map](https://docs.aws.amazon.com/location/previous/developerguide/map-concepts.html)  | arn:${Partition}:geo:${Region}:${Account}:map/${MapName} | [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_) | 
|  [place-index](https://docs.aws.amazon.com/location/previous/developerguide/places-concepts.html)  | arn:${Partition}:geo:${Region}:${Account}:place-index/${IndexName} | [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_) | 
|  [route-calculator](https://docs.aws.amazon.com/location/previous/developerguide/route-concepts.html)  | arn:${Partition}:geo:${Region}:${Account}:route-calculator/${CalculatorName} | [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_) | 
|  [tracker](https://docs.aws.amazon.com/location/latest/developerguide/tracking-components.html)  | arn:${Partition}:geo:${Region}:${Account}:tracker/${TrackerName} | [aws:ResourceTag/${TagKey}](#list_location-aws_ResourceTag___TagKey_)<br />[geo:DeviceIds](#list_location-geo_DeviceIds) | 

## Condition keys for Amazon Location
<a name="list_location-policy-keys"></a>

Amazon Location defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag's key and value in a request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in a request | ArrayOfString | 
|   [geo:DeviceIds](https://docs.aws.amazon.com/location/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the presence of device ids in the request | ArrayOfString | 
|   [geo:GeofenceIds](https://docs.aws.amazon.com/location/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the presence of geofence ids in the request | ArrayOfString | 