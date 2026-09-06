

# Enabling accelerated recovery for managing public DNS records
<a name="accelerated-recovery"></a>

Route 53 accelerated recovery for managing public DNS records helps you achieve a 60-minute Recovery Time Objective (RTO) if the US East (N. Virginia) Region becomes unavailable. When you turn on this feature for a Route 53 public hosted zone, you can resume making DNS changes within about 60 minutes after AWS detects that the US East (N. Virginia) Region is impaired.

**Important**  
Accelerated recovery is available only for public hosted zones. Private hosted zones are not supported.

**Note**  
DNS query resolution from the Route 53 data plane continues to work normally during Regional service impairment. See [Resilience in Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/disaster-recovery-resiliency.html) for an understanding of data plane versus control plane operations.

**Topics**
+ [How accelerated recovery for public DNS records works](#accelerated-recovery-how-it-works)
+ [Resubmitting DNS changes after failover](#accelerated-recovery-resubmit)
+ [Failback to the US East (N. Virginia) Region](#accelerated-recovery-failback)
+ [Additional considerations](#accelerated-recovery-considerations)
+ [How to enable accelerated recovery for managing public DNS records](#accelerated-recovery-enable)

## How accelerated recovery for public DNS records works
<a name="accelerated-recovery-how-it-works"></a>

When accelerated recovery is on, Route 53 keeps a copy of your public hosted zone in the US West (Oregon) Region. If the US East (N. Virginia) Region becomes unavailable for a long time, Route 53 fails over within 60 minutes. It then routes control plane requests for your enabled hosted zones to the US West (Oregon) Region. You can then keep making DNS changes through the CLI, SDK, and API. Note that only some API methods work during failover. See the "Additional considerations" section for details. When the Region recovers, Route 53 fails back to the US East (N. Virginia) Region.

**Note**  
You must turn on accelerated recovery before any issues with the US East (N. Virginia) Region occur. You can do this through the Console, CLI, SDK, or API (see the section titled *How to enable accelerated recovery for managing public DNS records* below). You cannot turn on accelerated recovery after a failover starts.

## Resubmitting DNS changes after failover
<a name="accelerated-recovery-resubmit"></a>

Under normal conditions, changes to public hosted zones with accelerated recovery are accepted by the US East (N. Virginia) Region and then copied to the US West (Oregon) Region. However, when an outage occurs in the US East (N. Virginia) Region, some changes might be accepted there but not yet copied to the US West (Oregon) Region. These in-flight changes are called "stranded changes". After failover finishes, Route 53 suggests that you resubmit stranded changes before you continue your DNS work. You can do this with the API or with AWS CloudFormation, as described below.

### Using the API to track and submit DNS changes
<a name="accelerated-recovery-api"></a>

If you use the Route 53 API, AWS CLI, or AWS SDKs to manage DNS records, use the [ChangeResourceRecordSets API](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html) to submit changes and the [GetChange API](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) to track them.

When you call ChangeResourceRecordSets, Route 53 returns an ID for the change (see [ChangeInfo](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeInfo.html) for details). You can then pass this ID to GetChange to check the status. A status of INSYNC means the change was copied to the US West (Oregon) Region and sent to all Route 53 DNS servers. You don't need to do anything more for these changes. However, during an outage in the US East (N. Virginia) Region, GetChange might return PENDING, meaning the change might not have been copied. If that happens, after failover finishes, GetChange returns NoSuchChange. This means Route 53 could not copy that change. You can safely ignore these stranded changes and resubmit them as new changes. The failover is done when Route 53 posts a message to the AWS Health Dashboard.

### Using AWS CloudFormation to track and submit changes
<a name="accelerated-recovery-cloudformation"></a>

AWS CloudFormation tracks status for your DNS changes using the GetChange API. It only marks an update as done after changes are INSYNC. If the US East (N. Virginia) Region becomes unavailable while you are using CloudFormation to manage DNS records, your actions won't finish during the outage. After the Route 53 failover is done, retry the same actions to let CloudFormation resubmit the DNS changes.

## Failback to the US East (N. Virginia) Region
<a name="accelerated-recovery-failback"></a>

Route 53 fails back control plane work for your public hosted zone to the US East (N. Virginia) Region after that Region recovers. During failback, you don't need to resubmit DNS changes, because no stranded changes are created during this process.

## Additional considerations
<a name="accelerated-recovery-considerations"></a>

There are a few more things to know about the accelerated recovery feature:

1. You can't create new hosted zones, delete hosted zones, turn on DNSSEC signing, or turn off DNSSEC signing during failover.

1. AWS PrivateLink links won't work after failover, but will work again after failback to the US East (N. Virginia) Region.

1. [CloudFront flat-rate plans](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.html) are not supported at this time.

1. Hosted zones with accelerated recovery can't be deleted. You must turn off accelerated recovery before you can delete the hosted zone.

1. During failover, these API methods will still work for public hosted zones with accelerated recovery. All other Route 53 API methods won't work until failback.
   + `ChangeResourceRecordSets`
   + `GetChange`
   + `GetGeoLocation`
   + `GetHostedZone`
   + `GetHostedZoneCount`
   + `GetHostedZoneLimit`
   + `GetReusableDelegationSet`
   + `GetReusableDelegationSetLimit`
   + `ListGeoLocations`
   + `ListHostedZones`
   + `ListHostedZonesByName`
   + `ListResourceRecordSets`
   + `ListReusableDelegationSets`

## How to enable accelerated recovery for managing public DNS records
<a name="accelerated-recovery-enable"></a>

You can turn on accelerated recovery using the Route 53 console, API, CLI, or SDK. The time it takes depends on the size of your hosted zone and other factors. Plan for the process to take up to several hours. You can check the status in the Accelerated recovery tab of your hosted zone or through the `GetHostedZone` API. Near the end of the process, there is a brief period of up to several minutes where DNS changes are not accepted. After this, DNS changes work as normal.

**To enable and disable accelerated recovery using the Route 53 console**

1. Open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**.

1. Choose the public hosted zone for which you want to enable accelerated recovery.

1. In the **Accelerated recovery** tab, choose **Enable**.

1. Choose **Save changes**.

1. Monitor the hosted zone status. The status shows **Enabling accelerated recovery** during setup and changes to **Enabled** when complete.

You can disable accelerated recovery using the same steps above, but instead choosing **Disable**.

**CLI example to enable**

```
aws route53 update-hosted-zone-features --enable-accelerated-recovery --hosted-zone-id Z123456789
```

**CLI example to disable**

```
aws route53 update-hosted-zone-features --no-enable-accelerated-recovery --hosted-zone-id Z123456789
```