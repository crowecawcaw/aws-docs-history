AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# app2container remote configure command

Run this command from a worker machine to configure the connections needed to
run remote workflows on application servers. This interactive command prompts
for the required information for each application server that you enter, or you
can provide a JSON input file with your connection information by specifying the
`--input-json` parameter when you run the command.

###### Note

For the remote configure command prompts, if you specify the Fully
Qualified Domain Name (FQDN), the server IP address is optional and is
not used by App2Container.

## Syntax

```
app2container remote configure [--input-json `myhosts.json`] [--help]
```

## Parameters and options

###### Parameters

**--input-json**

Uses the provided JSON file as input to configure
connections to application servers for the worker machine
to run remote commands.

###### Options

**--help**

Displays the command help.

## Input

To see the input file format, choose the system platform that matches
your configuration. For key/value pairs that do not apply to your configuration,
set string values to an empty string.

The Linux `remote_hosts.json` file contains an array
of Linux platform hosts, with connection information. The key for each host
is the host IP address or FQDN, with an array of strings for the connection
information. Each host includes the following content:

- Fqdn (string, conditionally required)
  – the fully qualified domain name of the host, used as the
  identifier for connecting. _If an IP address is used
  as the host identifier, this must be empty. If the FQDN has a
  value, the IP address is ignored._
- Ip (string, conditionally required)
  – the IP address of the host, used as the identifier for
  connecting. _Required if the FQDN is empty._
- SecretArn (string, required) – the
  Amazon Resource Name (ARN) that identifies the Secrets Manager secret to
  use for credentials.
- AuthMethod (string, required) – the
  authentication method used to connect to the host. _Valid
  values include "cert" and "key"._
  The following example shows a `remote_hosts.json` file for a Java
  application running on Linux.

```
{
        "10.10.10.10": {
                "Fqdn": "",
                "Ip": "10.10.10.10",
                "SecretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:linux-cert-Abcdef",
                "AuthMethod": "cert"
        },
        "myhost.mydomain.com": {
                "Fqdn": "myhost.mydomain.com",
                "Ip": "",
                "SecretArn": "arn:aws:secretsmanager:us-west-2:987654321098:secret:linux-cert-Ghijkl",
                "AuthMethod": "key"
        }
}
```

The Windows `remote_hosts.json` file contains an array
of Windows Server platform hosts, with connection information. The key for
each host is the host IP address or FQDN, with an array of strings for the
connection information. Each host includes the following content:

- fqdn (string, conditionally required)
  – the fully qualified domain name of the host, used as the
  identifier for connecting. _If an IP address is used
  as the host identifier, this must be empty. If the FQDN has a
  value, the IP address is ignored._
- ip (string, conditionally required)
  – the IP address of the host, used as the identifier for
  connecting. _Required if the FQDN is empty._
- secretArn (string, required) – the
  Amazon Resource Name (ARN) that identifies the Secrets Manager secret to
  use for credentials.
  The following example shows a `remote_hosts.json` file for a .NET
  application running on Windows Server.

```
{
        "10.10.10.10": {
                "fqdn": "",
                "ip": "10.10.10.10",
                "secretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:windows-cred-Abcdef"
        }
}
```

## Output

This command does not produce a configurable output file.
For troubleshooting purposes, or if you need to verify what
was entered during the interactive command dialog, you can
find the entries in the `remote_hosts.json`
file by searching the folder structure on the server where
you ran the command.

## Examples

Choose the operating system platform tab for the application server or worker machine where
you run the command.

Linux
The following example shows the **remote configure** command with no additional options.

```
`$` `sudo app2container remote configure` `Server IP address: 10.10.10.10
Server FQDN (Fully Qualified Domain Name):
Authentication method to be used key/cert: cert
Secret ARN for remote connection credentials: arn:aws:secretsmanager:us-west-2:123456789012:secret:linux-cert-Abcdef
Continue to configure servers? (y/N)[default: n]: y
Server IP address:
Server FQDN (Fully Qualified Domain Name): fqdn2
Authentication method to be used key/cert: key
Secret ARN for remote connection credentials: arn:aws:secretsmanager:us-west-2:987654321098:secret:linux-cert-Ghijkl
Continue to configure servers? (y/N)[default: n]: n`
```

Windows
The following example shows the **remote configure** command with no additional options.

```
`PS>` `app2container remote configure` `Server IP address: 10.10.10.10
Server FQDN (Fully Qualified Domain Name):
Authentication method to be used key/cert: cert
Secret ARN for remote connection credentials: arn:aws:secretsmanager:us-west-2:123456789012:secret:windows-cred-Abcdef
Continue to configure servers? (y/N)[default: n]: y
Server IP address:
Server FQDN (Fully Qualified Domain Name): fqdn2
Authentication method to be used key/cert: key
Secret ARN for remote connection credentials: arn:aws:secretsmanager:us-west-2:987654321098:secret:windows-cred-Ghijkl
Continue to configure servers? (y/N)[default: n]: n`
```
