

# Agentic AI sustainability

 Agentic AI advertising workloads on Amazon Bedrock draw resources through foundation model inference, knowledge base retrieval, and multi-agent orchestration, and those resources grow with campaign activity. Operating them sustainably means measuring resource consumption per advertising outcome, assigning each agent the least resource-intensive model that meets its quality bar, and matching inference capacity to each agent's campaign-cycle invocation pattern. Energy is reported as a proxy estimate derived from these resource metrics. The generative AI mechanisms that are not specific to advertising, such as prompt caching, knowledge base retrieval tuning, orchestration patterns, and inference pricing models, are covered by the Sustainability pillar of the Generative AI Lens and by the agentic AI cost practices in ADVCOST05. 


|  ADVSUS04: How do you minimize the resource and carbon footprint of your agentic AI advertising workloads across their lifecycle?  | 
| --- | 
| [ADVSUS04-BP01 Continually measure resource consumption of agentic AI advertising workloads, and adjust model and agent allocation accordingly](advsus04-bp01.md) | 
| [ADVSUS04-BP02 Match model capability to task complexity to reduce agent fleet energy use](advsus04-bp02.md) | 

## Capability intent
<a name="advsus04-capability-intent"></a>
+  Resource consumption for every advertising agent is measured continuously and attributed to the individual agent, model, and campaign responsible for it, expressed against business outcomes such as compute per campaign plan or per brand safety assessment. Energy is reported as a proxy estimate derived from these metrics. 
+  Each agent runs on the least resource-intensive foundation model that still meets its quality threshold, with assignments grounded in measured resource-per-task and quality benchmarks. 
+  Provisioning is matched to demand: steady-state agents run on provisioned capacity sized to baseline, bursty agents run on-demand, and non-real-time work is batched and scheduled toward periods of lower grid carbon intensity. 
+  Model assignments are re-evaluated on a recurring cadence against newer models and features, and every change is validated against a quality benchmark before promotion so efficiency is never gained at the expense of output quality. 
+  Sustainability and advertising operations stakeholders share visibility into the resource footprint of agentic AI workloads and act on it together. 

## Common issues to watch for
<a name="advsus04-common-issues-to-watch-for"></a>
+  Treating aggregate Amazon Bedrock spend or token counts as a single number, with no attribution to individual agents, campaigns, or workflows, and measuring consumption once at launch without revisiting it as volumes change. 
+  Defaulting every agent to a single high-capability model regardless of whether its task is basic classification or complex multi-channel generation. 
+  Provisioning throughput sized for peak campaign spikes so capacity sits idle off-peak, or running steady-state agents around the clock on on-demand pricing where provisioned capacity would be more efficient. 
+  Selecting a foundation model at launch and never revisiting it, or adopting newer models for efficiency without a quality benchmark and discovering output regressions in production. 