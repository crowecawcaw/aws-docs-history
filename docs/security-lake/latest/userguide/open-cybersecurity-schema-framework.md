

# Open Cybersecurity Schema Framework (OCSF) in Security Lake
<a name="open-cybersecurity-schema-framework"></a>

## What is OCSF?
<a name="what-is-ocsf"></a>

The [Open Cybersecurity Schema Framework (OCSF)](https://schema.ocsf.io/) is a collaborative, open-source effort by AWS and leading partners in the cybersecurity industry. OCSF provides a standard schema for common security events, defines versioning criteria to facilitate schema evolution, and includes a self-governance process for security log producers and consumers. The public source code for OCSF is hosted on [GitHub](https://github.com/ocsf/ocsf-schema).

Security Lake automatically converts logs and events that come from natively-supported AWS services to the OCSF schema. After conversion to OCSF, Security Lake stores the data in an Amazon Simple Storage Service (Amazon S3) bucket (one bucket per AWS Region) in your AWS account. Logs and events that are written to Security Lake from custom sources must adhere to the OCSF schema and an Apache Parquet format. Subscribers can treat the logs and events as generic Parquet records or apply the OCSF schema event class to more accurately interpret the information contained in a record.

## OCSF event classes
<a name="ocsf-event-classes"></a>

Logs and events from a given Security Lake [source](source-management.md) match a specific event class defined in OCSF. DNS Activity, SSH Activity, and Authentication are examples of [event classes in OCSF](https://schema.ocsf.io/classes?extensions=). You can specify which event class a particular source matches. 

## OCSF source identification
<a name="ocsf-source-identification"></a>

OCSF uses a variety of fields to help you determine where a specific set of logs or events originated. These are the values of the relevant fields for AWS services that are natively supported as sources in Security Lake. 

`The OCSF source identification for AWS log sources (Version 1) are listed in the following table.`


| Source | metadata.product.name | metadata.product.vendor\_name | metadata.product.feature.name | class\_name | metadata.version | 
| --- | --- | --- | --- | --- | --- | 
| CloudTrail Lambda Data Events | `CloudTrail` | `AWS` | `Data` | `API Activity` | `1.0.0-rc.2` | 
| CloudTrail Management Events | `CloudTrail` | `AWS` | `Management` | `API Activity`, `Authentication`, or `Account Change` | `1.0.0-rc.2` | 
| CloudTrail S3 Data Events | `CloudTrail` | `AWS` | `Data` | `API Activity` | `1.0.0-rc.2` | 
| Route 53 | `Route 53` | `AWS` | `Resolver Query Logs` | `DNS Activity` | `1.0.0-rc.2` | 
| Security Hub CSPM | `Security Hub CSPM` | `AWS` | Matches Security Hub CSPM [`ProductName`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecurityFindingFilters.html) value | `Security Finding` | `1.0.0-rc.2` | 
| VPC Flow Logs | `Amazon VPC` | `AWS` | `Flowlogs` | `Network Activity` | `1.0.0-rc.2` | 

`The OCSF source identification for AWS log sources (Version 2) are listed in the following table.`


| Source | metadata.product.name | metadata.product.vendor\_name | metadata.product.feature.name | class\_name | metadata.version | 
| --- | --- | --- | --- | --- | --- | 
| CloudTrail Lambda Data Events | `CloudTrail` | `AWS` | `Data` | `API Activity` | `1.1.0` | 
| CloudTrail Management Events | `CloudTrail` | `AWS` | `Management` | `API Activity`, `Authentication`, or `Account Change` | `1.1.0` | 
| CloudTrail S3 Data Events | `CloudTrail` | `AWS` | `Data` | `API Activity` | `1.1.0` | 
| Route 53 | `Route 53` | `AWS` | `Resolver Query Logs` | `DNS Activity` | `1.1.0` | 
| Security Hub CSPM | Matches AWS Security Finding Format (ASFF) [`ProductName`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecurityFindingFilters.html) value | Matches AWS Security Finding Format (ASFF) [`CompanyName`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecurityFindingFilters.html) value | Matches [`featureName`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecurityFindingFilters.html) value from ASFF `ProductFields` | `Vulnerability Finding, Compliance Finding, or Detection Finding` | `1.1.0` | 
| VPC Flow Logs | `Amazon VPC` | `AWS` | `Flowlogs` | `Network Activity` | `1.1.0` | 
| EKS Audit Logs | `Amazon EKS` | `AWS` | `Elastic Kubernetes Service` | `API Activity` | `1.1.0` | 
| AWS WAFv2 Logs | `AWS WAF` | `AWS` | `—` | `HTTP Activity` | `1.1.0` | 