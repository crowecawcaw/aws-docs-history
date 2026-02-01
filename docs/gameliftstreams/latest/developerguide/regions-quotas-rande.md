# AWS Regions and streaming locations supported by

Amazon GameLift Streams

An AWS Region is a collection of AWS resources in a geographic area. Each
AWS Region is isolated and independent of the other Regions. For general information
about AWS Regions, see [Managing AWS Regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md") in the
_AWS General Reference_.

The following table lists the AWS Regions where the Amazon GameLift Streams service is available and
the endpoints for each Region. You create all Amazon GameLift Streams application and stream group
resources in a specified Region, whether you work in the Amazon GameLift Streams console, use the AWS Command Line Interface
(AWS CLI), or make programmatic calls. The Region where you create these resources is known
as the _primary location_. Use your primary location's endpoint to
connect to the Amazon GameLift Streams service programmatically.

## Service endpoints

Amazon GameLift Streams supports dual-stack service endpoints, allowing clients and resources to
interact with the service using IPv6 or IPv4.

| Region Name          | Region         | Endpoint                               | Protocol |
| -------------------- | -------------- | -------------------------------------- | -------- |
| US East (Ohio)       | us-east-2      | gameliftstreams.us-east-2.api.aws      | HTTPS    |
| US West (Oregon)     | us-west-2      | gameliftstreams.us-west-2.api.aws      | HTTPS    |
| Asia Pacific (Tokyo) | ap-northeast-1 | gameliftstreams.ap-northeast-1.api.aws | HTTPS    |
| Europe (Frankfurt)   | eu-central-1   | gameliftstreams.eu-central-1.api.aws   | HTTPS    |

## Streaming locations

Amazon GameLift Streams supports streaming from all the following locations from any of the service endpoints. We
recommend that you choose streaming locations that are geographically close to your users to
optimize latency and stream quality.

| Region name               | AWS Region     |
| ------------------------- | -------------- |
| US East (N. Virginia)     | us-east-1      |
| US East (Ohio)            | us-east-2      |
| US West (Oregon)          | us-west-2      |
| Asia Pacific (Mumbai)     | ap-south-1     |
| Asia Pacific (Seoul)      | ap-northeast-2 |
| Asia Pacific (Sydney)     | ap-southeast-2 |
| Asia Pacific (Tokyo)      | ap-northeast-1 |
| Europe (Frankfurt)        | eu-central-1   |
| Europe (Ireland)          | eu-west-1      |
| Europe (London)           | eu-west-2      |
| Europe (Stockholm)        | eu-north-1     |
| South America (São Paulo) | sa-east-1      |
