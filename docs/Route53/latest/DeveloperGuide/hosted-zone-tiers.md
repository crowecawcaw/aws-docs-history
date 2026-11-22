

# Hosted zone tiers

A *hosted zone tier* is a bundle of features that Route 53 offers together. Each public or private hosted zone can only have one tier at a time.

Route 53 offers the following tiers:
+ `STANDARD` – Includes standard Change Guardrails and Accelerated Recovery. The default tier, at no additional cost.
+ `ADVANCED` – Includes all `STANDARD` features plus additional features, at additional cost. For more information, see [Advanced hosted zones](#hosted-zone-tiers-advanced).

You can choose the tier when you create a hosted zone or change it at any time. For more information about features that each tier offers, see [Hosted zone features](hosted-zone-features.md).

**Note**  
Changing the tier doesn't affect the records in a hosted zone or how Route 53 responds to DNS queries. Features that affect DNS responses, such as Public DNS Fallback, take effect only after you turn them on.

**Topics**
+ [Advanced hosted zones](#hosted-zone-tiers-advanced)
+ [Choosing a tier when you create a hosted zone](#hosted-zone-tiers-create)
+ [Changing the tier of a hosted zone](#hosted-zone-tiers-change)
+ [Viewing the tier of a hosted zone](#hosted-zone-tiers-view)
+ [Considerations for hosted zone tiers](#hosted-zone-tiers-considerations)

## Advanced hosted zones
<a name="hosted-zone-tiers-advanced"></a>

A hosted zone that uses the `ADVANCED` tier is an *advanced hosted zone*. Advanced hosted zones help you prevent and investigate DNS changes that can take your applications offline. You can create a hosted zone with the `ADVANCED` tier, or change an existing public or private hosted zone to it.

Advanced hosted zones add the following features:
+ [Change Guardrails](hosted-zones-change-guardrails.md) that block deleting records and delegations that are still in use (`ALIAS_TARGET_CHECK`, `ACTIVE_RECORD_CHECK`, and `ACTIVE_DELEGATION_CHECK`)
+ [Change History](hosted-zone-change-history.md) that tracks who changed the records in the hosted zone, what they changed, and when
+ [Public DNS Fallback](hosted-zone-private-public-dns-fallback.md) that resolves queries against public DNS when a name doesn't exist in a private hosted zone

## Choosing a tier when you create a hosted zone
<a name="hosted-zone-tiers-create"></a>

You can specify the tier for any hosted zone. For general information about creating hosted zones, see [Creating a public hosted zone](CreatingHostedZone.md) and [Creating a private hosted zone](hosted-zone-private-creating.md).

### Using the Route 53 console
<a name="hosted-zone-tiers-create-console"></a>

**To choose a tier when you create a hosted zone**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**.

1. Choose **Create hosted zone**.

1. Enter the settings for your public or private hosted zone.

1. In the tier settings, select the tier for the hosted zone.

1. Choose **Create hosted zone**.

### Using the AWS CLI
<a name="hosted-zone-tiers-create-cli"></a>

**To choose a tier when you create a hosted zone**
+ Run the `create-hosted-zone` command. The following AWS Command Line Interface (AWS CLI) command creates a public hosted zone that uses the `ADVANCED` tier.

  ```bash
  aws route53 create-hosted-zone \
      --name {{example.org}} \
      --caller-reference {{2026-12-01-example}} \
      --hosted-zone-config HostedZoneTier=ADVANCED
  ```

### Using an AWS SDK
<a name="hosted-zone-tiers-create-sdk"></a>

**To choose a tier when you create a hosted zone**
+ Call the [CreateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html) API, and set `HostedZoneTier` in `HostedZoneConfig`. The following AWS SDK for Python (Boto3) example creates a public hosted zone that uses the `ADVANCED` tier. Replace {{example.org}} with your domain name.

  ```python
  import time
  import boto3
  
  route53 = boto3.client("route53")
  
  route53.create_hosted_zone(
      Name="{{example.org}}",
      CallerReference=str(time.time()),
      HostedZoneConfig={"HostedZoneTier": "ADVANCED"},
  )
  ```

### Using CloudFormation
<a name="hosted-zone-tiers-create-cfn"></a>

**To choose a tier when you create a hosted zone**
+ In your template, set the `HostedZoneTier` property in `HostedZoneConfig`. The following example creates a public hosted zone that uses the `ADVANCED` tier.

  ```yaml
  Resources:
    ExampleHostedZone:
      Type: AWS::Route53::HostedZone
      Properties:
        Name: {{example.org}}
        HostedZoneConfig:
          HostedZoneTier: ADVANCED
  ```

  For more information, see [AWS::Route53::HostedZone](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-hostedzone.html) in the *CloudFormation Template Reference Guide*.

## Changing the tier of a hosted zone
<a name="hosted-zone-tiers-change"></a>

You can change an existing hosted zone to any tier.

When you change a hosted zone from `ADVANCED` to `STANDARD`:
+ Before the change, you must turn off the `ADVANCED`-only optional features: `ALIAS_TARGET_CHECK`, `ACTIVE_RECORD_CHECK`, `ACTIVE_DELEGATION_CHECK`, and Public DNS Fallback. Otherwise the request fails.
+ Route 53 turns off Change History. You can no longer read the existing change history.
+ If you later change back to `ADVANCED`, Change History starts a new history. It doesn't restore the old one.
+ `NS_FORMAT_CHECK` and `NS_DELEGATION_AUTHORITY_CHECK` stay on. `NS_OCCLUSION_CHECK` and Accelerated Recovery keep their current settings.
+ Route 53 stops the additional charges for the `ADVANCED` tier.
+ Records and DNS query responses don't change.

Before you change the tier, review [Considerations for hosted zone tiers](#hosted-zone-tiers-considerations).

### Using the Route 53 console
<a name="hosted-zone-tiers-change-console"></a>

**To change the tier of a hosted zone**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**.

1. Choose the name of the hosted zone.

1. Choose the option to change the tier.

1. Select the new tier.

1. When prompted, confirm the change.

### Using the AWS CLI
<a name="hosted-zone-tiers-change-cli"></a>

**To change the tier of a hosted zone**
+ Run the `update-hosted-zone-tier` command, and set `--hosted-zone-tier` to the new tier. The following AWS CLI command changes a hosted zone to the `ADVANCED` tier. Replace {{Z11111112222222333333}} with the ID of your hosted zone.

  ```bash
  aws route53 update-hosted-zone-tier \
      --hosted-zone-id {{Z11111112222222333333}} \
      --hosted-zone-tier ADVANCED
  ```

  If the command succeeds, it returns no output. To validate the request without changing the tier, add `--dry-run`.

### Using an AWS SDK
<a name="hosted-zone-tiers-change-sdk"></a>

**To change the tier of a hosted zone**
+ Call the [UpdateHostedZoneTier](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHostedZoneTier.html) API. The following AWS SDK for Python (Boto3) example changes a hosted zone to the `ADVANCED` tier. Replace {{Z11111112222222333333}} with the ID of your hosted zone.

  ```python
  import boto3
  
  route53 = boto3.client("route53")
  
  route53.update_hosted_zone_tier(
      HostedZoneId="{{Z11111112222222333333}}",
      HostedZoneTier="ADVANCED",
  )
  ```

  To validate the request without changing the tier, add `DryRun=True`.

### Using CloudFormation
<a name="hosted-zone-tiers-change-cfn"></a>

**To change the tier of a hosted zone**
+ In your template, change the value of `HostedZoneTier` in `HostedZoneConfig`, and then update the stack. The following example changes the hosted zone to the `ADVANCED` tier.

  ```yaml
        HostedZoneConfig:
          HostedZoneTier: ADVANCED
  ```

## Viewing the tier of a hosted zone
<a name="hosted-zone-tiers-view"></a>

### Using the Route 53 console
<a name="hosted-zone-tiers-view-console"></a>

**To view the tier of a hosted zone**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**.

1. Choose the name of the hosted zone.

1. In the hosted zone details, review the tier.

### Using the AWS CLI
<a name="hosted-zone-tiers-view-cli"></a>

**To view the tier of a hosted zone**
+ Run the `get-hosted-zone` command with the `--query` option to return only the tier. Replace {{Z11111112222222333333}} with the ID of your hosted zone.

  ```bash
  aws route53 get-hosted-zone --id {{Z11111112222222333333}} --query 'HostedZone.Config.HostedZoneTier'
  ```

  The output looks similar to the following.

  ```json
  "ADVANCED"
  ```

### Using an AWS SDK
<a name="hosted-zone-tiers-view-sdk"></a>

**To view the tier of a hosted zone**
+ Call the [GetHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZone.html) API. The tier is in `HostedZone.Config.HostedZoneTier`. The following AWS SDK for Python (Boto3) example prints the tier. Replace {{Z11111112222222333333}} with the ID of your hosted zone.

  ```python
  import boto3
  
  route53 = boto3.client("route53")
  
  response = route53.get_hosted_zone(Id="{{Z11111112222222333333}}")
  print(response["HostedZone"]["Config"]["HostedZoneTier"])
  ```

## Considerations for hosted zone tiers
<a name="hosted-zone-tiers-considerations"></a>

Before you choose or change a tier, review the following:
+ Route 53 prorates the additional charges for the `ADVANCED` tier. For example, if a hosted zone uses the `ADVANCED` tier for half of a month, you pay about half of the monthly `ADVANCED` charge for that month. For more information, see [Amazon Route 53 pricing](https://aws.amazon.com/route53/pricing/).
+ You can't change the tier of a hosted zone that's associated with any Amazon CloudFront flat-rate pricing plan, including paid plans. To change the tier, first disassociate the hosted zone from the plan. For more information, see [CloudFront flat-rate plans](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.html) in the *Amazon CloudFront Developer Guide*.