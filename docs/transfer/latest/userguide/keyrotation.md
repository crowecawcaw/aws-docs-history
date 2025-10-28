# Rotate SSH keys

For security, we recommend the best practice of rotating your SSH keys. Usually, this
rotation is specified as a part of a security policy and is implemented in some
automated fashion. Depending upon the level of security, for a highly sensitive
communication, an SSH key pair might be used only once. Doing this eliminates any risk
due to stored keys. However, it is much more common to store SSH credentials for a
period of time and set an interval that doesn't place undue burden on users. A time
interval of three months is common.

###### Note

For automated SSH key rotation using infrastructure as code, see [Transfer Family Terraform modules](terraform.md "terraform.md").

There are two methods used to perform SSH key rotation:

- On the console, you can upload a new SSH public key and delete an existing SSH
  public key.
- Using the API, you can update existing users by using the [DeleteSshPublicKey](../APIReference/API_DeleteSshPublicKey.md "../APIReference/API_DeleteSshPublicKey.md") API to delete a user's Secure Shell (SSH) public
  key and the [ImportSshPublicKey](../APIReference/API_ImportSshPublicKey.md "../APIReference/API_ImportSshPublicKey.md") API to add a new Secure Shell (SSH) public key
  to the user's account.

Console

###### To perform a key rotation in the console

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. Navigate to the **Servers** page.
3. Choose the identifier in the **Server ID** column
   to see the **Server details** page.
4. Under **Users**, select the check box of the user
   whose SSH public key that you want to rotate, then choose
   **Actions**, and then choose **Add
   key** to see the **Add key**
   page.

or

Choose the username to see the **User details**
page, and then choose **Add SSH public key** to see
the **Add key** page. 5. Enter the new SSH public key and choose **Add
key**.

###### Important

The format of the SSH public key depends on the type of key
you generated.

    * For RSA keys, the format is `ssh-rsa
     `string``.
    * For ED25519 keys, the format is `ssh-ed25519
     `string``.
    * For ECDSA keys, the key begins with
     `ecdsa-sha2-nistp256`,
     `ecdsa-sha2-nistp384`, or
     `ecdsa-sha2-nistp521`, depending on the
     size of the key you generated. The beginning string is
     then followed by
     ``string``,
     similar to the other key types.

You are returned to the **User details** page,
and the new SSH public key that you just entered appears in the
**SSH public keys** section. 6. Select the check box of the old you key that you want to delete
and then choose **Delete**. 7. Confirm the deletion operation by entering the word
`delete`, and then choose
**Delete**.

API

###### To perform a key rotation using the API

1. On macOS, Linux, or Unix operating systems, open a command
   terminal.
2. Retrieve the SSH key that you want to delete by entering the
   following command. To use this command, replace
   `serverID` with the
   server ID for your Transfer Family server, and replace
   `username` with your
   username.

```
aws transfer describe-user --server-id='`serverID`' --user-name='`username`'
```

The command returns details about the user. Copy the contents of
the `"SshPublicKeyId":` field. You will need to enter
this value later in this procedure.

```
"SshPublicKeys": [ { "SshPublicKeyBody": "`public-key`", "SshPublicKeyId": "`keyID`",
   "DateImported": 1621969331.072 } ],
```

3. Next, import a new SSH key for your user. At the prompt, enter
   the following command. To use this command, replace
   `serverID` with the
   server ID for your Transfer Family server, replace
   `username` with your
   username, and replace
   `public-key` with the
   fingerprint of your new public key.

```
aws transfer import-ssh-public-key --server-id='`serverID`' --user-name='`username`'
   --ssh-public-key-body='`public-key`'
```

If the command is successful, no output is returned. 4. Finally, delete the old key by running the following command. To
use this command, replace
`serverID` with the server
ID for your Transfer Family server, replace
`username` with your
username, and replace
`keyID-from-step-2`
with the key ID value that you copied in step 2 of this procedure

```
aws transfer delete-ssh-public-key --server-id='`serverID`' --user-name='`username`'
   --ssh-public-key-id='`keyID-from-step-2`'
```

5. (Optional) To confirm that the old key no longer exists, repeat
   step 2.
