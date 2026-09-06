

# Using Amazon Q Developer in the IDE
<a name="q-in-IDE"></a>

**End of support notice**  
On April 30, 2027, AWS will discontinue support for Amazon Q Developer IDE plugins. For capabilities similar to Amazon Q Developer IDE plugins, explore Kiro to access the latest models and features, including agentic coding, chat and MCP support. For more information, see [Amazon Q Developer IDE plugins end of support](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-developer-ide-end-of-support.html).

Use Amazon Q Developer in integrated development environments (IDEs) to learn about AWS and get assistance with your software development needs. In IDEs, Amazon Q includes capabilities to provide guidance and support across various aspects of software development, such as answering questions about building on AWS, generating and updating code, security scanning, and optimizing and refactoring code.

To install Amazon Q in your IDE, see [Installing the Amazon Q Developer extension or plugin in your IDE](q-in-IDE-setup.md) .

**Topics**
+ [Supported IDEs and available features](#supported-ides-features)
+ [Installing the Amazon Q Developer extension or plugin in your IDE](q-in-IDE-setup.md)
+ [Chatting with Amazon Q Developer about code](q-in-IDE-chat.md)
+ [Generating inline suggestions with Amazon Q Developer](inline-suggestions.md)
+ [Supported languages for Amazon Q Developer in the IDE](q-language-ide-support.md)

## Supported IDEs and available features
<a name="supported-ides-features"></a>

The features you have access to depend on the IDE where you use Amazon Q. The following table describes the IDEs supported by Amazon Q and the availability and limitations of features in each IDE.

If no language support is specified, the IDE supports languages listed in the [Supported languages](q-language-ide-support.md) topic.



| Feature | VSCode | JetBrains | Eclipse | Visual Studio | 
| --- | --- | --- | --- | --- | 
|  [Chat](q-in-IDE-chat.md)  | Yes | Yes | Yes | Yes | 
|  [Agentic coding](q-in-IDE-chat.md#agentic-coding)  | Yes | Yes | Yes | Yes | 
| [MCP servers](mcp-ide.md) | Yes | Yes | Yes | Yes | 
|  [Context in chat](ide-chat-context.md)  | Yes | Yes | Yes | Yes | 
|  [Inline chat](q-in-IDE-inline-chat.md)  | Yes | Yes | Yes | No | 
|  [Workspace context in chat](workspace-context.md)  | Yes | Yes | Yes | Yes | 
|  [Inline suggestions](inline-suggestions.md)  | Yes | Yes | Yes | Yes | 
|  [Transformations](transform-java.md)  | Yes | Yes | No | Yes | 
|   | Yes | Yes | Yes | No | 

You can also generate inline suggestions in AWS coding environments. For more information, see [Generating inline suggestions in AWS coding environments](setting-up-AWS-coding-env.md) .