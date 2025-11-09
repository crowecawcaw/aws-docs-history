# Cross-Region calls with Amazon Q in AWS Supply Chain

Amazon Q in AWS Supply Chain has a dependency on Amazon Kendra for retrieving relevant search results from public documentation that may be used to answer your questions. Amazon Kendra is available in a subset of AWS Regions that Amazon Q in AWS Supply Chain supports. Amazon Q in AWS Supply Chain calls Amazon Kendra local endpoints when Amazon Kendra is available locally in an AWS Region. When Amazon Kendra is not available locally, Amazon Q in AWS Supply Chain calls Amazon Kendra’s endpoints in a different AWS Region. In these cross-region calls, Amazon Q in AWS Supply Chain may send your prompts to Amazon Kendra.

| Amazon Q in AWS Supply Chain<br>Region | Amazon Kendra Region |
| -------------------------------------- | -------------------- | ----------- | ---------------- |
| Region Code                            | Region Name          | Region Code | Region Name      |
| eu-central-1                           | Europe (Frankfurt)   | eu-west-1   | Europe (Ireland) |
