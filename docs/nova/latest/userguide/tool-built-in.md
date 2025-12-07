# Using built-in tools

Built-in tools are fully managed tools that are available out of the box, with no need for custom implementation.
These can be enabled in the Converse API with a simple toggle.

## Code interpreter

Code Interpreter allows Nova to securely execute Python code in isolated sandbox environments. This enables writing
and executing code, analyzing data, creating visualizations, and solving mathematical problems. For example, Code Interpreter
can be used to:

- Generate financial reports based on uploaded data
- Complete statistical analysis or algorithm simulations
- Execute database migration scripts in isolated environments
- Run unit tests for new generated code

Here’s an example of how to enable Code Interpreter with the Converse API:

```

{
  "messages": [
    {
      "role": "user",
      "content": [{"text":  "What is the average of 10, 24, 2, 3, 43, 52, 13, 68, 6, 7, 902, 82")}]
    }
  ],

"toolConfig": {
    "tools": [
        {
            "systemTool": {
                "name": "nova_code_interpreter"
            }
        }
    ]
},

```

In this case, the model will determine that the request requires computation so it generates
the required Python code and calls the code interpreter tool.

```

{
    "toolUse": {
        "input": {
            "code": "'''Calculate the average of the given numbers.'''\nnumbers = [10, 24, 2, 3, 43, 52, 13, 68, 6, 7, 902, 82]\nsum_numbers = sum(numbers)\ncount = len(numbers)\naverage = sum_numbers / count\n(sum_numbers, count, average)"
        },
        "name": "nova_code_interpreter",
        "toolUseId": "tooluse_WytfF0g1S5qUeEPm0ptOdQ",
        "type": "server_tool_use"
    }
},

```

The interpreter runs this code in a sandbox and captures the result, output in a standard schema:

```

{
  "stdOut": String,
  "stdErr": String,
  "exitCode": int,
  "isError": boolean
}

```

In this case, you would receive back:

```

{
    "toolResult": {
        "content": [
            {
                "text": "{\"stdOut\":\"(1212, 12, 101.0)\",\"stdErr\":\"\",\"exitCode\":0,\"isError\":false}"
            }
        ],
        "status": "success",
        "toolUseId": "tooluse_WytfF0g1S5qUeEPm0ptOdQ",
        "type": "nova_code_interpreter_result"
    }
}

```

## Model Context Protocol

The Model Context Protocol (MCP) is an open standard that enables developers to build secure, two-way connections
between their data sources and AI-powered tools. Instead of writing custom adapters for each API or service, you can run
an MCP server and let Nova discover its tools automatically through a client bridge. Once connected, Nova treats these
tools like any other external integration: it decides when to call them, sends the required parameters, and incorporates
the results into its response.
