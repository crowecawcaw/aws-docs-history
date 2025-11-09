# Step 2 – Install the AWS PCS

agent

Install the agent that configures the instances launched by AWS PCS for use with
Slurm. For more information about the AWS PCS agent, see [AWS PCS agent versions](pcs-agent-versions.md "pcs-agent-versions.md").

###### To install the AWS PCS agent

1. Connect to the instance you launched. For more information, see Connect to your Linux
   instance.
2. (Optional) To ensure that all of your software packages are up to date, perform a quick
   software update on your instance. This process may take a few minutes.
   - Amazon Linux 2, Amazon Linux 2023, RHEL 9, RHEL 8, Rocky Linux 9, and Rocky Linux 8

   ```
   sudo yum update -y
   ```

   - Ubuntu 22.04 and Ubuntu 24.04

   ```
   sudo apt-get update && sudo apt-get upgrade -y
   ```

3. Reboot the instance and reconnect to it.
4. Download the AWS PCS agent installation files. The installation files are packaged
   into a compressed tarball (`.tar.gz`) file. To download the latest
   _stable_ version, use the following command. Substitute
   `region` with the AWS Region where you launched your temporary
   instance, such as `us-east-1`.

```
curl https://aws-pcs-repo-`region`.s3.`region`.amazonaws.com/aws-pcs-agent/aws-pcs-agent-v1.3.1-1.tar.gz -o aws-pcs-agent-v1.3.1-1.tar.gz
```

You can also get the latest version by replacing the version number with
`latest` in the preceding command (for example:
`aws-pcs-agent-v1-latest.tar.gz`).

###### Note

This might change in future releases of the AWS PCS agent software. 5. (Optional) Verify the authenticity and integrity of the AWS PCS software tarball. We
recommend that you do this to verify the identity of the software publisher and to check that
the file has not been altered or corrupted since it was published.

    1. Download the public GPG key for AWS PCS and import it into your keyring. Substitute
     `region` with the AWS Region where you launched your temporary
     instance. The command should return a key value. Record the key value; you use it in the next
     step.



    ```
    wget https://aws-pcs-repo-public-keys-`region`.s3.`region`.amazonaws.com/aws-pcs-public-key.pub && \
        gpg --import aws-pcs-public-key.pub
    ```
    2. Run the following command to verify the GPG key's fingerprint.



    ```
    gpg --fingerprint 7EEF030EDDF5C21C
    ```

    The command should return a fingerprint that is identical to the following:



    ```
    1C24 32C1 862F 64D1 F90A  239A 7EEF 030E DDF5 C21C
    ```

    ###### Important

    Don't run the AWS PCS agent installation script if the fingerprint doesn't match. Contact [AWS Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").
    3. Download the signature file and verify the signature of the AWS PCS software tarball
     file. Replace `region` with the AWS Region where you launched your
     temporary instance, such as `us-east-1`.



    ```
    wget https://aws-pcs-repo-`region`.s3.`region`.amazonaws.com/aws-pcs-agent/aws-pcs-agent-v1.3.1-1.tar.gz.sig && \
        gpg --verify ./aws-pcs-agent-v1.3.1-1.tar.gz.sig
    ```

    The output should be similar to the following:



    ```
    gpg: assuming signed data in './aws-pcs-agent-v1.3.1-1.tar.gz'
    gpg: Signature made Thu 06 Nov 2025 11:10:36 AM CET using RSA key ID ECC0AE5C
    gpg: Good signature from "AWS PCS Packages (AWS PCS Packages)"
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.
    Primary key fingerprint: 1C24 32C1 862F 64D1 F90A  239A 7EEF 030E DDF5 C21C
       Subkey fingerprint: B7E1 8788 3517 6A74 C3D5  EAF5 6088 136D ECC0 AE5C
    ```

    If the result includes `Good signature` and the fingerprint matches the
     fingerprint returned in the previous step, proceed to the next step.


    ###### Important

    Don't run the AWS PCS software installation script if the fingerprint doesn't
     match. Contact [AWS Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").

6. Extract the files from the compressed `.tar.gz` file and navigate to the
   extracted directory.

```
tar -xf aws-pcs-agent-v1.3.1-1.tar.gz && \
    cd aws-pcs-agent
```

7. Install the AWS PCS software.

```
sudo ./installer.sh
```

8. Check the AWS PCS software version file to confirm a successful installation.

```
cat /opt/aws/pcs/version
```

The output should be similar to the following:

```
AGENT_INSTALL_DATE='Fri Dec 13 12:28:43 UTC 2024'
AGENT_VERSION='1.3.1'
AGENT_RELEASE='1'
```
