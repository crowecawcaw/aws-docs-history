# unregister-api-client

Deactivates a registered Session Manager client. A deactivated Session Manager client can no longer use its credentials
to retrieve OAuth 2.0 access tokens.

###### Topics

- [Syntax](#sytnax "#sytnax")
- [Options](#options "#options")
- [Example](#example "#example")

## Syntax

```
sudo -u root dcv-session-manager-broker unregister-api-client --client-id `client_id`
```

## Options

**`--client -id`**

The client ID of the Session Manager client to deactivate.

Type: String

Required: Yes

## Example

The following example deactivates a Session Manager client with a client ID of `f855b54b-40d4-4769-b792-b727bEXAMPLE`.

**Command**

```
`sudo -u root dcv-session-manager-broker unregister-api-client --client-id f855b54b-40d4-4769-b792-b727bEXAMPLE`
```

**Output**

```
Client f855b54b-40d4-4769-b792-b727bEXAMPLE unregistered.
```
