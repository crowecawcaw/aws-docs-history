# Security considerations and best practices

Amazon Q provides powerful capabilities that can modify your system and AWS resources. Understanding security implications and following best practices helps you use these capabilities safely.

## Understanding security risks

When using Amazon Q, be aware of the following potential security risks:

- _Unintended system changes_: Amazon Q may interpret your requests in unexpected ways, leading to unintended modifications
- _AWS resource modifications_: Resources could be created, modified, or deleted, potentially affecting production environments or incurring costs
- _Data loss_: Commands that delete or overwrite files could result in data loss
- _Security vulnerabilities_: Commands might compromise system security if not properly reviewed

These risks are significantly increased when using `/tools trust-all` or `/acceptall`, which bypass confirmation prompts.

Specific examples of risks include:

- A request to "clean up old files" might delete important configuration files
- A request to "optimize my EC2 instances" might terminate running instances
- A request to "fix security issues" might modify permissions in ways that expose sensitive data

###### Warning

AWS recommends against using `/tools trust-all` or `/acceptall` mode in production environments or when working with sensitive data or resources. You are responsible for all actions performed by Amazon Q.

## General security best practices

When using Amazon Q in any environment, especially those with sensitive files, private keys, tokens, or other confidential information, consider implementing these security measures:

### Restricting file access

By default, Amazon Q can read files without asking for permission each time (`fs_read` is trusted by default). For sensitive environments, you can restrict this behavior:

```
Amazon Q> /tools untrust fs_read
```

With this setting, Amazon Q will ask for your explicit permission before reading any file. This gives you granular control over which files Amazon Q can access during your session.

You can also make this setting persistent by adding it to your shell startup script:

```
echo 'alias q="q --untrust-fs-read"' >> ~/.bashrc
```

This ensures that every new Amazon Q session starts with `fs_read` untrusted, requiring explicit permission for file access.

### Additional security measures

For environments with highly sensitive information, consider these additional measures:

- Use Amazon Q in a dedicated development environment that doesn't contain sensitive credentials or data
- Store sensitive files outside your project directories or in locations with restricted permissions
- Use environment variables for sensitive values instead of hardcoding them in files
- Consider using `/tools untrust use_aws` to require explicit permission before making AWS API calls
- Use project rules to define security guidelines and restrictions (see [Using project rules](command-line-context.md#command-line-context-profiles-project-rules "command-line-context.md#command-line-context-profiles-project-rules")
  )

## Using /tools trust-all safely

If you must use `/tools trustall` or `/acceptall` for specific workflows, follow these safety practices to minimize risks:

- Only use in development or testing environments, never in production
- Enable `/tools trust-all` only for specific tasks, then immediately disable it using `/tools reset` to return to default permissions
- Back up important data before enabling `/tools trust-all`
- Use AWS credentials with minimal permissions when `/tools trust-all` is enabled
- Carefully monitor all actions Amazon Q takes while `/tools trust-all` is enabled

To return to the default permission settings after using `/tools trust-all`, use the reset command:

```
Amazon Q> /tools reset
```

This reverts all tools to their default permission levels, with only `fs_read` trusted by default.
