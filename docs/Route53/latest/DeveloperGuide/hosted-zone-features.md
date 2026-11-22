

# Hosted zone features

A *hosted zone feature* is a capability of a hosted zone, such as Change Guardrails or Change History. A *hosted zone tier* is a bundle of features. Each tier includes different features, and some features apply only to public or only to private hosted zones. For more information about tiers, see [Hosted zone tiers](hosted-zone-tiers.md).

**Topics**
+ [Available hosted zone features](#hosted-zone-features-status)
+ [Updating optional features](#hosted-zone-features-optional)
+ [Viewing the features of a hosted zone](#hosted-zone-features-view)
+ [Viewing the change history of a hosted zone](hosted-zone-change-history.md)
+ [Change Guardrails for hosted zones](hosted-zones-change-guardrails.md)
+ [Public DNS fallback for private hosted zones](hosted-zone-private-public-dns-fallback.md)
+ [Enabling accelerated recovery for managing public DNS records](accelerated-recovery.md)

## Available hosted zone features
<a name="hosted-zone-features-status"></a>

The following table lists each feature and what it does. It also shows the tiers that offer the feature, whether it's on by default, and the hosted zone types it applies to.


**Hosted zone features by tier**  

| Feature | Description | Tiers | Default | Hosted zone types | 
| --- | --- | --- | --- | --- | 
| [Change History](hosted-zone-change-history.md) | Tracks who changed the records in the hosted zone, what they changed, and when. | ADVANCED | On; can't be turned off | Public and private | 
| [Change Guardrails](hosted-zones-change-guardrails.md) – NS\_FORMAT\_CHECK | Rejects an NS record whose value looks like a Route 53 name server but isn't one. | STANDARD, ADVANCED | On; can't be turned off | Public and private | 
| [Change Guardrails](hosted-zones-change-guardrails.md) – NS\_DELEGATION\_AUTHORITY\_CHECK | Rejects an NS record that delegates a subdomain to Route 53 name servers that aren't authoritative for it. | STANDARD, ADVANCED | On; can't be turned off | Public | 
| [Change Guardrails](hosted-zones-change-guardrails.md) – NS\_OCCLUSION\_CHECK | Rejects a record that a delegation would hide, or a delegation that would hide existing records. | STANDARD, ADVANCED | Off | Public and private | 
| [Change Guardrails](hosted-zones-change-guardrails.md) – ALIAS\_TARGET\_CHECK | Rejects deleting a record that an alias record points to. | ADVANCED | Off | Public and private | 
| [Change Guardrails](hosted-zones-change-guardrails.md) – ACTIVE\_RECORD\_CHECK | Rejects deleting a record that still receives DNS queries. | ADVANCED | Off | Public and private | 
| [Change Guardrails](hosted-zones-change-guardrails.md) – ACTIVE\_DELEGATION\_CHECK | Rejects deleting a delegation that resolvers still use. | ADVANCED | Off | Public and private | 
| [Public DNS Fallback](hosted-zone-private-public-dns-fallback.md) | Falls back to public DNS when the name doesn't exist in the private hosted zone. | ADVANCED | Off | Private | 
| [Accelerated Recovery](accelerated-recovery.md) | Lets you resume making DNS changes within about 60 minutes if the US East (N. Virginia) Region is impaired. | STANDARD, ADVANCED | Off | Public | 

## Updating optional features
<a name="hosted-zone-features-optional"></a>

You can turn optional features on or off with any of the following methods. You can also turn on optional features when you create a hosted zone. To do so, pass the same options to the `create-hosted-zone` command or the [CreateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html) API.

### Using the Route 53 console
<a name="hosted-zone-features-optional-console"></a>

**To turn optional features on or off**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**.

1. Choose the name of the hosted zone.

1. Choose **Edit features**.

1. Turn each optional feature on or off.

1. Choose **Save changes**.

### Using the AWS CLI
<a name="hosted-zone-features-optional-cli"></a>

**To turn optional features on or off**
+ Run the `update-hosted-zone-features` command. Replace {{Z11111112222222333333}} with the ID of your hosted zone. The following example turns on the `ACTIVE_RECORD_CHECK` guardrail. To turn it off, set `Status` to `DISABLED`.

  ```bash
  aws route53 update-hosted-zone-features \
      --hosted-zone-id {{Z11111112222222333333}} \
      --change-guardrails Name=ACTIVE_RECORD_CHECK,Status=ENABLED
  ```

  If the command succeeds, it returns no output. To validate the request without changing any features, add `--dry-run`.

### Using an AWS SDK
<a name="hosted-zone-features-optional-sdk"></a>

To turn optional features on or off with an AWS SDK, call the [UpdateHostedZoneFeatures](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHostedZoneFeatures.html) API. The following AWS SDK for Python (Boto3) example turns on the `ACTIVE_RECORD_CHECK` guardrail. Replace {{Z11111112222222333333}} with the ID of your hosted zone.

```python
import boto3

route53 = boto3.client("route53")

route53.update_hosted_zone_features(
    HostedZoneId="{{Z11111112222222333333}}",
    ChangeGuardrails=[
        {"Name": "ACTIVE_RECORD_CHECK", "Status": "ENABLED"}
    ],
)
```

To validate the request without changing any features, add `DryRun=True`.

### Using CloudFormation
<a name="hosted-zone-features-optional-cfn"></a>

To turn on optional features in CloudFormation, use the `HostedZoneFeatures` property. The following example template creates an `ADVANCED` tier hosted zone. It also turns on the `ACTIVE_RECORD_CHECK` guardrail.

```yaml
Resources:
  ExampleHostedZone:
    Type: AWS::Route53::HostedZone
    Properties:
      Name: {{example.org}}
      HostedZoneConfig:
        HostedZoneTier: ADVANCED
      HostedZoneFeatures:
        ChangeGuardrails:
          - Name: ACTIVE_RECORD_CHECK
            Status: ENABLED
```

In the `HostedZoneFeatures` property, you can also set `EnableAcceleratedRecovery` and `EnablePublicDNSFallback`. You can declare only the optional guardrails. For more information, see [AWS::Route53::HostedZone](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-hostedzone.html) in the *CloudFormation Template Reference Guide*.

For instructions on turning on specific features, see the following topics:
+ [Enabling and disabling guardrails for a hosted zone](hosted-zones-change-guardrails.md#change-guardrails-enable)
+ [Enabling and disabling public DNS fallback](hosted-zone-private-public-dns-fallback.md#hosted-zone-private-public-dns-fallback-enable)
+ [How to enable accelerated recovery for managing public DNS records](accelerated-recovery.md#accelerated-recovery-enable)

## Viewing the features of a hosted zone
<a name="hosted-zone-features-view"></a>

### Using the Route 53 console
<a name="hosted-zone-features-view-console"></a>

**To view the features of a hosted zone**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**.

1. Choose the name of the hosted zone.

1. In the hosted zone details, review the status of each feature.

### Using the AWS CLI
<a name="hosted-zone-features-view-cli"></a>

**To view the features of a hosted zone**
+ Run the `get-hosted-zone` command. Replace {{Z11111112222222333333}} with the ID of your hosted zone.

  ```bash
  aws route53 get-hosted-zone --id {{Z11111112222222333333}}
  ```

  The output looks similar to the following.

  ```json
  {
      "HostedZone": {
          "Id": "/hostedzone/Z11111112222222333333",
          "Name": "example.org.",
          "CallerReference": "2026-12-01-example",
          "Config": {
              "PrivateZone": false,
              "HostedZoneTier": "ADVANCED"
          },
          "ResourceRecordSetCount": 2,
          "Features": {
              "ChangeHistory": {
                  "Status": "ENABLED",
                  "RetentionStartsAt": "2026-12-01T17:48:16.751Z"
              },
              "ChangeGuardrails": [
                  {
                      "Name": "NS_FORMAT_CHECK",
                      "Status": "ENABLED"
                  },
                  {
                      "Name": "NS_DELEGATION_AUTHORITY_CHECK",
                      "Status": "ENABLED"
                  },
                  {
                      "Name": "NS_OCCLUSION_CHECK",
                      "Status": "DISABLED"
                  },
                  {
                      "Name": "ALIAS_TARGET_CHECK",
                      "Status": "DISABLED"
                  },
                  {
                      "Name": "ACTIVE_RECORD_CHECK",
                      "Status": "ENABLED"
                  },
                  {
                      "Name": "ACTIVE_DELEGATION_CHECK",
                      "Status": "DISABLED"
                  }
              ]
          }
      },
      "DelegationSet": {
          "NameServers": [
              "ns-111.awsdns-11.com",
              "ns-222.awsdns-22.net",
              "ns-1333.awsdns-33.org",
              "ns-1444.awsdns-44.co.uk"
          ]
      }
  }
  ```

  In the output, `HostedZone.Features` shows the status of each feature. For a `STANDARD` tier hosted zone, Change History and the features that only `ADVANCED` offers show `DISABLED`.

### Using an AWS SDK
<a name="hosted-zone-features-view-sdk"></a>

**To view the features of a hosted zone**
+ Call the [GetHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZone.html) API. The following AWS SDK for Python (Boto3) example prints the features of a hosted zone. Replace {{Z11111112222222333333}} with the ID of your hosted zone.

  ```python
  import boto3
  
  route53 = boto3.client("route53")
  
  response = route53.get_hosted_zone(Id="{{Z11111112222222333333}}")
  print(response["HostedZone"]["Features"])
  ```

  The `Features` object shows the status of each feature.