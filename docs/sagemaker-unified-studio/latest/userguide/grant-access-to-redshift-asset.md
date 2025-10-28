# Grant access to managed Amazon Redshift assets in

Amazon SageMaker Unified Studio

When a subscription to an Amazon Redshift table or view is approved, Amazon SageMaker Unified Studio can
automatically add the subscribed asset to the Amazon Redshift Serverless workgroup
created for the project, so that members of the project can query the data using the Amazon
Redshift query editor link within the project. Under the hood, Amazon SageMaker Unified Studio creates the necessary
grants and datashares.

The process of granting access varies depending on where the source database (publisher)
and the target database (subscriber) are located.

- Same cluster, same database - if data must be shared within the same database,
  Amazon SageMaker Unified Studio grants permissions directly on the source table.
- Same cluster, different database - if data must be shared across two databases within
  the same cluster, Amazon SageMaker Unified Studio creates a view in the target database and permissions are
  granted on the created view.
- Same account different cluster - Amazon SageMaker Unified Studio creates a datashare between the source and
  target cluster and creates a view on top of the shared table. Permissions are granted on
  the view.
- Cross-account - same as above but an additional step is required to authorize
  cross-account datashare on the producer cluster side and another step to associate the
  data share on consumer cluster side.
  Make sure that your publishing and subscribing Amazon Redshift clusters meet all
  requirements for Amazon Redshift datashares. For more information, see [Data sharing in
  Amazon Redshift](../../../redshift/latest/dg/datashare-overview.md "../../../redshift/latest/dg/datashare-overview.md") in the Amazon Redshift Developer Guide.

###### Note

Cross-Region data sharing using Amazon Redshift is not supported.
