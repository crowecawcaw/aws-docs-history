# Box integration

With Box integration in Amazon Quick Suite, you can manage files, folders, and collaborate on documents directly from your Amazon Quick Suite environment through Model Context Protocol (MCP) server connectivity.

## What you can do

The Box integration provides action capabilities through MCP server connectivity, enabling you to:

- Upload and download files
- Create and manage folders
- Share files and folders
- Search for content
- Manage file permissions
- Use AI-powered tools to ask questions, extract insights, and analyze content across files and hubs.

## Available tools

The Box MCP server typically provides the following tools:

- `who_am_i` - Returns detailed information about the currently authenticated Box user.
- `get_file_content` - Returns the content of a file stored in Box.
- `get_file_details` - Gets comprehensive file information from Box including metadata, permissions, and version details.
- `update_file_properties` - Updates file properties, including name, description, tags, and collections.
- `upload_file` - Uploads a new file to Box.
- `upload_file_version` - Uploads a new file version by providing the entire file contents to update an existing file in Box.
- `create_folder` - Creates a new folder in Box.
- `get_folder_details` - Retrieves comprehensive folder information including metadata, permissions, and collaboration settings.
- `list_folder_content_by_folder_id` - Lists files, folders, and web links in a folder.
- `update_folder_properties` - Updates folder properties, including name, description, tags, and collections.
- `search_files_keyword` - Searches for files using keywords. Supports metadata filters, file extension filtering, and field selection.
- `search_folders_by_name` - Searches for folders within Box by name using keyword matching.
- `ai_qa_hub` - Asks a question to a Box Hub using Box AI.
- `ai_qa_single_file` - Asks a question to a single file using Box AI.
- `ai_qa_multi_file` - Asks a question to multiple files using Box AI.
- `ai_extract_freeform` - Extracts metadata from files using Box AI in freeform format without requiring predefined template structures.
- `ai_extract_structured` - Extracts structured metadata from files using Box AI based on either custom fields definition or an existing metadata template.
- `create_file_comment` - Creates a new comment on a specific file.
- `list_file_comments` - Lists all comments on a specific file.
- `list_tasks` - Lists all tasks associated with a specific file, including status, message, and due dates.
- `add_items_to_hub` - Adds files, folders, or web links to a specific hub.
- `create_hub` - Creates a new hub.
- `get_hub_details` - Retrieves detailed information about a specific hub.
- `get_hub_items` - Gets items (files and folders) associated with a specific hub.
- `list_hubs` - Lists all hubs accessible to the authenticated user.
- `update_hub` - Updates the title and description of a specific hub.

###### Note

The specific tools and capabilities available through this MCP server may change over time. For the most current information about supported tools, features, and implementation details, check the official Box documentation and MCP server repository.

## Setup requirements

To set up Box integration, you need:

- Box account with appropriate permissions
- Box API credentials (Client ID and Client Secret)
- Amazon Quick Suite with MCP integration enabled

## Compatibility

Box integration supports:

- **Chat Agents:** Yes
- **Flows:** Yes
- **Knowledge Base:** No
