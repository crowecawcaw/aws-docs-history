AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Amazon Q Developer in chat applications organization policies

Organization administrators can manage multiple Amazon Q Developer in chat applications settings across all accounts within an organization using Amazon Q Developer in chat applications chat applications policies (chat applications policies).
Chat applications policies define where Amazon Q Developer in chat applications can deliver notifications and if it can respond to Amazon Q Developer in chat applications mention events. Using chat applications policies, administrators can:

- Enforce which chat platforms can be used across your organization (Amazon Chime, Microsoft Teams, and Slack)
- Restrict chat client access to specific workspaces and teams.
- Restrict Slack channel visibility to either public or private channels.
- Set and enforce specific role settings.
  Chat applications policies restrict and take precedence over account level settings like [role settings](understanding-permissions.md#role-settings "understanding-permissions.md#role-settings") and [Channel guardrail policies](understanding-permissions.md#channel-guardrails "understanding-permissions.md#channel-guardrails"). Administrators can define
  rules in a policy and apply those rules to an entire organization or a group of accounts, referred to as OUs. For more information, see [Managing organizational units](../../../organizations/latest/userguide/orgs_manage_ous.md "../../../organizations/latest/userguide/orgs_manage_ous.md") in the _AWS Organizations User Guide_.
  You can access and modify these policies from the Amazon Q Developer in chat applications console or the AWS Organizations console.
  For more information about organization policies, see [Managing policies in AWS Organizations](../../../organizations/latest/userguide/orgs_manage_policies.md "../../../organizations/latest/userguide/orgs_manage_policies.md") _AWS Organizations User Guide_.

If your users try to perform an action restricted by your chat applications policy, they are informed via error message that they are disallowed due to the policy and we recommend that they contact their organization administrator.

###### Note

Amazon Q Developer in chat applications organization policies are validated at runtime, so existing resources are continuously checked for compliance.
There is no overlap with existing IAM permissions as there aren’t currently any runtime-based IAM permissions for sending notifications or interacting with Amazon Q Developer in chat applications.

###### Note

Chat application policies are limited to AWS account access to Amazon Q Developer in chat applications. These policies don't manage Amazon Q Business access from chat applications.

###### Topics

- [Example Amazon Q Developer in chat applications organization policy](#example-org-policy "#example-org-policy")
- [Enabling chat applications policies](#enable-org-pol "#enable-org-pol")
- [Disabling chat applications policies](#disable-org-pol "#disable-org-pol")
- [Tutorial: Creating chat applications policies in Amazon Q Developer in chat applications](org-policy-tutorial.md "org-policy-tutorial.md")
- [Editing chat applications policies in Amazon Q Developer in chat applications](edit-org-pol.md "edit-org-pol.md")
- [Deleting chat applications policies in Amazon Q Developer in chat applications](delete-org-pol.md "delete-org-pol.md")

## Example Amazon Q Developer in chat applications organization policy

The following policy allows restricted Amazon Q Developer in chat applications access for selected Slack workspaces and a Microsoft Teams tenant.

```
{
    "chatbot":{
       "platforms":{
          "slack":{
             "client":{
                "@@assign":"enabled"
             },
             "workspaces": { // limit 255
                   "@@assign":[
                      "Slack-Workspace-Id1",
                      "Slack-Workspace-Id2"
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
             "overrides":{ // limit 255
                "Slack-Workspace-Id2":{
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
             "tenants":{ // limit 36
                "Microsoft-Teams-Tenant-Id":{ // limit 36
                   "@@assign":[
                      "Microsoft-Teams-Team-Id"
                   ]
                }
             },
             "default":{
                "supported_role_settings":{
                   "@@assign":[
                      "user_role"
                   ]
                }
             },
             "overrides":{ // limit 36
                "Microsoft-Teams-Tenant-Id":{
                   "Microsoft-Teams-Team-Id":{
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
  This default also disables any new chat platform that Amazon Q Developer in chat applications supports. For example, if Amazon Q Developer in chat applications supports a new chat platform, this default disables that newly supported chat platform as well.

## Enabling chat applications policies

Before you can create chat applications policies, you must first enable them using the AWS Organizations console. For more information, see [Enabling a policy type](../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md#enable-policy-type "../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md#enable-policy-type") in the _AWS Organizations User Guide_.

## Disabling chat applications policies

If you no longer want to use chat applications policies in your organization, you can disable them to prevent accidental use. For more information, see [Disabling a policy type](../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md#disable-policy-type "../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md#disable-policy-type") in the _AWS Organizations User Guide_.
