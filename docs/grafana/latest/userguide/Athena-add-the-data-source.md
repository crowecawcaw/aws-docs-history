

# Manually adding the Athena data source
<a name="Athena-add-the-data-source"></a>

## Prerequisites
<a name="Athena-prerequisites2"></a>
+ The [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) is installed and configured in your environment.
+  You have access to **Amazon Athena** from your account.

**To manually add the Athena data source:**

1.  In the Grafana console side menu, pause on the **Configuration** (gear) icon, then choose **Data Sources**.

1. Choose **Add data source**.

1. Choose the **AWS Athena** data source. If necessary, you can start typing **Athena** in the search box to help you find it.

1.  In **Connection Details** menu, configure the authentication provider (recommended: **Workspace IAM Role**) 

1.  Select your targeted Athena data source, database, and workgroup.

   To create a new Athena account, follow the instructions at [Getting started with Athena](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html).

1.  If your workgroup doesn't have an output location configured already, specify an S3 bucket and folder to use for query results. For example, `s3://grafana-athena-plugin-test-data/query-result-output/ `. 

1.  Select **Save & Test**. 

The following is an example of the **Athena Details** settings.

![Athena Details example](http://docs.aws.amazon.com/grafana/latest/userguide/images/athena.png)
