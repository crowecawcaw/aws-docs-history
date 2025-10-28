# unregister-agent-client

Unregister an agent from the broker.

###### Topics

- [Syntax](#sytnax "#sytnax")
- [Options](#options "#options")
- [Example](#example "#example")

## Syntax

```
sudo -u root dcv-session-manager-broker unregister-agent-client --client-id `client_id`
```

## Options

**`--client-id`**

The ID of the agent to unregister.

Type: String

Required: Yes

## Example

The following example unregisters an agent.

**Command**

```
`sudo -u root dcv-session-manager-broker unregister-agent-client --client-id 3b0d7b1d-78c7-4e79-b2e1-b976dEXAMPLE`
```

**Output**

```
agent client 3b0d7b1d-78c7-4e79-b2e1-b976dEXAMPLE unregistered
```
