# describe-api-clients

Lists the Session Manager clients that have been registered with the broker.

###### Topics

- [Syntax](#sytnax "#sytnax")
- [Output](#output "#output")
- [Example](#example "#example")

## Syntax

```
sudo -u root dcv-session-manager-broker describe-api-clients
```

## Output

**`name`**

The unique name of the Session Manager client.

**`id`**

The unique ID of the Session Manager client.

**`active`**

Indicates the status of the Session Manager client. If the client is active, the value is
`true`; otherwise, it's `false`.

## Example

The following example lists the registered Session Manager clients.

**Command**

```
`sudo -u root dcv-session-manager-broker describe-api-clients`
```

**Output**

```
Api clients
[ {
"name" : "client-abc",
"id" : "f855b54b-40d4-4769-b792-b727bEXAMPLE",
"active" : false
}, {
"name" : "client-xyz",
"id" : "21cfe9cf-61d7-4c53-b1b6-cf248EXAMPLE",
"active" : true
}]
```
