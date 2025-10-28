# Factors that may slow down cold starts of Neptune Gremlin Lambda functions

The first time an AWS Lambda function is invoked is referred to as a cold start.
There are several factors that can increase the latency of a cold start:

- **Be sure to assign enough memory to your Lambda function.**   –  
  Compilation during a cold start can be significantly slower for a Lambda function
  than it would be on EC2 because AWS Lambda allocates CPU cycles [linearly in proportion to the memory](../../../lambda/latest/dg/configuration-console.md "../../../lambda/latest/dg/configuration-console.md")
  that you assign to the function. With 1,769 MB of memory, a function receives
  the equivalent of one full vCPU (one vCPU-second of credits per second). The impact
  of not assigning enough memory to receive adequate CPU cycles is particularly
  pronounced for large Lambda functions written in Java.
- **Be aware that [enabling IAM database
  authentication](iam-auth-enable.md "iam-auth-enable.md") may slow down a cold start**   –  
  AWS Identity and Access Management (IAM) database authentication can also slow down cold starts, particularly
  if the Lambda function has to generate a new signing key. This latency only affects
  the cold start and not subsequent requests, because once IAM DB auth has established
  the connection credentials, Neptune only periodically validates that they are
  still valid.
