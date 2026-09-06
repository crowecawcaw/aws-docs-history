

# Reinforcement fine-tuning (RFT)
<a name="nova-hp-rft"></a>

Reinforcement Fine-Tuning (RFT) is a technique that improves model performance through feedback signals — measurable scores or rewards indicating response quality — rather than direct supervision with exact correct answers. Unlike SFT that learns from input-output pairs, RFT uses reward functions to evaluate model responses and iteratively optimizes the model to maximize these rewards. RFT supports both single-turn and multi-turn training:
+ **Single-turn RFT**: The model generates a single response to a prompt, and a reward function scores that response. Best for tasks with clear per-response quality metrics such as math, code generation, and structured reasoning.
+ **Multi-turn RFT**: The model engages in multi-step interactions (for example, agentic workflows with tool use), and a reward function evaluates the overall trajectory. Best for complex tasks requiring sequential decision-making, such as multi-step problem solving, tool orchestration, and conversational agents.

**When to use RFT**  
Use RFT when you can define clear, measurable success criteria but struggle to provide exact correct outputs for training. RFT is ideal when:
+ You have a reliable reward function that can evaluate model outputs programmatically
+ You need to align model behavior with specific preferences or constraints
+ Collecting high-quality labeled examples is expensive or impractical
+ Multiple valid solutions exist but some are clearly better than others (creative writing, code optimization, complex reasoning)

RFT excels in domains where output quality can be objectively measured: mathematical problem-solving, code generation, scientific reasoning, structured data analysis, multi-step reasoning, tool usage, and complex workflows with specific constraints.

**Supported models**  
Single-turn and multi-turn RFT are available for the following Amazon Nova models:
+ Nova 2.0 (Lite)

**When to use Single-turn RFT vs. Multi-turn RFT**  
Choose Single-turn RFT when the task is a one-shot exchange: the model receives a prompt and produces a single response that can be scored on its own, with no intermediate tool calls or environment state to track. This fits use cases like classification, extraction, domain-specific Q&A, summarization, content moderation, or any task with a verifiable answer (exact match, F1, schema validation, a rule-based or LLM-judge check on the final output). It is simpler, cheaper, and faster to run, because each rollout is a single generation and the reward is computed once at the end.

Choose Multi-turn RFT when the task requires the model to act as an agent over several steps — calling tools, reading and mutating state, and adapting to what comes back — before the outcome can be judged. This fits agentic workflows like tool-use sequences, multi-step troubleshooting, conversational assistants, or any task where success depends on the trajectory (the order and correctness of actions across turns), not just a final answer.

Rule of thumb: if your task can be scored from a single model output with no tool calls or evolving state, use Single-turn RFT; if success depends on a sequence of actions against tools or a stateful environment, use Multi-turn RFT.

**When to use Nova 1.0 versus Nova 2.0**  
RFT is only available on Nova 2.0 Lite. For Nova 1.0 models, use Direct Preference Optimization (DPO) or Proximal Policy Optimization (PPO) as alternative alignment techniques.

**Reasoning mode**  
Amazon Nova 2.0 supports reasoning mode during RFT training. The following modes are available:
+ **none**: No reasoning (omit the reasoning\_effort field)
+ **low**: Minimal reasoning overhead
+ **high**: Maximum reasoning capability (default when reasoning\_effort is specified)

**Note**  
There is no medium option for RFT. If the reasoning\_effort field is absent from your configuration, reasoning is disabled.