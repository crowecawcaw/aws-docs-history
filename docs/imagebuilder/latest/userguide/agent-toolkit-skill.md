# Troubleshoot builds with an AI coding agent

The [Agent Toolkit for
AWS](../../../agent-toolkit/latest/userguide/what-is-agent-toolkit.md "../../../agent-toolkit/latest/userguide/what-is-agent-toolkit.md") gives AI coding agents the tools, knowledge, and guardrails they need
to work with AWS services. It works with agents such as Kiro, Claude Code, Cursor,
and Codex. The toolkit includes the `amazon-ec2-image-builder` skill, a
curated package of instructions and reference material that guides your agent
through Image Builder tasks.

With the skill loaded, your agent can diagnose a failed build from your terminal or
IDE. The skill directs the agent to the workflow step that failed and to the component
logs in Amazon CloudWatch Logs. It provides remediation steps for common failure scenarios such as
instance connectivity timeouts, missing instance profile permissions, and component
errors.

The skill covers the rest of the Image Builder workflow: the build IAM role,
Amazon managed and custom components, image recipes, and infrastructure and
distribution configuration. It handles one-off builds and recurring pipelines
for golden AMI automation and OS patching. It supports Linux, Windows, and macOS
AMIs, and container images.

###### Note

The skill runs in your own AI coding agent. For AI-powered root cause analysis
built into the Image Builder console, see
[Troubleshoot failed builds with AI - Preview](devops-agent-troubleshooting.md "devops-agent-troubleshooting.md").

###### Contents

- [Get the skill](#agent-toolkit-skill-get "#agent-toolkit-skill-get")
- [Considerations](#agent-toolkit-skill-considerations "#agent-toolkit-skill-considerations")

## Get the skill

Your agent can get the skill in the following ways:

- **Discover at runtime through the AWS MCP
  Server** – Agents connected to the AWS MCP Server can
  search for and load the skill on demand, without local installation. For
  more information, see [Skills](../../../agent-toolkit/latest/userguide/skills.md "../../../agent-toolkit/latest/userguide/skills.md") in the
  _Agent Toolkit for AWS User Guide_.
- **Install with the AWS CLI** – The
  following command installs the skill for the AI coding agents that are
  detected on your system. The command specifies the `us-east-1`
  Region because the skills catalog is available only in that Region. This
  doesn't limit where you can use the skill. For setup and version
  requirements, see [AWS CLI](../../../agent-toolkit/latest/userguide/aws-cli.md "../../../agent-toolkit/latest/userguide/aws-cli.md") in
  the _Agent Toolkit for AWS User Guide_.

```
aws agent-toolkit add-skill \
    --skill-name amazon-ec2-image-builder \
    --region us-east-1
```

- **Download from GitHub** – The skill
  source is available in the [Agent Toolkit for AWS repository](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/ec2-skills/amazon-ec2-image-builder "https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/ec2-skills/amazon-ec2-image-builder") on GitHub. Add it to your
  agent's skills directory.

## Considerations

Note the following when you use the skill:

- Your agent uses your AWS credentials to call Image Builder and related services.
  We recommend that you scope the agent's IAM permissions to the minimum
  that the task needs.
- AI generates the responses. Verify the analysis and recommendations
  before you modify your resources.
