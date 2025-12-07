# Tool use beyond the browser (Preview)

(Preview) Nova Act allows you to integrate external tools beyond the browser, such as an API call or database query, into workflows. This functionality enables developers to integrate remote MCP tools and agentic frameworks, such as Strands Agents, into their workflows.

## Defining a local tool

The first step in the workflow is defining the tool. The tool definition must include all of the necessary context to guide the model on appropriate tool invocation.

To make a Python function available as a tool, you annotate it with the `@tool` decorator. This allows you to include the required context. To do so, define the following within the function’s comments:

- a description of the tool
- its input parameters
- its return type

Below is an example of a tool defined to return a specific row from an Excel file:

```
@tool
def read_row_as_dict(file_path, row_number):
    """
    Reads a specific row from an Excel file and returns it as a dictionary
    where column headers are keys and row values are the corresponding
    dictionary values.

    Args:
        file_path (str): The path to the Excel file.
        row_number (int): The row number (1-based index) to retrieve.

    Returns:
        dict: A dictionary containing the data from the specified row.
    """
    # Read the Excel file using pandas
    df = pd.read_excel(file_path)

    # Check if the row_number is within the valid range
    if row_number < 1 or row_number > len(df):
        raise ValueError(f"Row number {row_number} is out of range. " f"The sheet has {len(df)} rows.")

    # Get the row data as a dictionary
    row_data = df.iloc[row_number - 1].to_dict()

    return row_data
```

## Using a tool

To use a tool with Nova Act, add it to the tools attribute of the Nova Act constructor. Nova Act will decide whether to call a tool given the request.

To define the tools available when initializing Nova Act, pass an array of tools, like below.

```
with NovaAct(
    starting_page=file_path,
    tools=[read_row_as_dict],
)
```

###### Note

For best performance, limit the number of tools you provide to the model in a single act command. For higher accuracy, you can be more specific in the prompt to let Nova Act know when you want it to invoke a specific tool. Nova Act performs best if you match the instructions to the tool description. Similar to browser commands, we recommend being prescriptive and succinct in what the agent should do and breaking down larger acts into smaller ones to improve reliability.

## Returning tool results

When Nova Act determines a tool is needed, it will call the tool with the appropriate arguments. Here is an example of how tool results show in the Nova Act logs:

```
think("I need to read the data from row number 1 in the Excel file.");
tool({"name":"read_row_as_dict","input":{"file_path":[file_path],"row_number":1}});
Result for tool call 'read_row_as_dict': {'First Name': 'John', 'Last Name': 'Doe', 'Email': 'jdoe@example.com'}
```

## Using MCP with Nova Act

The Model Context Protocol (MCP) is an open standard that enables developers to build secure, two-way connections between their data sources and AI-powered tools. Instead of writing custom adapters for each API or service, you can run an MCP server and integrate its tools with Nova Act automatically through a client bridge. Once connected, Nova Act treats these tools like any other external integration: it decides when to call them, sends the required parameters, and incorporates the results into its response.

Below is an example using the [AWS Documentation MCP Server](https://awslabs.github.io/mcp/servers/aws-documentation-mcp-server "https://awslabs.github.io/mcp/servers/aws-documentation-mcp-server"). This example requires installing the [Strands Agents library](https://strandsagents.com/latest/ "https://strandsagents.com/latest/").

```
from mcp import StdioServerParameters, stdio_client
from strands.tools.mcp import MCPClient
with MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx",
            args=["awslabs.aws-documentation-mcp-server@latest"]
        )
) as aws_docs_client:
```

Once the MCP is initialized, retrieve the list of available tools from the MCP server and pass them to NovaAct.

```
with NovaAct(
    starting_page=file_path,
    tools=aws_docs_client.list_tools_sync(),
)
```
