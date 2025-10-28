# Amazon Location Service in AWS GovCloud (US)

This service is currently available in AWS GovCloud (US-West) only, because Amazon Cognito is not available
in AWS GovCloud (US-East).

Amazon Location Service lets you securely add location data to your application.
Amazon Location provides access to location-based functionality and data providers through AWS
resources. Amazon Location offers five types of AWS resources, depending on the type of
functionality you need. Use the different resources together to create a full location-based
application.

## How Amazon Location Service differs for

AWS GovCloud (US)

- [Granting
  access to resources using API keys](../../../location/latest/developerguide/using-apikeys.md "../../../location/latest/developerguide/using-apikeys.md") is not supported.

## Documentation for Amazon Location Service

[Amazon Location
documentation](../../../location/index.md "../../../location/index.md").

## Export-controlled content

For AWS services architected within the AWS GovCloud (US) Regions, the following list explains which components of
data may leave or remain within the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide
to help meet applicable customer compliance obligations.

- When you use the following [geolocation data providers](https://aws.amazon.com/location/data-providers/ "https://aws.amazon.com/location/data-providers/"), you transmit request
  parameters (such as location searches) from Amazon Location features (Maps, Places,
  and Routes) to the geolocation provider for processing, which may be outside of
  the AWS Region in which your request was made.
  - Esri
  - Here
  - GrabMaps

- The exception is requests to the Open Data geolocation provider, which are
  processed by AWS in the AWS Region in which your request was made.
- Request parameters transmitted by using Amazon Location features Trackers and
  Geofences are processed by AWS in the AWS Region in which your request was
  made.
