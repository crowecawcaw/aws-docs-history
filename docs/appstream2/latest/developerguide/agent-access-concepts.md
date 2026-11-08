

# How it works
<a name="agent-access-concepts"></a>

Amazon WorkSpaces Applications connects an AI agent to a desktop and gives it the tools to operate that desktop the way a person would. The AI agent is one that you bring, running in the framework or managed runtime of your choice. It connects to WorkSpaces for AI agents, the managed MCP server, using either OAuth or AWS IAM (SigV4) credentials. Through the MCP server, the agent then operates a WorkSpaces Applications desktop, which you prepare in advance, over a secure channel.

As the agent works, the MCP server records its activity to three monitoring services so that you can review every action: it logs each tool call to AWS CloudTrail, stores the screenshots it captures in Amazon S3, and reports the time each tool call takes to CloudWatch. The following diagram shows this flow.

![An AI agent connects to WorkSpaces for AI agents, the managed MCP server, with OAuth or SigV4 and calls tools such as mouse, keyboard, screen, and forwarded tools. WorkSpaces for AI agents operates a WorkSpaces Applications desktop over a secure, monitored channel. Agent activity is recorded in AWS CloudTrail, Amazon S3, and Amazon CloudWatch.](https://docs.aws.amazon.com/appstream2/latest/developerguide/images/agent-access-how-it-works.png)


**The agent**: you bring your own agent. This can be a coding agent such as Claude Code, Kiro, or Codex, or a custom-built agent that you develop with the framework or managed runtime of your choice. The agent connects to the managed MCP server with either OAuth or AWS IAM (SigV4) credentials and drives the work throughout the session.

**The MCP interface**: the agent reaches the desktop through a managed MCP server. WorkSpaces Applications gives the agent a set of tools that let it move and click the mouse, type with the keyboard, and view the screen through screenshots. You can forward additional tools through the same MCP server, so the agent can also read PDFs, access files on the desktop, or run shell commands alongside the built-in tools.

**The desktop**: the agent does its work on a WorkSpaces Applications desktop, a secure and ephemeral environment created for the task. The desktop runs from an image that includes the applications the agent needs to use. You set up the desktop before any agent connects to it: you choose the type of compute environment you need, then configure networking, IAM permissions, and the other settings that control access.

**Monitoring**: you have visibility into everything the agent does. Every tool call is logged in AWS CloudTrail, every screenshot can be stored in Amazon S3, and the time each tool call takes is available in CloudWatch.