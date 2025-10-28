# Update the EMQX

deployment configuration for authorization

###### To update the EMQX deployment configuration for authorization

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
14. Paste the following content in the **Configuration to
    merge** section based on your OS.

Linux

```
{
    "emqxConfig": {
        "authorization": {
            "no_match": "deny",
            "sources": [
                {
                    "type": "built_in_database"
                },
                {
                    "type": "file",
                    "path": "data/authz/acl.conf"
                }
            ]
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
            "no_match": "deny",
            "sources": [
                {
                    "type": "built_in_database"
                },
                {
                    "type": "file",
                    "path": "C:\\greengrass\\v2\\work\\aws.greengrass.clientdevices.mqtt.EMQX\\v2\\data\\authz\\acl.conf"
                }
            ]
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

15. Choose **Confirm**.
16. Choose **Next** until you reach the
    **Review** step.
17. Choose **Deploy**.

###### Note

From this point onward, you can't edit the ACL file to update the
authorization rules. Alternatively, you can proceed to [Add authorization rules through the
EMQX Dashboard for users](add-rules-emqx-broker.md "add-rules-emqx-broker.md") after a successful
deployment.
