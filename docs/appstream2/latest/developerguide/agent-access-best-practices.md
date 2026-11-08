

# Best practices for building and evaluating computer-use agents
<a name="agent-access-best-practices"></a>

A computer-use agent works in a loop: it looks at the screen, acts, and looks again. The following practices help you build agents that complete tasks reliably, in fewer steps, and at lower cost. They apply across workflows and model families. Results vary with your workflow, model, prompts, and environment, so measure each change on your own tasks.

## Design the action loop
<a name="agent-access-best-practices-loop"></a>

Most of an agent's effort goes into reading the screen and typing, not into moving between windows. Reduce reading errors and the number of steps before you tune navigation.
+ **Give the agent text instead of pixels**. Reading exact values, such as names, email addresses, and account numbers, from a screenshot is a common source of errors. When the data has a text copy, provide it through a tool. For values in tables or columns, also have the agent view the image, because a text layer can mix up columns.
+ **Put the instruction before the screenshot**. When the agent must find and click something, place the instruction ahead of the image in the request, so that the agent knows what to look for.
+ **Start from a known layout**. Maximize each application with a keyboard shortcut before the agent works in it. A consistent layout makes repeated flows more predictable and reduces scrolling.
+ **Prefer the keyboard**. Use keyboard shortcuts to scroll, maximize windows, and open menus, especially for small or hard-to-hit controls. Shortcuts don't depend on locating a control on the screen.
+ **Confirm each action**. An application that is busy can ignore a keystroke. Wait briefly after each action, keep a few recent screenshots in view, and have the agent repeat an action that had no effect.
+ **Use Tab only where it's safe**. The Tab key works well across plain text fields. Click into fields where the application reacts when a field loses focus, such as fields with autofill, dropdowns, or date pickers.
+ **Switch, don't relaunch**. To move between running applications, use the taskbar or the application switcher. Relaunching an application adds steps.
+ **Locate controls on the current screen**. Coordinates copied from an earlier screen go stale when a window moves. Use fixed coordinates only in a maximized, fixed layout.
+ **Detect actions that change nothing**. When two actions in a row leave the screen unchanged, have the agent change approach. Limit repeated scrolling, so that a run doesn't spend its step budget on one action.
+ **Batch actions with care**. A batch shows the agent only the screen after its last action, so end a batch on the one screen that the agent needs to read. Measure whether batching saves time on your full workflow before you rely on it. Return batch errors as text only, because some models reject an error result that includes an image.

## Adapt to the model family
<a name="agent-access-best-practices-models"></a>

Model families operate a desktop differently. Build the agent loop once, and adapt the skill and the settings for each family. A skill tuned for one family usually needs corrections before it works with another.
+ **Send a fresh screenshot after each change**. Some models keep acting on an old screenshot without signaling a problem. Attach a new screenshot after every action that changes the screen.
+ **Handle coordinates explicitly**. Some models report pixel coordinates, and others report coordinates on a normalized grid that you must convert to pixels. State the screen size and the valid coordinate range in the prompt, and check that each click is within the screen.
+ **Size screenshots to the model**. Match the screenshot resolution to the model's image limit. If you downscale a screenshot, scale the model's coordinates back up before you click.
+ **Clear fields before typing**. On some models, typing appends to a field instead of replacing its value. Focus the field, select all, delete, type once, and read the value back.
+ **Control parallel tool calls**. If a model sends several actions in one message regardless of the prompt, turn off parallel tool calls in the client. Run batched actions in order and stop at the first failure.
+ **Keep reasoning effort low by default**. Simple tasks often succeed at low effort, and higher effort adds cost without improving accuracy. Raise the effort for branching or multi-step tasks.
+ **Match the prompt length to the model**. Stronger models can work from a short goal. Add rules only where a model needs them, and shorten the prompt as models improve.
+ **Keep reasoning between turns**. If you call a reasoning model through a framework or a compatibility API, confirm that the model's reasoning is carried from one turn to the next. A loop that drops it can stall.
+ **Compare on cost per finished task**. Models differ in how many tokens they use per step, so price per token alone doesn't predict cost. Compare models with the tool surface that you plan to use.

## Write skills and prompts
<a name="agent-access-best-practices-skills"></a>

The skill, the instructions that you give the agent for a workflow, has a large effect on accuracy and cost. A poorly designed generic prompt can perform worse than no prompt at all.
+ **Include a few working rules**. For example: remember what you read, verify before you move on, change approach after two failed attempts, and wait for the application to respond.
+ **Give facts, not procedures**. Current models need less step-by-step guidance. Keep the skill short, and include the facts that the agent can't discover, such as file paths, field formats, and application quirks.
+ **Define high-value fields**. State the exact format of fields such as identifiers and account numbers, and have the agent check each value against that format before typing.
+ **Make verification required and targeted**. Agents can enter wrong values with full confidence, so don't leave verification to the agent's judgment. Check each value once, right after typing it, and read back the few high-value fields before saving. A full re-check of every field adds steps without improving accuracy.
+ **Correct errors in place**. When a value is wrong, have the agent fix that field instead of clearing and retyping the whole form.
+ **Hand off cleanly to sub-agents**. Give a sub-agent complete instructions and ask for a report at the end, instead of checking its work as it goes.
+ **Improve skills from your own runs**. Review the screenshots, actions, and reasoning of each run, change one rule at a time, and keep a change only if every run still succeeds. Divide the workflow into milestones, so that you can see where failed runs stop.

## Manage context and cost
<a name="agent-access-best-practices-cost"></a>

Cost depends mainly on the context that the model carries and on the number of steps in a run. Each call resends the history, so every extra step costs more than the last. The most effective way to lower cost is to choose the model and skill that finish the task in the fewest steps.
+ **Reset context between tasks**. Start each independent task from a clean context and a known screen state.
+ **Keep only recent screenshots**. Keep a few recent screenshots, such as the last three, and replace older images with a short text note. Keeping only one screenshot can increase cost, because the agent scrolls back to see what it lost.
+ **Tell the agent what you remove**. Explain that older screenshots are removed on purpose, and have the agent record each value in its reply while the value is on the screen.

Prompt caching can lower cost substantially, but only when you build the payload carefully:
+ Only add to the end of the conversation. Caching matches the payload from the start, so an edit to an earlier turn invalidates the cache.
+ Remove old screenshots in batches, not on every turn, so that the cached prefix stays the same between removals.
+ Don't rebuild the conversation on each turn. A payload that changes every turn can cost more with caching than without it.
+ Confirm that caching engages. Models have a minimum prefix size for caching, and a smaller prefix isn't cached and doesn't return an error.

## Measure results
<a name="agent-access-best-practices-measure"></a>
+ **Run enough trials**. Results vary between identical runs. Run many trials, report the spread, and use a statistical test, such as a paired test, before you conclude that one version is better.
+ **Calculate cost from every token type**. Include fresh input, output, cache writes, and cache reads. Providers report cache tokens differently, so check how each one counts them. Report tokens alongside cost.
+ **Report cost with the score**. A change can keep the same success rate although it increases cost. Report the success rate, cost, and steps together, and keep the cost of passing and failing runs separate.
+ **Set the step limit with care**. Set the limit above what the workflow needs, and report how many runs reached it. A run that ran out of steps needs a different fix from a run that produced a wrong result. Also set time and cost limits, and support cancellation.
+ **Change one thing at a time**. Hold everything else fixed, so that you can see the effect of each change.
+ **Sort failures by cause**. Separate failures to read the screen from failures to act. A skill can improve how the agent acts, but not how well the model reads. Before you credit a rule with an improvement, check that the agent followed it.
+ **Grade the outcome, not the agent's report**. Check the saved record and the final screen with an automatic evaluator that requires every field to match, and include a negative control. An agent can report a task as complete when it isn't.
+ **Check your test setup**. Errors in the evaluator or the environment can look like agent failures. Log every prompt, screenshot, and action, so that you can trace failed runs. Don't publish results that you can't reproduce.

## Oversight and safety
<a name="agent-access-best-practices-safety"></a>
+ **Keep a person in the loop**. Require confirmation before consequential or hard-to-reverse actions, such as payments, deletions, or submissions. Treat typing sensitive data into a form as sending it. Check for required confirmation before each action in a batch, and locate the target again after a person approves, because the screen might have changed.
+ **Pass the agent's questions to a person**. Some models stop and ask for confirmation on their own, for example when the screen suggests a production system. Make sure that your loop can show the question to a person.
+ **Limit what the agent can reach**. Run the agent in an isolated environment with minimal permissions. Keep sign-in credentials out of the agent's reach where possible, and limit internet access to an allowlist of domains.
+ **Treat on-screen content as untrusted**. Text on a page or in a document can't grant permissions or change the task. Don't let instructions on the screen redirect the agent.
+ **Keep the agent off the open web**. Put the information that the agent needs in the skill, instead of having it search the web, where it can encounter CAPTCHAs and untrusted content.

## Related resources
<a name="agent-access-best-practices-resources"></a>

Model providers publish computer-use guidance for their models. Their current documentation describes model-specific details, such as supported screen sizes, coordinate systems, and tools.
+ [Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) in the Anthropic documentation
+ [Computer use](https://developers.openai.com/api/docs/guides/tools-computer-use) in the OpenAI documentation
+ [Computer use](https://ai.google.dev/gemini-api/docs/computer-use) in the Gemini API documentation