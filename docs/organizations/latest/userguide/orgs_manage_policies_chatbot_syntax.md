# Chat applications policy syntax and

examples

This topic describes chat applications policy syntax and provides examples.

## Syntax for chat applications policies

A chat applications policy is a plaintext file that is structured according to the rules
of [JSON](http://json.org "http://json.org"). The syntax for chat applications policies
follows the syntax for management policy types. For a complete discussion of that
syntax, see [Understanding management policy
inheritance](orgs_manage_policies_inheritance_mgmt.md "orgs_manage_policies_inheritance_mgmt.md"). This topic focuses on
applying that general syntax to the specific requirements of the chat applications policy
type.

The following example shows the basic syntax for a chat applications policy:

```
{
    "chatbot":{
       "platforms":{
          "slack":{
             "client":{
                "@@assign":"`enabled`" // enabled | disabled
             },
             "workspaces": { // limit 255
                   "@@assign":[
                      "`Slack-Workspace-Id`"
                   ]
             },
             "default":{
                "supported_channel_types":{
                   "@@assign":[
                      "`private`" // public | private
                   ]
                },
                "supported_role_settings":{
                   "@@assign":[
                      "`user_role`" // user_role | channel_role
                   ]
                }
             },
             "overrides":{ // limit 255
                "`Slack-Workspace-Id`":{
                   "supported_channel_types":{
                      "@@assign":[
                         "`public`" // public | private
                      ]
                   },
                   "supported_role_settings":{
                      "@@assign":[
                         "`user_role`" // user_role | channel_role
                      ]
                   }
                }
             }
          },
          "microsoft_teams":{
             "client":{
                "@@assign":"`enabled`"
             },
             "tenants":{ // limit 36
                "`Microsoft-Teams-Tenant-Id`":{ // limit 36
                   "@@assign":[
                      "`Microsoft-Teams-Team-Id`"
                   ]
                }
             },
             "default":{
                "supported_role_settings":{
                   "@@assign":[
                      "`user_role`" // user_role | channel_role
                   ]
                }
             },
             "overrides":{ // limit 36
                "`Microsoft-Teams-Tenant-Id`":{ // limit 36
                   "`Microsoft-Teams-Team-Id`":{
                      "supported_role_settings":{
                         "@@assign":[
                            "`user_role`" // user_role | channel_role
                         ]
                      }
                   }
                }
             }
          },
          "chime":{
            "client":{
               "@@assign":"`disabled`" // enabled | disabled
            }
         }
       },
       "default":{
          "client":{
             "@@assign":"`disabled`" // enabled | disabled
          }
       }
    }
 }
```

This chat applications policy includes the following elements:

- The `chatbot` field key name. Chat applications policies always start with this fixed key name. It's the top line in this example policy.
- Under `chatbot`, there is a `platforms` block, which contains the configuration for the different supported chat applications: Slack, Microsoft Teams, and Amazon Chime.
  - For Slack, the following fields are available:
    - `"client"`:
      - `"enabled"`: The Slack client is enabled. Slack integrations are allowed.
      - `"disabled"`: The Slack client is disabled. Slack integrations are not allowed.

    - `"workspaces"`: Comma-separated listed of allowed Slack workspaces. In this example, the allowed Slack workspaces are `Slack-Workspace-Id1` and `Slack-Workspace-Id2`.
    - `"default"`: The default settings for Slack workspaces.
      - `"supported_channel_types"`:
        - `"public"`: Slack workspaces in scope allow public Slack channels by default.
        - `"private"`: Slack workspaces in scope allow private Slack channels by default.

      - `supported_role_settings`:
        - `"user_role"`: Slack workspaces in scope allow User level IAM roles by default.
        - `"channel_role"`: Slack workspaces in scope allow Channel level IAM roles by default.

    - `"overrides"`: The override settings for the Slack workspaces.
      - `Slack-Workspace-Id2`: Comma-separated listed of Slack workspaces where the override setting apply. In this example, the Slack workspace is `Slack-Workspace-Id2`.
        - `"supported_channel_types"`:
          - `"public"`: Override setting whether Slack workspaces in scope allow public Slack channels.
          - `"private"`: Override setting whether Slack workspaces in scope allow private Slack channels.

        - `supported_role_settings`:
          - `"user_role"`: Override setting whether Slack workspaces in scope allow User level IAM roles.
          - `"channel_role"`: Override setting whether Slack workspaces in scope allow Channel level IAM roles.

  - For Microsoft Teams, the following fields are available:
    - `"client"`:
      - `"enabled"`: The Microsoft Teams client is enabled. Microsoft Teams integrations are allowed.
      - `"disabled"`: The Microsoft Teams client is disabled. Microsoft Teams integrations are not allowed.

    - `"tenants"`: Comma-separated listed of allowed Microsoft Teams tenants.
      In this example, the allowed tenant is `Microsoft-Teams-Tenant-Id`.
      - `Microsoft-Teams-Tenant-Id`:
        Comma-separated list of allowed teams within the tenant. In this example, the allowed team is `Microsoft-Teams-Team-Id`.

    - `"default"`: The default settings for the teams within the tenant.
      - `supported_role_settings`:
        - `"user_role"`: Teams in scope allow User level IAM roles by default.
        - `"channel_role"`: Teams in scope allow Channel level IAM roles by default.

    - `"overrides"`: The override settings for the Microsoft Teams tenants.
      - `Microsoft-Teams-Tenant-Id`: Comma-separated listed of tenants where the override setting apply.
        In this example, the tenant is `Microsoft-Teams-Tenant-Id`.
        - `Microsoft-Teams-Team-Id`: Comma-separate listed of teams within the tenant. In this example, the allowed team is `Microsoft-Teams-Team-Id`.
          - `supported_role_settings`:
            - `"user_role"`: Override setting whether the teams in scope allow User level IAM roles.
            - `"channel_role"`: Override setting whether the teams in scope allow Channel level IAM roles.

  - For Amazon Chime, the following fields are available:
    - `"client"`:
      - `"enabled"`: The Amazon Chime client is enabled. Amazon Chime integrations are allowed.
      - `"disabled"`: The Amazon Chime client is disabled. Amazon Chime integrations are not allowed.

- Under `chatbot`, there is a `default` block which disables Amazon Q Developer in chat applications across the organization unless overridden at a lower level.
  This default also disables any new chat application that Amazon Q Developer in chat applications supports. For example, if Amazon Q Developer in chat applications supports a new chat application, this default disables that newly supported chat application as well.

###### Note

For more information about Channel level IAM roles and User level IAM roles, see [Understanding Amazon Q Developer in chat applications permissions](../../../chatbot/latest/adminguide/understanding-permissions.md "../../../chatbot/latest/adminguide/understanding-permissions.md") in the _Amazon Q Developer in chat applications Administrator Guide_.

## Chat applications policy examples

The example policies that follow are for information purposes only.

### Example 1:

Allow only private Slack Channels in a specific workspace, disable Microsoft Teams, all authentication modes supported

The following policy is focused on controlling the allowed configurations for Slack and Microsoft Teams chatbot integrations.

```
{
   "chatbot": {
      "platforms": {
         "slack": {
            "client": {
               "@@assign": "enabled"
            },
            "workspaces": {
               "@@assign": [
                  "`Slack-Workspace-Id`"
               ]
            },
            "default": {
               "supported_channel_types": {
                  "@@assign": [
                     "private"
                  ]
               },
               "supported_role_settings": {
                  "@@assign": [
                     "channel_role",
                     "user_role"
                  ]
               }
            }
         },
         "microsoft_teams": {
            "client": {
               "@@assign": "disabled"
            }
         },
         "chime":{
            "client":{
               "@@assign":"disabled"
            }
         },
         "default":{
            "client":{
               "@@assign":"disabled"
            }
         }
      }
   }
}
```

**For Slack**

- The Slack client is enabled.
- Only the specific Slack workspace `Slack-Workspace-Id` is allowed.
- The default settings are to allow only private Slack channels, Channel level IAM roles, and User level IAM roles.

**For Microsoft Team**

- The Microsoft Teams client is disabled.

**For Amazon Chime**

- The Amazon Chime client is disabled.

**Additional details**

- The `default` block at the bottom sets the client to be disabled, which disables Amazon Q Developer in chat applications across the organization unless overridden at a lower level.
  This default also disables any new chat application that Amazon Q Developer in chat applications supports. For example, if Amazon Q Developer in chat applications supports a new chat application, this default disables that newly supported chat application as well.

### Example 2: Allow only Slack integrations with User Level IAM roles

The following policy takes a more permissive approach to Slack, allowing all Slack workspaces but restricting the authentication mode to only User level IAM roles.

```
{
   "chatbot":{
      "platforms":{
         "slack":{
            "client":{
               "@@assign":"enabled"
            },
            "workspaces":
               {
                  "@@assign":[
                     "*"
                  ]
               },
            "default":{
               "supported_role_settings":{
                  "@@assign":[
                     "user_role"
                  ]
               }
            }
         },
         "microsoft_teams":{
            "client":{
               "@@assign":"disabled"
            }
         },
         "chime":{
            "client":{
               "@@assign":"disabled"
            }
         }
      },
      "default":{
         "client":{
            "@@assign":"disabled"
         }
      }
   }
}
```

**For Slack**

- The Slack client is enabled.
- No specific Slack workspaces are defined using the wildcard `"*"`, so all workspaces are permitted.
- The default settings are to allow only User level IAM roles.

**For Microsoft Team**

- The Microsoft Teams client is disabled.

**For Amazon Chime**

- The Amazon Chime client is disabled.

**Additional details**

- The `default` block at the bottom sets the client to be disabled, which disables Amazon Q Developer in chat applications across the organization unless overridden at a lower level.
  This default also disables any new chat application that Amazon Q Developer in chat applications supports. For example, if Amazon Q Developer in chat applications supports a new chat application, this default disables that newly supported chat application as well.

### Example 3: Allow only Microsoft Teams integrations in a specific Tenants

The following example policy locks down the organization to only allow Microsoft Teams chatbot integrations within the specified tenant, while completely blocking Slack integrations.

```
{
   "chatbot":{
      "platforms":{
         "slack":{
            "client": {
               "@@assign": "disabled"
            },
         },
         "microsoft_teams":{
            "client": {
               "@@assign": "enabled"
            },
            "tenants":{
               "`Microsoft-Teams-Tenant-Id`":{
                  "@@assign":[
                     "*"
                  ]
               }
            }
         },
         "chime": {
            "client":{
               "@@assign": "disabled"
            }
         }
      }
   }
}
```

**For Slack**

- The Slack client is disabled.

**For Microsoft Team**

- Only the specific tenant `Microsoft-Teams-Tenant-Id` is permitted, using the wildcard `"*"` to allow all teams within that tenant.

**For Amazon Chime**

- The Amazon Chime client is disabled.

**Additional details**

- The `default` block at the bottom sets the client to be disabled, which disables Amazon Q Developer in chat applications across the organization unless overridden at a lower level.
  This default also disables any new chat application that Amazon Q Developer in chat applications supports. For example, if Amazon Q Developer in chat applications supports a new chat application, this default disables that newly supported chat application as well.

### Example 4: Allows restricted Amazon Q Developer in chat applications access for Slack workspaces and a Microsoft Teams tenant

The following policy allows restricted Amazon Q Developer in chat applications access for selected Slack workspaces and a Microsoft Teams tenant.

```
{
    "chatbot":{
       "platforms":{
          "slack":{
             "client":{
                "@@assign":"enabled"
             },
             "workspaces": {
                   "@@assign":[
                      "`Slack-Workspace-Id1`",
                      "`Slack-Workspace-Id2`"
                   ]
             },
             "default":{
                "supported_channel_types":{
                   "@@assign":[
                      "private"
                   ]
                },
                "supported_role_settings":{
                   "@@assign":[
                      "user_role"
                   ]
                }
             },
             "overrides":{
                "`Slack-Workspace-Id2`":{
                   "supported_channel_types":{
                      "@@assign":[
                         "public",
                         "private"
                      ]
                   },
                   "supported_role_settings":{
                      "@@assign":[
                         "channel_role",
                         "user_role"
                      ]
                   }
                }
             }
          },
          "microsoft_teams":{
             "client":{
                "@@assign":"enabled"
             },
             "tenants":{
                "`Microsoft-Teams-Tenant-Id`":{
                   "@@assign":[
                      "`Microsoft-Teams-Team-Id`"
                   ]
                }
             },
             "default":{
                "supported_role_settings":{
                   "@@assign":[
                      "`user_role`"
                   ]
                }
             },
             "overrides":{
                "`Microsoft-Teams-Tenant-Id`":{
                   "`Microsoft-Teams-Team-Id`":{
                      "supported_role_settings":{
                         "@@assign":[
                            "channel_role",
                            "user_role"
                         ]
                      }
                   }
                }
             }
          }
       },
       "default":{
          "client":{
             "@@assign":"disabled"
          }
       }
    }
 }
```

**For Slack**

- The Slack client is enabled.
- The allowed Slack workspaces are `Slack-Workspace-Id1` and `Slack-Workspace-Id2`.
- The default settings for Slack are to only allow private channels and User level IAM roles.
- There is an override for the workspace `Slack-Workspace-Id2` that allows both public and private channels as well as both Channel level IAM roles and User level IAM roles.

**For Microsoft Team**

- The Microsoft Teams is enabled.
- The allowed Teams tenants are `Microsoft-Teams-Tenant-Id` with the team `Microsoft-Teams-Team-Id`.
- The default settings are to only allow User level IAM roles.
- There is an override for the tenant `Microsoft-Teams-Tenant-Id` that allows both Channel level IAM roles and User level IAM roles for the team `Microsoft-Teams-Team-Id`.

**Additional details**

- The `default` block at the bottom sets the client to be disabled, which disables Amazon Q Developer in chat applications across the organization unless overridden at a lower level. This means Amazon Chime is disabled in this example.
  This default also disables any new chat application that Amazon Q Developer in chat applications supports. For example, if Amazon Q Developer in chat applications supports a new chat application, this default disables that newly supported chat application as well.
