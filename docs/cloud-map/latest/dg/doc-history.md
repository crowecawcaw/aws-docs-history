

# Document history for AWS Cloud Map
<a name="doc-history"></a>

The following table describes the major updates and new features for the *AWS Cloud Map Developer Guide*. We also update the documentation frequently to address the feedback that you send us. 

| Change | Description | Date | 
| --- |--- |--- |
| [AWS Cloud Map cross-account namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) | You can now share namespaces with other AWS accounts or within an organization in AWS Organizations using AWS Resource Access Manager (AWS RAM) for simplified cross-account service discovery and registry. | August 14, 2025 | 
| [AWS Cloud Map service attributes](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html) | You can now specify attributes at the service level to avoid duplicating attributes across instances that are registered to a service. You can use these attributes for complex traffic routing, setting timeout and retry values, and for coordination between services and external integrations. | December 13, 2024 | 
| [Tutorials added](https://docs.aws.amazon.com/cloud-map/latest/dg/tutorials.html) | Two tutorials showing common use cases for using AWS Cloud Map added. | March 27, 2024 | 
| [CloudTrail integration documentation updated](https://docs.aws.amazon.com/cloud-map/latest/dg/logging-using-cloudtrail.html) | The documentation describing the AWS Cloud Map integration with CloudTrail to log API activity has been updated. | March 20, 2024 | 
| [Managed policy updates](https://docs.aws.amazon.com/cloud-map/latest/dg/security-iam-awsmanpol.html) | `AWSCloudMapDiscoverInstanceAccess`, `AWSCloudMapRegisterInstanceAccess`, and `AWSCloudMapReadOnlyAccess` policies were updated. | September 20, 2023 | 
| [Cloud Map and AWS PrivateLink](https://docs.aws.amazon.com/cloud-map/latest/dg/vpc-interface-endpoints.html) | You can now use an AWS PrivateLink to create a private connection between your VPC and AWS Cloud Map. | September 15, 2023 | 
| [Managed policy update](https://docs.aws.amazon.com/cloud-map/latest/dg/security-iam-awsmanpol.html#security-iam-awsmanpol-AWSCloudMapDiscoverInstanceAccess) | `AWSCloudMapDiscoverInstanceAccess` policy was updated. | August 15, 2023 | 
| [AWS SDK for Python](https://docs.aws.amazon.com/cloud-map/latest/dg/registering-instances.html) | Added Python command line examples. | September 13, 2022 | 
| [IPv6 support](https://docs.aws.amazon.com/cloud-map/latest/dg/registering-instances.html) | API endpoints are now available in `IPv6`-only networks. | January 28, 2022 | 
| [Service instance discovery](https://docs.aws.amazon.com/cloud-map/latest/dg/creating-services.html) | AWS Cloud Map added support for creating services in a namespace that supports DNS queries that are discoverable only using the [DiscoverInstances](https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html) API operation and not using DNS queries. | March 24, 2021 | 
| [Resource tagging](https://docs.aws.amazon.com/cloud-map/latest/dg/using-tags.html) | AWS Cloud Map added support for adding metadata tags to your namespaces and services using the AWS Management Console. | February 8, 2021 | 
| [Resource tagging](https://docs.aws.amazon.com/cloud-map/latest/dg/using-tags.html) | AWS Cloud Map added support for adding metadata tags to your namespaces and services using the AWS CLI and APIs. | June 22, 2020 | 
| [Initial Release](https://docs.aws.amazon.com/cloud-map/latest/dg/) | This is the first release of *AWS Cloud Map Developer Guide*.  | November 28, 2018 | 