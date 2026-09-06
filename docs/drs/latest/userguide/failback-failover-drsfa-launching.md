

# Installing the DRSFA Client
<a name="failback-failover-drsfa-launching"></a>

Installing the DRSFA client is a one-time operation.

The DRSFA client is supported on Ubuntu 22.04, 24.04, and 26.04. Launch an Ubuntu 22.04, 24.04, or 26.04 x86\_64 instance in EC2 or use a public ISO to run the client locally in your vCenter environment. Follow the [Create your EC2 resources and launch your EC2 instance](https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html) guidelines in the EC2 documentation.

After your instance is ready, connect to it and download the DRSFA client installer:

```
wget https://drsfa-us-west-2.s3.us-west-2.amazonaws.com/drs_failback_automation_installer.sh
```

**Note**  
Verify the hash of the installer: `https://drsfa-hashes-us-west-2.s3.us-west-2.amazonaws.com/drs_failback_automation_installer.sh.sha512`

Run the installation script:

```
bash drs_failback_automation_installer.sh
```

**Note**  
This command might ask for a sudo password if you use the Ubuntu ISO. Enter the password but **do not** run this command as sudo.

After installation completes, reload your shell profile:

```
source ~/.profile
```

The DRSFA client is installed in the `drs_failback_automation_client` directory. You can optionally delete the installer:

```
rm drs_failback_automation_installer.sh
```

## Generating the seed ISO
<a name="failback-failover-drsfa-seed-iso"></a>

Generate a `drs_failback_automation_seed.iso` file that contains the password for the Failback Client VM. Upload this file to your datastore.

```
bash drs_failback_automation_seed_creator.sh
```

Enter a unique password that follows the [AWS recommended password policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html).

Two files are generated: `drs_failback_automation_seed.iso` and `drs_failback_automation_seed.iso.sha512`. Upload the seed ISO to the same datastore where the DRS Failback Client ISO is stored.

After generating the seed ISO, you can optionally delete the seed creator:

```
rm drs_failback_automation_seed_creator.sh
```