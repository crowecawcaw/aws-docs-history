

# Endpoints and quotas for EMR Serverless
<a name="endpoints-quotas"></a>

## Service endpoints
<a name="endpoints"></a>

To connect programmatically to an AWS service, you use an *endpoint*. An endpoint is the URL of the entry point for an AWS web service. In addition to the standard AWS endpoints, some AWS services offer FIPS endpoints in selected Regions. The following table lists the service endpoints for EMR Serverless. For more information, refer to [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).


**EMR Serverless service endpoints**  

| Region name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 (limited to the following Availability Zones: use2-az1, use2-az2, and use2-az3) | `emr-serverless.us-east-2.amazonaws.com` | HTTPS | 
| US East (N. Virginia) | us-east-1 (limited to the following Availability Zones: use1-az1, use1-az2, use1-az4, use1-az5, and use1-az6) | `emr-serverless.us-east-1.amazonaws.com`<br />`emr-serverless-fips.us-east-1.amazonaws.com` | HTTPS | 
| US West (N. California) | us-west-1 | `emr-serverless.us-west-1.amazonaws.com` | HTTPS | 
| US West (Oregon) | us-west-2 | `emr-serverless.us-west-2.amazonaws.com`<br />`emr-serverless-fips.us-west-2.amazonaws.com` | HTTPS | 
| Africa (Cape Town) | af-south-1 | `emr-serverless.af-south-1.amazonaws.com` | HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 | `emr-serverless.ap-east-1.amazonaws.com` | HTTPS | 
| Asia Pacific (Taipei) | ap-east-2 | `emr-serverless.ap-east-2.amazonaws.com` | HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 | `emr-serverless.ap-southeast-3.amazonaws.com` | HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 | `emr-serverless.ap-southeast-4.amazonaws.com` | HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 | `emr-serverless.ap-southeast-5.amazonaws.com` | HTTPS | 
| Asia Pacific (New Zealand) | ap-southeast-6 | `emr-serverless.ap-southeast-6.amazonaws.com` | HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 | `emr-serverless.ap-southeast-7.amazonaws.com` | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 | `emr-serverless.ap-south-1.amazonaws.com` | HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 | `emr-serverless.ap-south-2.amazonaws.com` | HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 | `emr-serverless.ap-northeast-3.amazonaws.com` | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 | `emr-serverless.ap-northeast-2.amazonaws.com` | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 | `emr-serverless.ap-southeast-1.amazonaws.com` | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 | `emr-serverless.ap-southeast-2.amazonaws.com` | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | `emr-serverless.ap-northeast-1.amazonaws.com` | HTTPS | 
| Canada (Central) | ca-central-1 (limited to the following Availability Zones: cac1-az1 and cac1-az2) | `emr-serverless.ca-central-1.amazonaws.com` | HTTPS | 
| Canada West (Calgary) | ca-west-1 | `emr-serverless.ca-west-1.amazonaws.com` | HTTPS | 
| Europe (Frankfurt) | eu-central-1 | `emr-serverless.eu-central-1.amazonaws.com` | HTTPS | 
| Europe (Zurich) | eu-central-2 | `emr-serverless.eu-central-2.amazonaws.com` | HTTPS | 
| Europe (Ireland) | eu-west-1 | `emr-serverless.eu-west-1.amazonaws.com` | HTTPS | 
| Europe (London) | eu-west-2 (limited to the following Availability Zones: euw2-az1, euw2-az2, and euw2-az3) | `emr-serverless.eu-west-2.amazonaws.com` | HTTPS | 
| Europe (Milan) | eu-south-1 | `emr-serverless.eu-south-1.amazonaws.com` | HTTPS | 
| Europe (Paris) | eu-west-3 | `emr-serverless.eu-west-3.amazonaws.com` | HTTPS | 
| Europe (Spain) | eu-south-2 | `emr-serverless.eu-south-2.amazonaws.com` | HTTPS | 
| Europe (Stockholm) | eu-north-1 | `emr-serverless.eu-north-1.amazonaws.com` | HTTPS | 
| Israel (Tel Aviv) | il-central-1 | `emr-serverless.il-central-1.amazonaws.com` | HTTPS | 
| Middle East (Bahrain) | me-south-1 | `emr-serverless.me-south-1.amazonaws.com` | HTTPS | 
| Middle East (UAE) | me-central-1 | `emr-serverless.me-central-1.amazonaws.com` | HTTPS | 
| Mexico (Central) | mx-central-1 | `emr-serverless.mx-central-1.amazonaws.com` | HTTPS | 
| South America (São Paulo) | sa-east-1 | `emr-serverless.sa-east-1.amazonaws.com` | HTTPS | 
| China (Beijing) | cn-north-1 (limited to the following Availability Zones: cnn1-az1, cnn1-az2) | `emr-serverless.cn-north-1.amazonaws.com.cn` | HTTPS | 
| AWS GovCloud (US-East) | us-gov-east-1 | `emr-serverless.us-gov-east-1.amazonaws.com` | HTTPS | 
| AWS GovCloud (US-West) | us-gov-west-1 | `emr-serverless.us-gov-west-1.amazonaws.com` | HTTPS | 

## Regional release support
<a name="regional-release-support"></a>

For information about the minimum supported releases in each Region, see the following table.


**Minimum supported EMR releases by Region**  

| Region name | Region | Minimum supported EMR release | 
| --- | --- | --- | 
| Asia Pacific (Taipei) | `ap-east-2` | emr-7.10.0 and later | 
| Asia Pacific (Malaysia) | `ap-southeast-5` | emr-7.10.0 and later | 
| Asia Pacific (New Zealand) | `ap-southeast-6` | emr-7.10.0 and later | 
| Asia Pacific (Thailand) | `ap-southeast-7` | emr-7.10.0 and later | 
| Canada West (Calgary) | `ca-west-1` | emr-6.9.0 and later | 
| Mexico (Central) | `mx-central-1` | emr-7.10.0 and later | 

## Service quotas
<a name="quotas"></a>

*Service quotas*, also known as *limits*, are the maximum number of service resources or operations that your AWS account can use. EMR Serverless collects service quota usage metrics every minute and publishes them in the `AWS/Usage` namespace.

**Note**  
New AWS accounts have initial lower quotas that can increase over time. Amazon EMR Serverless monitors account usage within each AWS Region, and then automatically increases the quotas based on your usage.

The following table lists the service quotas for EMR Serverless. For more information, refer to [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).



| Name | Default limit | Adjustable? | Description | 
| --- | --- | --- | --- | 
| Max concurrent vCPUs per account | 16 | Yes | The maximum number of vCPUs that can concurrently run for the account in the current AWS Region.<br />Valid Period: 1 minute<br />Valid Statistics: Sum | 

## API limits
<a name="api-limits"></a>

The following describes the API limits per Region for your AWS account.



| Resource | Default quota | 
| --- | --- | 
| [ListApplications](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListApplications.html) | 10 transactions per second. Burst of 50 transactions per second. | 
| [CreateApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_CreateApplication.html) | 1 transaction per second. Burst of 25 transactions per second. | 
| [DeleteApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_DeleteApplication.html) | 1 transaction per second. Burst of 25 transactions per second. | 
| [GetApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetApplication.html) | 10 transactions per second. Burst of 50 transactions per second. | 
| [UpdateApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_UpdateApplication.html) | 1 transaction per second. Burst of 25 transactions per second. | 
| [ListJobRuns](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListJobRuns.html) | 1 transaction per second. Burst of 25 transactions per second. | 
| [StartJobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_StartJobRun.html) | 1 transaction per second. Burst of 25 transactions per second. | 
| [GetDashboardForJobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetDashboardForJobRun.html) | 1 transaction per second. Burst of 2 transactions per second. | 
| [CancelJobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_CancelJobRun.html) | 1 transaction per second. Burst of 25 transactions per second. | 
| [GetJobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetJobRun.html) | 10 transactions per second. Burst of 50 transactions per second. | 
| [StartApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_StartApplication.html) | 1 transaction per second. Burst of 25 transactions per second. | 
| [StopApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_StopApplication.html) | 1 transaction per second. Burst of 25 transactions per second. | 