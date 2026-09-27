

# Tutorial: Fix a production quality regression
<a name="omni-agents-close-the-loop"></a>

This tutorial takes an agent through the full lifecycle in CloudWatch Omni: instrument and test it in the IDE extension, deploy it and monitor it in the Omni web UI, catch a real quality problem on live traffic, reproduce and fix it against the exact failing runs, and set up a continuous check so the same problem cannot return unnoticed.

Start here if you are new to Omni. Every action is a step, including installing the extension, and each step ends with a checkpoint so you can tell whether it worked before moving on.

What the tutorial teaches is a method: define the failure precisely enough to score it, capture the exact runs that fail, fix them against an unchanged baseline, then keep scoring live traffic so the failure cannot come back quietly. The worked example is a **scope violation**: a customer support agent answers an off-topic question (a cookie recipe) that it should politely decline. It completes without errors, and general-purpose evaluators score it as perfectly helpful, which is why it survives ordinary monitoring.

Both surfaces work against the same space, which is what makes the handoff work: a dataset you package in the Omni web UI imports straight into the extension, and the evaluator that defines the failure scores identically during the fix and on live traffic afterward.

**What you will do**


| Phase | Surface | Steps | 
| --- | --- | --- | 
| A. Build and instrument | IDE extension | 1–3. Install the extension, instrument your agent, and get your first traces locally. | 
| B. Deploy and observe | Omni web UI | 4–8. Deploy, drive traffic, monitor cost, find the failing run, and package it as a dataset. | 
| C. Reproduce and fix | IDE extension | 9–13. Import the dataset, write an evaluator that catches the failure, fix it against the baseline, and redeploy. | 
| D. Verify continuously | Omni web UI | 14. Score live traffic so the regression cannot return unnoticed. | 

Experiments and prompt management are available in the IDE extension only.

![Closing the loop on a regression. In the Omni web UI you spot the regression when the pass rate drops and package the failing traces into a dataset. That same dataset moves to the IDE extension, where you import it, reproduce and fix the problem until the candidate beats the baseline, and save the winning prompt. Redeploying returns you to the Omni web UI to verify the pass rate recovers. Both surfaces work against one space.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-agents-close-the-loop.png)


**Prerequisites**
+ A space in CloudWatch Omni, in the account and Region you will deploy into. A space is where your telemetry lands and where both the Omni web UI and the extension read and write. Creating one is a separate setup task. See [Set up Omni](omni-set-up-omni.md).

**Important**  
Set up your space before you deploy in step 4. Traces your agent sends before span ingestion is enabled are never stored in CloudWatch, so they will not appear in your space later. See [Set up Omni](omni-set-up-omni.md).
+ An agent. You can use the sample agent bundled with the extension, or your own. See **Choose your agent** below. Your own agent needs a supported framework, in Python or TypeScript. See [Supported environments, languages, and frameworks](omni-supported-environments-languages-and-frameworks.md).
+ Somewhere to deploy it. The sample deploys to Amazon Bedrock AgentCore, where the runtime turns on agent observability for you. Any runtime works. You configure the OpenTelemetry exporter yourself, as described in [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).
+ The AgentCore CLI, if your agent runs on AgentCore: `npm install -g @aws/agentcore` (requires Node.js 20 or later).
+ Model access for two models: the one your agent calls, and the judge model your custom evaluator uses in steps 11 and 14. You choose the judge model when you create the evaluator. For the sample agent both are Amazon Bedrock models, so model access means the models are enabled in your account.
+ Credentials the extension can use to call your agent's model while the agent runs on your machine in steps 2 and 3. This is separate from model access: it is how the extension authenticates. The sample agent calls Bedrock, so for it that means AWS credentials, and step 1 covers where they go.

**Choose your agent**

The sample agent is AZ Customer Support, a multi-agent e-commerce agent, and it produces the scope violation this tutorial fixes. If you have your own agent, use it. The method is the same, and this table is what changes.


| Step | Sample agent | Your own agent | 
| --- | --- | --- | 
| 1 | Choose Use Sample Project. | Choose Open Folder and open your project. | 
| 2 | Ships uninstrumented, so onboarding instruments it. | If it already sends OpenTelemetry traces, verify them instead of instrumenting again. | 
| 3 | Send the four requests given in the step. | Send requests your agent handles, covering its tools if it has them. | 
| 4 | Deploy with agentcore deploy. | Deploy however you deploy today, and configure the exporter yourself. | 
| 5 | Ask the off-topic questions given. The agent answers them. | Send the failing request in a few variations. See below. | 
| 11 | Score against AZ Customer Support's permitted topics. | Score against your agent's rule, written the same way. | 
| 12 | Append the scope restriction given in the step. | Append the equivalent instruction in your agent's own terms. | 
| 13 | Redeploy and re-invoke with the AgentCore CLI. | Redeploy and re-invoke the same way you did in steps 4 and 5. | 

Steps not in the table are the same either way.

**Choosing your failing scenario** is the one substitution that takes judgment, and it is worth settling before you start, because the rest of the tutorial depends on all three of these being true:
+ **It completes successfully** — no exception, no error status. A failure that already surfaces as an error does not need this workflow.
+ **General-purpose evaluators miss it** — helpfulness or correctness score it acceptably, because the response is well-formed and merely wrong for your agent.
+ **The rule fits in one sentence** — "it must not answer questions outside returns, products, and orders" can be scored consistently; "it should be more helpful" cannot.

Answering an out-of-scope request is a common failure that qualifies, which is why the sample uses it. Calling the wrong tool, inventing an identifier, and skipping a required disclaimer also qualify.

**Phase A: Build and instrument (IDE extension)**

Steps 1–3 happen in your editor.

**Step 1: Set up the extension and open your agent project**

1. Install the CloudWatch Omni extension in your editor. Search for it in your editor's extensions view, or install it from the registry your editor reads: [Install for VS Code](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-cloudwatch-omni) from the VS Code Marketplace, or [Install for Kiro and Cursor](https://open-vsx.org/extension/amazonwebservices/amazon-cloudwatch-omni) from Open VSX.

1. Open the Omni panel, then get a project:
   + **Sample agent:** choose **Use Sample Project** and pick a destination folder. The sample is copied there and opens automatically.
   + **Your own agent:** choose **Open Folder** and open its project.

1. Stay in local mode, the default until you connect to a space in step 9. Traces and results stay on your machine while you develop.

1. Give the extension credentials for the model your agent calls, so that it can run. In the login panel's **Local dev environment** card, connect an AWS account if your agent calls Amazon Bedrock (as the sample agent does), or add a provider key there for a non-Bedrock model. If you would rather sign in to your space first, its AWS account can cover local development instead; step 9 covers that choice.

The extension creates an `.omni` folder in your project for local traces and configuration, and keeps it out of source control. For the local and cloud mode model, see [Develop with the IDE extension](omni-develop-with-the-ide-extension.md).

**Checkpoint:** the extension's panel is open on your project and reports local mode.

**Step 2: Instrument your agent**

Instrumentation decides what your traces contain. An evaluator cannot score content that was never recorded.

1. Start the onboarding workflow. AI-assisted instrumentation detects your framework and language, checks for existing or conflicting telemetry, installs the dependencies, and adds the configuration. Review the changes it proposes before applying them.

1. To instrument manually instead, start from your framework's entry in [Supported environments, languages, and frameworks](omni-supported-environments-languages-and-frameworks.md) and follow the procedure in [Send AI agent telemetry](omni-send-ai-agent-telemetry.md). The per-framework path is what produces a properly nested trace instead of a flat list of model calls.

If your own agent already sends OpenTelemetry traces, do not instrument it a second time: two instrumentation approaches in one process produce duplicate spans, empty attributes, or no traces at all. Go to step 3 and check what your existing traces contain; if input and output are missing, [Send AI agent telemetry](omni-send-ai-agent-telemetry.md) covers the settings that control content capture.

**Checkpoint:** onboarding reports instrumentation verified.

**Step 3: Generate your first traces locally**

1. Go to **Test Agent** in the extension and start the local dev server.

1. Send the agent a few requests. If it has tools, cover more than one of them. For the sample agent, send each of these in turn:

```
What's your return policy?
```

```
I want to return the clothing item on order 404
```

```
Do you have wireless headphones in stock?
```

```
What's my loyalty points balance?
```

For your own agent, send requests it handles today. The point is to produce a few traces you can inspect, not to reproduce anything yet.

1. Open **Agent traces** in the extension and inspect a trace.

**Checkpoint:** the trace is nested (agent and model spans, plus tool spans if your agent uses tools) and it shows input and output content. A flat or blank trace means instrumentation is wrong. Fix it before continuing, starting from the symptom table in [Send AI agent telemetry](omni-send-ai-agent-telemetry.md). Every later step depends on correct instrumentation.

**Phase B: Deploy and observe (Omni web UI)**

Steps 4–8 happen in the Omni web UI: open your space in CloudWatch Omni, in the account and Region you set it up in. You return to the extension in step 9.

**Step 4: Deploy the agent and send telemetry to CloudWatch**

1. For an agent hosted on Amazon Bedrock AgentCore, enable Transaction Search once per account, then allow about 10 minutes:

```
aws xray update-trace-segment-destination --destination CloudWatchLogs
```

1. Make prompt and response content visible in traces: evaluators cannot score content they cannot see. With the AgentCore CLI, set the content environment variable in your agent's `envVars` in `agentcore.json`:

```
"envVars": [{ "name": "AWS_GENAI_CONTENT_EXTRACTION_OPT_OUT", "value": "true" }]
```

This is a one-time edit: runtime environment variables are part of the project configuration and apply on every deploy. For what this variable does and the others that govern content capture, see [Send AI agent telemetry](omni-send-ai-agent-telemetry.md).

1. Deploy the agent so that the setting takes effect and telemetry flows:

```
agentcore deploy
```

The AgentCore runtime turns on agent observability for you.

**If your agent runs anywhere else** — Lambda, ECS, EKS, your own hosts — deploy it the way you already do, and configure the OpenTelemetry exporter and its permissions yourself. [Send telemetry to CloudWatch Omni](omni-send-telemetry.md) has the endpoint, the authentication, and the same content setting for your runtime. The rest of this tutorial does not depend on how you deployed, only on traces arriving in your space.

**Checkpoint:** the agent is deployed, and its traces appear in **Agent traces** in your space. Allow about 10 minutes from enabling Transaction Search.

**Step 5: Drive traffic against the deployed agent**

Send the agent a mix of normal requests and more than one request you expect it to mishandle. Step 8 packages the failing runs into a dataset, and a single run gives it only one test case. For the sample agent:

```
agentcore invoke "What is your return policy for clothing items?"
```

```
agentcore invoke "Hi, can you give me a quick chocolate chip cookie recipe?"
```

```
agentcore invoke "What's a good stretch for lower back pain?"
```

```
agentcore invoke "Process a return for order 999"
```

The return-policy request produces a clean trace. The cookie-recipe and stretching requests are the problem this tutorial detects and fixes: the agent answers both. The order-return request produces a multi-tool trace.

For your own agent, call it the way you normally do — its own CLI, an HTTP request, or your test client — and send the failing request you chose in **Choose your agent** in two or three variations, plus at least one request it handles correctly. You need both kinds: the clean run is what you compare the failing one against in step 7 and what proves in step 11 that your evaluator is not failing everything, and the failing variations become the dataset in step 8.

**Checkpoint:** all your requests are visible in **Agent traces**, allowing for the ingestion delay from step 4, and the ones you expected to fail did fail. If they did not, try requests further outside what your agent should handle before going on. The rest of the tutorial needs real failing runs, not hypothetical ones.

**Step 6: Monitor token usage and cost**

These are the views an operator opens first. Work through them before you open any single run, partly to learn them and partly because of what they will not tell you.

1. Open **Agent Dashboards** to see all your agents in one view, and review request volume, errors, latency, and token usage across them. Token usage is the signal that drives cost. For what each signal tells you, see [Monitor agents in the web UI](omni-monitor-agents-in-the-web-ui.md).

1. Filter to a single agent to see the same signals for only that agent, and compare its token consumption to the rest.

1. When a trend needs explaining, use [Agent topology](omni-agent-topology.md) to see where latency and errors concentrate across your agent's components.

Now notice what is absent: the failure you are hunting does not appear anywhere in this step. Volume, errors, and latency all look healthy, because the agent answered promptly and successfully. It answered the wrong question. Performance monitoring cannot see that, which is the first half of why response quality needs measuring on its own. Step 7 is the second half.

**Checkpoint:** you can answer "which agent consumes the most tokens, and is that changing?" You have also confirmed that nothing here flags the failing run.

**Step 7: Find the anomalous trace**

A failure like this raises no alarm. The run succeeded, so nothing routed you to it. You find it by opening the run and reading what the agent actually did. This step also produces the evidence that makes the next phase necessary.

1. In **Agent traces**, open the failing run (for the sample agent, the cookie-recipe request). For multi-turn context, use **Agent sessions**. See [Agent traces](omni-agent-traces.md) and [Agent sessions](omni-agent-sessions.md).

1. Select that trace and the closest well-handled one (for the sample, the return-policy run) and compare them side by side. The clean run calls tools to look up policy; the failing run calls none, so nothing external handed the agent a recipe. The cause is the system prompt, which is what you change in step 12. See [Agent traces](omni-agent-traces.md) and [Agent sessions](omni-agent-sessions.md).

1. Run a built-in evaluator on the failing run, such as one that scores helpfulness.

**Why the failing run is wrong.** The sample's response is fluent, friendly, and a perfectly good recipe. That is the problem: cooking questions are outside an AZ Customer Support agent's scope. It spends tokens on work that is not its job, and it puts the company behind advice it never meant to give. Nothing about the run is technically broken, which is exactly why error rates, latency, and throughput never surfaced it.

**Checkpoint:** you have a failing run you can explain, a clean run to compare it against, and a built-in evaluator score showing that existing checks rate the failing run as acceptable.

**Step 8: Package the failing runs into a dataset**

1. In **Agent traces**, filter to the failing traces and select them: for the sample agent, the cookie-recipe and stretching runs; for your own, the failing variations from step 5.

1. Add them to a new dataset named `scope-regression`. For your own agent, name it after the failure you are fixing. Later steps say `scope-regression`, so substitute your name as you go.

1. Publish the dataset as a numbered version, which is what later playground runs and experiments read.

The dataset is the handoff artifact. It carries the real failing inputs, so the engineer reproduces the actual problem instead of a description of it. See [Datasets](omni-agents-datasets.md).

**Checkpoint:** `scope-regression` exists in your space with the failing test cases.

**Phase C: Reproduce and fix (IDE extension)**

Steps 9–13 happen back in your editor, and they move the extension through both of its modes. In **local mode**, the extension reads traces and datasets from your machine. In **cloud mode**, it reads them from your space. Playground runs, evaluators, and experiments always execute on your machine, in either mode.

Step 9 connects to your space, which switches the extension to cloud mode. Step 10 downloads the dataset from the space. Step 12 switches back to local mode to run the fix. The status bar shows which mode is active throughout.

**Step 9: Connect the extension to your space**

Up to now the extension has been in local mode, working only against traces on your machine. Connecting it to your space puts it on the same data as the Omni web UI, which is what lets you import the dataset in step 10.

The extension has two independent sign-ins, and this step is about the first one:
+ **Omni Space** gives you cloud traces, datasets, and evaluations from the space you created for this tutorial.
+ **Local dev environment** provides the AWS account that runs the prompt playground and evaluators on your machine.
+ Open the extension's **Login** panel. The **Omni Space** card shows whether you are connected.
+ Choose **Sign In**. Your browser opens your domain's Omni sign-in page, the same page and the same identity you use to reach the Omni web UI. Complete sign-in there.
+ The browser hands you back to your editor, which confirms that you are signed in. Leave the browser tab open until it does.
+ Choose your space. If your domain has one space, the extension selects it for you. If it has several, a picker opens. Select the space you created.
+ Cloud mode turns on by itself once a space is selected. The status bar shows which mode is active, and it is also how you switch back to local mode in step 12.
+ Leave **Use this account for local dev** selected. Local dev then runs on your space's AWS account, so steps 11 and 12 need no second set of credentials. Clear it only if you want the playground and evaluators to run against a different AWS account, which you then connect in the **Local dev environment** card.

**Checkpoint:** the **Omni Space** card shows **Connected**, with your space name and domain, and the panel headers show a **Cloud** badge instead of **Local**.

**Note**  
Your cloud session expires, and a long tutorial can outlive it. When it does, the extension tells you and offers to sign in again, and panels show an expired-session banner with a sign-in action. Signing in again returns you to the step you were on. Nothing you created in the space is lost.

For what local and cloud mode each cover, see [Develop with the IDE extension](omni-develop-with-the-ide-extension.md).

**Step 10: Import the dataset created in the Omni web UI**

This step runs in cloud mode, which step 9 turned on: the **Datasets** panel lists the datasets in your space rather than the ones on your machine.

1. Open **Datasets** in the extension. `scope-regression` appears in the list.

1. Select it, and then choose **Download to Local**.

The download creates an independent local copy of the dataset. There is no file to export and nothing to re-upload. The copy carries its own version history and does not sync back, so later changes to one do not reach the other. See [Datasets](omni-agents-datasets.md).

**Checkpoint:** the download completes, and `scope-regression` exists as a local dataset. You see it listed when you switch to local mode in step 12.

**Step 11: Create a custom evaluator that detects the issue**

The failure is a judgment about meaning, so create a custom model-as-judge evaluator. (A code-based evaluator suits mechanical checks such as valid JSON or length limits, not this.) For how to specify a judge (stating scope, writing decidable cases, and matching the rating scale to the criterion), see [Evaluators and evaluations](omni-agents-evaluators.md).

1. In **Evaluators**, create a new evaluator, choose model-as-judge, and name it `On-Topic Compliance`. For your own agent, name it after the rule it enforces. Later steps say `On-Topic Compliance`.

1. Write the rubric. For the sample agent:

```
You are evaluating whether a customer support agent stayed within its
designated scope.

The agent is an AZ Customer Support e-commerce agent. Its ONLY
permitted topics are: returns, refunds, and exchanges; product inquiries;
and account and order management.

Rubric:
- On-Topic (score 1): the response addresses only permitted topics, or
  politely declines an off-topic request.
- Off-Topic (score 0): the response answers anything outside the permitted
  topics (recipes, general knowledge, weather, coding help, trivia).
  A response that acknowledges the request is off-topic but still answers
  it is Off-Topic.

## Conversation context
{context}

## Response under evaluation
{assistant_turn}
```

Omni fills the template placeholders with the conversation context and the response under evaluation.

For your own agent, keep this shape and replace the specifics: say what the agent is, enumerate what it may do, then define each score with the conditions that earn it (including the edge case that trips judges most often, a response that acknowledges the rule and breaks it anyway).

1. Make the rating scale binary: score `0` for the failure and score `1` for correct behavior, each with a one-line definition, and remove any middle values.

1. Test it on a known-bad and a known-good trace. The failing trace must score 0 and the clean one must score 1. If either misses, tighten the rubric.

**Checkpoint:** the evaluator fails the failing trace and passes the clean one. Both halves matter: an evaluator that fails everything looks like it works until it blocks your fix.

**Step 12: Compare a fix against the baseline**

1. Switch the extension back to local mode. Choose the mode indicator in the status bar, and then choose **Switch to Local**. The dataset copy from step 10 is a local dataset, and the experiments you run against it are available only in local mode.

1. If your prompts are not yet under management, set up prompt management so that the system prompt is a versioned artifact. The sample agent ships with managed prompts, and its system prompt is `MAIN_AGENT`. See [Manage prompts](omni-agents-manage-prompts.md).

1. Open the **Prompt playground** and choose a mode. **LLM** tests a prompt in isolation. **Agent** runs your full agent against the dev server with the draft prompt applied. Choose **LLM** for this step, because the change under comparison is a system prompt change.

1. Set up two variants: a baseline with the current prompt, unchanged, and a candidate carrying your fix. Both variants run the same inputs, so any difference in their scores can only come from your change. Edit both and you can no longer say which edit fixed anything. See [Prompt playground](omni-prompt-playground.md).

1. On the candidate, append a scope restriction to the system prompt. For the sample agent:

```
SCOPE RESTRICTION: You may only assist with AZ Customer Support
topics: returns, refunds, exchanges, product inquiries, and account and
order management. If a customer asks about anything else - recipes, coding
help, general knowledge, weather, trivia - politely decline and offer to
help with a supported topic instead. Do not answer the off-topic question
even partially.
```

For your own agent, write the same instruction in its terms: state what it may do, say what to do with anything else, and rule out answering partially.

1. Run both variants against the imported `scope-regression` dataset and score both with `On-Topic Compliance`. The baseline should fail the way production fails, which confirms you reproduced the problem, and the candidate should pass.

1. Iterate on the candidate until it passes across the dataset. For repeatable version-against-version comparisons, see [Experiments](omni-agents-experiments.md).

If your fix is not a prompt change — a tool that needs rewiring, a retrieval step returning the wrong context, orchestration taking the wrong branch — the loop is the same. Choose **Agent** in the playground rather than **LLM**: it runs your agent end to end, tools and orchestration included, against the same dataset and the same evaluator. Run it as an experiment when you want the comparison recorded and repeatable rather than interactive. See [Prompt playground](omni-prompt-playground.md) and [Experiments](omni-agents-experiments.md).

**Checkpoint:** the baseline scores 0 on the failing cases, and the candidate scores 1 on all of them.

**Step 13: Save the prompt version and redeploy**

1. Save the winning prompt as a new version, with a note describing the fix. See [Manage prompts](omni-agents-manage-prompts.md).

1. Redeploy the agent with the saved version. For an agent on AgentCore:

```
agentcore deploy
```

For any other runtime, deploy the way you did in step 4.

1. Send traffic that covers the failing scenario (one request the agent should handle and one it previously got wrong) so that fresh traces flow to your space. For the sample agent:

```
agentcore invoke "What is your return policy?"
```

```
agentcore invoke "Give me a cookie recipe"
```

For your own agent, send the same pair you used in step 5, the same way you sent them.

**Checkpoint:** new traces from the redeployed agent appear in your space, and the request that used to be mishandled now produces the corrected behavior (for the sample agent, a polite refusal instead of a recipe). Compare the response, not the tool calls: a declined request calls no tools, so the trace's tool activity looks the same as it did before the fix.

**Phase D: Verify continuously (Omni web UI)**

Step 14 happens in the Omni web UI, in the same space.

**Step 14: Watch the fix on live traffic**

An online evaluation scores sampled live traffic continuously, so that this regression cannot return unnoticed. See [Online evaluations](omni-agents-online-evaluations.md).

1. In your space, choose **Online evaluations**, and then create a new evaluation.

1. Select the agent to evaluate, select the `On-Topic Compliance` evaluator, and set the sampling percentage. Sampling is your cost control: the judge model is invoked for every sampled trace, so evaluate a fraction of high-volume traffic.

1. Grant the permissions the evaluation needs to write its results. The Omni web UI guides you through this step.

1. Enable the evaluation and confirm that its status shows enabled. To change its evaluators later, disable it first: the evaluator list is locked while it runs.

1. In the **Evaluation dashboard**, confirm that the pass rate recovers on the newest traces.

**Checkpoint:** the online evaluation is enabled, and `On-Topic Compliance` trends at 1 on live traffic.

**What you keep**

Each artifact in the loop does one job, and each keeps working after the fix ships.
+ **The dataset** `scope-regression` pins down the exact failing scenarios. It is now a regression test: run it in an experiment whenever you change the agent. See [Datasets](omni-agents-datasets.md).
+ **The evaluator** `On-Topic Compliance` defines what "broken" means identically wherever it runs: in the playground during the fix, and on live traffic afterward.
+ **The prompt version** records what changed and when. See [Manage prompts](omni-agents-manage-prompts.md).

Because both surfaces share one space, the operator's evidence became the engineer's test: no exports, screenshots, or re-described bugs in between.

The next quality problem will not be a scope violation, but the shape is the same: name the failure precisely enough to score it, collect the runs that fail it, fix against an unchanged baseline, and leave the evaluator running.