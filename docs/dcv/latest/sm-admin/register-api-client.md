# register-api-client

Registers a Session Manager client with the broker and generates client credentials that can be used by the client to
retrieve an OAuth 2.0 access token, which is needed to make API requests.

###### Important

Ensure that you store the credentials in a safe place. They can't be recovered
later.

This command is used only if the broker is used as the OAuth 2.0 authentication server.

###### Topics

- [Syntax](#sytnax "#sytnax")
- [Options](#options "#options")
- [Output](#output "#output")
- [Example](#example "#example")

## Syntax

```
sudo -u root dcv-session-manager-broker register-api-client --client-name `client_name`
```

## Options

**`--name`**

A unique name used to identify the Session Manager client.

Type: String

Required: Yes

## Output

**`client-id`**

The unique client ID to be used by the Session Manager client to retrieve an
OAuth 2.0 access token.

**`client-password`**

The password to be used by the Session Manager client to retrieve an OAuth 2.0
access token.

## Example

The following example registers a client named `my-sm-client`.

**Command**

```
sudo -u root dcv-session-manager-broker register-api-client --client-name my-sm-client
```

**Output**

```
client-id: 21cfe9cf-61d7-4c53-b1b6-cf248EXAMPLE
client-password: NjVmZDRlN2ItNjNmYS00M2QxLWFlZmMtZmNmMDNkMEXAMPLE
```
