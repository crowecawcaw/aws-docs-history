

# Multi-turn reinforcement learning
<a name="model-customize-mtrl"></a>

Multi-turn reinforcement learning (RL) trains an agent to make good decisions across a sequence of steps, not just in a single moment. The agent observes its environment, takes an action, receives a reward, and moves to a new state, repeating this process over many timesteps. The goal is to learn a policy (model behavior) that maximizes cumulative reward across the whole sequence rather than optimizing for any one step in isolation. This approach is increasingly used to train language models on multi-step reasoning and agentic tasks, where the model takes actions like tool calls, code execution, or web search across several turns and is rewarded based on the whole sequence. This is different from single-turn RLHF/RLAIF, where a reward is assigned to one output at a time.

## A simple analogy
<a name="model-customize-mtrl-analogy"></a>

Imagine you are a customer service agent handling a support ticket. You do not resolve it in one message. You ask clarifying questions, look up the customer's account, try a fix, check if it worked, and follow up if it did not. At the end, the customer either leaves satisfied or they do not. Over time, you get better at recognizing which sequence of steps tends to lead to a good resolution.

Multi-turn RL trains the model the same way. Instead of grading the model on a single response, it lets the model work through a task across multiple steps and rewards it based on the whole sequence. The model learns which decisions earlier in the conversation actually mattered.

## Key terminology
<a name="model-customize-mtrl-terminology"></a>
+ **Agent:** the decision-making entity in the system. It observes the current situation, decides what action to take, and learns over time to improve its strategy. In practice, the agent is powered by an AI model, but the two are not the same thing. The model is the underlying neural network; the agent is the broader system that uses it to perceive, decide, and act. *In simple terms: the customer service rep handling the ticket.*
+ **Environment/Agentic Application:** everything the agent interacts with, including the conversation history, the customer's account details, and any tools the agent can use. *In simple terms: the support platform, the customer, and all the information available to the rep.*
+ **State:** a snapshot of the current situation the agent observes before deciding what to do next. *In simple terms: what the rep knows right now, such as the customer's issue, what has already been tried, and the latest reply.*
+ **Action:** what the agent does at each step, such as asking a clarifying question, calling a tool, or sending a response. *In simple terms: the rep's next move, whether that is asking a question, looking something up, or sending a fix.*
+ **Reward:** the feedback signal the agent receives, either at each step or at the end of the task, indicating how well things went. *In simple terms: did the customer leave satisfied? That outcome is the reward.*
+ **Policy:** the strategy the agent has learned. It maps a given state to the action most likely to lead to a good outcome. *In simple terms: the rep's knowledge built up from experience, knowing what tends to work in a given situation.*
+ **Episode:** one complete run of a task from start to finish. *In simple terms: one full support conversation, from the customer's first message to the resolution.*
+ **Turn:** a single exchange within an episode, typically one action taken by the agent and the response it receives from the environment. In a conversation, this is one message and its reply. *In simple terms: one step in the support conversation, like the agent asking a question and the customer responding.*
+ **Trajectory:** the full sequence of states, actions, and rewards recorded across an entire episode. It is the complete record of what the agent did and what happened as a result, used to compute the reward and update the policy. *In simple terms: the entire transcript of the support conversation from start to finish, including every decision the agent made and how things unfolded.*
+ **Cumulative reward:** the total reward accumulated across all steps in an episode, which is what the agent is ultimately trying to maximize. *In simple terms: not just whether one step went well, but whether the whole conversation went well overall.*

## Use cases for multi-turn reinforcement learning
<a name="model-customize-mtrl-use-cases"></a>

Multi-turn RL is the right approach when a single response is not enough to complete a task well. If your use case involves a sequence of steps, decisions that depend on earlier ones, multi-turn RL is worth considering.

Here are some signals that point toward it:
+ **Your task requires back-and-forth interaction:** The model needs to ask questions, gather information, and adapt based on what it learns along the way. A single prompt-response cycle is not enough. Example: a support agent that diagnoses an issue by asking follow-up questions before suggesting a fix.
+ **The quality of the outcome depends on a sequence of actions:** Getting the right answer at the end requires making the right moves throughout. Rewarding only the final output is not enough if the path to get there matters. Example: a coding assistant that plans, writes, runs, and debugs code across multiple steps.
+ **The model needs to use tools across multiple steps:** The model calls external tools like search, APIs, or code execution, and the results of one tool call influence what it does next. Example: a research assistant that searches for information, evaluates the results, and refines its query before producing a summary.
+ **Mistakes mid-task should be recoverable:** You want the model to recognize when something is not working and course-correct, rather than committing to a bad path from the start. Example: an agent that tries a solution, checks if it worked, and tries a different approach if it did not.
+ **You are seeing good single-turn performance but poor end-to-end task completion:** If your model handles individual steps well but struggles to string them together into a coherent, successful outcome, multi-turn RL can help bridge that gap.

## Supported models, pricing, and regions
<a name="model-customize-mtrl-supported"></a>

### Supported models
<a name="model-customize-mtrl-supported-models"></a>


| Model | Region | 
| --- | --- | 
| Nova Lite 2.0 | IAD (us-east-1), PDX (us-west-2) | 
| GPT-OSS-20B | IAD (us-east-1), PDX (us-west-2) | 
| Gemma-4-31B-it | PDX (us-west-2) | 
| Qwen 3.6 27B | PDX (us-west-2) | 

### Pricing
<a name="model-customize-mtrl-pricing"></a>

For full pricing details, refer to the [public pricing page](https://aws.amazon.com/sagemaker/ai/pricing/). Charges are based on three dimensions:
+ **Prefill:** the cost of processing the input tokens fed into the model at the start of each training step. This includes the prompt, conversation history, and any context the model receives before generating a response.
+ **Sample:** the cost of the tokens the model generates during the training rollout. This is where the model produces its responses, which are then evaluated and used to compute the reward signal.
+ **Train:** the cost of the backward pass, where the model's weights are updated based on the reward signal. This is the core learning step in the RL process.

## Topics
<a name="w2aac29c25c17c13"></a>
+  [Prerequisites](model-customize-mtrl-prereqs.md) 
+  [Preparing your agent](model-customize-mtrl-agent.md) 
+  [Creating assets for multi-turn reinforcement learning](model-customize-mtrl-assets.md) 
+  [Training job submission](model-customize-mtrl-job.md) 
+  [Model evaluation](model-customize-mtrl-evaluation.md) 
+  [Model deployment](model-customize-mtrl-deployment.md) 
+  [Hyperparameters reference](model-customize-mtrl-hyperparams.md) 
+  [Configure a VPC for multi-turn RL jobs](model-customize-mtrl-vpc.md) 
+  [Encryption at rest for multi-turn reinforcement learning](model-customize-mtrl-encryption-at-rest.md) 
+  [Troubleshooting](model-customize-mtrl-troubleshooting.md) 
+  [Quotas](model-customize-mtrl-quotas.md) 
+  [Sample datasets and tutorials](model-customize-mtrl-samples.md) 