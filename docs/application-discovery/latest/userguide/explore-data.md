AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Exploring data in Amazon Athena

Data exploration in Amazon Athena allows you to analyze the data that's collected from all the
discovered on-premises servers by Discovery Agent in one place. Once Data exploration in Amazon Athena
is enabled from the Migration Hub console (or by using the StartContinousExport API) and the data
collection for agents is turned on, data that's collected by agents is automatically get
stored in your S3 bucket at regular intervals. For more information, see Exploring data in Amazon Athena.

Data exploration in Amazon Athena allows you to analyze the data that's collected from all the
discovered on-premises servers by Discovery Agents in one place. Once data exploration in Amazon Athena
is enabled from the Migration Hub console (or by using the StartContinousExport API) and the data
collection for agents is turned on, data that's collected by agents is automatically get
stored in your S3 bucket at regular intervals.

You can then visit Amazon Athena to run pre-defined queries to analyze the time-series system
performance for each server, the type of processes that are running on each server and the
network dependencies between different servers. In addition, you can write your own custom
queries using Amazon Athena, upload additional existing data sources such as configuration
management database (CMDB) exports, and associate the discovered servers with the actual
business applications. You can also integrate the Athena database with Amazon Quick Suite to visualize
the query outputs and perform additional analysis.

The topics in this section describe the ways that you can work with your data in Athena to
assess and plan for migrating your local environment to AWS.
