

# Navigation
<a name="maps-navigation-map"></a>

The navigation features such as `Traffic` and `Truck TravelModes` provide dynamic visualization tools that enhance navigation and route planning. They help users understand real-time road conditions and choose the most efficient travel options based on their transportation needs.

## Traffic
<a name="maps-navigation-traffic"></a>

The traffic layer provides real-time visualization of traffic conditions, including road congestion, construction zones, and reported incidents. This feature helps users make informed routing decisions and optimize travel efficiency based on current roadway conditions.

Use the `traffic` parameter in your API request to display real-time traffic information. This includes data on road congestion, construction areas, and incidents, helping users make informed and efficient routing decisions. See [how to show real-time traffic on a map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-set-real-time-traffic-map.html).

------
#### [ All ]

![](http://docs.aws.amazon.com/location/latest/developerguide/images/zoom-traffic-all.gif)


------
#### [ Congestion ]

![](http://docs.aws.amazon.com/location/latest/developerguide/images/zoom-traffic-congestion.gif)


------

## Travel modes
<a name="maps-navigation-travel-modes"></a>

The travel modes feature enables visualization and selection of different transportation methods. It supports routing information for various modes such as public transit, trucking, or other specialized navigation types that consider road restrictions and regulations. This helps users plan routes optimized for their specific mode of travel.

Use the `travel-modes` parameter in your API request to show transportation-specific routing data. See [how to show transit details on a map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-show-transit-details-map.html) and [how to create a logistics map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-create-logistic-map.html).

![](http://docs.aws.amazon.com/location/latest/developerguide/images/map-travel-modes-transit.gif)


![](http://docs.aws.amazon.com/location/latest/developerguide/images/map-travel-modes-truck.gif)
