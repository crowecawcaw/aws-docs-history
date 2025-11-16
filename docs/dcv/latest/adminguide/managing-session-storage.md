# Managing Amazon DCV Session storage

Session storage is a directory on the Amazon DCV server that clients can access when they are connected to a Amazon DCV session.

If session storage is enabled on the Amazon DCV server, you can use the `dcv set-storage-root` command to specify the directory on
the server to be used for session storage. For more information about enabling session storage on the Amazon DCV server, see [Enabling session storage](manage-storage.md "manage-storage.md").

To set the session storage path, use the `dcv set-storage-root` command and specify the session ID and the path to the
directory to use.

###### Topics

- [Syntax](#managing-session-storage-syntax "#managing-session-storage-syntax")
- [Options](#managing-session-storage-options "#managing-session-storage-options")
- [Examples](#session-storage-example "#session-storage-example")

## Syntax

```
dcv set-storage-root --session `session_id` `/path_to/directory`
```

For the directory path, you can use `%home%` to specify the home directory of the user who is currently signed in.
For example, the `%home%/storage/` path resolves to `c:\Users\`username`\storage\`
on Windows servers. It resolves to `$HOME/storage/` on Linux servers.

###### Note

The `storage-root` value must be an absolute path on macOS.

## Options

The following options can be used with the `dcv set-storage-root` command

**`--session`**

The session ID for which to specify the storage directory.

Type: String

Required: Yes

## Examples

###### Windows Amazon DCV server example

The following example sets to storage path to `c:\session-storage` for a session with a session ID of
`my-session`.

```
`C:\>` dcv set-storage-root --session `my-session c:\session-storage`
```

###### Linux Amazon DCV server example

The following example sets to storage path to a directory named `session-storage` in the current user's home
directory, for a session with a session ID of `my-session`.

```
`$` dcv set-storage-root --session `my-session %home%/session-storage/`
```
