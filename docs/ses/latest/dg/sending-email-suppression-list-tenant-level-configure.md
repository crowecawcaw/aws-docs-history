

# Configuring tenant-level suppression
<a name="sending-email-suppression-list-tenant-level-configure"></a>

Configure tenant-level suppression settings to control how Amazon Simple Email Service (Amazon SES) handles bounces and complaints for individual tenants. By default, tenants use your account-level suppression list. When you enable tenant-level suppression, SES maintains a separate suppression list for each tenant. This gives you granular control over email deliverability.

This topic provides procedures for enabling, modifying, disabling, and viewing tenant-level suppression settings by using the AWS CLI.

**Important**  
Disabling tenant-level suppression does not delete existing entries from the tenant's suppression list. If you re-enable tenant-level suppression later, those entries are still active.

## Prerequisites
<a name="configuring-tenant-suppression-prerequisites"></a>

Before you configure tenant-level suppression, make sure that you meet the following requirements:
+ Multi-tenancy is enabled in your SES account.
+ At least one tenant exists in your account, or you plan to create one as part of this procedure.
+ AWS CLI version 2 is installed and configured with appropriate permissions. For more information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).
+ You are familiar with account-level suppression concepts. For more information, see [Using the Amazon SES account-level suppression list](sending-email-suppression-list.md).

## Enabling tenant-level suppression for an existing tenant
<a name="enable-tenant-suppression"></a>

Use the `PutTenantSuppressionAttributes` API operation to enable tenant-level suppression for an existing tenant. This operation is idempotent, so you can call it multiple times with the same parameters without side effects.

**To enable tenant-level suppression**

1. At the command line, run the following `put-tenant-suppression-attributes` command to enable tenant-level suppression for both bounces and complaints:

------
#### [ Linux, macOS, or Unix ]

   ```
   aws sesv2 put-tenant-suppression-attributes \
   --tenant-name {{MyTenant}} \
   --suppression-scope TENANT \
   --suppressed-reasons BOUNCE COMPLAINT
   ```

------
#### [ Windows ]

   ```
   aws sesv2 put-tenant-suppression-attributes `
   --tenant-name {{MyTenant}} `
   --suppression-scope TENANT `
   --suppressed-reasons BOUNCE COMPLAINT
   ```

------

   Replace {{MyTenant}} with the name of your tenant.

1. Verify that the command returns no output. A successful request returns an HTTP 200 response with no body.

1. Confirm the configuration by running the following command:

   ```
   aws sesv2 get-tenant --tenant-name {{MyTenant}}
   ```

The tenant now uses its own suppression list for both bounces and complaints.

You can also configure suppression for a single reason type. The following examples show how to enable suppression for bounces only or complaints only.

The following command suppresses bounces only:

------
#### [ Linux, macOS, or Unix ]

```
aws sesv2 put-tenant-suppression-attributes \
--tenant-name {{MyTenant}} \
--suppression-scope TENANT \
--suppressed-reasons BOUNCE
```

------
#### [ Windows ]

```
aws sesv2 put-tenant-suppression-attributes `
--tenant-name {{MyTenant}} `
--suppression-scope TENANT `
--suppressed-reasons BOUNCE
```

------

The following command suppresses complaints only:

------
#### [ Linux, macOS, or Unix ]

```
aws sesv2 put-tenant-suppression-attributes \
--tenant-name {{MyTenant}} \
--suppression-scope TENANT \
--suppressed-reasons COMPLAINT
```

------
#### [ Windows ]

```
aws sesv2 put-tenant-suppression-attributes `
--tenant-name {{MyTenant}} `
--suppression-scope TENANT `
--suppressed-reasons COMPLAINT
```

------

**Note**  
You must provide `--suppression-scope` and `--suppressed-reasons` together. Providing one without the other returns an `InvalidParameterValueException`.

## Configuring suppression when creating a new tenant
<a name="create-tenant-with-suppression"></a>

Use the `CreateTenant` API operation with the `SuppressionAttributes` parameter to create a tenant with tenant-level suppression enabled from the start.

**To create a tenant with tenant-level suppression**

1. At the command line, run the following `create-tenant` command:

------
#### [ Linux, macOS, or Unix ]

   ```
   aws sesv2 create-tenant \
   --tenant-name {{MyNewTenant}} \
   --suppression-attributes '{"SuppressionScope":"TENANT","SuppressedReasons":["BOUNCE","COMPLAINT"]}'
   ```

------
#### [ Windows ]

   ```
   aws sesv2 create-tenant `
   --tenant-name {{MyNewTenant}} `
   --suppression-attributes '{"SuppressionScope":"TENANT","SuppressedReasons":["BOUNCE","COMPLAINT"]}'
   ```

------

   Replace {{MyNewTenant}} with the name for your new tenant.

1. Verify that the response contains the tenant ID:

   ```
   {
       "TenantId": "tn-abc123def456"
   }
   ```

The tenant is created with tenant-level suppression enabled for both bounces and complaints.

**Note**  
If you omit `--suppression-attributes`, the tenant defaults to `ACCOUNT` scope and uses the account-level suppression list.

## Overriding tenant suppression with a configuration set
<a name="override-tenant-suppression-config-set"></a>

You can override a tenant's suppression settings by adding `SuppressionScope` to a configuration set's `SuppressionOptions`. When you send email using this configuration set, the configuration set's suppression settings take precedence over the tenant's settings. You can override scope only, reasons only, or both independently.

**To create a configuration set with tenant scope override**

1. At the command line, run the following `create-configuration-set` command:

------
#### [ Linux, macOS, or Unix ]

   ```
   aws sesv2 create-configuration-set \
   --configuration-set-name {{my-config-set}} \
   --suppression-options '{"SuppressionScope":"TENANT","SuppressedReasons":["BOUNCE"]}'
   ```

------
#### [ Windows ]

   ```
   aws sesv2 create-configuration-set `
   --configuration-set-name {{my-config-set}} `
   --suppression-options '{"SuppressionScope":"TENANT","SuppressedReasons":["BOUNCE"]}'
   ```

------

   Replace {{my-config-set}} with the name for your configuration set.

1. Verify that the command returns no output. A successful request returns an HTTP 200 response.

**To update an existing configuration set with suppression options**

1. At the command line, run the following `put-configuration-set-suppression-options` command:

------
#### [ Linux, macOS, or Unix ]

   ```
   aws sesv2 put-configuration-set-suppression-options \
   --configuration-set-name {{my-config-set}} \
   --suppression-scope TENANT \
   --suppressed-reasons BOUNCE
   ```

------
#### [ Windows ]

   ```
   aws sesv2 put-configuration-set-suppression-options `
   --configuration-set-name {{my-config-set}} `
   --suppression-scope TENANT `
   --suppressed-reasons BOUNCE
   ```

------

   Replace {{my-config-set}} with the name of your configuration set.

1. Verify that the command returns no output. A successful request returns an HTTP 200 response.

## Disabling tenant-level suppression
<a name="disable-tenant-suppression"></a>

To return a tenant to account-level suppression, you can either set the scope to `ACCOUNT` or clear all suppression settings.

**To set the tenant to account-level suppression**

1. At the command line, run the following command to explicitly set the scope to `ACCOUNT`:

------
#### [ Linux, macOS, or Unix ]

   ```
   aws sesv2 put-tenant-suppression-attributes \
   --tenant-name {{MyTenant}} \
   --suppression-scope ACCOUNT \
   --suppressed-reasons BOUNCE COMPLAINT
   ```

------
#### [ Windows ]

   ```
   aws sesv2 put-tenant-suppression-attributes `
   --tenant-name {{MyTenant}} `
   --suppression-scope ACCOUNT `
   --suppressed-reasons BOUNCE COMPLAINT
   ```

------

   Replace {{MyTenant}} with the name of your tenant.

1. Verify that the command returns no output.

**To clear all suppression settings**

1. At the command line, run the following command without specifying scope or reasons:

   ```
   aws sesv2 put-tenant-suppression-attributes --tenant-name {{MyTenant}}
   ```

   Replace {{MyTenant}} with the name of your tenant.

1. Verify that the command returns no output.

**Note**  
When you omit both `--suppression-scope` and `--suppressed-reasons`, SES clears the tenant's suppression settings. The tenant falls back to account-level suppression behavior.

**Important**  
Disabling tenant-level suppression does not delete existing entries from the tenant's suppression list. If you re-enable tenant-level suppression later, those entries are still active.

## Viewing current suppression configuration
<a name="view-tenant-suppression"></a>

Use the `GetTenant` API operation to check a tenant's current suppression settings.

**To view a tenant's suppression configuration**

1. At the command line, run the following `get-tenant` command:

   ```
   aws sesv2 get-tenant --tenant-name {{MyTenant}}
   ```

   Replace {{MyTenant}} with the name of your tenant.

1. Review the response. The following example shows a tenant with tenant-level suppression enabled:

   ```
   {
       "Tenant": {
           "TenantName": "MyTenant",
           "TenantId": "tn-abc123def456",
           "TenantArn": "arn:aws:ses:us-east-1:123456789012:tenant/MyTenant/tn-abc123def456",
           "SendingStatus": "ENABLED",
           "CreatedTimestamp": 1705312800,
           "UpdateTimestamp": 1705762800,
           "SuppressionAttributes": {
               "SuppressionScope": "TENANT",
               "SuppressedReasons": ["BOUNCE", "COMPLAINT"]
           }
       }
   }
   ```

The following table describes the key fields in the `SuppressionAttributes` object.


| Field | Description | 
| --- | --- | 
| SuppressionScope | The suppression scope for the tenant. A value of TENANT means the tenant uses its own suppression list. A value of ACCOUNT means the tenant uses the account-level suppression list. | 
| SuppressedReasons | The suppression reasons that are active for the tenant. Possible values are BOUNCE, COMPLAINT, or both. | 

If `SuppressionAttributes` is absent or null in the response, the tenant uses account-level suppression.

## Troubleshooting
<a name="troubleshooting-tenant-suppression"></a>

The following are common errors that you might encounter when configuring tenant-level suppression.

`InvalidParameterValueException: SuppressedReasons cannot be null when SuppressionScope is provided`  
+ **Cause** – You specified `--suppression-scope` without `--suppressed-reasons`.
+ **Fix** – Provide both parameters together, or omit both to clear settings.

`InvalidParameterValueException: SuppressionScope is required when SuppressedReasons are provided`  
+ **Cause** – You specified `--suppressed-reasons` without `--suppression-scope`.
+ **Fix** – Provide both parameters together.

`NotFoundException`  
+ **Cause** – The tenant name that you specified doesn't exist.
+ **Fix** – Verify the tenant name by running the following command:

  ```
  aws sesv2 list-tenants
  ```

## Related resources
<a name="related-resources-tenant-suppression"></a>
+ [Using tenant-level suppression lists in Amazon SES](sending-email-suppression-list-tenant-level.md)
+ [Managing tenant suppression list entries](sending-email-suppression-list-tenant-level-manage.md)
+ [Using the Amazon SES account-level suppression list](sending-email-suppression-list.md)
+ [Tenants](tenants.md)