# Include Process Checks Within a

Conformance Pack

1. Add a process check in the conformance pack template. Refer to [Sample
   Conformance Pack Template for Creating Process Checks](Sample-CPack-Template-for-Creating-Process-Check-Rule.md "Sample-CPack-Template-for-Creating-Process-Check-Rule.md").

```
Resources:
  ConfigEnabledAllRegions:
    Properties:
      ConfigRuleName: Config-Enabled-All-Regions
      Description: Ensure AWS Config is enabled in all Regions.
      Source:
        Owner: AWS
        SourceIdentifier: AWS_CONFIG_PROCESS_CHECK
    Type: AWS::Config::ConfigRule
```

2. Enter the name for the process check.
3. Enter the description for the process check.
4. Deploy the conformance pack. For more
   information, see [Deploying Conformance Packs for AWS Config](conformance-pack-deploy.md "conformance-pack-deploy.md").
