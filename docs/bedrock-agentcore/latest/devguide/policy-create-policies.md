# Create a policy

AgentCore Policy in Amazon Bedrock AgentCore uses Cedar as its authorization language to control access to
tools and resources. This guide explains how to understand Cedar policies and write authorization
requirements in natural language that can be automatically converted to Cedar.

Cedar is a formal policy language that provides precise, verifiable access control. When
working with AgentCore Gateway authorization:

- **Understand Cedar policies** - Read and interpret existing
  Cedar policies to understand access control rules
- **Write in natural language** - Express authorization
  requirements using clear, precise natural language
- **Convert to Cedar** - Use policy authoring service to
  automatically generate Cedar policies from natural language
- **Verify policies** - Review generated Cedar policies to
  ensure they match your requirements
  You don't need to memorize Cedar syntax. Focus on understanding policy structure and writing
  precise natural language requirements.

###### Topics

- [Understanding Cedar policies](policy-understanding-cedar.md "policy-understanding-cedar.md")
- [Policy scope](policy-scope.md "policy-scope.md")
- [Policy conditions](policy-conditions.md "policy-conditions.md")
- [Authorization flow](policy-authorization-flow.md "policy-authorization-flow.md")
- [Schema constraints](policy-schema-constraints.md "policy-schema-constraints.md")
- [Limitations](policy-limitations-section.md "policy-limitations-section.md")
- [Common policy patterns](policy-common-patterns.md "policy-common-patterns.md")
