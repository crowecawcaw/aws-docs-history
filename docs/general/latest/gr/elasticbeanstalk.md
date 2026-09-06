

# AWS Elastic Beanstalk endpoints and quotas
<a name="elasticbeanstalk"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="elasticbeanstalk_region"></a>

**Note**  
The AWS Elastic Beanstalk service offers dual stack endpoints, so that you can send it either IPv4 or IPv6 requests. For more information about the naming syntax for dual-stack endpoints, see [Dual stack endpoints](rande.md#dual-stack-endpoints) in this guide. For more information about Elastic Beanstalk support for dual-stack endpoints, see [IPv6 support](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/vpc-vpce.html#vpc-vpce.ipv6) in the *AWS Elastic Beanstalk Developer Guide*. 

### Elastic Beanstalk
<a name="elasticbeanstalk-service"></a>


| Region Name | Region | Endpoint | Protocol | Route 53 Hosted Zone ID | 
| --- | --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  elasticbeanstalk.us-east-2.amazonaws.com <br /> elasticbeanstalk-fips.us-east-2.api.aws <br /> elasticbeanstalk-fips.us-east-2.amazonaws.com <br /> elasticbeanstalk.us-east-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | Z14LCN19Q5QHIC<br /> <br /> <br />  | 
| US East (N. Virginia) | us-east-1 |  elasticbeanstalk.us-east-1.amazonaws.com <br /> elasticbeanstalk-fips.us-east-1.api.aws <br /> elasticbeanstalk-fips.us-east-1.amazonaws.com <br /> elasticbeanstalk.us-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | Z117KPS5GTRQ2G<br /> <br /> <br />  | 
| US West (N. California) | us-west-1 |  elasticbeanstalk.us-west-1.amazonaws.com <br /> elasticbeanstalk-fips.us-west-1.api.aws <br /> elasticbeanstalk-fips.us-west-1.amazonaws.com <br /> elasticbeanstalk.us-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | Z1LQECGX5PH1X<br /> <br /> <br />  | 
| US West (Oregon) | us-west-2 |  elasticbeanstalk.us-west-2.amazonaws.com <br /> elasticbeanstalk-fips.us-west-2.api.aws <br /> elasticbeanstalk-fips.us-west-2.amazonaws.com <br /> elasticbeanstalk.us-west-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | Z38NKT9BP95V3O<br /> <br /> <br />  | 
| Africa (Cape Town) | af-south-1 |  elasticbeanstalk.af-south-1.amazonaws.com <br /> elasticbeanstalk.af-south-1.api.aws  | HTTPS<br />HTTPS | Z1EI3BVKMKK4AM<br />  | 
| Asia Pacific (Hong Kong) | ap-east-1 |  elasticbeanstalk.ap-east-1.amazonaws.com <br /> elasticbeanstalk.ap-east-1.api.aws  | HTTPS<br />HTTPS | ZPWYUBWRU171A<br />  | 
| Asia Pacific (Hyderabad) | ap-south-2 |  elasticbeanstalk.ap-south-2.amazonaws.com <br /> elasticbeanstalk.ap-south-2.api.aws  | HTTPS<br />HTTPS | Z10223522IBWPBF2C2FJS<br />  | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  elasticbeanstalk.ap-southeast-3.amazonaws.com <br /> elasticbeanstalk.ap-southeast-3.api.aws  | HTTPS<br />HTTPS | Z05913172VM7EAZB40TA8<br />  | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  elasticbeanstalk.ap-southeast-5.amazonaws.com <br /> elasticbeanstalk.ap-southeast-5.api.aws  | HTTPS<br />HTTPS | Z01812971H0QCYWSL7WOH<br />  | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  elasticbeanstalk.ap-southeast-4.amazonaws.com <br /> elasticbeanstalk.ap-southeast-4.api.aws  | HTTPS<br />HTTPS | Z0666869LC74UHAO5YE4<br />  | 
| Asia Pacific (Mumbai) | ap-south-1 |  elasticbeanstalk.ap-south-1.amazonaws.com <br /> elasticbeanstalk.ap-south-1.api.aws  | HTTPS<br />HTTPS | Z18NTBI3Y7N9TZ<br />  | 
| Asia Pacific (New Zealand) | ap-southeast-6 |  elasticbeanstalk.ap-southeast-6.amazonaws.com <br /> elasticbeanstalk.ap-southeast-6.api.aws  | HTTPS<br />HTTPS | Z01144401H1NECCLJDD4D<br />  | 
| Asia Pacific (Osaka) | ap-northeast-3 |  elasticbeanstalk.ap-northeast-3.amazonaws.com <br /> elasticbeanstalk.ap-northeast-3.api.aws  | HTTPS<br />HTTPS | ZNE5GEY1TIAGY<br />  | 
| Asia Pacific (Seoul) | ap-northeast-2 |  elasticbeanstalk.ap-northeast-2.amazonaws.com <br /> elasticbeanstalk.ap-northeast-2.api.aws  | HTTPS<br />HTTPS | Z3JE5OI70TWKCP<br />  | 
| Asia Pacific (Singapore) | ap-southeast-1 |  elasticbeanstalk.ap-southeast-1.amazonaws.com <br /> elasticbeanstalk.ap-southeast-1.api.aws  | HTTPS<br />HTTPS | Z16FZ9L249IFLT<br />  | 
| Asia Pacific (Sydney) | ap-southeast-2 |  elasticbeanstalk.ap-southeast-2.amazonaws.com <br /> elasticbeanstalk.ap-southeast-2.api.aws  | HTTPS<br />HTTPS | Z2PCDNR3VC2G1N<br />  | 
| Asia Pacific (Thailand) | ap-southeast-7 |  elasticbeanstalk.ap-southeast-7.amazonaws.com <br /> elasticbeanstalk.ap-southeast-7.api.aws  | HTTPS<br />HTTPS | Z08384933QM5LSQCVMNZM<br />  | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  elasticbeanstalk.ap-northeast-1.amazonaws.com <br /> elasticbeanstalk.ap-northeast-1.api.aws  | HTTPS<br />HTTPS | Z1R25G3KIG2GBW<br />  | 
| Canada (Central) | ca-central-1 |  elasticbeanstalk.ca-central-1.amazonaws.com <br /> elasticbeanstalk.ca-central-1.api.aws  | HTTPS<br />HTTPS | ZJFCZL7SSZB5I<br />  | 
| Canada West (Calgary) | ca-west-1 |  elasticbeanstalk.ca-west-1.amazonaws.com <br /> elasticbeanstalk.ca-west-1.api.aws  | HTTPS<br />HTTPS | Z1021028356Y0CYS11DQI<br />  | 
| Europe (Frankfurt) | eu-central-1 |  elasticbeanstalk.eu-central-1.amazonaws.com <br /> elasticbeanstalk.eu-central-1.api.aws  | HTTPS<br />HTTPS | Z1FRNW7UH4DEZJ<br />  | 
| Europe (Ireland) | eu-west-1 |  elasticbeanstalk.eu-west-1.amazonaws.com <br /> elasticbeanstalk.eu-west-1.api.aws  | HTTPS<br />HTTPS | Z2NYPWQ7DFZAZH<br />  | 
| Europe (London) | eu-west-2 |  elasticbeanstalk.eu-west-2.amazonaws.com <br /> elasticbeanstalk.eu-west-2.api.aws  | HTTPS<br />HTTPS | Z1GKAAAUGATPF1<br />  | 
| Europe (Milan) | eu-south-1 |  elasticbeanstalk.eu-south-1.amazonaws.com <br /> elasticbeanstalk.eu-south-1.api.aws  | HTTPS<br />HTTPS | Z10VDYYOA2JFKM<br />  | 
| Europe (Paris) | eu-west-3 |  elasticbeanstalk.eu-west-3.amazonaws.com <br /> elasticbeanstalk.eu-west-3.api.aws  | HTTPS<br />HTTPS | Z5WN6GAYWG5OB<br />  | 
| Europe (Spain) | eu-south-2 |  elasticbeanstalk.eu-south-2.amazonaws.com <br /> elasticbeanstalk.eu-south-2.api.aws  | HTTPS<br />HTTPS | Z0243492AO4B9S3KI68O<br />  | 
| Europe (Stockholm) | eu-north-1 |  elasticbeanstalk.eu-north-1.amazonaws.com <br /> elasticbeanstalk.eu-north-1.api.aws  | HTTPS<br />HTTPS | Z23GO28BZ5AETM<br />  | 
| Europe (Zurich) | eu-central-2 |  elasticbeanstalk.eu-central-2.amazonaws.com <br /> elasticbeanstalk.eu-central-2.api.aws  | HTTPS<br />HTTPS | Z00227012FSHBMZNNSJJI<br />  | 
| Israel (Tel Aviv) | il-central-1 |  elasticbeanstalk.il-central-1.amazonaws.com <br /> elasticbeanstalk.il-central-1.api.aws  | HTTPS<br />HTTPS | Z02941091PERNCB1MI5H7<br />  | 
| Middle East (Bahrain) | me-south-1 |  elasticbeanstalk.me-south-1.amazonaws.com <br /> elasticbeanstalk.me-south-1.api.aws  | HTTPS<br />HTTPS | Z2BBTEKR2I36N2<br />  | 
| Middle East (UAE) | me-central-1 |  elasticbeanstalk.me-central-1.amazonaws.com <br /> elasticbeanstalk.me-central-1.api.aws  | HTTPS<br />HTTPS | Z0650511N84AAKGW7QUK<br />  | 
| South America (São Paulo) | sa-east-1 |  elasticbeanstalk.sa-east-1.amazonaws.com <br /> elasticbeanstalk.sa-east-1.api.aws  | HTTPS<br />HTTPS | Z10X7K2B4QSOFV<br />  | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  elasticbeanstalk.us-gov-east-1.amazonaws.com <br /> elasticbeanstalk.us-gov-east-1.api.aws  | HTTPS<br />HTTPS | Z35TSARG0EJ4VU<br />  | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  elasticbeanstalk.us-gov-west-1.amazonaws.com <br /> elasticbeanstalk.us-gov-west-1.api.aws  | HTTPS<br />HTTPS | Z4KAURWC4UUUG<br />  | 

### Elastic Beanstalk Health Service
<a name="elasticbeanstalk-health"></a>


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  elasticbeanstalk-health.us-east-2.amazonaws.com  | HTTPS | 
| US East (N. Virginia) | us-east-1 |  elasticbeanstalk-health.us-east-1.amazonaws.com  | HTTPS | 
| US West (N. California) | us-west-1 |  elasticbeanstalk-health.us-west-1.amazonaws.com  | HTTPS | 
| US West (Oregon) | us-west-2 |  elasticbeanstalk-health.us-west-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  elasticbeanstalk-health.ap-east-1.amazonaws.com  | HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 |  elasticbeanstalk-health.ap-south-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  elasticbeanstalk-health.ap-southeast-3.amazonaws.com  | HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  elasticbeanstalk-health.ap-southeast-5.amazonaws.com  | HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  elasticbeanstalk-health.ap-southeast-4.amazonaws.com  | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  elasticbeanstalk-health.ap-south-1.amazonaws.com  | HTTPS | 
| Asia Pacific (New Zealand) | ap-southeast-6 |  elasticbeanstalk-health.ap-southeast-6.amazonaws.com  | HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 |  elasticbeanstalk-health.ap-northeast-3.amazonaws.com  | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  elasticbeanstalk-health.ap-northeast-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  elasticbeanstalk-health.ap-southeast-1.amazonaws.com  | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  elasticbeanstalk-health.ap-southeast-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  elasticbeanstalk-health.ap-southeast-7.amazonaws.com  | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  elasticbeanstalk-health.ap-northeast-1.amazonaws.com  | HTTPS | 
| Canada (Central) | ca-central-1 |  elasticbeanstalk-health.ca-central-1.amazonaws.com  | HTTPS | 
| Canada West (Calgary) | ca-west-1 |  elasticbeanstalk-health.ca-west-1.amazonaws.com  | HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  elasticbeanstalk-health.eu-central-1.amazonaws.com  | HTTPS | 
| Europe (Ireland) | eu-west-1 |  elasticbeanstalk-health.eu-west-1.amazonaws.com  | HTTPS | 
| Europe (London) | eu-west-2 |  elasticbeanstalk-health.eu-west-2.amazonaws.com  | HTTPS | 
| Europe (Paris) | eu-west-3 |  elasticbeanstalk-health.eu-west-3.amazonaws.com  | HTTPS | 
| Europe (Spain) | eu-south-2 |  elasticbeanstalk-health.eu-south-2.amazonaws.com  | HTTPS | 
| Europe (Stockholm) | eu-north-1 |  elasticbeanstalk-health.eu-north-1.amazonaws.com  | HTTPS | 
| Europe (Zurich) | eu-central-2 |  elasticbeanstalk-health.eu-central-2.amazonaws.com  | HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  elasticbeanstalk-health.il-central-1.amazonaws.com  | HTTPS | 
| Middle East (Bahrain) | me-south-1 |  elasticbeanstalk-health.me-south-1.amazonaws.com  | HTTPS | 
| Middle East (UAE) | me-central-1 |  elasticbeanstalk-health.me-central-1.amazonaws.com  | HTTPS | 
| South America (São Paulo) | sa-east-1 |  elasticbeanstalk-health.sa-east-1.amazonaws.com  | HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  elasticbeanstalk-health.us-gov-east-1.amazonaws.com  | HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  elasticbeanstalk-health.us-gov-west-1.amazonaws.com  | HTTPS | 

## Service quotas
<a name="limits_elastic_beanstalk"></a>


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Application versions | Each supported Region: 1,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/elasticbeanstalk/quotas/L-D64F1F14)  | The maximum number of application versions that you can create in this account in the current Region. The limit applies across applications, not per application. | 
| Applications | Each supported Region: 75 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/elasticbeanstalk/quotas/L-1CEABD17)  | The maximum number of applications that you can create in this account in the current Region. | 
| Configuration templates | Each supported Region: 2,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/elasticbeanstalk/quotas/L-9838E43F)  | The maximum number of configuration templates that you can create in this account in the current Region. | 
| Custom platform versions | Each supported Region: 50 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/elasticbeanstalk/quotas/L-E593A077)  | The maximum number of custom platform versions that you can create in this account in the current Region. The limit applies across custom platforms, not per custom platform. | 
| Environments | Each supported Region: 200 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/elasticbeanstalk/quotas/L-8EFC1C51)  | The maximum number of environments that you can create in this account in the current Region. The limit applies across applications, not per application. | 