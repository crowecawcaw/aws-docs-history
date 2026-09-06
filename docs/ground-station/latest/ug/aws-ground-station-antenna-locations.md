

# AWS Ground Station Locations
<a name="aws-ground-station-antenna-locations"></a>

 AWS Ground Station provides a global network of ground stations in close proximity to our global network of AWS infrastructure regions. You can configure your use of these locations from any supported AWS Region. This includes the AWS Region in which data is delivered. 

 ![Map showing shared locations with antenna and data delivery regions marked.](http://docs.aws.amazon.com/ground-station/latest/ug/images/antenna-locations.png) 

## Finding the AWS region for a ground station location
<a name="aws-ground-station-antenna-locations.antenna-regions"></a>

 The AWS Ground Station global network includes ground station locations that are not physically located in the [AWS Region ](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) to which they are connected. The list of ground stations that you have access to can be retrieved via the AWS SDK [ ListGroundStation ](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListGroundStations.html) response. As of June 16, 2026, AWS Ground Station no longer supports antenna resources in Seoul. The full list of ground station locations is presented below. Please refer to the onboarding guide to add or modify site approvals for your satellites. 



| Ground Station Name | Ground Station Location | AWS Region Name | AWS Region Code | Notes | 
| --- | --- | --- | --- | --- | 
| Alaska 1 | Alaska, USA | US West (Oregon) | us-west-2 | Not physically located in an AWS region | 
| Bahrain 1 | Bahrain | Middle East (Bahrain) | me-south-1 |  | 
| Cape Town 1 | Cape Town, South Africa | Africa (Cape Town) | af-south-1 |  | 
| Dubbo 1 | Dubbo, Australia | Asia Pacific (Sydney) | ap-southeast-2 | Not physically located in an AWS region | 
| Hawaii 1 | Hawaii, USA | US West (Oregon) | us-west-2 | Not physically located in an AWS region | 
| Ireland 1 | Ireland | Europe (Ireland) | eu-west-1 |  | 
| Ohio 1 | Ohio, USA | US East (Ohio) | us-east-2 |  | 
| Oregon 1 | Oregon, USA | US West (Oregon) | us-west-2 |  | 
| Punta Arenas 1 | Punta Arenas, Chile | South America (São Paulo) | sa-east-1 | Not physically located in an AWS region | 
| Singapore 1 | Singapore | Asia Pacific (Singapore) | ap-southeast-1 |  | 
| Stockholm 1 | Stockholm, Sweden | Europe (Stockholm) | eu-north-1 |  | 

## AWS Ground Station supported AWS regions
<a name="aws-ground-station-service-regions"></a>

 You can deliver data and configure your **Contacts** via the AWS SDK or the AWS Ground Station console from supported AWS Regions. You can view the supported regions and their associated endpoints at the [AWS Ground Station endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/gs.html). 

## Digital twin availability
<a name="aws-ground-station-digital-twin-service-regions"></a>

 [Use the AWS Ground Station digital twin feature](digital-twin.md) is available in all [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) where AWS Ground Station is available. Digital twin ground stations are exact copies of production ground stations with a modifying prefix to Ground Station Name of “Digital Twin ”. For example, "Digital Twin Ohio 1" is a digital twin ground station that is an exact copy of the "Ohio 1" production ground station. 

## Dedicated Antennas
<a name="aws-ground-station-dedicated-antenna"></a>

 In addition to the publicly available ground station locations listed above, AWS Ground Station offers Dedicated Antennas. A Dedicated Antenna is a custom-built antenna system that AWS manages on your behalf. A Dedicated Antenna is not restricted to existing AWS Ground Station ground station locations and can be built with capabilities beyond those of public ground stations as described in [AWS Ground Station Site Capabilities](locations.capabilities.md). The locations and capabilities of Dedicated Antennas are not publicly disclosed. 

 For more information about Dedicated Antennas, see [AWS Ground Station Dedicated Antennas](dedicated-antennas.md). To learn more or to get started with Dedicated Antennas, contact AWS Support through the [AWS Support Center Console](https://console.aws.amazon.com/support). 

## Viewing antennas at a ground station
<a name="aws-ground-station-antennas"></a>

 Each ground station location has one or more antennas. You can view the antennas at a ground station by using the [ListAntennas](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListAntennas.html) API. This API returns the antennas at a specified ground station, including each antenna's name. 

 Antenna information is useful when combined with the [ListGroundStationReservations](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListGroundStationReservations.html) API to understand capacity and availability at a ground station. For more information about viewing reservations, see [View ground station reservations](locations.reservations.md). 

 To call `ListAntennas`, you must have a satellite onboarded to the ground station or have azimuth elevation ephemeris permissions for the ground station. For more information, see [Provide azimuth elevation ephemeris data](providing-azimuth-elevation-ephemeris-data.md). 

### Example: List antennas at a ground station
<a name="aws-ground-station-antennas.example"></a>

 The following example lists all antennas at a ground station using the AWS SDK for Python (Boto3). 

```
import boto3

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

# The ground station ID to list antennas for.
# Use the ListGroundStations API to find available ground station IDs.
ground_station_id = "Ohio 1"

# List all antennas at a ground station.
# This is useful for understanding the capacity of a ground station
# and for planning multi-antenna operations.
print(f"Listing antennas for ground station '{ground_station_id}'...")

paginator = ground_station_client.get_paginator("list_antennas")
page_iterator = paginator.paginate(
    groundStationId=ground_station_id,
    PaginationConfig={
        "MaxItems": 100,
        "PageSize": 20,
    },
)

for page in page_iterator:
    for antenna in page["antennaList"]:
        print(f"  Antenna: {antenna['antennaName']}")
        print(f"    Ground Station: {antenna['groundStationName']}")
        print(f"    Region: {antenna['region']}")
        print()
```