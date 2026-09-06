

# Creating and managing integrations
<a name="zero-etl-creating-managing"></a>



## Creating an integration
<a name="zero-etl-creating"></a>

This section describes the general steps to create an integration. This example uses Amazon DynamoDB as a source.

1. On the AWS Glue console home page, select **Zero-ETL integrations**.

1. You can view all your integrations on the Zero ETL integration home page. To create a new integration, select **Create zero-ETL integration**.   
![The screenshot shows the main zero-ETL integration page.](http://docs.aws.amazon.com/glue/latest/dg/images/zero-etl-main.png)

1. You are prompted to select a **Source Type**. Select your source and click **Next**. Refer to the source configuration sections for SaaS integration sources.

1. In the **Configure source and target** page, select the tables or entities to replicate. For Amazon DynamoDB make sure the PITR and RBAC policy is configured.

1. Specify your integration target: 
   + For an AWS Glue Data Catalog target, select the AWS Glue database you want to replicate the data to.
   + For an Amazon Redshift data warehouse target, select the Redshift cluster namespace or Redshift Serverless workgroup namespace.

   For more information, see [Configuring the integration with your target](zero-etl-target.md#zero-etl-config-target-configuring-the-integration).

1. Provide the **Target IAM Role** that you created in the prerequisites.

1. If you want to configure an optional **Target KMS Key** for your data being stored in the target, provide an enabled KMS Key. Likewise, if you want to configure a target network connection, select an AWS Glue connection.

1. The **Fix Target** button configures some of the steps in the Prerequisite section of this documentation. Namely it will 1) provide a Catalog RBAC Policy and 2) if no Amazon S3 URI is provided it will generate one for you, otherwise it will use the provided URI.

1. In the **Output setting** section of the **Configure source and target** page, select a schema unnesting option that you want for your data in the target. If you want to use customer partition keys for your data, select **Specify custom partition keys** and provide up to 10 keys. Otherwise, you can simply use the partition keys that are assigned to your DynamoDB table being replicated.

1. In the **Security and data encryption** section, you can provide a KMS key that will be used in the intermediary process of replicating your data to the target. Otherwise, an AWS managed KMS key will be used. Enter a name for the Zero ETL integration in **Integration details**.

1. Review and make sure that all the provided details are correct. Click **Create and launch integration** once everything has been confirmed.

1. In the Zero ETL home page, you can select the integration you created and the details for your integrations will appear. The "Status" indicates the state of your integration.

## Modifying an integration
<a name="zero-etl-modifying"></a>

You can modify an existing integration.

1. Select **Edit** in the top right corner of your integration details page.

1. On the **Edit source and target** page you can change the Target IAM role and Target network connection. The other fields are not editable after integration creation. Click **Next**.

1. You can also edit the name and description of the integration in the **Edit integration and configuration** page. Click **Next**.

1. Review your edits and once confirmed, click **Update integration**.

## Deleting an integration
<a name="zero-etl-deleting"></a>

Delete is a terminal state for an integration. Once deleted, the integration cannot be revived. Deleting an integration clears up all internal metadata and any intermediate stored data.

During this process any running tasks which are writing data to a target table are terminated. AWS Glue will not delete or cleanup the target AWS Glue database (in the Data Catalog) and the associated data in the Amazon S3 bucket in your account. You need to explicitly clean those up if required.

To delete an integration:

1. In the integration details page, click **Delete**.

1. Enter "Delete" and click **Delete**. Note: This is an irreversible action.

1. In the integration details page, the status shows "Deleting". Once the integration is actually deleted, it will no longer appear on the Zero ETL integration home page.

## Integration states
<a name="zero-etl-integration-states"></a>

Integration goes through various states from creation to deletion:
+ `CREATING` - This is the first state when integration creation is initiated. In this state, AWS Glue does the initializations. This state should quickly move to CREATED state unless some configurations are missing.
+ `ACTIVE` - Once the integration reaches this state, AWS Glue will start the data transfer (initial full load). Unless there are permission issues, after the initial full load completes, periodic change data capture will follow.
+ `MODIFYING` - Once you make modification to the integration, the integration goes into Modifying state. Once the modification is applied, the integration goes to `ACTIVE` if integration was successful after the modification or will go into `NEEDS_ATTENTION` or `FAILED` if there were any issues.
+ `NEEDS_ATTENTION` - Integration will move into this state if there are either user error or system error. User error includes missing permissions, missing source or target resource(s), unsupported data errors. System error includes internal system errors. For both the error types, AWS Glue Zero ETL will keep retrying for data sync for 7 days before marking the integration as FAILED. If you fix the issue before that, the integration will become ACTIVE again and start transferring data.
+ `SYNCING` - Integration will move into this state if AWS Glue Zero ETL detects any data type changes in regards to incoming schema for columns within table/tables. In such cases AWS Glue Zero ETL will request fresh set of snapshots for all such tables. During this time the integration will be in SYNCING state and will eventually transition to ACTIVE state once newly requested snapshots are available for ingestion.
+ `FAILED` - This is a non-recoverable state. Once the integration moves into this state, it cannot be recovered. The only way to start the data transfer from source to target again is to delete and re-create the integration. If AWS Glue Zero ETL identifies that user error or system error has not been fixed for a period of 7 days and all retries are exhausted, AWS Glue Zero ETL will mark the integration as FAILED.
+ `DELETING` - When you invoke delete-integration API, AWS Glue first moves the integration into DELETING state. After all the metadata is cleared and internal processings are terminated, AWS Glue will move the integration into DELETED state.
+ `DELETED` - This is the terminal state for integration. Integration cannot be moved from this state into any other state. If the data transfer is required from same source to target, you should create the integration again.