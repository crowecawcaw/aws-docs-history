# Grant access to managed Amazon Redshift

assets in Amazon DataZone

When a subscription to an Amazon Redshift table or view is approved, Amazon DataZone can
automatically add the subscribed asset to all the data warehouse environments within the
project, so that members of the project can query the data using the Amazon Redshift
query editor link within their environments. Under the hood, Amazon DataZone, creates the
necessary grants and datashares between the source and the subscription target.

The process of granting access varies depending on where the source database
(publisher) and the target database (subscriber) are located.

- Same cluster, same database - if data must be shared within the same database,
  Amazon DataZone grants permissions directly on the source table.
- Same cluster, different database - if data must be shared across two databases
  within the same cluster, Amazon DataZone creates a view in the target database and
  permissions are granted on the created view.
- Same account different cluster - Amazon DataZone creates a datashare between the
  source and target cluster and creates a view on top of the shared table.
  Permissions are granted on the view.
- Cross-account - same as above but an additional step is required to authorize
  cross-account datashare on the producer cluster side and another step to
  associate the data share on consumer cluster side.

###### Note

If a new data warehouse environment is added to the project after the subscribed
Amazon Redshift assets have been automatically added to the existing data warehouse
environments, you have to manually add these subscribed Amazon Redshift assets to
this new data warehouse environment. You can do this by choosing the **Add
grant** option in the **Data** tab of the project's
overview page in the Amazon DataZone data portal.

Make sure that your publishing and subscribing Amazon Redshift clusters meet all
requirements for Amazon Redshift datashares. For more information, see [Amazon Redshift
Developer Guide](../../../redshift/latest/dg/welcome.md "../../../redshift/latest/dg/welcome.md").

###### Note

Amazon DataZone supports automatically granting subscriptions to both Amazon Redshift
Cluster and Amazon Redshift Serverless assets.

Cross-Region data sharing using Amazon Redshift is not supported.
