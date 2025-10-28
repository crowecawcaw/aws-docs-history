# Reset the landing zone to resolve drift

When you create your landing zone, the landing zone and all the organizational units (OUs), accounts, and resources
are compliant with the governance rules enforced by your chosen controls. As you and your organization members use the
landing zone, changes in this compliance status may occur. These changes are called _drift_.

To identify if your landing zone is in drift, you can call the `GetLandingZone` API. This API returns
the landing zone's **drift status** of `DRIFTED` or `IN_SYNC`.

To resolve drift within your landing zone you can use the `ResetLandingZone` API to reset the landing zone back to its original configuration.
For example, AWS Control Tower enables IAM Identity Center by default to help you manage your AWS accounts-- but if you configure your
original landing zone parameters with IAM Identity Center disabled, calling `ResetLandingZone` maintains that disabled IAM Identity Center configuration.

You can only use the `ResetLandingZone` API if you are using the latest available landing zone version. You can call the
`GetLandingZone` API and compare your landing zone version with the **latest available version**. If necessary,
you can [Update your landing zone](lz-api-update.md "lz-api-update.md") so your landing zone uses the latest available version. In these examples, we are using version 3.3 as the latest version.

1. Call the `GetLandingZone` API. If the API returns a **drift status** of
   `DRIFTED`, your landing zone is in drift.
2. Call the `ResetLandingZone` API to reset your landing zone to its original configuration.

```
aws controltower reset-landing-zone --landing-zone-identifier "arn:aws:controltower:us-west-2:123456789123:landingzone/1A2B3C4D5E6F7G8H"
```

**Output**:

```
{
   "operationIdentifier": "55XXXXXX-e2XX-41XX-a7XX-446XXXXXXXXX"
}
```

###### Note

Resetting the landing zone does not update the landing zone version. Review [Update your landing zone](lz-api-update.md "lz-api-update.md")  
 for details about updating the landing zone version.
