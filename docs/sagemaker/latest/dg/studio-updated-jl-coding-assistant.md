

# Using a coding assistant to expedite your machine learning workflows
<a name="studio-updated-jl-coding-assistant"></a>

## Overview
<a name="studio-updated-jl-coding-assistant-overview"></a>

JupyterLab in Amazon SageMaker AI includes integrated coding assistant support through the Agent Context Protocol (ACP). By default, Kiro coding assistant is pre-configured in the chat panel, providing AI-powered code completion, debugging assistance, and interactive coding support directly within your JupyterLab environment.

When you use coding assistants in Amazon SageMaker AI JupyterLab, the space automatically loads relevant Amazon SageMaker AI Skills into your assistant's context. These Skills are loaded from the AWSLabs GitHub repository and provide specialized knowledge about SageMaker APIs, ML workflows, best practices, and common patterns, enabling your coding assistant to give more accurate, SageMaker-specific guidance.

Additionally, you can configure other ACP-compatible coding assistants of your choice, giving you flexibility to work with the tools that best fit your workflow. ACP-compatible assistants can benefit from the same Amazon SageMaker AI Skills integration when used within Amazon SageMaker AI JupyterLab.

## What is Agent Context Protocol (ACP)?
<a name="studio-updated-jl-coding-assistant-acp"></a>

The Agent Context Protocol (ACP) is an open protocol that standardizes communication between code editors and AI coding agents. This means you can switch between different coding assistants without learning new interfaces or workflows.

## Minimum requirements
<a name="studio-updated-jl-coding-assistant-requirements"></a>
+ Active Amazon SageMaker AI account with JupyterLab access
+ SageMaker Distribution (SMD) version 4.1
+ For Kiro: Valid Kiro account credentials

## Getting Started
<a name="studio-updated-jl-coding-assistant-getting-started"></a>

**Step 1: Open or Create a SageMaker Space with JupyterLab**

1. Navigate to Amazon SageMaker AI Studio

1. Go to **Spaces** in the left navigation panel or click "Customize with agent" from the model hub

1. Either:
   + Click **Create Space** and select JupyterLab as your application
   + Open an existing Space that includes JupyterLab

**Step 2: Start Using Kiro in the Chat Panel:**

Kiro requires authentication before you can use it as your coding assistant. The chat panel will guide you through the authentication process.

1. In JupyterLab, open the chat panel by clicking the chat icon in the right sidebar

1. You can type @ to see your available agents

1. Select @Kiro from the agent dropdown

1. Start asking questions or requesting code assistance

Note that the first time you use Kiro in a space, it will ask you to log in. In order to log in, follow the instructions provided by the chat, or follow here:

1. In JupyterLab, open a new terminal: **File** > **New** > **Terminal**

1. Run the following command

   ```
   kiro-cli login --use-device-flow
   ```

Select one of the 3 login options in the terminal:

1. Use for Free with Builder ID

1. Use for Free with Google or GitHub

1. Use with Pro license

Follow the instructions and screens for the selected option.

**Example prompts:**
+ "I want to customize a model"

## Accessing Amazon SageMaker AI Skills in Kiro
<a name="studio-updated-jl-coding-assistant-skills"></a>

Amazon SageMaker AI Skills are automatically available when you use Kiro in SageMaker JupyterLab. These Skills are loaded from the AWSLabs GitHub repository and stored in the `.kiro/skills` and `.agent/skills` folders within your JupyterLab environment, making them compatible with any agent that loads from these directories.

Skills are update-able, allowing you to benefit from the latest SageMaker best practices and API patterns as they evolve. To update your Skills, you can pull the latest versions from the AWSLabs repository. You can run the following command to update your skills for use with Kiro:

```
npx skills add https://github.com/awslabs/agent-plugins/tree/main/plugins/sagemaker-ai/skills --all --agent kiro-cli --copy
```

For other agents, please see the [SageMaker AI Skills README](https://github.com/awslabs/agent-plugins/tree/main/plugins/sagemaker-ai) for more information. To view the available Skills in your environment, navigate to the `.kiro/skills` folder in the JupyterLab file browser.

As part of new SageMaker Distribution (SMD) releases, we provide updated versions of the skills. We will update skills automatically as long as they have not been modified or deleted by the user within a space. If you manually update or modify your skills, please use the `npx` commands above to update or reset your skills.

## Configuring Other Coding Assistants with JupyterLab AI
<a name="studio-updated-jl-coding-assistant-other"></a>

Amazon SageMaker AI JupyterLab supports any coding assistant that implements the Agent Context Protocol (ACP). Example assistants that support ACP include:
+ **Claude** (via claude-agent-acp)
+ **OpenCode** (via opencode CLI >= 1.0.0)
+ **Gemini** (via gemini CLI >= 0.34.0)
+ **Codex** (via codex-acp)

To use a different ACP-compatible coding assistant:

1. Install the assistant's CLI tool in your JupyterLab terminal:

   For Claude: `npm install -g @anthropic-ai/claude-code @agentclientprotocol/claude-agent-acp`

   For Gemini: `npm install -g @google/gemini-cli`

   For OpenCode: `npm install -g opencode-ai`
**Note**  
Global npm packages are installed outside of the home directory (`/home/sagemaker-user`) and do not persist when the space restarts. To persist the installation, use a [lifecycle configuration (LCC)](https://docs.aws.amazon.com/sagemaker/latest/dg/jl-lcc.html) or a [custom image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-byoi-how-to.html).

1. Restart the space by running the command `restart-jupyter-server` or by restarting the space via the Studio UI. Please note this will result in any unsaved work or in memory state (like active kernels) being lost.

1. Authenticate with the assistant following its specific authentication process

1. Select the assistant from the persona dropdown in the JupyterLab chat panel (e.g., @Claude, @Gemini, @OpenCode)

Please note that for Claude Code specifically, you can configure it to use AWS Bedrock as the backend. Follow the [prerequisites](https://code.claude.com/docs/en/amazon-bedrock) in the Claude code guide, specifically enabling Bedrock model access and providing your execution role access to `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream`. Then, create the following file to configure Claude Code to use Bedrock.

`~/.claude/settings.json`:

```
{
  "env": {
    "CLAUDE_CODE_USE_BEDROCK": "1"
  }
}
```

## Switching Between Assistants
<a name="studio-updated-jl-coding-assistant-switching"></a>

You can switch between different coding assistants at any time:

1. Type @ to see your available agents

1. Select your preferred assistant (e.g., @Kiro, @Claude, @Gemini)

1. Continue your conversation with the new assistant

Each assistant maintains its own conversation context, so you can switch back and forth as needed for different tasks.

## Switching Between Kiro Profiles
<a name="studio-updated-jl-coding-assistant-profiles"></a>

Kiro in Amazon SageMaker AI JupyterLab supports multiple profiles that are optimized for different workflows and use cases. You can switch between profiles to access different sets of capabilities and behaviors tailored to your current task. Amazon SageMaker AI JupyterLab comes with the following Kiro profiles:
+ **sagemaker-ai-default**: Optimized for general Amazon SageMaker AI development with access to Amazon SageMaker AI Skills. This is the default profile when you first start using Kiro in SageMaker JupyterLab.
+ **kiro-default**: Standard Kiro profile without SageMaker-specific customizations, providing general coding assistance across languages and frameworks.
+ **kiro-planner**: Focused on project planning, architecture design, and high-level technical decision-making for ML projects.

To switch between Kiro profiles in JupyterLab:

1. Open the Kiro chat panel in JupyterLab

1. Type the following command:

   ```
   @Kiro /agent swap <agent name>
   ```

   For example:

   ```
   /agent swap kiro-default
   ```

1. Kiro will confirm the profile switch and reload with the new profile's capabilities

## Additional Resources
<a name="studio-updated-jl-coding-assistant-resources"></a>
+ [Jupyter AI ACP Client Documentation](https://github.com/jupyter-ai-contrib/jupyter-ai-acp-client)
+ [Agent Context Protocol Specification](https://acp-protocol.dev/)
+ [Kiro Documentation](https://kiro.dev/docs)
+ [Amazon SageMaker AI Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/)