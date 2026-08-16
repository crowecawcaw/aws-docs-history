# Authentication using SCRAM-SHA-256

Amazon DocumentDB (with MongoDB compatibility) supports the Salted Challenge Response Authentication Mechanism (SCRAM) for password-based authentication.
With SCRAM, the server verifies that a client knows a user's password without transmitting the password to the server.
Amazon DocumentDB supports two SCRAM mechanisms: `SCRAM-SHA-1` and `SCRAM-SHA-256`.
`SCRAM-SHA-256` uses the stronger SHA-256 hash function and works with FIPS mode.

You assign one or both SCRAM mechanisms to a user when you create or update that user.
Users that were created with `SCRAM-SHA-1` continue to work without any changes.
SCRAM-SHA-256 authentication is available in Amazon DocumentDB instance-based cluster minor versions 5.0.1+ and 8.0.1+.

###### SCRAM and IAM authentication are mutually exclusive

A user can have either a SCRAM mechanism or the `MONGODB-AWS` mechanism, but not both.
For IAM identity authentication, see [Authentication using IAM identity](iam-identity-auth.md "iam-identity-auth.md").

###### Topics

- [Creating users with SCRAM mechanisms](#scram-sha-256-auth-creating-users "#scram-sha-256-auth-creating-users")
- [Updating existing users](#scram-sha-256-auth-updating-users "#scram-sha-256-auth-updating-users")
- [Authenticating with SCRAM-SHA-256](#scram-sha-256-auth-authenticating "#scram-sha-256-auth-authenticating")

## Creating users with SCRAM mechanisms

When you create a user, you can specify the SCRAM mechanisms to enable with the `mechanisms` field.
The following examples create users with `SCRAM-SHA-1` only, `SCRAM-SHA-256` only, and both mechanisms:

```
db.runCommand({
    createUser: 'sha1user',
    pwd: passwordPrompt(),
    roles: ['readWrite'],
    mechanisms: ['SCRAM-SHA-1']
});
db.runCommand({
    createUser: 'sha256user',
    pwd: passwordPrompt(),
    roles: ['readWrite'],
    mechanisms: ['SCRAM-SHA-256']
});
db.runCommand({
    createUser: 'bothuser',
    pwd: passwordPrompt(),
    roles: ['readWrite'],
    mechanisms: ['SCRAM-SHA-1','SCRAM-SHA-256']
});
```

### Default mechanisms

If you don't specify the `mechanisms` field, Amazon DocumentDB enables both `SCRAM-SHA-1` and
`SCRAM-SHA-256` for the user. The following two commands are equivalent:

```
db.runCommand({
    createUser: 'user1',
    pwd: passwordPrompt(),
    roles: ['readWrite']
});
// is equivalent to:
db.runCommand({
    createUser: 'user1',
    pwd: passwordPrompt(),
    roles: ['readWrite'],
    mechanisms: ['SCRAM-SHA-1','SCRAM-SHA-256']
});
```

Enabling both mechanisms by default maintains compatibility with older MongoDB drivers that support only
`SCRAM-SHA-1`. Newer drivers and FIPS mode prefer `SCRAM-SHA-256`.
If you don't want any user to authenticate with `SCRAM-SHA-1`, specify only
`SCRAM-SHA-256` in the `mechanisms` field for all of your users.

## Updating existing users

Users created with `SCRAM-SHA-1` continue to be supported with no changes.
To switch an existing user from `SCRAM-SHA-1` to `SCRAM-SHA-256`, update the user with a new
password and the `SCRAM-SHA-256` mechanism:

```
db.runCommand({
    updateUser: 'existing',
    pwd: passwordPrompt(),
    mechanisms: ['SCRAM-SHA-256']
});
```

## Authenticating with SCRAM-SHA-256

Your driver automatically authenticates using the connection string parameters before it sends the first
command on each connection. To select `SCRAM-SHA-256` in a connection URI, set the
`authMechanism` parameter to `SCRAM-SHA-256`:

```
mongodb://username:password@hostname:port/authenticationDatabase?authMechanism=SCRAM-SHA-256
```

You can also send an explicit authentication request from mongosh:

```
db.auth({user: 'sha256user', pwd: passwordPrompt(), mechanism: 'SCRAM-SHA-256'})
Enter password:
1
```

If you don't specify an authentication mechanism in your connection options, the driver automatically
selects a mechanism that the target database user supports.
