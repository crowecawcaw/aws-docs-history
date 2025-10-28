# register-auth-server

Registers an external authentication server for use with the broker.

By default, Session Manager uses the broker as the authentication server to generate OAuth 2.0 access
tokens. If you use the broker as the authentication server, no additional configuration is
required.

However, if you choose to use an external authentication server, such as Active Directory or
Amazon Cognito, you must use this command to register the external authentication server.

###### Topics

- [Syntax](#sytnax "#sytnax")
- [Options](#options "#options")
- [Example](#example "#example")

## Syntax

```
sudo -u root dcv-session-manager-broker register-auth-server --url  `server_url`.well-known/jwks.json
```

## Options

**`--url`**

The URL of the external authentication server to be used. You must append
`.well-known/jwks.json` to the authentication server URL.

Type: String

Required: Yes

## Example

The following example registers an external authentication server with a URL of
`https://my-auth-server.com/`.

**Command**

```
`sudo -u root dcv-session-manager-broker register-auth-server --url https://my-auth-server.com/.well-known/jwks.json`
```

**Output**

```
Jwk url registered.
```
