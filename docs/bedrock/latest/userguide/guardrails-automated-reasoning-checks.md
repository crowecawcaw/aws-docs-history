# Improve accuracy by adding Automated

Reasoning checks in Amazon Bedrock Guardrails

Automated Reasoning checks in Amazon Bedrock Guardrails mathematically verify natural language content against
your defined policies, ensuring strict compliance with your guardrails. These checks can help to
systematically block harmful or non-compliant content before it reaches your users. Unlike
pattern-matching approaches, Automated Reasoning delivers higher accuracy with fewer false
positives, particularly for complex policy requirements. For customers prioritizing precision,
policy rules can be customized to enhance guardrail effectiveness through clear logic
statements.

A key challenge with large language models (LLMs) is ensuring the accuracy of their
responses. Without validation, LLMs can sometimes produce hallucinations or inaccurate
information that undermines trust.

Automated Reasoning checks in Amazon Bedrock Guardrails solve this problem by using mathematical techniques
to:

- Detect hallucinations in LLM responses
- Highlight unstated assumptions
- Provide explanations for why accurate statements are correct
  This feature is especially valuable when you need to demonstrate the factual basis for an
  LLM's response in:

- Regulated industries like healthcare and human resources
- Applications with complex rules (mortgage approvals, zoning laws)
- Compliance scenarios requiring auditable AI responses
  Automated Reasoning checks in Amazon Bedrock Guardrails will not protect against prompt injection attacks. These
  checks validate exactly what you send them - if malicious or manipulated content is provided as
  input, the validation will be performed on that content as-is (garbage-in, garbage-out). To
  detect and block prompt injection attacks, use [Content
  filters](guardrails-components.md#guardrails-content-filters "guardrails-components.md#guardrails-content-filters") in combination with Automated Reasoning checks.

Automated Reasoning only analyzes and detects text that is relevant to the Automated
Reasoning policy. It will ignore the rest of the content and cannot tell developers whether the
answer is off-topic or not. If you need to detect off-topic responses, use other guardrail
components such as [topic
policies](guardrails-components.md#guardrails-topic-policies "guardrails-components.md#guardrails-topic-policies").

###### Note

Automated Reasoning checks in Amazon Bedrock Guardrails is generally available in US (N.
Virginia, Oregon, and Ohio) and EU (Frankfurt, Paris, Ireland) Regions.

###### Note

Automated Reasoning checks in Amazon Bedrock Guardrails complement other Amazon Bedrock Guardrails features like content filters and
topic policies. For more information, see [Guardrail
components](guardrails-components.md "guardrails-components.md").

CloudFormation is currently not supported. CloudFormation support will be coming
soon.

Automated Reasoning checks in Amazon Bedrock Guardrails currently support English (US) only.

Automated Reasoning checks in Amazon Bedrock Guardrails does not support streaming APIs.

## Limitations and considerations

Before implementing Automated Reasoning checks, be aware of these important
limitations:

- **Document complexity:** Source documents should be
  well-structured with clear, unambiguous rules. Highly complex documents with nested
  conditions or contradictory statements may not extract cleanly into formal logic.
- **Processing time:** Automated Reasoning validation adds
  latency to your application responses. Plan for additional processing time, especially for
  complex policies with many rules.
- **Policy scope:** Each policy should focus on a specific
  domain (for example, HR, finance, legal) rather than trying to cover multiple unrelated
  areas in a single policy.
- **Variable limits:** Policies with excessive numbers of
  variables or overly complex rule interactions may hit processing limits or return
  TOO_COMPLEX results.
- **Natural language dependency:** The accuracy of
  validation depends heavily on how well natural language in user prompts and model
  responses can be translated to your policy's formal logic variables.

## Best practices

Follow these best practices to maximize the effectiveness of your Automated Reasoning
policies:

- **Start simple:** Begin with a focused policy covering
  core rules, then gradually add complexity. Test thoroughly at each stage.
- **Write comprehensive variable descriptions:** Include
  how users might naturally refer to concepts, not just technical definitions from your
  source document.
- **Test edge cases:** Create tests that specifically
  target boundary conditions, exceptions, and unusual scenarios your users might
  encounter.
- **Monitor confidence thresholds:** Start with higher
  confidence thresholds (0.8-0.9) and adjust based on your tolerance for false positives vs.
  false negatives.
- **Regular policy maintenance:** Review and update your
  policies as business rules change or as you identify gaps through testing and production
  use.
- **Document your annotations:** Keep track of policy
  modifications and the reasoning behind them for future reference and team knowledge
  sharing.

## Pricing

Automated Reasoning checks in Amazon Bedrock Guardrails are charged based on the number of validation requests
processed. For current pricing information, see the [Amazon Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").

Charges are incurred for each validation request, regardless of the result (for example,
VALID, INVALID, TRANSLATION_AMBIGUOUS). To optimize costs:

- Use appropriate confidence thresholds to balance accuracy with processing
  requirements
- Consider caching validation results for identical or similar queries when appropriate
  for your use case
- Monitor usage patterns and adjust policies to reduce unnecessary validation
  requests

## Cross-region inference for policy

operations

Automated Reasoning utilizes cross-region inference to optimize the performance and
availability of policy creation and testing operations. Specific API operations automatically
distribute processing across AWS Regions within your geographic boundary to ensure reliable
service delivery.

The following Automated Reasoning API operations employ cross-region inference:

- `StartAutomatedReasoningPolicyBuildWorkflow` - Invoked during policy
  creation and compilation from source documents
- `StartAutomatedReasoningPolicyTestWorkflow` - Invoked during policy
  validation and testing procedures

These operations invoke large language models to extract formal logic rules from source
documents and translate natural language constructs into structured logical representations.
To ensure optimal performance and availability, request processing is distributed according to
the following geographic routing:

- **United States Regions:** API requests originating from
  US East (N. Virginia), US West (Oregon), or US East (Ohio) may be processed in any
  supported US Region.
- **European Union Regions:** API requests originating from
  EU (Frankfurt), EU (Paris), or EU (Ireland) may be processed in any supported EU
  Region.

###### Important

Customer data remains within the originating geographic boundary (United States or
European Union) and is processed in accordance with AWS data residency commitments.
Cross-region inference routes requests exclusively within the same geographic Region to
optimize performance and service availability.

Cross-region inference operates transparently without requiring customer configuration.
API functionality remains consistent regardless of the specific Region that processes the
request.

**To use Automated Reasoning checks in Amazon Bedrock Guardrails, follow these
steps:**

1. **Upload a source document** that contains the rules you
   want to enforce
2. **Review the extracted policy** with automatically
   identified concepts and rules
3. **Test and refine** the policy to ensure it works
   correctly
4. **Deploy the policy** to validate your foundation model's
   responses
   The workflow can be visualized as:

```

Source Document → Extracted Policy → Testing → Deployment → Runtime Validation
    (rules)        (formal logic)    (verify)   (activate)    (check responses)

```

### Policies

Automated Reasoning policies are the foundation of accuracy validation, containing logic
rules and variables that are automatically extracted from your source document. These
policies serve as the mathematical representation of your business rules, enabling the
system to systematically validate whether foundation model responses comply with your
defined constraints. To perform Automated Reasoning checks in your application, you
configure your guardrail to use a policy that matches your specific domain and validation
requirements.

### Rules

Rules are logic that Automated Reasoning extracts from your source document. These might
be written as if-then statements. Here are some examples of the rule format:

`if <premise>, then <claim>`

`<premise> is true`

###### Note

**Important:** Rules that are not in if-then format can
have unintended consequences by laying out axioms about the world. For example, if a rule
simply states `accountBalance > 5`, then it becomes impossible for an account
balance to be 5 or less, regardless of what the content for validation says. The rule has
made it logically impossible for that condition to exist. This could result in unexpected
validation results where content is incorrectly flagged as non-compliant because it
contradicts the axiom established by the rule. To avoid this, structure rules as
conditional statements (if-then format) that describe relationships rather than absolute
constraints.

### Variables

Variables represent concepts in your Automated Reasoning policy that can have values
assigned to them when translating natural language into formal logic. Your policy rules
define constraints on what are valid or invalid values for these variables.

Variables have a name, a type, and a description. For example, a policy about employee
benefits might have a variable with the name "employee_age", the type "integer", and the
description "The age of the employee in years". This variable could be assigned a value like
25 based on natural language in a prompt to an application.

For example, an `is_full_time` variable in an HR policy might have a
description that states "Employees that work more than 20 hours per week," which is a direct
quote from the source document. When using a chatbot, users are more likely to say "I'm
full-time," and not, "I work more than 20 hours per week."

The accuracy of the translation from natural language to formal logic is highly
dependent on the quality of variable descriptions. While the reasoning process is sound once
the translation is complete, clear and comprehensive variable descriptions ensure that user
prompts are correctly interpreted. Without complete variable descriptions, Automated
Reasoning might return `NO_DATA` because it can't translate the input natural
language into its formal logic representation.

It's important for a variable description to account for scenarios like this. A
comprehensive variable description might state, "Employees who work more than 20 hours per
week are full-time. Users will say full-time to set this value to true, or part-time to set
it to false."

#### Predefined

variable types

The following table describes the predefined types of variables that your policy can
have.

| Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bool | Boolean variables can be true or false. For example, in a leave of absence<br>policy, you would use a `bool` variable to identify whether leave of<br>absence is allowed or not.                                                                                                                                                                                                                                                                                                       |
| int  | Numerical `int` variables can store positive or negative whole<br>numbers. For example, in a leave of absence policy, you would use an<br>`int` variable to store the accrued vacation days if fractional<br>days are not allowed.                                                                                                                                                                                                                                                     |
| real | Numerical `real` variables can store positive or negative numbers<br>that need decimal precision. For example, in a leave of absence policy, you<br>would use a `real` variable to store the dollar payment amount for<br>unused vacation days.                                                                                                                                                                                                                                        |
| enum | Enum variables can store a single value selected from a set of fixed<br>options. For example, in a leave of absence policy, you could use an enum<br>variable to store the leave type: (1) Paid Vacation; (2) Personal time; (3)<br>Leave of Absence<br>You can also create custom, user-defined enum types that provide additional<br>context beyond the predefined variable types. These custom types allow you to<br>define specific sets of values relevant to your policy domain. |

###### Topics

- [Create your Automated Reasoning policy](create-automated-reasoning-policy.md "create-automated-reasoning-policy.md")
- [Test an Automated Reasoning policy](test-automated-reasoning-policy.md "test-automated-reasoning-policy.md")
- [Validate your Automated Reasoning policy test results](validate-automated-reasoning-policy-results.md "validate-automated-reasoning-policy-results.md")
- [Address failed Automated Reasoning policy tests](address-failed-automated-reasoning-tests.md "address-failed-automated-reasoning-tests.md")
- [Deploy your Automated Reasoning policy in your application](deploy-automated-reasoning-policy.md "deploy-automated-reasoning-policy.md")
