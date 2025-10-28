# Update your landing zone

When a new landing zone version is available, or to make other updates to your landing zone configuration, you can call the `UpdateLandingZone`
API and reference an updated landing zone manifest file. This API returns an `OperationIdentifier`, which you can then use when calling the `GetLandingZoneOperation`
API to check the update operation's status.

**To update the landing zone**

1. Call the AWS Control Tower `UpdateLandingZone` API and refer to the updated **landing zone version** or your **updated landing zone manifest file**.

```
aws controltower update-landing-zone --landing-zone-version 3.3 --landing-zone-identifier "arn:aws:controltower:us-west-2:123456789123:landingzone/1A2B3C4D5E6F7G8H" --manifest file://LandingZoneManifest.json
```

**Example LandingZoneManifest.json** file, with Regions and centralized logging:

```
{
   "governedRegions": ["us-west-2","us-west-1"],
   "organizationStructure": {
       "security": {
           "name": "Security"
       },
       "sandbox": {
           "name": "Sandbox"
       }
   },
   "centralizedLogging": {
        "accountId": "`LOG ARCHIVE ACCOUNT ID`",
        "configurations": {
            "loggingBucket": {
                "retentionDays":2555
            },
            "accessLoggingBucket": {
                "retentionDays": 2555
            },
            "kmsKeyArn": "arn:aws:kms:us-west-1:123456789123:key/e84XXXXX-6bXX-49XX-9eXX-ecfXXXXXXXXX"
        },
        "enabled": true
   },
   "securityRoles": {
        "accountId": "`SECURITY ACCOUNT ID`"
   },
   "accessManagement": {
        "enabled": true
   }
}
```

**Output**:

```
{
   "operationIdentifier": "55XXXXXX-e2XX-41XX-a7XX-446XXXXXXXXX"
}
```

###### Optionally Re-register OU to update accounts

For registered AWS Control Tower OUs with fewer than 1000 accounts, you can use the
AWS Control Tower console access the **OU page** in the dashboard and select **Re-register
OU** to update the accounts in that OU.
