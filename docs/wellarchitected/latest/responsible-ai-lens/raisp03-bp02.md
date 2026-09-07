

# RAISP03-BP02 Add security filters
<a name="raisp03-bp02"></a>

 Implement security safeguards that detect and block threats such as prompt injections, roleplay jailbreaks, and other adversarial inputs. Design input validation mechanisms that identify unwanted prompts and suspicious query patterns before they can manipulate system behavior or extract sensitive information. Implement guardrails with content filtering capabilities designed to block the generation of harmful outputs even when inputs successfully bypass input protections. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation considerations
<a name="implementation-considerations-75"></a>

1.  Revisit your security analysis in RAIBR02-BP06 to understand the scope of security issues, including chat interfaces, knowledge bases, file systems and tools, considering the entire system architecture and component interactions beyond just user touchpoints. 

1.  Design multi-layered security using input validation, content filtering, and rate limiting, utilizing tools like Amazon Bedrock Guardrails for unwanted prompt detection and Amazon Comprehend for input validation. 

1.  Apply traditional security best practices like least privilege access using AWS IAM roles and policies, while securing infrastructure components and monitoring systems. 

1.  Design your AI system with a zero-trust model, where no user or device is trusted by default and verification is required for every access attempt. 

1.  Design for providing the right access level to users and applications invoking AI features and related Resources. For example, provide role-based access control (RBAC) and attribute-based access control (ABAC) to assign permissions based on user roles and context, granting access only to necessary functions and data. Grant users and agents only the minimum permissions necessary to perform their tasks. 

1.  Design for encrypting sensitive data used in AI systems both at rest (in storage) and in transit to block unauthorized access. 

1.  Design for sanitizing sensitive inputs coming in and going out of AI system. Validate that system inputs conform to expected formats. 

## Resources
<a name="resources-72"></a>

 **Related documents:** 
+  [Detect and filter harmful content by using Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) 
+  [ISO/IEC 42001:2023 A.6.1.2 Objectives for responsible development of AI system](https://www.iso.org/standard/42001) 

 **Related tools:** 
+  [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) 