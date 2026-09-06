

# Using tenant-level suppression lists in Amazon SES
<a name="sending-email-suppression-list-tenant-level"></a>

If you use Amazon Simple Email Service (SES) multi-tenancy to send email on behalf of multiple tenants, you can give each tenant its own suppression list. Tenant-level suppression isolates bounces and complaints so that they affect only the tenant that sent the email. Without this feature, all tenants share the account-level suppression list. When a recipient bounces or complains about one tenant's email, that address is suppressed for every tenant in the account. Tenant-level suppression prevents this cross-tenant contamination by maintaining a separate list of suppressed addresses for each tenant.

## How tenant-level suppression works
<a name="sending-email-suppression-list-tenant-level-how-it-works"></a>

Two settings control suppression behavior for each tenant: *suppression scope* and *suppressed reasons*. You configure both settings together by using the `PutTenantSuppressionAttributes` API operation, or by specifying `SuppressionAttributes` when you create a tenant with the `CreateTenant` API operation.

**Suppression scope** determines which suppression list SES uses for the tenant:
+ `TENANT` – Use the tenant's own suppression list.
+ `ACCOUNT` – Use the account-level suppression list. This is the default for both existing and new tenants.

**Suppressed reasons** determines which events cause SES to add addresses to the suppression list:
+ `BOUNCE` – Add addresses that produce hard bounces.
+ `COMPLAINT` – Add addresses that produce complaints.
+ `BOUNCE` and `COMPLAINT` – Add addresses that produce either event.
+ Empty – Don't check or record to any suppression list.

**Note**  
You must provide `SuppressionScope` and `SuppressedReasons` together, or set both to null. Setting both to null clears the tenant's suppression settings and returns the tenant to the default `ACCOUNT` scope behavior.

### Suppression behavior by configuration
<a name="sending-email-suppression-list-tenant-level-behavior-by-config"></a>

The following table describes the send-time and recording behavior for each combination of suppression scope and suppressed reasons.


| Scope | Reasons | Send-time behavior | Recording behavior | 
| --- | --- | --- | --- | 
| TENANT | BOUNCE, COMPLAINT | Checks tenant list for bounces and complaints | Records both to tenant list | 
| TENANT | BOUNCE | Checks tenant list for bounces only | Records bounces to tenant list only | 
| TENANT | COMPLAINT | Checks tenant list for complaints only | Records complaints to tenant list only | 
| TENANT | Empty | No suppression check | No recording | 
| ACCOUNT | BOUNCE, COMPLAINT | Checks account list for bounces and complaints | Records both to account list | 
| ACCOUNT | BOUNCE | Checks account list for bounces only | Records bounces to account list only | 
| ACCOUNT | COMPLAINT | Checks account list for complaints only | Records complaints to account list only | 
| ACCOUNT | Empty | No suppression check | No recording | 

## Suppression precedence and send-time behavior
<a name="sending-email-suppression-list-tenant-level-precedence"></a>

SES resolves suppression settings in the following precedence order, from highest to lowest:

1. **Configuration set** – If the configuration set specifies suppression settings, SES uses those settings.

1. **Tenant** – If no configuration set override exists, SES uses the tenant's suppression settings.

1. **Account** – If neither the configuration set nor the tenant specifies settings, SES uses the account-level defaults.

**Important**  
The suppression scope determines which suppression list SES checks at send time. When the scope is `TENANT`, SES checks only the tenant's suppression list and skips the account-level suppression list. An address that is on the account-level suppression list but not on the tenant's suppression list is not suppressed. When the scope is `ACCOUNT`, SES checks only the account-level suppression list. The scope also controls where bounces and complaints are recorded.

### Configuration set overrides
<a name="sending-email-suppression-list-tenant-level-config-set-overrides"></a>

The `SuppressionOptions` for a configuration set now includes a `SuppressionScope` field. You can use a configuration set to override the scope only, the reasons only, or both independently. This gives you fine-grained control over suppression behavior for specific sending workflows. You don't need to change the tenant's default settings.

## Automatic suppression recording
<a name="sending-email-suppression-list-tenant-level-auto-recording"></a>

When the suppression scope is `TENANT`, SES automatically records suppression entries as follows:
+ **Hard bounces** – SES adds the address to the tenant's suppression list and the global suppression list. SES does *not* add the address to the account-level suppression list.
+ **Complaints** – SES adds the address to the tenant's suppression list only.
+ **Not-spam feedback** – When a recipient marks a previously reported message as not spam, SES automatically removes `COMPLAINT`-reason entries from the tenant's suppression list.

## Identifying tenant suppression bounces
<a name="sending-email-suppression-list-tenant-level-identifying-bounces"></a>

When SES suppresses a message because the address is on a tenant's suppression list, you can identify the event by using the following indicators:
+ **Bounce notification** – The bounce type is `Permanent` with a subtype of `OnTenantSuppressionList`.
+ **Virtual Deliverability Manager (VDM)** – The bounce reason is `ON_TENANT_SUPPRESSION_LIST`.
+ **Diagnostic code** – `"Amazon SES did not send the message to this address because it is on the suppression list for your tenant."`
+ **Event tag** – SES adds a `ses:tenant-name` tag to bounce and complaint notifications so that you can identify which tenant the event belongs to.

## Managing tenant suppression list entries
<a name="sending-email-suppression-list-tenant-level-managing-entries"></a>

You manage tenant suppression list entries by using the same API operations that you use for account-level entries. To target a tenant's suppression list, include the `TenantName` parameter in your request:
+ `PutSuppressedDestination` – Add an address to a tenant's suppression list.
+ `GetSuppressedDestination` – Retrieve details about a suppressed address for a tenant.
+ `DeleteSuppressedDestination` – Remove an address from a tenant's suppression list.
+ `ListSuppressedDestinations` – List all suppressed addresses for a tenant.

If you omit the `TenantName` parameter, these operations target the account-level suppression list. This maintains backward compatibility with existing integrations.

## Considerations and limitations
<a name="sending-email-suppression-list-tenant-level-considerations"></a>

Keep the following in mind when you use tenant-level suppression lists:
+ **Multi-tenancy required** – You must have SES multi-tenancy configured with at least one tenant to use this feature.
+ **One list per tenant** – Each tenant has exactly one suppression list. There is a 1:1 mapping between tenants and suppression lists.
+ **Region-specific** – Tenant suppression lists are specific to the AWS Region in which you configure them.
+ **Addresses persist** – Suppressed addresses remain on the tenant's list until you explicitly remove them or until SES automatically removes them (for example, when a recipient reports a not-spam event for a `COMPLAINT`-reason entry).
+ **Case-sensitive storage** – Email addresses on the suppression list are stored with case preserved. API calls for suppression list management require an exact case match.
+ **Sending quota impact** – Messages suppressed by a tenant suppression list count against your daily sending quota.
+ **Gmail complaint data** – Gmail does not send complaint data to SES. Addresses hosted by Gmail are not automatically added to the suppression list for complaints.
+ **Sandbox restrictions** – You can't call `PutSuppressedDestination` until your account has production access.
+ **Clearing settings** – To clear a tenant's suppression settings, call `PutTenantSuppressionAttributes` with null values for both scope and reasons.
+ **Deleting a tenant** – When you delete a tenant, SES also deletes all suppression list entries for that tenant.

## Related resources
<a name="sending-email-suppression-list-tenant-level-related-resources"></a>

The following resources can help you learn more about suppression lists in SES.
+ [Using the Amazon SES account-level suppression list](sending-email-suppression-list.md)
+ [Amazon SES global suppression list](sending-email-global-suppression-list.md)