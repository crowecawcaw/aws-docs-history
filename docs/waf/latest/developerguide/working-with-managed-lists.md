**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using Firewall Manager managed lists

This section explains what managed lists are and how to use them.

Managed application and protocol lists streamline your configuration and management of
AWS Firewall Manager content audit security group policies. You use managed lists to define the
protocols and applications that your policy allows and disallows.
For information about content audit security group policies, see [Using content audit security group policies with Firewall Manager](security-group-policies-audit.md "security-group-policies-audit.md").

You can use the following types of managed lists in a content audit security group
policy:

- **Firewall Manager application lists and protocol lists**
  – Firewall Manager manages these lists.
  - The application lists include
    `FMS-Default-Public-Access-Apps-Allowed` and
    `FMS-Default-Public-Access-Apps-Denied`, which describe
    commonly used applications that should be allowed or denied to the
    general public.
  - The protocol lists include `FMS-Default-Protocols-Allowed`,
    a list of commonly used protocols that should be allowed to the general
    public. You can use any list that Firewall Manager manages, but you can't edit or
    delete it.

- **Custom application lists and protocol lists** – You
  manage these lists. You can create lists of either type with the settings that
  you need. You have full control over your own custom managed lists, and you can
  create, edit, and delete them as needed.

###### Note

Currently, Firewall Manager doesn't check references to a custom managed list when you delete it.
This means that you can delete a custom managed application list or protocol
list even when it is in use by an active policy. This can cause the policy
to stop functioning. Delete an application list or protocol list only after
you have verified that it isn't referenced by any active polices.
Managed lists are AWS resources. You can tag a custom managed list. You can't tag
a Firewall Manager managed list.

## Managed list versioning

Custom managed lists don't have versions. When you edit a custom list, policies that
reference the list automatically use the updated list.

Firewall Manager managed lists are versioned. The Firewall Manager service team publishes new
versions as needed, in order to apply the best security practices to the lists.

When you use a Firewall Manager managed list in a policy, you choose your versioning strategy as
follows:

- **Latest available version** – If you don't specify an explicit
  version setting for the list, then your policy automatically uses the latest
  version. This is the only option available through the console.
- **Explicit version** – If you specify a version for
  the list, then your policy uses that version. Your policy remains locked to
  the version that you specified until you modify the version setting. To
  specify the version, you must define the policy outside of the console, for
  example through the CLI or one of the SDKs.

For more information about choosing the version setting for a list, see [Using managed lists in your content audit security group
policies](#using-managed-lists "#using-managed-lists").

## Using managed lists in your content audit security group

policies

When you create a content audit security group policy, you can choose to use managed audit
policy rules. Some of the settings for this option require a managed application
list or protocol list. Examples of these settings include protocols that are allowed
in security group rules and applications can access the internet.

The following restrictions apply for each policy setting that uses a managed list:

- You can specify at most one Firewall Manager managed list for any setting. By default, you can
  specify at most one custom list. The custom list limit is a soft quota, so
  you can request an increase to it. For more information, see [AWS Firewall Manager quotas](fms-limits.md "fms-limits.md").
- In the console, if you select a Firewall Manager managed list, you can't specify the version. The
  policy will always use the latest version of the list. To specify the
  version, you must define the policy outside of the console, for example
  through the CLI or one of the SDKs. For information about versioning for
  Firewall Manager managed lists, see [Managed list versioning](#versioning-managed-lists "#versioning-managed-lists").

For information about creating a content audit security group policy through the
console, see [Creating a
content audit security group policy](create-policy.md#creating-firewall-manager-policy-audit-security-group "create-policy.md#creating-firewall-manager-policy-audit-security-group").
