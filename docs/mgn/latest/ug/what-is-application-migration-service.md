NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# What Is AWS Application Migration Service?

AWS Application Migration Service (MGN) is a highly automated lift-and-shift (rehost)
solution that simplifies, expedites, and reduces the cost of migrating applications to AWS. It
allows companies to lift-and-shift a large number of physical, virtual, or cloud servers without
compatibility issues, performance disruption, or long cutover windows. Application Migration Service replicates source
servers into your AWS account. When you’re ready, it automatically converts and launches your
servers on AWS so you can quickly benefit from the cost savings, productivity, resilience, and
agility of the cloud. Once your applications are running on AWS, you can leverage AWS services and
capabilities to quickly and easily replatform or refactor those applications – which makes
lift-and-shift a fast route to modernization.

## Accessing the AWS Application Migration Service console

You can access AWS Application Migration Service through the AWS Console or through the
following link:

[[https://console.aws.amazon.com/mgn/home](https://console.aws.amazon.com/mgn/home "https://console.aws.amazon.com/mgn/home")](https://console.aws.amazon.com/mgn/home "https://console.aws.amazon.com/mgn/home")

## Supported AWS Regions

The following AWS Regions are supported by AWS Application Migration Service:

| Region name               | Region identity | Support in AWS Application Migration Service |
| ------------------------- | --------------- | -------------------------------------------- |
| US East (Ohio)            | us-east-2       | Yes                                          |
| US East (N. Virginia)     | us-east-1       | Yes                                          |
| US West (N. California)   | us-west-1       | Yes                                          |
| US West (Oregon)          | us-west-2       | Yes                                          |
| Africa (Cape Town)        | af-south-1      | Yes                                          |
| Asia Pacific (Hong Kong)  | ap-east-1       | Yes                                          |
| Asia Pacific (Thailand)   | ap-southeast-7  | Yes                                          |
| Asia Pacific (Jakarta)    | ap-southeast-3  | Yes                                          |
| Asia Pacific (Malaysia)   | ap-southeast-5  | Yes                                          |
| Asia Pacific (Melbourne)  | ap-southeast-4  | Yes                                          |
| Asia Pacific (Mumbai)     | ap-south-1      | Yes                                          |
| Asia Pacific (Hyderabad)  | ap-south-2      | Yes                                          |
| Asia Pacific (Osaka)      | ap-northeast-3  | Yes                                          |
| Asia Pacific (Seoul)      | ap-northeast-2  | Yes                                          |
| Asia Pacific (Singapore)  | ap-southeast-1  | Yes                                          |
| Asia Pacific (Sydney)     | ap-southeast-2  | Yes                                          |
| Asia Pacific (Tokyo)      | ap-northeast-1  | Yes                                          |
| Canada (Central)          | ca-central-1    | Yes                                          |
| Europe (Frankfurt)        | eu-central-1    | Yes                                          |
| Europe (Zurich)           | eu-central-2    | Yes                                          |
| Europe (Ireland)          | eu-west-1       | Yes                                          |
| Europe (London)           | eu-west-2       | Yes                                          |
| Europe (Paris)            | eu-west-3       | Yes                                          |
| Europe (Milan)            | eu-south-1      | Yes                                          |
| Europe (Spain)            | eu-south-2      | Yes                                          |
| Europe (Stockholm)        | eu-north-1      | Yes                                          |
| Israel (Tel Aviv)         | il-central-1    | Yes                                          |
| Middle East (Bahrain)     | me-south-1      | Yes                                          |
| Middle East (UAE)         | me-central-1    | Yes                                          |
| South America (São Paulo) | sa-east-1       | Yes                                          |
| AWS GovCloud (US-East)    | us-gov-east-1   | Yes                                          |
| AWS GovCloud (US-West)    | us-gov-west-1   | Yes                                          |

Learn more about [AWS
Regional services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

AWS Application Migration Service regional support includes [AWS Local Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-local-zones "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-local-zones") associated with the above supported regions.

## Using the AWS Migration Hub with AWS MGN

AWS Application Migration Service works with the AWS Migration Hub (MGH), allowing you to
organize your servers into applications and then to track the progress of all your MGN at the
server and app level, even as you move servers into multiple AWS Regions.

You must choose a Migration Hub Home Region for AWS MGN to work with the Migration Hub. [Learn more about choosing a Migration Hub Home Region.](../../../migrationhub/latest/ug/home-region.md#select-home-region "../../../migrationhub/latest/ug/home-region.md#select-home-region")

You can access the AWS Migration Hub from the AWS MGN navigation menu.

AWS Application Migration Service supports auto tagging in MGH. Migrated resources (Amazon EC2
instances or Amazon Machine Images (AMIs)) reported to Migration Hub by AWS MGN are automatically
tagged with Application Discovery Service server IDs. If you turn on cost allocation tagging, you
can view the cost of the AWS resources that are tagged by Migration Hub in the AWS Cost Explorer
Service. Resource tagging by Migration Hub can’t be turned off. This tagging is implemented
automatically and doesn't count against your limit of 50 tags per resource. Learn more about
tagging migration resources in the [Migration Hub documentation](../../../en_us/migrationhub/latest/ug/doing-more.md#tagging-migration-resources "../../../en_us/migrationhub/latest/ug/doing-more.md#tagging-migration-resources").

## MGN technical training materials

The following technical trainings are available for AWS MGN:

- [AWS Application Migration Service - A Technical Introduction](https://www.aws.training/Details/eLearning?id=71732 "https://www.aws.training/Details/eLearning?id=71732")
- [Blog posts related to AWS MGN](https://aws.amazon.com/application-migration-service/resources/#Blog_posts_.26_articles "https://aws.amazon.com/application-migration-service/resources/#Blog_posts_.26_articles")
- [AWS MGN video playlist](https://www.youtube.com/playlist?list=PLhr1KZpdzukcQMnw93OpyqLTsx-Y-lC7i "https://www.youtube.com/playlist?list=PLhr1KZpdzukcQMnw93OpyqLTsx-Y-lC7i")
