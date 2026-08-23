# Connect an AI coding tool

###### Warning

We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

You can provide your AI coding tool with access to your
project and install the Agent Toolkit, which bundles the AWS MCP server configuration and
a curated set of agent skills. This lets your AI coding tool create and manage AWS resources
on your behalf.

## Considerations for connecting your coding tool to your project

- You can connect AI coding tools to a project you own or a project
  that has been shared with you.
- When an AI coding tool or local agent creates AWS resources, you are still
  responsible for them. This includes the proper security of your resources as defined by the
  [shared
  responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") and any charges that might occur from these resources,
  whether they are accounted for in the Free Plan or charged on the Paid
  Plan.
- You are responsible for any actions that your AI coding tool takes on your
  behalf in your projects.
- To view a resource that your agent created, go to the service console for
  that service.
- The credentials you generate are for use by the AWS CLI, AWS Tools for
  PowerShell, and AWS SDKs. External tools may not be supported. The access to your
  resources is valid for 12 hours. Use the following command to renew your
  credentials:

```
aws login --profile `profile-name`
```

Replace `profile-name` with the profile name you chose
during initial setup. The command will automatically open your default browser, but you
do not need to take any action. AWS can renew your credentials for 90 days. After 90
days, you'll need to grant access in a browser window again.

## Connect your AI coding tool to your project

Each project has its own set of credentials that AI coding tools can use to create
and manage AWS resources on your behalf.

AWS Management Console

###### To connect your AI coding tool to your project using the AWS console

1. Open AWS Settings at [https://settings.aws.com](https://settings.aws.com "https://settings.aws.com").
2. In the main navigation pane, choose the project you want to access.
3. In the navigation bar on the upper right, choose **Create and manage
   cloud infrastructure**.
4. Choose **Use your AWS credentials with AI coding
   tools**.
5. Choose **Copy agent prompt** and enter it in your coding
   agent.

This creates a prompt that shares a steering file with your AI coding agent.
The steering file accesses a script from AWS that sets up the connection between
your project credentials and your AI coding agent.

Use your terminal
Run the following command to download and follow the setup instructions:

```
curl -fsSL https://github.com/aws/agent-toolkit-for-aws/blob/main/setup-instructions/setup.md
```

When you use our new AWS experience, your agent will install the AWS MCP server, and
you get access to agent skills that can be used with your projects. You'll also get a rule
file with guidance tuned for this experience. The rule file will also let you define what
level of help you want the agent to provide. The following are the supported help
levels:

- **Low**: While you're building, the skill will
  only flag security risks. It won't suggest any improvements or alternatives to your
  architecture.
- **Medium**: While you're building, the skill
  might ask some clarifying questions if it detects potential issues. It won't suggest any
  improvements or alternatives to your architecture.
- **High**: While you're building, the skill will
  provide a high level of support. It will suggest improvements or alternatives to your
  architecture.

After you've made the connection between your AI coding tool and your project, make sure
you always sign into your project before you log in using `aws login` with your
agent.
