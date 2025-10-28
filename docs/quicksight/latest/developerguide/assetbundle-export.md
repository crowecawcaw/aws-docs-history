# Asset bundle export operations

Quick Sight developers can use asset bundle export operations to export existing Quick Sight assets and download their definitions to be saved in your own storage.
Quick Sight doesn't export data contained within the asset. These exported assets can be imported back into Quick Sight whenever you want. To
export Quick Sight assets, start a named asynchronous export job. Then, poll for the job's completion, and then download the asset bundle with the download URL that's provided by the Quick Sight API.

Assets that are exported with the Quick Sight asset bundle APIs can be exported as a Quick Sight JSON bundle or a CloudFormation JSON file.

When you run an export job that generates a Quick Sight JSON file, the job returns a `.qs` zip file. The file can be unzipped to access the exported asset definitions.

Use the following sections to learn more about the asset bundle export API operations.

## StartAssetBundleExportJob

Export jobs are configured with the `StartAssetBundleExportJobRequest` object.

Export jobs are identified by an `AssetBundleExportJobId` that you provide when you create the new export job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.

Export jobs include a list of Quick Sight asset ARNs to be exported. You can choose to have all dependencies of the specified asset ARNs to be exported automatically with the rest of the job. For example, if you're creating a job to export a Quick Sight dashboard, you can also choose to export the dashboard's theme, dataset, and data source.

Developers can also choose to have all assets in a folder and its subfolders exported automatically to preserve folder hierarchy and folder memberships. Parent folders are considered to be dependencies of subfolders and are included in the export if the `IncludeAllDependencies` parameter is set to `True`. Assets in a folder are considered folder members and are included in the export if the `IncludeFolderMembers` parameter is set to `ONE_LEVEL/RECURSE`. When assets are exported directly, folder membership information can be preserved when the `IncludeFolderMemberships` parameter is set to `True`. To include the folder in the direct export, set `IncludeAllDependencies` to `True`.

All export jobs run asynchronously after they are started. Poll the status of an export job with a `DescribeAssetBundleExportJob` call to know is the current status of the job. Callers must have read-only permissions for all of the resource types that are exported, including the optional dependencies that are included in the export job.

In some cases, certain Quick Sight assets contain anomalies that don't impact the end user's experience. By default, the `StartAssetBundleExportJob` API operates in `Lenient` mode, which ignores these anomalies. Callers can choose to enforce stricter validations with `Strict` mode during export. To do so, set the value of the optional `StrictModeForAllResources` parameter to `"True”`. The `StartAssetBundleImportJob` API operation follows the validation strategy that is defined in the exported bundle. To import an existing bundle with `Lenient` mode, run a new export job with the optional `StrictModeForAllResources` parameter set to `"False"`.

For more information about the `StartAssetBundleExportJob` operation, see [StartAssetBundleExportJob](../APIReference/API_StartAssetBundleExportJob.md "../APIReference/API_StartAssetBundleExportJob.md") in the _Quick Sight API Reference_.

## DescribeAssetBundleExportJob

Use the `DescribeAssetBundleExportJob` operation to obtain the current status of an existing export job that's up to 14 days old. You can also use this operation to review a specified job's configuration.

Export jobs that have succeeded return a download URL for the asset bundle file in their description. Failed export jobs return error information in their description. Poll this operation until the export job that you want the status of has succeeded or failed.

For more information about the `DescribeAssetBundleExportJob` operation, see [DescribeAssetBundleExportJob](../APIReference/API_DescribeAssetBundleExportJob.md "../APIReference/API_DescribeAssetBundleExportJob.md") in the _Quick Sight API Reference_.

## ListAssetBundleExportJobs

Use the `ListAssetBundleExportJobs` operation to retrieve a list of all export jobs that were created in the last 14 days. Export jobs are listed in the order that they were started, starting with the most recently started job. To have multiple lists by this operation, you can choose to specify a maximum page size to be returned and use a pagination token.

For more information about the `ListAssetBundleImportJobs` operation, see [ListAssetBundleExportJobs](../APIReference/API_ListAssetBundleExportJobs.md "../APIReference/API_ListAssetBundleExportJobs.md") in the _Quick Sight API Reference_.

## Examples

The following example uses a `StartAssetBundleExportJob` API call to create a CloudFormation JSON file with override parameters.

```
# configure and start the export job
aws quicksight start-asset-bundle-export-job
--aws-account-id `AWSACCOUNTID` \
--asset-bundle-export-job-id `JOBID` \
--resource-arns '["arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:dashboard/`RESOURCEID`","arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:analysis/`RESOURCEID`"]' \
--cloud-formation-override-property-configuration '{"Dashboards": [{"Arn": "arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:dashboard/`RESOURCEID`","Properties": ["Name"]}]}' \
--include-all-dependencies \
--export-format CLOUDFORMATION_JSON

# poll job description until status is success
aws quicksight describe-asset-bundle-export-job
--aws-account-id `AWSACCOUNTID` \
--asset-bundle-export-job-id `JOBID`

# download the provided bundle (wget used here - any tool or browser works as well)
wget -O `~/qs-bundle.qs` '`https://the-long-url-from-your-job-description...`'
```

The following example uses a `StartAssetBundleExportJob` API call to create a Quick Sight asset bundle file.

```
# configure and start the export job
aws quicksight start-asset-bundle-export-job
--aws-account-id `AWSACCOUNTID` \
--asset-bundle-export-job-id `JOBID` \
--resource-arns '["arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:dashboard/`RESOURCEID`","arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:analysis/`RESOURCEID`"]' \
--include-all-dependencies \
--export-format QUICKSIGHT_JSON

# poll job description until status is success
aws quicksight describe-asset-bundle-export-job
--aws-account-id `AWSACCOUNTID` \
--asset-bundle-export-job-id `JOBID`

# download the provided bundle (wget used here - any tool or browser works as well)
wget -O `~/qs-bundle.qs` '`https://the-long-url-from-your-job-description...`'
```

The following example uses a `StartAssetBundleExportJob` API call to include information for tags. By default, tag information is not exported.

```
# Export in QuickSight format
aws quicksight start-asset-bundle-export-job
--aws-account-id `AWSACCOUNTID` \
--asset-bundle-export-job-id `JOBID` \
--resource-arns '["arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:dashboard/`RESOURCEID`","arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:analysis/`RESOURCEID`"]' \
--include-all-dependencies \
--include-tags \
--export-format QUICKSIGHT_JSON

# Export in CloudFormation format, with optional tags overrides
aws quicksight start-asset-bundle-export-job
--aws-account-id `AWSACCOUNTID` \
--asset-bundle-export-job-id `JOBID` \
--resource-arns '["arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:dashboard/`RESOURCEID`","arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:analysis/`RESOURCEID`"]' \
--include-all-dependencies \
--include-tags \
--export-format CLOUDFORMATION_JSON
```

The following example uses a `StartAssetBundleExportJob` API call to include permissions information. By default, permission information is not exported. Permission overrides are not supported for the AWS CloudFormation format. To import permissions for a AWS CloudFormation format file, make sure that the source and target accounts are the same or have the same principal names for users, groups, and namespaces.

```
# Export in QuickSight format
aws quicksight start-asset-bundle-export-job
--aws-account-id `AWSACCOUNTID` \
--asset-bundle-export-job-id `JOBID` \
--resource-arns '["arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:dashboard/`RESOURCEID`","arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:analysis/`RESOURCEID`"]' \
--include-all-dependencies \
--include-permissions \
--export-format QUICKSIGHT_JSON


# Export in CloudFormation format
aws quicksight start-asset-bundle-export-job
--aws-account-id `AWSACCOUNTID` \
--asset-bundle-export-job-id `JOBID` \
--resource-arns '["arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:dashboard/`RESOURCEID`","arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:analysis/`RESOURCEID`"]' \
--include-all-dependencies \
--include-permissions \
--export-format CLOUDFORMATION_JSON
```

The following example recusrively exports a folder along with all subfolders and the parent folder tree.

```
aws quicksight start-asset-bundle-export-job
--aws-account-id `AWSACCOUNTID` \
--asset-bundle-export-job-id `JOBID` \
--resource-arns '["arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:folder/`RESOURCEID`"]' \
--include-all-dependencies \
--include-folder-members RECURSE \
--export-format QUICKSIGHT_JSON"
```

The following example runs a dashboard export job that preserves the dashboard's folder memberships.

```
aws quicksight start-asset-bundle-export-job
--aws-account-id `AWSACCOUNTID` \
--asset-bundle-export-job-id `JOBID` \
--resource-arns '["arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:dashboard/`RESOURCEID`"]' \
--include-folder-memberships \
--export-format QUICKSIGHT_JSON
```

The following example calls the `StartAssetBundleExportJob` API with `Strict` mode.

```
aws quicksight start-asset-bundle-export-job
--aws-account-id `AWSACCOUNTID` \
--asset-bundle-export-job-id `JOBID` \
--resource-arns '["arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:dashboard/`RESOURCEID`","arn:aws:quicksight:`REGION`:`AWSACCOUNTID`:analysis/`RESOURCEID`"]' \
--include-all-dependencies \
--export-format QUICKSIGHT_JSON
```
