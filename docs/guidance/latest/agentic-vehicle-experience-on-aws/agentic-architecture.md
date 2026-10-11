

# Agentic Architecture
<a name="agentic-architecture"></a>

AVX builds its agentic layer on Amazon Bedrock AgentCore — a managed runtime that hosts the Strands-based supervisor agent, orchestrates the specialist sub-agent mesh, and delivers low-latency voice experiences through Amazon Nova 2 Sonic. This chapter covers the two-tier design and the Tier 1 conversational layer. [Tier 2 Autonomous Agents](avx-agent-pattern.md) covers the autonomous agents, their contracts, the Actions framework, the delivery broker and the deterministic seams.