# Step 3 – Install Slurm

Install a version of Slurm that is compatible with AWS PCS.
For more information, see [Slurm versions in AWS PCS](slurm-versions.md "slurm-versions.md").

###### Note

If you have an AMI with a previous version of the Slurm software installed on it,
you must perform the following steps to install the new version of Slurm.
The AWS PCS agent enables the correct version of the Slurm binaries at runtime,
according to the Slurm version configured at cluster creation time.

###### To install Slurm

1. Connect to the same temporary instance where you installed the AWS PCS software.
2. Download the Slurm installer software. The Slurm installer is packaged into a compressed
   tarball (`.tar.gz`) file. To download the latest _stable_
   version, use the following command. Substitute `region` with the
   AWS Region of your temporary instance, such as `us-east-1`.

```
curl https://aws-pcs-repo-`region`.s3.`region`.amazonaws.com/aws-pcs-slurm/aws-pcs-slurm-25.05-installer-25.05.5-1.tar.gz \
     -o aws-pcs-slurm-25.05-installer-25.05.5-1.tar.gz
```

You can also get the latest version by replacing the version number with
`latest` in the preceding command (for example:
`aws-pcs-slurm-25.05-installer-latest.tar.gz`). For a complete list of available versions with checksums, see [Slurm versions in AWS PCS](slurm-versions.md "slurm-versions.md").

###### Note

This might change in future releases of the Slurm installer software. 3. (Optional) Verify the authenticity and integrity of the Slurm installer tarball. We
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

    Don't run the Slurm installation script if the fingerprint doesn't match. Contact [AWS Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").
    3. Download the signature file and verify the signature of the Slurm installer tarball
     file. Replace `region` with the AWS Region where you launched your
     temporary instance, such as `us-east-1`.



    ```
    wget https://aws-pcs-repo-`region`.s3.`region`.amazonaws.com/aws-pcs-slurm/aws-pcs-slurm-25.05-installer-25.05.5-1.tar.gz.sig && \
         gpg --verify ./aws-pcs-slurm-25.05-installer-25.05.5-1.tar.gz.sig
    ```

    The output should be similar to the following:



    ```
    gpg: assuming signed data in './aws-pcs-slurm-25.05-installer-25.05.5-1.tar.gz'
    gpg: Signature made Fri 14 Nov 2025 11:35:15 AM UTC using RSA key ID ECC0AE5C
    gpg: Good signature from "AWS PCS Packages (AWS PCS Packages)"
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.
    Primary key fingerprint: 1C24 32C1 862F 64D1 F90A  239A 7EEF 030E DDF5 C21C
         Subkey fingerprint: B7E1 8788 3517 6A74 C3D5  EAF5 6088 136D ECC0 AE5C
    ```

    If the result includes `Good signature` and the fingerprint matches the
     fingerprint returned in the previous step, proceed to the next step.


    ###### Important

    Don't run the Slurm installation script if the fingerprint doesn't match. Contact
     [AWS Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").

4. Extract the files from the compressed `.tar.gz` file and navigate into the
   extracted directory.

```
tar -xf aws-pcs-slurm-25.05-installer-25.05.5-1.tar.gz && \
    cd aws-pcs-slurm-25.05-installer
```

5. Install Slurm. The installer downloads, compiles, and installs Slurm and its dependencies.
   It takes several minutes, depending on the specifications of the temporary instance you
   selected.

```
sudo ./installer.sh -y
```

6. Check the scheduler version file to confirm the installation.

```
cat /opt/aws/pcs/scheduler/slurm-25.05/version
```

The output should be similar to the following:

```
SLURM_INSTALL_DATE='Fri Nov 14 15:15:37 UTC 2025'
SLURM_VERSION='25.05.5'
PCS_SLURM_RELEASE='1'
```
