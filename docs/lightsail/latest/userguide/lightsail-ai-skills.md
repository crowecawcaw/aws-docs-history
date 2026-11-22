

# Lightsail AI skills

Lightsail publishes its skills in the [Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/what-is-agent-toolkit.html), which follows the open Agent Skills standard, so you can use them with any agent that supports that standard. Each section that follows describes what a skill does, the command that installs it, and example prompts.

To connect your agent before you install a skill, see [Set up an AI agent for Amazon Lightsail](agent-setup-guide.md).

## Deploying containers to Lightsail
<a name="lightsail-ai-skills-containers"></a>

With the `deploying-containers-to-amazon-lightsail` skill, your agent can deploy a container image from a public registry, a local Docker build, or a GitHub repository to a Lightsail container service. It chooses the capacity and reports what it costs each month, confirms that the public URL serves traffic, and finds why a deployment isn't serving. For more information about container services, see [Deploy and manage containers on Amazon Lightsail](amazon-lightsail-container-services.md).

Run the following command to install the skill.

```bash
npx skills add https://github.com/aws/agent-toolkit-for-aws \
    --skill deploying-containers-to-amazon-lightsail \
    --yes \
    --global
```

The following prompts show the kinds of requests that this skill handles. Each one names the skill, so that your agent uses it instead of answering on its own. Replace the example values with your own.
+ "Use the Lightsail container skill to deploy docker.io/library/nginx:latest to a new container service in us-east-1 on port 80."
+ "Use the Lightsail container skill to build the Dockerfile in this directory and deploy it. The app listens on port 3000."
+ "Use the Lightsail container skill to move my container service to the next power up and tell me the new monthly price."
+ "Use the Lightsail container skill to read the log for my failed deployment and tell me why it failed."