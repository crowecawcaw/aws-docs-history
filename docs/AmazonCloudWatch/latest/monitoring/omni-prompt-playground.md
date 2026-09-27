

# Prompt playground
<a name="omni-prompt-playground"></a>

The Prompt playground is an interactive space to try changes and see the effect immediately, without deploying your agent. Where datasets and experiments give you repeatable measurement, the playground is for quick iteration: form a hypothesis, try it, and see the result. Then formalize what worked into a dataset case or an experiment.

**Differences by surface** In the Omni web UI, the playground supports **prompt testing** — try a prompt against a model and compare outputs. In the IDE extension, it adds **agent behavior testing** — run your agent end to end against test inputs. Agent behavior testing is available in the IDE extension only.

**Model access (first-time use)** The playground invokes Amazon Bedrock foundation models directly. The first time you use a given model in your account, you may need to request access to it in the Amazon Bedrock console first — see [Add or remove access to Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html). Until access is granted, runs against that model fail with an access error.

**Work in variants: baseline against candidate**

The playground is organized around side-by-side variants. You start with a baseline (your current prompt or agent configuration, unchanged) and add a variation that carries your proposed change, such as an appended instruction or a different model. Both variants run the same input, so the difference in output can only come from your change. Leave the baseline unchanged: if you edit both variants, you can no longer tell which edit caused the improvement.

**Prompt testing**

Prompt testing runs a prompt directly against a model — no agent in the loop — so you can isolate the prompt as the variable. Use it to compare phrasings, instructions, or models side by side before changing your agent.

1. Choose `Prompt playground`, and select a prompt version from your managed prompts as the baseline, or enter a prompt directly.

1. Add a variation, and apply your change to it. Leave the baseline unchanged.

1. Run both variants against the same input and compare the outputs. To score the comparison, run an evaluator over both results: a failing baseline and a passing candidate is evidence that the change works. See [Evaluators and evaluations](omni-agents-evaluators.md).

1. When a variant performs better, save it as a new prompt version with a note describing the change, so your agent can use it and you can trace which version produced which behavior. See [Manage prompts](omni-agents-manage-prompts.md).

**Agent behavior testing (IDE extension)**

Agent behavior testing runs your agent (its prompts, tools, and orchestration together) against test inputs from inside the extension. Unlike prompt testing, this exercises the full execution path, so you see the trace the run produced and can tell whether a change fixed the behavior or only moved the failure. It uses the local dev server, so iterations stay on your machine. See the local testing steps in [Develop with the IDE extension](omni-develop-with-the-ide-extension.md).

You can also run the variants against the test cases in a dataset (in prompt testing or agent behavior testing), so the comparison covers your curated scenarios instead of a single hand-typed input. A dataset alone is not enough: the run requires a prompt version. The dataset supplies only the test cases. This is the step before formalizing the change as an experiment. See [Datasets](omni-agents-datasets.md).