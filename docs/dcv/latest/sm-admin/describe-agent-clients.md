# describe-agent-clients

Describes the agents that are registered with the broker.

###### Topics

- [Syntax](#sytnax "#sytnax")
- [Output](#output "#output")
- [Example](#example "#example")

## Syntax

```
sudo -u root dcv-session-manager-broker describe-agent-clients
```

## Output

**`name`**

The name of the agent.

**`id`**

The unique ID of the agent.

**`active`**

The state of the agent. `true` if the agent is active; otherwise it's
`false`.

## Example

The following example describes the agents.

**Command**

```
`sudo -u root dcv-session-manager-broker describe-agent-clients`
```

**Output**

```
Session manager agent clients
[ {
"name" : "test",
"id" : "6bc05632-70cb-4410-9e54-eaf9bEXAMPLE",
"active" : true
}, {
"name" : "test",
"id" : "27131cc2-4c71-4157-a4ca-bde38EXAMPLE",
"active" : true
}, {
"name" : "test",
"id" : "308dd275-2b66-443f-95af-33f63EXAMPLE",
"active" : false
}, {
"name" : "test",
"id" : "ce412d1b-d75c-4510-a11b-9d9a3EXAMPLE",
"active" : true
} ]
```
