

# unregister-auth-server
<a name="unregister-auth-server"></a>

Unregisters an external authentication server. After you unregister an external authentication server, it can no longer be used to generate OAuth 2.0 access tokens.

**Topics**
+ [Syntax](#sytnax)
+ [Options](#options)
+ [Output](#output)
+ [Example](#example)

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker unregister-auth-server --url  {{server_url}}.well-known/jwks.json
```

## Options
<a name="options"></a>

**`--url`**  
The URL of the external authentication server to unregister. You must append `.well-known/jwks.json` to the authentication server URL.  
Type: String  
Required: Yes

## Output
<a name="output"></a>

**`Url`**  
The URL of the unregistered external authentication server.

## Example
<a name="example"></a>

The following example registers an external authentication server with a URL of `https://my-auth-server.com/`.

**Command**

```
sudo -u root dcv-session-manager-broker unregister-auth-server --url https://my-auth-server.com/.well-known/jwks.json
```

**Output**

```
Jwk urlhttps://my-auth-server.com/.well-known/jwks.json unregistered
```