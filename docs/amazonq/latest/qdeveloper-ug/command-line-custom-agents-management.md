# Managing custom agents

This section covers how to organize, manage, and work with custom agents effectively in your development workflow.

## Custom agent file locations

Custom agent configuration files are stored as JSON files in specific directories:

Global custom agents

`~/.aws/amazonq/cli-agents/{agent-name}.json`

Available across all projects and directories on your system.

Project-level custom agents

`.amazonq/cli-agents/{agent-name}.json`

Available only within the specific project directory and its subdirectories.

**Important:** The `{agent-name}` in the filename is for your reference only. The actual agent name is determined by the `name` field within the JSON configuration file itself, which is required.

### Custom agent precedence and conflict resolution

When Amazon Q Developer CLI looks for an custom agent, it follows a specific precedence order:

1. **Local custom agents first** - Checks for custom agents in the current working directory
2. **Global custom agents second** - Falls back to custom agents in your home directory
3. **Built-in default** - Uses the default agent if no custom custom agent is found

If both local and global directories contain custom agents with the same name, the local custom agent takes precedence. Amazon Q Developer CLI will display a warning message when this occurs:

```
WARNING: Agent conflict for my-agent. Using workspace version.
```

This precedence system allows you to:

- Override global custom agents with project-specific versions
- Test custom agent modifications locally before making them global
- Maintain different custom agent configurations for different projects

## Best practices for organizing custom agents

### When to use global custom agents

Use global custom agents for:

- **General-purpose workflows** - Custom agents used across multiple projects
- **Personal productivity** - Custom agents tailored to your individual work style
- **Common development tasks** - Code review, debugging, documentation generation
- **Tool-specific workflows** - AWS management, Git operations, Docker workflows

### When to use local custom agents

Use local custom agents for:

- **Project-specific configurations** - Custom agents that need access to specific project files
- **Team collaboration** - Custom agents shared through version control
- **Development environments** - Custom agents with unique requirements for specific projects
- **Testing and experimentation** - Temporary custom agent modifications without affecting global settings

### Custom agent naming conventions

Consider these naming conventions for better custom agent organization:

- **Purpose-based names** - `aws-specialist.json`, `code-reviewer.json`, `documentation-writer.json`
- **Technology-specific names** - `python-dev.json`, `react-frontend.json`, `terraform-ops.json`
- **Project-specific names** - `project-alpha.json`, `mobile-app.json`, `api-backend.json`
- **Environment-specific names** - `development.json`, `staging.json`, `production.json`

## Editing existing agents

You can modify existing agents during a chat session using the `/agent edit` command:

```
/agent edit agent-name
```

This opens the agent configuration file for editing. After saving changes, restart your chat session to use the updated configuration.

## Sharing custom agents with teams

Local custom agents can be shared with team members through version control systems. This approach allows teams to:

- **Standardize development environments** - Ensure all team members have access to the same tools and configurations
- **Share project-specific context** - Include project documentation, coding standards, and custom scripts
- **Maintain consistency** - Use the same tool permissions and settings across the team
- **Collaborate on improvements** - Use pull requests to review and improve custom agent configurations

### Version control best practices

When sharing custom agents through version control:

- **Include custom agent directories** - Add `.aws/amazonq/agents/` to your repository
- **Document custom agent purposes** - Use clear descriptions in custom agent configuration files
- **Review custom agent changes** - Treat custom agent configuration changes like code changes
- **Test custom agent configurations** - Verify that shared custom agents work correctly for all team members
- **Avoid sensitive information** - Don't include API keys, passwords, or personal information in shared custom agents
