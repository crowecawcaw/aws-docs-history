

# Anthropic
<a name="model-cards-anthropic"></a>

The following Anthropic models are available in Amazon Bedrock:


| **Model** | **Description** | 
| --- | --- | 
| [Claude Haiku 5.5](model-card-anthropic-claude-haiku-5-5.md) | Claude Haiku 5.5 is the fastest and most efficient model in the Claude 5.5 family, built for high-volume, latency-sensitive work. It's the most capable Haiku model yet, with a clear step up over Claude Haiku 4.5 on coding and agent tasks. | 
| [Claude Sonnet 5.5](model-card-anthropic-claude-sonnet-5-5.md) | Claude Sonnet 5.5 is a smarter, more efficient Sonnet. It's a clear leap forward from Sonnet 5 on coding and knowledge work, at a much lower cost per task. | 
| [Claude Opus 5.5](model-card-anthropic-claude-opus-5-5.md) | Claude Opus 5.5 is Anthropic's most capable Opus model. Better at coding, knowledge work, and long-running tasks. It's easier to collaborate with and more cost efficient than ever. | 
| [Claude Fable 5.1](model-card-anthropic-claude-fable-5-1.md) | Claude Fable 5.1 is Anthropic's frontier model for ambitious coding, long-horizon agents, and enterprise knowledge work. | 
| [Claude Mythos 5.1](model-card-anthropic-claude-mythos-5-1.md) | Claude Mythos 5.1 is Anthropic's most capable model for cybersecurity defense and life sciences research, including threat intelligence, vulnerability discovery, red teaming, drug discovery, and biodefense screening. | 
| [Claude Opus 5](model-card-anthropic-claude-opus-5.md) | Claude Opus 5 is Anthropic's most advanced Opus model, powering long-running agents while delivering improvements in coding and professional work. | 
| [Claude Sonnet 5](model-card-anthropic-claude-sonnet-5.md) | Claude Sonnet 5 is Anthropic's most capable Sonnet model yet, built for coding, agents, and professional work at scale. | 
| [Claude Mythos 5](model-card-anthropic-claude-mythos-5.md) | Claude Mythos 5 is Anthropic's most capable model for cybersecurity and life sciences, including vulnerability discovery, drug design, and biodefense screening. | 
| [Claude Fable 5](model-card-anthropic-claude-fable-5.md) | Claude Fable 5 is Anthropic's next-generation model for complex knowledge work and coding, capable of sustained autonomous operation across multi-day tasks. | 
| [Claude Opus 4.8](model-card-anthropic-claude-opus-4-8.md) | Claude Opus 4.8 is an Anthropic Opus model optimized for coding, agents, and deeper reasoning in enterprise workflows. | 
| [Claude Opus 4.7](model-card-anthropic-claude-opus-4-7.md) | Claude Opus 4.7 is an Anthropic Opus model built for coding, enterprise workflows, and long-running agentic tasks. | 
| [Claude Sonnet 4.6](model-card-anthropic-claude-sonnet-4-6.md) | Claude Sonnet 4.6 is a full upgrade of Anthropic's mid-tier model with improved coding, computer use, long-context reasoning, and agent planning with a 1M token context window. | 
| [Claude Opus 4.6](model-card-anthropic-claude-opus-4-6.md) | Claude Opus 4.6 is Anthropic's flagship model that plans more carefully, sustains agentic tasks longer, and operates reliably in massive codebases. | 
| [Claude Opus 4.5](model-card-anthropic-claude-opus-4-5.md) | Claude Opus 4.5 is Anthropic's model for coding, agents, and computer use with improvements for spreadsheets and long-running chats. | 
| [Claude Haiku 4.5](model-card-anthropic-claude-haiku-4-5.md) | Claude Haiku 4.5 is Anthropic's lightweight model optimized for speed and efficiency with strong coding and agent performance. | 
| [Claude Sonnet 4.5](model-card-anthropic-claude-sonnet-4-5.md) | Claude Sonnet 4.5 is Anthropic's model optimized for agents, coding, and computer use with significant improvements across all benchmarks. | 
| [Claude Opus 4.1](model-card-anthropic-claude-opus-4-1.md) | Claude Opus 4.1 is an upgrade to Anthropic's model with improved coding, reasoning, and agentic task capabilities. | 
| [Claude Sonnet 4](model-card-anthropic-claude-sonnet-4.md) | Claude Sonnet 4 is Anthropic's balanced model with strong coding and reasoning capabilities, improved instruction following, and extended thinking with tool use. | 
| [Claude 3 Haiku](model-card-anthropic-claude-3-haiku.md) | Claude 3 Haiku is Anthropic's fastest and most compact Claude 3 model, optimized for speed and efficiency in near-instant responses. | 

## Billing notes
<a name="model-cards-anthropic-billing-notes"></a>

The following billing behaviors apply specifically to Anthropic models on Amazon Bedrock:
+ **Refused requests** – A refused request returns HTTP 200 with `stop_reason: "refusal"`. Whether it's billed depends on when the refusal occurred and on `stop_details.category`. These rules apply on both the `bedrock-runtime` and `bedrock-mantle` endpoints.

  The following table describes each `stop_details.category` value and whether Amazon Bedrock bills a refusal in that category before any output.


<table>
<thead>
  <tr><th><b><code>stop_details.category</code></b></th><th><b>What it means</b></th><th><b>Billed before any output</b></th></tr>
</thead>
<tbody>
  <tr><td><code>"cyber"</code></td><td>The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.</td><td>No</td></tr>
  <tr><td><code>"bio"</code></td><td>The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.</td><td>Yes</td></tr>
  <tr><td><code>"frontier_llm"</code></td><td>The request could help with the development of competing AI models, which is restricted under Anthropic's commercial terms. Benign machine learning work can also trigger this category.</td><td>Yes</td></tr>
  <tr><td><code>"reasoning_extraction"</code></td><td>The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use adaptive thinking. This category has no recommended fallback model, so change the prompt instead of retrying on another model.</td><td>Yes</td></tr>
  <tr><td><code>"general_harms"</code></td><td>The request falls under a usage-policy area outside the four named categories. Benign work can also trigger this category.</td><td>No</td></tr>
  <tr><td><code>null</code></td><td>The refusal doesn't map to a named category. <code>null</code> is a valid final value, not a placeholder.</td><td>No</td></tr>
</tbody>
</table>


  Amazon Bedrock bills a refusal before any output like any other request, at the refused model's rates. For a refusal that arrives mid-stream, after partial output, Amazon Bedrock bills the input tokens and the output tokens already streamed, in any category. Treat any partial output as incomplete and discard it.

  In every case, the response's `usage` still reports token counts, and the request counts against your quotas. The set of billed categories can change.