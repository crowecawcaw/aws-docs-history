

# Use agents in Amazon Braket notebook instances

Amazon Braket notebook instances include tools for agents. An agent can write code, explain code, and help you fix errors. An agent can also use tools to do actions in your notebook instance. The agent uses Model Context Protocol (MCP) servers to connect to AWS and to your notebooks.

Each notebook instance includes the following items. The notebook instance installs and configures these items to work with the Kiro CLI.
+ **Kiro CLI** – Kiro is an agent that runs in a terminal. You can open Kiro from the JupyterLab Launcher or from the left sidebar. For more information, see the [Kiro CLI docs page](https://kiro.dev/docs/cli/).
+ **`amazon-braket` skill** – With a skill, the agent has specialized knowledge. The `amazon-braket` skill contains guidance about the Braket SDK, devices, quantum tasks, and hybrid jobs. For more information, see the [`amazon-braket` skill](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/quantum-computing-skills/amazon-braket) in the Agent Toolkit for AWS GitHub repository.
+ **AWS MCP Server** – With the AWS MCP Server, the agent can call AWS APIs and read AWS documentation. For more information, see [AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html) in the *Agent Toolkit for AWS User Guide*.
+ **Jupyter MCP Server** – With the Jupyter MCP Server, the agent can read and edit your notebooks. For example, the agent can add, change, or run a cell. For more information, see the [jupyter-server-mcp](https://github.com/jupyter-ai-contrib/jupyter-server-mcp) GitHub repository.

**Topics**
+ [Prerequisites](#braket-notebook-agents-prereqs)
+ [Use Kiro](#braket-notebook-agents-kiro)
+ [Use other agents](#braket-notebook-agents-other)

## Prerequisites
<a name="braket-notebook-agents-prereqs"></a>

Before you use an agent, make sure that you have the following items:
+ An Amazon Braket notebook instance. For instructions on how to create a notebook instance, see [Create an Amazon Braket notebook instance](braket-get-started-create-notebook.md).
+ A Kiro account. For more information, see the [Kiro website](https://kiro.dev/).

## Use Kiro
<a name="braket-notebook-agents-kiro"></a>

To use Kiro in your notebook instance, open Kiro in one of the following ways:
+ **From the Launcher** – In the Launcher, under **Other**, choose **Kiro**. Kiro opens in a terminal next to your notebook.  
![The JupyterLab Launcher. The Kiro card is in the Other section, next to the Terminal card.](https://docs.aws.amazon.com/braket/latest/developerguide/images/notebook-kiro-launcher-card.png)
+ **From the left sidebar** – In the left sidebar, choose the **Kiro** icon. Kiro opens in the sidebar.  
![The JupyterLab left sidebar with the Kiro icon selected. The Kiro panel is open and shows the Kiro sign-in options.](https://docs.aws.amazon.com/braket/latest/developerguide/images/notebook-kiro-sidebar-panel.png)

If you are not signed in to Kiro, Kiro starts the sign-in first. Follow the instructions in the terminal. For instructions on how to sign in, see [Device flow](https://kiro.dev/docs/getting-started/authentication/#device-flow) on the Kiro website.

You can also use Kiro in any terminal. To open a terminal in JupyterLab, choose **File**, **New**, **Terminal**. To sign in to Kiro, run the following Kiro CLI command:

```bash
kiro-cli login --use-device-flow
```

To start Kiro, run the following Kiro CLI command:

```bash
kiro-cli
```

The agent can do only the AWS actions that the execution role of your notebook instance allows. For more information, see [Managing access to Amazon Braket](braket-manage-access.md).

## Use other agents
<a name="braket-notebook-agents-other"></a>

You can install other agents in your notebook instance. For instructions on how to install an agent, see [Configuring other coding assistants with JupyterLab AI](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-coding-assistant.html#studio-updated-jl-coding-assistant-other) in the *Amazon SageMaker AI Developer Guide*.

**Installed agents might not stay after a restart**  
The notebook instance does not guarantee that the agents that you install stay after a restart. After you restart the notebook instance, make sure that your agents are installed. If an agent is missing, install it again.