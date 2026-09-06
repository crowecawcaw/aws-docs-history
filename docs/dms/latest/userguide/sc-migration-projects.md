

# Managing migration projects in DMS Schema Conversion
<a name="sc-migration-projects"></a>

After you create an instance profile and compatible data providers for schema conversion, create a migration project. For more information, see [ Creating migration projects](migration-projects-create.md).

To use this new project in DMS Schema Conversion, on the **Migration projects** page, choose your project from the list. Next, on the **Schema conversion** tab, choose **Launch schema conversion**.

The first launch of DMS Schema Conversion requires some setup. AWS Database Migration Service (AWS DMS) starts a schema conversion instance, which takes up to five minutes. This process also reads the metadata from the source and target databases. After a successful first launch, you can access DMS Schema Conversion faster.

Amazon terminates the schema conversion instance that your migration project uses in three days after you complete the project. You can retrieve your converted schema and assessment report from the Amazon S3 bucket that you use for DMS Schema Conversion.

## Specifying migration project settings for DMS Schema Conversion
<a name="migration-projects-settings"></a>

After you create your migration project and launch schema conversion, you can specify migration project settings. You can change conversion settings to improve the performance of converted code, and you can customize the schema conversion view with tree view settings.

For information about the common conversion settings, the tree view settings, and the settings for each conversion path, see [Specifying schema conversion settings for migration projects](schema-conversion-settings.md).

## Access logs for AWS DMS Schema Conversion
<a name="migration-projects-logs"></a>

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/](https://console.aws.amazon.com/dms/).

1. Choose **Migration projects**. The **Migration projects** page opens.

1. Choose your migration project, and on the **Overview** tab copy migration project id from the **ARN** field.  
![This an image showing how to get the ARN ID from the AWS DMS console.](http://docs.aws.amazon.com/dms/latest/userguide/images/dms-schema-conversion-log.png)

1. Open **CloudWatch** service.

1. Choose **Log groups** and enter `dms-tasks-sct-{migration_project_id}` where `{migration_project_id}` is the `id` from Step 3.

1. Inside the **Log group** you can find **Log stream** with logs.