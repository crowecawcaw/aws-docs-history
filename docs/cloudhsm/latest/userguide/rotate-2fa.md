# Manage 2FA for HSM users using AWS CloudHSM Management Utility

Use **changePswd** in AWS CloudHSM Management Utility (CMU) to modify two-factor
authentication (2FA) for a user. Each time you enable 2FA, you must provide a public key for 2FA
logins.

**changePswd** performs any of the following scenarios:

- Change the password for a 2FA user
- Change the password for a non-2FA user
- Add 2FA to a non-2FA user
- Remove 2FA from a 2FA user
- Rotate the key for a 2FA user
  You can also combine tasks. For example, you can remove 2FA from a user and change the
  password at the same time, or you might rotate the 2FA key and change the user password.

###### To change passwords or rotate keys for CO users with 2FA enabled

1. Use CMU to log in to the HSM as a CO with 2FA enabled.
2. Use **changePswd** to change the password or rotate the key from CO users
   with 2FA enabled. Use the `-2fa` parameter and include a location in the file
   system for the system to write the `authdata` file. This file includes a
   digest for each HSM in the cluster.

```
`aws-cloudhsm >` **changePswd** CO example-user `<new-password>` -2fa `/path/to/`authdata``
```

CMU prompts you to use the private key to sign the digests in the
`authdata` file and return the signatures with the public key. 3. Use the private key to sign the digests in the `authdata` file, add
the signatures and the public key to the JSON formatted `authdata` file and
then provide CMU with the location of the `authdata` file. For more
information, see [Configuration reference for 2FA with AWS CloudHSM Management Utility](reference-2fa.md "reference-2fa.md").

###### Note

The cluster uses the same key for quorum authentication and 2FA. If you are using quorum
authentication or plan to use quorum authentication, see [Quorum authentication and 2FA in AWS CloudHSM clusters using AWS CloudHSM
Management Utility](quorum-2fa.md "quorum-2fa.md").
