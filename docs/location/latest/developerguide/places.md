

# Amazon Location Service Places
<a name="places"></a>

![An overview of Amazon Location Service Places.](http://docs.aws.amazon.com/location/latest/developerguide/images/illustration-places.PNG)


With Amazon Location Places, you can add location-based capabilities to your application. Using Places APIs, you can search or geocode locations by querying a comprehensive place database containing over 400 million addresses and points of interest (POIs) across 108 countries.

## What is a Place?
<a name="place-definition"></a>

A place refers to any specific location, including administrative areas, addresses, POIs, geographic areas, and more. Places have various associated information such as name, address, coordinates, type, and details like business hours, contacts, access points, and POI categories.
+ **Address:** Includes specific point addresses (like offices, homes, apartments), street addresses, and interpolated addresses.
+ **Points of Interest (POI):** Includes businesses (like restaurants, stores) and landmarks (like parks, monuments).
+ **Administrative Areas:** Includes regions like countries, states, provinces, districts, and postal areas.
+ **Geographic Areas:** Includes locations like cities, neighborhoods, and localities.

## Features
<a name="features"></a>

Search APIs enable users to discover places, points of interest (POIs), and addresses by querying based on names, categories, or locations.
+ **Geocode APIs:** Convert physical locations or addresses into geographic coordinates (longitude and latitude).
+ **Intended use:** Places APIs allow users to retrieve and utilize location data for various applications, from one-time uses to storing data for future reference. By default, data is retrieved for single-use, but options are available to store data persistently for analysis or further use.

## Use cases
<a name="use-cases"></a>

**Enhance your checkout experience**  
Provide real-time suggestions for valid street addresses as customers enter their location on websites or apps. This helps ensure accurate delivery or pickup locations, reducing errors and creating a seamless checkout experience. Enhance cart completion rates by validating addresses to improve user satisfaction and drive conversions.  
*For more information, refer to the related APIs:* Autocomplete and Suggest.

**Discover local places**  
Assist customers in finding the nearest, most relevant places. Real estate clients, for example, can locate nearby schools, grocery stores, and parks. Build lists of target businesses to market services and gain insights by searching by category and retrieving essential information like addresses and geocodes.  
*For more information, refer to the related APIs:* SearchNearby and SearchText.

**Provide customers with up-to-date business details**  
Deliver the latest information on local businesses. Enable users to search by business name or category within a specific area, enhancing customer experience and supporting business decision-making. For example, help gym members locate health food stores nearby, or ensure delivery drivers arrive during open hours.  
*For more information, refer to the related APIs:* SearchNearby, SearchText, Suggest, and GetPlace.

**Enrich customer addresses with detailed insights**  
Enhance existing customer address data with additional insights like postal codes, geo-coordinates, contact details, and business categories. Use the perpetual storage option to save this data in your database for strategic use in marketing and decision-making.  
*For more information, refer to the related APIs:* Geocode, Reverse Geocode, SearchText, and SearchNearby.

**Find geospatial coordinates of addresses to calculate routes and driving directions**  
Convert addresses or business names into geospatial coordinates and calculate optimal routes for tasks like food delivery or rideshare services. Use waypoint sequencing to create efficient paths for multiple stops.  
*For more information, refer to the related APIs:* Suggest and SearchText.

**Identify time zones for locations**  
Determine the correct time zone for specific locations (city, address, coordinates, or place ID). This feature is ideal for travel applications that require accurate time zones for itineraries and scheduling applications. Ensure that billing and compliance records use the appropriate timestamps.  
*For more information, refer to the related APIs:* Geocode, Reverse Geocode, SearchText, and GetPlace.

## Places APIs overview
<a name="places-api-table"></a>


| API name | Description | Additional resources | 
| --- | --- | --- | 
| Autocomplete | Autocomplete completes potential search places or addresses as the user types, based on the partial input. Autocomplete is not available in Japan. | [Autocomplete](autocomplete.md) | 
| Geocode | Geocode or forward geocode is converting a textual address or place into geographic coordinates. | [Geocode](geocode.md) | 
| Reverse Geocode | Reverse geocode is converting geographic coordinates into a human-readable address or place. | [Reverse Geocode](reverse-geocode.md) | 
| GetPlace | Get Place retrieves detailed information about a specific place, such as its address, opening hours, contacts, and other metadata. | [GetPlace](get-place.md) | 
| Suggest | Suggest provides intelligent predictions or recommendations based on the user’s input or context, such as relevant places, points of interest or query term | [Suggest](suggest.md) | 
| Search Text | Search Text provides an ability to search for places, addresses or point of interest using textual input, and it returns information such as a place name, address, phone, category, food type, contact, opening hours. | [Search Text](search-text.md) | 
| Search Nearby | Search nearby provides an ability to search for points of interest within a specified radius or distance from a geographic coordinates. | [Search Nearby](search-nearby.md) | 