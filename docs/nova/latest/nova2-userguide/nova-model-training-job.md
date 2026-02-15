# Amazon Nova customization on SageMaker AI training jobs

SageMaker AI training jobs is an environment that enables you to train machine learning models
at scale. It automatically provisions and scales compute resources, loads training data from
sources like Amazon S3, executes your training code, and stores the resulting model
artifacts.

The purpose of training is to customize the base Amazon Nova model using your proprietary data.
The training process typically involves steps to prepare your data, choose a [recipe](../../../sagemaker/latest/dg/nova-model-recipes.md "../../../sagemaker/latest/dg/nova-model-recipes.md"), modify configuration parameters in YAML files, and submit a training
job. The training process will output trained model checkpoint in a service-managed Amazon S3
bucket. You can use this checkpoint location for evaluation jobs. Nova customization on SageMaker AI
training jobs stores model artifacts in a service-managed Amazon S3 bucket. Artifacts in the
service-managed bucket are encrypted with SageMaker AI-managed KMS keys. Service-managed Amazon S3
buckets don't currently support data encryption using customer-managed KMS keys.

## Best Practices for Amazon Nova customization

### Overview

This section provides an overview of customization techniques and helps you choose the best approach for your needs and available data.

#### Two stages of LLM training

Large language model training consists of two major stages: pre-training and post-training. During pre-training, the model processes tokens of raw text and optimizes for next-token prediction. This process creates a pattern completer that absorbs syntax, semantics, facts, and reasoning patterns from web and curated text. However, the pre-trained model doesn't understand instructions, user goals, or context-appropriate behavior. It continues text in whatever style fits its training distribution. A pre-trained model autocompletes rather than follows directions, produces inconsistent formatting, and can mirror undesirable biases or unsafe content from the training data. Pre-training builds general competence, not task usefulness.

Post-training transforms the pattern completer into a useful assistant. You run multiple rounds of Supervised Fine-Tuning (SFT) to teach the model to follow instructions, adhere to schemas and policies, call tools, and produce reliable outputs by imitating high-quality demonstrations. This alignment teaches the model to respond to prompts as tasks rather than text to continue. You then apply Reinforcement Fine-Tuning (RFT) to optimize behavior using measurable feedback (such as verifiers or an LLM-as-a-judge), balancing trade-offs like accuracy versus brevity, safety versus coverage, or multi-step reasoning under constraints. In practice, you alternate SFT and RFT in cycles to shape the pre-trained model into a reliable, policy-aligned system that performs complex tasks consistently.

### Choose the right customization approach

In this section we will cover post training customization strategies: RFT and SFT.

#### Reinforcement fine-tuning (RFT)

Reinforcement fine-tuning improves model performance through feedback signals—measurable scores or rewards that indicate response quality—rather than direct supervision with exact correct answers. Unlike traditional supervised fine-tuning that learns from input-output pairs, RFT uses reward functions to evaluate model responses and iteratively optimizes the model to maximize these rewards. This approach works well for tasks where defining the exact correct output is challenging, but you can reliably measure response quality. RFT enables models to learn complex behaviors and preferences through trial and feedback, making it ideal for applications that require nuanced decision-making, creative problem-solving, or adherence to specific quality criteria that you can programmatically evaluate. For example, answering complex legal questions is an ideal use case for RFT because you want to teach the model how to reason better to answer questions more accurately.

##### How it works

In reinforcement fine-tuning, you start from an instruction-tuned baseline and treat each prompt like a small tournament. For a given input, you sample a handful of candidate answers from the model, score each one with the reward function, then rank them within that group. The update step nudges the model to make higher-scoring candidates more likely next time and lower-scoring ones less likely, while a stay-close-to-baseline constraint keeps behavior from drifting or becoming verbose or exploitative. You repeat this loop over many prompts, refreshing hard cases, tightening verifiers or judge rubrics when you see exploits, and continuously tracking task metrics.

##### When to use RFT

Tasks that benefit most from RFT share several traits. They have measurable success signals even when a single correct output is hard to specify. They admit partial credit or graded quality so you can rank better versus worse answers within a prompt or using a reward function. They involve multiple objectives that must be balanced (such as accuracy with brevity, clarity, safety, or cost). They require adherence to explicit constraints that you can programmatically check. They operate in tool-mediated or environment-based settings where outcomes are observable (success or failure, latency, resource use). They occur in low-label regimes where collecting gold targets is expensive but automated or rubric-based feedback is plentiful. RFT works best when you can turn quality into a reliable scalar or ranking and want the model to preferentially amplify higher-scoring behaviors without needing exhaustive labeled targets.

**Consider other methods when:**

- You have plentiful, reliable labeled input-output pairs – Use SFT
- The main gap is knowledge or jargon – Use retrieval-augmented generation (RAG)
- Your reward signal is noisy or unreliable and you can't fix it with better rubrics or checkers – Stabilize that first before RFT

##### When not to use RFT

Avoid RFT in these situations:

- You can cheaply produce reliable labeled input-output pairs (SFT is simpler, cheaper, and more stable)
- The gap is knowledge or jargon rather than behavior (use RAG)
- Your reward signal is noisy, sparse, easy to game, or expensive or slow to compute (fix the evaluator first)
- Baseline performance is near-zero (bootstrap with SFT before optimizing preferences)
- The task has deterministic schemas, strict formatting, or a single correct answer (SFT or rule-based validation works better)
- Tight latency or cost budgets can't absorb the extra sampling or exploration RFT requires
- Safety or policy constraints aren't crisply specified and enforceable in the reward

If you can point to "the right answer," use SFT. If you need new knowledge, use RAG. Use RFT only after you have a solid baseline and a robust, fast, hard-to-exploit reward function.

#### Supervised fine-tuning (SFT)

Supervised fine-tuning trains the LLM on a dataset of human-labeled input-output pairs for your task. You provide examples of prompts (questions, instructions, and so on) with the correct or desired responses, and continue training the model on these examples. The model adjusts its weights to minimize a supervised loss (typically cross-entropy between its predictions and the target output tokens). This is the same training used in most supervised machine learning tasks, applied to specialize an LLM.

SFT changes behavior, not knowledge. It doesn't teach the model new facts or jargon it didn't see in pre-training. It teaches the model how to answer, not what to know. If you need new domain knowledge (such as internal terminology), use retrieval-augmented generation (RAG) to provide that context at inference time. SFT then adds the desired instruction-following behavior on top.

##### How it works

SFT optimizes LLM by minimizing the average cross-entropy loss on response tokens, treating prompt tokens as context and masking them from the loss. The model internalizes your target style, structure, and decision rules, learning to generate the correct completion for each prompt. For example, to classify documents into custom categories, you fine-tune the model with prompts (the document text) and labeled completions (the category labels). You train on those pairs until the model outputs the right label for each prompt with high probability.

You can perform SFT with as few as a few hundred examples and scale up to a few hundred thousand. SFT samples must be high quality and directly aligned with the desired model behavior.

##### When to use SFT

Use SFT when you have a well-defined task with clear desired outputs. If you can explicitly state "Given X input, the correct output is Y" and gather examples of such mappings, supervised fine-tuning is a good choice. SFT excels in these scenarios:

- **Structured or complex classification tasks** – Classify internal documents or contracts into many custom categories. With SFT, the model learns these specific categories better than prompting alone.
- **Question-answering or transformation tasks with known answers** – Fine-tune a model to answer questions from a company's knowledge base, or convert data between formats where each input has a correct response.
- **Formatting and style consistency** – Train the model to always respond in a certain format or tone by fine-tuning on examples of the correct format or tone. For instance, training on prompt-response pairs that demonstrate a particular brand voice teaches the model to generate outputs with that style. Instruction-following behavior is often initially taught through SFT on curated examples of good assistant behavior.

SFT is the most direct way to teach an LLM a new skill or behavior when you can specify what the right behavior looks like. It uses the model's existing language understanding and focuses it on your task. Use SFT when you want the model to do a specific thing and you have or can create a dataset of examples.

Use SFT when you can assemble high-quality prompt and response pairs that closely mirror the behavior you want. It fits tasks with clear targets or deterministic formats such as schemas, function or tool calls, and structured answers where imitation is an appropriate training signal. The goal is behavior shaping: teaching the model to treat prompts as tasks, follow instructions, adopt tone and refusal policies, and produce consistent formatting. Plan for at least hundreds of demonstrations, with data quality, consistency, and deduplication mattering more than raw volume. For a straightforward, cost-efficient update, use parameter-efficient methods like Low-Rank Adaptation to train small adapters while leaving most of the backbone untouched.

##### When not to use SFT

Don't use SFT when the gap is knowledge rather than behavior. It doesn't teach the model new facts, jargon, or recent events. In those cases, use retrieval-augmented generation to bring external knowledge at inference. Avoid SFT when you can measure quality but can't label a single right answer. Use reinforcement fine-tuning with verifiable rewards or an LLM-as-a-judge to optimize those rewards directly. If your needs or content change frequently, rely on retrieval and tool use rather than retraining the model.

###### Topics

- [Nova Customization SDK](nova-customization-sdk.md "nova-customization-sdk.md")
- [Fine-tune Nova 2.0](nova-fine-tune-2.md "nova-fine-tune-2.md")
- [Reinforcement Fine-Tuning (RFT) with Amazon Nova models](nova-reinforcement-fine-tuning.md "nova-reinforcement-fine-tuning.md")
- [Monitoring Progress Across Iterations](nova-model-monitor.md "nova-model-monitor.md")
- [Evaluating your SageMaker AI-trained model](nova-model-evaluation.md "nova-model-evaluation.md")
- [Iterative training](smtj-iterative-training.md "smtj-iterative-training.md")
