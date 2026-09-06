

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Document History for AWS Application Discovery Service
<a name="doc-history"></a>

**Latest User Guide documentation update**: May 16, 2023

The following table describes important changes to the *Application Discovery Service User Guide* after January 18, 2019. For notifications about documentation updates, you can subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Maintenance mode](#doc-history) | AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html). | November 7, 2025 | 
| [Transition from Discovery Connector to Agentless Collector](#doc-history) | We recommend that customers who are currently using Discovery Connector transition to the new Agentless Collector. Starting November 17, 2025, AWS Application Discovery Service will stop accepting new data from Discovery Connectors. For more information, see [Discovery Connector](https://docs.aws.amazon.com/application-discovery/latest/userguide/appendix.html).  | November 12, 2024 | 
| [Released the Agentless Collector Network Data Collection module](#doc-history) | The Network Data Collection module makes it possible for you to discover dependencies among servers in your on-premises data center. For more information, see [Using the Agentless Collector Network Data Collection module](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-network-data-collection.html).  | November 8, 2024 | 
| [Support for agentless collection for dependency mapping](#doc-history) | For more information, see [Using the VMware vCenter Agentless Collector data collection module](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-data-collection-vcenter.html).  | October 24, 2024 | 
| [Released Agentless Collector version 2 based on Amazon Linux 2023](#doc-history) | For more information, see [Prerequisites for Agentless Collector](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-prerequisites.html).  | September 26, 2024 | 
| [Updated Agentless Collector prerequisites](#doc-history) | For more information, see [Prerequisites for Agentless Collector](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-prerequisites.html).  | September 9, 2024 | 
| [Eventual consistency in the API](#doc-history) | For more information, see [Eventual consistency in the AWS Application Discovery Service API ](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#eventual-consistency).  | June 20, 2024 | 
| [Agentless Collector updates](#doc-history) | We added `sts.amazonaws.com` to the lists of domains that require outbound access. For more information, see [Configure firewall for outbound access to AWS domains ](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-prerequisites.html#agentless-collector-gs-prerequisites-firewall).  | June 20, 2024 | 
| [To separate access, create and use separate AWS accounts.](#doc-history) | For more information, see [Actions, resources, and condition keys for AWS Application Discovery Service ](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationdiscoveryservice.html).  | April 5, 2024 | 
| [Introducing the Agentless Collector database and analytics data collection module](#doc-history) | The database and analytics data collection module is the new module of Application Discovery Service Agentless Collector (Agentless Collector). You can use this data collection module to connect to your environment and collect metadata and performance metrics from your on-premises database and analytics servers. For more information, see [Database and analytics data collection module](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-database-analytics-collection.html).  | May 16, 2023 | 
| [Introducing Application Discovery Service Agentless Collector](#doc-history) | Application Discovery Service Agentless Collector (Agentless Collector) is the new AWS Application Discovery Service on-premises application that collects information through agentless methods about your on-premises environment to help you effectively plan your migration to the AWS Cloud. For more information, see [Agentless Collector](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector.html).  | August 16, 2022 | 
| [IAM update](#doc-history) | The AWS Identity and Access Management (IAM) `discovery:GetNetworkConnectionGraph` action is now available for granting access to the AWS Migration Hub console network diagram when creating an identity-based policy. For more information, see [Granting permissions to use the network diagram](https://docs.aws.amazon.com/application-discovery/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-network-connection-graph).  | May 24, 2022 | 
| [Introducing the home Region](#doc-history) | The Migration Hub home Region provides a single repository of discovery and migration planning information for your entire portfolio, and a single view of migrations into multiple AWS Regions. | November 20, 2019 | 
| [Introducing the Migration Hub import feature](#doc-history) | Migration Hub import allows you to import information about your on-premises servers and applications into Migration Hub, including server specifications and utilization data. You can also use this data to track the status of application migrations. For more information, see [Migration Hub Import](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html). | January 18, 2019 | 

The following table describes documentation releases for the *Application Discovery Service User Guide* before January 18, 2019:



| Change | Description | Date | 
| --- | --- | --- | 
| New Feature | Updated docs to support data exploration in Amazon Athena and added Troubleshooting chapter. | August 09, 2018 | 
| Major revision | Rewrites to usage & output details; entire document restructured. | May 25, 2018 | 
| Discovery Agent 2.0 | A new and improved Application Discovery agent was released. | October 19, 2017 | 
| Console | The AWS Management Console was added. | December 19, 2016 | 
| Agentless discovery | This release describes how to set up and configure agentless discovery. | July 28, 2016 | 
| New details for Microsoft Windows Server and command issue fixes | This update adds details about Microsoft Windows Server. It also documents fixes to various command issues. | May 20, 2016 | 
| Initial publication | This is the first release of the Application Discovery Service User Guide. | May 12, 2016 | 