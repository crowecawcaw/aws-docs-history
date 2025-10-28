# Connect to managed integrations for AWS IoT Device Management FIPS endpoints

AWS IoT provides a control plane endpoint that support the [Federal Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/"). FIPS
compliant endpoints are different from standard AWS endpoints. To interact with managed integrations for AWS IoT Device Management
in a FIPS-compliant manner, you must use the endpoints described below with your FIPS
compliant client. The AWS IoT console is not FIPS compliant.

The following sections describe how to access the FIPS compliant AWS IoT endpoint by
using the REST API, an SDK, or the AWS CLI.

## Control plane endpoints

The FIPS compliant **control plane** endpoints
that support the managed integrations
operations and their related AWS CLI commands are listed in [FIPS
Endpoints by Service](https://aws.amazon.com/compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com/compliance/fips/#FIPS_Endpoints_by_Service"). In [FIPS
Endpoints by Service](https://aws.amazon.com/compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com/compliance/fips/#FIPS_Endpoints_by_Service"), find the **AWS IoT Device Management - Managed integrations** service, and look up the endpoint for your
AWS Region.

To use the FIPS compliant endpoint when you access themanaged integrations
operations, use the AWS SDK or the REST API with the endpoint that is appropriate
for your AWS Region.

To use the FIPS compliant endpoint when you run managed integrations CLI commands, add the
**--endpoint** parameter with the appropriate endpoint for your
AWS Region to the command.
