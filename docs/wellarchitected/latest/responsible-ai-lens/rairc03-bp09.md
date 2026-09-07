

# RAIRC03-BP09 Measure security risks and threats
<a name="rairc03-bp09"></a>

 Consider quantitative measurements of security risks to AI systems, such as measuring adversarial attack success rates. For example, measure the rate of successful prompt injection attempts, prompt injection detection rates, jailbreaking success rate, guardrail bypass rates, and model extraction resistance (measuring how simply model parameters or behavior can be reverse engineered). 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation considerations
<a name="implementation-considerations-38"></a>

1.  Track metrics such as the percentage of prompt injections that successfully change your system's behavior, how many jailbreaking attempts bypass your guardrails, and whether attackers can extract sensitive information about your model's architecture or training data. 

1.  Measure attack detection accuracy. Determine the correct balance between blocking suspected attacks and not blocking legitimate user inputs. 

1.  Test your defenses with advanced attack combinations like prompt injections embedded within seemingly innocent requests or multi-turn conversations that gradually escalate toward harmful content. See if your security holds up when attackers chain techniques together or adapt their methods based on your system's responses. 

1.  Include red teaming exercises where security experts attempt to break your system using creative attack methods you might not have considered. 

## Resources
<a name="resources-36"></a>

 **Related documents** 
+  [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and validation 

 **Related tools** 
+  [Threat Composer](https://github.com/awslabs/threat-composer?tab=readme-ov-file) 
+  [Metrics in Amazon Cloudwatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) 
+  [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) 