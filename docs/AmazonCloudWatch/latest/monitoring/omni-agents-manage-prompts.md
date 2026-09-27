

# Manage prompts
<a name="omni-agents-manage-prompts"></a>

Manage your agent's prompts as versioned artifacts in the extension, so you can track changes, compare versions, and reuse prompts across runs.

**Availability** Available in the IDE extension only.

You can also use and compare prompt versions in the prompt playground and in experiments. See [Prompt playground](omni-prompt-playground.md) and [Experiments](omni-agents-experiments.md).

**Bring existing prompts under management**

Most agents start with prompts embedded in code. When you set up prompt management, your coding agent finds the prompts in your project and extracts them into managed, versioned artifacts. Each one becomes a named entry with a version history, and your code references the managed prompt instead of an inline string. From then on, every change is a recorded version.

To set it up:

1. In the IDE extension, open the prompt management view.

1. Follow the on-screen onboarding instructions.

1. When the flow hands off to your coding agent, invoke it to perform the extraction.

**What a version captures**

Each version records the prompt's messages and its model configuration (the provider, model, and inference parameters such as temperature and maximum tokens), along with a note describing the change. A comparison between versions reflects both. A version does not capture your agent's tools, orchestration, or code; to compare those, run an experiment. See [Experiments](omni-agents-experiments.md).

Versions are saved to a prompt store in your project, and each save is recorded as a git commit using your note as the commit message. Your prompt history is part of your project's history.

**To create a new version**

You create new versions from the playground: edit the prompt there, and when a change works, save it as a new version with a note describing the change. See [Prompt playground](omni-prompt-playground.md).

**To review and manage versions**

1. In the extension, open the prompt management view and choose a prompt.

1. Select a version from the timeline to see the messages and model configuration it recorded, and compare it with other versions.

1. Each version also shows the traces your agent produced while that version was in effect, so when behavior shifts you can tie the change to a specific version.

1. To try the selected version, choose `Test in Playground`. To roll back to it, choose `Revert`.

Reverting does not delete later versions. It creates a new latest version that restores the older version's messages and model configuration, so the rollback is itself a recorded change.