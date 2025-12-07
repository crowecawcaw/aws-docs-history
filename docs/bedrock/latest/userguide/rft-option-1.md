# Option 1: Provide your own prompts for data preparation

Collect your prompts and store them in `.jsonl` file format. Each record in the JSONL must use the OpenAI chat completion
format in the following structure:

- In the messages field, include the user, system or assistant role containing the input prompt provided to the model.
- [Optional] You can add fields used by grader Lambda for grading.
  **Example format:**

```
{
  "messages": [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What is machine learning?"}
  ],
  "reference_answer": "Machine learning is a subset of artificial intelligence that enables computers to learn and make decisions from data without being explicitly programmed."
}
```
