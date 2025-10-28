Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Configuring and running Amazon EKS Anywhere on Snowball Edge devices

Follow these procedures to configure and start Amazon EKS Anywhere on your Snowball Edge
devices. Then, to configure Amazon EKS Anywhere to operate on disconnected devices, complete
additional procedures before disconnecting those devices from the external network. For more
information, see [Configuring Amazon EKS Anywhere on AWS Snow for disconnected operation](configure-disconnected.md "configure-disconnected.md").

###### Topics

- [Initial setup for Amazon EKS Anywhere on Snowball Edge](#initial-setup "#initial-setup")
- [Configuring and running Amazon EKS Anywhere on Snowball Edge devices automatically](#auto-eksa-configuration "#auto-eksa-configuration")
- [Configuring and running Amazon EKS Anywhere on Snowball Edge devices manually](#manual-eksa-configuration "#manual-eksa-configuration")

## Initial setup for Amazon EKS Anywhere on Snowball Edge

Perform the initial setup on each Snowball Edge device by connecting the device to your
local network, downloading the Snowball Edge client, getting credentials, and unlocking the
device.

###### Perform initial setup

1. Download and install the Snowball Edge client. For more information, see [Downloading and installing the Snowball Edge
   Client](using-client-commands.md#download-the-client "using-client-commands.md#download-the-client").
2. Connect the device to your local network. For more information, see [Connecting a Snowball Edge to your local
   network](getting-started.md#getting-started-connect "getting-started.md#getting-started-connect").
3. Get credentials to unlock your device. For more information, see [Getting credentials to access a Snowball Edge](getting-started.md#get-credentials "getting-started.md#get-credentials").
4. Unlock the device. For more information, see [Unlocking the Snowball Edge](unlockdevice.md "unlockdevice.md"). You can also use a script tool instead of unlocking devices manually. See [Unlock devices](https://github.com/aws-samples/aws-snow-tools-for-eks-anywhere/tree/main/setup-tools#Unlock-devices "https://github.com/aws-samples/aws-snow-tools-for-eks-anywhere/tree/main/setup-tools#Unlock-devices").

## Configuring and running Amazon EKS Anywhere on Snowball Edge devices automatically

You can use sample script tools to set up the environment and run an Amazon EKS Anywhere admin instance or you can do so manually. To use the script tools, see [Unlock devices and setup environment for Amazon EKS Anywhere](https://github.com/aws-samples/aws-snow-tools-for-eks-anywhere/tree/main/setup-tools#Unlock-devices-and-setup-envorinment-for-EKS-Anywhere "https://github.com/aws-samples/aws-snow-tools-for-eks-anywhere/tree/main/setup-tools#Unlock-devices-and-setup-envorinment-for-EKS-Anywhere"). After the environment is set up and the Amazon EKS Anywhere admin instance is running, if you need to configure Amazon EKS Anywhere to operate on the Snowball Edge device while disconnected from a network, see [Configuring Amazon EKS Anywhere on AWS Snow for disconnected operation](configure-disconnected.md "configure-disconnected.md"). Otherwise, see [Creating and maintaining clusters on Snowball Edge devices](maintain-eks-a-clusters-snow.md "maintain-eks-a-clusters-snow.md").

To manually set up the environment and run an Amazon EKS Anywhere admin instance, see [Configuring and running Amazon EKS Anywhere on Snowball Edge devices manually](#manual-eksa-configuration "#manual-eksa-configuration").

## Configuring and running Amazon EKS Anywhere on Snowball Edge devices manually

Before configuring Amazon EKS Anywhere on a Snowball Edge device, set up a profile for the Snowball Edge Client. For more information, see [Configuring and using the Snowball Edge Client](using-client-commands.md "using-client-commands.md").

###### Topics

- [Create an Amazon EKS Anywhere IAM local user](#create-role "#create-role")
- [(Optional) Create and import a Secure Shell key on a Snowball Edge](#create-ssh-key "#create-ssh-key")
- [Run an Amazon EKS Anywhere admin instance on a Snowball Edge and transfer credential and certificate files to it](#start-config-eksa-admin-instance "#start-config-eksa-admin-instance")

### Create an Amazon EKS Anywhere IAM local user

For best security practices, create a local IAM user for Amazon EKS Anywhere on the
Snowball Edge device. You can do this by manually using the following procedures.

###### Note

Do this for each Snowball Edge device that you use.

#### Create a local user on the Snowball Edge

Use the `create-user` command to create the Amazon EKS Anywhere IAM user.

```

aws iam create-user --user-name `user-name` --endpoint http://`snowball-ip`:6078 --profile `profile-name`
    {
        "User": {
            "Path": "/",
            "UserName": "eks-a-user",
            "UserId": "AIDACKCEVSQ6C2EXAMPLE",
            "Arn": "arn:aws:iam::123456789012:user/eks-a-user",
            "CreateDate": "2022-04-06T00:13:35.665000+00:00"
        }
    }

```

#### Create a policy for the local user on the Snowball Edge

Create a policy document, use it to create an IAM policy, and attach that policy to
the Amazon EKS Anywhere local user.

###### To create a policy document and attach it to the Amazon EKS Anywhere local user

1. Create a policy document and save it to your computer. Copy the policy below to the
   document.
2. Use the `create-policy` command to create an IAM policy based on the
   policy document. The value of the `--policy-document` parameter should use
   the absolute path to the policy file. For example,
   `file:///home/user/policy-name.json`

```

aws iam create-policy --policy-name `policy-name` --policy-document `file:///home/user/policy-name.json` --endpoint http://`snowball-ip`:6078 --profile `profile-name`
{
    "Policy": {
        "PolicyName": "policy-name",
        "PolicyId": "ANPACEMGEZDGNBVGY3TQOJQGEZAAAABP76TE5MKAAAABCCOTR2IJ43NBTJRZBU",
        "Arn": "arn:aws:iam::123456789012:policy/policy-name",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 0,
        "IsAttachable": true,
        "CreateDate": "2022-04-06T04:46:56.907000+00:00",
        "UpdateDate": "2022-04-06T04:46:56.907000+00:00"
    }
}

```

3. Use the `attach-user-policy` command to attach the IAM policy to the Amazon EKS Anywhere local user.

```

aws iam attach-user-policy --policy-arn `policy-arn` --user-name `user-name` --endpoint http://`snowball-ip`:6078 --profile `profile-name`

```

#### Create an access key and a credential

file on the Snowball Edge

Create an access key for the Amazon EKS Anywhere IAM local user. Then, create a credential file and include in it the values of `AccessKeyId` and `SecretAccessKey` generated for the local user. The credential file will be used by the Amazon EKS Anywhere admin instance later.

1. Use the `create-access-key` command to create an access key for the Amazon EKS Anywhere local user.

```

aws iam create-access-key --user-name `user-name` --endpoint http://`snowball-ip`:6078 --profile `profile-name`
    {
        "AccessKey": {
            "UserName": "eks-a-user",
            "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
            "Status": "Active",
            "SecretAccessKey": "RTT/wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "CreateDate": "2022-04-06T04:23:46.139000+00:00"
        }
    }

```

2. Create a credential file. In it, save the `AccessKeyId` and
   `SecretAccessKey` values in the following format.

```

[snowball-ip]
aws_access_key_id = ABCDEFGHIJKLMNOPQR2T
aws_secret_access_key = AfSD7sYz/TBZtzkReBl6PuuISzJ2WtNkeePw+nNzJ
region = snow

```

###### Note

If you're working with multiple Snowball Edge devices, the order of the credentials in the
file doesn’t matter, but the credentials for all devices do need to be in one
file.

#### Create a certificates file for the

admin instance on the Snowball Edge

The Amazon EKS Anywhere admin instance needs the certificates of the Snowball Edge devices in order to run on them. Create a certificates file holding the certificate to access Snowball Edge devices for use later by the Amazon EKS Anywhere admin instance.

###### To create a certificates file

1. Use the `list-certificates` command to get certificates for each Snowball Edge device that you plan to use.

```

`PATH_TO_Snowball_Edge_CLIENT`/bin/snowballEdge list-certificates --endpoint https://`snowball-ip` --manifest-file `path-to-manifest-file` --unlock-code `unlock-code`
{
  "Certificates" : [ {
    "CertificateArn" : "arn:aws:snowball-device:::certificate/xxx",
    "SubjectAlternativeNames" : [ "ID:JID-xxx" ]
  } ]
}

```

2. Use the value of `CertificateArn` as the value for the `--certificate-arn` parameter of the `get-certificate` command.

```

`PATH_TO_Snowball_Edge_CLIENT`/bin/snowballEdge get-certificate --certificate-arn `ARN` --endpoint https://`snowball-ip` --manifest-file `path-to-manifest-file` --unlock-code `unlock-code`

```

3. Create a device certificate file. Put the output of `get-certificate` into the certificate file. Following is an example of how to save the output.

###### Note

If you're working with multiple Snowball Edge devices, the order of the credentials in the
file doesn’t matter, but the credentials for all devices do need to be in one
file.

```

-----BEGIN CERTIFICATE-----
ZWtzYSBzbm93IHRlc3QgY2VydGlmaWNhdGUgZWtzYSBzbm93IHRlc3QgY2VydGlm
aWNhdGVla3NhIHNub3cgdGVzdCBjZXJ0aWZpY2F0ZWVrc2Egc25vdyB0ZXN0IGNl
cnRpZmljYXRlZWtzYSBzbm93IHRlc3QgY2VydGlmaWNhdGVla3NhIHNub3cgdGVz
dCBjZXJ0aWZpY2F0ZQMIIDXDCCAkSgAwIBAgIJAISM0nTVmbj+MA0GCSqGSIb3DQ
...
-----END CERTIFICATE-----

```

4. Repeat [Create an Amazon EKS Anywhere IAM local user](#create-role "#create-role") to create an IAM local user for Amazon EKS Anywhere on all Snowball Edge devices.

### (Optional) Create and import a Secure Shell key on a Snowball Edge

Use this optional procedure to create a Secure Shell (SSH) key to access all Amazon EKS
Anywhere node instances and to import the public key to all Snowball Edge devices. Keep and
secure this key file.

If you skip this procedure, Amazon EKS Anywhere will create and import an SSH key
automatically when necessary. This key will be stored on the admin instance in
`${PWD}/${CLUSTER_NAME}/eks-a-id_rsa`.

###### Create an SSH key and import it to the Amazon EKS Anywhere instance

1. Use the `ssh-keygen` command to generate a SSH key.

```

ssh-keygen -t rsa -C "`key-name`" -f `path-to-key-file`

```

2. Use the `import-key-pair` command to import the key from your computer
   to the Snowball Edge device.

###### Note

The value of the `key-name` parameter must be the same when you import the key to all devices.

```

aws ec2 import-key-pair --key-name `key-name` --public-key-material fileb:///`path/to/key-file` --endpoint http://`snowball-ip`:8008 --profile `profile-name`
{
    "KeyFingerprint": "5b:0c:fd:e1:a0:69:05:4c:aa:43:f3:3b:3e:04:7f:51",
    "KeyName": "default",
    "KeyPairId": "s.key-85edb5d820c92a6f8"
}

```

### Run an Amazon EKS Anywhere admin instance on a Snowball Edge and transfer credential and certificate files to it

#### Run an Amazon EKS Anywhere admin instance on a Snowball Edge

Follow this procedure to manually run an Amazon EKS Anywhere admin instance, configure a
Virtual Network Interface (VNI) for the admin instance, check the status of the instance,
create an SSH key, and connect to the admin instance with it. You can use a sample script tool to automate creating an Amazon EKS Anywhere admin instance and transferring credential and certificate files to this instance. See [Create Amazon EKS Anywhere admin instance](https://github.com/aws-samples/aws-snow-tools-for-eks-anywhere/tree/main/setup-tools#Create-EKS-Anywhere-admin-instance "https://github.com/aws-samples/aws-snow-tools-for-eks-anywhere/tree/main/setup-tools#Create-EKS-Anywhere-admin-instance"). After the script tool completes, you can ssh into the instance and create clusters by referring to [Creating and maintaining clusters on Snowball Edge devices](maintain-eks-a-clusters-snow.md "maintain-eks-a-clusters-snow.md"). If you want to set up the Amazon EKS Anywhere instance manually, use the following steps..

###### Note

If you're using more than one Snowball Edge devices to provision the cluster, you can launch
an Amazon EKS Anywhere admin instance on any of the Snowball Edge devices.

###### To run an Amazon EKS Anywhere admin instance

1. Use the `create-key-pair` command to create a SSH key for the Amazon EKS Anywhere admin instance. The command saves the key to `$PWD/key-file-name`.

```

aws ec2 create-key-pair --key-name `key-name` --query 'KeyMaterial' --output text --endpoint http://`snowball ip`:8008 > `key-file-name` --profile `profile-name`
```

2. Use the `describe-images` command to find the image name that begins with `eks-anywhere-admin` from the output.

```

aws ec2 describe-images --endpoint http://`snowball-ip`:8008 --profile `profile-name`

```

3. Use the `run-instance` command to start an eks-a admin instance with the Amazon EKS Anywhere admin image.

```

aws ec2 run-instances --image-id `eks-a-admin-image-id` --key-name `key-name` --instance-type sbe-c.xlarge --endpoint http://`snowball-ip`:8008 --profile `profile-name`

```

4. Use the `describe-instances` command to check the status of the Amazon EKS Anywhere instance. Wait until the command indicates the instances state is `running` before continuing.

```

aws ec2 describe-instances --instance-id `instance-id` --endpoint http://`snowball-ip`:8008 --profile `profile-name`

```

5. From the output of the `describe-device` command, note the value of `PhysicalNetworkInterfaceId` for the physical network interface that is connected to your network. You will use this to create a VNI.

```

`PATH_TO_Snowball_Edge_CLIENT`/bin/snowballEdge describe-device --endpoint https://`snowball-ip` --manifest-file `path-to-manifest-file` --unlock-code `unlock-code`

```

6. Create a VNI for the Amazon EKS Anywhere admin instance. Use the value of `PhysicalNetworkInterfaceId` as the value of the `physical-network-interface-id` parameter.

```

`PATH_TO_Snowball_Edge_CLIENT`/bin/snowballEdge create-virtual-network-interface --ip-address-assignment dhcp --physical-network-interface-id `PNI` --endpoint https://`snowball-ip` --manifest-file `path-to-manifest-file` --unlock-code `unlock-code`

```

7. Use the value of `IpAddress` as the value of the `public-ip` parameter of the `associate-address` command to associate the public address to the Amazon EKS Anywhere admin instance.

```

aws ec2 associate-address --instance-id `instance-id` --public-ip `VNI-IP` --endpoint http://`snowball-ip`:8008 --profile `profile-name`

```

8. Connect to the Amazon EKS Anywhere admin instance by SSH.

```

ssh -i `path-to-key` ec2-user@`VNI-IP`

```

#### Transfer certificate and credential files to the

admin instance on the Snowball Edge

After the Amazon EKS Anywhere admin instance is running, transfer the credentials and
certificates of your Snowball Edge devices to the admin instance. Run the following
command from the same directory where you saved the credentials and certificates files in
[Create an access key and a credential
file on the Snowball Edge](#create-eksa-iam-user-access-key "#create-eksa-iam-user-access-key") and [Create a certificates file for the
admin instance on the Snowball Edge](#create-credentials-for-admin-instance "#create-credentials-for-admin-instance").

```

scp -i `path-to-key` `path-to-credentials-file` `path-to-certificates-file` ec2-user@`eks-admin-instance-ip`:~

```

Verify the contents of the files on the Amazon EKS Anywhere admin instance. Following are examples of the credential and certificate files.

```

[192.168.1.1]
aws_access_key_id = EMGEZDGNBVGY3TQOJQGEZB5ULEAAIWHWUJDXEXAMPLE
aws_secret_access_key = AUHpqjO0GZQHEYXDbN0neLNlfR0gEXAMPLE
region = snow

[192.168.1.2]
aws_access_key_id = EMGEZDGNBVGY3TQOJQGEZG5O7F3FJUCMYRMI4KPIEXAMPLE
aws_secret_access_key = kY4Cl8+RJAwq/bu28Y8fUJepwqhDEXAMPLE
region = snow

```

```

-----BEGIN CERTIFICATE-----
ZWtzYSBzbm93IHRlc3QgY2VydGlmaWNhdGUgZWtzYSBzbm93IHRlc3QgY2VydGlm
aWNhdGVla3NhIHNub3cgdGVzdCBjZXJ0aWZpY2F0ZWVrc2Egc25vdyB0ZXN0IGNl
cnRpZmljYXRlZWtzYSBzbm93IHRlc3QgY2VydGlmaWNhdGVla3NhIHNub3cgdGVz
dCBjZXJ0aWZpY2F0ZQMIIDXDCCAkSgAwIBAgIJAISM0nTVmbj+MA0GCSqGSIb3DQ
...
-----END CERTIFICATE-----

-----BEGIN CERTIFICATE-----
KJ0FPl2PAYPEjxr81/PoCXfZeARBzN9WLUH5yz1ta+sYUJouzhzWuLJYA1xqcCPY
mhVlkRsN4hVdlBNRnCCpRF766yjdJeibKVzXQxoXoZBjrOkuGwqRy3d3ndjK77h4
OR5Fv9mjGf7CjcaSjk/4iwmZvRSaQacb0YG5GVeb4mfUAuVtuFoMeYfnAgMBAAGj
azBpMAwGA1UdEwQFMAMBAf8wHQYDVR0OBBYEFL/bRcnBRuSM5+FcYFa8HfIBomdF
...
-----END CERTIFICATE-----

```
