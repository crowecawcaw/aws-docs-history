

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
| US West (N. California) | us-west-1 (limited to the following Availability Zones: usw1-az1 and usw1-az3) | `emr-serverless.us-west-1.amazonaws.com` | HTTPS | 
| US West (Oregon) | us-west-2 (limited to the following Availability Zones: usw2-az1, usw2-az2, usw2-az3, and usw2-az4) | `emr-serverless.us-west-2.amazonaws.com`<br />`emr-serverless-fips.us-west-2.amazonaws.com` | HTTPS | 
| Africa (Cape Town) | af-south-1 (limited to the following Availability Zones: afs1-az1, afs1-az2, and afs1-az3) | `emr-serverless.af-south-1.amazonaws.com` | HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 (limited to the following Availability Zones: ape1-az1, ape1-az2, and ape1-az3) | `emr-serverless.ap-east-1.amazonaws.com` | HTTPS | 
| Asia Pacific (Taipei) | ap-east-2 (limited to the following Availability Zones: ape2-az1, ape2-az2, and ape2-az3) | `emr-serverless.ap-east-2.amazonaws.com` | HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 (limited to the following Availability Zones: apse3-az1, apse3-az2, and apse3-az3) | `emr-serverless.ap-southeast-3.amazonaws.com` | HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 (limited to the following Availability Zones: apse4-az1, apse4-az2, and apse4-az3) | `emr-serverless.ap-southeast-4.amazonaws.com` | HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 (limited to the following Availability Zones: apse5-az1, apse5-az2, and apse5-az3) | `emr-serverless.ap-southeast-5.amazonaws.com` | HTTPS | 
| Asia Pacific (New Zealand) | ap-southeast-6 (limited to the following Availability Zones: apse6-az1, apse6-az2, and apse6-az3) | `emr-serverless.ap-southeast-6.amazonaws.com` | HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 (limited to the following Availability Zones: apse7-az1, apse7-az2, and apse7-az3) | `emr-serverless.ap-southeast-7.amazonaws.com` | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 (limited to the following Availability Zones: aps1-az1, aps1-az2, and aps1-az3) | `emr-serverless.ap-south-1.amazonaws.com` | HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 (limited to the following Availability Zones: aps2-az1, aps2-az2, and aps2-az3) | `emr-serverless.ap-south-2.amazonaws.com` | HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 (limited to the following Availability Zones: apne3-az1, apne3-az2, and apne3-az3) | `emr-serverless.ap-northeast-3.amazonaws.com` | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 (limited to the following Availability Zones: apne2-az1, apne2-az2, apne2-az3, and apne2-az4) | `emr-serverless.ap-northeast-2.amazonaws.com` | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 (limited to the following Availability Zones: apse1-az1, apse1-az2, and apse1-az3) | `emr-serverless.ap-southeast-1.amazonaws.com` | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 (limited to the following Availability Zones: apse2-az1, apse2-az2, and apse2-az3) | `emr-serverless.ap-southeast-2.amazonaws.com` | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 (limited to the following Availability Zones: apne1-az1, apne1-az2, and apne1-az4) | `emr-serverless.ap-northeast-1.amazonaws.com` | HTTPS | 
| Canada (Central) | ca-central-1 (limited to the following Availability Zones: cac1-az1, cac1-az2, and cac1-az4) | `emr-serverless.ca-central-1.amazonaws.com` | HTTPS | 
| Canada West (Calgary) | ca-west-1 (limited to the following Availability Zones: caw1-az1, caw1-az2, and caw1-az3) | `emr-serverless.ca-west-1.amazonaws.com` | HTTPS | 
| Europe (Frankfurt) | eu-central-1 (limited to the following Availability Zones: euc1-az1, euc1-az2, and euc1-az3) | `emr-serverless.eu-central-1.amazonaws.com` | HTTPS | 
| Europe (Zurich) | eu-central-2 (limited to the following Availability Zones: euc2-az1, euc2-az2, and euc2-az3) | `emr-serverless.eu-central-2.amazonaws.com` | HTTPS | 
| Europe (Ireland) | eu-west-1 (limited to the following Availability Zones: euw1-az1, euw1-az2, and euw1-az3) | `emr-serverless.eu-west-1.amazonaws.com` | HTTPS | 
| Europe (London) | eu-west-2 (limited to the following Availability Zones: euw2-az1, euw2-az2, and euw2-az3) | `emr-serverless.eu-west-2.amazonaws.com` | HTTPS | 
| Europe (Milan) | eu-south-1 (limited to the following Availability Zones: eus1-az1, eus1-az2, and eus1-az3) | `emr-serverless.eu-south-1.amazonaws.com` | HTTPS | 
| Europe (Paris) | eu-west-3 (limited to the following Availability Zones: euw3-az1, euw3-az2, and euw3-az3) | `emr-serverless.eu-west-3.amazonaws.com` | HTTPS | 
| Europe (Spain) | eu-south-2 (limited to the following Availability Zones: eus2-az1, eus2-az2, and eus2-az3) | `emr-serverless.eu-south-2.amazonaws.com` | HTTPS | 
| Europe (Stockholm) | eu-north-1 (limited to the following Availability Zones: eun1-az1, eun1-az2, and eun1-az3) | `emr-serverless.eu-north-1.amazonaws.com` | HTTPS | 
| Israel (Tel Aviv) | il-central-1 (limited to the following Availability Zones: ilc1-az1, ilc1-az2, and ilc1-az3) | `emr-serverless.il-central-1.amazonaws.com` | HTTPS | 
| Middle East (Bahrain) | me-south-1 | `emr-serverless.me-south-1.amazonaws.com` | HTTPS | 
| Middle East (UAE) | me-central-1 (limited to the following Availability Zones: mec1-az1, mec1-az2, and mec1-az3) | `emr-serverless.me-central-1.amazonaws.com` | HTTPS | 
| Mexico (Central) | mx-central-1 (limited to the following Availability Zones: mxc1-az1, mxc1-az2, and mxc1-az3) | `emr-serverless.mx-central-1.amazonaws.com` | HTTPS | 
| South America (São Paulo) | sa-east-1 (limited to the following Availability Zones: sae1-az1, sae1-az2, and sae1-az3) | `emr-serverless.sa-east-1.amazonaws.com` | HTTPS | 
| China (Beijing) | cn-north-1 (limited to the following Availability Zones: cnn1-az1, cnn1-az2) | `emr-serverless.cn-north-1.amazonaws.com.cn` | HTTPS | 
| AWS GovCloud (US-East) | us-gov-east-1 (limited to the following Availability Zones: usge1-az1, usge1-az2, and usge1-az3) | `emr-serverless.us-gov-east-1.amazonaws.com` | HTTPS | 
| AWS GovCloud (US-West) | us-gov-west-1 (limited to the following Availability Zones: usgw1-az1, usgw1-az2, and usgw1-az3) | `emr-serverless.us-gov-west-1.amazonaws.com` | HTTPS | 

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