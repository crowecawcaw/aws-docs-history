

# list-auth-servers
<a name="list-auth-servers"></a>

Lists the external authentication servers that have been registered.

**Topics**
+ [Syntax](#sytnax)
+ [Output](#output)
+ [Example](#example)

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker list-auth-servers
```

## Output
<a name="output"></a>

**`Urls`**  
The URLs of the registered external authentication servers.

## Example
<a name="example"></a>

The following example lists all external authentication servers that have been registered.

**Command**

```
sudo -u root dcv-session-manager-broker list-auth-servers
```

**Output**

```
Urls: [ "https://my-auth-server.com/.well-known/jwks.json" ]
```