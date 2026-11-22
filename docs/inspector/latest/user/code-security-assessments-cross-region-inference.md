

# Cross-Region inference for Amazon Inspector Code Security

 Amazon Inspector Code Security uses artificial intelligence to analyze your code. To do this, it uses cross-Region inference in Amazon Bedrock to process requests for its AI-powered analysis. This analysis includes Static Application Security Testing (SAST) scanning and automatic fix pull requests. Cross-Region inference automatically selects the optimal AWS Region within your geography to process each request, which maximizes available compute resources and model availability. 

 Your data remains stored only in the AWS Region where the request originates. Inference requests are processed within the same geography as that Region and are never routed outside that geography. All data is encrypted when transmitted across the Amazon secure network. 

 Amazon Inspector Code Security routes inference requests within the geography where the request originates, as shown in the following table. Code Security is available in 10 AWS Regions. 


| Geography | Code Security Regions | 
| --- | --- | 
| United States | US East (N. Virginia)<br />US East (Ohio)<br />US West (Oregon) | 
| Europe | Europe (Frankfurt)<br />Europe (Ireland)<br />Europe (London)<br />Europe (Stockholm) | 
| Japan | Asia Pacific (Tokyo) | 
| Australia | Asia Pacific (Sydney) | 
| Asia Pacific | Asia Pacific (Singapore) | 