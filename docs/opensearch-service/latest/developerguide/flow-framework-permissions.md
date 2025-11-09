# Configure permissions

If you create a new domain with version 2.13 or later, permissions are already in
place. If you enable flow framework on a preexisting OpenSearch Service domain with version 2.11
or earlier that you then upgrade to version 2.13 or later, you must define the
`flow_framework_manager` role. Non-admin users must be mapped to this
role in order to manage warm indexes on domains using fine-grained access control.
To manually create the `flow_framework_manager` role, perform the
following steps:

1. In OpenSearch Dashboards, go to **Security** and choose
   **Permissions**.
2. Choose **Create action group** and configure the
   following groups:

| Group name                    | Permissions                                                                                                                                                                                                                                                    |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `flow_framework_full_access`  | • `cluster:admin/opensearch/flow_framework/*`<br>• `cluster_monitor`                                                                                                                                                                                           |
| `flow_framework_read_accesss` | • `cluster:admin/opensearch/flow_framework/workflow/get`<br>• `cluster:admin/opensearch/flow_framework/workflow/search`<br>• `cluster:admin/opensearch/flow_framework/workflow_state/get`<br>• `cluster:admin/opensearch/flow_framework/workflow_state/search` |

3. Choose **Roles** and **Create
   role**.
4. Name the role **flow_framework_manager**.
5. For **Cluster permissions,** select
   `flow_framework_full_access` and
   `flow_framework_read_access`.
6. For **Index**, type `*`.
7. For **Index permissions**, select
   `indices:admin/aliases/get`,
   `indices:admin/mappings/get`, and
   `indices_monitor`.
8. Choose **Create**.
9. After you create the role, [map it](fgac.md#fgac-mapping "fgac.md#fgac-mapping") to
   any user or backend role that will manage flow framework indexes.
