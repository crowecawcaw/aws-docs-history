# Download prebuilt packages of the Network Flow Monitor agent by using the command line

You can use the command line to install the Network Flow Monitor agent as a package in Amazon Linux 2023,
or download and install prebuilt packages of the Network Flow Monitor agent.

Before or after you download a prebuilt package, you can optionally verify the package signature.
For more information, see [Verify the signature of the Network Flow Monitor agent package](#CloudWatch-NetworkFlowMonitor-agents-download-agent-commandline-verify-sig "#CloudWatch-NetworkFlowMonitor-agents-download-agent-commandline-verify-sig").

Choose from the following instructions, depending on the Linux operating system that you're using
and the type of installation that you want.

**Amazon Linux AMIs**
The Network Flow Monitor agent is available as a package in Amazon Linux 2023. If you're using
this operating system, you can install the package by entering the following command:

`sudo yum install network-flow-monitor-agent`

You must also make sure that the IAM role attached to the instance has the
[CloudWatchNetworkFlowMonitorAgentPublishPolicy](security-iam-awsmanpol-network-flow-monitor.md#security-iam-awsmanpol-CloudWatchNetworkFlowMonitorAgentPublishPolicy "security-iam-awsmanpol-network-flow-monitor.md#security-iam-awsmanpol-CloudWatchNetworkFlowMonitorAgentPublishPolicy") policy
attached. For more information, see [Configure permissions for agents](CloudWatch-NetworkFlowMonitor-agents-ec2-permissions.md "CloudWatch-NetworkFlowMonitor-agents-ec2-permissions.md").

**Amazon Linux 2023**
Install the package for your architecture by using one of the following commands:

- **x86_64**: `sudo yum install 
https://networkflowmonitoragent.awsstatic.com/latest/x86_64/network-flow-monitor-agent.rpm`
- **ARM64 (Graviton)**: `sudo yum install 
https://networkflowmonitoragent.awsstatic.com/latest/arm64/network-flow-monitor-agent.rpm`

Verify that Network Flow Monitor agent is successfully installed by running the following command and
verifying that the response shows that the agent is enabled and active:

```
service network-flow-monitor status
network-flow-monitor.service - Network Flow Monitor Agent
     Loaded: loaded (/usr/lib/systemd/system/network-flow-monitor.service; enabled; preset: enabled)
     Active: active (running) since Wed 2025-04-23 19:17:16 UTC; 1min 9s ago
```

**DEB-based distributions (Debian, Ubuntu)**

Install the package for your architecture by using one of the following commands:

- **x86_64**:
  `wget https://networkflowmonitoragent.awsstatic.com/latest/x86_64/network-flow-monitor-agent.deb`
- **ARM64 (Graviton)**:
  `wget https://networkflowmonitoragent.awsstatic.com/latest/arm64/network-flow-monitor-agent.deb`

Install the package by using the following command: `$ sudo apt-get install ./network-flow-monitor-agent.deb`

Verify that Network Flow Monitor agent is successfully installed by running the following command and
verifying that the response shows that the agent is enabled and active:

```
service network-flow-monitor status
network-flow-monitor.service - Network Flow Monitor Agent
     Loaded: loaded (/usr/lib/systemd/system/network-flow-monitor.service; enabled; preset: enabled)
     Active: active (running) since Wed 2025-04-23 19:17:16 UTC; 1min 9s ago
```

## Verify the signature of the Network Flow Monitor agent package

The Network Flow Monitor agent rpm and deb installer packages for Linux instances are cryptographically signed.
You can use a public key to verify that the agent package is original and unmodified. If the files
are damaged or have been altered, the verification fails. You can verify the signature of the
installer package using either RPM or GPG. The following information is for Network Flow Monitor agent versions 0.1.3 or later.

To find the correct signature file for each architecture and operating system, use the following table.

| Architecture | Platform          | Download link                                                                               | Signature file link                                                                             |
| ------------ | ----------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| x86-64       | Amazon Linux 2023 | https://networkflowmonitoragent.awsstatic.com/latest/x86\_64/network-flow-monitor-agent.rpm | https://networkflowmonitoragent.awsstatic.com/latest/x86\_64/network-flow-monitor-agent.rpm.sig |
| ARM64        | Amazon Linux 2023 | https://networkflowmonitoragent.awsstatic.com/latest/arm64/network-flow-monitor-agent.rpm   | https://networkflowmonitoragent.awsstatic.com/latest/arm64/network-flow-monitor-agent.rpm.sig   |
| x86-64       | Debian/Ubuntu     | https://networkflowmonitoragent.awsstatic.com/latest/x86\_64/network-flow-monitor-agent.deb | https://networkflowmonitoragent.awsstatic.com/latest/x86\_64/network-flow-monitor-agent.deb.sig |
| ARM64        | Debian/Ubuntu     | https://networkflowmonitoragent.awsstatic.com/latest/arm64/network-flow-monitor-agent.deb   | https://networkflowmonitoragent.awsstatic.com/latest/arm64/network-flow-monitor-agent.deb.sig   |

Follow the steps here to verify the signature of the Network Flow Monitor agent.

###### To verify the signature of the Network Flow Monitor agent for Amazon S3 package

1. Install GnuPG so that you can run the gpg command. GnuPG is required to verify the authenticity
   and integrity of a downloaded Network Flow Monitor agent for an Amazon S3 package. GnuPG is installed by default on
   Amazon Linux Amazon Machine Images (AMIs).
2. Copy the following public key and save it to a file named `nfm-agent.gpg`.

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

mQINBGf0b5IBEAC6YQc0aYrTbcHNWWMbLuqsqfspzWrtCvoU0yQ62ld7nvCGBha9
lu4lbhtiwoDawC3h6Xsxc3Pmm6kbMQfZdbo4Gda4ahf6zDOVI5zVHs3Yu2VXC2AU
5BpKQJmYddTb7dMI3GBgEodJY05NHQhq1Qd2ptdh03rsX+96Fvi4A6t+jsGzMLJU
I+hGEKGif69pJVyptJSibK5bWCDXh3eS/+vB/CbXumAKi0sq4rXv/VPiIhn6bsCI
A2lmzFd3vMJQUM/T7m7skrqetZ4mWHr1LPDFPK/H/81s8TJawx7MACsK6kIRUxu+
oicW8Icmg9S+BpIgONT2+Io5P1tYO5a9AyVF7X7gU0VgHUA1RoLnjHQHXbCmnFtW
cYEuwhUuENMl+tLQCZ+fk0kKjOlIKqeS9AVwhks92oETh8wpTwTE+DTBvUBP9aHo
S39RTiJCnUmA6ZCehepgpwW9AYCc1lHv/xcahD418E0UHV22qIw943EwAkzMDA4Q
damdRm0Nud0OmilCjo9oogEB+NUoy//5XgQMH1hhfsHquVLU/tneYexXYMfo/Iu5
TKyWL2KdkjKKP/dMR4lMAXYi0RjTJJ5tg5w/VrHhrHePFfKdYsgN6pihWwj2Px/M
ids3W1Ce50LOEBc2MOKXYXGd9OZWyR8l15ZGkySvLqVlRGwDwKGMC/nS2wARAQAB
tEJOZXR3b3JrIEZsb3cgTW9uaXRvciBBZ2VudCA8bmV0d29yay1mbG93LW1vbml0
b3ItYWdlbnRAYW1hem9uLmNvbT6JAlcEEwEIAEEWIQR2c2ypl63T6dJ3JqjvvaTM
vJX60QUCZ/RvkgIbAwUJBaOagAULCQgHAgIiAgYVCgkICwIEFgIDAQIeBwIXgAAK
CRDvvaTMvJX60euSD/9cIu2BDL4+MFFHhyHmG3/se8+3ibW0g8SyP3hsnq7qN+bm
ZzLAhll7DVoveNmEHI1VC7Qjwb30exgLcyK2Ld6uN6lwjjK0qiGGz943t230pJ3z
u7V2fVtAN+vgDVmD7agE6iqrRCWu3WfcgzFlEkE/7nkhtbWzlaK+NkdEBzNZ+W7/
FmLClzIbMjIBW2M8LdeZdQX0SWljy18x7NGNukWeNTJxmkDsjAeKl+zkXYk9h7ay
n3AVl1KrLZ5P9vQ5XsV5e4T6qfQ3XNY1lm54cpa+eD7NyYcTGRDK+vIxO4xD8i2M
yl1iNf2+84Tt6/SAgR/P9SJ5tbKD0iU9n4g1eBJVGmHDuXTtDR4H/Ur7xRSxtuMl
yZP/sLWm8p7+Ic7aQJ5OVw36MC7Oa7/K/zQEnLFFPmgBwGGiNiw5cUSyCBHNvmtv
FK0Q2XMXtBEBU9f44FMyzNJqVdPywg8Y6xE4wc/68uy7G6PyqoxDSP2ye/p+i7oi
OoA+OgifchZfDVhe5Ie0zKR0/nMEKTBV0ecjglb/WhVezEJgUFsQcjfOXNUBesJW
a9kDGcs3jIAchzxhzp/ViUBmTg6SoGKh3t+3uG/RK2ougRObJMW3G+DI7xWyY+3f
7YsLm0eDd3dAZG3PdltMGp0hKTdslvpws9qoY8kyR0Fau4l222JvYP27BK44qg==
=INr5
-----END PGP PUBLIC KEY BLOCK-----
```

3. Import the public key into your keyring and note the returned value.

```
`PS>`  rpm --import nfm-agent.gpg
`gpg: key 3B789C72: public key "Network Flow Monitor Agent" imported
gpg: Total number processed: 1
gpg: imported: 1 (RSA: 1)`
```

Make a note of the key value because you need it in the next step. In this
example, the key value is `3B789C72`. 4. Verify the fingerprint by running the following command. Be sure to replace
`key-value` with the value from the preceding step. We
recommend that you use GPG to verify the fingerprint even if you use RPM to verify
the installer package.

```
`PS>`  gpg --fingerprint `key-value`
`pub rsa4096 2025-04-08 [SC] [expires: 2028-04-07]
 7673 6CA9 97AD D3E9 D277 26A8 EFBD A4CC BC95 FAD1
uid Network Flow Monitor Agent <network-flow-monitor-agent@amazon.com>`
```

The fingerprint string should be equal to the following:

`7673 6CA9 97AD D3E9 D277 26A8 EFBD A4CC BC95 FAD1`

If the fingerprint string doesn't match, don't install the agent. Contact
Amazon Web Services.

After you have verified the fingerprint, you can use it to verify the signature of
the Network Flow Monitor agent package. 5. Download the package signature file, if you haven't already done so, based on your instance's architecture
and operating system. 6. Verify the installer package signature. Be sure to replace the `signature-filename`
and `agent-download-filename` with the values that you specified when you
downloaded the signature file and agent, as shown in the table earlier in this topic.

```
`PS>` gpg --verify `sig-filename` `agent-download-filename`
`gpg: Signature made Tue Apr 8 00:40:02 2025 UTC
gpg: using RSA key 77777777EXAMPLEKEY
gpg: issuer "network-flow-monitor-agent@amazon.com"
gpg: Good signature from "Network Flow Monitor Agent <network-flow-monitor-agent@amazon.com>" [unknown]
gpg: WARNING: Using untrusted key!`
```

If the output includes the phrase `BAD signature`, check to make sure that you
performed the procedure correctly. If you continue to get this response, contact
[AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/")
and avoid using the downloaded file.

Note the warning about trust. A key is trusted only if you or someone who you trust
has signed it. This doesn't mean that the signature is invalid, only that you have not
verified the public key.

Next, follow the steps here to verify the RPM package.

###### To verify the signature of the RPM package

1. Copy the following public key and save it to a file named `nfm-agent.gpg`.

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

mQINBGf0b5IBEAC6YQc0aYrTbcHNWWMbLuqsqfspzWrtCvoU0yQ62ld7nvCGBha9
lu4lbhtiwoDawC3h6Xsxc3Pmm6kbMQfZdbo4Gda4ahf6zDOVI5zVHs3Yu2VXC2AU
5BpKQJmYddTb7dMI3GBgEodJY05NHQhq1Qd2ptdh03rsX+96Fvi4A6t+jsGzMLJU
I+hGEKGif69pJVyptJSibK5bWCDXh3eS/+vB/CbXumAKi0sq4rXv/VPiIhn6bsCI
A2lmzFd3vMJQUM/T7m7skrqetZ4mWHr1LPDFPK/H/81s8TJawx7MACsK6kIRUxu+
oicW8Icmg9S+BpIgONT2+Io5P1tYO5a9AyVF7X7gU0VgHUA1RoLnjHQHXbCmnFtW
cYEuwhUuENMl+tLQCZ+fk0kKjOlIKqeS9AVwhks92oETh8wpTwTE+DTBvUBP9aHo
S39RTiJCnUmA6ZCehepgpwW9AYCc1lHv/xcahD418E0UHV22qIw943EwAkzMDA4Q
damdRm0Nud0OmilCjo9oogEB+NUoy//5XgQMH1hhfsHquVLU/tneYexXYMfo/Iu5
TKyWL2KdkjKKP/dMR4lMAXYi0RjTJJ5tg5w/VrHhrHePFfKdYsgN6pihWwj2Px/M
ids3W1Ce50LOEBc2MOKXYXGd9OZWyR8l15ZGkySvLqVlRGwDwKGMC/nS2wARAQAB
tEJOZXR3b3JrIEZsb3cgTW9uaXRvciBBZ2VudCA8bmV0d29yay1mbG93LW1vbml0
b3ItYWdlbnRAYW1hem9uLmNvbT6JAlcEEwEIAEEWIQR2c2ypl63T6dJ3JqjvvaTM
vJX60QUCZ/RvkgIbAwUJBaOagAULCQgHAgIiAgYVCgkICwIEFgIDAQIeBwIXgAAK
CRDvvaTMvJX60euSD/9cIu2BDL4+MFFHhyHmG3/se8+3ibW0g8SyP3hsnq7qN+bm
ZzLAhll7DVoveNmEHI1VC7Qjwb30exgLcyK2Ld6uN6lwjjK0qiGGz943t230pJ3z
u7V2fVtAN+vgDVmD7agE6iqrRCWu3WfcgzFlEkE/7nkhtbWzlaK+NkdEBzNZ+W7/
FmLClzIbMjIBW2M8LdeZdQX0SWljy18x7NGNukWeNTJxmkDsjAeKl+zkXYk9h7ay
n3AVl1KrLZ5P9vQ5XsV5e4T6qfQ3XNY1lm54cpa+eD7NyYcTGRDK+vIxO4xD8i2M
yl1iNf2+84Tt6/SAgR/P9SJ5tbKD0iU9n4g1eBJVGmHDuXTtDR4H/Ur7xRSxtuMl
yZP/sLWm8p7+Ic7aQJ5OVw36MC7Oa7/K/zQEnLFFPmgBwGGiNiw5cUSyCBHNvmtv
FK0Q2XMXtBEBU9f44FMyzNJqVdPywg8Y6xE4wc/68uy7G6PyqoxDSP2ye/p+i7oi
OoA+OgifchZfDVhe5Ie0zKR0/nMEKTBV0ecjglb/WhVezEJgUFsQcjfOXNUBesJW
a9kDGcs3jIAchzxhzp/ViUBmTg6SoGKh3t+3uG/RK2ougRObJMW3G+DI7xWyY+3f
7YsLm0eDd3dAZG3PdltMGp0hKTdslvpws9qoY8kyR0Fau4l222JvYP27BK44qg==
=INr5
-----END PGP PUBLIC KEY BLOCK-----
```

2. Import the public key into your keyring.

```
`PS>`  rpm --import nfm-agent.gpg
```

3. Verify the installer package signature. Be sure to replace the `agent-download-filename`
   with the value that you specified when you downloaded the agent, as shown in the table earlier in this topic.

```
`PS>`  rpm --checksig `agent-download-filename`
```

For example, for the x86_64 architecture on Amazon Linux 2023, use the following command:

```
`PS>`  rpm --checksig network-flow-monitor-agent.rpm
```

This command returns output similar to the following.

```
network-flow-monitor-agent.rpm: digests signatures OK
```

If the output contains the phrase `NOT OK (MISSING KEYS: (MD5) key-id)`, check to make
sure that you performed the procedure correctly. If you continue to get this response, contact
[AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") and don't install the agent.
