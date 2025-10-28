# Describe your key pairs

You can describe the key pairs that you stored in Amazon EC2. You can also retrieve the public
key material and identify the public key that was specified at launch.

###### Tasks

- [Describe your key pairs](#describe-public-key "#describe-public-key")
- [Retrieve the public key material](#retrieving-the-public-key "#retrieving-the-public-key")
- [Identify the public key specified at
  launch](#identify-key-pair-specified-at-launch "#identify-key-pair-specified-at-launch")

## Describe your key pairs

You can view the following information about your public keys that are stored in Amazon EC2:
public key name, ID, key type, fingerprint, public key material, the date and time (in the
UTC time zone) the key was created by Amazon EC2 (if the key was created by a third-party tool,
then it's the date and time the key was imported to Amazon EC2), and any tags that are associated
with the public key.

Console

###### To view information about your key pairs

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigator, choose **Key Pairs**.
3. You can view the information about each public key in the **Key
   pairs** table.

![Key pairs table.](images/key-pairs-describe-console.png) 4. To view a public key's tags, select the checkbox next to the key, and then
choose **Actions**, **Manage tags**.

AWS CLI

###### To view information about a key pair

Use the [describe-key-pairs](../../../cli/latest/reference/ec2/describe-key-pairs.md "../../../cli/latest/reference/ec2/describe-key-pairs.md") command.

```
aws ec2 describe-key-pairs --key-names `key-pair-name`
```

PowerShell

###### To view information about a key pair

Use the [Get-EC2KeyPair](../../../powershell/latest/reference/items/Get-EC2KeyPair.md "../../../powershell/latest/reference/items/Get-EC2KeyPair.md") cmdlet.

```
Get-EC2KeyPair -KeyName `key-pair-name`
```

## Retrieve the public key material

You can get the public key material for your key pairs. The following is an
example public key. Note that there are line breaks added for readability.

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQClKsfkNkuSevGj3eYhCe53pcjqP3maAhDFcvBS7O6V
hz2ItxCih+PnDSUaw+WNQn/mZphTk/a/gU8jEzoOWbkM4yxyb/wB96xbiFveSFJuOp/d6RJhJOI0iBXr
lsLnBItntckiJ7FbtxJMXLvvwJryDUilBMTjYtwB+QhYXUMOzce5Pjz5/i8SeJtjnV3iAoG/cQk+0FzZ
qaeJAAHco+CY/5WrUBkrHmFJr6HcXkvJdWPkYQS3xqC0+FmUZofz221CBt5IMucxXPkX4rWi+z7wB3Rb
BQoQzd8v7yeb7OzlPnWOyN0qFU0XA246RA8QFYiCNYwI3f05p6KLxEXAMPLE
```

Private key

###### To retrieve the public key material using ssh-keygen (Linux)

On your local Linux or macOS computer, use the **ssh-keygen**
command. Specify the path where you downloaded your private key (the
`.pem` file).

```
ssh-keygen -y -f /`path_to_key_pair`/`my-key-pair`.pem
```

If this **ssh-keygen** command fails, run the following
**chmod** command to ensure that the private key file has
the required permissions.

```
chmod 400 `key-pair-name`.pem
```

###### To retrieve the public key material using PuTTYgen (Windows)

On your local Windows computer, start PuTTYgen. Choose **Load**.
Select the `.ppk` or `.pem` private key file.
PuTTYgen displays the public key under **Public key for pasting into
OpenSSH authorized_keys file**. You can also view the public key by
choosing **Save public key**, specifying a name for the file,
saving the file, and then opening the file.

AWS CLI

###### To retrieve the public key material

Use the following [describe-key-pairs](../../../cli/latest/reference/ec2/describe-key-pairs.md "../../../cli/latest/reference/ec2/describe-key-pairs.md")
command and specify the `--include-public-key` option.

```
aws ec2 describe-key-pairs \
    --key-names `key-pair-name` \
    --include-public-key \
    --query "KeyPairs[].PublicKey"
```

PowerShell

###### To retrieve the public key material

Use the [Get-EC2KeyPair](../../../powershell/latest/reference/items/Get-EC2KeyPair.md "../../../powershell/latest/reference/items/Get-EC2KeyPair.md")
cmdlet.

```
(Get-EC2KeyPair -KeyName `key-pair-name` -IncludePublicKey $true).PublicKey
```

IMDSv2

###### Linux

Run the following commands from your Linux instance.

```
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key
```

###### Windows

Run the following cmdlets from your Windows instance.

```
[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token
```

```
Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key
```

IMDSv1

###### Linux

Run the following command from your Linux instance.

```
curl http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key
```

###### Windows

Run the following cmdlet from your Windows instance.

```
Invoke-RestMethod -uri  http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key
```

## Identify the public key specified at

launch

If you specify a public key when you launch an instance, the public key name is
recorded by the instance. The public key name reported for an instance does not
change, even if you change the public key on the instance or add public keys.

Console

###### To identify the public key specified at instance launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance.
4. On the **Details** tab, under **Instance
   details**, find **Key pair assigned at launch**.

AWS CLI

###### To identify the public key specified at instance launch

Use the following [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md")
command.

```
aws ec2 describe-instances \
    --instance-id `i-1234567890abcdef0` \
    --query "Reservations[].Instances[].KeyName" \
    --output text
```

The following is example output.

```
key-pair-name
```

PowerShell

###### To identify the public key specified at instance launch

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md")
cmdlet.

```
(Get-EC2Instance -InstanceId `i-1234567890abcdef0`).Instances | Select KeyName
```

The following is example output.

```
KeyName
-------
key-pair-name
```
