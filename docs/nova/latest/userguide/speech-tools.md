

# Tool Use, RAG, and Agentic Flows with Amazon Nova Sonic
<a name="speech-tools"></a>

**Note**  
This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 Sonic guide, visit [Tool configuration](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-tool-configuration.html).

The Amazon Nova Sonic model extends its capabilities beyond pre-trained knowledge by supporting tool use. Tool use, sometimes called function calling, enables integration with external functions, APIs, and data sources. This section explains how to implement tool use, Retrieval-Augmented Generation (RAG), and agentic workflows with Amazon Nova Sonic.

![Diagram that explains how Amazon Nova Sonic calls a tool and uses it to generate results.](http://docs.aws.amazon.com/nova/latest/userguide/images/novaSonicDiagram.png)


You can control what tool the model uses by specifying the `toolChoice` parameter. For more information, see [Choosing a tool](https://docs.aws.amazon.com/nova/latest/userguide/tool-choice.html).

**Topics**
+ [Using tools](speech-tools-use.md)
+ [Controlling how tools are chosen](speech-tools-choice.md)
+ [Tool choice best practices](speech-tools-bp.md)
+ [Implementing RAG](speech-rag.md)
+ [Building agentic flows](speech-agentic.md)