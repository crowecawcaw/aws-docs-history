# list-auth-servers

Lists the external authentication servers that have been registered.

###### Topics

- [Syntax](#sytnax "#sytnax")
- [Output](#output "#output")
- [Example](#example "#example")

## Syntax

```
sudo -u root dcv-session-manager-broker list-auth-servers
```

## Output

**`Urls`**

The URLs of the registered external authentication servers.

## Example

The following example lists all external authentication servers that have been registered.

**Command**

```
`sudo -u root dcv-session-manager-broker list-auth-servers`
```

**Output**

```
Urls: [ "https://my-auth-server.com/.well-known/jwks.json" ]
```
