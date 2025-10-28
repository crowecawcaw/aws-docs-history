# Use AMS SSP to provision Amazon Lex in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Lex capabilities directly in your AMS managed account. Amazon Lex is a service for building conversational interfaces into any application
using voice and text. Amazon Lex provides the advanced deep learning functionalities of
automatic speech recognition (ASR) for converting speech to text, and natural language
understanding (NLU) to recognize the intent of the text, to enable you to build applications
with highly engaging user experiences and lifelike conversational interactions.
With Amazon Lex, the same deep learning technologies that power Amazon Alexa are
now available to any developer, enabling you to quickly and easily build sophisticated,
natural language, conversational bots ﻿or chatbots﻿.
To learn more, see [Amazon Lex](https://aws.amazon.com/lex/ "https://aws.amazon.com/lex/").

## Amazon Lex in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Amazon Lex in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add change type (ct-1w8z66n899dct).
This RFC provisions the following IAM role to your account: `customer_lex_author_role`.
Once provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon Lex in my AMS account?**

Amazon Lex integration with Lambda is limited to Lambda functions
without an "AMS-" prefix, in order to prevent any modifications to AMS infrastructure.

**Q: What are the prerequisites or dependencies to using Amazon Lex in my AMS account?**

There are no prerequisites or dependencies to use Amazon Lex in your AMS account.
