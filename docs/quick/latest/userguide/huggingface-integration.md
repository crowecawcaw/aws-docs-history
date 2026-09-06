

# HuggingFace integration
<a name="huggingface-integration"></a>

With HuggingFace integration in Amazon Quick, you can access machine learning models, datasets, and spaces through MCP server connectivity. This integration provides action capabilities for ML workflow operations and model management.

## What you can do
<a name="huggingface-integration-capabilities"></a>

HuggingFace integration provides connector capabilities through MCP server connectivity:
+ Browse and download models from HuggingFace Hub
+ Access and manage datasets
+ Interact with HuggingFace Spaces
+ Upload and manage your own models
+ Run inference on hosted models
+ Manage model repositories and versions

## Available tools
<a name="huggingface-integration-tools"></a>

The HuggingFace MCP server typically provides these tools:
+ `search_models` - Search for models on HuggingFace Hub
+ `get_model_info` - Get detailed model information
+ `download_model` - Download models locally
+ `list_datasets` - List available datasets
+ `get_dataset_info` - Get dataset information
+ `run_inference` - Run inference on hosted models
+ `upload_model` - Upload models to Hub
+ `list_spaces` - List HuggingFace Spaces

**Note**  
The specific tools and capabilities available through this MCP server may change over time. For the most current information about supported tools, features, and implementation details, check the official HuggingFace documentation and MCP server repository.

## Setting up HuggingFace integration
<a name="huggingface-integration-setup"></a>

HuggingFace integration uses MCP server connectivity to provide action capabilities. For detailed setup instructions, see [Model Context Protocol (MCP) integration](mcp-integration.md).

You'll need:
+ HuggingFace account with appropriate permissions
+ HuggingFace API token for authentication

## Compatibility
<a name="huggingface-integration-compatibility"></a>

HuggingFace integration supports:
+ **Chat Agents:** Yes
+ **Flows:** Yes
+ **Knowledge Base:** No