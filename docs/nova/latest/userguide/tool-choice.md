# Choosing a tool

Amazon Nova models support the functionality of _tool choice_. Tool choice allows you, as the developer, to control the manner in which a tool is called. There are three supported parameter options for tool choice: `tool`, `any`, and `auto`.

- **Tool** - The specified tool will be called once.
- **Any** - One of the provided tools will be called at least once.
- **Auto** - The model will decide whether to call a tool and multiple tools will be called if required.

Tool
Using `tool` as the tool choice allows you to control the specific tool that the model calls. The example below highlights this with a structured output use case where the response is required to be formatted in a consistent manner.

```

tool_config = {
    "toolChoice": {
        "tool": { "name" : "extract_recipe"}
    },
    "tools": [
        {
            "toolSpec": {
                "name": "extract_recipe",
                "description": "Extract recipe for cooking instructions",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "Name of the recipe"
                            },
                            "description": {
                                "type": "string",
                                "description": "Brief description of the dish"
                            },
                            "ingredients": {
                                "type": "array",
                                "items": {
                                    "type": "string",
                                    "description": "Name of ingredient"
                                }
                            }
                        },
                        "required": ["name", "description", "ingredients"]
                    }
                }
            }
        }
    ]
}
```

Any
Using `any` as the tool choice allows you to ensure that at least one tool is called each time. While the decision of which tool to call is left up to the model, there will always be a tool returned. The example below highlights using tool choice any for an API selection endpoint use case. This is one example of when it is helpful to require the model to return a specific tool.

```
tool_config = {
    "toolChoice": {
        "any": {}
    },
    "tools": [
         {
            "toolSpec": {
                "name": "get_all_products",
                "description": "API to retrieve multiple products with filtering and pagination options",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "sort_by": {
                                "type": "string",
                                "description": "Field to sort results by. One of: price, name, created_date, popularity",
                                "default": "created_date"
                            },
                            "sort_order": {
                                "type": "string",
                                "description": "Order of sorting (ascending or descending). One of: asc, desc",
                                "default": "desc"
                            },
                        },
                        "required": []
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name": "get_products_by_id",
                "description": "API to retrieve retail products based on search criteria",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "product_id": {
                                "type": "string",
                                "description": "Unique identifier of the product"
                            },
                        },
                        "required": ["product_id"]
                    }
                }
            }
        }
    ]
}
```

Auto
Using `auto` as the tool choice is the default functionality of the tool support and allows the model to decide when to call a tool and how many tools to call. This is the behavior if you don’t include tool choice in your request.

###### Note

The default behavior of Amazon Nova tool calling is to use chain-of-thought for tool selection. When using the default behavior or tool choice `auto`, there will also be the thought process output in <thinking> tags.

The following example highlights a chatbot use case where you might want to allow the model to search the internet for recent information or to respond directly to the user. This tool choice provides flexibility and will leave the reasoning to the model.

```
tool_config = {
    "toolChoice": {
        "auto": {}
    },
    "tools": [
         {
            "toolSpec": {
                "name": "search",
                "description": "API that provides access to the internet",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Query to search by",
                            },
                        },
                        "required": ["query"]
                    }
                }
            }
        }
    ]
}
```

###### Note

When setting the tool choice parameter, you might still see the model output text or perform sequential tool calls after the original tool selection. We recommend that you set a stop sequence here to limit the output to just the tool:

```
“stopSequences”: [“</tool>”]
```

For more information, see [InferenceConfiguration](../../../bedrock/latest/APIReference/API_agent_InferenceConfiguration.md "../../../bedrock/latest/APIReference/API_agent_InferenceConfiguration.md") in the Amazon Bedrock API guide.
