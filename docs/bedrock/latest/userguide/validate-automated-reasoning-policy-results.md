# Validate your Automated Reasoning policy test results

When a test finishes, you're provided with a set of validation results to understand how your Automated Reasoning policy is performing.

A test includes the following information:

- **Query** and **Content**: A question a user might ask your GenAI application and a possible response. You define these if you manually create the test. Automated Reasoning defines these if you generated test scenarios.
- **Confidence threshold**: The minimum confidence level for logic validation that you set for your test. This threshold determines how Automated Reasoning handles uncertainty in translating natural language to formal logic. Content that meets or exceeds the threshold is considered a high-confidence finding that can be validated with a definitive result (VALID or INVALID). Content that falls below the threshold is a low-confidence finding that's marked as TRANSLATION_AMBIGUOUS, indicating the system detected ambiguity and chose not to provide a potentially incorrect validation result.
- **Validation results**:
  - **Expected result**: The result you expect from running the test.
  - **Actual result**: The result from running the test.
  - **Execution result**: Indicates whether the test passed. If the expected and actual results align, the test passed. If not, the test failed.

- **Findings**: The output from an Automated Reasoning policy test is a set of _findings_. Findings represent factual claims contained in your test question and answer. Use these to help you understand why a test passed or failed.
  - **Type**: Translations can include a combination of _claims_ and _premises_.
    - **Premises**: Provides context, assumptions, or conditions that affect how a claim should be evaluated. In question-and-answer formats, the premise is often the question itself. Answers can also contain premises that establish constraints or conditions. For example, in the question, "What numbers are divisible by 2?" and answer, "Even numbers", the premise is "numbers divisible by 2". In the statement, "When the traffic light turns green, you must go," the premises is "traffic light is green".
    - **Claims**: Factual statements that Automated Reasoning evaluates for accuracy. In a question-and-answer format, the claim is typically the answer. In a standalone statement, the claim is the fact being asserted. For example, in the question, "What numbers are divisible by 2?" and answer, "Even numbers", the claim is "even numbers".

  - **Result**: Indicates how valid a finding's claims are. For more information, see [Test validation results](#automated-reasoning-test-validation-results "#automated-reasoning-test-validation-results").
  - **Confidence**: The confidence score (ranging from 0.0 to 1.0) that Automated Reasoning has in the translation from natural language to formal logic, representing how certain the system is about correctly interpreting the input text. Higher scores indicate greater certainty in the translation. For example, if a translation has a confidence of "1.0", that indicates maximum certainty that the natural language was accurately converted to formal logic. Lower confidence scores suggest the system has some uncertainty about the translation that you may want to review.
  - **Assignments**: Variable assignments from your policy that prove the finding is valid or not. Translations have logic statements that show how the natural language was converted to formal logic. These can be more complex when there is nested logic. For example, `hasDogHistoryOfAggression is false`.
  - **Rules**: The extracted logic from your policy that supports the finding. A test provides you with enough relevant rules from your policy to help you understand the finding result.

## Test validation results

The following list details possible validation results from an Automated Reasoning policy test:

`VALID`

The claims in the model's response are logically consistent with your policy rules and can be mathematically proven correct. The response correctly follows all applicable logical constraints and the reasoning from premises to conclusions is sound.

**Example:** If your policy states "Employees with 1+ year of service get parental leave" and the model responds "You qualify for parental leave since you've worked here for 18 months," this would be VALID because 18 months exceeds the 1-year requirement.

`INVALID`

The claims in the model's response contradict or violate your policy rules. The response contains statements that are mathematically provable as incorrect based on your policy's formal logic constraints.

**Example:** If your policy states "Employees with 1+ year of service get parental leave" and the model responds "You qualify for parental leave even though you've only worked here for 3 months," this would be INVALID because 3 months doesn't meet the 1-year requirement.

`SATISFIABLE`

The claims are consistent with at least one possible interpretation of your policy rules, but may not address all relevant rules. This means the response doesn't contradict your policy, but it might not fully address all applicable constraints.

**Example:** If your policy states "Employees need 1+ year of service for parental leave AND must submit form HR-101" and the model responds "You qualify for parental leave since you've worked here for 2 years," this would be SATISFIABLE because the response correctly addresses the service requirement but doesn't mention the form requirement (without contradicting it).

`IMPOSSIBLE`

Automated Reasoning can't make a statement about the claims. This can happen if the premises are logically incorrect, or if there is a conflict within the Automated Reasoning policy itself.

**Example:** If your policy contains contradictory rules like "All employees get vacation days" and "No employees get vacation days," or if the test question contains impossible premises like "What benefits do employees get if they work negative hours?", the result would be IMPOSSIBLE because the logical foundation is flawed.

`TRANSLATION_AMBIGUOUS`

Detected an ambiguity in the translation meant it would be unsound to continue with validity checking. Additional context or follow-up questions might be needed to get translation to succeed.

**Example:** If your test question is "Can they take leave?" without specifying who "they" refers to, or if the model response uses ambiguous pronouns like "It depends on their situation" without clear referents, the result would be TRANSLATION_AMBIGUOUS because the system cannot reliably translate the vague language into formal logic.

`TOO_COMPLEX`

The input contains too much information for Automated Reasoning to process within its latency limits.

**Example:** If your test includes an extremely long model response with hundreds of interconnected claims about employee benefits, vacation policies, health insurance, retirement plans, and performance reviews all in a single response, the result might be TOO_COMPLEX because the logical analysis would exceed processing time limits.

`NO_TRANSLATIONS`

Identifies that some or all of the input prompt wasn't translated into logic. This can happen if the input isn't relevant to the Automated Reasoning policy, or if the policy doesn't have variables to model relevant input. If Automated Reasoning can't translate anything, you get a single `NO_TRANSLATIONS` finding. You might also see a `NO_TRANSLATIONS` (along with other findings) if some part of the validation isn't translated.

**Example:** If your HR policy is designed to validate employee benefits but your test question asks "What's the weather like today?" or "How do I cook pasta?", the result would be NO_TRANSLATIONS because the content is completely unrelated to your policy's domain and variables.
