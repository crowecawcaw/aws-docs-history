

# AWS Transfer Family in AWS GovCloud (US)
<a name="govcloud-tf"></a>

 AWS Transfer Family is a secure transfer service that enables you to transfer files into and out of Amazon Simple Storage Service (Amazon S3) and Amazon Elastic File System (Amazon EFS) file systems over the following protocols:
+ Secure Shell (SSH) File Transfer Protocol (SFTP) (AWS Transfer for SFTP).
+ File Transfer Protocol Secure (FTPS) (AWS Transfer for FTPS).
+ File Transfer Protocol (FTP) (AWS Transfer for FTP).
+ Applicability Statement 2 (AS2).

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How AWS Transfer Family differs
<a name="govcloud-tf-diffs"></a>

The following differences apply to AWS Transfer Family:
+ PUBLIC and VPC\_ENDPOINT endpoint types are not available. Only VPC endpoint type is supported, for both internal and internet facing access. For more information, see [Creating a server in a virtual private cloud](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html)in the *AWS Transfer Family User Guide*.
+ If you are providing your end users access to your endpoint using a custom hostname, you need to map your endpoint’s IP addresses to the custom domain using Amazon Route 53 or any DNS provider. If you use a hostname registered with Route 53, there are some DNS limitations. For more information about using Route 53 for GovCloud endpoints, see [Setting Up Amazon Route 53 with Your AWS GovCloud (US) Resources](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/migrating-route53-hostedzone.html).
+ For Transfer Family web apps, you can enable FIPS during configuration. To do so, select the **FIPS Enabled endpoint** checkbox on the **Configure web app** screen.

## Documentation
<a name="govcloud-tf-docs"></a>
+  [AWS Transfer Family documentation](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html) 

## Export-controlled content
<a name="govcloud-tf-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  AWS Transfer Family metadata is not permitted to contain export-controlled data.