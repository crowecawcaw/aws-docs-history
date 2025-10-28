# Configure permissions

If you're upgrading to 2.5 from a previous OpenSearch Service domain version, the snapshot
management security permissions might not be defined on the domain. Non-admin users
must be mapped to this role in order to use snapshot management on domains using
fine-grained access control. To manually create the snapshot management role,
perform the following steps:

1. In OpenSearch Dashboards, go to **Security** and choose
   **Permissions**.
2. Choose **Create action group** and configure the
   following groups:

| Group name                        | Permissions                                                                                                                                                                                                                                                                    |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `snapshot_management_full_access` | <br>• `cluster:admin/opensearch/snapshot_management/*` <br>• `cluster:admin/opensearch/notifications/feature/publish` <br>• `cluster:admin/repository/*` <br>• `cluster:admin/snapshot/*`                                                                                      |
| `snapshot_management_read_access` | <br>• `cluster:admin/opensearch/snapshot_management/policy/get` <br>• `cluster:admin/opensearch/snapshot_management/policy/search` <br>• `cluster:admin/opensearch/snapshot_management/policy/explain` <br>• `cluster:admin/repository/get` <br>• `cluster:admin/snapshot/get` | 3. Choose **Roles** and **Create role**. 4. Name the role **snapshot_management_role**. 5. For **Cluster permissions**, select `snapshot_management_full_access` or `snapshot_management_read_access`. 6. Choose **Create**. 7. After you create the role, [map it](fgac.md#fgac-mapping "fgac.md#fgac-mapping") to any user or backend role that will manage snapshots. |
