# FIPS compliance in

Amazon OpenSearch Serverless

Amazon OpenSearch Serverless supports Federal Information Processing Standards (FIPS) 140-2, which is a U.S.
and Canadian government standard that specifies security requirements for cryptographic
modules that protect sensitive information. When you connect to FIPS-enabled endpoints with
OpenSearch Serverless, cryptographic operations occur using FIPS-validated cryptographic libraries.

OpenSearch Serverless FIPS endpoints are available in AWS Regions where FIPS is supported. These
endpoints use TLS 1.2 or later and FIPS-validated cryptographic algorithms for all
communications. For more information, see [FIPS compliance](../../../verified-access/latest/ug/fips-compliance.md "../../../verified-access/latest/ug/fips-compliance.md") in the
_AWS Verified access User Guide_.

###### Topics

- [Using FIPS endpoints with
  OpenSearch Serverless](#using-fips-endpoints-opensearch-serverless "#using-fips-endpoints-opensearch-serverless")
- [Use FIPS endpoints with AWS
  SDKs](#using-fips-endpoints-aws-sdks "#using-fips-endpoints-aws-sdks")
- [Configure security groups
  for VPC endpoints](#configuring-security-groups-vpc-endpoints "#configuring-security-groups-vpc-endpoints")
- [Use the FIPS VPC endpoint](#using-fips-vpc-endpoint "#using-fips-vpc-endpoint")
- [Verify FIPS compliance](#verifying-fips-compliance "#verifying-fips-compliance")
- [Resolve FIPS endpoint connectivity issues
  in private hosted zones](serverless-fips-endpoint-issues.md "serverless-fips-endpoint-issues.md")

## Using FIPS endpoints with

OpenSearch Serverless

In AWS Regions where FIPS is supported, OpenSearch Serverless collections are accessible through
both standard and FIPS-compliant endpoints. For more information, see [FIPS
compliance](../../../verified-access/latest/ug/fips-compliance.md "../../../verified-access/latest/ug/fips-compliance.md") in the _AWS Verified access User
Guide_.

In the following examples, replace `collection_id` and
`AWS Region` with your collection ID and its
AWS Region.

- **Standard endpoint** –
  `https://`collection_id`.`AWS Region`.aoss.amazonaws.com`.
- **FIPS-compliant endpoint** –
  `https://`collection_id`.`AWS Region`.aoss-fips.amazonaws.com`.

Similarly, OpenSearch Dashboards are accessible through both standard and FIPS-compliant
endpoints:

- **Standard Dashboards endpoint** –
  `https://`collection_id`.`AWS Region`.aoss.amazonaws.com/_dashboards`.
- **FIPS-compliant Dashboards endpoint** –
  `https://`collection_id`.`AWS Region`.aoss-fips.amazonaws.com/_dashboards`.

###### Note

In FIPS-enabled Regions, both standard and FIPS-compliant endpoints provide
FIPS-compliant cryptography. The FIPS-specific endpoints help you meet compliance
requirements that specifically mandate the use of endpoints with
**FIPS** in the name.

## Use FIPS endpoints with AWS

SDKs

When using AWS SDKs, you can specify the FIPS endpoint when creating the client. In
the following example, replace `collection_id` and
`AWS Region` with your collection ID and its
AWS Region.

```
# Python SDK example
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
import boto3
host = '"https://`collection_id`.`AWS Region`.aoss-fips.amazonaws.com"
region = 'us-west-2'
service = 'aoss'
credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region, service)
client = OpenSearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = auth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection,
    pool_maxsize = 20
)
```

## Configure security groups

for VPC endpoints

To ensure proper communication with your FIPS-compliant Amazon VPC (VPC) endpoint, create
or modify a security group to allow inbound HTTPS traffic (TCP port 443) from the
resources in your VPC that need to access OpenSearch Serverless. Then associate this security group
with your VPC endpoint during creation or by modifying the endpoint after creation. For
more information, see [Create a security
group](../../../vpc/latest/userguide/creating-security-groups.md "../../../vpc/latest/userguide/creating-security-groups.md") in the _Amazon VPC User Guide_.

## Use the FIPS VPC endpoint

After creating the FIPS-compliant VPC endpoint, you can use it to access OpenSearch Serverless from
resources within your VPC. To use the endpoint for API operations, configure your
SDK to use the Regional FIPS endpoint as described in the [Using FIPS endpoints with
OpenSearch Serverless](#using-fips-endpoints-opensearch-serverless "#using-fips-endpoints-opensearch-serverless") section. For
OpenSearch Dashboards access, use the collection-specific Dashboards URL, which will
automatically route through the FIPS-compliant VPC endpoint when accessed from within
your VPC. For more information, see [Using OpenSearch Dashboards with Amazon OpenSearch Service](dashboards.md "dashboards.md").

## Verify FIPS compliance

To verify that your connections to OpenSearch Serverless are using FIPS-compliant cryptography, use
AWS CloudTrail to monitor API calls made to OpenSearch Serverless. Check that the `eventSource`
field in CloudTrail logs displays `aoss-fips.amazonaws.com` for API calls.

For OpenSearch Dashboards access, you can use browser developer tools to inspect the TLS
connection details and verify that FIPS-compliant cipher suites are being used.
