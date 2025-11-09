AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `StartSession` with a CLI

The following code examples show how to use `StartSession`.

CLI

**AWS CLI**

**Example 1: To start a Session Manager session**

This `start-session` example establishes a connection with an instance for a Session Manager session. Note that this interactive command requires the Session Manager plugin to be installed on the client machine making the call.

```
`aws ssm start-session \
 --target `"i-1234567890abcdef0"``

```

Output:

```
Starting session with SessionId: Jane-Roe-07a16060613c408b5
```

**Example 2: To start a Session Manager session using SSH**

This `start-session` example establishes a connection with an instance for a Session Manager session using SSH. Note that this interactive command requires the Session Manager plugin to be installed on the client machine making the call, and that the command uses the default user on the instance, such as `ec2-user` for EC2 instances for Linux.

```
ssh -i /path/my-key-pair.pem ec2-user@i-02573cafcfEXAMPLE
```

Output:

```
Starting session with SessionId: ec2-user-07a16060613c408b5
```

For more information, see [Start a Session](session-manager-working-with-sessions-start.md "session-manager-working-with-sessions-start.md") and [Install the Session Manager Plugin for the AWS CLI](session-manager-working-with-install-plugin.md "session-manager-working-with-install-plugin.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [StartSession](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-session.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-session.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example initiates a connection to a target for a Session Manager session, enabling port forwarding.**

```
Start-SSMSession -Target 'i-064578e5e7454488f' -DocumentName 'AWS-StartPortForwardingSession' -Parameter @{ localPortNumber = '8080'; portNumber = '80' }

```

**Output:**

```
SessionId    StreamUrl
----------    ----------
random-id0    wss://ssmmessages.amazonaws.com/v1/data-channel/random-id
```

- For API details, see
  [StartSession](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example initiates a connection to a target for a Session Manager session, enabling port forwarding. Note: You need to add Region parameter if not already set using AWSCredentials.**

```
Start-SSMSession -Target 'i-064578e5e7454488f' -DocumentName 'AWS-StartPortForwardingSession' -Parameter @{ localPortNumber = '8080'; portNumber = '80' } -Region 'us-west-1'

```

**Output:**

```
Starting session with SessionId: testUser-xi4glew849asyeryde34u4dfsdfy
Port 8080 opened for sessionId testUser-xi4glew849asyeryde34u4dfsdfy.
Waiting for connections...
```

**Example 2: This example creates an interactive session with a specified instance for a Session Manager session.**

```
Start-SSMSession -Target 'i-1234567890abcdef0' -Region 'us-west-1'

```

**Output:**

```
Starting session with SessionId : testUser-xi4glew849asyeryde34u4dfsdfy
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements!

PS C:\Windows\system32> whoami
ec2amaz-fnsdrwv\ec2-test-user
PS C:\Windows\system32>
```

**Example 3: This example creates a session without connecting to it and returns the SessionId, StreamUrl, and TokenValue properties required to connect to the session.**

```
Start-SSMSession -Target 'i-1234567890abcdef0' -Region 'us-west-1' -DisablePluginInvocation

```

**Output:**

```
SessionId        : testUser-xi4glew849asyeryde34u4dfsdfy
StreamUrl        : {StreamUrl value redacted}
TokenValue       : {Token value redacted}
ContentLength    : 1207
HttpStatusCode   : OK
```

- For API details, see
  [StartSession](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
