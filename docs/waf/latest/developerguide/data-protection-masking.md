

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Data protection
<a name="data-protection-masking"></a>

AWS WAF data protection settings let you implement customized and granular protection of sensitive information (passwords, API keys, authentication tokens, and other confidential data) on specific data fields such as headers, parameters, and body content.

You can configure data protection at either:
+ The protection pack (web ACL) level, which applies across all output destinations.
+ Logging only, which only affects the data that AWS WAF sends to the configured logging destination. 

Data protection can be specified as either a substitution or hashing. 

Substitution refers to replacing content with the word `REDACTED`. 

 Hashing refers to replacing content, from string to SHA-256 binary to Base64:

1. First, the algorithm builds a string from account\_number and content.

1. It then applies SHA-256 to produce a binary hash.

1. Finally, it encodes those bytes using Base64.

**Tip**  
 You should review the characteristics of SHA-256 hashing to determine if it meets your requirements before you select the appropriate data protection method. We do not recommend relying on SHA-256 hashing if you intend to achieve an outcome equivalent to encryption or tokenization.

**Topics**
+ [Enabling data protection](enable-protection.md)
+ [Data protection exceptions](data-protection-exceptions.md)
+ [Data protection limitations](data-protection-limitations.md)
+ [Examples of data protection](data-protection-examples.md)
+ [Configuring data protection for a protection pack (web ACL)](data-protection-configure.md)