# Document history for AWS Cloud Map

The following table describes the major updates and new features for the *AWS Cloud Map
 Developer Guide*. We also update the documentation frequently to address the feedback
 that you send us. 



| Change | Description | Date |
| --- | --- | --- |
| [AWS Cloud Map cross-account namespace sharing](sharing-namespaces.md "sharing-namespaces.md") | You can now share namespaces with other AWS accounts or within an organization in AWS Organizations using AWS Resource Access Manager (AWS RAM) for simplified cross-account service discovery and registry. | August 14, 2025 |
| [AWS Cloud Map service attributes](working-with-services.md "working-with-services.md") | You can now specify attributes at the service level to avoid duplicating attributes across instances that are registered to a service. You can use these attributes for complex traffic routing, setting timeout and retry values, and for coordination between services and external integrations. | December 13, 2024 |
| [Tutorials added](tutorials.md "tutorials.md") | Two tutorials showing common use cases for using AWS Cloud Map added. | March 27, 2024 |
| [CloudTrail integration documentation updated](logging-using-cloudtrail.md "logging-using-cloudtrail.md") | The documentation describing the AWS Cloud Map integration with CloudTrail to log API activity has been updated. | March 20, 2024 |
| [Managed policy updates](security-iam-awsmanpol.md "security-iam-awsmanpol.md") | `AWSCloudMapDiscoverInstanceAccess`, `AWSCloudMapRegisterInstanceAccess`, and `AWSCloudMapReadOnlyAccess` policies were updated. | September 20, 2023 |
| [Cloud Map and AWS PrivateLink](vpc-interface-endpoints.md "vpc-interface-endpoints.md") | You can now use an AWS PrivateLink to create a private connection between your VPC and AWS Cloud Map. | September 15, 2023 |
| [Managed policy update](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSCloudMapDiscoverInstanceAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSCloudMapDiscoverInstanceAccess") | `AWSCloudMapDiscoverInstanceAccess` policy was updated. | August 15, 2023 |
| [AWS SDK for Python](registering-instances.md "registering-instances.md") | Added Python command line examples. | September 13, 2022 |
| [IPv6 support](registering-instances.md "registering-instances.md") | API endpoints are now available in `IPv6`-only networks. | January 28, 2022 |
| [Service instance discovery](creating-services.md "creating-services.md") | AWS Cloud Map added support for creating services in a namespace that supports DNS queries that are discoverable only using the [DiscoverInstances](https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html") API operation and not using DNS queries. | March 24, 2021 |
| [Resource tagging](using-tags.md "using-tags.md") | AWS Cloud Map added support for adding metadata tags to your namespaces and services using the AWS Management Console. | February 8, 2021 |
| [Resource tagging](using-tags.md "using-tags.md") | AWS Cloud Map added support for adding metadata tags to your namespaces and services using the AWS CLI and APIs. | June 22, 2020 |
| [Initial Release](../dg.md "../dg.md") | This is the first release of *AWS Cloud Map Developer Guide*.  | November 28, 2018 |
