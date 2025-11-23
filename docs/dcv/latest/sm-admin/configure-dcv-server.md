# Step 4: Configure the Amazon DCV server to use the broker as the authentication server

Configure the Amazon DCV server to use the broker as the external authentication server for validating client connection
tokens. You must also configure the Amazon DCV server to trust the broker's self-signed CA.

Linux Amazon DCV server

###### To add the local service user for Linux Amazon DCV servers

1. Open `/etc/dcv/dcv.conf` using your preferred text editor.
2. Add the `ca-file` and `auth-token-verifier` parameters
   to the `[security]` section.
   - For `ca-file`, specify the path to the broker's self-signed
     CA that you copied to the host in the previous step.
   - For `auth-token-verifier`, specify the URL for the token verifier on the
     broker in the following format:
     `https://`broker_ip_or_dns`:`port`/agent/validate-authentication-token`.
     Specify the port used for broker-agent communication, which is 8445 by default. If you are
     running the broker on an Amazon EC2 instance, you must use the private DNS or private IP
     address.

   For example

   ```
   [security]
   ca-file="/etc/dcv-session-manager-agent/broker_cert.pem"
   auth-token-verifier="https://my-sm-broker.com:8445/agent/validate-authentication-token"

   ```

3. Save and close the file.
4. Stop and restart the Amazon DCV server. For more information, see [Stopping the Amazon DCV Server](../adminguide/manage-stop.md "../adminguide/manage-stop.md")
   and [Starting the Amazon DCV Server](../adminguide/manage-start.md "../adminguide/manage-start.md") in the _Amazon DCV Administrator
   Guide_.

Windows Amazon DCV server

###### On Windows Amazon DCV servers

1. Open the Windows Registry Editor and navigate to the
   **HKEY_USERS/S-1-5-18/Software/GSettings/com/nicesoftware/dcv/security/**
   key.
2. Open the **ca-file** parameter.
3. For **Value data**, specify the path
   to the broker's self-signed CA that you copied to the host in the previous
   step.

###### Note

If the parameter does not exist, create a new string parameter and name it
`ca-file`. 4. Open the **auth-token-verifier** parameter. 5. For **Value data**,
specify the URL for the token verifier on the broker in the following format:
`https://`broker_ip_or_dns`:`port`/agent/validate-authentication-token`. 6. Specify the port used for broker-agent communication, which is 8445 by default. If you are running the
broker on an Amazon EC2 instance, you must use the private DNS or private IP address.

###### Note

If the parameter does not exist, create a new string parameter and
name it `auth-token-verifier`. 7. Choose **OK** and close the Windows Registry Editor. 8. Stop and restart the Amazon DCV server. For more information, see [Stopping the Amazon DCV Server](../adminguide/manage-stop.md "../adminguide/manage-stop.md")
and [Starting the Amazon DCV Server](../adminguide/manage-start.md "../adminguide/manage-start.md") in the _Amazon DCV Administrator
Guide_.

macOS Amazon DCV server

###### To add the local service user for macOS Amazon DCV servers

1. Open `/etc/dcv/dcv.conf` using your preferred text editor.
2. Add the `ca-file` and `auth-token-verifier` parameters
   to the `[security]` section.
   - For `ca-file`, specify the path to the broker's self-signed
     CA that you copied to the host in the previous step.
   - For `auth-token-verifier`, specify the URL for the token verifier on the
     broker in the following format:
     `https://`broker_ip_or_dns`:`port`/agent/validate-authentication-token`.
     Specify the port used for broker-agent communication, which is 8445 by default. If you are
     running the broker on an Amazon EC2 instance, you must use the private DNS or private IP
     address.

   For example

   ```
   [security]
   ca-file="/usr/local/etc/dcv-session-manager-agent/broker_cert.pem"
   auth-token-verifier="https://my-sm-broker.com:8445/agent/validate-authentication-token"

   ```

3. Save and close the file.
4. Stop and restart the Amazon DCV server. For more information, see [Stopping the Amazon DCV Server](../adminguide/manage-stop.md "../adminguide/manage-stop.md")
   and [Starting the Amazon DCV Server](../adminguide/manage-start.md "../adminguide/manage-start.md") in the _Amazon DCV Administrator
   Guide_.
