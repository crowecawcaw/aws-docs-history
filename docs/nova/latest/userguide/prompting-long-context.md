# Utilizing long context windows

Amazon Nova Premier has a supported context length of 1 million tokens, which translates to 1M tokens of text, 500 images, or 90 minutes of video. Amazon Nova Premier excels at code understanding and question answering on long documents. It's performance can decline slightly as the context size increases, so for best results consider the following guidelines:

- **Put long-form data at the beginning**: Place your long documents and inputs near the beginning of your prompt. They should be placed before your query, instructions, and examples.
- **Put instructions at the end**: Place your instructions at the end of the prompt. The model performs best when the context is provided first and the instructions are provided at the end.
- **Structure document content start and end markers**: Use start and end markers, such as `[Document Start]` and `[Document End]`, to denote the start and end of a long document.

Here is an example template:

```
// Provide your long inputs at the top of your prompt
[Document Start]
{{ Your document}}
[Document End]

// Then specify your query and instructions
{{ User query}}
{{ Instructions}}
```

- **Ground your responses using citation markers**: For long document tasks, we recommended that you instruct the Amazon Nova model to ground its responses using citations from the relevant sections of the documents before it proceeds with the task. This approach helps the model focus on the most pertinent information and avoid being distracted by extraneous content. When you request that the model grounds its response, the sections that can be cited should be number. For example, Passage %[1]%, Passage %[2]%, and so on or just <C1>, <C2>, and so on. For detailed information on how to include citations in prompts, see [Build your own RAG](prompting-tools-rag.md "prompting-tools-rag.md").

Here is an example prompt:

```
"""
You are an AI financial assistant. Your task is to find patterns and insights from multi-year financial documents

Passage %[1]%
{{ Your document}}

Passage %[2]%
{{ Your document}}

Passage %[3]%
{{ Your document}}

Passage %[4]%
{{ Your document}}

## Task:
Analyze Amazon's financial reports across multiple years to identify significant performance trends, segment growth patterns, and strategic shifts.

## Context information:
- You have access to Amazon's annual financial reports (10-K) for multiple fiscal years in PDF format
- These reports contain comprehensive financial data including income statements, balance sheets, cash flow statements, and management discussions
- The analysis should focus on year-over-year comparisons to identify meaningful trends
- Amazon operates multiple business segments including North America retail, International retail, Amazon Web Services (AWS), advertising, and subscription services

Based on the provided Context, extract key financial metrics from each year's reports phrases from the documents, citing them using %[1]%, %[2]%, %[3]%, and for the corresponding
passage that supports the response.

## Response Schema:
%[1]%  (Extracted Financial Metrics)
%[2]%   (Extracted Financial Metrics)
%[3]%   (Extracted Financial Metrics)
...
"""
```

After you have extracted key information based on the user's task, you can use the extracted financial metrics to answer the relevant questions as shown:

```
"""
## Task
Analyze Amazon's financial reports across multiple years to identify significant performance trends, segment growth patterns, and strategic shifts.
{{ extracted financial metrics }}

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
