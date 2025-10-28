# Linux subscription settings in

License Manager

During the process of discovery, License Manager searches the EC2 instances that
are running under your AWS account for Linux subscriptions. It detects if you
have more than one Linux subscription defined for any instances, and aggregates the
data.

## Linux subscriptions settings

You can configure settings for Linux subscriptions to control how License Manager handles
discovery and aggregation. Default discovery settings apply across all types of
Linux subscriptions.

The following actions are available to configure Linux subscription discovery.

**Edit**

Change settings for Linux subscription discovery.

**Deactivate**

Deactivate discovery and aggregation for Linux subscriptions associated
with your EC2 instances. If you also have discovery activated for
Red Hat Subscription Manager, License Manager first deactivates your RHSM registered provider,
then it continues with deactivation for Linux subscription discovery.

###### Note

Deactivation doesn't affect your access secret for Red Hat Subscription Manager (RHSM).
To avoid charges on your AWS bill for an associated secret that you
no longer need, see [Delete an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/manage_delete-secret.md "../../../secretsmanager/latest/userguide/manage_delete-secret.md") in the
_AWS Secrets Manager User Guide_.

 

The following settings are displayed in the License Manager console for Linux subscription discovery.

###### Linux subscription discovery settings

_Linux subscription discovery_

Indicates whether you've activated Linux subscription discovery for
your account.

_Source AWS Regions_

AWS Regions where you want License Manager to discover subscription data.

_AWS Organizations_

Optionally aggregate subscription data across your accounts in AWS Organizations.

For more information, see [Manage Linux subscriptions in License Manager](linux-subscriptions.md "linux-subscriptions.md").

## Red Hat Subscription Manager discovery

If you've activated Linux subscription discovery, you can configure access for License Manager to
retrieve additional data for RHEL subscriptions that are managed through
Red Hat Subscription Manager (RHSM).

The following actions are available to configure your RHSM subscription discovery.

**Edit tags**

Change the tags that are associated with your access secret.

###### Note

If you need to make other changes to your RHSM subscription,
you must deactivate your current registration first, then set up
a new registration.

**Deactivate**

Deactivate your RHSM registered provider.

###### Note

Deactivation doesn't affect your access secret for Red Hat Subscription Manager (RHSM).
To avoid charges on your AWS bill for an associated secret that you
no longer need, see [Delete an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/manage_delete-secret.md "../../../secretsmanager/latest/userguide/manage_delete-secret.md") in the
_AWS Secrets Manager User Guide_.

 

The following settings are displayed in the License Manager console for RHSM discovery.

###### Red Hat Subscription Manager discovery settings

_Discovery status_

Indicates whether you've activated discovery for RHSM subscriptions.

_Secret name_

Links to the RHSM access secret in AWS Secrets Manager that contains your
Red Hat offline token. License Manager uses this secret to generate a new temporary
access token to request subscription data from Red Hat Subscription Manager (RHSM).

You can make changes to an existing secret through Secrets Manager. To update
tags or other metadata for your secret, see [Modify an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/manage_update-secret.md "../../../secretsmanager/latest/userguide/manage_update-secret.md") in the
_AWS Secrets Manager User Guide_. To update the secret value,
see [Update the value for an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/manage_update-secret-value.md "../../../secretsmanager/latest/userguide/manage_update-secret-value.md").

_Last data synchronized on_

The timestamp from the last successful update of subscription data
from the registered Red Hat Subscription Manager (RHSM) account.

_Tags_

You can define key value pairs for tags that License Manager assigns to
your RHSM access secret in Secrets Manager. To retrieve and decrypt your
RHSM access secret, the License Manager service-linked role policy
requires the secret, and any associated AWS KMS key, to have the
following tag assigned:

```
`"LicenseManagerLinuxSubscriptions": "enabled"`
```

The tag is automatically assigned if License Manager created your secret during
the registration process. If you create your own secret for the
offline token, make sure that you assign that tag to the secret and to
the associated KMS key, if it's encrypted. To add the tag,
see [Modify an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/manage_update-secret.md "../../../secretsmanager/latest/userguide/manage_update-secret.md") in the
_AWS Secrets Manager User Guide_.
