

# Use AI to create resources and troubleshoot builds in Image Builder

EC2 Image Builder provides AI assistance for the two sides of image building: configuring resources and diagnosing failed builds. You can use the AI features built into the Image Builder console, or bring the same capabilities to your own AI coding agent:
+ **Create with AI** – Describe the resource that you want in the Image Builder console, and the assistant suggests values that you review, apply, and submit yourself. For more information, see [Create and update resources with AI](ai-assisted-resource-creation.md).
+ **Troubleshoot** – Start an AI-powered investigation of a failed build from the Image Builder console, and receive a root cause analysis with remediation steps. For more information, see [Troubleshoot failed builds with AI](devops-agent-troubleshooting.md).
+ **Image Builder skill for AI coding agents** – Load the `amazon-ec2-image-builder` skill from the Agent Toolkit for AWS so that an agent such as Kiro, Claude Code, Cursor, or Codex can create images and diagnose failed builds from your terminal or IDE. For more information, see [Use Image Builder with an AI coding agent](agent-toolkit-skill.md).

AWS DevOps Agent powers the console features, which share the same agent space setup and pricing. The skill runs in your own AI coding agent with your AWS credentials, and doesn't use AWS DevOps Agent.

**Topics**
+ [Create and update resources with AI](ai-assisted-resource-creation.md)
+ [Troubleshoot failed builds with AI](devops-agent-troubleshooting.md)
+ [Use Image Builder with an AI coding agent](agent-toolkit-skill.md)