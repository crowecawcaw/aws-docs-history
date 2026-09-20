

# Configure permissions
<a name="sm-security"></a>

If you're upgrading to 2.5 from a previous OpenSearch Service domain version, the snapshot management security permissions might not be defined on the domain. Non-admin users must be mapped to this role in order to use snapshot management on domains using fine-grained access control. To manually create the snapshot management role, perform the following steps:

1. In OpenSearch Dashboards, go to **Security** and choose **Permissions**.

1. Choose **Create action group** and configure the following groups: 


<table>
<thead>
  <tr><th>Group name</th><th>Permissions</th></tr>
</thead>
<tbody>
  <tr><td><code>snapshot_management_full_access</code></td><td> <ul><li> <code>cluster:admin/opensearch/snapshot_management/*</code> </li><li> <code>cluster:admin/opensearch/notifications/feature/publish</code> </li><li> <code>cluster:admin/repository/*</code> </li><li> <code>cluster:admin/snapshot/*</code> </li></ul> </td></tr>
  <tr><td><code> snapshot_management_read_access</code></td><td> <ul><li> <code>cluster:admin/opensearch/snapshot_management/policy/get</code> </li><li> <code>cluster:admin/opensearch/snapshot_management/policy/search</code> </li><li> <code>cluster:admin/opensearch/snapshot_management/policy/explain</code> </li><li> <code>cluster:admin/repository/get</code> </li><li> <code>cluster:admin/snapshot/get</code> </li></ul> </td></tr>
</tbody>
</table>


1. Choose **Roles** and **Create role**.

1. Name the role **snapshot\_management\_role**.

1. For **Cluster permissions**, select `snapshot_management_full_access` or `snapshot_management_read_access`.

1. Choose **Create**.

1. After you create the role, [map it](fgac.md#fgac-mapping) to any user or backend role that will manage snapshots.