# Grant acceptance and activation in License Manager

When a grant is created for a granted license, it is distributed to the recipient. A
granted license must be accepted and activated before it can be used by the grant
recipient. The grant activation process can include additional options for granted licenses
sourced from the AWS Marketplace.

By default, the **Grant overview** page for a granted license has a
status of `Pending Acceptance`. You can choose to `Accept`,
`Accept and Activate`, or `Reject` the grant. Grants that are
accepted but not yet activated have a status of `Disabled`. Accepted and
activated grants have a status of `Active`.

A granted license must be accepted and activated before it can be used by the grant
recipient. By default, the grant details page for a granted license has a status of
**Pending acceptance**. You can choose to **Accept**,
**Accept and Activate**, or **Reject** the license.
Grants that are accepted but not yet activated have a status of
**Disabled**. Accepted and activated grants have a status of
**Active**.

###### Tip

You can automatically accept grants that come from the management account of your
organization. To enable grant auto-acceptance, link your organization accounts on the
[settings](settings.md "settings.md") page in the AWS License Manager console from the management account.

You can't activate two licenses for the same product from AWS Marketplace at the same time. If you
have two subscriptions (for example, the public offer for a product and a private offer, or
a subscribed license for a product and a granted license for the same product), you can
take one of the following actions:

1. Disable the existing grant for the same product and then activate the new
   grant.
2. Activate the new grant and specify that you want to disable and replace the
   existing active grant with the new grant. You can use the License Manager console or the
   AWS CLI:
   1. Using the License Manager console, activate the new grant while selecting
      **Yes** that you want to replace active grants.
   2. Using the `CreateGrantVersion` API, activate the new grant by
      specifying `ALL_GRANTS_PERMITTED_BY_ISSUER` for the
      `ActivationOverrideBehavior` with a `Status` of
      `Active`.

Console
You can use the License Manager console to activate a grant. When you activate a grant
sourced from the AWS Marketplace, you might be presented with the option whether to replace
active grants:

- As a license administrator, you must specify if you want to replace
  active grants when activating a grant.

- As a grantor, you can optionally specify if you want to replace active
  grants when you activate a grant for another account in your
  organization.

- As a grantee, if the grantor creating the distributed grant didn't
  specify whether to replace active grants, you must make a selection when
  activating the grant.

###### To activate a grant (Console)

1. Open the License Manager console at
   https://console.aws.amazon.com/license-manager/.
2. In the navigation pane, choose **Granted
   licenses**.
3. Choose a license ID to open the **License overview**
   page.
4. Choose a grant name to open the **Grant overview**
   page.
5. If presented, select an activation option for whether you want to replace
   active grants:
   1. **No** – This option will activate the
      grant without replacing any existing active grants for the recipient
      (grantee).
   2. **Yes** – This option will disable grants
      for the same product and activate a new grant for the defined
      recipient (grantee):
      1. A specified AWS account.
      2. Member accounts of the specified organization OU.
      3. All member accounts of the organization.

6. (Optional) Provide a reason for activating the grant.
7. Enter `activate` into the input box, and choose
   **Activate**.

AWS CLI
You can use the AWS CLI to work with your granted licenses.

###### To work with distributed grants using the AWS CLI:

- [accept-grant](../../../cli/latest/reference/license-manager/accept-grant.md "../../../cli/latest/reference/license-manager/accept-grant.md")
- [create-grant-version](../../../cli/latest/reference/license-manager/create-grant-version.md "../../../cli/latest/reference/license-manager/create-grant-version.md")
- [list-received-grants](../../../cli/latest/reference/license-manager/list-received-grants.md "../../../cli/latest/reference/license-manager/list-received-grants.md")
- [list-received-grants-for-organization](../../../cli/latest/reference/license-manager/list-received-grants-for-organization.md "../../../cli/latest/reference/license-manager/list-received-grants-for-organization.md")
- [reject-grant](../../../cli/latest/reference/license-manager/reject-grant.md "../../../cli/latest/reference/license-manager/reject-grant.md")
