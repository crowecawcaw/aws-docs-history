# Fleet Management Dashboard

The web-based dashboard provides comprehensive fleet management capabilities with real-time data visualization.

**Dashboard Features**:

- **Real-time Map**: Live vehicle locations updated every 5 seconds from Redis cache
- **Fleet Overview**: Summary statistics and KPIs aggregated from DynamoDB
- **Vehicle Details**: Individual vehicle history and diagnostics
- **Driver Management**: Assign drivers and track performance
- **Alerts and Notifications**: Safety events and maintenance alerts

**Scalability**:

**Amazon Location Services Integration**:

The dashboard uses Amazon Location Services for interactive map visualization and geospatial features:

- **Vector Map Rendering**: Esri Streets vector map (VectorEsriStreets style) rendered via MapLibre GL JS
- **Real-Time Vehicle Tracking**: Vehicle markers updated every 5 seconds with smooth position interpolation
- **Place Search**: Esri-powered place index (cms-place-index) for address search and geocoding
- **Reverse Geocoding**: Convert GPS coordinates to human-readable addresses for trip start/end locations
- **Route Visualization**: Display historical trip routes as polylines on the map with color-coded segments
- **Geofencing**: Define geographic boundaries for fleet zones, service areas, and restricted regions
- **Heatmaps**: Visualize vehicle density, safety events, and maintenance alerts by geographic area
- **Cognito Integration**: Unauthenticated and authenticated IAM roles grant map access via geo:GetMap\* and geo:SearchPlaceIndex\* permissions
  The map component uses MapLibre GL JS with Amazon Location Utilities Auth Helper and Cognito credentials to securely access Location Services resources without exposing API keys in the frontend code.

- **CloudFront CDN**: Global edge caching for sub-100ms page loads
- **S3 Static Hosting**: Unlimited scalability for static assets
- **API Caching**: Redis cache reduces DynamoDB queries by 90%

**Extensibility**:

- **Custom Widgets**: Add custom visualizations and analytics
- **Third-Party Integration**: Embed maps from Mapbox, Google Maps, or HERE
- **Mobile Apps**: Reuse APIs for iOS and Android mobile applications
