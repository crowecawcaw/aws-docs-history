# Remotely connect to Amazon GameLift Servers fleet instances

You can connect to any instance in your active Amazon GameLift Servers managed EC2 or container fleets. Common reasons to
remotely access an instance include:

- Troubleshoot issues with your game server integration.
- Fine-tune your runtime configuration and other fleet-specific settings.
- Get real-time game server activity, such as log tracking.
- Run benchmarking tools using actual player traffic.
- Investigate specific issues with a game session or server process.
  When connecting to an instance, consider these potential issues:

- You can connect to any instance in an active fleet. Generally, you can't connect
  to non-active fleets, such as fleets that are in the process of activating or are in
  an error state. (These fleets might have limited availability for a short period of
  time.) For help with fleet activation issues, see [Debug Amazon GameLift Servers fleet issues](fleets-creating-debug.md "fleets-creating-debug.md").
- Connecting to an active instance doesn't affect the instance's hosting activity.
  The instance continues to start and stop server processes based on the runtime
  configuration. It activates and runs game sessions. The instance might shut down in
  response to a scale down event or other event.
- Any changes you make to files or settings on the instance might impact the
  instance's active game sessions and connected players.

## Remote access through the console

You can connect to fleet instances directly from the Amazon GameLift Servers console using Amazon EC2 Systems Manager (SSM). This method provides secure access without requiring additional setup or credential management.

1. In the Amazon GameLift Servers console, choose **Managed EC2** or **Managed containers** from the navigation pane, and then **Fleets**.
2. Choose the fleet ID that contains the instance you want to access.
3. On the fleet details page, choose the **Instances** tab to view all compute instances for the fleet.
4. Select the instance you want to connect to, then choose **Connect**. This displays the Connect to instance dialog which informs you of the details of the connection, and allows you to view the script that will be used to connect to your instance. Confirm by choosing **Connect** again.
5. In the connection dialog, choose **Run** to create a new SSM session. The system authenticates your session through AWS Key Management Service (AWS KMS) and opens a terminal in your browser.

###### Note

Console-based remote access is available for fleets running server SDK version 5.x. For fleets running earlier SDK versions, use the AWS CLI method described in the following section.

## Remote access with the AWS CLI

The following instructions describe how to remotely connect to an instance using the AWS
command line interface (CLI). You can also make programmatic calls using the AWS SDK, as
documented in the [service API reference for Amazon GameLift Servers](../../../gamelift/latest/apireference.md "../../../gamelift/latest/apireference.md").

### Gather instance data

To connect to an Amazon GameLift Servers managed EC2 fleet instance, you need the following information:

- The ID of the instance you want to connect to. You can use either the instance
  ID or ARN.
- the server SDK for Amazon GameLift Servers version being used on the instance. The server SDK is
  integrated with the game build that is running on the instance.

The following instructions describe how complete these tasks using the AWS CLI.
You must know the fleet ID for the instance you want to connect to.

1. **Get the compute name.** Get a list of all
   active computes in the fleet. Call [list-compute](../../../cli/latest/reference/gamelift/list-compute.md "../../../cli/latest/reference/gamelift/list-compute.md") with a
   fleet ID or ARN. For a single-location fleet, specify the fleet identifier only.
   For a multi-location fleet, specify the fleet identifier and a location. With
   managed EC2 fleets, `list-compute` returns a list of fleet instances,
   and the property `ComputeName` is the instance ID. Find the compute
   you want to access.

**Request**

```
aws gamelift list-compute \
  --fleet-id  "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa" \
  --location ""sa-east-1"
```

**Response**

```
{
  "ComputeList": [
    {
      "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
      "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
      "ComputeName": "i-0abc12d3e45fa6b78",
      "IpAddress": "00.00.000.00",
      "DnsName": "b08444ki909kvqu6zpw3is24x5pyz4b6m05i3jbxvpk9craztu0lqrbbrbnbkks.uwp57060n1k6dnlnw49b78hg1rw4rcz7.us-west-2.amazongamelift.com",
      "ComputeStatus": "Active",
      "Location": "sa-east-1",
      "CreationTime": "2023-07-09T22:51:45.931000-07:00",
      "OperatingSystem": "AMAZON_LINUX_2023",
      "Type": "c4.large"
    }
  ]
}
```

2. **Find the server SDK version.** For this
   information you need to look up the build that is deployed to the fleet. Server
   SDK version is a build property.
   1. Call [describe-fleet-attributes](../../../cli/latest/reference/gamelift/describe-fleet-attributes.md "../../../cli/latest/reference/gamelift/describe-fleet-attributes.md") with a fleet ID or ARN to get the
      fleet's build ID and ARN.
   2. Call [describe-build](../../../cli/latest/reference/gamelift/describe-build.md "../../../cli/latest/reference/gamelift/describe-build.md") with the
      build ID or ARN to get the build's server SDK version.

   For example:

   **Request**

```
aws gamelift describe-fleet-attributes /
  --fleet-ids  "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
```

**Response**

```
{
  "FleetAttributes": [
    {
      "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
      "ComputeType": "EC2",
      "BuildId": "build-3333cccc-44dd-55ee-66ff-00001111aa22",
      . . .
    }
  ]
}
```

**Request**

```
aws gamelift describe-build /
  --build-id "build-3333cccc-44dd-55ee-66ff-00001111aa22"
```

**Response**

```
"Build": {
  "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
  "Name": "My_Game_Server_Build_One",
 "OperatingSystem": "AMAZON\_LINUX\_2023",

  "ServerSdkVersion": "5.1.1",
  . . .
}
```

## Connect to an instance (server SDK

5.

If the instance you want to connect to is running a game build with server SDK version
5.x, connect to the instance using Amazon EC2 Systems Manager (SSM). You can access remote instances
that are running either Windows or Linux.

###### Before you start:

Complete the SSM setup steps and install the SSM plugin on your local machine.
For more information, see [Setting up SSM](../../../systems-manager/latest/userguide/session-manager-getting-started.md "../../../systems-manager/latest/userguide/session-manager-getting-started.md") and [Install the Session Manager plugin for the AWS CLI](../../../systems-manager/latest/userguide/session-manager-working-with-install-plugin.md "../../../systems-manager/latest/userguide/session-manager-working-with-install-plugin.md") in the
_Amazon EC2 Systems Manager User Guide_.

1. **Request access credentials for the instance.**
   Call [get-compute-access](../../../cli/latest/reference/gamelift/get-compute-access.md "../../../cli/latest/reference/gamelift/get-compute-access.md") with the fleet ID and the compute name for the
   instance you want to connect to. Amazon GameLift Servers returns a set of temporary credentials
   for accessing the instance. For example:

**Request**

```
aws gamelift get-compute-access \
--compute-name i-11111111a222b333c \
--fleet-id fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa
--region us-west-2
```

**Response**

```
{
  "ComputeName": " i-11111111a222b333c ",
  "Credentials": {
    "AccessKeyId": " ASIAIOSFODNN7EXAMPLE ",
    "SecretAccessKey": " wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY ",
    "SessionToken": " AQoDYXdzEJr...<remainder of session token>"
  },
  "FleetArn": " arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa ",
  "FleetId": " fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa "
}
```

2. **Export the access credentials (optional).** You
   can export the credentials to environment variables and use them to configure
   the AWS CLI for the default user. For more details, see [Environment variables to configure the AWS CLI](../../../cli/latest/userguide/cli-configure-envvars.md "../../../cli/latest/userguide/cli-configure-envvars.md") in the
   AWS Command Line Interface User Guide.

```
export AWS_ACCESS_KEY_ID=ASIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_SESSION_TOKEN=AQoDYXdzEJr...<remainder of session token>
```

3. **Connect to the fleet instance.** Start an SSM
   session with the instance you want to connect to. Include the AWS Region or
   location of the instance. For more information, including how to set up SSM
   and the SSM plugin, see [Starting a session (AWS CLI)](../../../systems-manager/latest/userguide/session-manager-working-with-sessions-start.md#sessions-start-cli "../../../systems-manager/latest/userguide/session-manager-working-with-sessions-start.md#sessions-start-cli") in the _Amazon EC2 Systems
   Manager User Guide_.

The start-session request will automatically use the credentials that you
acquired in Step 1.

```
aws ssm start-session \
--target i-11111111a222b333c \
--region us-west-2 \
```

###### Note

If you get an access denied error, you might have an `AWS_PROFILE`
environment variable set to an AWS profile, which causes AWS CLI to use
the wrong credentials for remote access. To resolve, temporarily unset your
`AWS_PROFILE` environment variable. Alternatively, you can
create a custom AWS profile for your remote access credentials and add the
`--profile` command line parameter to your
`start-session` request.

## Connect to an instance (server SDK

4.x or earlier)

If the instance you want to connect to is running a game build with server SDK version
4 or earlier, use the following instructions. You can connect to instances that are
running either Windows or Linux. Connect to a Windows instance using a remote desktop
protocol (RDP) client. Connect to a Linux instance using an SSH client.

1. **Request access credentials for the instance.**
   When you have an instance ID, use the command [get-instance-access](../../../cli/latest/reference/gamelift/get-instance-access.md "../../../cli/latest/reference/gamelift/get-instance-access.md") to request access credentials. If successful,
   Amazon GameLift Servers returns the instance's operating system, IP address, and a set of
   credentials (user name and secret key). The credentials format depends on the
   instance operating system. Use the following instructions to retrieve
   credentials for either RDP or SSH.
   - **For Windows instances** – To
     connect to a Windows instance, RDP requires a user name and password.
     The `get-instance-access` request returns these values as
     simple strings, so you can use the returned values as is. Example
     credentials:

   ```
   "Credentials": {
       "Secret": "aA1bBB2cCCd3EEE",
       "UserName": "gl-user-remote"
   }
   ```

   - **For Linux instances** – To
     connect to a Linux instance, SSH requires a user name and private key.
     Amazon GameLift Servers issues RSA private keys and returns them as a single string, with
     the newline character (`\n`) indicating line breaks. To make
     the private key usable, take these steps: (1) convert the string to a
     `.pem` file, and (2) set permissions for the new
     file. Example credentials returned:

   ```
   "Credentials": {
       "Secret": "-----BEGIN RSA PRIVATE KEY-----nEXAMPLEKEYKCAQEAy7WZhaDsrA1W3mRlQtvhwyORRX8gnxgDAfRt/gx42kWXsT4rXE/b5CpSgie/\nvBoU7jLxx92pNHoFnByP+Dc21eyyz6CvjTmWA0JwfWiW5/akH7iO5dSrvC7dQkW2duV5QuUdE0QW\nZ/aNxMniGQE6XAgfwlnXVBwrerrQo+ZWQeqiUwwMkuEbLeJFLhMCvYURpUMSC1oehm449ilx9X1F\nG50TCFeOzfl8dqqCP6GzbPaIjiU19xX/azOR9V+tpUOzEL+wmXnZt3/nHPQ5xvD2OJH67km6SuPW\noPzev/D8V+x4+bHthfSjR9Y7DvQFjfBVwHXigBdtZcU2/wei8D/HYwIDAQABAoIBAGZ1kaEvnrqu\n/uler7vgIn5m7lN5LKw4hJLAIW6tUT/fzvtcHK0SkbQCQXuriHmQ2MQyJX/0kn2NfjLV/ufGxbL1\nmb5qwMGUnEpJaZD6QSSs3kICLwWUYUiGfc0uiSbmJoap/GTLU0W5Mfcv36PaBUNy5p53V6G7hXb2\nbahyWyJNfjLe4M86yd2YK3V2CmK+X/BOsShnJ36+hjrXPPWmV3N9zEmCdJjA+K15DYmhm/tJWSD9\n81oGk9TopEp7CkIfatEATyyZiVqoRq6k64iuM9JkA3OzdXzMQexXVJ1TLZVEH0E7bhlY9d8O1ozR\noQs/FiZNAx2iijCWyv0lpjE73+kCgYEA9mZtyhkHkFDpwrSM1APaL8oNAbbjwEy7Z5Mqfql+lIp1\nYkriL0DbLXlvRAH+yHPRit2hHOjtUNZh4Axv+cpg09qbUI3+43eEy24B7G/Uh+GTfbjsXsOxQx/x\np9otyVwc7hsQ5TA5PZb+mvkJ5OBEKzet9XcKwONBYELGhnEPe7cCgYEA06Vgov6YHleHui9kHuws\nayav0elc5zkxjF9nfHFJRry21R1trw2Vdpn+9g481URrpzWVOEihvm+xTtmaZlSp//lkq75XDwnU\nWA8gkn6O3QE3fq2yN98BURsAKdJfJ5RL1HvGQvTe10HLYYXpJnEkHv+Unl2ajLivWUt5pbBrKbUC\ngYBjbO+OZk0sCcpZ29sbzjYjpIddErySIyRX5gV2uNQwAjLdp9PfN295yQ+BxMBXiIycWVQiw0bH\noMo7yykABY7Ozd5wQewBQ4AdSlWSX4nGDtsiFxWiI5sKuAAeOCbTosy1s8w8fxoJ5Tz1sdoxNeGs\nArq6Wv/G16zQuAE9zK9vvwKBgF+09VI/1wJBirsDGz9whVWfFPrTkJNvJZzYt69qezxlsjgFKshy\nWBhd4xHZtmCqpBPlAymEjr/TOlbxyARmXMnIOWIAnNXMGB4KGSyl1mzSVAoQ+fqR+cJ3d0dyPl1j\njjb0Ed/NY8frlNDxAVHE8BSkdsx2f6ELEyBKJSRr9snRAoGAMrTwYneXzvTskF/S5Fyu0iOegLDa\nNWUH38v/nDCgEpIXD5Hn3qAEcju1IjmbwlvtW+nY2jVhv7UGd8MjwUTNGItdb6nsYqM2asrnF3qS\nVRkAKKKYeGjkpUfVTrW0YFjXkfcrR/V+QFL5OndHAKJXjW7a4ejJLncTzmZSpYzwApc=\n-----END RSA PRIVATE KEY-----",
       "UserName": "gl-user-remote"
   }
   ```

   When using the AWS CLI, you can automatically generate a
   `.pem` file by including the _--query_ and _--output_ parameters to your
   `get-instance-access` request.

   To set permissions on the `.pem` file, run the following
   command:

   ```
   $ chmod 400 MyPrivateKey.pem
   ```

2. **Open a port for the remote connection.** You
   can access instances in Amazon GameLift Servers fleets through any port authorized in the fleet
   configuration. You can view a fleet's port settings using the command [`describe-fleet-port-settings`](../../../cli/latest/reference/gamelift/describe-fleet-port-settings.md "../../../cli/latest/reference/gamelift/describe-fleet-port-settings.md").

As a best practice, we recommend opening ports for remote access only when you
need them and closing them when you're finished. You can't update port settings
after creating a fleet but before it's active. If you get stuck, re-create the
fleet with the port settings open.

Use the command [`update-fleet-port-settings`](../../../cli/latest/reference/gamelift/update-fleet-port-settings.md "../../../cli/latest/reference/gamelift/update-fleet-port-settings.md") to add a port setting
for the remote connection (such as `22` for SSH or `3389`
for RDP). For the IP range value, specify the IP addresses for the devices you
plan to use to connect (converted to CIDR format). Example:

```
$ AWS gamelift update-fleet-port-settings
    --fleet-id  "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
    --inbound-permission-authorizations "FromPort=22,ToPort=22,IpRange=54.186.139.221/32,Protocol=TCP"
```

The following example opens up port 3389 on a Windows fleet

```
$ AWS gamelift update-fleet-port-settings
--fleet-id  "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
    --inbound-permission-authorizations "FromPort=3389,ToPort=3389,IpRange=54.186.139.221/32,Protocol=TCP"
```

3. **Open a remote connection client.** Use Remote
   Desktop for Windows or SSH for Linux instances. Connect to the instance using
   the IP address, port setting, and access credentials.

SSH example:

```
ssh -i MyPrivateKey.pem gl-user-remote@192.0.2.0
```

## View files on remote

instances

Regardless of whether you have connected to an instance remotely through the console or the AWS CLI, you have full user and administrative access to it.
This means you also have the ability to cause errors or failures with game hosting. If
the instance is hosting games with active players, you may run the risk of crashing game
sessions and dropping players, or disrupting game shutdown processes which could cause errors
in saved game data and logs.

Look for these resources on a hosting instance:

- **Game build files.** These files are the game
  build that you uploaded to Amazon GameLift Servers. They include one or more game server
  executables, assets, and dependencies. Game build files are in a root directory
  called `game`:
  - On Windows: `c:\game`
  - On Linux: `/local/game`

- **Game log files.** Find the log files that your
  game server generates in the `game` root directory at whatever
  directory path you designated.
- **Amazon GameLift Servers hosting resources.** The root directory
  `Whitewater` contains files used by the Amazon GameLift Servers service to manage
  game hosting activity. Don't modify these files for any reason.
- **Runtime configuration.** Don't access runtime
  configuration for individual instances. To make changes to a runtime
  configuration property, update the fleet's runtime configuration (see the AWS
  SDK operation [UpdateRuntimeConfiguration](../../../gamelift/latest/apireference/API_UpdateRuntimeConfiguration.md "../../../gamelift/latest/apireference/API_UpdateRuntimeConfiguration.md") or the AWS CLI [update-runtime-configuration](../../../cli/latest/reference/gamelift/update-runtime-configuration.md "../../../cli/latest/reference/gamelift/update-runtime-configuration.md")).
- **Fleet data.** A JSON file contains information
  about the fleet that the instance belongs to, for use by server processes
  running on the instance. The JSON file is in the following location:
  - On Windows: `C:\GameMetadata\gamelift-metadata.json`
  - On Linux:
    `/local/gamemetadata/gamelift-metadata.json`

- **TLS certificates.** If the instance is on a
  fleet that has TLS certificate generation enabled, look for certificate files,
  including the certificate, certificate chain, private key, and root certificate
  in the following location:
  - On Windows: `c:\\GameMetadata\Certificates`
  - On Linux: `/local/gamemetadata/certificates/`
