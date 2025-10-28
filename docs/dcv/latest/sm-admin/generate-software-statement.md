# generate-software-statement

Generates a software statement.

Agents must be registered with the broker to enable communication. Agents need a software
statement in order to register with the broker. After the agent has a software
statement, it can automatically register itself with the broker by using the [OAuth 2.0 Dynamic Client Registration
Protocol](https://tools.ietf.org/html/rfc7591 "https://tools.ietf.org/html/rfc7591"). After the agent has registered with the broker, it receives a
client ID and client secret that it uses to authenticate with the broker.

The broker and agent receive and use a default software statement when they're first
installed. You can continue to use the default software statement, or you can choose to
generate a new one. If you generate a new software statement, you must place the
software statement into a new file on the agent, and then add the file path to the
`agent.software_statement_path` parameter in the `agent.conf`
file. After you have done this, stop and restart the agent so that it can use the new
software statement to register with the broker.

###### Topics

- [Syntax](#sytnax "#sytnax")
- [Output](#output "#output")
- [Example](#example "#example")

## Syntax

```
sudo -u root dcv-session-manager-broker generate-software-statement
```

## Output

**`software-statement`**

The software statement.

## Example

The following example generates a software statement.

**Command**

```
`sudo -u root dcv-session-manager-broker generate-software-statement`
```

**Output**

```
software-statement: ewogICJpZCIgOiAiYjc1NTVhN2QtNWI0MC00OTJhLWJjOTUtNmUzOWNhYzkxMDcxIiwKICAiYWN0aXZlIiA6IHRydWUsCiAgImlzc3VlZEF0IiA6IDE1OTY3OTU4ODEuMDYxMDAwMDAwLAogICJicm9rZXJWZXJzaW9uIiA6ICIxLjAuMCIKfQ==
```
