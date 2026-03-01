# Managing Amazon Q Business data sources

To manage data source connectors, you can perform the following actions:

###### Actions

- [Deleting an Amazon Q Business data source connector](#delete-datasource "#delete-datasource")
- [Getting properties of an Amazon Q Business data source connector](#describe-datasource "#describe-datasource")
- [Listing Amazon Q Business data source connectors](#list-datasources "#list-datasources")
- [Updating Amazon Q Business data source connectors](#update-datasources "#update-datasources")
- [Starting data source connector sync jobs](#start-datasource-sync-jobs "#start-datasource-sync-jobs")
- [Stopping data source connector sync jobs](#end-datasource-sync-jobs "#end-datasource-sync-jobs")
- [Listing data source connector sync jobs](#list-datasource-sync-jobs "#list-datasource-sync-jobs")

## Deleting an Amazon Q Business data source connector

To delete an Amazon Q Business data source connector, you can use the
console or the [DeleteDataSource](../api-reference/API_DeleteDataSource.md "../api-reference/API_DeleteDataSource.md") API operation
.

The following tabs provide a procedure for the AWS Management Console and code examples for
the AWS CLI.

Console
**To delete an Amazon Q Business data
source connector**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the
   application environment that you want to delete data sources from.
3. From the left navigation menu, select **Data
   sources**.
4. From the **Data sources** list, select
   the data source you want to delete.
5. From **Actions**, choose
   **Delete**.
6. In the dialog box that opens, type
   `Delete` to confirm deletion, and
   then choose **Delete**.

You are returned to the service console while your data
source connector is deleted. When the deletion process is
complete, the console displays a message confirming
successful deletion.

AWS CLI
**To delete an Amazon Q Business data
source connector**

```

aws qbusiness delete-data-source \
--application-id `application-id` \
--index-id `index-id` \
--data-source-id `data-source-id`

```

## Getting properties of an Amazon Q Business data source connector

To get the properties of an Amazon Q Business data source connector, you
can use the [GetDataSource](../api-reference/API_GetDataSource.md "../api-reference/API_GetDataSource.md") API
operation.

The following tabs provide a procedure for the AWS Management Console and code examples for
the AWS CLI.

Console
**To get properties of an Amazon Q Business data source connector**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the
   application environment you want that contains your data sources.
3. From the left navigation menu, select **Data
   sources**.
4. From the **Data sources** list, select
   the data source that you want to view details for.
5. Under **Data source details**, the
   following details are available:
   - **Name** – The name of
     your data source.
   - **Status** – The status of
     your data source.
   - **Last sync status** – The
     status of your last sync.
   - **Description** – The
     description that you gave to your data source.
   - **Type** – The type of
     data source that you're using.
   - **Last sync time** – The
     time that your data source was last synced.
   - **Data source ID** – The
     ID of your data source.
   - **IAM role ARN**
     – The Amazon Resource Name (ARN) of the
     IAM role that's associated with
     your data source.
   - **Current sync state** –
     The current sync state of your data source.

**To get Amazon Q Business data source
connector settings**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the
   application environment you want that contains your data sources.
3. From the left navigation menu, select **Data
   sources**.
4. From the **Data sources** list, select
   the data source you want to delete.
5. For **Data source details**, choose
   **Settings**.
6. For **Settings**, the following settings
   are available:
   - **IAM role**
     – The ARN of the IAM that's
     associated with your data source.
   - **Sync scope** – The
     configuration details for your data source.
   - **Sync mode** – The sync
     type that you chose for your data source.
   - **Sync schedule** – The
     sync schedule that you chose for your data source.
   - **Field mappings** – The
     data source document fields that you chose to map to
     Amazon Q Business index fields.

AWS CLI
**To get Amazon Q Business data source
connector properties**

```

aws qbusiness get-data-source \
--application-id `application-id` \
--index-id `index-id` \
--data-source-id `data-source-id`

```

## Listing Amazon Q Business data source connectors

To list Amazon Q Business data source connectors, you can use the
console or the [ListDataSources](../api-reference/API_ListDataSources.md "../api-reference/API_ListDataSources.md") API
operation.

The following tabs provide a procedure for the AWS Management Console and code examples for
the AWS CLI.

Console
**To list Amazon Q Business data source
connectors**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the
   application environment you want that contains your data sources.
3. From the left navigation menu, select **Data
   sources**.
4. On the **Data sources**, under
   **Data sources**, a list of data
   sources connected to your application environment is displayed.

AWS CLI
**To list Amazon Q Business data source
connectors**

```

aws qbusiness list-data-sources \
--application-id `application-id` \
--index-id `index-id` \
--max-results `maximum-number-of-results-to-return`

```

## Updating Amazon Q Business data source connectors

To update your Amazon Q Business data source connectors, you can use the
console or the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") API
operation.

The following tabs provide a procedure for the AWS Management Console and code examples for
the AWS CLI.

Console
**To update a Amazon Q Business data
source connector**

###### Option 1

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the
   application environment you want to delete data sources from.
3. From the left navigation menu, select **Data
   sources**.
4. On the application page, from **Data
   sources**, select the data source that you want
   to edit.
5. From **Actions**, choose
   **Edit**.

You are redirected to your data source configuration page
to edit your existing settings.

###### Option 2

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the
   application environment you want to delete data sources from.
3. On the application page, from **Data
   sources**, select the data source that you want
   to edit.
4. On the data source page, from
   **Actions**, choose
   **Edit**.

You are redirected to your data source configuration page
to edit your existing settings.

CLI
**To update your Amazon Q Business
connector**

```

aws qbusiness update-data-source \
--application-id `application-id` \
--data-source-id `data-source-id` \
--index-id `index-id` \
--configuration `data-source-configuration-details` \
--description `description` \
--display-name `display-name` \
--document-enrichment-configuration `document-enrichment-configuration` \
--role-arn `roleArn` \
--sync-schedule `sync-schedule-information` \
--vpc-configuration `vpc-configuration`

```

## Starting data source connector sync jobs

To start Amazon Q Business data source connector sync jobs, you can use
the console or the [StartDataSourceSyncJobs](../api-reference/API_StartDataSourceSyncJobs.md "../api-reference/API_StartDataSourceSyncJobs.md") API
operation.

The following tabs provide a procedure for the AWS Management Console and code examples for
the AWS CLI.

Console
**To start your Amazon Q Business data
source connector sync jobs**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the
   application environment you want to sync data sources in.
3. On the application page, from **Data
   sources**, select the data source that you want
   to sync.
4. Choose **Sync now**.

The console displays a message confirming that your sync
job has started successfully.

###### Note

You can also view your sync job report in the Amazon CloudWatch
console.

AWS CLI
**To start your Amazon Q Business data
source connector sync jobs**

```

aws qbusiness start-data-source-sync-job \
--application-id `application-id` \
--index-id `index-id` \
--data-source-id `data-source-id`

```

## Stopping data source connector sync jobs

To stop your Amazon Q Business connector sync jobs, you can use the
console or the [StopDataSourceSyncJobs](../api-reference/API_StopDataSourceSyncJobs.md "../api-reference/API_StopDataSourceSyncJobs.md") API
operation.

###### Note

You can only stop a sync job already in progress.

The following tabs provide a procedure for the AWS Management Console and code examples for
the AWS CLI.

Console
**To stop your Amazon Q Business data
source connector sync jobs**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the
   application environment you want to sync data sources in.
3. On the application page, from **Data
   sources**, select the data source that you want
   to stop the sync for.
4. Choose **Stop sync**.
5. In the dialog box that opens , type
   `Stop` to confirm your action and
   then select **Stop sync**.

The console displays a message confirming that your data
source sync job is being stopped.

AWS CLI
**To stop your Amazon Q Business data
source connector sync jobs**

```

aws qbusiness stop-data-source-sync-job \
--application-id `application-id` \
--data-source-id `data-source-id` \
--index-id `index-id`

```

## Listing data source connector sync jobs

To list Amazon Q Business data source connector sync jobs that are in
progress, you can use the console or the [ListDataSourceSyncJobs](../api-reference/API_ListDataSourceSyncJobs.md "../api-reference/API_ListDataSourceSyncJobs.md") API
operation.

The following tabs provide a procedure for the AWS Management Console and code examples for
the AWS CLI.

Console
**To list your Amazon Q Business data
source connector sync jobs**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the
   application environment you want that contains your data sources.
3. On the application page, from **Data
   sources**, select the data source that you want
   to view details for.
4. Under **Data source details**, choose the
   **Sync run history** tab.

You will see a list of ongoing, completed, and failed sync
jobs for your data sources.

CLI
**To list your Amazon Q Business data
source connector sync jobs**

```

aws qbusiness list-data-source-sync-job \
--application-id `application-id` \
--data-source-id `data-source-id` \
--index-id `index-id` \
--max-results `max-results-to-return`

```
