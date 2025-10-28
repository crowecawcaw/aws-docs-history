# Storing an encryption or decryption passphrase

There are encryption scenarios in AWS Elemental MediaLive that require you to store the passphrase for
an encryption key in a _secret_ in AWS Secrets Manager. For example:

- If you create an SRT output group in an AWS Elemental MediaLive channel, you must encrypt the
  output to protect it on transit to the downstream system (the system that you are
  sharing the output with). You must store the encryption passphrase as a
  _secret_. For more information about creating an SRT output
  group and how to use the passphrase, see [Creating an SRT caller output group](opg-srt-caller.md "opg-srt-caller.md").
- You might create an SRT input to ingest a source that the upstream system has
  encrypted. In this case, you must obtain the encryption passphrase from the upstream
  system (the system that is sharing the source with you). You must store that
  passphrase as a _secret_. For more information about creating an
  SRT input group and how to use the passphrase, see [Setting up an
  SRT input](input-caller-srt.md "input-caller-srt.md").
  **Supported encryption algorithms**

MediaLive supports symmetric AES 128, AES 192, or AES 256 encryption.

**Passphrases**

A passphrase is a text string that is used to generate and protect an encryption key. With
the types of encryption scenarios described above, you and the other party (the sender or
receiver of the content) must agree on a passphrase that you will each use to encrypt and
decrypt the content. You must store the passphrase as a value in a secret in Secrets Manager. You must
give the MediaLive trusted entity (for example, MediaLiveAccessRole) permission to obtain the
value in the secret.

You must configure the input or output group with the ARN of the secret.

When the MediaLive channel is running and MediaLive needs to encrypt or decrypt content, it
requests the passphrase from Secrets Manager, and uses that passphrase in the decrypt or encrypt
algorithm.

###### Topics

- [Step 1: Agree on the passphrase](#encryption-secret-create-passphrase "#encryption-secret-create-passphrase")
- [Step 2: Store your encryption
  passphrase in AWS Secrets Manager](#encryption-secret-create-passphrase-store "#encryption-secret-create-passphrase-store")
- [Step 3: Update the trusted entity](#encryption-secret-trusted-entity "#encryption-secret-trusted-entity")

## Step 1: Agree on the passphrase

When you use Secrets Manager to encrypt data, there are two pieces of data:

- The encryption passphrase. You and the operator of the upstream or downstream
  system must agree on the encryption passphrase.

We recommend that the encryption passphrase follows these rules:

    + Minimum passphrase length of 10 characters and a maximum length of 80
     characters.
    + Minimum of three of the following mix of character types:


    uppercase, lowercase, numbers, and `! @ # $ % ^ & * ( )
     _ + - = [ ] { } | '`
    + Don't use your AWS account name or email address in the
     passphrase

- The name for the _secret_ that holds the
  passphrase. This can be any name, but it should be descriptive because your
  organization might store a lot of secrets. For example,
  `2018-12-01_baseball-game-source`.

## Step 2: Store your encryption

passphrase in AWS Secrets Manager

You must store the encryption passphrase in your account. The other party stores the
passphrase as appropriate. Here are the possibilities:

- If you and the other party are the same AWS account, one of you can store
  the passphrase in a secret. That person then gives the ARN of the secret to the
  other person.
- If the other party is an AWS customer with a different account, they
  typically also store the passphrase in their own secret in Secrets Manager. You share the
  passphrase but you don't share the secret.
- If the other party isn't an AWS customer, they should store the passphrase
  according to their organization's policies.

To store the passphrase, follow these steps.

1. Sign in to the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. On the **Secrets** page, choose **Store a new
   secret**. The first page of the **Secrets** wizard
   appears.
3. Complete the fields, which appear over several pages:
   - **Select secret type**: Choose **Other type
     of secrets**.
   - **Key/value pairs**:Choose
     **Plaintext**. Clear any text in the box. Type in
     the passphrase.
   - **Encryption key**: Choose the encryption key that
     Secrets Manager will use to encrypt the passphrase in the secret. We recommend
     that you use default encryption
     key(**aws/secretsmanager**).
   - **Secret name**: Enter a name for the secret.
     Keep in mind that your organization might store a lot of secrets, so the name should be descriptive. For
     example, `2018-12-01_baseball-game-source`.
   - **Configure automatic rotation**: Complete as
     appropriate. Your organization might have a policy of rotating secrets.
     If not, leave rotation off. For more information, select the
     **Info** link.

4. Choose **Next** and then choose **Store**.
5. On the next screen, select the name of the secret you created. Details about
   the secret appear.
6. Make a note of the name and the ARN of the secret.

## Step 3: Update the trusted entity

MediaLive needs permission to read the value of the secret you created. You might need to
update the trusted entity to include that permission. These possibilities exist:

- If you use the **MediaLiveAccessRole** trusted entity with
  the channel that includes encrypted content, no action is required. This entity
  already has the required permission.
- If you use a custom trusted entity with the channel, you must update it to
  include the required permissions. See the information about Secrets Manager in [Access requirements for the trusted entity](trusted-entity-requirements.md "trusted-entity-requirements.md").
