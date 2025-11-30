# Enabling accelerated recovery for managing public DNS records

Route 53 accelerated recovery for managing public DNS records is designed to achieve a 60-minute Recovery Time Objective (RTO) in the event of service unavailability in the US East (N. Virginia) Region. When enabled on a Route 53 public hosted zone, you will be able to resume making changes to DNS records in the public hosted zone within approximately 60 minutes after AWS detects that operations in the US East (N. Virginia) Region are impaired.

###### Important

Accelerated recovery is available only for public hosted zones. Private hosted zones are not supported.

###### Note

DNS query resolution from the Route 53 data plane continues to work normally during Regional service impairment. See [Resilience in Route 53](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md") for an understanding of data plane versus control plane operations.

###### Topics

- [How accelerated recovery for public DNS records works](#accelerated-recovery-how-it-works "#accelerated-recovery-how-it-works")
- [Resubmitting DNS changes after failover](#accelerated-recovery-resubmit "#accelerated-recovery-resubmit")
- [Failback to the US East (N. Virginia) Region](#accelerated-recovery-failback "#accelerated-recovery-failback")
- [Additional considerations](#accelerated-recovery-considerations "#accelerated-recovery-considerations")
- [How to enable accelerated recovery for managing public DNS records](#accelerated-recovery-enable "#accelerated-recovery-enable")

## How accelerated recovery for public DNS records works

When accelerated recovery is enabled, Route 53 will maintain a copy of your public hosted zone in the US West (Oregon) Region. If services in the US East (N. Virginia) Region become unavailable for an extended period, Route 53 will execute failover within 60 minutes, automatically redirecting control plane operations for your accelerated recovery enabled public hosted zones to the US West (Oregon) Region. You can then continue to make DNS changes programmatically via the CLI, SDK, and API. Note that a limited set of API methods will be available during failover. See the "Additional considerations" section for more details. When the region recovers, Route 53 will execute the failback procedure, automatically directing control plane operations back to the US East (N. Virginia) Region.

###### Note

Before any impairment to US East (N. Virginia) Region occurs, you must first enable accelerated recovery for managing public DNS records on your public hosted zone. This can be done via the Console, CLI, SDK, or API (see the section titled _How to enable accelerated recovery for managing public DNS records_ on this page below). You cannot enable accelerated recovery for managing public DNS records after a failover occurs.

## Resubmitting DNS changes after failover

Under normal conditions, changes to public hosted zones with accelerated recovery enabled will be accepted by the US East (N. Virginia) Region and will then be successfully replicated to the US West (Oregon) Region. However, when service disruption occurs in the US East (N. Virginia) Region, some changes may be accepted by the US East (N. Virginia) Region, but may not be replicated to the US West (Oregon) Region. These in-flight changes are referred to as "stranded changes". Once failover completes, Route 53 recommends that you resubmit stranded changes before resuming your DNS workflows. You can achieve this either by using the API, or by using AWS CloudFormation, which are described below.

### Using the API to track and submit DNS changes

If you are using the Route 53 API, AWS CLI, or AWS SDKs to manage DNS records, then you will need to use the [ChangeResourceRecordSets API](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md") and the [GetChange API](../APIReference/API_GetChange.md "../APIReference/API_GetChange.md") to submit and track DNS changes, respectively.

When you use the ChangeResourceRecordSets API to make DNS changes, Route 53 returns an identifier (ID) for the change you made (see [ChangeInfo](../APIReference/API_ChangeInfo.md "../APIReference/API_ChangeInfo.md") for change response object details). You can provide this ID in a subsequent request to the GetChange API and observe the status of the change. DNS changes with INSYNC status have been replicated to the US West (Oregon) Region and propagated to all Route 53 DNS servers. There are no further actions you need to take on these changes before or after a failover. However, during impairment to the US East (N. Virginia) Region, GetChange may return PENDING, indicating your change may not have replicated to the US West (Oregon) Region. If that's the case, when failover completes, GetChange will return NoSuchChange, indicating that Route 53 could not replicate this DNS change. Therefore, after failover you can safely disregard these stranded DNS changes and resubmit them as new DNS changes. You will know the failover process has completed when Route 53 posts a message to the AWS Health Dashboard.

### Using AWS CloudFormation to track and submit changes

AWS CloudFormation automatically tracks replication status for your DNS changes utilizing the GetChange API, and only completes an update after DNS changes are confirmed as INSYNC. If you are using CloudFormation to manage DNS records and the US East (N. Virginia) Region becomes unavailable, then the actions you take using CloudFormation will not complete successfully during the period of unavailability. However, you can simply retry the same actions to allow CloudFormation to resubmit DNS changes, once the Route 53 failover process completes.

## Failback to the US East (N. Virginia) Region

Route 53 will fail back control plane operations for your public hosted zone to the US East (N. Virginia) Region once the region recovers. During the failback, you will not need to resubmit your DNS changes, as no stranded changes will be introduced during this process.

## Additional considerations

There are a few additional considerations to be aware of related to the accelerated recovery feature:

1. You will not be able to create new hosted zones, delete existing hosted zones, enable DNSSEC signing, or disable DNSSEC signing during failover.
2. AWS PrivateLink connections will not work after failover, but will work once again after a failback to the US East (N. Virginia) Region.
3. [CloudFront flat-rate plans](../../../AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.md "../../../AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.md") are not supported at this time.
4. Hosted zones with accelerated recovery enabled cannot be deleted. You must disable accelerated recovery before attempting to delete the hosted zone.
5. During failover, the following API methods will continue to be supported for public hosted zones with accelerated recovery enabled. However, all other Route 53 API methods will not be functional until a failback occurs.
   - `ChangeResourceRecordSets`
   - `GetChange`
   - `GetGeoLocation`
   - `GetHostedZone`
   - `GetHostedZoneCount`
   - `GetHostedZoneLimit`
   - `GetReusableDelegationSet`
   - `GetReusableDelegationSetLimit`
   - `ListGeoLocations`
   - `ListHostedZones`
   - `ListHostedZonesByName`
   - `ListResourceRecordSets`
   - `ListReusableDelegationSets`

## How to enable accelerated recovery for managing public DNS records

You can enable accelerated recovery for managing public DNS records using the Route 53 console, API, CLI, or SDK. The time it takes to enable accelerated recovery will depend on the size of your public hosted zone and other factors. You should plan for the process of enabling accelerated recovery to take up to several hours. You can check on the status of the enablement process in the Accelerated recovery tab of your public hosted zone or via the `GetHostedZone` API. As the process finalizes, there will be a brief period of time lasting up to several minutes where DNS changes are not accepted. Once completed, DNS changes can proceed as normal.

###### To enable and disable accelerated recovery using the Route 53 console

1. Open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Hosted zones**.
3. Choose the public hosted zone for which you want to enable accelerated recovery.
4. In the **Accelerated recovery** tab, choose **Enable**.
5. Choose **Save changes**.
6. Monitor the hosted zone status. The status shows **Enabling accelerated recovery** during setup and changes to **Enabled** when complete.

You can disable accelerated recovery using the same steps above, but instead choosing **Disable**.

CLI example to enable

```
aws route53 update-hosted-zone-features --enable-accelerated-recovery --hosted-zone-id Z123456789
```

CLI example to disable

```
aws route53 update-hosted-zone-features --no-enable-accelerated-recovery --hosted-zone-id Z123456789
```
