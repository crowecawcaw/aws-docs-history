

# Discovering the registry
<a name="registry-searching"></a>

As a consumer, you can discover MCP servers, agents, skills, and other resources that have been approved and published to the registry. AWS Agent Registry supports three discovery modes on its data plane — natural-language search, paginated browsing of the approved-record catalog, and bulk retrieval by record ID — plus a Model Context Protocol (MCP) endpoint that MCP-compatible clients can invoke directly. This section covers how to use each mode.

**Important**  
 AWS Agent Registry stores record metadata as publishers provide it and doesn’t verify the packages, repositories, or endpoints that records reference. Before your agent installs, downloads, or connects to anything a record references, validate it against sources you trust. For more information, see [Validate record metadata before you act on it](registry-data-protection.md#registry-consumer-validation).

**Topics**
+ [Search for registry records](registry-search-records.md)
+ [Browse approved records](registry-browse-records.md)
+ [Using the Registry MCP endpoint](registry-mcp-endpoint.md)