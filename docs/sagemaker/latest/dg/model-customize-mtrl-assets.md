

# Creating assets for multi-turn reinforcement learning
<a name="model-customize-mtrl-assets"></a>

## Prompt dataset format
<a name="model-customize-mtrl-assets-prompt-dataset-format"></a>

Your training dataset is a collection of prompts that SageMaker AI sends to your agent during training. Each prompt kicks off one rollout: your agent processes it, takes actions across one or more turns, and returns a reward. The quality and structure of your dataset directly affects what the model learns.

### Supported file formats
<a name="model-customize-mtrl-assets-supported-formats"></a>


| Format | Extension | Notes | 
| --- | --- | --- | 
| Apache Parquet | .parquet | Recommended for large datasets — efficient storage and fast loading | 
| JSON Lines | .jsonl | One JSON object per line — easy to create and human-readable | 
| JSON | .json | Array of JSON objects | 
| CSV | .csv | Comma-separated values with a header row | 

### Dataset schema
<a name="model-customize-mtrl-assets-dataset-schema"></a>

**Prompt column detection**

The RFT service detects the prompt column using the following rules, in order:
+ If a column named `prompt` exists, that column is used.
+ Otherwise, the first column in the dataset is used.

Always name your prompt column `prompt` to avoid ambiguity. You can include additional columns for your own tracking purposes, but only the prompt column is read by the RFT service.

**How prompts are used**

The RFT service reads the prompt column and passes the string value directly to your agent as-is. It does not parse, validate, or transform the content. What format to use depends entirely on what your agent expects — a simple agent might take plain text, while a more sophisticated one might expect a JSON string containing conversation history, tool configuration, and reward specifications.

**Data protection**

Because the RFT service passes prompts through without inspection, you are responsible for protecting sensitive content. Consider encoding or encrypting prompt data before storing it, and handling decoding or decryption in your agent.

Common approaches:
+ Base64 encoding — simple obfuscation for non-sensitive data
+ Encryption — for sensitive or proprietary data (e.g., AES with keys managed by your agent)

## Example 1: Simple Q&A Dataset (Plain Text)
<a name="model-customize-mtrl-assets-example1"></a>

For straightforward training tasks with plain text prompts.

**Use case**: Basic question answering, simple instruction following

**Parquet (Python)**

```
import pyarrow as pa
import pyarrow.parquet as pq

data = {
    "prompt": [
        "What is 2 + 2?",
        "Explain the concept of machine learning.",
        "Write a Python function to reverse a string.",
        "What is the capital of France?",
        "How does photosynthesis work?",
    ]
}

table = pa.table(data)
pq.write_table(table, "training_data.parquet")
```

**JSON Lines (.jsonl)**

```
{"prompt": "What is 2 + 2?"}
{"prompt": "Explain the concept of machine learning."}
{"prompt": "Write a Python function to reverse a string."}
```

## Example 2: Search/Reasoning with Tool Use
<a name="model-customize-mtrl-assets-example2"></a>

For tasks requiring external tool access (e.g., search engines) during model reasoning.

**Use case**: Fact-based Q&A with web search, retrieval-augmented reasoning

**Structure:**

```
prompt (column) = JSON string (recommend encoded/encrypted) containing:
├── data_source: Dataset origin identifier
├── prompt: Conversation messages [system, user]
├── ability: Task category (e.g., "fact-reasoning")
├── env_class: "search"
├── reward_spec: Ground truth answer for evaluation
└── extra_info: Tool configuration and metadata
```

**Example Row:**

```
import pyarrow as pa
import pyarrow.parquet as pq
import json

task_data = {
    "data_source": "searchR1_nq",
    "prompt": [
        {
            "role": "system",
            "content": "You are a helpful and harmless assistant."
        },
        {
            "role": "user",
            "content": "Answer the given question. You must conduct reasoning inside <think> and </think> first every time you get new information. After reasoning, if you find you lack some knowledge, you can call a search engine by <search> query </search> and it will return the top searched results between <information> and </information>. You can search as many times as you want. If you find no further external knowledge needed, you can directly provide the answer inside <answer> and </answer>, without detailed illustrations. For example, <answer> Beijing </answer>. Question: total number of death row inmates in the us?"
        }
    ],
    "ability": "fact-reasoning",
    "env_class": "search",
    "reward_spec": {
        "ground_truth": {
            "target": [
                "2,718"
            ]
        },
        "style": "rule"
    },
    "extra_info": {
        "index": 0,
        "question": "total number of death row inmates in the us?",
        "split": "train",
        "need_tools_kwargs": true,
        "tools_kwargs": {
            "search": {
                "create_kwargs": {
                    "question": "total number of death row inmates in the us?",
                    "ground_truth": {
                        "target": [
                            "2,718"
                        ]
                    },
                    "data_source": "searchR1_nq"
                }
            }
        }
    }
}

# Recommend: encode or encrypt before storing
data = {"prompt": [json.dumps(task_data)]}
table = pa.table(data)
pq.write_table(table, "search_training_data.parquet")
```

## Example 3: SQL Generation (Multi-Turn with Complex Context)
<a name="model-customize-mtrl-assets-example3"></a>

For code generation tasks requiring database schemas, multi-step reasoning, and SQL execution feedback.

**Use case**: Text-to-SQL, code generation with execution verification

**Structure:**

```
prompt (column) = JSON string (recommend encoded/encrypted) containing:
├── input_seq: Human-readable task description
├── prompt: Conversation messages [system, user]
├── env_class: "text2sql"
├── reward_spec: Ground truth SQL and evaluation config
├── instance_id: Unique task identifier
├── schema: Database schema definition
├── question: Natural language question
└── extra_info: Additional metadata
```

**Example Row:**

```
import pyarrow as pa
import pyarrow.parquet as pq
import json

task_data = {
    "input_seq": "Task Overview:\nYou are a data science expert. Below, you are provided with a database schema\nand a natural language question. Your task is to understand the schema and\ngenerate a valid SQL query to answer the question.\n\nDatabase Engine: SQLite\n\nDatabase Schema:\nCREATE TABLE countries (\n    country_id INTEGER PRIMARY KEY,\n    english_name TEXT,\n    population INTEGER\n);\n\nCREATE TABLE country_metrics (\n    metric_id INTEGER PRIMARY KEY,\n    country_id INTEGER,\n    metric_type TEXT,\n    year INTEGER,\n    value REAL\n);\n\nQuestion: List all countries with their current population and average\npopulation over the last five years.",
    "prompt": [
        {
            "role": "system",
            "content": "Task Overview:\nYou are a data science expert. Your task is to understand the schema and generate\na valid SQL query to answer the question within limited turns.\n\nInstructions:\n- Make sure you only output the information asked in the question.\n- Think through the steps before generating the final SQL query.\n\nFormat:\n- Conduct thinking inside <think>...</think> blocks.\n- You can use SQL tool written within <sql>your sql</sql> to explore or verify.\n- SQL tool output will be shown inside <observation>...</observation>.\n- Provide the final SQL query inside <solution>...</solution>."
        },
        {
            "role": "user",
            "content": "Database Schema:\nCREATE TABLE countries (\n    country_id INTEGER PRIMARY KEY,\n    english_name TEXT,\n    population INTEGER\n);\n\nCREATE TABLE country_metrics (\n    metric_id INTEGER PRIMARY KEY,\n    country_id INTEGER,\n    metric_type TEXT,\n    year INTEGER,\n    value REAL\n);\n\nQuestion: List all countries with their current population and average\npopulation over the last five years."
        }
    ],
    "env_class": "text2sql",
    "instance_id": "sql_task_001",
    "reward_spec": {
        "ground_truth": "SELECT c.english_name, c.population, AVG(m.value) as avg_pop\nFROM countries c\nJOIN country_metrics m ON c.country_id = m.country_id\nWHERE m.metric_type = 'Population' AND m.year > strftime('%Y', 'now') - 5\nGROUP BY c.country_id;",
        "style": "rule"
    },
    "schema": "CREATE TABLE countries (...); CREATE TABLE country_metrics (...);",
    "question": "List all countries with their current population...",
    "extra_info": {
        "split": "train",
        "difficulty": "medium"
    }
}

# Recommend: encode or encrypt before storing
data = {"prompt": [json.dumps(task_data)]}
table = pa.table(data)
pq.write_table(table, "sql_training_data.parquet")
```

## Best Practices
<a name="model-customize-mtrl-assets-best-practices"></a>

**Dataset Size**

Minimum examples at least equal to `training_batch_size`. 10x\+ your batch size for diversity is recommended.

**Prompt Quality**
+ **Complete context**: Include all information needed for the model to generate useful responses
+ **Consistent structure**: Maintain consistent formatting across all prompts
+ **Avoid duplicates**: Unique prompts provide better training signal
+ **Clear instructions**: For tool-use tasks, provide explicit format instructions

**Data Protection**
+ **Encode or encrypt** prompt content to protect sensitive data
+ **Manage decryption keys** securely on your rollout server
+ The RFT service passes prompts through without inspection, so protection is your responsibility

## Reward function design
<a name="model-customize-mtrl-assets-reward-design"></a>

Reward function design is critical for providing effective learning signals in complex, multi-step agent systems. When designing reward functions for multi-turn RL, consider the following guidelines.
+ **Start with outcome-based rewards.** Score the final result first to establish a clean and reliable baseline before adding intermediate rewards or reward shaping.
+ **Consider continuous rewards over binary rewards.** Continuous rewards can provide clearer partial-credit signals, but are easy to game. Binary rewards are preferred when partial credit is hard to define or when a clean baseline is needed.
+ **Use shaping rewards carefully.** Shaping rewards can guide learning, but they should be used sparingly because overly strong or misaligned shaping may teach shortcuts.
+ **Guard against reward hacking.** Make rewards difficult to exploit, and verify that the model is solving the real task rather than gaming the scoring rule.
+ **Validate before training.** Test the reward function on real trajectories before training to catch bugs, loopholes, or misleading signals.
+ **Monitor behavioral metrics, not just reward.** Track metrics such as completion rate, turn count, tool use, and overfitting gap to ensure the model is improving in the intended way.

### Reward design process
<a name="model-customize-mtrl-assets-reward-process"></a>

1. Define what success looks like and determine whether it can be scored automatically.

1. Evaluate the base model to establish a baseline success rate.

1. Design reward tiers: positive rewards for success, zero rewards for failure, and negative rewards for degenerate behavior.

1. Handle edge cases explicitly, including timeouts, environment errors, malformed outputs, and empty responses.

1. Check each reward component for potential reward hacking.

1. Validate on real trajectories before training.

1. Monitor alongside behavioral metrics during training.

1. Iterate based on initial results.

In practice, a reward function takes the full message history of an episode as input and returns two outputs: a scalar reward (a floating-point score measuring trajectory quality, with higher values indicating better performance) and a metrics dictionary for logging, debugging, and monitoring.

### Example: Search agent reward function
<a name="model-customize-mtrl-assets-reward-example"></a>

The following example shows a reward function for an agent that answers questions using search. It demonstrates outcome evaluation, format shaping, and answer correctness checking.

```
class TextAnswerReward:
    """Reward function to check text answer against gold answers.

    formula: format_coef * (correct_format - 1) + correct_answer
    """

    gold_answers: list[str]
    format_coef: float = 0.1

    async def __call__(self, history: list[Message]) -> tuple[float, dict[str, float]]:
        """Grade the completed episode by checking the final assistant message."""
        final_message = None
        for msg in reversed(history):
            if msg.get("role") == "assistant":
                final_message = msg
                break

        if final_message is None:
            return 0.0, {"format": 0.0, "correct": 0.0}

        content = get_text_content(final_message)

        correct_format = float(self._extract_answer(content) is not None)
        correct_answer = float(self._check_answer(content))

        reward = self.format_coef * (correct_format - 1) + correct_answer
        return reward, {"format": correct_format, "correct": correct_answer}

    def _extract_answer(self, text: str) -> str | None:
        if "Answer:" not in text:
            return None
        parts = text.split("Answer:")
        if len(parts) != 2:
            return None
        return parts[1].strip()

    def _check_answer(self, text: str) -> bool:
        model_answer = self._extract_answer(text)
        if model_answer is None or len(self.gold_answers) == 0:
            return False
        for gold in self.gold_answers:
            if normalize_answer(model_answer) == normalize_answer(gold):
                return True
        return False
```

This reward function includes the following key design choices:
+ **Correctness dominates.** A correct answer always scores higher than an incorrect one, regardless of format.
+ **Format is a small shaping signal.** The format coefficient (0.1) is 10% of the outcome reward, small enough that the model cannot profit from format compliance alone, but large enough to steer it toward parseable outputs.
+ **Wrong format with wrong answer is mildly penalized.** The -0.1 score creates a small gradient away from completely unstructured outputs, without overwhelming the learning signal.
+ **No answer is treated as incorrect with bad format.** If the model never produces an assistant message, the function returns 0.0, distinguishing it from the active penalty of -0.1 for a present but malformed response.