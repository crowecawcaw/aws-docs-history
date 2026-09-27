

# Datasets
<a name="omni-agents-datasets"></a>

A dataset is a curated collection of test cases that you evaluate against repeatedly. It gives you a repeatable measurement: because the test cases stay fixed, you can run them after every change and compare scores over time. These evaluation datasets are distinct from the CloudWatch Dataset, the store that holds your space's telemetry (see [CloudWatch Omni](cloudwatch-omni.md)).

**What a test case contains**

Each test case in a dataset represents one scenario:
+ **An input** — the request the agent should handle. For a multi-turn scenario, a test case carries the conversation turns, which run in order within a single session so the agent keeps context between them.
+ **An expected outcome (optional)** — a reference response, the tools the agent is expected to call, or natural-language assertions the response must satisfy. Evaluators that compare against a reference need this; evaluators that judge the response on its own do not. Every test case follows the same dataset schema, so any evaluator can draw the fields it needs from any case.

**Build from real traces**

You can write test cases by hand, but start from real traffic. Your traces already contain the requests your users make and the failures they hit. When you add a trace to a dataset, Omni converts it into a test case: the trace's input becomes the test input, and its response and tool calls can seed the expected outcome for you to review and edit.

**To build a dataset from traces**

1. In [Agent traces](omni-agent-traces.md) or [Agent sessions](omni-agent-sessions.md), find representative runs. Aim for a mix: common requests that must keep working, edge cases, and failures you have fixed and do not want to regress.

1. Add each run to a dataset. Review the generated test case, and record or correct the expected outcome where your evaluators need one.

1. Run your agent against the dataset's test cases (for example, in an experiment) and score the outputs with evaluators to get a baseline. See [Evaluators and evaluations](omni-agents-evaluators.md) and [Experiments](omni-agents-experiments.md).

**Publish a version before you use it**

A dataset you are editing is a working draft. Before you can run it (in the prompt playground or an experiment), you publish it as a numbered version. Publishing matters because:
+ **A version is immutable.** Once published, its test cases are frozen, so a score is always tied to an exact set of cases. Continued editing happens on the draft and does not disturb versions you have already run.
+ **Scores stay comparable over time.** Comparing two agent versions, or a before/after change, is valid only when both ran against the same fixed cases. Versioning guarantees that.
+ **You can keep publishing.** As you add or refine cases, publish a new version. Earlier versions remain available, so you can always re-run an old baseline or track which version produced which result.

**Keep the dataset honest as your agent evolves**
+ When you find a new failure in production, add its trace to the dataset before you fix it. The fix then has a test case proving it. Publish a version so the fix is measured against a frozen baseline.
+ Keep failure cases in the dataset after fixing them; they are your regression suite.
+ If your agent's scope changes, retire test cases that no longer represent real traffic. A dataset full of obsolete cases rewards the wrong behavior. Publish a fresh version once you have pruned.

**Use a dataset in the prompt playground**

In the [Prompt playground](omni-prompt-playground.md) you can run your baseline and candidate variants against a published dataset instead of one hand-typed input, so a comparison covers your whole curated set at once. A candidate that passes cases the baseline fails is evidence that the change works. See [Prompt playground](omni-prompt-playground.md).

**Datasets move between surfaces**

Datasets sync in both directions between the Omni web UI and the IDE extension, using the **Upload to Cloud** and **Download to Local** buttons:
+ **Download to Local** brings a cloud dataset into the extension, so you can run it against your local development loop.
+ **Upload to Cloud** pushes a dataset you built locally (for example, while running your agent on your own machine) up to the Omni web UI, where the team can use it for experiments and shared review.

An operator packages failing traces into a dataset in the Omni web UI, and a developer downloads it to reproduce and fix the problem locally. In the other direction, a developer curating cases against a local agent uploads them so the same cases are available in the cloud. For the end-to-end workflow, see [Tutorial: Fix a production quality regression](omni-agents-close-the-loop.md).

**Each transfer creates a new dataset.** Upload to Cloud and Download to Local always create a **new** dataset in the target environment. They do not publish a new version of an existing dataset, and they do not merge into an existing one.