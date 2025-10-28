# Connect to the EC2 Serial Console

You can connect to the serial console of your EC2 instance by using the Amazon EC2 console or
through SSH. After connecting to the serial console, you can use it for troubleshooting boot,
network configuration, and other issues. For more information about troubleshooting, see [Troubleshoot your Amazon EC2 instance using the
EC2 Serial Console](troubleshoot-using-serial-console.md "troubleshoot-using-serial-console.md").

###### Considerations

- Only 1 active serial console connection is supported per instance.
- The serial console connection typically lasts for 1 hour unless [you disconnect from it](disconnect-serial-console-session.md "disconnect-serial-console-session.md"). However,
  during system maintenance, Amazon EC2 will disconnect the serial console session.

The duration of the connection is not determined by the duration of your IAM
credentials. If your IAM credentials expire, the connection continues to persist until the
maximum duration of the serial console connection is reached. When using the EC2 Serial
Console console experience, if your IAM credentials expire, terminate the connection by
closing the browser page.

- It takes 30 seconds to tear down a session after you've disconnected from the serial
  console in order to allow a new session.
- Supported serial console ports: `ttyS0` (Linux instances) and
  `COM1` (Windows instances)
- When you connect to the serial console, you might observe a slight drop in your
  instance’s throughput.

###### Topics

- [Connect using the browser-based
  client](#sc-connect-browser-based-client "#sc-connect-browser-based-client")
- [Connect using your own key and SSH client](#sc-connect-SSH "#sc-connect-SSH")
- [EC2 Serial Console endpoints and
  fingerprints](#sc-endpoints-and-fingerprints "#sc-endpoints-and-fingerprints")

## Connect using the browser-based

client

You can connect to your EC2 instance's serial console by using the browser-based client.
You do this by selecting the instance in the Amazon EC2 console and choosing to connect to the
serial console. The browser-based client handles the permissions and provides a successful
connection.

EC2 serial console works from most browsers, and supports keyboard and mouse
input.

Before connecting, make sure you have completed the [prerequisites](ec2-serial-console-prerequisites.md "ec2-serial-console-prerequisites.md").

###### To connect to your instance's serial port using the browser-based client (Amazon EC2

console)

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance and choose **Actions**, **Monitor and
   troubleshoot**, **EC2 Serial Console**,
   **Connect**.

Alternatively, select the instance and choose **Connect**,
**EC2 Serial Console**, **Connect**.

An in-browser terminal window opens. 4. Press **Enter**. If a login prompt returns, you are connected to
the serial console.

If the screen remains black, you can use the following information to help resolve
issues with connecting to the serial console:

    * **Check that you have configured access to the serial
     console.** For more information, see [Configure access to the EC2 Serial Console](configure-access-to-serial-console.md "configure-access-to-serial-console.md").
    * (Linux instances only) **Use SysRq to connect to the serial
     console.** SysRq does not require that you connect using the browser-based
     client. For more information, see [(Linux instances) Use SysRq to troubleshoot your instance](troubleshoot-using-serial-console.md#SysRq "troubleshoot-using-serial-console.md#SysRq").
    * (Linux instances only) **Restart getty.** If you
     have SSH access to your instance, then connect to your instance using SSH, and
     restart getty using the following command.



    ```
    `[ec2-user ~]$` sudo systemctl restart serial-getty@ttyS0
    ```
    * **Reboot your instance.** You can reboot your
     instance by using SysRq (Linux instances), the EC2 console, or the AWS CLI. For more
     information, see [(Linux instances) Use SysRq to troubleshoot your instance](troubleshoot-using-serial-console.md#SysRq "troubleshoot-using-serial-console.md#SysRq") (Linux instances) or
     [Reboot your Amazon EC2 instance](ec2-instance-reboot.md "ec2-instance-reboot.md").

5. (Linux instances only) At the `login` prompt, enter the username of the
   password-based user that you [set up previously](configure-access-to-serial-console.md#set-user-password "configure-access-to-serial-console.md#set-user-password"),
   and then press **Enter**.
6. (Linux instances only) At the `Password` prompt, enter the password, and
   then press **Enter**.

## Connect using your own key and SSH client

You can use your own SSH key and connect to your instance from the SSH client of your
choice while using the serial console API. This enables you to benefit from the serial
console capability to push a public key to the instance.

After pushing the SSH key to the instance, the SSH connection is not subject to the
IAM policies that you configured to grant users EC2 Serial Console access.

###### Before you begin

Verify that the [prerequisites](ec2-serial-console-prerequisites.md "ec2-serial-console-prerequisites.md")
are met.

###### To connect to an instance's serial console using SSH

1. **Push your SSH public key to the instance to start a serial
   console session**

Use the [send-serial-console-ssh-public-key](../../../cli/latest/reference/ec2-instance-connect/send-serial-console-ssh-public-key.md "../../../cli/latest/reference/ec2-instance-connect/send-serial-console-ssh-public-key.md") command to push your SSH public key to the
instance. This starts a serial console session.

If a serial console session has already been started for this instance, the command
fails because you can only have one session open at a time. It takes 30 seconds to tear
down a session after you've disconnected from the serial console in order to allow a new
session.

```
aws ec2-instance-connect send-serial-console-ssh-public-key \
    --instance-id `i-001234a4bf70dec41EXAMPLE` \
    --serial-port 0 \
    --ssh-public-key file://`my_key.pub` \
    --region `us-east-1`
```

2. ###### Connect to the serial console using your private key

Use the **ssh** command to connect to the serial console before the
public key is removed from the serial console service. You have 60 seconds before it is
removed.

Use the private key that corresponds to the public key.

The username format is `instance-id.port0`, which comprises the instance
ID and port 0. In the following example, the username is
`i-001234a4bf70dec41EXAMPLE.port0`.

The endpoint of the serial console service is different for each Region. See the
[EC2 Serial Console endpoints and
fingerprints](#sc-endpoints-and-fingerprints "#sc-endpoints-and-fingerprints") table for each Region's endpoint. In
the following example, the serial console service is in the us-east-1 Region.

```
ssh -i `my_key` `i-001234a4bf70dec41EXAMPLE.port0`@`serial-console.ec2-instance-connect.us-east-1.aws`
```

The following example uses `timeout 3600` to set your SSH session to
terminate after 1 hour. Processes started during the session may continue running on
your instance after the session terminates.

```
timeout 3600 ssh -i `my_key` `i-001234a4bf70dec41EXAMPLE.port0`@`serial-console.ec2-instance-connect.us-east-1.aws`
```

3. ###### (Optional) Verify the fingerprint

When you connect for the first time to the serial console, you are prompted to
verify the fingerprint. You can compare the serial console fingerprint with the
fingerprint that's displayed for verification. If these fingerprints don't match,
someone might be attempting a "man-in-the-middle" attack. If they match, you can
confidently connect to the serial console.

The following fingerprint is for the serial console service in the us-east-1 Region.
For the fingerprints for each Region, see [EC2 Serial Console endpoints and
fingerprints](#sc-endpoints-and-fingerprints "#sc-endpoints-and-fingerprints").

```
SHA256:dXwn5ma/xadVMeBZGEru5l2gx+yI5LDiJaLUcz0FMmw
```

The fingerprint only appears the first time you connect to the serial
console. 4. Press **Enter**. If a prompt returns, you are connected
to the serial console.

If the screen remains black, you can use the following information to help resolve
issues with connecting to the serial console:

    * **Check that you have configured access to the serial
     console.** For more information, see [Configure access to the EC2 Serial Console](configure-access-to-serial-console.md "configure-access-to-serial-console.md").
    * (Linux instances only) **Use SysRq to connect to the serial
     console.** SysRq does not require that you connect using SSH. For more
     information, see [(Linux instances) Use SysRq to troubleshoot your instance](troubleshoot-using-serial-console.md#SysRq "troubleshoot-using-serial-console.md#SysRq").
    * (Linux instances only) **Restart getty.** If you
     have SSH access to your instance, then connect to your instance using SSH, and
     restart getty using the following command.



    ```
    `[ec2-user ~]$` sudo systemctl restart serial-getty@ttyS0
    ```
    * **Reboot your instance.** You can reboot your
     instance by using SysRq (Linux instances only), the EC2 console, or the AWS CLI. For
     more information, see [(Linux instances) Use SysRq to troubleshoot your instance](troubleshoot-using-serial-console.md#SysRq "troubleshoot-using-serial-console.md#SysRq") (Linux instances
     only) or [Reboot your Amazon EC2 instance](ec2-instance-reboot.md "ec2-instance-reboot.md").

5. (Linux instances only) At the `login` prompt, enter the username of the
   password-based user that you [set up previously](configure-access-to-serial-console.md#set-user-password "configure-access-to-serial-console.md#set-user-password"),
   and then press **Enter**.
6. (Linux instances only) At the `Password` prompt, enter the password, and
   then press **Enter**.

## EC2 Serial Console endpoints and

fingerprints

The following are the service endpoints and fingerprints for EC2 Serial Console. To
connect programmatically to an instance's serial console, you use an EC2 Serial Console
endpoint. The EC2 Serial Console endpoints and fingerprints are unique for each AWS
Region.

| Region Name               | Region         | Endpoint                                                        | Fingerprint                                        |
| ------------------------- | -------------- | --------------------------------------------------------------- | -------------------------------------------------- |
| US East (Ohio)            | us-east-2      | serial-console.ec2-instance-connect.us-east-2.aws               | SHA256:EhwPkTzRtTY7TRSzz26XbB0/HvV9jRM7mCZN0xw/d/0 |
| US East (N. Virginia)     | us-east-1      | serial-console.ec2-instance-connect.us-east-1.aws               | SHA256:dXwn5ma/xadVMeBZGEru5l2gx+yI5LDiJaLUcz0FMmw |
| US West (N. California)   | us-west-1      | serial-console.ec2-instance-connect.us-west-1.aws               | SHA256:OHldlcMET8u7QLSX3jmRTRAPFHVtqbyoLZBMUCqiH3Y |
| US West (Oregon)          | us-west-2      | serial-console.ec2-instance-connect.us-west-2.aws               | SHA256:EMCIe23TqKaBI6yGHainqZcMwqNkDhhAVHa1O2JxVUc |
| Africa (Cape Town)        | af-south-1     | ec2-serial-console.af-south-1.api.aws                           | SHA256:RMWWZ2fVePeJUqzjO5jL2KIgXsczoHlz21Ed00biiWI |
| Asia Pacific (Hong Kong)  | ap-east-1      | ec2-serial-console.ap-east-1.api.aws                            | SHA256:T0Q1lpiXxChoZHplnAkjbP7tkm2xXViC9bJFsjYnifk |
| Asia Pacific (Hyderabad)  | ap-south-2     | ec2-serial-console.ap-south-2.api.aws                           | SHA256:WJgPBSwV4/shN+OPITValoewAuYj15DVW845JEhDKRs |
| Asia Pacific (Jakarta)    | ap-southeast-3 | ec2-serial-console.ap-southeast-3.api.aws                       | SHA256:5ZwgrCh+lfns32XITqL/4O0zIfbx4bZgsYFqy3o8mIk |
| Asia Pacific (Malaysia)   | ap-southeast-5 | ec2-serial-console.ap-southeast-5.api.aws                       | SHA256:cQXTHQMRcqRdIjmAGoAMBSExeoRobYyRwT67yTjnEiA |
| Asia Pacific (Melbourne)  | ap-southeast-4 | ec2-serial-console.ap-southeast-4.api.aws                       | SHA256:Avaq27hFgLvjn5gTSShZ0oV7h90p0GG46wfOeT6ZJvM |
| Asia Pacific (Mumbai)     | ap-south-1     | serial-console.ec2-instance-connect.ap-south-1.aws              | SHA256:oBLXcYmklqHHEbliARxEgH8IsO51rezTPiSM35BsU40 |
| Asia Pacific (Osaka)      | ap-northeast-3 | ec2-serial-console.ap-northeast-3.api.aws                       | SHA256:Am0/jiBKBnBuFnHr9aXsgEV3G8Tu/vVHFXE/3UcyjsQ |
| Asia Pacific (Seoul)      | ap-northeast-2 | serial-console.ec2-instance-connect.ap-northeast-2.aws          | SHA256:FoqWXNX+DZ++GuNTztg9PK49WYMqBX+FrcZM2dSrqrI |
| Asia Pacific (Singapore)  | ap-southeast-1 | serial-console.ec2-instance-connect.ap-southeast-1.aws          | SHA256:PLFNn7WnCQDHx3qmwLu1Gy/O8TUX7LQgZuaC6L45CoY |
| Asia Pacific (Sydney)     | ap-southeast-2 | serial-console.ec2-instance-connect.ap-southeast-2.aws          | SHA256:yFvMwUK9lEUQjQTRoXXzuN+cW9/VSe9W984Cf5Tgzo4 |
| Asia Pacific (Thailand)   | ap-southeast-7 | ec2-serial-console.ap-southeast-7.api.aws                       | SHA256:KCAZiRYrR1Q2lqsg7vTwixWmvc2wmjVT31XRgSdEfDY |
| Asia Pacific (Tokyo)      | ap-northeast-1 | serial-console.ec2-instance-connect.ap-northeast-1.aws          | SHA256:RQfsDCZTOfQawewTRDV1t9Em/HMrFQe+CRlIOT5um4k |
| Canada (Central)          | ca-central-1   | serial-console.ec2-instance-connect.ca-central-1.aws            | SHA256:P2O2jOZwmpMwkpO6YW738FIOTHdUTyEv2gczYMMO7s4 |
| Canada West (Calgary)     | ca-west-1      | ec2-serial-console.ca-west-1.api.aws                            | SHA256:s3rc8lI2xhbhr3iedjJNxGAFLPGOLjx7IxxXrGckk6Q |
| China (Beijing)           | cn-north-1     | ec2-serial-console.cn-north-1.api.amazonwebservices.com.cn      | SHA256:2gHVFy4H7uU3+WaFUxD28v/ggMeqjvSlgngpgLgGT+Y |
| China (Ningxia)           | cn-northwest-1 | ec2-serial-console.cn-northwest-1.api.amazonwebservices.com.cn  | SHA256:TdgrNZkiQOdVfYEBUhO4SzUA09VWI5rYOZGTogpwmiM |
| Europe (Frankfurt)        | eu-central-1   | serial-console.ec2-instance-connect.eu-central-1.aws            | SHA256:aCMFS/yIcOdOlkXvOl8AmZ1Toe+bBnrJJ3Fy0k0De2c |
| Europe (Ireland)          | eu-west-1      | serial-console.ec2-instance-connect.eu-west-1.aws               | SHA256:h2AaGAWO4Hathhtm6ezs3Bj7udgUxi2qTrHjZAwCW6E |
| Europe (London)           | eu-west-2      | serial-console.ec2-instance-connect.eu-west-2.aws               | SHA256:a69rd5CE/AEG4Amm53I6lkD1ZPvS/BCV3tTPW2RnJg8 |
| Europe (Milan)            | eu-south-1     | ec2-serial-console.eu-south-1.api.aws                           | SHA256:lC0kOVJnpgFyBVrxn0A7n99ecLbXSX95cuuS7X7QK30 |
| Europe (Paris)            | eu-west-3      | serial-console.ec2-instance-connect.eu-west-3.aws               | SHA256:q8ldnAf9pymeNe8BnFVngY3RPAr/kxswJUzfrlxeEWs |
| Europe (Spain)            | eu-south-2     | ec2-serial-console.eu-south-2.api.aws                           | SHA256:GoCW2DFRlu669QNxqFxEcsR6fZUz/4F4n7T45ZcwoEc |
| Europe (Stockholm)        | eu-north-1     | serial-console.ec2-instance-connect.eu-north-1.aws              | SHA256:tkGFFUVUDvocDiGSS3Cu8Gdl6w2uI32EPNpKFKLwX84 |
| Europe (Zurich)           | eu-central-2   | ec2-serial-console.eu-central-2.api.aws                         | SHA256:8Ppx2mBMf6WdCw0NUlzKfwM4/IfRz4OaXFutQXWp6mk |
| Israel (Tel Aviv)         | il-central-1   | ec2-serial-console.il-central-1.api.aws                         | SHA256:JR6q8v6kNNPi8+QSFQ4dj5dimNmZPTgwgsM1SNvtYyU |
| Mexico (Central)          | mx-central-1   | ec2-serial-console.mx-central-1.api.aws                         | SHA256:BCuVl13iQNk+CcVnt18Ef4p2ZHUrBBAOxlFetB32GS0 |
| Middle East (Bahrain)     | me-south-1     | ec2-serial-console.me-south-1.api.aws                           | SHA256:nPjLLKHu2QnLdUq2kVArsoK5xvPJOMRJKCBzCDqC3k8 |
| Middle East (UAE)         | me-central-1   | ec2-serial-console.me-central-1.api.aws                         | SHA256:zpb5duKiBZ+l0dFwPeyykB4MPBYhI/XzXNeFSDKBvLE |
| South America (São Paulo) | sa-east-1      | serial-console.ec2-instance-connect.sa-east-1.aws               | SHA256:rd2+/32Ognjew1yVIemENaQzC+Botbih62OqAPDq1dI |
| AWS GovCloud (US-East)    | us-gov-east-1  | serial-console.ec2-instance-connect.us-gov-east-1.amazonaws.com | SHA256:tIwe19GWsoyLClrtvu38YEEh+DHIkqnDcZnmtebvF28 |
| AWS GovCloud (US-West)    | us-gov-west-1  | serial-console.ec2-instance-connect.us-gov-west-1.amazonaws.com | SHA256:kfOFRWLaOZfB+utbd3bRf8OlPf8nGO2YZLqXZiIw5DQ |
