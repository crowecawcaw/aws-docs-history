

# Selective optimization
<a name="advanced-prompt-optimization-selective"></a>

By default, Advanced Prompt Optimization rewrites any part of your entire prompt template end-to-end. With selective optimization, you control exactly which sections of your prompt the optimizer can modify. Use selective optimization when your prompt is large or complex and some sections are already well-tuned. This lets you improve only the parts that still need work.

## Tag syntax
<a name="advanced-prompt-optimization-selective-tags"></a>

Annotate your prompt template with reserved XML-style tags using the `advpo:` (Advanced Prompt Optimization) namespace to control optimization scope:
+ `<advpo:optimize>...</advpo:optimize>` – Marks a section as the focus area for optimization. The optimizer rewrites content inside these tags.
+ `<advpo:exclude>...</advpo:exclude>` – Marks a section as frozen. The optimizer does not modify content inside these tags under any circumstances.

The `advpo:` namespace prefix prevents conflicts with prompts that already use XML-like markup for other purposes.

## How the optimizer determines what to rewrite
<a name="advanced-prompt-optimization-selective-modes"></a>

The optimizer's behavior depends on which tags are present in your prompt template.


| Tags present | Behavior | Mode | 
| --- | --- | --- | 
| No tags | Entire prompt is optimized end-to-end (same as current behavior) | Legacy mode | 
| At least one `<advpo:optimize>` | The optimizer rewrites only content inside `<advpo:optimize>` blocks. All untagged content is preserved. | Explicit inclusion mode | 
| Only `<advpo:exclude>` tags (no `<advpo:optimize>`) | The optimizer rewrites everything that is not inside `<advpo:exclude>` blocks | Exclusion-only mode | 
| Both tag types present | Explicit inclusion mode applies. The optimizer rewrites only `<advpo:optimize>` content. The optimizer accepts `<advpo:exclude>` tags but treats them as redundant. | Explicit inclusion mode | 

**Tip**  
You don't need both tag types. If you wrap your focus areas in `<advpo:optimize>`, everything else is automatically preserved. You don't need to add `<advpo:exclude>` tags around content you want to keep. Use `<advpo:exclude>` only when you have no `<advpo:optimize>` tags. It freezes specific sections while optimizing everything else.

## Examples
<a name="advanced-prompt-optimization-selective-examples"></a>

The following examples show how to use `<advpo:optimize>` and `<advpo:exclude>` tags to control which sections of your prompt template the optimizer rewrites.

**Example Using advpo:optimize to focus on one section**  <a name="advanced-prompt-optimization-selective-ex-optimize"></a>
In this example, only the complaint-response instructions are optimized. The optimizer preserves the identity statement and the policy constraint exactly as written.  

```
You are a helpful customer service agent for Acme Corp. Always be polite and professional.

<advpo:optimize>When responding to a complaint, acknowledge the customer's frustration, summarize the issue, and propose exactly one concrete resolution. Use bullet points for clarity.</advpo:optimize>

Never disclose internal pricing or employee information.
```

**Example Using advpo:exclude to freeze specific sections**  <a name="advanced-prompt-optimization-selective-ex-exclude"></a>
In this example, the identity statement and the policy constraint are frozen. Everything else (the complaint-response instructions) is optimized.  

```
<advpo:exclude>You are a helpful customer service agent for Acme Corp. Always be polite and professional.</advpo:exclude>

When responding to a complaint, acknowledge the customer's frustration, summarize the issue, and propose exactly one concrete resolution. Use bullet points for clarity.

<advpo:exclude>Never disclose internal pricing or employee information.</advpo:exclude>
```

**Example Multiple optimize blocks**  <a name="advanced-prompt-optimization-selective-ex-multiple"></a>
You can mark multiple non-contiguous sections for optimization. The optimizer can rewrite any or all of them.  

```
You are a technical support assistant for CloudWidget.

<advpo:optimize>When diagnosing an issue, ask clarifying questions about the customer's environment before suggesting solutions.</advpo:optimize>

Always check the knowledge base before escalating.

<advpo:optimize>When providing a solution, include step-by-step instructions with numbered steps. End with a verification step the customer can perform.</advpo:optimize>

Never share internal ticket IDs with customers.
```

**Example Empty optimize block for content generation**  <a name="advanced-prompt-optimization-selective-ex-empty"></a>
An empty `<advpo:optimize>` block tells the optimizer to generate and insert new prompt content at that location.  

```
You are a helpful assistant that summarizes documents.

{{document}}

<advpo:optimize></advpo:optimize>

Respond in plain English. Keep your summary under 200 words.
```

## Interaction with placeholder variables
<a name="advanced-prompt-optimization-selective-variables"></a>

The following rules describe how placeholder variables interact with selective optimization tags.
+ **Variables inside `<advpo:exclude>`:** The runtime still substitutes variables like `{{variableName}}` at runtime. The exclusion applies to the template text around them – "don't rewrite this template text" does not mean "don't substitute variables."
+ **Variables inside `<advpo:optimize>`:** Variable placeholders are preserved as placeholders. The optimizer rewrites the surrounding instructions but keeps `{{variableName}}` references intact.
+ **Tags inside variable values at runtime:** The optimizer ignores these tags. Tag parsing happens on the template only, before variable substitution. This prevents injection of optimization directives through user-supplied input values.

## Validation rules
<a name="advanced-prompt-optimization-selective-validation"></a>

The following configurations cause a validation error.


| Invalid configuration | Error | Resolution | 
| --- | --- | --- | 
| Nested tags (for example, `<advpo:optimize>` inside `<advpo:exclude>`, or the other way around) | ValidationException | Remove the nesting. Use only one tag type at any given location in your template. | 
| Malformed or unclosed tags (for example, `<advpo:optimize>` with no closing tag) | ValidationException | Ensure every opening tag has a matching closing tag. | 
| Misspelled tags in the `advpo:` namespace (for example, `<advpo:optmize>`) | ValidationException | Check the spelling of `optimize` and `exclude`. Advanced Prompt Optimization validates both the opening and closing tags. | 

## Output behavior
<a name="advanced-prompt-optimization-selective-output"></a>

In the optimized prompt returned at the end of the job, the optimizer strips all `<advpo:optimize>` and `<advpo:exclude>` tags. You receive a clean prompt without any optimization markup. The content inside `<advpo:exclude>` blocks (and untagged content in explicit inclusion mode) appears unchanged. The content inside `<advpo:optimize>` blocks contains the optimizer's rewritten version.

## Additional behaviors
<a name="advanced-prompt-optimization-selective-edge-cases"></a>

The following table describes how the optimizer handles additional scenarios.


| Scenario | Behavior | 
| --- | --- | 
| Multiple `<advpo:optimize>` blocks | All are eligible for optimization. The optimizer can rewrite any or all of them. | 
| Multiple `<advpo:exclude>` blocks | All content inside all `<advpo:exclude>` tags is frozen. | 
| Empty `<advpo:optimize>` block | Valid. The optimizer generates and inserts new content at that location. | 
| Whitespace-only `<advpo:optimize>` block | Treated the same as an empty block. | 
| Empty `<advpo:exclude>` block | Ignored (no-op). No content to freeze. | 
| Tags split a sentence mid-word or mid-phrase | Allowed. The optimizer operates on the tagged content as a unit. The optimizer might emit a warning. | 

## Best practices
<a name="advanced-prompt-optimization-selective-best-practices"></a>

Follow these best practices when using selective optimization.
+ **Start with `<advpo:optimize>` tags.** Explicit inclusion mode is the most intuitive – you mark what you want improved, and everything else stays the same.
+ **Keep optimize blocks self-contained.** Place complete instructions or logical sections inside each block. Splitting mid-sentence is allowed but can produce awkward results.
+ **Use selective optimization when your prompt is already partially tuned.** If you have already tuned your safety constraints or output format instructions, freeze them so the optimizer focuses on the sections that still need work.
+ **Combine with multi-turn patterns.** In a monolithic multi-phase prompt (see [Optimizing multi-turn and staged prompts](advanced-prompt-optimization-advanced-topics.md#advanced-prompt-optimization-multi-turn)), use `<advpo:optimize>` to target only the phase instructions that need improvement while keeping conversation-handling boilerplate frozen.