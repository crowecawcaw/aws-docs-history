# Address failed Automated Reasoning policy tests

If a test of your Automated Reasoning policy fails, review the extracted logic and rules in the test findings. There are several ways to address the failure depending on the issue:

###### Note

**Tutorial video:** For a step-by-step walkthrough of refining and troubleshooting an Automated Reasoning policy, watch the following tutorial:

[Tutorial Demo 3 - Refining the Automated Reasoning policy](https://youtu.be/YmohVGWr_PA "https://youtu.be/YmohVGWr_PA")

## Understanding annotations

Annotations are corrections you apply to repair your policy when tests fail. If a test doesn't return your expected result, you can modify the test conditions, rerun it, and apply the successful modification as an annotation to update your policy.

Use annotations to:

- Fix incorrect rules
- Add missing variables
- Improve variable descriptions
- Resolve translation ambiguities

### Example: Policy repair annotation

**Problem:** Policy approved leave for all full time employees, but source document requires 1+ years.

**Original rule:**

```
if isFullTime is true, then eligibleForParentalLeave is true
```

**Annotation applied:**

1. Added `tenureMonths` variable (INT type)
2. Updated rule to: `if isFullTime is true and tenureMonths is greater than 12, then eligibleForParentalLeave is true`
3. Test now correctly returns INVALID for employees with less than 12 months of tenure

- Update the failed test's conditions and rerun it. If you the test returns the validation result you expect, you can apply this annotation to update your policy.
- Update your policy's variable names or descriptions to help Automated Reasoning distinguish between them as it translates natural language into logic.
- Update your policy's rules if you believe that Automated Reasoning misunderstood your source document or your source document contains errors.
- Edit your policy's logic by adding variables and types. You can then update your rules to use the new variables. This is an advanced use case that we typically don't recommend.
- Recreate your policy with more comprehensive instructions. The instructions should include enough context so that Automated Reasoning can extract logic that's relevant to how your application will be used. We also recommend including example questions and answers that you expect to be asked about your source document.

## When it's impossible to provide guidance

In some cases, Automated Reasoning may indicate that it's impossible to provide guidance for a failed test. This typically occurs when there are fundamental issues with the policy structure that prevent clear analysis.

Common scenarios where guidance cannot be provided include:

- **Conflicting rules**: Your policy contains contradictory rules that create logical inconsistencies. For example, one rule might state that full-time employees are eligible for leave, while another rule states that employees with less than one year of service are not eligible, without specifying how to handle full-time employees with less than one year of service.
- **Incomplete rule coverage**: Your policy has gaps where certain combinations of conditions are not addressed by any rules, making it impossible to determine the correct outcome.
- **Circular dependencies**: Rules that depend on each other in a way that creates logical loops, preventing the system from reaching a definitive conclusion.
- **Overly complex rule interactions**: When multiple rules interact in ways that create ambiguous or contradictory outcomes for specific test scenarios.

**To address these issues:**

1. **Review your policy rules systematically**: the definitions page in the console will show warnings around rules that are in conflict, unused variables, and unused values incustom types. The same information is available in the `QUALITY_REPORT` asset from the `GetAutomatedReasoningPolicyBuildWorkflowResultAssets` API action.
2. **Check for rule completeness**: Ensure that your rules cover all possible combinations of conditions that might occur in your domain. Identify any gaps where no rule applies.
3. **Simplify complex interactions**: If you have many interconnected rules, consider breaking them down into simpler, more focused rules that are easier to understand and validate.
4. **Test edge cases**: Create additional tests that specifically target the boundary conditions and edge cases in your policy to identify where conflicts or gaps might exist.
5. **Consider policy restructuring**: If conflicts persist, you may need to restructure your policy with clearer rule hierarchies or precedence orders to resolve ambiguities.

When you encounter this situation, it's often helpful to start with a simpler version of your policy and gradually add complexity while testing at each step to identify where conflicts are introduced.

The following examples are common reasons why a test might fail and how to address them.

## Automated reasoning doesn't understand the source document

### Common cause

Automated Reasoning might not have extracted all the necessary variables from your source document, or the variable descriptions might not be clear enough for proper translation from natural language to formal logic.

### Resolution

1. Review the **Variables** list on the **Definition** screen to verify that all variables needed to extract factual claims from your question and answer are present in your policy.
2. If a required variable is missing:
   1. Choose **Add** to create a new variable.
   2. Select the appropriate type (bool, int, real, or enum).
   3. Write a clear, comprehensive variable description.

3. If a variable exists but wasn't properly assigned during the question and answer validation, improve its description to help Automated Reasoning better translate natural language. For example:

**Original description (too limited):**
"Employees working more than 20 hours per week."

**Improved description:**
"Employees working more than 20 hours per week are considered full-time. Set this value to true when users mention being 'full-time' or working full hours, and false when they mention being 'part-time' or working reduced hours."

## The rules in your Automated Reasoning policy are wrong

### Common cause

Automated Reasoning might have misinterpreted your source document, or your source document
might contain errors or inconsistencies.

### Resolution

1. If the validation output quotes an incorrect rule, edit the rule. You likely would first
   notice this because a test came back as `VALID` when you expected it to be
   `INVALID`.
2. When referencing variables in the rule, use the full variable name that's specified in
   the **Definitions** section of the policy. For example, spell out
   `isFullTime`. If you expected the input Q&A to match a specific rule, first
   check that the **Variables** from the input Q&A are correct. If they are,
   you might need to add a new rule.
3. Use the **Add** button at the top-right of the rules list to enter a new
   rule. Use natural language to specify the rule. Specify constraints first and reference
   variables by their full name. For example, for a rule that only allows full-time employees to
   take leave of absence, the text could be something like, "If an employee
   `isFullTime`, then they are allowed to take leave of absence, paid
   (LoAP)".

## Automated reasoning policy returns `TRANSLATION_AMBIGUOUS`

### Common causes

If your policy returns `TRANSLATION_AMBIGUOUS`, this indicates that Automated Reasoning detected ambiguity in translating natural language to formal logic. This occurs when the system cannot definitively determine how to map natural language concepts to the formal logic variables and rules in your policy.

Translation ambiguity can arise from several underlying causes:

- **Overlapping variable definitions**: When multiple variables in your policy could reasonably represent the same concept mentioned in natural language, the system cannot determine which variable to use. For example, if you have both `tenureMonths` and `monthsOfService` variables with similar descriptions, the system may struggle to determine which one to use when a user asks about "how long someone has worked at the company." This creates ambiguity in the translation process and can lead to inconsistent results.
- **Incomplete variable descriptions**: Variable descriptions that lack sufficient detail about how users might refer to concepts in everyday language, making it difficult to map user input to the correct formal logic representation.
- **Ambiguous natural language input**: User prompts or model responses that contain vague, contradictory, or multi-interpretable statements that cannot be clearly translated into formal logic.
- **Missing contextual information**: When the natural language refers to concepts that exist in your domain but are not adequately represented in your policy's variable schema.
- **Inconsistent terminology**: When the same concept is referred to using different terms in your source document, variable descriptions, and user interactions, creating confusion during translation.

Understanding these causes can help you debug issues with your tests and determine what changes to make to your policy. In some cases, you may need to adjust the confidence level settings for your policy to better balance between strict accuracy and practical usability in your specific use case.

### Resolution

There are several ways to correct this depending on the underlying issue:

- **Variable descriptions are too similar**: When two variables have similar names or descriptions, the translation process might inconsistently choose between them. For example, if you have both `isFullTime` and `fullTimeStatus` variables with similar descriptions, the system may not consistently map natural language about employment status to the correct variable. Review your variable descriptions so that each has clearly differentiated purposes and contexts. Consider consolidating duplicate concepts into a single variable or ensuring each variable has a distinct purpose with clear, non-overlapping descriptions that specify exactly when each should be used.
- **Insufficient variable context**: Your variable descriptions might not adequately cover how users can refer to concepts in your domain. Update your variable descriptions with the right level of context.
- **Inconsistent value formatting**: Translation ambiguity can occur when the system is unsure how to format values (such as numbers or dates). Update your variable descriptions to clarify expected formats.
- **Ambiguous input**: If the input text contains ambiguous statements, use the disagreements between the alternative interprestations to revise them to be more precise.
