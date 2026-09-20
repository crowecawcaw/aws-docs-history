

# Configure permissions
<a name="flow-framework-permissions"></a>

If you create a new domain with version 2.13 or later, permissions are already in place. If you enable flow framework on a preexisting OpenSearch Service domain with version 2.11 or earlier that you then upgrade to version 2.13 or later, you must define the `flow_framework_manager` role. Non-admin users must be mapped to this role in order to manage warm indexes on domains using fine-grained access control. To manually create the `flow_framework_manager` role, perform the following steps:

1. In OpenSearch Dashboards, go to **Security** and choose **Permissions**.

1. Choose **Create action group** and configure the following groups: 


<table>
<thead>
  <tr><th>Group name</th><th>Permissions</th></tr>
</thead>
<tbody>
  <tr><td><code>flow_framework_full_access</code></td><td> <ul><li> <code>cluster:admin/opensearch/flow_framework/*</code> </li><li> <code>cluster_monitor</code> </li></ul> </td></tr>
  <tr><td><code>flow_framework_read_accesss</code></td><td> <ul><li> <code>cluster:admin/opensearch/flow_framework/workflow/get</code> </li><li> <code>cluster:admin/opensearch/flow_framework/workflow/search</code> </li><li> <code>cluster:admin/opensearch/flow_framework/workflow_state/get</code> </li><li> <code>cluster:admin/opensearch/flow_framework/workflow_state/search</code> </li></ul> </td></tr>
</tbody>
</table>


1. Choose **Roles** and **Create role**.

1. Name the role **flow\_framework\_manager**.

1. For **Cluster permissions,** select `flow_framework_full_access` and `flow_framework_read_access`.

1. For **Index**, type `*`.

1. For **Index permissions**, select `indices:admin/aliases/get`, `indices:admin/mappings/get`, and `indices_monitor`.

1. Choose **Create**.

1. After you create the role, [map it](fgac.md#fgac-mapping) to any user or backend role that will manage flow framework indexes.