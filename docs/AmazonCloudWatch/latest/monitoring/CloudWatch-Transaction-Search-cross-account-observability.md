# Monitoring spans across accounts


 Spans sent to X-Ray are ingested and managed in a log group called `aws/spans`. 
 To monitor spans across multiple accounts, you must [enable Transaction Search](CloudWatch-Transaction-Search-getting-started.md "CloudWatch-Transaction-Search-getting-started.md") across all source and monitoring accounts and [enable cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md") for logs and traces. 
 When you enable cross-account observability, you can search up to 10,000 accounts and get visibility into traces across accounts. 
 This feature is provided at no extra cost for the `aws/spans` log group. 
 If you enable cross-account observability for trace summaries, the first trace summary copy is free. 
 For more information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
