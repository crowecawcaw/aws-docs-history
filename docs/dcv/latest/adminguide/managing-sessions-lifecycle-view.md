# Viewing Amazon DCV sessions

The administrator on a Windows Amazon DCV server or the root user on a Linux Amazon DCV server can view all active sessions that are running on the
server. Amazon DCV users can only view sessions that they have created.

###### Topics

- [Viewing all active sessions](#list-all "#list-all")
- [Viewing a specific active session](#view-specific "#view-specific")

## Viewing all active sessions

To list the active console or virtual sessions on a Windows or Linux Amazon DCV server, use the `dcv list-sessions`
command.

###### Topics

- [Syntax](#list-all-syntax "#list-all-syntax")
- [Output](#output "#output")

### Syntax

```
dcv list-sessions
```

### Output

The command returns a list of active sessions in the following format.

```
Session: `session-id` (owner:`session-owner` type:`virtual|console` name:'`my session`')
```

## Viewing a specific active session

To view information about a session, use the `dcv describe-session` command and specify the unique session ID.

###### Topics

- [Syntax](#view-specific-syntax "#view-specific-syntax")
- [Output](#output "#output")

### Syntax

```
`$` dcv describe-session `session_id`
```

### Output

In the following example output, the `display-layout` element indicates that the session's display layout is set to
use two 800x600 screens. Of these, the second screen is offset to x=800 (to the right) of the first screen.

```
Session: test
  owner: `session-id`
  name: `session-name`
  x display: :1
  x authority: /run/user/1009/dcv/test.xauth
  display layout: 800x600+0+0,800x600+800+0
```

You can also include the `--json` (or `-j`) option to force the command to return the output in JSON
format. The JSON output provides additional details about the session.

```
`$` dcv describe-session `session-id` --json
```

The following is example JSON output.

```
{
  "id" : "`session-id`",
  "owner" : "dcvuser",
  "name" : "`session-name`",
  "num-of-connections" : 0,
  "creation-time" : "2020-03-02T16:08:50Z",
  "last-disconnection-time" : "",
  "licenses" : [
    {
      "product" : "dcv",
      "status" : "licensed",
      "check-timestamp" : "2020-03-02T16:08:50Z",
      "expiration-date" : "2020-03-29T00:00:00Z"
    },
    {
      "product" : "dcv-gl",
      "status" : "licensed",
      "check-timestamp" : "2020-03-02T16:08:50Z",
      "expiration-date" : "2020-03-29T00:00:00Z"
    }
  ],
  "storage-root" : "",
  "type" : "virtual",
  "x11-display" : ":2",
  "x11-authority" : "/run/user/1009/dcv/vsession.xauth",
  "display-layout" : [
    {
      "width" : 800,
      "height" : 600,
      "x" : 0,
      "y" : 0
    },
    {
      "width" : 800,
      "height" : 600,
      "x" : 800,
      "y" : 0
    }
  ]
}
```
