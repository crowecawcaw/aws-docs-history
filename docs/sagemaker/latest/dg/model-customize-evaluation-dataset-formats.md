

# Supported Dataset Formats for Bring-Your-Own-Dataset (BYOD) Tasks
<a name="model-customize-evaluation-dataset-formats"></a>

The Custom Scorer and LLM-as-judge evaluation types require a custom dataset JSONL file located in AWS S3. You must provide the file as a JSON Lines file adhering to one of the following supported formats. The examples in this doc are expanded for clarity.

Each format has its own nuances but at a minimum all require a user prompt.


**Required Fields**  

| Field | Required | 
| --- | --- | 
| User Prompt | Yes | 
| System Prompt | No | 
| Ground truth | Only for Custom Scorer | 
| Category | No | 

**1. OpenAI Format**

```
{
    "messages": [
        {
            "role": "system",    # System prompt (looks for system role)
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",       # Query (looks for user role)
            "content": "Hello!"
        },
        {
            "role": "assistant",  # Ground truth (looks for assistant role)
            "content": "Hello to you!"
        }
    ]
}
```

**2. SageMaker Evaluation**

```
{
   "system":"You are an English major with top marks in class who likes to give minimal word responses: ",
   "query":"What is the symbol that ends the sentence as a question",
   "response":"?", # Ground truth
   "category": "Grammar"
}
```

**3. HuggingFace Prompt Completion**

Both Standard and Conversational formats are supported.

```
# Standard

{
    "prompt" : "What is the symbol that ends the sentence as a question", # Query
    "completion" : "?" # Ground truth
}

# Conversational
{
    "prompt": [
        {
            "role": "user", # Query (looks for user role)
            "content": "What is the symbol that ends the sentence as a question"
        }
    ],
    "completion": [
        {
            "role": "assistant", # Ground truth (looks for assistant role)
            "content": "?"
        }
    ]
}
```

**4. HuggingFace Preference**

Support for both standard format (string) and conversational format (messages array).

```
# Standard: {"prompt": "text", "chosen": "text", "rejected": "text"}
{
     "prompt" : "The sky is", # Query
     "chosen" : "blue", # Ground truth
     "rejected" : "green"
}

# Conversational:
{
    "prompt": [
        {
            "role": "user", # Query (looks for user role)
            "content": "What color is the sky?"
        }
    ],
    "chosen": [
        {
            "role": "assistant", # Ground truth (looks for assistant role)
            "content": "It is blue."
        }
    ],
    "rejected": [
        {
            "role": "assistant",
            "content": "It is green."
        }
    ]
}
```

**5. Verl Format**

The Verl format (both current and legacy formats) is supported for reinforcement learning use cases. Verl docs for reference: [https://verl.readthedocs.io/en/latest/preparation/prepare\_data.html](https://verl.readthedocs.io/en/latest/preparation/prepare_data.html)

Users of the VERL format typically do not provide a ground truth response. If you want to provide one anyways, use either of the fields `extra_info.answer` or `reward_model.ground_truth`; `extra_info` takes precedence.

SageMaker preserves the following VERL-specific fields as metadata if present:
+ `id`
+ `data_source`
+ `ability`
+ `reward_model`
+ `extra_info`
+ `attributes`
+ `difficulty`

```
# Newest VERL format where `prompt` is an array of messages.
{
  "data_source": "openai/gsm8k",
  "prompt": [
    {
      "content": "You are a helpful math tutor who explains solutions to questions step-by-step.",
      "role": "system"
    },
    {
      "content": "Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May? Let's think step by step and output the final answer after \"####\".",
      "role": "user"
    }
  ],
  "ability": "math",
  "extra_info": {
    "answer": "Natalia sold 48/2 = <<48/2=24>>24 clips in May.\nNatalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May.\n#### 72",
    "index": 0,
    "question": "Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?",
    "split": "train"
  },
  "reward_model": {
    "ground_truth": "72" # Ignored in favor of extra_info.answer
  }
}

# Legacy VERL format where `prompt` is a string. Also supported.
{
  "data_source": "openai/gsm8k",
  "prompt": "Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May? Let's think step by step and output the final answer after \"####\".",
  "extra_info": {
    "answer": "Natalia sold 48/2 = <<48/2=24>>24 clips in May.\nNatalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May.\n#### 72",
    "index": 0,
    "question": "Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?",
    "split": "train"
  }
}
```