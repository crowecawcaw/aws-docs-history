

# Tier 2 Autonomous Agents
<a name="avx-agent-pattern"></a>

AVX agent behavior is organized around three contracts: the **Finding contract** that Tier 2 agents satisfy when writing conclusions, the **Action contract** that governs what happens when an owner approves a Finding, and the **executor pattern** that carries Actions to target systems. The **outreach broker** decides, independently of any agent, whether a Finding produces a push notification, an in-app card, or both. Adding an agent means registering a module; adding a target system means adding one executor class.