

# AWS User Notifications endpoints and quotas
<a name="notifications"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="uno_region"></a>


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  notifications.us-east-2.api.aws  | HTTPS | 
| US East (N. Virginia) | us-east-1 |  notifications.us-east-1.api.aws  | HTTPS | 
| US West (N. California) | us-west-1 |  notifications.us-west-1.api.aws  | HTTPS | 
| US West (Oregon) | us-west-2 |  notifications.us-west-2.api.aws  | HTTPS | 
| Africa (Cape Town) | af-south-1 |  notifications.af-south-1.api.aws  | HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  notifications.ap-east-1.api.aws  | HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 |  notifications.ap-south-2.api.aws  | HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  notifications.ap-southeast-3.api.aws  | HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  notifications.ap-southeast-5.api.aws  | HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  notifications.ap-southeast-4.api.aws  | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  notifications.ap-south-1.api.aws  | HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 |  notifications.ap-northeast-3.api.aws  | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  notifications.ap-northeast-2.api.aws  | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  notifications.ap-southeast-1.api.aws  | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  notifications.ap-southeast-2.api.aws  | HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  notifications.ap-southeast-7.api.aws  | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  notifications.ap-northeast-1.api.aws  | HTTPS | 
| Canada (Central) | ca-central-1 |  notifications.ca-central-1.api.aws  | HTTPS | 
| Canada West (Calgary) | ca-west-1 |  notifications.ca-west-1.api.aws  | HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  notifications.eu-central-1.api.aws  | HTTPS | 
| Europe (Ireland) | eu-west-1 |  notifications.eu-west-1.api.aws  | HTTPS | 
| Europe (London) | eu-west-2 |  notifications.eu-west-2.api.aws  | HTTPS | 
| Europe (Milan) | eu-south-1 |  notifications.eu-south-1.api.aws  | HTTPS | 
| Europe (Paris) | eu-west-3 |  notifications.eu-west-3.api.aws  | HTTPS | 
| Europe (Spain) | eu-south-2 |  notifications.eu-south-2.api.aws  | HTTPS | 
| Europe (Stockholm) | eu-north-1 |  notifications.eu-north-1.api.aws  | HTTPS | 
| Europe (Zurich) | eu-central-2 |  notifications.eu-central-2.api.aws  | HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  notifications.il-central-1.api.aws  | HTTPS | 
| Mexico (Central) | mx-central-1 |  notifications.mx-central-1.api.aws  | HTTPS | 
| Middle East (Bahrain) | me-south-1 |  notifications.me-south-1.api.aws  | HTTPS | 
| Middle East (UAE) | me-central-1 |  notifications.me-central-1.api.aws  | HTTPS | 
| South America (São Paulo) | sa-east-1 |  notifications.sa-east-1.api.aws  | HTTPS | 

## AWS User Notifications Contacts endpoints
<a name="uno_contacts_region"></a>


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 |  notifications-contacts.us-east-1.api.aws  | HTTPS | 

## Service quotas
<a name="quotas_notifications"></a>



| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Notification configurations total for an AWS account | 50 notification configurations. | No | The maximum number of notification configurations that you can create in an AWS account. | 
| Notification configurations for a single Service | 20 notification configurations for any specific service for an AWS account. | No | The maximum number of notification configurations that you can create for a given service in an AWS account. | 
| Notification configurations per Service and Event type | 10 notification configurations for each service and event type for an AWS account. | No | The maximum number of notification configurations by Service and Event type you can create for a given AWS account. | 
| Event rules for a given notification configuration | 10 event rules | No | The maximum number of event rules that you can create for each notification configuration in your AWS account. | 
| Channels for a given notification configuration | 50 channels (email, mobile devices, or chat channels) for each notification configuration. | No | The maximum number of channels for each notification configuration that you can create in your AWS account. | 
| Email contacts | 500 email contacts for each AWS account. | No | The maximum number of email contacts that you can add for each AWS account. | 
| Notification hubs | 3 hubs for each AWS account. | No | The maximum number of notification hubs you can add to each AWS account. | 
| Rate of source events for a given AWS account | 1 per second. | No | The maximum number of source events per second you can receive in each AWS account. | 