

# renew-auth-server-api-key
<a name="renew-auth-server-api-key"></a>

Renews the public and private keys used by the broker to sign the OAuth 2.0 access tokens that are vended to the Session Manager client. If you renew the keys, then you must provide the new private key to the developer, as it is needed to make API requests.

**Topics**
+ [Syntax](#sytnax)
+ [Example](#example)

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker renew-auth-server-api-key
```

## Example
<a name="example"></a>

The following example renews the public and private keys.

**Command**

```
sudo -u root dcv-session-manager-broker renew-auth-server-api-key
```

**Output**

```
Keys renewed.
```