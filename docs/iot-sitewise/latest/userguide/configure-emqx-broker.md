# Configure the EMQX broker

This section covers how to add usernames and passwords. It also covers how to
establish a TLS connection from an external source using the added username and
password. You can configure the EMQX broker using Linux or Microsoft
Windows.

###### Note

To configure the broker, you need a core device that is setup with the
default EMQX configuration in your MQTT-enabled, V3 gateway.

###### Important

After completing this procedure, we highly recommend configuring
authorization rules. For more information, see [Set up authorization rules for
AWS IoT SiteWise Edge in EMQX](authorization-rules-emqx-broker.md "authorization-rules-emqx-broker.md"). Authorization rules
for added users enhances security.

## Update the EMQX

deployment configuration for authentication

###### To update the EMQX deployment configuration for

authentication

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation, choose **Edge gateways** in the **Edge** section.
3. Choose the gateway to configure.
4. In the **Edge gateway configuration** section,
   copy your **Greengrass core device** value. Save it
   for later use.
5. Open the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
6. On the left navigation, under the **Manage**
   section, choose **Greengrass devices**, then
   **Deployments**.
7. Find the core device value you saved earlier and choose that link
   to open the deployment.
8. Choose the **Actions** dropdown button, then
   **Revise**.
9. Read the message that appears and then choose **Revise
   deployment**. The **Specify target**
   page appears.
10. Choose **Next** until you reach the
    **Configure components** step.
11. Select the `aws.greengrass.clientdevices.mqtt.EMQX`
    radio button.
12. Choose the **Configure component** button. A
    configuration page appears for the component.
13. Under **Configuration update**, choose
    **Reset to default configuration for component version:
    2.\*.\***.
14. Enter the following configuration in the **Configuration
    to merge** section based on your OS.

Linux

```
{
    "emqxConfig": {
        "authorization": {
            "no_match": "allow"
        },
        "listeners": {
            "tcp": {
                "default": {
                    "enabled": true,
                    "enable_authn": false
                }
            },
            "ssl": {
                "default": {
                    "enabled": true,
                    "enable_authn": true,
                    "ssl_options": {
                        "verify": "verify_none",
                        "fail_if_no_peer_cert": false
                    }
                }
            }
        },
        "authentication": {
            "enable": true,
            "backend": "built_in_database",
            "mechanism": "password_based",
            "password_hash_algorithm": {
                "iterations": 210000,
                "mac_fun": "sha512",
                "name": "pbkdf2"
            },
            "user_id_type": "username"
        },
        "dashboard": {
            "listeners": {
                "http": {
                    "bind": 18083
                }
            }
        }
    },
    "authMode": "bypass",
    "dockerOptions": "-p 8883:8883 -p 127.0.0.1:1883:1883 -p 127.0.0.1:18083:18083 -v emqx-data:/opt/emqx/data -e EMQX_NODE__NAME=emqx@local",
    "requiresPrivilege": "true"
}
```

Windows

```
{
    "emqxConfig": {
        "authorization": {
            "no_match": "allow"
        },
        "listeners": {
            "tcp": {
                "default": {
                    "enabled": true,
                    "enable_authn": false
                }
            },
            "ssl": {
                "default": {
                    "enabled": true,
                    "enable_authn": true,
                    "ssl_options": {
                        "verify": "verify_none",
                        "fail_if_no_peer_cert": false
                    }
                }
            }
        },
        "authentication": {
            "enable": true,
            "backend": "built_in_database",
            "mechanism": "password_based",
            "password_hash_algorithm": {
                "iterations": 210000,
                "mac_fun": "sha512",
                "name": "pbkdf2"
            },
            "user_id_type": "username"
        },
        "dashboard": {
            "listeners": {
                "http": {
                    "bind": 18083
                }
            }
        }
    },
    "authMode": "bypass",
    "requiresPrivilege": "true"
}
```

The `dockerOptions` field is only for Linux
gateways. 15. Choose **Confirm**. 16. Choose **Next** until you reach the
**Review** step. 17. Choose **Deploy**. 18. After the deployment succeeds, proceed to the next step.

## Enable username and

password authentication

This section shows you how to add usernames and passwords through the EMQX
dashboard GUI.

###### Note

The EMQX-related instructions provided are for reference only. As EMQX
documentation and features may change over time, and we do not maintain
their documentation, we recommend consulting [EMQX's official
documentation](https://docs.emqx.com/en/emqx/latest/ "https://docs.emqx.com/en/emqx/latest/") for the most current information.

EMQX Dashboard

###### To enable username and password authentication through

the EMQX dashboard

1. Ensure that you are within the gateway host.
2. Open a browser window and visit [`http://localhost:18083/`](http://localhost:18083/ "http://localhost:18083/").
3. Enter the default username of
   `admin` and the default
   password of `public`. For more
   information, see [EMQX Dashboard](https://docs.emqx.com/en/emqx/latest/dashboard/introduction.html#first-login "https://docs.emqx.com/en/emqx/latest/dashboard/introduction.html#first-login") in the _EMQX
   Docs_.
4. After login, you are prompted to change your password.
   Update your password to continue to the EMQX
   Dashboard.
5. In the left navigation, choose the shield icon, then
   **Authentication**.
6. In the **Built-in Database** row,
   choose the **Users** button.
7. Choose the plus sign icon button to add users. An
   **Add** screen appears.
8. Enter a username and password for the user of the
   external application.
9. Choose **Save**. The username you
   chose appears in the **Authentication**
   page's table.

###### Note

Existing or default authorization rules apply to the new
user. It's recommended to review and adjust them to your
external application needs.

EMQX Management with Linux
Use the AWS IoT SiteWise EMQX CLI tool at
`/greengrass/v2/bin/swe-emqx-cli`.

###### To enable username and password authentication through

EMQX Management using Linux

1. Change the admin password by running the following
   command:

```
/greengrass/v2/bin/swe-emqx-cli admin change-pwd
```

2.  When prompted, do the following:

        1. Enter your current administrator user (default
         is `admin`) and password (default is
         `public`).
        2. Enter and confirm your new password.

    If successful, you see the following message:

```
admin password changed successfully
```

3. Add users for external applications by running the
   following command:

```
/greengrass/v2/bin/swe-emqx-cli users add
```

4.  When prompted, do the following:

        1. Enter the username for the new user.
        2. Enter and confirm the password for the new
         user.

    If successful, you see the following message:

```
User '[username]' created successfully
```

5. Verify user configuration by running the following
   command:

```
/greengrass/v2/bin/swe-emqx-cli users list
```

The output shows all configured users:

```
Users:
- [your-added-username]

Total users: 1
```

EMQX Management with Windows
Use the AWS IoT SiteWise EMQX CLI tool at one of the following
locations:

- PowerShell:
  `C:\greengrass\v2\bin\swe-emqx-cli.ps1`
- Command Prompt:
  `C:\greengrass\v2\bin\swe-emqx-cli.bat`

###### To enable username and password authentication through

EMQX Management using Windows

1. Change the admin password by running the following
   command:

```
C:\greengrass\v2\bin\swe-emqx-cli.ps1 admin change-pwd
```

2.  When prompted, do the following:

        1. Enter your current administrator user (default
         is `admin`) and password (default is
         `public`).
        2. Enter and confirm your new password.

    If successful, you see the following message:

```
admin password changed successfully
```

3. Add users for external applications by running the
   following command:

```
C:\greengrass\v2\bin\swe-emqx-cli.ps1 users add
```

4.  When prompted, do the following:

        1. Enter the username for the new user.
        2. Enter and confirm the password for the new
         user.

    If successful, you see the following message:

```
User '[username]' created successfully
```

5. Verify user configuration by running the following
   command:

```
C:\greengrass\v2\bin\swe-emqx-cli.ps1 users list
```

The output shows all configured users:

```
Users:
- [your-added-username]

Total users: 1
```
