# Managing connectors and connections

You use the **Connections** page in AWS Glue to manage your connectors and
connections.

###### Topics

- [Viewing connector and connection details](#connector-details "#connector-details")
- [Editing connectors and connections](#editing-connectors "#editing-connectors")
- [Deleting connectors and connections](#deleting-connectors "#deleting-connectors")
- [Cancel a subscription for a connector](#cancel-subscription "#cancel-subscription")

## Viewing connector and connection details

You can view summary information about your connectors and connections in the
**Your connectors** and **Your connections** resource
tables on the **Connectors** page. To view detailed information, perform
the following steps.

###### To view connector or connection details

1. In the AWS Glue Studio console, choose **Connectors** in the console
   navigation pane.
2. Choose the connector or connection that you want to view detailed information
   for.
3. Choose **Actions**, and then choose **View details**
   to open the detail page for that connector or connection.
4. On the detail page, you can choose to **Edit** or
   **Delete** the connector or connection.
   - For connectors, you can choose **Create connection** to create
     a new connection that uses the connector.
   - For connections, you can choose **Create job** to create a job
     that uses the connection.

## Editing connectors and connections

You use the **Connectors** page to change the information stored in
your connectors and connections.

###### To modify a connector or connection

1. In the AWS Glue Studio console, choose **Connectors** in the console
   navigation pane.
2. Choose the connector or connection that you want to change.
3. Choose **Actions**, and then choose
   **Edit**.

You can also choose **View details** and on the connector or
connection detail page, you can choose **Edit**. 4. On the **Edit connector** or **Edit connection**
page, update the information, and then choose **Save**.

## Deleting connectors and connections

You use the **Connectors** page to delete connectors and connections.
If you delete a connector, then any connections that were created for that connector should
also be deleted.

###### To remove connectors from AWS Glue Studio

1. In the AWS Glue Studio console, choose **Connectors** in the console navigation pane.
2. Choose the connector or connection you want to delete.
3. Choose **Actions**, and then choose
   **Delete**.

You can also choose **View details**, and on the connector or
connection detail page, you can choose **Delete**. 4. Verify that you want to remove the connector or connection by entering
`Delete`, and then choose **Delete**.

When deleting a connector, any connections that were created for that connector are
also deleted.

Any jobs that use a deleted connection will no longer work. You can either edit the jobs
to use a different data store, or remove the jobs.
For information about how to delete a job, see [Delete jobs](managing-jobs-chapter.md#delete-jobs "managing-jobs-chapter.md#delete-jobs").

If you delete a connector, this doesn't cancel the subscription for the connector in
AWS Marketplace. To remove a subscription for a deleted connector, follow the instructions in [Cancel a subscription for a connector](#cancel-subscription "#cancel-subscription") .

## Cancel a subscription for a connector

After you delete the connections and connector from AWS Glue Studio, you can cancel your subscription
in AWS Marketplace if you no longer need the connector.

###### Note

If you cancel your subscription to a connector, this does not remove the connector or
connection from your account. Any jobs that use the connector and related connections will
no longer be able to use the connector and will fail.

Before you unsubscribe or re-subscribe to a connector from AWS Marketplace, you should delete
existing connections and connectors associated with that AWS Marketplace product.

###### To unsubscribe from a connector in AWS Marketplace

1. Sign in to the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace "https://console.aws.amazon.com/marketplace").
2. Choose **Manage subscriptions**.
3. On the **Manage subscriptions** page, choose
   **Manage** next to the connector subscription that you want to
   cancel.
4. Choose **Actions** and then choose **Cancel
   subscription**.
5. Select the check box to acknowledge that running instances are charged to your
   account, and then choose **Yes, cancel
   subscription**.
