# View, edit, or delete vended logs

dashboards

## View vended logs dashboards in CloudWatch Logs or

OpenSearch Service

To be able to view dashboards, you must be signed in to an IAM principal that
has the **CloudWatchOpenSearchDashboardAccess** IAM
policy.

###### To view vended log dashboards

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Logs Insights** and
   then choose the **Analyze with OpenSearch** tab.
3. Choose the dashboard in the **OpenSearch dashboards**
   box.
4. (Optional) In the upper right, choose **View in
   OpenSearch**.

The OpenSearch Service console opens and you see the same dashboard there. In the OpenSearch Service
console, you can make changes to the dashboard and its widgets, and these
changes will also be visible when you view the dashboard in CloudWatch Logs.

## Grant dashboard viewing access to

additional IAM roles or IAM users

To grant access to additional IAM principals after you've created the
integration, take the following steps.

###### To grant vended log dashboard access to additional IAM roles or

users

1. Edit the data access policy for the collection to add these roles or
   users. For more information, see [Data access control for Amazon OpenSearch Service Serverless](../../../opensearch-service/latest/developerguide/serverless-data-access.md "../../../opensearch-service/latest/developerguide/serverless-data-access.md") in the OpenSearch Service
   Developer Guide.
2. Grant the **CloudWatchOpenSearchDashboardAccess** to
   these users. For more information about the contents of this policy, see
   [CloudWatchOpenSearchDashboardAccess](iam-identity-based-access-control-cwl.md#managed-policies-cwl-CloudWatchOpenSearchDashboardAccess "iam-identity-based-access-control-cwl.md#managed-policies-cwl-CloudWatchOpenSearchDashboardAccess").

## Edit dashboard configuration

You can edit the name, description, and synchronization frequency of existing
vended log dashboards.

###### To edit a vended log dashboard

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Logs Insights** and
   then choose the **Analyze with OpenSearch** tab.
3. Choose the dashboard in the **OpenSearch dashboards**
   box.
4. Choose **Actions**, **Change dashboard
   details**.
5. Make your changes, then choose **Confirm
   changes**.

## Delete a vended log dashboard

You can delete a vended log dashboard. If you do so, the dashboard, the metrics,
and indexes created in the OpenSearch Service collection are all deleted.

###### Note

After you delete a vended log dashboard, wait at least six hours before trying
to re-create that same dashboard. If you don't wait, the re-created dashboard
won't work correctly.

###### To delete a vended log dashboard

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Logs Insights** and
   then choose the **Analyze with OpenSearch** tab.
3. Choose the dashboard in the **OpenSearch dashboards**
   box.
4. Choose **Actions**, **Delete**.
5. Confirm your decision by entering `delete`, then
   choose **Delete**.

## Delete all vended log

dashboard integration with OpenSearch Service

You can delete your entire OpenSearch integration. If you do, all vended logs
dashboards and the data that was displayed in them is deleted.

###### Important

To avoid ongoing costs, we strongly recommend that you manually delete the
following resources before you delete the integration. Deleting the integration
doesn't automatically delete these resources, and after you delete the
integration you won't be able to access these resources to delete them. To find
the names of the resources to delete, see the following procedure.

- [The data source](../../../opensearch-service/latest/developerguide/direct-query-s3-managing-data-sources.md#direct-query-s3-delete "../../../opensearch-service/latest/developerguide/direct-query-s3-managing-data-sources.md#direct-query-s3-delete")
- [The collection](../../../opensearch-service/latest/developerguide/serverless-manage.md#serverless-delete.html "../../../opensearch-service/latest/developerguide/serverless-manage.md#serverless-delete.html")
- [The data access policy](../../../opensearch-service/latest/developerguide/serverless-data-access.md#serverless-data-access-delete "../../../opensearch-service/latest/developerguide/serverless-data-access.md#serverless-data-access-delete")
- [The encryption policy](../../../opensearch-service/latest/developerguide/serverless-encryption.md#serverless-encryption-delete "../../../opensearch-service/latest/developerguide/serverless-encryption.md#serverless-encryption-delete")
- [The network policy](../../../opensearch-service/latest/developerguide/serverless-network.md#serverless-network-delete "../../../opensearch-service/latest/developerguide/serverless-network.md#serverless-network-delete")
- [The lifecycle policy](../../../opensearch-service/latest/developerguide/serverless-lifecycle.md#serverless-lifecycle-delete "../../../opensearch-service/latest/developerguide/serverless-lifecycle.md#serverless-lifecycle-delete")

###### To delete your entire vended log dashboard integration with OpenSearch Service

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Settings**.
3. Choose the **Logs** tab.
4. In the **OpenSearch integration** section, choose
   **Delete integration**.

The next screen displays the names of the OpenSearch Service resources that you should
delete before deleting the integration. 5. Confirm your decision by entering `delete`, then
choose **Delete integration**.
