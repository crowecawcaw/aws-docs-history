# RFT on Nova 2.0

RFT training data follows the OpenAI conversational format. Each training example is a
JSON object containing messages, reference answers, and optional tool definitions. This
section provides guidance on preparing effective training data for RFT on Nova 2.0.

###### Topics

- [Data format and structure](#nova-hp-rft-data-format "#nova-hp-rft-data-format")
- [Field descriptions](#nova-hp-rft-field-descriptions "#nova-hp-rft-field-descriptions")
- [Hyperparameter guidance](#nova-hp-rft-monitoring-hyperparams "#nova-hp-rft-monitoring-hyperparams")
- [Additional properties](#nova-hp-rft-additional-properties "#nova-hp-rft-additional-properties")
- [Dataset size recommendations](#nova-hp-rft-dataset-size "#nova-hp-rft-dataset-size")
- [Characteristics of effective training
  data](#nova-hp-rft-effective-data "#nova-hp-rft-effective-data")
- [Monitoring RFT training](nova-hp-rft-monitoring.md "nova-hp-rft-monitoring.md")

## Data format and structure

Each training example is a JSON object containing the following:

- **messages**: An array of conversational turns using
  system, user, and optionally assistant roles
- **reference_answer**: Expected output or evaluation
  criteria for reward calculation
- **tools** (optional): Array of function definitions
  available to the model
- **id** (optional): Unique identifier for tracking and
  deduplication

Each example should be on a single line in your JSONL file, with one JSON object per
line.

The following example shows a chemistry problem with reference answer containing
ground truth values:

```
{
  "id": "chem-001",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful chemistry assistant"
    },
    {
      "role": "user",
      "content": "Predict hydrogen bond donors and acceptors for this SMILES: CCN(CC)CCC(=O)c1sc(N)nc1C"
    }
  ],
  "reference_answer": {
    "donor_bond_counts": 2,
    "acceptor_bond_counts": 4,
    "explanation": "Calculated using Lipinski's rule of five: N-H groups (2 donors), N and O atoms with lone pairs (4 acceptors)"
  }
}
```

###### Note

The reference_answer contains ground truth values calculated using
domain-specific rules. Your reward function compares the model's predicted values
against these reference values to calculate a reward score.

The following example shows a math problem with solution steps:

```
{
  "id": "math-001",
  "messages": [
    {
      "role": "system",
      "content": "You are a math tutor"
    },
    {
      "role": "user",
      "content": "Solve: 2x + 5 = 13"
    }
  ],
  "reference_answer": {
    "solution": "x = 4",
    "steps": ["2x = 13 - 5", "2x = 8", "x = 4"]
  }
}
```

The following example shows tool usage with expected behavior:

```
{
  "id": "tool-001",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful game master assistant"
    },
    {
      "role": "user",
      "content": "Generate a strength stat for a warrior character. Apply a +2 racial bonus modifier."
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "StatRollAPI",
        "description": "Generates character stats by rolling 4d6, dropping the lowest die result, and applying a modifier.",
        "parameters": {
          "type": "object",
          "properties": {
            "modifier": {
              "description": "An integer representing the modifier to apply to the total of the stat roll.",
              "type": "integer"
            }
          },
          "required": ["modifier"]
        }
      }
    }
  ],
  "reference_answer": {
    "tool_called": "StatRollAPI",
    "tool_parameters": {
      "modifier": 2
    },
    "expected_behavior": "Call StatRollAPI with modifier=2 and return the calculated stat value"
  }
}
```

## Field descriptions

| Field              | Description                                                      | Additional notes                                                                                         | Required |
| ------------------ | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------- |
| id                 | Unique identifier for this RFT example                           | String (for example, "sample-001"). Useful for tracking and<br>deduplication.                            | No       |
| messages           | Ordered list of chat messages that define the prompt and context | Array of objects. Model sees them in order. Typically starts with a system<br>message, then user.        | Yes      |
| messages[].role    | Who is speaking in the message                                   | Common values: "system", "user" (sometimes "assistant" in other<br>contexts)                             | No       |
| messages[].content | The text content of the message                                  | Plain string. For system it's instructions, for user it's the task or<br>input.                          | No       |
| tools              | Tool specifications available to the model during this example   | Array. Each item defines a tool's interface and metadata. Types may include<br>"function" or "internal". | No       |
| reference_answer   | The expected model output for this example                       | String or object depending on task. Used as target for evaluation or<br>training.                        | No       |

###### Note

Any additional custom fields (for example, task_id, difficulty_level, context_data)
are not validated and will be passed to your reward function as metadata.

## Hyperparameter guidance

Use the following recommended hyperparameters based on your training approach:

**General:**

- Epochs: 1
- Learning rate (lr): 1e-7
- Number of generations: 8
- Max new tokens: 8192
- Batch size: 256

**LoRA (Low-Rank Adaptation):**

- LoRA Rank: 32

###### Note

Adjust these values based on your dataset size and validation performance. Monitor
training metrics to prevent overfitting.

## Additional properties

The "additionalProperties": true setting allows you to include custom fields beyond
the core schema requirements, providing flexibility to add any data your reward function
needs for proper evaluation.

### Common additional fields

You can include the following types of additional fields:

**Metadata:**

- task_id: Unique identifier for tracking
- difficulty_level: Problem complexity indicator
- domain: Subject area or category
- expected_reasoning_steps: Number of steps in solution

**Evaluation criteria:**

- evaluation_criteria: Specific grading rubrics
- custom_scoring_weights: Relative importance of different aspects
- context_data: Background information for the problem
- external_references: Links to relevant documentation or resources

### Example with additional

properties

The following example includes custom metadata fields:

```
{
  "id": "algebra_001",
  "messages": [
    {
      "role": "system",
      "content": "You are a math tutor"
    },
    {
      "role": "user",
      "content": "Solve: 2x + 5 = 13"
    }
  ],
  "reference_answer": {
    "solution": "x = 4",
    "steps": ["2x = 13 - 5", "2x = 8", "x = 4"]
  },
  "task_id": "algebra_001",
  "difficulty_level": "easy",
  "domain": "algebra",
  "expected_reasoning_steps": 3
}
```

## Dataset size recommendations

### Starting point

Begin with the following minimum dataset sizes:

- Minimum 100 training examples
- Minimum 100 evaluation examples

Prioritize high-quality input data and a reliable reward function that executes
consistently on model responses.

### Evaluation-first approach

Before investing in large-scale RFT training, evaluate your model's baseline
performance:

- **High performance (greater than 95% reward)**: RFT
  may be unnecessary—your model already performs well
- **Very poor performance (0% reward)**: Switch to
  SFT first to establish basic capabilities
- **Moderate performance**: RFT is likely
  appropriate

This evaluation-first approach ensures your reward function is bug-free and
determines if RFT is the right method for your use case. Starting small allows you to
get comfortable with the RFT workflow, identify and fix issues early, validate your
approach before scaling up, and test reward function reliability. Once validated, you
can expand to larger datasets to further improve performance.

## Characteristics of effective training

data

### Clarity and consistency

Good RFT examples require clear, unambiguous input data that enables accurate reward
calculation across different model outputs. Avoid noise in your data, including:

- Inconsistent formatting
- Contradictory labels or instructions
- Ambiguous prompts
- Conflicting reference answers

Any ambiguity will mislead the training process and cause the model to learn
unintended behaviors.

### Diversity

Your dataset should capture the full diversity of production use cases to ensure
robust real-world performance. Include:

- Various problem types and difficulty levels
- Different input formats and edge cases
- Representative samples from all expected scenarios

This diversity helps prevent overfitting and ensures the model handles unfamiliar
inputs gracefully.

### Reward function

considerations

Design your reward function for efficient training:

- Execute within seconds (not minutes)
- Parallelize effectively with Lambda
- Return consistent, reliable scores
- Handle different types of model outputs gracefully

Fast, scalable reward functions enable rapid iteration and cost-effective
experimentation at scale.
