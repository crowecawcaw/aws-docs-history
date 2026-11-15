

# Deploy agents
<a name="genai-deploy-agents"></a>

## Watch the demo
<a name="watch-the-demo"></a>

See how to deploy a CID agent with `cid-cmd` and then use it in Amazon Quick:

[![AWS Videos](https://img.youtube.com/vi/jvDxORiYdhI?rel=0/0.jpg)](https://www.youtube.com/watch?v=jvDxORiYdhI?rel=0)


## Prerequisites
<a name="prerequisites"></a>
+ At least one of the agent’s dashboards deployed. Agents never deploy dashboards: missing ones are listed with a link to their deployment guide, and the agent works with the dashboards you have. If none of them is deployed, `cid-cmd create-agent` stops and creates nothing.
+ Amazon Quick Enterprise edition, in a Region where Amazon Quick chat agents and Spaces are available. See [Supported AWS Regions for Amazon Quick](https://docs.aws.amazon.com/quick/latest/userguide/regions.html).
+ A Quick user with the **Author Pro** or **Admin Pro** role to own the agent and its Space.
+ IAM permissions for the Amazon Quick agent and Space APIs. Being able to create agents in the Quick console is not enough: the API needs these actions in addition to the usual permissions for deploying CID dashboards.

### IAM actions used by the agent commands
<a name="genai-iam-actions"></a>

 `quicksight:CreateAgent`, `quicksight:DescribeAgent`, `quicksight:UpdateAgent`, `quicksight:UpdateAgentPermissions`, `quicksight:ListAgents`, `quicksight:DeleteAgent`, `quicksight:CreateSpace`, `quicksight:DescribeSpace`, `quicksight:UpdateSpace`, `quicksight:UpdateSpaceResources`, `quicksight:UpdateSpacePermissions`, `quicksight:ListSpaceResources`, `quicksight:SearchSpaces`, `quicksight:DeleteSpace` 

## Create an agent
<a name="create-an-agent"></a>

1. Open [AWS CloudShell](https://console.aws.amazon.com/cloudshell) in the account and Region of your CID dashboards.

1. Install or update `cid-cmd` (version 4.4.19 or later):

   ```
   pip3 install -U cid-cmd
   ```

1. See which agents are ready for your account:

   ```
   cid-cmd list-agents
   ```

1. Create an agent. Choose one from the list, or pass its id, for example `--agent-id finops`:

   ```
   cid-cmd create-agent
   ```

   Before creating anything, `cid-cmd` shows which dashboards and datasets it found and asks you to confirm.

1. Open the link printed at the end and start chatting. The starter prompts are a good first try.

## Use an agent
<a name="use-an-agent"></a>

1. Open the agent: use the link that `cid-cmd create-agent` prints, or in the Quick console choose **Chat agents** and then **Chat** next to the agent.

1. Start with one of the starter prompts, or ask your own question in plain language, for example "Which three savings opportunities should we act on first?"

1. Ask follow-up questions to drill down by account, Region, service or time period. The agent remembers the conversation.

1. To verify a number, ask the agent where to find it in the dashboards.

For more example questions, see the [Agent catalog](genai-agent-catalog.md). For tips on getting better answers, see [Tips and troubleshooting](genai-tips.md).

## Share an agent
<a name="share-an-agent"></a>

Share the agent and its Space with other Quick users from the Quick console: choose **Chat agents**, select the agent and choose **Share**. Users need access to the Space and to its dashboards to get answers. See [Share custom chat agents](https://docs.aws.amazon.com/quick/latest/userguide/custom-agents.html#share-custom-agents).

## Update an agent
<a name="update-an-agent"></a>

Update an agent to get its latest version from CID, or to add a dashboard you deployed after creating it. Choose one of two options. In both, `cid-cmd` first lists what it will change and asks you to confirm.

### Option 1: Update and keep your additions (default)
<a name="option-1-update-and-keep-your-additions-default"></a>

```
cid-cmd update-agent --agent-id finops
```

Adds the dashboards and datasets the agent needs and updates its name, instructions, starter prompts and welcome message. Everything you added yourself stays: dashboards, datasets and knowledge bases in the Space, and Spaces and action connectors on the agent.

### Option 2: Match the CID definition exactly
<a name="option-2-match-the-cid-definition-exactly"></a>

```
cid-cmd update-agent --agent-id finops --on-drift override
```

Does the same as option 1, and also removes everything that is not in the CID definition. Use it to reset an agent you customized, or to clean up content you no longer need.

### What each option changes
<a name="what-each-option-changes"></a>


|  | Option 1 (default) | Option 2 (`--on-drift override`) | 
| --- | --- | --- | 
| Name, instructions, starter prompts, welcome message | Replaced with the CID version | Replaced with the CID version | 
| Dashboards and datasets the agent needs | Added | Added | 
| Dashboards, datasets and knowledge bases you added to the Space | Kept | Removed from the Space | 
| Spaces and action connectors you attached to the agent | Kept | Removed from the agent | 
| Other Space content, such as uploaded files | Kept | Kept | 

Changes you made to the instructions or starter prompts in the Quick console are replaced with both options. To keep your own version, [build your own agent](#genai-build-your-own) instead. Dashboards themselves are never deleted, only removed from the Space.

## Delete an agent
<a name="delete-an-agent"></a>

```
cid-cmd delete-agent --agent-id finops --delete-space
```

 `--delete-space` also deletes the agent’s Space when no other CID agent uses it. Dashboards are never deleted. `cid-cmd` only modifies or deletes agents and Spaces that CID created.

## Build your own agent in the console
<a name="genai-build-your-own"></a>

You can also create an agent manually in the Quick console, for example to start from a CID agent and adapt it:

1. Create a Space and add your CID dashboards. See [Creating a space](https://docs.aws.amazon.com/quick/latest/userguide/creating-spaces.html).

1. Create a chat agent, link the Space and paste the instructions of a CID agent from its `persona.yaml` in the [CID GitHub repository](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/tree/main/agentic/agents). See [Custom chat agents](https://docs.aws.amazon.com/quick/latest/userguide/custom-agents.html).

1. Launch the agent and test it with the prompts from the [Agent catalog](genai-agent-catalog.md).

For all `cid-cmd` options, see the [cid-cmd reference](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/docs/cid-cmd.md).