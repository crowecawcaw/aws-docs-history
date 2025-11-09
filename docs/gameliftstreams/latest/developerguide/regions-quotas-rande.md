# AWS Regions and remote locations supported by

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

## Remote locations

Amazon GameLift Streams can extend coverage to remote locations, enabling you to host your
application and stream sessions in more locations. The remote locations available to you
depend on your primary location. We recommend that you choose locations that are
geographically close to your users to optimize latency and stream quality.

| Primary location                        | Remote locations                                                                                                                                                                                    |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (Ohio) – `us-east-2`            | • US East (N. Virginia) – `us-east-1`<br>• US West (Oregon) – `us-west-2`<br>• Europe (Ireland) – `eu-west-1`<br>• Europe (Frankfurt) – `eu-central-1`<br>• Asia Pacific (Tokyo) – `ap-northeast-1` |
| US West (Oregon) – `us-west-2`          | • US East (N. Virginia) – `us-east-1`<br>• US East (Ohio) – `us-east-2`<br>• Europe (Ireland) – `eu-west-1`<br>• Europe (Frankfurt) – `eu-central-1`<br>• Asia Pacific (Tokyo) – `ap-northeast-1`   |
| Asia Pacific (Tokyo) – `ap-northeast-1` | • US East (N. Virginia) – `us-east-1`<br>• US West (Oregon) – `us-west-2`<br>• US East (Ohio) – `us-east-2`<br>• Europe (Ireland) – `eu-west-1`<br>• Europe (Frankfurt) – `eu-central-1`            |
| Europe (Frankfurt) – `eu-central-1`     | • US East (N. Virginia) –<br>`us-east-1`<br>• US West (Oregon) – `us-west-2`<br>• US East (Ohio) – `us-east-2`<br>• Europe (Ireland) – `eu-west-1`<br>• Asia Pacific (Tokyo) – `ap-northeast-1`     |
