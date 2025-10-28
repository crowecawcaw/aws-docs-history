# Managing query access for Security Lake

subscribers

Subscribers with query access can query data that Security Lake collects. These subscribers
directly query AWS Lake Formation tables in your S3 bucket with services like Amazon Athena. Although the
primary query engine for Security Lake is Athena you can also use other services, such as [Amazon Redshift
Spectrum](../../../redshift/latest/dg/c-getting-started-using-spectrum.md "../../../redshift/latest/dg/c-getting-started-using-spectrum.md") and Spark SQL, that integrate with the AWS Glue Data Catalog.

Subscribers query source
data from AWS Lake Formation tables in your S3 bucket by using services like Amazon Athena. This
subscription type is identified as `LAKEFORMATION` in the
`accessTypes` parameter of the [CreateSubscriber](../APIReference/API_CreateSubscriber.md "../APIReference/API_CreateSubscriber.md") API.

###### Note

This section explains how to grant query access to a third-party subscriber. For
information about running queries against your own data lake, see [Step 4: View and query your own data](get-started-console.md#explore-data-lake "get-started-console.md#explore-data-lake").

###### Topics

- [Prerequisites](prereqs-query-subscriber.md "prereqs-query-subscriber.md")
- [Creating a subscriber with query access](create-query-subscriber-procedures.md "create-query-subscriber-procedures.md")
- [Editing a subscriber with query access](editing-query-access-subscriber.md "editing-query-access-subscriber.md")
