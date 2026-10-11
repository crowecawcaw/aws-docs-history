

# Building on CMS and ADP
<a name="building-on-cms-and-adp"></a>

AVX is designed to compose on top of independently deployed CMS and ADP foundations, consuming live vehicle state from CMS and governed analytical data products and knowledge from ADP through clearly defined cross-account integration patterns. This chapter covers the composition model in detail: which data each foundation provides, how session initialization fuses those data sources, how cross-account grants and resource policies are structured, and the prescriptive steps to wire a new AVX deployment onto existing CMS and ADP stacks.

For the grounding strategy — how the agent decides when to use Bedrock KB RAG versus AgentCore Memory LTM for a given query — see [Knowledge and Grounding](knowledge-and-grounding.md).