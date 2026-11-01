

# Example designations
<a name="example-designations"></a>

The following example designations show common permission sets that you can use as starting points when you create custom designations. Each example describes a persona, the purpose of that persona, and the permissions to select in the visual permission selector when you create the designation. These are examples only. Adjust the permissions to match your organization's access control requirements. When you create a designation, you can also start from a quick-start template (Steward, Consumer, or Viewer) that pre-selects a set of permissions that you can then customize. For the steps to create a designation, see [Create designations](create-designations.md).

## Viewer
<a name="example-designation-viewer"></a>

The Viewer designation is for users who need to explore the catalog and monitor project resources without making changes, such as business analysts or auditors. It grants read-only access across the project.

To create the Viewer designation, select the following permissions:


| Category | Permissions | 
| --- | --- | 
| Project | Read-only actions | 
| Catalog | Read-only actions | 
| Subscriptions | Read-only actions | 
| Notebooks and Querybooks | Read-only actions | 

**Note**  
The Viewer designation grants read-only permissions in the project interface, but it does not restrict data operations, such as querying or modifying tables, in the project's query editor. Those operations are governed by the project's IAM role. For more information, see [Designation permissions](designation-permissions.md).

## Data Engineer
<a name="example-designation-data-engineer"></a>

The Data Engineer designation is for users who build and operate the data pipelines that ingest, transform, and prepare data for analytics. It grants permissions to manage connections and run data source runs, manage environments and project compute for processing jobs, create and manage catalog assets and data products, and request subscriptions to source data.

To create the Data Engineer designation, select the following permissions:


| Category | Permissions | 
| --- | --- | 
| Project | Manage environments, Manage user compute | 
| Connections | Manage connections | 
| Catalog | Manage assets, Manage data products | 
| Subscriptions | Manage subscription requests | 

## Machine Learning Engineer (ML Engineer)
<a name="example-designation-ml-engineer"></a>

The Machine Learning Engineer (ML Engineer) designation is for users who build, train, and iterate on machine learning models. It grants access to notebooks (which include querybooks) and project compute, the ability to manage data assets and data products, permission to use connections to access data, and the ability to request subscriptions to additional datasets.

To create the ML Engineer designation, select the following permissions:


| Category | Permissions | 
| --- | --- | 
| Project | Manage user compute | 
| Notebooks and Querybooks | All actions | 
| Catalog | Manage assets, Manage data products | 
| Connections | Use connection | 
| Subscriptions | Manage subscription requests | 

## Data Steward
<a name="example-designation-data-steward"></a>

The Data Steward designation is for users who govern and curate the business data catalog. It grants permissions to manage glossaries, governed terms, metadata forms, and asset types, publish catalog listings, run and review metadata generation, manage asset filters, and approve subscription requests, along with read-only access to catalog resources.

To create the Data Steward designation, select the following permissions:


| Category | Permissions | 
| --- | --- | 
| Catalog | Manage glossaries, Manage governed terms, Manage metadata forms, Manage asset types, Manage predictions, Execute metadata generation, Manage asset publishing, Read-only actions | 
| Subscriptions | Manage subscription approvals, Manage asset filters | 