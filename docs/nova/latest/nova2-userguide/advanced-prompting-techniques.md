# Advanced prompting techniques

These sections provide advanced guidance for how to improve the quality of your prompts
and leverage key features like extended thinking.

Amazon Nova 2 models offer an optional reasoning mode that enhances the model's approach to
complex problem-solving by allowing it to work through problems systematically before
responding. Leveraging the model's reasoning mode is a powerful way to improve the
accuracy of your prompts.

**When to use it:** Reasoning mode is recommended for
complex tasks such as use cases with:

- **Multiple reasoning steps:** Mathematical proofs,
  algorithm design, system architecture
- **Cross-referencing information:** Document analysis,
  option comparison, trade-off evaluation
- **Error-prone calculations:** Financial modeling,
  data analysis, complex debugging
- **Planning with constraints:** Resource optimization,
  dependency management, risk assessment
- **Complex classifications:** Multi-label
  categorization, hierarchical taxonomies, nuanced decision boundaries
- **Tool calling scenarios:** Multi-step API workflows,
  database query optimization, coordinated system integrations

###### Note

For more information on the reasoning mode, refer to [Using reasoning](using-converse-api.md#converse-api-reasoning "using-converse-api.md#converse-api-reasoning").

For situations where the model needs to assess multiple approaches to solve the
problem, instruct it to take a **top-down** approach.

- Amazon Nova 2 models perform better when the model starts with the big picture and then
  breaks it down into smaller, more detailed subproblems or steps.
- Explicitly direct the model to first identify the main objective, then decompose
  it into manageable components before working through the details of each part.
- This structured approach helps the model organize its thinking and produce more
  coherent reasoning chains.
  **Example:**

```
{{User query}}. Start with the big picture and break it down into progressively smaller, more detailed subproblems or steps.
```

While reasoning mode provides enhanced accuracy through systematic problem-solving,
there are specific scenarios where Chain of Thought (CoT) prompting in non-reasoning mode
may better serve your needs.

**When to use it:**

- **Transparency and auditability:** When you want to
  see, verify, or audit the model's reasoning process, CoT provides full visibility into
  each step. This is critical for regulated industries, high-stakes decisions, or when
  you want to document the logic behind an answer.
- **Custom reasoning structures:** Use CoT to enforce
  specific reasoning patterns or methodologies. You can guide the model to follow your
  organization's decision frameworks, use domain-specific problem-solving approaches, or
  ensure factors are considered in a specific order.
- **Prompt development and debugging:** During the
  prompt engineering phase, CoT helps you understand how the model approaches problems,
  identify where reasoning breaks down and iterate on your prompts more
  effectively.
- **Hybrid approaches:** Consider using CoT during
  development to perfect your prompts, then switching to reasoning mode for production
  deployment once you're confident in the model's approach to your specific use
  case.

###### Note

Not all tasks require CoT. For simpler tasks, allow the model to use its own
reasoning process.

**Guiding the model's CoT direction:**

```
{{User query}} Please follow these steps:

1. {{Step 1}}
2. {{Step 2}}
...
```

Amazon Nova 2 models have a supported context length of 1 million tokens and excel at code
understanding and question answering on long documents. Its performance (including system
prompt adherence and tool use) can decline slightly as the context size increases.

**How to use it:**

- **Put long-form data at the beginning:** Place your
  long documents and inputs near the beginning of your prompt. Place them before your
  query, instructions and examples.
- **Put instructions at the end:** Place your
  instructions at the end of the prompt. The model performs best when the context is
  provided first and the instructions are provided at the end.
- **Structure document content start and end markers:**
  Use start and end markers, such as `DOCUMENT {idx} START` and
  `DOCUMENT {idx} END`, to denote the start and end of long documents where
  {idx} represents the index of the specific document.
  **Example Template:**

```
// Provide your long inputs at the top of your prompt
BEGIN INPUT DOCUMENTS

DOCUMENT 1 START
{{Your document}}
DOCUMENT 1 END

END INPUT DOCUMENTS

// Then specify your query and instructions
BEGIN QUESTION
{{User query}}
END QUESTION

BEGIN INSTRUCTIONS
{{Instructions}}
END INSTRUCTIONS
```

We recommend that you provide the model with trusted information relevant to the input
query. This information, along with the input query, is often a part of the system called
retrieval augmented generation (RAG).

- In this process, some relevant, contextual document or information is augmented to
  the actual user prompt so that the model gets trustworthy content to generate a
  relevant and accurate response.
- Instructing Amazon Nova 2 to answer using a reference text from a trusted source can
  guide it to compose its response based on the provided material and ensure that its
  response is grounded in accurate and relevant information, enhancing the reliability
  and credibility of the generated content.
- Using a reference text can help avoid hallucinating, thereby improving the overall
  quality and trustworthiness of the responses. To minimize hallucination, we recommend
  explicitly mentioning `DO NOT USE INFORMATION THAT IS NOT IN REFERENCE
 TEXTS!` in your model instructions.
  The following shows an example:

###### Example Grounding prompt template

```
System:
In this session, the model has access to search results and a user's question, your job is to answer the user's question using only information from the search results.

Model Instructions:
- DO NOT USE INFORMATION THAT IS NOT IN SEARCH RESULTS!

User: {Query}
Resource: Search Results: {Reference texts}
```

This table shows how grounding context can prevent the model from
hallucinating.

| Role   | Prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | In this session, the model has access to search results and a user's<br>question, your job is to answer the user's question using only information<br>from the search results. Model Instructions:<br>• DO NOT USE INFORMATION THAT IS<br>NOT IN SEARCH RESULTS!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| User   | What were the economic impacts of the COVID-19 pandemic on the United<br>States in 2020? Resource: Search Results: In 2020, the United States<br>experienced significant economic impacts due to the COVID-19 pandemic. The<br>U.S. economy contracted by 3.5% in 2020, according to the Bureau of Economic<br>Analysis. Unemployment rates surged to 14.7% in April 2020, the highest since<br>the Great Depression, before gradually declining. Small businesses faced<br>severe challenges, with millions of firms closing permanently. Additionally,<br>consumer spending dropped sharply as people reduced non-essential expenditures<br>and saved more. Government intervention played a critical role in mitigating<br>these impacts through stimulus packages and support programs, such as the<br>Paycheck Protection Program (PPP) for small businesses and direct payments to<br>individuals. Despite these measures, the economic recovery remained uneven<br>across different sectors and regions. |

### Ground using citation markers

For long document tasks, we recommend that you instruct the Amazon Nova 2 model to ground
its responses using citations from the relevant sections of the documents before it
proceeds with the task.

This approach helps the model focus on the most pertinent information and avoid
being distracted by extraneous content. When you request that the model grounds its
response, the sections that can be cited should be numbered. For example, `Passage
 %[1]%`, `Passage %[2]%` and so on.

###### Example Citation markers prompt

```
You are an AI financial assistant. Your task is to find patterns and insights from multi-year financial documents

Passage %[1]%
{{Your document}}

Passage %[2]%
{{Your document}}

## Task:
Analyze my LLC's reports across multiple years to identify significant performance trends, segment growth patterns and strategic shifts.

## Context information:
- You have access to my LLC's annual financial reports (10-K) for multiple fiscal years in PDF format
- These reports contain comprehensive financial data including income statements, balance sheets, cash flow statements and management discussions
- The analysis should focus on year-over-year comparisons to identify meaningful trends
- I operate two business segments, one in Massachusetts and one in New York

Based on the provided Context, extract key financial metrics from each year's reports phrases from the documents.
Place citations as inline markers (e.g., %[1]%, %[2]%, etc.) directly within the relevant parts of the response
text. Do not include a separate citation section after the response.
## Response Schema:
%% (Extracted Financial Metrics)
%% (Extracted Financial Metrics)
%% (Extracted Financial Metrics)
...
```

After you extract key information based on the user's task, you can use the
extracted financial metrics to answer the relevant questions as shown:

###### Example Follow-up analysis with extracted metrics

```
## Task
Analyze my LLC's financial reports across multiple years to identify significant performance trends, segment growth patterns and strategic shifts.

{{extracted financial metrics}}

## Model Instructions:
- Organize data chronologically to identify meaningful trends
- DO compare segment performance across the five-year period
- DO identify significant strategic shifts or investments mentioned in management discussions
- DO NOT make speculative predictions beyond what is supported by the data
- ALWAYS note any changes in accounting practices or reporting methodologies that might affect year-over-year comparisons

## Response style and format requirements:
- Respond in markdown
- Structure the analysis with clear headings and subheadings
- Present key financial metrics in tabular format showing all five years side-by-side
- Include percentage changes year-over-year for all major metrics
- Create a section dedicated to visualizing the most significant trends (with descriptions of what would be shown in charts)
- Limit the executive summary to 250 words maximum
- Format segment analysis as separate sections with consistent metrics across all segments
- MUST include a Key Insights bullet-pointed list at the end of each major section
```

### Use Nova web grounding

Instead of prompting directly for citations to ground the model in supporting text,
Amazon Nova 2 models provide an internal web grounding tool that can be used. When enabled,
Amazon Nova 2 models will directly query the web and Amazon's knowledge graphs and ground the
final response with citations.

To learn more on how to leverage Amazon Nova Web Grounding, you can reference the [Amazon Nova Web Grounding user guide](web-grounding.md "web-grounding.md").

To ensure consistent and structured output formats, you can use structured outputs,
including formats like XML, JSON, Markdown, or using tool use functionality.

- This approach allows downstream systems to more effectively understand and parse
  the outputs generated by the model.
- By providing explicit instructions to the model, the responses are generated in a
  way that adheres to a predefined schema.
  For example, if the downstream parser expects specific naming conventions for keys in
  a JSON object, you should specify the response schema at the end of the prompt.
  Additionally, if you prefer responses to be in JSON format without any preamble text,
  instruct the model accordingly. That is, explicitly state `PLEASE GENERATE ONLY THE
 JSON OUTPUT. DO NOT PROVIDE ANY PREAMBLE.` to ensure clean output.

###### Tip

- We observe best adherence to data format requirements when they are defined in
  the schema itself instead of through the use of exemplars (such as, specifying dates
  in YYYY/MM/DD format).
- For simple JSON outputs with up to 10 keys, you can find the schema below. For
  more complex schemas, we recommend you define your schema through a tool. Tool use
  leverages a technique called constrained decoding that will increase the model's
  adherence for these complex scehmas.

### Common formatting schemas

The following are examples of common formatting schemas.

**JSON:**

````
JSON_format = """Write your response following the JSON format below:
```json
{
  "key1": "value1",
  "key2": "value2",
  "key3": [{
    "key3_1": "value_3_1 written in YYYY/MM/DD format",
    "key3_2": "value_3_2 day of the week written in full form",
    ...
  }]
}
````

"""

```

**XML:**



```

ML_format = """Write your response following the XML format below:

<output>
    <task>"task1"</task>
    <subtask>
        <task1_result> ( task 1 result )</task1_result>
        <task2_result> ( task 2 result )</task2_result>
        <task3_result> ( task 3 result )</task3_result>
    </subtask>
    <task>"task2"</task>
    <subtask>
        <task1_result> ( task 1 result )</task1_result>
        <task2_result> ( task 2 result )</task2_result>
        <task3_result> ( task 3 result )</task3_result>
    </subtask>
</output>

"""

```

**Markdown:**



```

markdown_schema = """Write your response following the markdown format below:

## Introduction

( 2-3 line intro)

## Design Guidance

(Bulleted list of design guidance)

## Step by Step Instructions on Execution

( Bulleted list of instructions with each with bold title.)

## Conclusion

( conclusion )
"""

``````

### Prefill assistant content


If you are producing structured output in non-reasoning mode, you can nudge the
 model's response by prefilling the assistant content.


Prefilling improves consistency in the output format while in non-reasoning mode. It
 allows you to direct the model's actions, bypass preambles and enforce specific output
 formats like JSON and XML. For example, if you prefill the assistant content with
 `{` or ````json`, that input guides the model to generate the
 JSON object without additional information.


###### Tip

If you are explicitly looking for extracting JSON, a common pattern is to prefill
 with ````json` and add a stop sequence on `````. This ensures
 the model outputs a JSON object that can be programmatically parsed.


###### Example Prefill assistant content

The following code demonstrates how to prefill with the API:


``````

import boto3
import json

# Create a Bedrock Runtime client.

client = boto3.client(
"bedrock-runtime",
region_name="us-east-1"
)

request_body = {
"system": [
{"text": "You write JSON objects based on the given instructions"}
],
"messages": [
{
"role": "user",
"content": [{"text": "Provide details about the best selling full-frame cameras in past three years. Answer in JSON format with keys like name, brand, price and a summary."}]
},
{
"role": "assistant",
"content": [{"text": " Here is the JSON response: ```json"}]
}
],
"inferenceConfig": {
"maxTokens": 1000,
}
}

# Invoke the model and extract the response body.

response = client.invoke_model(
modelId="amazon.nova-2-lite-v1:0",
body=json.dumps(request_body)
)

model_response = json.loads(response["body"].read())

````

### Specify a tool to use for complex
 schemas


Another approach is to use tools to force a specific schema for the model's response
 by including the *pydantic JSON schema* in the tool use schema
 section. You can specify tool choice to the provided schema and Amazon Nova's response will
 be structured based on the tool selected. To learn more about how to leverage tool use
 see [Tool
 Use](../userguide/tool-use.md "../userguide/tool-use.md").


### Examples


Adding the Output Schema section with the appropriate schema makes the model
 prefer to fit that schema. However, model output is not deterministic and can vary
 from the output schema.



| Role | Unspecific Prompt | Specific Prompt |
| --- | --- | --- |
| User | Provide details about the best selling full-frame cameras in past three<br>years. Answer in JSON format with keys like name, brand, price and a<br>summary. | Provide details about the best selling full-frame cameras in past three<br>years. You MUST answer in JSON format only. Write your response following<br>the the format below: [{ "name": "name goes here", "brand": "brand goes<br>here", "price": "price goes here", "summary": "summary goes here" }] |
| Assistant | ```json [ { "name": "Sony Alpha A7R IV", "brand": "Sony", "price":<br>"Approximately $3,500", "summary": "The Sony Alpha A7R IV is renowned for<br>its exceptional image quality, thanks to a 61-megapixel full-frame sensor.<br>It also features 4K video recording and a robust build, making it a favorite<br>among professional photographers and videographers." }, { "name": "Canon EOS<br>R5", "brand": "Canon", "price": "Approximately $3,900", "summary": "The<br>Canon EOS R5 combines high-resolution imaging with advanced video<br>capabilities. It houses a 45-megapixel sensor, 8K video recording, and<br>impressive autofocus performance, appealing to both photography and<br>filmmaking professionals." }, { "name": "Nikon Z7 II", "brand": "Nikon",<br>"price": "Approximately $2,800", "summary": "The Nikon Z7 II offers a<br>45.7-megapixel full-frame sensor and is praised for its high resolution and<br>excellent dynamic range. It also supports 4K video recording and features a<br>versatile Z-mount lens system, making it a strong contender in the<br>full-frame market." }, { "name": "Fujifilm GFX 100S", "brand": "Fujifilm",<br>"price": "Approximately $7,000", "summary": "While not a traditional<br>full-frame camera, the Fujifilm GFX 100S stands out with its 102-megapixel<br>medium format sensor. It is lauded for its stunning detail and color<br>reproduction, though it comes at a higher price point and is aimed at<br>specialized users." } ] ``` | [ { "name": "Nikon D850", "brand": "Nikon", "price": "$3,296.95",<br>"summary": "The Nikon D850 is a professional full-frame DSLR camera known<br>for its exceptional image quality, 45.7-megapixel resolution, 7 fps<br>continuous shooting, and 4K video capabilities." }, { "name": "Canon EOS 5D<br>Mark IV", "brand": "Canon", "price": "$3,499.00", "summary": "The Canon EOS<br>5D Mark IV is a popular full-frame DSLR appreciated for its 30.4-megapixel<br>sensor, 4K video recording, robust build quality, and reliable autofocus<br>system." }, { "name": "Sony A7R III", "brand": "Sony", "price": "$3,198.00",<br>"summary": "The Sony A7R III is a high-resolution full-frame mirrorless<br>camera renowned for its 42.4-megapixel sensor, excellent low-light<br>performance, and versatile lens compatibility." }, { "name": "Fujifilm GFX<br>100S", "brand": "Fujifilm", "price": "$5,999.99", "summary": "The Fujifilm<br>GFX 100S is a medium format mirrorless camera that stands out for its<br>102-megapixel sensor, high dynamic range, and exceptional color<br>reproduction." }, { "name": "Sony A7 III", "brand": "Sony", "price":<br>"$1,998.00", "summary": "The Sony A7 III is a full-frame mirrorless camera<br>popular among enthusiasts and professionals for its 24.2-megapixel sensor,<br>fast autofocus, and 4K video capabilities." } ] |

Another approach is to prefill the model's response by including the desired
 initial text within the assistant's message. In this case, Amazon Nova model's
 response will continue from where the assistant's message leaves off.

**Tip:** Prefill is only valid when reasoning is
 not enabled.



| Role | Prompt |
| --- | --- |
| User | Provide details about the best selling full-frame cameras in past three<br>years. Your response should be in JSON format, with the following keys:<br>name, brand, year, price, summary. |
| Assistant (Prefilling) | ```json |
| Assistant | { "cameras": [ { "name": "Sony Alpha A7 III", "brand": "Sony", "year":<br>2018, "price": "$1999", "summary": "The Sony Alpha A7 III is a highly<br>acclaimed full-frame mirrorless camera known for its excellent image<br>quality, advanced autofocus system, and 4K video capabilities." }, { "name":<br>"Canon EOS R5", "brand": "Canon", "year": 2020, "price": "$3899", "summary":<br>"The Canon EOS R5 is a top-tier full-frame mirrorless camera that offers<br>stunning 45MP images, 8K video recording, and exceptional performance in<br>various lighting conditions." }, { "name": "Nikon Z7 II", "brand": "Nikon",<br>"year": 2020, "price": "$2999", "summary": "The Nikon Z7 II is a flagship<br>full-frame mirrorless camera with a 45.7MP sensor, superb image quality, and<br>advanced video recording features." }, { "name": "Fujifilm GFX 100S",<br>"brand": "Fujifilm", "year": 2020, "price": "$7999", "summary": "The<br>Fujifilm GFX 100S is a medium format mirrorless camera known for its<br>impressive 102MP sensor, beautiful film simulations, and versatile lens<br>options." }, { "name": "Sony Alpha A7R IV", "brand": "Sony", "year": 2019,<br>"price": "$3499", "summary": "The Sony Alpha A7R IV features a 61MP sensor,<br>excellent low-light performance, and advanced video capabilities, making it<br>a favorite among professional photographers." } ] } ``` |

As an alternative to using the prefill technique for structured output, you can
 combine Nova's tool functionality with toolChoice. In this example, the model will
 generate a tool call that adheres to the JSON schema provided and calls the specific
 tool specified to full JSON format defined. For additional guidance, refer to
 Advanced Systems.



| Role | Prompt |
| --- | --- |
| User | From the below provided Query, extract the relevant entities Query:<br>John works in BUILDING-0987 and has been in charge of product id 23564#. His<br>performance has been excellent in past years and is up for a raise. Use the<br>extract\_ner tool. |
| ToolConfig | { "tools": [ { "toolSpec": { "name": "extract\_ner", "description":<br>"Extract all the named entities. based on provided input", "inputSchema": {<br>"json": { "type": "object", "properties": { "entities": { "type": "array",<br>"items": { "type": "object", "properties": { "name": { "type": "string",<br>"description": "The extracted entity name. This should be a name of a<br>person, place, animal or thing" }, "location": { "type": "string",<br>"description": "The extracted location name. This is a site name or a<br>building name like SITE-001 or BUILDING-003" }, "product": { "type":<br>"string", "description": "The extracted product code, this is generally a 6<br>digit alphanumeric code such as 45623#, 234567" } }, "required": [ "name",<br>"location", "product" ] } } }, "required": [ "entities" ] } } } }],<br>"toolChoice": { "tool": { "name": "extract\_ner" } } } |


Amazon Nova 2 models have been trained on more than 200 languages and optimized for 15
 languages.

###### Topics

* [Prompt for accurate translations](#accurate-translations "#accurate-translations")
* [Enforce consistent writing
 conventions](#consistent-writing-conventions "#consistent-writing-conventions")

### Prompt for accurate translations


To leverage this capability for short form translations (a few sentences) you can
 instruct the model to translate the text into the specified target language.


###### Example Translation prompts


````

Translate the following text into {target language}. Please output only the translated text with no prefix or introduction: {text}

```

```

Translate the following sentence from {source_language} to {target language}: {text}

```

```

{text} How do you say this sentence in {target_language}

```

### Enforce consistent writing
 conventions


In character-based languages, the Amazon Nova 2 models may utilize the character set from
 the source language. You can use the following prompt to enforce a consistent
 output.


###### Example Enforce writing conventions


```

When translating, ensure to use the correct orthography / script / writing convention of the target language, not the source language's characters

```


### Agentic systems


###### Topics

* [Set the right inference parameters](#set-inference-parameters "#set-inference-parameters")
* [Consider latency requirements](#consider-latency-requirements "#consider-latency-requirements")
* [Use intentional wording for tool
 calling instructions](#intentional-wording-tool-calling "#intentional-wording-tool-calling")
* [Leverage thinking Commands](#leverage-thinking-commands "#leverage-thinking-commands")
* [Tool call ordering](#tool-call-ordering "#tool-call-ordering")
* [Create quality tool schemas](#designing-tool-schema "#designing-tool-schema")
* [Create sub-agents](#create-sub-agents "#create-sub-agents")
* [Use tools for multimodal inputs](#use-tools-multimodal-inputs "#use-tools-multimodal-inputs")
* [Next steps](#next-steps-best-practices "#next-steps-best-practices")

#### Set the right inference parameters


Tool calling requires a very specific structured output from the model and is
 improved by using the following inference parameters:



* **Non Reasoning Mode:** Temperature: 0.7 &
 Top P: 0.9
* **Reasoning Mode:** Temperature: 1 & Top P:
 0.9

#### Consider latency requirements


###### Tip

Amazon Nova 2 models are capable of tool calling with reasoning on and off. However,
 reasoning modes have a significant impact on latency.


For latency sensitive applications, you should optimize for reasoning off mode and
 simplify the required tool calls where possible. Split multistep workflows into
 discrete steps to reduce the model's reliance on regurgitating unnecessary
 parameters.


#### Use intentional wording for tool
 calling instructions


**Tool names:** Referencing tools in the system
 prompt is common in tool calling systems to instruct the model on when to call a tool.
 When you reference tools in the prompt, we recommend you use the tool name instead of
 xml or pythonic references or examples.



```

Use the 'run_shell_command' tool for running shell commands

```

```

Call run_shell_command() to run shell commands

```

#### Leverage thinking Commands


For all use cases where thinking is beneficial for tool calling, we recommend you
 leverage reasoning mode instead of prompting the model to “think in tags” or to use a
 “think” tool.


 Amazon Nova 2 models are trained extensively for reasoning mode and will produce the
 optimal results when used in reasoning mode for chain of thought.


#### Tool call ordering


In use cases that might require the use of built-in tools and native tool calling
 simultaneously, the model biases towards calling built-in tools first.


Don't instruct the model to act differently in the prompt. Instead, design your
 workflow to take this into account.


For example, if you do not want the model to use built-in tools, do not include
 them in your workflow so that the model does not bias towards them.


#### Create quality tool schemas


Tool schemas are one of the key places you can prompt engineer effective tool
 calling systems. However, it's important to consider what gets captured in the tool
 schema itself, how each schema element is described semantically and how the system
 prompt references tools and schema elements within system instructions.


Amazon Nova 2 models are optimizied for concise descriptions in the tool schemas. Keep
 it brief.


**Tool schema versus system prompt
 guidelines:**


**Include in the tool schema:**



* Core functionality: What the tool does (20-50 words recommended)
* Parameter specifications: Clear descriptions of each parameter (around 10
 words per parameter)
* Expected formats: Data types (like enum, int, float), required fields and
 valid value ranges

**Include in the system prompt:**



* Dedicate a `#Tool Usage` section with orchestration logic (when and
 why to use specific tools) and business rules (conditional logic, sequencing
 requirements, and dependencies).
* **Error handling strategies:** Add an
 `#Error Handling and Troubleshooting` section with instructions for
 how to respond to failures or unexpected outputs
* **Output formatting:** Add details on how to present to the user


```

You are a software engineering issue root cause analysis agent. You are tasked with reviewing a customer issue and examining the repository to identify a plan to resolve the issue. # Core Mandates

- **DO NOT** update the original issue that was posted by the user. You only add _additional_ comments to the reported issue if necessary

# Primary Workflows

1. **Understand:** Analyze the user's request and explore the codebase thoroughly using **get_file_contents** to grasp file structures and conventions.
2. **Plan:** Create a coherent, evidence-based plan for resolving the task and share it with the user following the format below

# Tool Usage

- **Read the Issue:** Always start by using the **read_issue** tool to get the details about the requested issue
- **File Paths:** Always end the file path with "/" if you are searching a directory using the **get_file_contents** tools
- **Parallelism:** Execute multiple independent tool calls in parallel when feasible

# Error Handling and Troubleshooting

- **File Exploration:** If you get an error that a file doesn't exist, try searching at the directory level first to validate the file path

# Output Formatting

Return your plan in markdown in the following format

## Issue

<Your root cause analysis of the issue>

## Resolution Plan

<your step by step plan of how to solve the issue>
```

#### Create sub-agents

Consider creating specialized sub-agents instead of a single agent with many tools
when you encounter:

- Tool count exceeds 20: Large tool sets become difficult to manage and increase
  selection errors
- Distinct functional domains: Tools naturally cluster into separate categories
  (such as data retrieval versus processing versus reporting)
- Complex schemas: When parameter depth exceeds 3-4 levels or tools have
  intricate interdependencies
- Conversation length: Workflows regularly exceed 15-20 turns may benefit from
  specialized sub-agents
- Performance degradation: If you observe decreased accuracy in tool selection
  or increased latency

###### Tip

MCP Servers come with tools and schemas you can't control. Only include the
necessary tools for your workflow to complete the required task.

#### Use tools for multimodal inputs

For multimodal tasks, we have not observed improved accuracy leveraging tools for
structured tasks (such as extraction or timestamp generation).

Instead, we recommend you review the relevant sections in the Prompting multimodal
inputs section for how to prompt the model successfully using the provided
templates.

#### Next steps

- For multimodal prompting, see [Prompting multimodal inputs](prompting-multimodal.md "prompting-multimodal.md").
