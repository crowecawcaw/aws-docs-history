

# Amazon Textract endpoints and quotas
<a name="textract"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="textract_region"></a>


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  textract.us-east-2.amazonaws.com <br /> textract-fips.us-east-2.api.aws <br /> textract-fips.us-east-2.amazonaws.com <br /> textract.us-east-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US East (N. Virginia) | us-east-1 |  textract.us-east-1.amazonaws.com <br /> textract-fips.us-east-1.api.aws <br /> textract-fips.us-east-1.amazonaws.com <br /> textract.us-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (N. California) | us-west-1 |  textract.us-west-1.amazonaws.com <br /> textract-fips.us-west-1.api.aws <br /> textract-fips.us-west-1.amazonaws.com <br /> textract.us-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 |  textract.us-west-2.amazonaws.com <br /> textract-fips.us-west-2.api.aws <br /> textract-fips.us-west-2.amazonaws.com <br /> textract.us-west-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  textract.ap-south-1.amazonaws.com <br /> textract.ap-south-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  textract.ap-northeast-2.amazonaws.com <br /> textract.ap-northeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  textract.ap-southeast-1.amazonaws.com <br /> textract.ap-southeast-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  textract.ap-southeast-2.amazonaws.com <br /> textract.ap-southeast-2.api.aws  | HTTPS<br />HTTPS | 
| Canada (Central) | ca-central-1 |  textract.ca-central-1.amazonaws.com <br /> textract-fips.ca-central-1.api.aws <br /> textract-fips.ca-central-1.amazonaws.com <br /> textract.ca-central-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  textract.eu-central-1.amazonaws.com <br /> textract.eu-central-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Ireland) | eu-west-1 |  textract.eu-west-1.amazonaws.com <br /> textract.eu-west-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (London) | eu-west-2 |  textract.eu-west-2.amazonaws.com <br /> textract.eu-west-2.api.aws  | HTTPS<br />HTTPS | 
| Europe (Paris) | eu-west-3 |  textract.eu-west-3.amazonaws.com <br /> textract.eu-west-3.api.aws  | HTTPS<br />HTTPS | 
| Europe (Spain) | eu-south-2 |  textract.eu-south-2.amazonaws.com <br /> textract.eu-south-2.api.aws  | HTTPS<br />HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  textract.us-gov-east-1.amazonaws.com <br /> textract-fips.us-gov-east-1.api.aws <br /> textract-fips.us-gov-east-1.amazonaws.com <br /> textract.us-gov-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  textract.us-gov-west-1.amazonaws.com <br /> textract-fips.us-gov-west-1.api.aws <br /> textract-fips.us-gov-west-1.amazonaws.com <br /> textract.us-gov-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 

## Service quotas
<a name="limits_textract"></a>


<table>
<thead>
  <tr><th colspan="2">Resources</th><th colspan="6">Regions</th></tr>
</thead>
<tbody>
  <tr><td>Synchronous Operations</td><td>API</td><td>US East (N. Virginia)</td><td>US West (Oregon)</td><td>US East (Ohio)</td><td>Europe (Ireland)</td><td>Asia Pacific (Mumbai)</td><td>Other Regions</td></tr>
  <tr><td rowspan="4">Transactions per second per account for synchronous operations</td><td>AnalyzeDocument</td><td>10</td><td>10</td><td>10</td><td>5</td><td>5</td><td>1</td></tr>
  <tr><td>DetectDocumentText</td><td>25</td><td>25</td><td>10</td><td>5</td><td>5</td><td>1</td></tr>
  <tr><td>AnalyzeExpense</td><td>5</td><td>5</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>
  <tr><td>AnalyzeID</td><td>5</td><td>5</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>
  <tr><td>Asynchronous Operations</td><td>API</td><td>US East (N. Virginia)</td><td>US West (Oregon)</td><td>US East (Ohio)</td><td>Europe (Ireland)</td><td>Asia Pacific (Mumbai)</td><td>Other Regions</td></tr>
  <tr><td rowspan="4">Transactions per second per account for all start (asynchronous) operations</td><td>StartDocumentAnalysis</td><td>10</td><td>10</td><td>10</td><td>5</td><td>5</td><td>2</td></tr>
  <tr><td>StartDocumentTextDetection</td><td>15</td><td>15</td><td>5</td><td>5</td><td>5</td><td>1</td></tr>
  <tr><td>StartExpenseAnalysis</td><td>5</td><td>5</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>
  <tr><td>StartLendingAnalysis</td><td>5</td><td>5</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>
  <tr><td rowspan="5">Transactions per second per account for all get (asynchronous) operations</td><td>GetDocumentAnalysis</td><td>10</td><td>10</td><td>10</td><td>5</td><td>5</td><td>5</td></tr>
  <tr><td>GetDocumentTextDetection</td><td>25</td><td>25</td><td>10</td><td>5</td><td>5</td><td>5</td></tr>
  <tr><td>GetExpenseAnalysis</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr>
  <tr><td>GetLendingAnalysis</td><td>25</td><td>25</td><td>5</td><td>5</td><td>5</td><td>5</td></tr>
  <tr><td>GetLendingAnalysisSummary</td><td>5</td><td>5</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>
  <tr><td>Maximum number of asynchronous jobs per account that can simultaneously exist</td><td></td><td>600</td><td>600</td><td>100</td><td>100</td><td>100</td><td>100</td></tr>
</tbody>
</table>


For more information, see [Amazon Textract Quotas](https://docs.aws.amazon.com/textract/latest/dg/limits.html) in the *Amazon Textract Developer Guide*.

## Adapters quotas
<a name="limits_textract-adapters"></a>
+  Maximum number of adapters - Total number of adapters allowed are 10. You can have a several adapter versions under a single adapter. 
+  Maximum AdapterVersions created per month - Number of successful adapter versions that can be created per AWS account per month is 10 which will be reset at the start of every month. Use the Service Quotas console to raise a service quota increase request. 
+  Maximum in-progress AdapterVersions (analogous to adapter training) per account - 3 

For more information, see [Amazon Textract Quotas](https://docs.aws.amazon.com/textract/latest/dg/limits.html) in the *Amazon Textract Developer Guide*.