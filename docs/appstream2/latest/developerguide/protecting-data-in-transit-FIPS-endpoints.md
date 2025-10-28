# Protecting Data in Transit with FIPS Endpoints

By default, when you communicate with the AppStream 2.0 service, whether as an administrator using the AppStream 2.0 console, the AWS Command Line Interface (AWS CLI), or an AWS SDK, or as a user streaming from an image builder or a fleet instance, all data in transit is encrypted using TLS 1.2.

If you require FIPS 140-2 validated cryptographic modules when accessing AWS through
a command line interface or an API, use a FIPS endpoint. AppStream 2.0 offers FIPS endpoints in all United
States AWS Regions where AppStream 2.0 is available. When you use a FIPS endpoint, all data in
transit is encrypted using cryptographic standards that comply with Federal Information
Processing Standard (FIPS) 140-2. For information about FIPS endpoints, including a list
of AppStream 2.0 endpoints, see [Federal Information Processing
Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips "https://aws.amazon.com/compliance/fips").

###### Topics

- [FIPS Endpoints for Administrative Use](FIPS-for-administrative-use.md "FIPS-for-administrative-use.md")
- [FIPS Endpoints for User Streaming Sessions](FIPS-for-user-streaming-sessions.md "FIPS-for-user-streaming-sessions.md")
- [Exceptions](FIPS-exceptions.md "FIPS-exceptions.md")
