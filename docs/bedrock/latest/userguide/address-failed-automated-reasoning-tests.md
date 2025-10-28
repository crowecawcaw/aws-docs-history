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

**Problem:** Policy approved leave for employee with 8 months tenure, but source document requires 1+ years.

**Original rule:**

```
if is_full_time = true, then eligible_for_parental_leave = true
```

**Annotation applied:**

1. Added `years_of_service` variable (real type)
2. Updated rule to: `if is_full_time = true and years_of_service >= 1.0, then eligible_for_parental_leave = true`
3. Test now correctly returns INVALID for 8-month employee

- Update the failed test's conditions and rerun it. If you the test returns the validation result you expect, you can apply this annotation to update your policy.
- Update your policy's variable names or descriptions to help Automated Reasoning distinguish between them as it translates natural language into logic.
- Update your policy's rules if you believe that Automated Reasoning misunderstood your source document or your source document contains errors.
- Edit your policy's logic by adding variables and types. You can then update your rules to use the new variables. This is an advanced use case that we typically don't recommend.
- Recreate your policy with more comprehensive instructions. The instructions should include enough context so that Automated Reasoning can extract logic that's relevant to how your application will be used. We also recommend including example questions and answers that you expect to be asked about your source document.

## When it's impossible to provide guidance

In some cases, Automated Reasoning may indicate that it's impossible to provide guidance for a failed test. This typically occurs when there are fundamental issues with the policy structure that prevent clear analysis. When this happens, you should inspect your policy rules and look for conflicts.

Common scenarios where guidance cannot be provided include:

- **Conflicting rules**: Your policy contains contradictory rules that create logical inconsistencies. For example, one rule might state that full-time employees are eligible for leave, while another rule states that employees with less than one year of service are not eligible, without specifying how to handle full-time employees with less than one year of service.
- **Incomplete rule coverage**: Your policy has gaps where certain combinations of conditions are not addressed by any rules, making it impossible to determine the correct outcome.
- **Circular dependencies**: Rules that depend on each other in a way that creates logical loops, preventing the system from reaching a definitive conclusion.
- **Overly complex rule interactions**: When multiple rules interact in ways that create ambiguous or contradictory outcomes for specific test scenarios.

**To address these issues:**

1. **Review your policy rules systematically**: Go through each rule in your policy and identify any that might conflict with others. Look for rules that could apply to the same scenario but produce different outcomes.
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
   `is_full_time`. If you expected the input Q&A to match a specific rule, first
   check that the **Variables** from the input Q&A are correct. If they are,
   you might need to add a new rule.
3. Use the **Add** button at the top-right of the rules list to enter a new
   rule. Use natural language to specify the rule. Specify constraints first and reference
   variables by their full name. For example, for a rule that only allows full-time employees to
   take leave of absence, the text could be something like, "If an employee
   `is_full_time`, then they are allowed to take leave of absence, paid
   (LoAP)".

## Automated reasoning policy returns `TRANSLATION_AMBIGUOUS`

### Common causes

If your policy returns `TRANSLATION_AMBIGUOUS`, this indicates that Automated Reasoning detected ambiguity in translating natural language to formal logic. This occurs when the system cannot definitively determine how to map natural language concepts to the formal logic variables and rules in your policy.

Translation ambiguity can arise from several underlying causes:

- **Overlapping variable definitions**: When multiple variables in your policy could reasonably represent the same concept mentioned in natural language, the system cannot determine which variable to use. For example, if you have both `employee_tenure_years` and `years_of_service` variables with similar descriptions, the system may struggle to determine which one to use when a user asks about "how long someone has worked at the company." This creates ambiguity in the translation process and can lead to inconsistent results.
- **Incomplete variable descriptions**: Variable descriptions that lack sufficient detail about how users might refer to concepts in everyday language, making it difficult to map user input to the correct formal logic representation.
- **Ambiguous natural language input**: User prompts or model responses that contain vague, contradictory, or multi-interpretable statements that cannot be clearly translated into formal logic.
- **Missing contextual information**: When the natural language refers to concepts that exist in your domain but are not adequately represented in your policy's variable schema.
- **Inconsistent terminology**: When the same concept is referred to using different terms in your source document, variable descriptions, and user interactions, creating confusion during translation.

Understanding these causes can help you debug issues with your tests and determine what changes to make to your policy. In some cases, you may need to adjust the confidence level settings for your policy to better balance between strict accuracy and practical usability in your specific use case.

### Resolution

There are several ways to correct this depending on the underlying issue:

- **Variable descriptions are too similar**: When two variables have similar names or descriptions, the translation process might inconsistently choose between them. For example, if you have both `is_full_time` and `full_time_status` variables with similar descriptions, the system may not consistently map natural language about employment status to the correct variable. Review your variable descriptions so that each has clearly differentiated purposes and contexts. Consider consolidating duplicate concepts into a single variable or ensuring each variable has a distinct purpose with clear, non-overlapping descriptions that specify exactly when each should be used.
- **Insufficient variable context**: Your variable descriptions might not adequately cover how users can refer to concepts in your domain. Update your variable descriptions with the right level of context.
- **Inconsistent value formatting**: Translation ambiguity can occur when the system is unsure how to format values (such as numbers or dates). Update your variable descriptions to clarify expected formats.
- **Ambiguous input**: If the input text contains ambiguous
  statements, revise them to be more precise.

You can use one of the following prompts to correct translation ambiguity issues:

**Ambiguity without source**

```
You are an expert in revising answers to questions based on logical disagreements found in the answers.
Given a domain, a question, an original answer, and logical ambiguities suggested from scearios, your task is to revise the original answer to address and resolve the logical ambiguities identified above. The revised answer should remove any ambiguities, such that one can clearly judge whether each scenario is consistent or inconsistent with the answer. The revised answer should have approximately the same length as the original answer. Avoid extending the answer with your own background knowledge.
Below is an example.
DOMAIN: DiscountPolicy
QUESTION: I want to buy tickets for next Thursday. How many people are needed to qualify for your group discount?
ORIGINAL ANSWER: You need at least 10 people to get the group discount.
LOGICAL AMBIGUITIES FOUND: disagree_scenario1: ['(= group_size 12)', '(= advanced_booking false)', '(= group_discount true)']
(Analysis: The scenario says the group size is 12, there is no advanced booking and group discount is true. Is this consistent with the answer? Well, the original answer does not mention advanced booking. Maybe the answer assumed advanced booking from the question "I want to buy tickets for next Thursday", but that's debatable. The revised answer should make it clear.)
REVISED ANSWER: You need at least 10 people and need to book in advance to get the group discount.
(Note: Scenarios are illustrative cases highlighting potential ambiguities. Do not overfit in your revised answer. In the example above, you should use the original "You need at least 10 people..." rather than the scenario-specific "If you have 12 people...")
Now complete the following task and return the revised answer. (Just return the answer. Do not return any analysis or notes)
DOMAIN: {domain}
QUESTION: {question}
ORIGINAL ANSWER: {original_answer}
LOGICAL AMBIGUITIES FOUND: It is unclear if the following scenarios are valid or not according to the answer. {disagreement_text}
REVISED ANSWER:
```

**Ambiguity with source**

```
You are an expert in revising answers to questions based on logical disagreements found in the answers.
Given a domain, a question, an original answer, a piece of policy source text, and logical ambiguities suggested from scearios, your task is to revise the original answer to address and resolve the logical ambiguities identified above. The revised answer should remove any ambiguities, such that one can clearly judge whether each scenario is consistent or inconsistent with the answer. The revised answer should have approximately the same length as the original answer. Avoid extending the answer with your own background knowledge. The revised answer should be consistent with the actual policy from the source text.
Below is an example.
DOMAIN: DiscountPolicy
QUESTION: I want to buy tickets for next Thursday. How many people are needed to qualify for your group discount?
ORIGINAL ANSWER: You need at least 10 people to get the group discount.
POLICY SOURCE TEXT: ... We offer discounts to students, seniors, and large groups. Students must present a valid ID ... A group of ten or more people are qualified for a group discount. Group discount tickets must be booked in advance. Each group ticket is 20% off the regular ticket price ...
LOGICAL AMBIGUITIES FOUND: disagree_scenario1: ['(= group_size 12)', '(= advanced_booking false)', '(= group_discount true)']
(Analysis: The scenario says the group size is 12, there is no advanced booking and group discount is true. Is this consistent with the answer? Well, the original answer does not mention advanced booking. Maybe the answer assumed advanced booking from the question "I want to buy tickets for next Thursday", but that's debatable. The revised answer should make it clear.)
REVISED ANSWER: You need at least 10 people and need to book in advance to get the group discount.
(Note: Scenarios are illustrative cases highlighting potential ambiguities. Do not overfit in your revised answer. In the example above, you should use the original "You need at least 10 people..." rather than the scenario-specific "If you have 12 people...")
Now complete the following task and return the revised answer. (Just return the answer. Do not return any analysis or notes)
DOMAIN: {domain}
QUESTION: {question}
ORIGINAL ANSWER: {original_answer}
POLICY SOURCE TEXT: {policy_source_text}
LOGICAL DISAGREEMENTS FOUND: It is unclear if the following scenarios are valid or not according to the answer. {disagreement_text}
REVISED ANSWER:
```
