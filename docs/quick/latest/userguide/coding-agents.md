

# Coding agents
<a name="coding-agents"></a>

In addition to cloud connectors, you can add a coding agent, an external AI coding tool such as Kiro or Claude Code, that Amazon Quick can hand development work to. Amazon Quick communicates with the coding agent by using the Agent Client Protocol (ACP). Like other local connectors, a coding agent runs on your own machine, so it is available only when that machine is on and connected. For an overview of cloud connectors, see [Connectors](action-integrations.md). For information about local connectors, see [Local connectors](local-connectors.md).

**To add a coding agent**

1. Open the Desktop App, go to **Customize**, and choose the **Connectors** tab.

1. Choose **Create**, and then choose **Coding agent**.

1. Configure the connection settings, and choose **Save**.

Each coding agent shows its name, a description, and a toggle to enable or disable it. After you configure a coding agent, you can delegate tasks to it from chat. For example, you can ask Amazon Quick to use Kiro to refactor a module, or ask Claude Code to write tests for a function. Amazon Quick dispatches the work to the coding agent and reports the results to you.