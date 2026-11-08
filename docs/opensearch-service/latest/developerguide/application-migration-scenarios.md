

# Migration scenarios for OpenSearch UI
<a name="application-migration-scenarios"></a>

OpenSearch UI can bring the saved objects from an associated data source—dashboards, visualizations, index patterns, and searches—into a workspace. The steps depend on the kind of data source and on how many tenants it has. Use the following table to find the scenario that matches your source.


| Source | How to identify it | Result | 
| --- | --- | --- | 
| Serverless collection | No security plugin badge in the migration dialog, one tenant, and an endpoint that ends in .aoss.amazonaws.com | One collection maps to one workspace | 
| Single-tenant domain | A security plugin badge, one tenant, and an endpoint that ends in .es.amazonaws.com | One domain maps to one workspace | 
| Multi-tenant domain | A security plugin badge, and more than one tenant | You choose one workspace for all tenants, or one workspace for each tenant | 
| A source that was migrated before | The dialog reports that the data source has been migrated before | You choose to update the existing workspace, or to create a new one | 

**Note**  
Serverless collections have a single tenant, `global_tenant`, and do not use the security plugin. Managed domains do use the security plugin, even when they have only one tenant, and the migration reads saved objects through the security plugin API. The badge in the migration dialog is what distinguishes the two.

## Migrating from a serverless collection
<a name="application-migration-scenarios-collection"></a>

Before you start, confirm that the collection is an associated data source in your OpenSearch UI application, and that it contains saved objects.

**To migrate from a serverless collection**

1. Open the **Migrate to OpenSearch UI** page from data administration, or choose **Migrate dashboards from data sources** on the home page.

1. Choose **Migrate**.

1. In the **Associated data source** list, choose your collection. The dialog expands to show the number of tenants and items, the source endpoint, a workspace name, and a workspace type.

1. Review the workspace name, and then choose **Start migration**. The migration runs on the server and redirects you to the new workspace when it finishes.

1. Return to the migration page. The **Recent migrations** table lists the completed migration with a link to the workspace.

## Migrating from a single-tenant domain
<a name="application-migration-scenarios-single"></a>

This is the most common scenario for a domain that does not use multi-tenancy. All users share the saved objects in the global tenant. Before you start, confirm that the domain is an associated data source, that the security plugin is enabled, and that the tenant contains saved objects.

**To migrate from a single-tenant domain**

1. Open the **Migrate to OpenSearch UI** page, and then choose **Migrate**.

1. In the **Associated data source** list, choose your domain. The dialog shows a security plugin badge, the tenant and item counts, and the source endpoint.

1. Review the workspace name, and then choose **Start migration**. When you start the migration, it exports the saved objects through the security plugin API and imports them into a new workspace.

1. Return to the migration page, and confirm the migration in the **Recent migrations** table.

Verify that dashboards render as expected, particularly any that reference a specific index pattern.

## Migrating from a multi-tenant domain
<a name="application-migration-scenarios-multi"></a>

In OpenSearch Dashboards, multiple tenants gave teams their own isolated set of dashboards. In OpenSearch UI, workspaces serve that purpose, so the migration asks how to map tenants to workspaces.

**To migrate from a multi-tenant domain**

1. Open the **Migrate to OpenSearch UI** page, and then choose **Migrate**.

1. Choose your domain. The dialog lists every tenant with its item count, and you can choose a tenant to preview its objects.

1. Choose how to translate tenants into workspaces:
   + **All in one workspace** consolidates the saved objects from every tenant into a single workspace. Choose this when your team is small, when tenants were used informally, or when you want a unified view.
   + **One workspace per tenant** keeps the tenants separate. Choose this when teams used tenants for isolation and you want to preserve that separation. The dialog shows a workspace name and type for each tenant, and you can edit each name.

1. Choose **Start migration**.

1. Return to the migration page, and confirm the migrations in the **Recent migrations** table.

After the migration, open each workspace and verify that the dashboards render. If you consolidated the tenants, review the workspace for objects that had the same name in different tenants. If you created one workspace for each tenant, set the workspace permissions to match the access that each tenant previously had. For more information about workspace permissions, see [Using Amazon OpenSearch Service workspaces](application-workspaces.md).

## Re-running a migration
<a name="application-migration-scenarios-rerun"></a>

When you select a data source that you migrated before, the dialog reports that you migrated the source previously and asks you to choose a migration mode.


| Mode | What it does | When to choose it | 
| --- | --- | --- | 
| Update existing workspace | This mode adds new saved objects and refreshes changed ones. The update does not modify objects that you created in the workspace | The source has new or updated dashboards that you want, and you do not want to lose the customizations you made in the workspace | 
| Create new workspace | This mode creates a new workspace with a fresh copy of all saved objects, and leaves the earlier workspace unchanged | You want a clean workspace, the existing workspace has diverged, or you want to compare the two | 

**Important**  
Updating a workspace never deletes saved objects. If the source no longer has an object, the workspace keeps it after the update. The update synchronizes only new and changed objects.

To update an existing workspace, choose **Update existing workspace**, choose the workspace in **Select workspace to update**, and then choose **Update workspace**. To start again, choose **Create new workspace**. The dialog then shows the same options as a first migration, including the tenant mapping, and the dialog leaves the earlier workspace in place.