

# Opting out of using your data for service improvement
<a name="omni-opting-out-of-using-your-data-for-service-improvement"></a>

CloudWatch Omni does not use your content to develop or improve the service or its AI features, and your content is not used to train any foundation models. Your content is used only to provide the service to you.

Some CloudWatch Omni features send your content to other AWS services to process. Those services have their own policies, and for some of them you can opt out of having your content used for service improvement. This page describes what each service does and how to opt out where an opt-out is available.

**How CloudWatch Omni uses your content**

CloudWatch Omni processes the telemetry you send, and your input to its AI features, only to provide the service to you: to answer your questions, run your queries and evaluations, and render your dashboards. It does not retain that content for service improvement, and it does not use it for model training.

For where those requests are processed, and the Regions they can reach, see [Cross-Region inference in CloudWatch Omni](omni-cross-region-inference-in-cloudwatch-omni.md).

**Other AWS services that process your content**

Several features send your content to another AWS service. CloudWatch Omni makes those calls using your own AWS credentials, in your own AWS account.


| Feature | Content sent | AWS service | 
| --- | --- | --- | 
| The Omni agent, AI-assisted dashboard creation, and AI-assisted summaries | Your questions and the responses, and the telemetry from your space that is used to answer them | Amazon Bedrock | 
| Prompt playground | The prompt you enter, any context you attach, and the model response | Amazon Bedrock | 
| Evaluations | The agent input, output, and trace content that is scored, and the evaluation instructions | Amazon Bedrock, Amazon Bedrock AgentCore | 
| Voice input and voice playback | The audio you record, its transcription, and the text that is read back to you | Amazon Transcribe, Amazon Polly | 

**Amazon Bedrock**

Amazon Bedrock does not use your inputs or outputs to train models or to improve the service, and does not share them with model providers. For more information, see the [Amazon Bedrock FAQs](https://aws.amazon.com/bedrock/faqs/). Amazon Bedrock is not one of the services covered by the AI services opt-out policy, because it does not use your content for service improvement.

For certain models, Amazon Bedrock retains model inputs and outputs for up to 30 days to detect abuse. Abuse detection is separate from service improvement and is not governed by the AI services opt-out policy. For more information, see [Amazon Bedrock abuse detection](https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html) in the *Amazon Bedrock User Guide*.

**Amazon Bedrock AgentCore**

Amazon Bedrock AgentCore processes content for evaluations that run against an agent runtime. AgentCore states that it "may use and store your content to improve your service experience or performance," and that "such improvements would be for your use of AgentCore and not for other customers." For more information, see [What is Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) in the *Amazon Bedrock AgentCore Developer Guide*.

AgentCore is not covered by the AI services opt-out policy.

**Amazon Transcribe and Amazon Polly**

Amazon Transcribe and Amazon Polly process the audio and text for voice input and voice playback. Both services can use content for service improvement, and both are covered by the AI services opt-out policy. To opt out for these services, create an AI services opt-out policy that includes the `transcribe` and `polly` service keys.

```
{
    "services": {
        "transcribe": {
            "opt_out_policy": {
                "@@assign": "optOut"
            }
        },
        "polly": {
            "opt_out_policy": {
                "@@assign": "optOut"
            }
        }
    }
}
```

For instructions, see [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html) in the *AWS Organizations User Guide*.

**Opting out for other Amazon CloudWatch AI features**

Other Amazon CloudWatch features that use artificial intelligence (including natural language query generation for CloudWatch Metrics Insights and CloudWatch Logs Insights, and CloudWatch investigations) can use your content for service improvement. Those features are covered by the AI services opt-out policy under the `cloudwatch` service key. Opting out with that key does not change CloudWatch Omni, which does not use your content for service improvement.

```
{
    "services": {
        "cloudwatch": {
            "opt_out_policy": {
                "@@assign": "optOut"
            }
        }
    }
}
```

**Note**  
An AI services opt-out policy is set in AWS Organizations, not in CloudWatch. Your organization must have all features enabled, and you must enable the AI services opt-out policy type before you can attach a policy. The policy applies to every account in the organization or organizational unit that you attach it to. A standalone account that is not part of an organization cannot use an AI services opt-out policy.

**Limiting what enters your telemetry**

Whether a service may use your content for improvement is separate from what your telemetry contains. To keep model prompt and response text out of your traces entirely, configure your instrumentation to omit it. See [Protect sensitive data](omni-data-protection.md).