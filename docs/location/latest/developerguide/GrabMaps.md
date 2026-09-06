

# GrabMaps for Southeast Asia
<a name="GrabMaps"></a>

 Grab is the leading superapp in Southeast Asia with the largest delivery and ride-hailing organization in the region. Their subsidiary, [GrabMaps](https://grabmaps.grab.com/), curates up-to-date and locally relevant data for Maps, Places, and Routing APIs across Southeast Asian markets, for their own use, and others. GrabMaps' location services are built to provide high-quality, authoritative, and ready-to-use location data, specifically for Southeast Asian countries. 

## Enhanced accuracy with GrabMaps data
<a name="grabmaps-enhanced-accuracy"></a>

 GrabMaps delivers hyperlocal mapping intelligence specifically built for Southeast Asia's unique geography and navigation challenges. GrabMaps' data is continuously validated through millions of journeys, capturing real-time feedback on road closures, address changes, and traffic conditions. This includes detailed coverage of back alleys, narrow side streets, and motorcycle-accessible routes that conventional maps often miss but are essential for navigation in Southeast Asian cities. Designed with a Southeast Asia-first mindset, GrabMaps also offers tailored maps for local transportation like motorcycles. Its local operations team, consisting of over 1,000 members and 200\+ specialists, ensures maps are accurate and detailed for each region. Features include local language search, traffic congestion models, and rich map displays. By respecting the differences between each country and learning from locals, GrabMaps provides an authentic and familiar experience. GrabMaps' comprehensive points of interest database and optimized routing reflect local road conditions, up-to-date locations that keep pace with constant urban change, and regional navigation preferences, enabling you to build applications that provide reliable location-based services for the region. 

## How to use GrabMaps data
<a name="grabmaps-supported-regions"></a>

 To use GrabMaps location services, simply use an Amazon Location Service endpoint in one of these Southeast Asian regions: 
+ Asia Pacific (Singapore): `ap-southeast-1`
+ Asia Pacific (Malaysia): `ap-southeast-5`

 You can find the endpoints for these regions [here](https://docs.aws.amazon.com/general/latest/gr/location.html). 

## GrabMaps data coverage
<a name="grabmaps-data-coverage"></a>

 GrabMaps provides detailed geospatial data across over 500 cities in the following countries: 
+ Malaysia
+ Philippines
+ Thailand
+ Singapore
+ Vietnam
+ Indonesia
+ Myanmar
+ Cambodia

## Supported Operations with GrabMaps
<a name="grabmaps-supported-operations"></a>

 The following operations using GrabMaps data are supported in the latest version of the Amazon Location Service APIs: 
+ Maps:
  + GetTile
  + GetStyleDescriptor
+ Places:
  + ReverseGeocode
  + Suggest
  + SearchText
  + GetPlace
  + SearchNearby
+ Routes:
  + CalculateRoutes
  + CalculateRouteMatrix

**Note**  
 Operations using GrabMaps data may have different supported request fields and available response fields compared to data providers used in all other regions. For detailed information about field availability and regional differences, see the [API Reference](https://docs.aws.amazon.com/location/latest/APIReference/API_Operations.html). 