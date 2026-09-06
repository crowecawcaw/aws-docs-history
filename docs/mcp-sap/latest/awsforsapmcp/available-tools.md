

# Available MCP tools
<a name="available-tools"></a>

With the AWS for SAP Model Context Protocol (MCP) Server, your AI agents can access tools and prompts for interacting with SAP systems. These tools are split into two categories: Read tools, which are available by default, and Write tools, which you must explicitly enable before they can be used.

## Tools reference
<a name="tools-reference"></a>


| Tool | Description | Classification | 
| --- | --- | --- | 
|  `find_sap_services`  | Discovers available SAP OData services from the standard or custom service catalog. Supports pagination (`top`/`skip`). | Read | 
|  `get_metadata`  | Retrieves OData service metadata. | Read | 
|  `odata_read`  | Reads data from SAP OData entity sets. | Read | 
|  `odata_count`  | Returns the count of records in an OData entity set, with optional filtering. Use this before `odata_read` to understand data volume. | Read | 
|  `odata_create`  | Creates a new entity record in an SAP OData entity set. Requires a JSON payload with entity data. | Write | 
|  `odata_update`  | Updates an existing entity record identified by key fields. | Write | 
|  `odata_delete`  | Deletes an entity record identified by key fields. | Write | 
|  `odata_function_import`  | Enables execution of custom backend logic that does not fit standard CRUD operations. | Write | 
|  `get_service_hints`  | Returns usage guidance and hints for a specific SAP OData service from the configured service hints file. | Read | 

**Important**  
By default, the AWS for SAP MCP Server runs in **read-only mode**. Your AI agents can perform non-mutating tasks such as querying service catalogs, inspecting metadata, and running read operations. Write actions — including create, read, update, and delete (CRUD) operations and function imports — are disabled unless you set both the global `Write Enabled` configuration and the operation specific flag to `true`.