# Managing configuration sets in Amazon SES

After creating a configuration set, you can manage it with the view, edit, and delete
options using the SES console, the Amazon SES API v2, and the Amazon SES CLI v2. Configuration sets
can also be assigned to a verified identity as its default configuration set that is applied
every time email is sent from the identity.

###### Topics in this section:

- [View, edit, & delete
  configuration set (console)](#console-detail-configuration-sets "#console-detail-configuration-sets")
- [List configuration sets (AWS CLI)](#cli-list-configuration-sets "#cli-list-configuration-sets")
- [Get configuration set details
  (AWS CLI)](#cli-get-configuration-set "#cli-get-configuration-set")
- [Delete a configuration set
  (AWS CLI)](#cli-delete-configuration-set "#cli-delete-configuration-set")
- [Stop sending email from a
  configuration set (AWS CLI)](#cli-configuration-set-stop-sending "#cli-configuration-set-stop-sending")
- [Understanding default configuration sets](#default-config-sets "#default-config-sets")
- [Creating Amazon SES event destinations](event-destinations-manage.md "event-destinations-manage.md")
- [Assigning IP pools in Amazon SES](managing-ip-pools.md "managing-ip-pools.md")
- [Configuring custom domains to handle
  open and click tracking](configure-custom-open-click-domains.md "configure-custom-open-click-domains.md")

## View, edit, & delete

configuration set (console)

###### Access an existing configuration set's

detail page

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the navigation pane, under **Configuration**, choose
   **Configuration sets**.
3. Select a **Name** from the configuration set list to open its
   details page in the **Overview** tab where you can view, edit,
   or disable the options you've selected. The same can be done for
   **Events destination** options by selecting its tab. For
   more information about each option and their fields, see the related section in
   [Create a configuration set
   (console)](creating-configuration-sets.md#config-sets-create-console "creating-configuration-sets.md#config-sets-create-console").
4. At the top of each configuration set's details page, visible from either the
   **Overview** or **Events destination**
   tab, are the following options:
   - Delete – this button will delete
     your configuration set.
   - Disable sending – this button
     will stop sending emails from your configuration set.

## List configuration sets (AWS CLI)

You can use the **list-configuration-sets** command in the AWS CLI to
generate a list of all the configuration sets associated with your account in the
current Region, as follows:

```
`aws sesv2 list-configuration-sets`
```

## Get configuration set details

(AWS CLI)

You can use the **get-configuration-set** command in the AWS CLI to get
details for a specific configuration set, as follows:

```
`aws sesv2 get-configuration-set --configuration-set-name `name``
```

## Delete a configuration set

(AWS CLI)

You can use the **delete-configuration-set** command in the AWS CLI to
delete a specific configuration set, as follows:

```
`aws sesv2 delete-configuration-set --configuration-set-name `name``
```

## Stop sending email from a

configuration set (AWS CLI)

You can use the **put-configuration-set-sending-options** command in
the AWS CLI to stop sending email from a specific configuration set, as follows:

```
`aws sesv2 put-configuration-set-sending-options --configuration-set-name `name` --no-sending-enabled`
```

To start sending again, run the same command with the `--sending-enabled`
option instead, as follows:

```
`aws sesv2 put-configuration-set-sending-options --configuration-set-name `name` --sending-enabled`
```

## Understanding default configuration sets

The concept of assigning a configuration set as the default to be used by a verified
identity is explained in this section to help understand the benefits and use
case.

A default configuration set automatically applies its rules to all messages that you
send from the email identity associated with that configuration set. You can apply
default configuration sets to both email address and domain identities during the
creation of the identity or after the fact as an edit function of an existing
identity.

**Default configuration set considerations**

- The configuration set must be created first before associating it with an
  identity.
- Default configuration sets will only be applied if the identity is
  verified.
- An email identity can be associated with only one configuration set at a time.
  However, you can apply the same configuration set to multiple identities.
- A default configuration set at the email address level overrides a default
  configuration set at the domain level. For example, a default configuration set
  associated with *joe@example.com* overrides the configuration
  set for the domain of _example.com_.
- A default configuration set at the domain level applies to all email addresses
  for that domain (unless you verify specific addresses for the domain).
- If you delete a configuration set that's designated as the default
  configuration set for an identity, and then attempt to send email through that
  identity, your call to Amazon SES fails with a "bad request" error.
- A default configuration set cannot be assigned to a verified identity that's
  being used by a [delegate
  sender](sending-authorization-overview.md "sending-authorization-overview.md").
- How to specify an existing configuration set to be used as the identity's
  default configuration set is actually a function of verified identities, so
  instructions are given in the identity workflows accordingly:
  - Specify a default configuration set during
    identity creation – follow the instructions given in
    the optional Step 6 for either [Domain
    identity default configuration set](creating-identities.md#verified-domain-identity-default-config-set "creating-identities.md#verified-domain-identity-default-config-set") or [Email identity
    default configuration set](creating-identities.md#verified-email-identity-default-config-set "creating-identities.md#verified-email-identity-default-config-set") located in the [Creating and verifying identities in Amazon SES](creating-identities.md "creating-identities.md")
    chapter.
  - Specify a default configuration set for an
    existing identity – follow the steps in [Edit an identity using the
    console](edit-verified-domain.md "edit-verified-domain.md") along with these
    details for Step 5:
    1. Choose the **Configuration set** tab.
    2. Choose **Edit** in the **Default
       configuration set** container.
    3. Select the list box and choose an existing configuration set
       to be used as the
       default.
    4. Continue with the remaining steps in [Edit an identity using the
       console](edit-verified-domain.md "edit-verified-domain.md").

###### Note

If the configuration set you assign as a default has reputation metrics enabled,
additional charges will be incurred for any mail sent using the default
configuration set, see [Price per metric for
CloudWatch](event-publishing-add-event-destination-cloudwatch.md#cw-add-pricing "event-publishing-add-event-destination-cloudwatch.md#cw-add-pricing").
