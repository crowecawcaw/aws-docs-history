# Look up Device Farm desktop browser testing sessions

Sessions are used to keep track of two things:

- Artifacts, which are records of the results of events. For more information, see [Artifacts in Device Farm desktop browser testing](managing-artifacts.md "managing-artifacts.md").
- Actions, which are the series of events that created artifacts. For more information, see [Actions in Device Farm desktop browser testing](managing-actions.md "managing-actions.md").
  You create a session when you start a `RemoteWebDriver`. Sessions are also the base unit of
  billing. Billing is determined by the time between your first WebDriver action (for example, getting a page) and
  the closing or timing out of the session, whichever comes first.

## Looking up sessions

You can use the `getTestGridSession` API action or `get-test-grid-session` CLI
command to look up a session. This action can take two sets of parameters: a session ARN or a project ARN
and a session ID. If you do not know your session ARN or session ID, you can use the
`listTestGridSessions` action or `list-test-grid-sessions` CLI command to search
for sessions. This command can search by session start, end, or status.

The following examples show how you can use the command to find sessions.

Look up sessions by their creation time and status

The following example shows how to look up active sessions created after a specified
time:

```
aws devicefarm list-test-grid-sessions \
    --project-arn "arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-project:`123e4567-e89b-12d3-a456-426655440000`" \
    --creation-time-after "2019-12-04T19:21:13" \
    --status "ACTIVE"
```

Look up sessions by the time they ended

The following example shows how to look up sessions that ended before a specified date and
time:

```
aws devicefarm list-test-grid-sessions \
    --project-arn "arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-project:`123e4567-e89b-12d3-a456-426655440000` \
    --end-time-before "2020-04-21T00:20:00" ; The state, "CLOSED", can be assumed here.
```

Look up a session by ARN

The following example shows how to look up a session by its ARN:

```
aws devicefarm get-test-grid-session --session-arn arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-session:123e4567-e89b-12d3-a456-426655440000/123e4567-e89b-12d3-a456-426655441111
```

Look up a session by project ARN and session ID

The following example shows how to look up a session by its project ARN and session ID:

```
aws devicefarm get-test-grid-session --project-arn arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-project:`123e4567-e89b-12d3-a456-426655440000` --session-id 123e4567-e89b-12d3-a456-426655441111
```
