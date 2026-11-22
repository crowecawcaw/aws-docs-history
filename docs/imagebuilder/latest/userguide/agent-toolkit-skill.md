

# Use Image Builder with an AI coding agent

The [Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/what-is-agent-toolkit.html) gives AI coding agents the tools, knowledge, and guardrails they need to work with AWS services. It works with agents such as Kiro, Claude Code, Cursor, and Codex. The toolkit includes the `amazon-ec2-image-builder` skill, a curated package of instructions and reference material that guides your agent through Image Builder tasks.

With the skill loaded, your agent can create images from your terminal or IDE. The skill covers the whole Image Builder workflow: the build AWS Identity and Access Management (IAM) role, Amazon managed and custom components, image recipes, and infrastructure and distribution configuration.

The skill handles one-off builds and recurring pipelines for golden Amazon Machine Image (AMI) automation and OS patching. It supports Linux, Windows, and macOS AMIs, and container images.

Your agent can also diagnose a failed build. The skill directs the agent to the workflow step that failed and to the component logs in Amazon CloudWatch Logs. It provides remediation steps for common failure scenarios such as instance connectivity timeouts, missing instance profile permissions, and component errors.

**Note**  
The skill runs in your own AI coding agent. For the AI features built into the Image Builder console, see [Create and update resources with AI](ai-assisted-resource-creation.md) and [Troubleshoot failed builds with AI](devops-agent-troubleshooting.md).

**Topics**
+ [Get the skill](#agent-toolkit-skill-get)
+ [Considerations](#agent-toolkit-skill-considerations)

## Get the skill
<a name="agent-toolkit-skill-get"></a>

**Work with your coding agent**  
For the fastest setup, you can drop this link directly into your agent's context to have your agent fetch the file and follow its steps to install the skill: `https://docs.aws.amazon.com/imagebuilder/latest/userguide/samples/aws-imagebuilder-agent-setup.md`

Your agent can get the skill in the following ways:
+ **Discover at runtime through the AWS MCP Server** – Agents connected to the AWS MCP Server can search for and load the skill on demand, without local installation. For more information, see [Skills](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/skills.html) in the *Agent Toolkit for AWS User Guide*.
+ **Install with the AWS CLI** – The following command installs the skill for the AI coding agents that are detected on your system. The command specifies the `us-east-1` Region because the skills catalog is available only in that Region. This doesn't limit where you can use the skill. For setup and version requirements, see [AWS CLI](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html) in the *Agent Toolkit for AWS User Guide*.

  ```bash
  aws agent-toolkit add-skill \
      --skill-name amazon-ec2-image-builder \
      --region us-east-1
  ```
+ **Download from GitHub** – The skill source is available in the [Agent Toolkit for AWS repository](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/ec2-skills/amazon-ec2-image-builder) on GitHub. Add it to your agent's skills directory.

## Considerations
<a name="agent-toolkit-skill-considerations"></a>

Note the following when you use the skill:
+ Your agent uses your AWS credentials to call Image Builder and related services. We recommend that you scope the agent's IAM permissions to the minimum that the task needs.
+ AI generates the responses. Verify the analysis and recommendations before you modify your resources.