

# Prerequisites
<a name="Redshift-prereq"></a>

To use the AWS managed policies for Amazon Managed Grafana, complete the following tasks before you configure the Amazon Redshift data source:
+ Tag your Amazon Redshift cluster with `GrafanaDataSource: true`. Otherwise, it won't be accessible.
+ Create the database credentials in one of the following mutually exclusive ways:
  + If you want to use the default mechanism (the temporary credentials options) to authenticate against the Redshift database, you must create a database user named `redshift_data_api_user`.
  + If you want to use the credentials from Secrets Manager, you must tag the secret with `RedshiftQueryOwner: true`. For more information, see [Identity-based policy examples in Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/security_iam_id-based-policy-examples.html)in this guide.