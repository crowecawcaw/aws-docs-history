# Manage PGP keys

To manage your PGP keys, use AWS Secrets Manager.

###### Note

Your secret name includes your Transfer Family server ID. This means you should have already
identified or created a server _before_ you can store your PGP
key information in AWS Secrets Manager.

If you want to use one key and passphrase for all of your users, you can store the PGP
key block information under the secret name
`aws/transfer/`server-id`/@pgp-default`,
where `server-id` is the ID for your Transfer Family server.
Transfer Family uses this default key if there is no key where the
`user-name` matches the user that's
executing the workflow.

You can create a key for a specific user. In this case, the format for the secret name
is
`aws/transfer/`server-id`/`user-name`,
 where `user-name`` matches the user that's running
the workflow for a Transfer Family server.

###### Note

You can store a maximum of 3 PGP private keys, per Transfer Family server, per user.

###### To configure PGP keys for use with decryption

1. Depending on the version of GPG that you are using, run one of the following
   commands to generate a PGP key pair that doesn't use a Curve 25519 encryption
   algorithm.
   - If you are using `GnuPG` version 2.3.0 or newer,
     run the following command:

   ```
   gpg --full-gen-key
   ```

   You can choose `RSA`, or, if you choose
   `ECC`, you can choose either
   `NIST` or `BrainPool` for
   the elliptic curve. If you run `gpg --gen-key` instead, you
   create a key pair that uses the ECC Curve 25519 encryption algorithm,
   which we don't currently support for PGP keys.
   - For versions of `GnuPG` prior to 2.3.0, you can
     use the following command, since RSA is the default encryption
     type.

   ```
   gpg --gen-key
   ```

###### Important

During the key-generation process, you must provide a passphrase and an
email address. Make sure to take note of these values. You must provide the
passphrase when you enter the key's details into AWS Secrets Manager later in this
procedure. And you must provide the same email address to export the private
key in the next step. 2. Run the following command to export the private key. To use this command,
replace `private.pgp` with the name of the
file in which to save the private key block, and
`marymajor@example.com` with the
email address that you used when you generated the key pair.

```
gpg --output `private.pgp` --armor --export-secret-key `marymajor@example.com`
```

3.  Use AWS Secrets Manager to store your PGP key.

        1. Sign in to the AWS Management Console and open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
        2. In the left navigation pane, choose **Secrets**.
        3. On the **Secrets** page, choose **Store a new
         secret**.
        4. On the **Choose secret type** page, for
         **Secret type**, select **Other type of
         secret**.
        5. In the **Key/value pairs** section, choose the
         **Key/value** tab.




        	* **Key** – Enter
        	 `PGPPrivateKey`.


        	###### Note

        	You must enter the `PGPPrivateKey`
        	 string exactly: do not add any spaces before or between
        	 characters.
        	* **value** – Paste the text of your
        	 private key into the value field. You can find the text of your
        	 private key in the file (for example,
        	 `private.pgp`) that you specified when
        	 you exported your key earlier in this procedure. The key begins
        	 with `-----BEGIN PGP PRIVATE KEY BLOCK-----` and ends
        	 with `-----END PGP PRIVATE KEY BLOCK-----`.


        	###### Note

        	Make sure that the text block contains only the private
        	 key and does not contain the public key as well.
        6. Select **Add row** and in the **Key/value
         pairs** section, choose the **Key/value**
         tab.




        	* **Key** – Enter
        	 `PGPPassphrase`.


        	###### Note

        	You must enter the `PGPPassphrase`
        	 string exactly: do not add any spaces before or between
        	 characters.
        	* **value** – Enter the passphrase you
        	 used when you generated your PGP key pair.

        ![The AWS Secrets Manager console, showing the keys and values that you enter to manage your PGP keys.](images/pgp-secrets-01.png)

        ###### Note

        You can add up to 3 sets of keys and passphrases. To add a second
         set, add two new rows, and enter
         `PGPPrivateKey2` and
         `PGPPassphrase2` for the keys, and paste in
         another private key and passphrase. To add a third set, key values
         must be `PGPPrivateKey3` and
         `PGPPassphrase3`.
        7. Choose **Next**.
        8. On the **Configure secret** page, enter a name and
         description for your secret.




        	* If you're creating a default key, that is, a key that can be
        	 used by any Transfer Family user, enter
        	 `aws/transfer/`server-id`/@pgp-default`.
        	 Replace ``server-id`` with
        	 the ID of the server that contains the workflow that has a
        	 decrypt step.
        	* If you're creating a key to be used by a specific Transfer Family user,
        	 enter
        	 `aws/transfer/`server-id`/`user-name``.
        	 Replace ``server-id`` with
        	 the ID of the server that contains the workflow that has a
        	 decrypt step, and replace
        	 ``user-name`` with
        	 the name of the user that's running the workflow. The
        	 ``user-name`` is
        	 stored in the identity provider that the Transfer Family server is
        	 using.
        9. Choose **Next** and accept the defaults on the
         **Configure rotation** page. Then choose
         **Next**.
        10. On the **Review** page, choose
         **Store** to create and store the secret.

    The following screenshot shows the details for the user
    `marymajor` for a specific Transfer Family server. This example shows
    three keys and their corresponding passphrases.

![The AWS Secrets Manager console, showing the secret details page with three keys and passphrases for a Transfer Family server and user.](images/pgp-secrets-02.png)
