# Setting up a managed workflow for decrypting a

file

This tutorial illustrates how to set up a managed workflow that contains a decrypt step.
The tutorial also shows how to upload an encrypted file to an Amazon S3 bucket and then view the
decrypted file in that same bucket.

###### Note

The AWS storage blog has a post that describes how to simply decrypt files without writing any code using Transfer Family Managed workflows,
[Encrypt and decrypt files with PGP and AWS Transfer Family](https://aws.amazon.com/blogs/storage/encrypt-and-decrypt-files-with-pgp-and-aws-transfer-family/ "https://aws.amazon.com/blogs/storage/encrypt-and-decrypt-files-with-pgp-and-aws-transfer-family/").

###### Topics

- [Step 1: Configure an execution
  role](#create-example-execution-role "#create-example-execution-role")
- [Step 2: Create a managed workflow](#create-example-workflow "#create-example-workflow")
- [Step 3: Add the workflow to a server and create
  a user](#add-workflow-to-server "#add-workflow-to-server")
- [Step 4: Create a PGP key pair](#create-example-pgp-key-pair "#create-example-pgp-key-pair")
- [Step 5: Store the PGP private key in
  AWS Secrets Manager](#output-private-key-to-secrets "#output-private-key-to-secrets")
- [Step 6: Encrypt a file](#encrypt-example-file "#encrypt-example-file")
- [Step 7: Run the workflow and view the
  results](#test-decrypt-workflow "#test-decrypt-workflow")

## Step 1: Configure an execution

role

Create an AWS Identity and Access Management (IAM) execution role that Transfer Family can use to launch a workflow. The
process of creating an execution role is described in [IAM policies for workflows](workflow-execution-role.md "workflow-execution-role.md").

###### Note

As part of creating an execution role, make sure to establish a trust relationship
between the execution role and Transfer Family, as described in [To establish a trust relationship](requirements-roles.md#establish-trust-transfer "requirements-roles.md#establish-trust-transfer").

The following execution role policy contains all the required permissions to start the
workflow that you create in this tutorial. To use this example policy, replace the
`user input placeholders` with your own
information. Replace `amzn-s3-demo-bucket` with the name of the Amazon S3 bucket
where you upload your encrypted files.

###### Note

Not every workflow requires every permission that's listed in this example. You
can restrict permissions based on the types of steps in your specific workflow. The
permissions needed for each predefined step type are described in [Use predefined steps](nominal-steps-workflow.md "nominal-steps-workflow.md"). The
permissions needed for a custom step are described in [IAM permissions for a custom step](custom-step-details.md#custom-step-iam "custom-step-details.md#custom-step-iam").

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "WorkflowsS3Permissions",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectTagging",
 "s3:GetObjectVersion",
 "s3:PutObject",
 "s3:PutObjectTagging",
 "s3:ListBucket",
 "s3:PutObjectTagging",
 "s3:PutObjectVersionTagging",
 "s3:DeleteObjectVersion",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket/*",
 "arn:aws:s3:::amzn-s3-demo-bucket"
 ]
 },
 {
 "Sid": "DecryptSecret",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:aws/transfer/*"
 }
 ]
}`

```

## Step 2: Create a managed workflow

Now you need to create a workflow that contains a decrypt step.

###### To create a workflow that contains a decrypt step

1.  Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2.  In the left navigation pane, choose **Workflows**, and then
    choose **Create workflow**.
3.  Enter the following details:
    - Enter a description, for example `Decrypt workflow
example`.
    - In the **Nominal steps** section, choose
      **Add step**.

4.  For **Choose step type**, choose **Decrypt
    file**, and then choose **Next**.
5.  In the **Configure parameters** dialog box, specify the
    following:

        * Enter a descriptive step name, for example,
         `decrypt-step`. Spaces are not allowed in step
         names.
        * For the **Destination for decrypted files**, choose
         Amazon S3.
        * For the **Destination bucket name**, choose the same
         Amazon S3 bucket that you specified as the `amzn-s3-demo-bucket`
         in the IAM policy that you created in Step 1.
        * For the **Destination key prefix**, enter the name of
         the prefix (folder) where you want to store your decrypted files in your
         destination bucket, for example,
         `decrypted-files/`.


        ###### Note

        Make sure to add a trailing slash (`/`) to
         your prefix.
        * For this tutorial, leave **Overwrite existing**
         cleared. When this setting is cleared, if you try to decrypt a file with
         the identical name of an existing file, the workflow processing stops,
         and the new file is not processed.

    Choose **Next** to move to the review screen.

6.  Review the details for the step. If everything is correct, choose
    **Create step**.
7.  Your workflow needs only the single decrypt step, so there are no additional
    steps to configure. Choose **Create workflow** to create the
    new workflow.

Note the workflow ID for your new workflow. You will need this ID for the next step.
This tutorial uses `w-1234abcd5678efghi` as the
example workflow ID.

## Step 3: Add the workflow to a server and create

a user

Now that you have a workflow with a decrypt step, you must associate it with a Transfer Family
server. This tutorial shows how to attach the workflow to an existing Transfer Family server.
Alternatively, you can create a new server to use with your workflow.

After you attach the workflow to a server, you must create a user that can SFTP into
the server and trigger the workflow to run.

###### To configure a Transfer Family server to run a workflow

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. In the left navigation pane, choose **Servers**, and then
   choose a server from the list. Make sure that this server supports the SFTP
   protocol.
3. On the details page for the server, scroll down to the **Additional
   details** section, and then choose **Edit**.
4. On the **Edit additional details** page, in the
   **Managed workflows** section, choose your workflow, and
   choose a corresponding execution role.
   - For **Workflow for complete file uploads**, choose
     the workflow that you created in [Step 2: Create a managed workflow](#create-example-workflow "#create-example-workflow"), for example,
     `w-1234abcd5678efghi`.
   - For **Managed workflows execution role**, choose the
     IAM role that you created in [Step 1: Configure an execution
     role](#create-example-execution-role "#create-example-execution-role").

5. Scroll to the bottom of the page, and choose **Save** to save
   your changes.

Note the ID for the server that you are using. The name of the AWS Secrets Manager secret that
you use to store your PGP keys is based in part on the server ID.

###### To add a user that can trigger the workflow

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. In the left navigation pane, choose **Servers**, and then
   choose the server that you're using for the decrypt workflow.
3. On the server details page, scroll down to the **Users**
   section, and choose **Add user**.
4. For your new user, enter the following details:
   - For **Username**, enter
     `decrypt-user`.
   - For **Role**, choose a user role that can access your
     server.
   - For **Home directory**, choose the Amazon S3 bucket that
     you used earlier, for example, `amzn-s3-demo-bucket`.
   - For **SSH public keys**, paste in a public key that
     corresponds to a private key that you have. For details, see [Generate SSH keys for service-managed users](sshkeygen.md "sshkeygen.md").

5. Choose **Add** to save your new user.

Note the name of your Transfer Family user for this server. The secret is partially based on the
name of the user. For simplicity, this tutorial uses a default secret that can be used
by any user of the server.

## Step 4: Create a PGP key pair

Use one of the [supported PGP clients](pgp-key-clients.md "pgp-key-clients.md") to
generate a PGP key pair. This process is described in detail in [Generate PGP keys](generate-pgp-keys.md "generate-pgp-keys.md").

###### To generate a PGP key pair

1. For this tutorial, you can use `gpg` (`GnuPG`) version
   2.0.22 client to generate a PGP key pair that uses RSA as the encryption
   algorithm. For this client, run the following command, and provide an email
   address and a passphrase. You can use any name or email address that you like.
   Make sure that you remember the values that you use, because you will need to
   enter them later in the tutorial.

```
gpg --gen-key
```

###### Note

If you're using `GnuPG` version 2.3.0 or newer, you
must run `gpg --full-gen-key`. When prompted for the type of key
to create, choose RSA or ECC. However, if you choose ECC, make sure to choose either
NIST or BrainPool for the elliptic curve.
**Do not** choose Curve 25519. 2. Export the private key by running the following command. Replace
`user@example.com` with the email
address that you used when you generated the key.

```
gpg --output workflow-tutorial-key.pgp --armor --export-secret-key `user@example.com`
```

This command exports the private key to the
`workflow-tutorial-key.pgp` file. You can name the
output file anything that you like. You can also delete the private key file
after you have added it to AWS Secrets Manager.

## Step 5: Store the PGP private key in

AWS Secrets Manager

You need to store the private key in Secrets Manager, in a very specific way, so that the
workflow can find the private key when the workflow runs a decrypt step on an uploaded
file.

###### Note

When you store secrets in Secrets Manager, your AWS account incurs charges. For information about
pricing, see [AWS Secrets Manager Pricing](https://aws.amazon.com/secrets-manager/pricing "https://aws.amazon.com/secrets-manager/pricing").

###### To store a PGP private key in Secrets Manager

1. Sign in to the AWS Management Console and open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. In the left navigation pane, choose **Secrets**.
3. On the **Secrets** page, choose **Store a new
   secret**.
4. On the **Choose secret type** page, for **Secret
   type**, choose **Other type of secret**.
5. In the **Key/value pairs** section, choose the
   **Key/value** tab.
   - **Key** – Enter
     `PGPPrivateKey`.
   - **value** – Paste the text of your private key
     into the value field.

6. Choose **Add row**, and in the **Key/value
   pairs** section, choose the **Key/value**
   tab.
   - **Key** – Enter
     `PGPPassphrase`.
   - **value** – Enter the passphrase that you used
     when you generated your PGP key pair in [Step 4: Create a PGP key pair](#create-example-pgp-key-pair "#create-example-pgp-key-pair").

7. Choose **Next**.
8. On the **Configure secret** page, enter a name and
   description for your secret. You can create a secret for a specific user or one
   that can be used by all users. If your server ID is
   `s-11112222333344445`, you name
   the secret as follows.
   - To create a default secret for all users, name the secret
     `aws/transfer/`s-11112222333344445`/@pgp-default`.
   - To create a secret only for the user that you created earlier, name
     the secret
     `aws/transfer/`s-11112222333344445`/decrypt-user`.

9. Choose **Next**, and then accept the defaults on the
   **Configure rotation** page. Then choose
   **Next**.
10. On the **Review** page, choose **Store** to
    create and store the secret.

For more information about adding your PGP private key to Secrets Manager, see [Use AWS Secrets Manager to store your PGP key](manage-pgp-keys.md#store-pgp-key-details "manage-pgp-keys.md#store-pgp-key-details").

## Step 6: Encrypt a file

Use the `gpg` program to encrypt a file for use in your workflow. Run the
following command to encrypt a file:

```
gpg -e -r `marymajor@example.com` --openpgp testfile.txt
```

Before running this command, note the following:

- For the `-r` argument, replace
  `marymajor@example.com` with the
  email address that you used when you created the PGP key pair.
- The `--openpgp` flag is optional. This flag makes the encrypted
  file conform to the [OpenPGP
  RFC4880](https://www.rfc-editor.org/rfc/rfc4880 "https://www.rfc-editor.org/rfc/rfc4880") standard.
- This command creates a file named `testfile.txt.gpg` in
  the same location as `testfile.txt`.

###### Important

When encrypting files for use with AWS Transfer Family workflows, always ensure you specify a
non-anonymous recipient using the `-r` parameter. Anonymous encryption
(without specifying a recipient) can cause decryption failures in the workflow
because the system won't be able to identify which key to use for decryption.
Debugging information for this issue is available at [Troubleshoot anonymous recipient
encryption issues](workflow-issues.md#workflows-decrypt-anonymous "workflow-issues.md#workflows-decrypt-anonymous").

## Step 7: Run the workflow and view the

results

To run the workflow, you connect to the Transfer Family server with the user that you created in
Step 3. Then you can look in the Amazon S3 bucket that you specified in [Step 2.5, configure destination
parameters](#configure-destination-details "#configure-destination-details") to see the decrypted file.

###### To run the decrypt workflow

1. Open a command terminal.
2. Run the following command, replacing
   `your-endpoint` with your actual
   endpoint, and `transfer-key` with your
   user's SSH private key:

```
sftp -i `transfer-key` decrypt-user@`your-endpoint`
```

For example, if the private key is stored in `~/.ssh/decrypt-user`,
and your endpoint is
`s-11112222333344445.server.transfer.us-east-2.amazonaws.com`,
the command is as follows:

```
sftp -i  ~/.ssh/decrypt-user decrypt-user@s-11112222333344445.server.transfer.us-east-2.amazonaws.com
```

3. Run the `pwd` command. If successful, this command will return the
   following:

```
Remote working directory: /`amzn-s3-demo-bucket`/decrypt-user
```

Your directory reflects the name of your Amazon S3 bucket. 4. Run the following command to upload the file and trigger the workflow to
run:

```
put testfile.txt.gpg
```

5. For the destination of the decrypted files, you specified the
   `decrypted-files/` folder when you created the workflow. Now, you
   can navigate to that folder and list the contents.

```
cd ../decrypted-files/
ls
```

If successful, the `ls` command lists the
`testfile.txt` file. You can download this file and
verify that it is the same as the original file that you encrypted
earlier.
