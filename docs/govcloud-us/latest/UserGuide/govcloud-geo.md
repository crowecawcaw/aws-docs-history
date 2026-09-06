

# Amazon Location Service in AWS GovCloud (US)
<a name="govcloud-geo"></a>

Amazon Location Service lets you securely add location data to your application. Amazon Location provides access to location-based functionality and data providers through AWS resources. Amazon Location offers five types of AWS resources, depending on the type of functionality you need. Use the different resources together to create a full location-based application.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 

## How Amazon Location Service differs
<a name="govcloud-diffs-7"></a>

The following differences apply to Amazon Location Service:
+  [Granting access to resources using API keys](https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html) is not available.

## Documentation
<a name="govcloud-docs-46"></a>
+  [Amazon Location documentation](https://docs.aws.amazon.com/location/index.html) 

## Export-controlled content
<a name="govcloud-itar-content-85"></a>

For AWS services architected within the AWS GovCloud (US) Regions, the following list explains which components of data may leave or remain within the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations.
+ When you use the following [geolocation data providers](https://aws.amazon.com/location/data-providers/), you transmit request parameters (such as location searches) from Amazon Location features (Maps, Places, and Routes) to the geolocation provider for processing, which may be outside of the AWS Region in which your request was made.
  + Esri
  + Here
  + GrabMaps
+ The exception is requests to the Open Data geolocation provider, which are processed by AWS in the AWS Region in which your request was made.
+ Request parameters transmitted by using Amazon Location features Trackers and Geofences are processed by AWS in the AWS Region in which your request was made.