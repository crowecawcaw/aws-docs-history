# Troubleshooting

This section provides guidance for troubleshooting common issues with AWS Transform custom.

## Log Locations

AWS Transform CLI maintains logs in the following locations:

**Conversation logs:**

```
~/.atx/<conversation_id>/logs/<timestamp>-conversation.log
```

These logs contain the full conversation history for debugging specific transformation executions.

**Developer debug logs:**

```
~/.atx/logs/atx-cli.log
~/.atx/logs/error.log
```

These logs provide detailed information about CLI operations and errors.

## Common Issues

**Installation issues:**

If installation fails, ensure you have Node.js 20 or later installed:

```
node --version
```

Download Node.js from https://nodejs.org/en/download if needed.

**Authentication issues:**

Verify your AWS credentials are configured correctly:

```
aws sts get-caller-identity
```

Ensure your IAM user or role has the required `transform-custom:*` permissions.

**Network connectivity issues:**

If you encounter connection errors, verify network access to required endpoints:

- `desktop-release.transform.us-east-1.api.aws`
- `transform-custom.us-east-1.api.aws`
- `*.s3.amazonaws.com`

If working in an internet-restricted environment, update firewall rules to allowlist these URLs.

**Git issues:**

Ensure Git is installed and your repository is under git source control:

```
git --version
git status
```

AWS Transform custom requires repositories to be under git source control.

**Transformation execution issues:**

If a transformation fails:

1. Review the conversation logs at `~/.atx/<conversation_id>/logs/`
2. Check for build or test failures in the transformation output
3. Verify the build command is correct for your project
4. Try running the transformation in interactive mode to provide feedback

**Conversation resumption issues:**

If you cannot resume a conversation:

- Verify the conversation is less than 30 days old
- Check the conversation ID is correct
- Ensure you have network connectivity

## Getting Support

For additional assistance, visit AWS Support through the [AWS Console](https://support.console.aws.amazon.com/support/home#/ "https://support.console.aws.amazon.com/support/home#/").

When opening a support ticket, include:

- Conversation logs from `~/.atx/<conversation_id>/logs/`
- Debug logs from `~/.atx/logs/`
- Steps to reproduce the issue
- AWS Transform CLI version (`atx --version`)
