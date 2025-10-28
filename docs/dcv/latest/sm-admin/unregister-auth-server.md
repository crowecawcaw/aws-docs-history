# unregister-auth-server

Unregisters an external authentication server. After you unregister an external
authentication server, it can no longer be used to generate OAuth 2.0 access
tokens.

###### Topics

- [Syntax](#sytnax "#sytnax")
- [Options](#options "#options")
- [Output](#output "#output")
- [Example](#example "#example")

## Syntax

```
sudo -u root dcv-session-manager-broker unregister-auth-server --url  `server_url`.well-known/jwks.json
```

## Options

**`--url`**

The URL of the external authentication server to unregister. You must append
`.well-known/jwks.json` to the authentication server URL.

Type: String

Required: Yes

## Output

**`Url`**

The URL of the unregistered external authentication server.

## Example

The following example registers an external authentication server with a URL of
`https://my-auth-server.com/`.

**Command**

```
`sudo -u root dcv-session-manager-broker unregister-auth-server --url https://my-auth-server.com/.well-known/jwks.json`
```

**Output**

```
Jwk urlhttps://my-auth-server.com/.well-known/jwks.json unregistered
```
