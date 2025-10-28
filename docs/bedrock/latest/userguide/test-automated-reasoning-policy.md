# Test an Automated Reasoning policy

You test a policy by sending natural language statements or QnAs for validation, then inspect Automated Reasoning checks feedback to ensure it is translating the input text using the right variables and that the rules it's validating against are correct.

You can create tests in two ways: manually defining question-and-answer (QnA) pairs or automatically generating test scenarios. QnAs are specific user questions with corresponding model responses that you write to test particular use cases, while test scenarios are logical situations automatically generated from your policy rules that may or may not be realistic in your application context.

###### Note

**Tutorial video:** For a step-by-step walkthrough of testing an Automated Reasoning policy, watch the following tutorial:

[Tutorial Demo 2 - Testing the Automated Reasoning policy](https://youtu.be/a_NLNMdm33M "https://youtu.be/a_NLNMdm33M")

Tests should mimic the questions your application's users would ask and the responses they might get from a foundation model. Automated Reasoning assesses the prompt and response accuracy with respect to the rules in your Automated Reasoning policy. Automated Reasoning performs this validation in the following steps:

###### Tip

**Best practice:** Create tests that cover both valid and invalid scenarios. For example, if your policy states "Employees need 1 year of service for parental leave," create tests for responses that correctly state this rule and tests for responses that incorrectly state a different requirement.

1. Uses your test's question and answer along with your policy's variables and their descriptions to translate the natural language inputs into formal logic.
2. Validates the translated logic against the policy by using sound mathematical techniques.

###### Note

Automated Reasoning translates natural language into logic using AI techniques that cannot guarantee perfect accuracy. However good tests will help detect and fix possible inaccuracies in your Automated Reasoning policies.

## Create a test manually in the console

1. Go to the Automated Reasoning policy that you want to test (for example,
   **MyHrPolicy**).
2. Choose **View tests**, then select **Add**.
3. In the **Add tests** dialog, do the following:
   1. Include an input (optional) and output. These represent the question a user might ask and the response your foundation model might provide - together forming a QnA pair that tests how your policy validates real user interactions.
   2. Choose the result you expect from the test (such as **Valid** or **Invalid**).
   3. Select a **Confidence threshold**, which is the minimum confidence level for logic validation.

4. Select **Save** to create the test.

###### Note

When creating a test, the confidence threshold is optional.

- Automated Reasoning checks uses multiple large language models (LLMs) to translate natural language tests into findings. It returns only "confident" findings that are supported by a significant percentage of the LLM translations. The confidence threshold defines the minimum percentage of support needed for a translation to become a finding with a validity result.
- If there are one or more translated findings that are not supported by a sufficient percentage of LLM translations, Automated Reasoning checks will surface an additional "TRANSLATION_AMBIGUOUS" finding. This finding will contain information to highlight the differences between the disagreeing LLM translations.

## Generate tests automatically in the console

1. Go to the Automated Reasoning policy that you want to test (for example, _MyHrPolicy_).
2. Choose **View tests**, then select **Generate**.
3. In the **Generate scenarios** dialog, review the generated scenario and related rules. Then do one of the following:
   - If you think the scenario could happen (also known as a _satisfiable_ scenario), select the thumbs up (yes).
   - If not, select the thumbs down (no). You can also provide an annotation to explain why you think the scenario isn't possible. This is similar to leaving a comment in a document.
   - If you want a different scenario to test, choose **Regenerate scenario**.

###### Tip

If you want to inspect the formal logic version of the scenario, enable **Show SMT-LIB**. 4. Select **Save and close** to save the test or **Save and add another** test. 5. If you provided annotations to any of the tests, choose **Apply
annotations**. Automated Reasoning will make changes to your policy based on
your feedback. 6. On the **Review policy changes** screen, review the changes to your policy's rules, variables, and variable types. Then select **Accept changes**.

## Run tests in the console

1. Go to the Automated Reasoning policy that you want to validate (for example,
   **MyHrPolicy**).
2. Choose **View tests**.
3. Do one of the following:
   - To run all of your policy's tests, choose **Validate all tests**.
   - To run tests individually, select the **Action** button next to the test that you want to run and choose **Validate**.

## Create a test manually using the API

You can use the `CreateAutomatedReasoningPolicyTestCase` API operation to create a test for your Automated Reasoning policy programmatically.

### Request parameters

The following parameters are required or optional when creating a test:

`policyArn` (required)

The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to create the test.

`guardContent` (required)

The output content that's validated by the Automated Reasoning policy. This represents the foundation model response that will be checked for accuracy.

`query` (optional)

The input query or prompt that generated the content. This provides context for the validation.

`expectedAggregatedFindingsResult` (optional)

The expected validation result for the test (for example, `VALID` or
`INVALID`).

`confidenceThreshold` (optional)

The minimum confidence level for logic validation. Content that meets the threshold is considered a high-confidence finding that can be validated.

### Example

The following example shows how to create a test for an Automated Reasoning policy using
the AWS CLI:

```
aws bedrock create-automated-reasoning-policy-test-case \
  --policy-arn "arn:aws:bedrock:us-west-2:123456789012:automated-reasoning-policy/k8m9n2p4q7r5" \
  --query-content "Can I take a leave of absence if I'm a part-time employee?" \
  --guard-content "No, only full-time employees are eligible for leave of absence." \
  --expected-aggregated-findings-result "VALID" \
  --confidence-threshold 0.8
```

Example response:

```
{
  "testCaseId": "test-12345abcde",
  "policyArn": "arn:aws:bedrock:us-west-2:123456789012:automated-reasoning-policy/k8m9n2p4q7r5"
}
```

## Generate tests automatically using the API

You can use the `GenerateAutomatedReasoningPolicyTestScenarios` API operation to automatically generate test scenarios based on your policy's rules.

### Request parameters

The following parameters are required or optional when generating test scenarios:

`policyArn` (required)

The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to generate test scenarios.

`maxResults` (optional)

The maximum number of test scenarios to generate.

### Example

The following example shows how to generate test scenarios for an Automated Reasoning
policy using the AWS CLI:

```
aws bedrock generate-automated-reasoning-policy-test-scenarios \
  --policy-arn "arn:aws:bedrock:us-west-2:123456789012:automated-reasoning-policy/k8m9n2p4q7r5" \
  --max-results 3
```

The response will include generated test scenarios that you can review and use to create tests.

## Run tests using the API

You can use the `ValidateAutomatedReasoningPolicyTest` API operation to run a test for your Automated Reasoning policy and the `GetAutomatedReasoningPolicyTestResult` operation to retrieve the results.

### Request parameters

The following parameters are required when running a test:

`policyArn` (required)

The Amazon Resource Name (ARN) of the Automated Reasoning policy.

`testCaseId` (required)

The unique identifier of the test to run.

### Get test results

To retrieve the results of a test, use the following parameters:

`policyArn` (required)

The Amazon Resource Name (ARN) of the Automated Reasoning policy.

`buildWorkflowId` (required)

The build workflow identifier. The build workflow must display a `COMPLETED` status to get results.

`testCaseId` (required)

The unique identifier of the test for which to retrieve results.

### Example

The following example shows how to run a test and retrieve the results using the
AWS CLI:

```
# Run the test
aws bedrock validate-automated-reasoning-policy-test \
  --policy-arn "arn:aws:bedrock:us-west-2:123456789012:automated-reasoning-policy/k8m9n2p4q7r5" \
  --test-case-id "test-12345abcde"

# Get the test results
aws bedrock get-automated-reasoning-policy-test-result \
  --policy-arn "arn:aws:bedrock:us-west-2:123456789012:automated-reasoning-policy/k8m9n2p4q7r5" \
  --build-workflow-id "workflow-67890fghij" \
  --test-case-id "test-12345abcde"
```

The response will include detailed test results with validation findings and execution status.
