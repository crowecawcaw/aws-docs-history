

# Step 4: Configure the Amazon DCV server to use the broker as the authentication server
<a name="configure-dcv-server"></a>

Configure the Amazon DCV server to use the broker as the external authentication server for validating client connection tokens. You must also configure the Amazon DCV server to trust the broker's self-signed CA.

------
#### [ Linux Amazon DCV server ]

**To add the local service user for Linux Amazon DCV servers**

1. Open `/etc/dcv/dcv.conf` using your preferred text editor.

1. Add the `ca-file` and `auth-token-verifier` parameters to the `[security]` section.
   + For `ca-file`, specify the path to the broker's self-signed CA that you copied to the host in the previous step.
   + For `auth-token-verifier`, specify the URL for the token verifier on the broker in the following format: `https://{{broker_ip_or_dns}}:{{port}}/agent/validate-authentication-token`. Specify the port used for broker-agent communication, which is 8445 by default. If you are running the broker on an Amazon EC2 instance, you must use the private DNS or private IP address.

     For example

     ```
     [security]
     ca-file="/etc/dcv-session-manager-agent/broker_cert.pem"
     auth-token-verifier="https://my-sm-broker.com:8445/agent/validate-authentication-token"
     ```

1. Save and close the file.

1. Stop and restart the Amazon DCV server. For more information, see [Stopping the Amazon DCV Server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-stop.html) and [ Starting the Amazon DCV Server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-start.html) in the *Amazon DCV Administrator Guide*.

------
#### [ Windows Amazon DCV server ]

**On Windows Amazon DCV servers**

1. Open the Windows Registry Editor and navigate to the **HKEY\_USERS/S-1-5-18/Software/GSettings/com/nicesoftware/dcv/security/** key.

1. Open the **ca-file** parameter.

1. For **Value data**, specify the path to the broker's self-signed CA that you copied to the host in the previous step.
**Note**  
If the parameter does not exist, create a new string parameter and name it `ca-file`.

1. Open the **auth-token-verifier** parameter.

1. For **Value data**, specify the URL for the token verifier on the broker in the following format: `https://{{broker_ip_or_dns}}:{{port}}/agent/validate-authentication-token`.

1. Specify the port used for broker-agent communication, which is 8445 by default. If you are running the broker on an Amazon EC2 instance, you must use the private DNS or private IP address.
**Note**  
If the parameter does not exist, create a new string parameter and name it `auth-token-verifier`.

1. Choose **OK** and close the Windows Registry Editor.

1. Stop and restart the Amazon DCV server. For more information, see [Stopping the Amazon DCV Server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-stop.html) and [ Starting the Amazon DCV Server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-start.html) in the *Amazon DCV Administrator Guide*.

------
#### [ macOS Amazon DCV server ]

**To add the local service user for macOS Amazon DCV servers**

1. Open `/etc/dcv/dcv.conf` using your preferred text editor.

1. Add the `ca-file` and `auth-token-verifier` parameters to the `[security]` section.
   + For `ca-file`, specify the path to the broker's self-signed CA that you copied to the host in the previous step.
   + For `auth-token-verifier`, specify the URL for the token verifier on the broker in the following format: `https://{{broker_ip_or_dns}}:{{port}}/agent/validate-authentication-token`. Specify the port used for broker-agent communication, which is 8445 by default. If you are running the broker on an Amazon EC2 instance, you must use the private DNS or private IP address.

     For example

     ```
     [security]
     ca-file="/usr/local/etc/dcv-session-manager-agent/broker_cert.pem"
     auth-token-verifier="https://my-sm-broker.com:8445/agent/validate-authentication-token"
     ```

1. Save and close the file.

1. Stop and restart the Amazon DCV server. For more information, see [Stopping the Amazon DCV Server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-stop.html) and [ Starting the Amazon DCV Server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-start.html) in the *Amazon DCV Administrator Guide*.

------