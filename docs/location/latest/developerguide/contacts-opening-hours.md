

# Contacts and opening hours
<a name="contacts-opening-hours"></a>

Amazon Location Service provides details on contacts and opening hours for various points of interest (POIs), enabling applications to offer comprehensive information about business operations. This section covers contact and business hours information and how to retrieve and interpret these details effectively.

Amazon Location Service can provide structured data on the contact details and business hours of points of interest (POIs), enabling applications to display accurate information. This data is valuable for applications where real-time availability or business operations influence customer experience.


| Filter Type | Geocode | Reverse Geocode | Autocomplete | Get Place | Search Text | Search Nearby | Suggest | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Contacts | No | No | No | Yes | Yes | Yes | No | 
| Opening Hours | No | No | No | Yes | Yes | Yes | No | 

## Contact details
<a name="contact-details"></a>

Contact details for a place include structured information such as phone numbers, email addresses, and websites. These details are available for businesses listed in place data.

**Phone number**  
The primary contact number for a business. This field may include international dialing codes to ensure accurate connection, regardless of the caller’s location.

**Email address**  
The primary contact email for inquiries. It may be available for businesses that provide an email address in their public listing.

**Website**  
A link to the official website, providing users with additional information or access to services such as online booking or support.

## Opening hours
<a name="opening-hours"></a>

Opening hours indicate the regular business hours for a location, providing users with insights into availability. This information is crucial for applications where users need to know when a business is open or closed.

**Regular hours**  
The standard weekly opening hours, typically provided as daily ranges (e.g., Monday to Friday, 9 AM to 5 PM). These indicate the usual operating schedule.

**Special hours**  
Exceptional hours for holidays or special events, provided as overrides to regular hours. For example, holiday hours or closures can be indicated to inform users of temporary changes in schedule.

**Open now**  
An indicator of whether a location is currently open, based on the local time. This information is helpful for users looking for businesses that are open at the time of their query.

For more information about contact details and opening hours for points of interest, see the Amazon Location Service [OpeningHours API reference](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_OpeningHours.html).