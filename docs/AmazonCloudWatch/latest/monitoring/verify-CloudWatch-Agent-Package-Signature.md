

# Verifying the signature of the CloudWatch agent package

Each CloudWatch agent package has a signature file that you can use to verify that the download is original and unmodified. Use the procedure for your operating system that follows.

The signature file link for each package is in the **Signature file link** column of the download table. For more information, see [Download the CloudWatch agent package](download-CloudWatch-Agent-on-EC2-Instance-commandline-first.md).

**To verify the CloudWatch agent package on a Linux server**

1. Download the public key.

   ```
   shell$ wget https://amazoncloudwatch-agent.s3.amazonaws.com/assets/amazon-cloudwatch-agent.gpg
   ```

1. Import the public key into your keyring.

   ```
   shell$  gpg --import amazon-cloudwatch-agent.gpg
   gpg: key 3B789C72: public key "Amazon CloudWatch Agent" imported
   gpg: Total number processed: 1
   gpg: imported: 1 (RSA: 1)
   ```

   Make a note of the key value, as you need it in the next step. In the preceding example, the key value is `3B789C72`.

1. Verify the fingerprint by running the following command, replacing {{key-value}} with the value from the preceding step:

   ```
   shell$  gpg --fingerprint {{key-value}}
   pub   2048R/3B789C72 2017-11-14
         Key fingerprint = 9376 16F3 450B 7D80 6CBD  9725 D581 6730 3B78 9C72
   uid                  Amazon CloudWatch Agent
   ```

   The fingerprint string should be equal to the following:

   `9376 16F3 450B 7D80 6CBD 9725 D581 6730 3B78 9C72`

   If the fingerprint string doesn't match, don't install the agent. Contact Amazon Web Services.

   After you have verified the fingerprint, you can use it to verify the signature of the CloudWatch agent package.

1. Download the package signature file using **wget**. To determine the correct signature file, see the preceding table.

   ```
   wget {{Signature File Link}}
   ```

1. To verify the signature, run **gpg --verify**.

   ```
   shell$ gpg --verify {{signature-filename}} {{agent-download-filename}}
   gpg: Signature made Wed 29 Nov 2017 03:00:59 PM PST using RSA key ID 3B789C72
   gpg: Good signature from "Amazon CloudWatch Agent"
   gpg: WARNING: This key is not certified with a trusted signature!
   gpg:          There is no indication that the signature belongs to the owner.
   Primary key fingerprint: 9376 16F3 450B 7D80 6CBD  9725 D581 6730 3B78 9C72
   ```

   If the output includes the phrase `BAD signature`, check whether you performed the procedure correctly. If you continue to get this response, contact Amazon Web Services and avoid using the downloaded file.

   Note the warning about trust. A key is trusted only if you or someone who you trust has signed it. This doesn't mean that the signature is invalid, only that you have not verified the public key.

**To verify the CloudWatch agent package on a server running Windows Server**

1. Download and install GnuPG for Windows from [https://gnupg.org/download/](https://gnupg.org/download/). When installing, include the **Shell Extension (GpgEx)** option.

   You can perform the remaining steps in Windows PowerShell.

1. Download the public key.

   ```
   PS> Invoke-WebRequest -Uri https://amazoncloudwatch-agent.s3.amazonaws.com/assets/amazon-cloudwatch-agent.gpg -OutFile amazon-cloudwatch-agent.gpg
   ```

1. Import the public key into your keyring.

   ```
   PS>  gpg --import amazon-cloudwatch-agent.gpg
   gpg: key 3B789C72: public key "Amazon CloudWatch Agent" imported
   gpg: Total number processed: 1
   gpg: imported: 1 (RSA: 1)
   ```

   Make a note of the key value because you need it in the next step. In the preceding example, the key value is `3B789C72`.

1. Verify the fingerprint by running the following command, replacing {{key-value}} with the value from the preceding step:

   ```
   PS>  gpg --fingerprint {{key-value}}
   pub   rsa2048 2017-11-14 [SC]
         9376 16F3 450B 7D80 6CBD  9725 D581 6730 3B78 9C72
   uid           [ unknown] Amazon CloudWatch Agent
   ```

   The fingerprint string should be equal to the following:

   `9376 16F3 450B 7D80 6CBD 9725 D581 6730 3B78 9C72`

   If the fingerprint string doesn't match, don't install the agent. Contact Amazon Web Services.

   After you have verified the fingerprint, you can use it to verify the signature of the CloudWatch agent package.

1. Download the package signature file using `Invoke-WebRequest`. To determine the correct signature file, see [CloudWatch Agent Download Links](download-CloudWatch-Agent-on-EC2-Instance-commandline-first.md#agent-download-link-table).

1. To verify the signature, run **gpg --verify**.

   ```
   PS> gpg --verify {{sig-filename}} {{agent-download-filename}}
   gpg: Signature made 11/29/17 23:00:45 Coordinated Universal Time
   gpg:                using RSA key D58167303B789C72
   gpg: Good signature from "Amazon CloudWatch Agent" [unknown]
   gpg: WARNING: This key is not certified with a trusted signature!
   gpg:          There is no indication that the signature belongs to the owner.
   Primary key fingerprint: 9376 16F3 450B 7D80 6CBD  9725 D581 6730 3B78 9C72
   ```

   If the output includes the phrase `BAD signature`, check whether you performed the procedure correctly. If you continue to get this response, contact Amazon Web Services and avoid using the downloaded file.

   Note the warning about trust. A key is trusted only if you or someone who you trust has signed it. This doesn't mean that the signature is invalid, only that you have not verified the public key.

**To verify the CloudWatch agent package on a macOS computer**
+ Use one of the following methods.
  + Check the package signature with **pkgutil**:

    ```
    pkgutil --check-signature amazon-cloudwatch-agent.pkg
    ```

    Confirm that the output shows `Status: signed by a developer certificate issued by Apple for distribution` and that the first certificate in the chain is `Developer ID Installer: AMZN Mobile LLC (94KV3E626L)`.
  + Verify the package with GnuPG and the signature file:

    1. Install GnuPG:

       ```
       brew install gnupg
       ```

    1. Import the public key and verify its fingerprint as described in the Linux procedure.

    1. Download the package signature file with **curl**. To find the signature file link, see [CloudWatch agent download links](download-CloudWatch-Agent-on-EC2-Instance-commandline-first.md#agent-download-link-table).

    1. Verify the signature:

       ```
       gpg --verify {{sig-filename}} {{agent-download-filename}}
       ```

       If the output includes `BAD signature`, don't install the package. The warning that the key isn't certified with a trusted signature is expected if you haven't signed the public key yourself.