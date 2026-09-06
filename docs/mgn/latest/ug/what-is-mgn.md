

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# What Is AWS Transform MGN?
<a name="what-is-mgn"></a>

AWS Transform MGN (MGN) automates the migration of physical, virtual, and cloud servers to AWS with minimal downtime, typically cutover windows of minutes. MGN performs continuous block-level replication of your source servers and converts them for launch on AWS, allowing you to migrate large numbers of servers without compatibility issues or performance disruption.

MGN works across a broad range of operating systems including Windows Server and various Linux distributions, and supports both IPv4 and IPv6 network configurations. You can replicate into standard Availability Zones or AWS Local Zones without any special configuration.

The service uses three configurable templates (replication, launch, and post-launch) to control how servers are replicated, launched, and configured after migration. Template settings are applied to each newly added server, and you can override settings for individual servers at any time.

To manage migrations at scale, you can group servers into applications and applications into waves. Configuration changes and actions such as launch, cutover, and archival can be performed at the server, application, or wave level, enabling bulk operations across large environments.

After migration, you can use AWS services to replatform or refactor your applications, making rehosting a fast first step toward modernization.

## Accessing the AWS Transform MGN console
<a name="accessing-console"></a>

You can access AWS Transform MGN through the AWS Management Console or through the following link:

[https://console.aws.amazon.com/mgn/home](https://console.aws.amazon.com/mgn/home)

## Supported AWS Regions
<a name="supported-regions"></a>

The following AWS Regions are supported by AWS Transform MGN:



| Region name | Region identity | Support in AWS Transform MGN | 
| --- | --- | --- | 
| US East (Ohio) | us-east-2 | Yes | 
| US East (N. Virginia) | us-east-1 | Yes | 
| US West (N. California) | us-west-1 | Yes | 
| US West (Oregon) | us-west-2 | Yes | 
| Africa (Cape Town) | af-south-1 | Yes | 
| Asia Pacific (Hong Kong) | ap-east-1 | Yes | 
| Asia Pacific (Taipei) | ap-east-2 | Yes | 
| Asia Pacific (Thailand) |  ap-southeast-7 | Yes | 
| Asia Pacific (Jakarta) | ap-southeast-3 | Yes | 
| Asia Pacific (Malaysia) | ap-southeast-5 | Yes | 
| Asia Pacific (New Zealand) | ap-southeast-6 | Yes | 
| Asia Pacific (Melbourne) | ap-southeast-4 | Yes | 
| Asia Pacific (Mumbai) | ap-south-1 | Yes | 
| Asia Pacific (Hyderabad) | ap-south-2 | Yes | 
| Asia Pacific (Osaka) | ap-northeast-3 | Yes | 
| Asia Pacific (Seoul) | ap-northeast-2 | Yes | 
| Asia Pacific (Singapore) | ap-southeast-1 | Yes | 
| Asia Pacific (Sydney) | ap-southeast-2 | Yes | 
| Asia Pacific (Tokyo) | ap-northeast-1 | Yes | 
| Canada (Central) | ca-central-1 | Yes | 
| Canada West (Calgary) | ca-west-1 | Yes | 
| Europe (Frankfurt) | eu-central-1 | Yes | 
| Europe (Zurich) | eu-central-2 | Yes | 
| Europe (Ireland) | eu-west-1 | Yes | 
| Europe (London) | eu-west-2 | Yes | 
| Europe (Paris) | eu-west-3 | Yes | 
| Europe (Milan) | eu-south-1 | Yes | 
| Europe (Spain) | eu-south-2 | Yes | 
| Europe (Stockholm) | eu-north-1 | Yes | 
| Israel (Tel Aviv) | il-central-1 | Yes | 
| Middle East (Bahrain) | me-south-1 | Yes | 
| Middle East (UAE) | me-central-1 | Yes | 
| Mexico (Central) | mx-central-1 | Yes | 
| South America (São Paulo) | sa-east-1 | Yes | 
| AWS GovCloud (US-East) | us-gov-east-1 | Yes | 
| AWS GovCloud (US-West) | us-gov-west-1 | Yes | 

Learn more about [AWS Regional services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

AWS Transform MGN regional support includes [AWS Local Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-local-zones) associated with the above supported regions.

**Important**  
MGN supports IPv6 in the regions where Amazon EC2 dual-stack endpoints are present. For the list of EC2 dual-stack endpoints, see [Dual-stack (IPv4 and IPv6) endpoints](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-endpoints.html#ipv6) in the *Amazon EC2 Developer Guide*.

## MGN technical training materials
<a name="mgn-training"></a>

The following technical trainings are available for MGN:
+ [AWS Transform MGN - A Technical Introduction](https://www.aws.training/Details/eLearning?id=71732)
+ [Blog posts related to MGN](https://aws.amazon.com/application-migration-service/resources/#Blog_posts_.26_articles)
+ [MGN video playlist](https://www.youtube.com/playlist?list=PLhr1KZpdzukcQMnw93OpyqLTsx-Y-lC7i)