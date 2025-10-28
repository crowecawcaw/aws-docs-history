# Store authentication credentials

for SFTP connectors in Secrets Manager

You can use Secrets Manager to store user credentials for your SFTP connectors. When
you create your secret, you must provide a username. Additionally, you can provide
either a password, a private key, or both. For details, see [Quotas for SFTP
connectors](scale-and-limits-sftp-connector.md#limits-sftp-connector "scale-and-limits-sftp-connector.md#limits-sftp-connector").

###### Note

When you store secrets in Secrets Manager, your AWS account incurs charges. For information about
pricing, see [AWS Secrets Manager Pricing](https://aws.amazon.com/secrets-manager/pricing "https://aws.amazon.com/secrets-manager/pricing").

###### To store user credentials in Secrets Manager for an SFTP connector

1.  Sign in to the AWS Management Console and open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2.  In the left navigation pane, choose **Secrets**.
3.  On the **Secrets** page, choose **Store a new
    secret**.
4.  On the **Choose secret type** page, for **Secret
    type**, choose **Other type of secret**.
5.  Provide the key/value information for your secret: you need to provide the
    username, and either a private key or a password.
    1.  In the **Key/value pairs** section, choose the
        **Key/value** tab.
        - **Key** – Enter
          `Username`.
        - **value** – Enter the name of the
          user that is authorized to connect to the partner's
          server.

    2.  If you want to provide a key pair, choose **Add
        row**, and in the **Key/value pairs**
        section, choose the **Key/value** tab.

            * **Key** – Enter
             `PrivateKey`.
            * **value** – paste in your private
             key.

        **Tip**: The private key data that
        you enter must correspond to the public key that is stored for this
        user on the remote SFTP server.

    ###### Note

    It is not possible to use a passphrase-protected private key
    for authentication with an AWS Transfer Family SFTP connector.

    For details on how to generate a public/private key pair, see
    [Creating SSH keys on macOS, Linux, or
    Unix](macOS-linux-unix-ssh.md "macOS-linux-unix-ssh.md"). 3. If you want to provide a password, choose **Add
    row**, and in the **Key/value pairs**
    section, choose the **Key/value** tab.

        * **Key** – Enter
         `Password`.
        * **value** – Enter the password for
         the user.

6.  Choose **Next**.
7.  On the **Configure secret** page, enter a name and
    description for your secret. We recommend that you use a prefix of
    `aws/transfer/` for the name. For example, you
    could name your secret
    `aws/transfer/connector-1`.
8.  Choose **Next**, and then accept the defaults on the
    **Configure rotation** page. Then choose
    **Next**.
9.  On the **Review** page, choose **Store**
    to create and store the secret.
