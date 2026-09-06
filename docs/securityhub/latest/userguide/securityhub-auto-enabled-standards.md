

# Turning off automatically enabled security standards
<a name="securityhub-auto-enabled-standards"></a>

If your organization doesn't use central configuration, it uses a configuration type called *local configuration*. With local configuration, AWS Security Hub CSPM can automatically enable default security standards for new member accounts when the accounts join your organization. All the controls that apply to these default standards are also enabled automatically.

Currently, the default security standards are the AWS Foundational Security Best Practices standard and the Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0 standard. For information about these standards, see the [Standards reference for Security Hub CSPM](standards-reference.md).

If you prefer to manually enable security standards for new member accounts, you can turn off automatic enablement of the default standards. You can do this only if you integrate with AWS Organizations and use local configuration. If you use central configuration, you can instead create a configuration policy that enables the default standards and associate the policy with the root. All of your organization accounts and OUs then inherit this configuration policy unless they are associated with a different policy or are self-managed. If you don't integrate with AWS Organizations, you can disable a default standard when you initially enable Security Hub CSPM or later. To learn how, see [Disabling a standard](disable-standards.md).

To turn off automatic enablement of the default standards for new member accounts, you can use the Security Hub CSPM console or the Security Hub CSPM API.

------
#### [ Security Hub CSPM console ]

Follow these steps to turn off automatic enablement of the default standards by using the Security Hub CSPM console.

**To turn off automatic enablement of default standards**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

   Sign in using the credentials of the administrator account.

1. In the navigation pane, under **Settings**, choose **Configuration**.

1. In the **Overview** section, choose **Edit**.

1. Under **New account settings**, clear the **Enable the default security standards** checkbox.

1. Choose **Confirm**.

------
#### [ Security Hub CSPM API ]

To turn off automatic enablement of the default standards programmatically, from the Security Hub CSPM administrator account, use the [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateOrganizationConfiguration.html) operation of the Security Hub CSPM API. In your request, specify `NONE` for the `AutoEnableStandards` parameter. 

If you're using the AWS CLI, run the [update-organization-configuration](https://docs.aws.amazon.com/cli/latest/reference/securityhub/update-organization-configuration.html) command to turn off automatic enablement of the default standards. For the `auto-enable-standards` parameter, specify `NONE`. For example, the following command automatically enables Security Hub CSPM for new member accounts, and turns off automatic enablement of the default standards for the accounts.

```
$ aws securityhub update-organization-configuration --auto-enable --auto-enable-standards {{NONE}}
```

------