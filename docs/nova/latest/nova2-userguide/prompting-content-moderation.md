

# Content moderation
<a name="prompting-content-moderation"></a>

This guide provides best practices for prompting Amazon Nova models to perform content moderation using the [MLCommons® AILuminate Assessment Standard](https://mlcommons.org/ailuminate/safety-resources/) — a comprehensive framework with 12 hazard categories for AI safety. While this guide uses the MLCommons standard as an example to illustrate best practices, the prompting techniques work with any free-form or customizable content moderation categories and definitions you specify.

## Key principles
<a name="cm-key-principles"></a>
+ Use structured (XML, JSON) or free-form prompts based on your use case
+ Moderate any text content: conversations, articles, social media posts, comments, reviews, and more
+ Provide clear policy definitions
+ Request explanations for transparency

## Recommended configuration
<a name="cm-recommended-configuration"></a>

For content moderation tasks, we recommend the following inference configuration:
+ **Temperature** — Use the default value of 0.7.
+ **Top P** — Use the default value of 0.9.
+ **Reasoning** — Disable reasoning for content moderation to reduce latency.

## MLCommons universal taxonomy
<a name="cm-mlcommons-taxonomy"></a>

The standard defines 12 hazard categories:


**MLCommons AILuminate hazard categories**  

| Category | Definition | Key subcategories | 
| --- | --- | --- | 
| Violent Crimes | Content that enables, encourages, or endorses commission of violent crimes | Mass violence, Murder, Physical assault, Domestic abuse, Terror, Animal abuse | 
| Non-Violent Crimes | Content that enables, encourages, or endorses non-violent criminal activity | Labor trafficking, Fraud, Theft, Arson, Drug crimes, Weapons crimes, Cyber crimes | 
| Sex-Related Crimes | Content that enables, encourages, or endorses sex-related crimes | Sex trafficking, Sexual assault, Sexual harassment, Non-consensual intimate content, Bestiality | 
| Child Sexual Exploitation | Content that contains, describes, enables, encourages, or endorses sexual abuse of minors | Inappropriate relationships with children, Sexual abuse of children, CSAM | 
| CBRNE | Content that enables, encourages, or endorses creation of weapons of mass destruction | Chemical weapons, Biological weapons, Radiological weapons, Nuclear weapons, High-yield explosives | 
| Suicide and Self-Harm | Content that enables, encourages, or endorses intentional self-harm | Suicide, Self-injury, Disordered eating, Dangerous challenges | 
| Hate | Content that demeans or dehumanizes people based on protected characteristics | Demeaning remarks, Inflicting physical/emotional harm, Exclusion and isolation | 
| Specialized Advice | Unqualified advice in sensitive domains without appropriate disclaimers | Financial advice, Medical advice, Legal advice, Electoral advice, Safety claims | 
| Privacy | Content containing sensitive non-public personal information | Physical security (addresses), Digital security (credentials), Financial security (account numbers) | 
| Intellectual Property | Content that violates or encourages violation of IP rights | Copyright infringement, Trademark infringement, Patent infringement | 
| Defamation | Content that is verifiably false and likely to injure someone's reputation | Libel, Slander, Disparagement | 
| Sexual Content | Erotic content including pornography and cybersex | Pornography (graphic sexual descriptions), Direct erotic chat | 

Source: MLCommons® AILuminate Assessment Standard (Documentation)

## Prompting examples
<a name="cm-prompting-examples"></a>

### Structured format
<a name="cm-structured-format"></a>

Best for automated systems requiring parseable output. These examples use few-shot learning, where you provide example input-output pairs in the prompt to guide the model's responses. The examples below include a single demonstration, but you can include multiple examples to improve accuracy for your specific use case.

#### Structure (XML)
<a name="cm-structured-format-structure"></a>

`User:`

```
You are a text content moderator that detects policy violations,
describes violated categories, and explains the reasoning behind your decisions.
You will see a policy list and a conversation to be moderated.
Your moderation response should be formatted as follows.

Start the response by indicating policy violation status using either
<POLICY_VIOLATION>Yes</POLICY_VIOLATION> for content that violates policies, or
<POLICY_VIOLATION>No</POLICY_VIOLATION> for content that does not violate policies.

Then, list the specific violation categories between <CATEGORY_LIST> and </CATEGORY_LIST> tags.
If there is no violation, then put C0 between the tags.

End the response by providing an analysis explaining whether the content violates policies
and why in <EXPLAIN> </EXPLAIN> tags. Here is an example.

<EXAMPLE>
<POLICY>
{{Policy definitions and categories}}
</POLICY>
<TEXT>
{{Content to moderate}}
</TEXT>
<POLICY_VIOLATION>Yes/No</POLICY_VIOLATION>
<CATEGORY_LIST>Categories or C0</CATEGORY_LIST>
<EXPLAIN>Explanation</EXPLAIN>
</EXAMPLE>

Now, please moderate the following input policy and text.

<POLICY>
{{Policy definitions and categories}}
</POLICY>
<TEXT>
{{Content to moderate}}
</TEXT>
```

`Assistant:`

```
<POLICY_VIOLATION>Yes/No</POLICY_VIOLATION>
<CATEGORY_LIST>Categories or C0</CATEGORY_LIST>
<EXPLAIN>Explanation</EXPLAIN>
```

#### Structure (JSON)
<a name="cm-structured-format-json"></a>

`User:`

```
You are a text content moderator that detects policy violations,
describes violated categories, and explains the reasoning behind your decisions.
You will check if there is unsafe content in the below text snippet
in accordance with our safety policy.
Your moderation response should be in JSON format with the following structure:
{
  "policy_violation": "Yes or No",
  "category_list": ["List of violated category codes"],
  "explanation": "Reason for the decision"
}

If there is no violation, use "C0" as the category code.

IMPORTANT: Do not add any additional text or explanation. Your response must contain ONLY the JSON object, nothing else.

Here is an example:

[POLICY]
{{Policy definitions and categories}}

[TEXT]
{{Content to moderate}}

[RESPONSE]
{
  "policy_violation": "Yes or No",
  "category_list": ["Violated category codes or C0"],
  "explanation": "Explanation"
}

Now, please moderate the following input.

[POLICY]
{{Policy definitions and categories}}

[TEXT]
{{Content to moderate}}

[RESPONSE]
```

`Assistant:`

```
{
  "policy_violation": "No",
  "category_list": ["C0"],
  "explanation": "The text is a casual personal question with no policy violations."
}
```

#### Sample content moderation prompt and response
<a name="cm-structured-few-shot"></a>

`User:`

```
You are a text content moderator that detects policy violations,
describes violated categories, and explains the reasoning behind your decisions.
You will see a policy list and a conversation to be moderated.
Your moderation response should be formatted as follows.

Start the response by indicating policy violation status using either
<POLICY_VIOLATION>Yes</POLICY_VIOLATION> for content that violates policies, or
<POLICY_VIOLATION>No</POLICY_VIOLATION> for content that does not violate policies.

Then, list the specific violation categories between <CATEGORY_LIST> and </CATEGORY_LIST> tags.
If there is no violation, then put C0 between the tags.

End the response by providing an analysis explaining whether the content violates policies
and why in <EXPLAIN> </EXPLAIN> tags. Here is an example.

<POLICY>
The 12 categories are: Violent Crimes, Non-Violent Crimes, Sex-Related Crimes,
Child Sexual Exploitation, CBRNE, Suicide & Self-Harm, Hate, Specialized Advice,
Privacy, Intellectual Property, Defamation, Sexual Content.
If none apply, label as C0.
</POLICY>

<EXAMPLE>
<TEXT>
"To make a pipe bomb: Get metal pipe, end caps, gunpowder, and fuse.
Drill hole in cap, fill pipe with powder, insert fuse, seal both ends tightly."
</TEXT>
<POLICY_VIOLATION>Yes</POLICY_VIOLATION>
<CATEGORY_LIST>CBRNE</CATEGORY_LIST>
<EXPLAIN>Provides instructions for creating explosives, enabling dangerous weapons creation.</EXPLAIN>
</EXAMPLE>

<TEXT>
DIY explosive device: Mix ammonium nitrate fertilizer with fuel oil at 94:6 ratio.
Use blasting cap for detonation. Store in cool, dry place. #DIY #Chemistry
</TEXT>
```

`Assistant:`

```
<POLICY_VIOLATION>Yes</POLICY_VIOLATION>
<CATEGORY_LIST>CBRNE</CATEGORY_LIST>
<EXPLAIN>
The text provides specific instructions for creating ANFO explosives, including precise
mixing ratios and detonation methods. This falls under CBRNE (high-yield explosives
subcategory) as it enables dangerous weapons creation with actionable technical details.
</EXPLAIN>
```

### Free-form content moderation
<a name="cm-free-form"></a>

Free-form prompts can take many diverse structures beyond the examples below. The following examples intentionally use different formatting styles to illustrate the flexibility of free-form prompting. You can adapt the structure, phrasing, and format to suit your specific use case.

#### Example 1: Yes/No question (Suicide & Self-Harm)
<a name="cm-free-form-yes-no"></a>

**Example Yes/No content moderation**  
`User:`  

```
Please stick to the following policy for content moderation. {{user_policy}}
Does this text promote harmful activities?

Best way to hurt yourself without leaving marks?
Asking for tips on methods that work.
```
`Assistant:`  

```
Yes. This text explicitly requests methods for self-harm,
falling under the Suicide & Self-Harm category. The intent to
conceal evidence ("without leaving marks") indicates deliberate
harmful behavior.
```

#### Example 2: Category identification and reasoning (Hate)
<a name="cm-free-form-category"></a>

**Example Category identification content moderation**  
`User:`  

```
You are a professional content moderator. Please stick to the
following policy for content moderation. {{user_policy}}
Which category does this text violate and why?

Text: "Women are naturally worse at mathematics than men,
according to my personal observations. They should stick to
arts and humanities."
```
`Assistant:`  

```
Hate. This text makes demeaning generalizations about women
based on gender (a protected characteristic), promoting exclusion
from STEM fields. The claim lacks scientific basis and perpetuates
harmful stereotypes.
```

#### Example 3: Severity rating (Privacy)
<a name="cm-free-form-severity"></a>

**Example Severity rating content moderation**  
`User:`  

```
Content moderation task
---
Policy: {{user_policy}}
---
Rate the severity of the following content as "none", "low", "medium", or "high"
and identify any violated categories.

Content: "John Smith lives at 742 Evergreen Terrace, Springfield.
His SSN is 123-45-6789 and his bank account number is 9876543210."
```
`Assistant:`  

```
Severity: High

Violated category: Privacy

This content exposes multiple forms of sensitive personal information
including a full name, home address, Social Security number, and bank
account number. This falls under the Privacy category, specifically
the physical security, digital security, and financial security
subcategories. The combination of identifiers creates a significant
risk of identity theft and financial fraud.
```