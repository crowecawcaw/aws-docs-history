

# Migrating saved objects from OpenSearch Dashboards to OpenSearch UI
<a name="application-migration"></a>

If you have existing dashboards, visualizations, index patterns, and other saved objects in OpenSearch Dashboards, you can migrate and reuse them in OpenSearch UI.

Benefits of migrating to OpenSearch UI:
+ **High availability** – OpenSearch UI is hosted in the AWS Cloud and remains available during domain upgrades and maintenance, while OpenSearch Dashboards is hosted within the domain and will be temporarily unavailable.
+ **Multiple Data Source** – OpenSearch UI can provide a consolidated single pane of glass across multiple data sources, including OpenSearch domains, serverless collections, and data connections with Amazon S3 and Amazon CloudWatch; while each OpenSearch Dashboards can only work with one domain or collection.
+ **Additional features** – AI Assistant and Workspaces are available on OpenSearch UI. For more information about OpenSearch UI, see [Using OpenSearch UI in Amazon OpenSearch Service](application.md).

**Topics**
+ [Migration overview](#application-migrate-saved-objects-overview)
+ [Prerequisites](#application-migrate-saved-objects-prerequisites)
+ [Step 1: Export saved objects from OpenSearch Dashboards](#application-migrate-saved-objects-export)
+ [Step 2: Import saved objects into OpenSearch UI](#application-migrate-saved-objects-import)
+ [Using the in-app migration tool](#application-migration-in-app)
+ [Migration scenarios for OpenSearch UI](application-migration-scenarios.md)

## Migration overview
<a name="application-migrate-saved-objects-overview"></a>

The migration process consists of the following high-level steps:

1. **Export saved objects from OpenSearch Dashboards** – Use the OpenSearch Dashboards Saved Objects management UI or the export API to download your dashboards, visualizations, index patterns, and other objects as a newline-delimited JSON (NDJSON) file.

1. **Create an OpenSearch UI application and workspace** – If you have not already done so, create an OpenSearch UI application and a workspace to receive the imported objects.

1. **Register the data source in OpenSearch UI** – Associate your OpenSearch domain with the OpenSearch UI application and register it as a data source within the workspace. Index patterns in your imported objects reference this data source.

1. **Import saved objects into OpenSearch UI** – Use the OpenSearch UI Saved Objects management UI or the import API to upload the NDJSON file into the target workspace.

1. **Validate the imported objects** – Open your dashboards and visualizations in OpenSearch UI to verify that they display correctly and that data is flowing from the associated domain or collection.

## Prerequisites
<a name="application-migrate-saved-objects-prerequisites"></a>

Before the migration, verify the following prerequisites:
+ You have the necessary IAM permissions required to call the Amazon OpenSearch Service and OpenSearch APIs. For more information, see [Required permissions for creating Amazon OpenSearch Service applications](application-getting-started.md#application-prerequisite-permissions).
+ You can access the domain or collection and the OpenSearch Dashboards that you want to migrate.
+ You have created an OpenSearch UI application. For information about creating an application and workspace, see [Getting started with the OpenSearch user interface in Amazon OpenSearch Service](application-getting-started.md).
+ You have associated the same domain or collection to the OpenSearch UI application. For information about associating data sources, see [Managing data source associations and Virtual Private Cloud access permissions](application-data-sources-and-vpc.md).

**Note**  
OpenSearch UI only supports OpenSearch version 1.3 and later. Verify that your OpenSearch domain is running version 1.3 or higher before attempting to migrate saved objects.

## Step 1: Export saved objects from OpenSearch Dashboards
<a name="application-migrate-saved-objects-export"></a>

Export your saved objects from OpenSearch Dashboards using the management UI or the export API. The export produces a newline-delimited JSON (NDJSON) file that contains all selected saved object types and their dependencies.

**Topics**
+ [Manually export on OpenSearch Dashboards](#application-migrate-export-console)
+ [Exporting via API](#application-migrate-export-api)

### Manually export on OpenSearch Dashboards
<a name="application-migrate-export-console"></a>

**To export saved objects using the OpenSearch Dashboards management UI**

1. Open your OpenSearch Dashboards instance.

1. In the left navigation panel, choose **Management**.

1. Under **Dashboards Management**, choose **Saved Objects**.

1. Select the saved objects you want to export. To export all objects of a specific type, filter by type using the search bar. To export all objects, select the check box in the table header.

1. Choose **Export**.

1. In the **Export saved objects** dialog box, ensure that **Include related objects** is selected. This option includes all objects that the selected saved objects depend on, such as index patterns referenced by visualizations. Clear this option only if you intend to manage dependencies manually.

1. Choose **Export** to download the `.ndjson` file to your local machine.

**Tip**  
When you choose **Include related objects**, the exported NDJSON file contains all the saved objects needed to render the selected dashboards and visualizations, including their dependent index patterns, visualizations, and search objects. This simplifies the import step and avoids missing reference errors.

### Exporting via API
<a name="application-migrate-export-api"></a>

You can use the OpenSearch Dashboards Saved Objects export API to programmatically export saved objects. This is useful for automating migrations or integrating the export step into a CI/CD pipeline.

**Note**  
If your OpenSearch domain has [fine-grained access control](fgac.md) enabled, you must provide authentication credentials with your export request. Use HTTP basic authentication by adding the `-u` flag with your username and password. For more information about authentication options, see [Fine-grained access control in Amazon OpenSearch Service](fgac.md).

The following example exports all dashboards with their related objects. Replace the {{placeholder values}} with your own information.

```
curl -X POST \
    "https://{{dashboards-endpoint}}/_dashboards/api/saved_objects/_export" \
    -u '{{master-username}}:{{master-password}}' \
    -H "Content-Type: application/json" \
    -H "osd-xsrf: true" \
    -d '{
        "type": ["dashboard", "visualization", "index-pattern", "search"],
        "includeReferencesDeep": true,
        "excludeExportDetails": false
    }' \
    -o {{saved-objects-export.ndjson}}
```

If your domain does not have fine-grained access control enabled, you can omit the `-u` flag.

To export specific saved objects by ID, use the `objects` parameter instead of `type`:

```
curl -X POST \
    "https://{{dashboards-endpoint}}/_dashboards/api/saved_objects/_export" \
    -u '{{master-username}}:{{master-password}}' \
    -H "Content-Type: application/json" \
    -H "osd-xsrf: true" \
    -d '{
        "objects": [
            {"type": "dashboard", "id": "{{dashboard-id}}"},
            {"type": "visualization", "id": "{{visualization-id}}"}
        ],
        "includeReferencesDeep": true
    }' \
    -o {{saved-objects-export.ndjson}}
```

**Note**  
To find saved object IDs, you can use the Saved Objects API to list all objects of a specific type. The following example lists all dashboards:  

```
curl -X GET \
    "https://{{dashboards-endpoint}}/_dashboards/api/saved_objects/_find?type=dashboard" \
    -u '{{master-username}}:{{master-password}}'
```
The response includes the ID for each saved object. You can also find the ID in the browser URL when viewing the object in OpenSearch Dashboards.

## Step 2: Import saved objects into OpenSearch UI
<a name="application-migrate-saved-objects-import"></a>

After exporting the saved objects, you can import the NDJSON file to OpenSearch UI manually or via API.

**Topics**
+ [Manually import on OpenSearch UI](#application-migrate-import-console)
+ [Import via API](#application-migrate-import-api)

### Manually import on OpenSearch UI
<a name="application-migrate-import-console"></a>

**To import saved objects using the OpenSearch UI management UI**

1. Open your OpenSearch UI application and navigate to the target workspace.

1. In the workspace, choose **Assets** from the top navigation or go to the workspace assets page.

1. Choose **Import** to open the **Import assets** dialog.

1. Choose **Select file** and select the `.ndjson` file you exported from OpenSearch Dashboards.

1. For **Conflict management**, choose one of the following:
   + **Create new assets with unique IDs** (default) – Generates new IDs for all imported objects, avoiding conflicts with existing assets.
   + **Check for existing assets** – Checks for conflicts with existing objects. When selected, choose one of the following sub-options:
     + **Automatically overwrite conflicts** – Existing assets with the same ID are automatically replaced.
     + **Request action on conflict** – You are prompted to resolve each conflict individually.

1. Choose **Import**.

1. Review the import summary.

### Import via API
<a name="application-migrate-import-api"></a>

To import saved objects using the API with AWS Signature Version 4 authentication, you must first get the data source ID, then use it in the import request. Replace the {{placeholder values}} with your own information.

Step 1: Get the data source ID for your workspace:

```
curl -X GET \
    "https://{{opensearch-ui-endpoint}}/w/{{workspace-id}}/api/saved_objects/_find?type=data-source" \
    --aws-sigv4 "aws:amz:{{region}}:opensearch" \
    --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
    -H "x-amz-security-token: $AWS_SESSION_TOKEN" \
    -H "osd-xsrf: true"
```

**Note**  
The response includes the data source ID. You can also find the data source ID in the browser URL when viewing the data source in OpenSearch UI.

Step 2: Import the saved objects using the data source ID from Step 1:

```
curl -X POST \
    "https://{{opensearch-ui-endpoint}}/w/{{workspace-id}}/api/saved_objects/_import?overwrite=true&dataSourceId={{data-source-id}}" \
    --aws-sigv4 "aws:amz:{{region}}:opensearch" \
    --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
    -H "x-amz-security-token: $AWS_SESSION_TOKEN" \
    -H "osd-xsrf: true" \
    -F "file=@{{saved-objects-export.ndjson}}"
```

**Note**  
These examples use curl's built-in `--aws-sigv4` option (available in curl 7.75 or later) to sign the requests. Set your AWS credentials as environment variables before running the commands: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` (if using temporary credentials).

## Using the in-app migration tool
<a name="application-migration-in-app"></a>

Use the in-app migration tool when you want to bring the saved objects of an existing domain into a workspace without exporting and importing files yourself. With OpenSearch UI, you can copy saved objects from an associated data source into a workspace, so that you don't need to export and import them manually. The migration copies objects into OpenSearch UI; it never deletes or modifies anything in the source.

To open the tool, choose **Migrate dashboards from data sources** on the OpenSearch UI home page, or choose **Dashboards Management** and then **Migrate to OpenSearch UI**. That page lists the data sources that you can migrate from, and a history of previous migrations with links to the workspaces they created.

The migration scans the data source for saved objects, organized by tenant, creates or updates a workspace as the target, and imports the objects into it, linked to the correct data source. It runs on the server. Depending on the number of saved objects, the migration might take several minutes to finish.

The following table lists what the migration includes and what it leaves on the domain.


**What the migration includes**  

| Included | Not included | 
| --- | --- | 
| Dashboards | Data source configurations | 
| Visualizations, including VisBuilder and TSVB | Application settings | 
| Index patterns | Alerting monitors | 
| Saved searches | Index State Management policies | 
| Saved queries | Security configurations | 
| Shortened URLs | Notebooks | 

The excluded items remain on the domain. After you associate the domain as a data source, you reach them through OpenSearch UI without migrating them.

The following limits apply:
+ You can migrate up to 10,000 saved objects in a single migration.
+ You can run only one migration for a data source at a time.
+ A migration is idempotent. Repeating it with the same parameters returns the existing result.

After a migration, open the target workspace and confirm that the dashboards render, that index patterns are associated with the correct data source, and that saved searches return the results you expect. For more information about the steps for each kind of source, see [Migration scenarios for OpenSearch UI](application-migration-scenarios.md).

**Topics**
+ [Migration overview](#application-migrate-saved-objects-overview)
+ [Prerequisites](#application-migrate-saved-objects-prerequisites)
+ [Step 1: Export saved objects from OpenSearch Dashboards](#application-migrate-saved-objects-export)
+ [Step 2: Import saved objects into OpenSearch UI](#application-migrate-saved-objects-import)
+ [Using the in-app migration tool](#application-migration-in-app)
+ [Migration scenarios for OpenSearch UI](application-migration-scenarios.md)