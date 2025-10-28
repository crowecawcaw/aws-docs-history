# Configure AWS Global Accelerator (AGA) for WorkSpaces Personal

You can enable AWS Global Accelerator (AGA) either at the WorkSpaces directory level or for
individual WorkSpaces running DCV protocol. When enabled, the service automatically routes
the streaming traffic through the nearest AWS edge location and across the AWS global
network, which is congestion-free and redundant. This helps deliver a more responsive and
stable streaming experience. The WorkSpaces service fully manages AGA usage and is subject to
outbound data volume limits.

###### Contents

- [Requirements](#configure-aga-requirements "#configure-aga-requirements")
- [Limitations](#configure-aga-limitations "#configure-aga-limitations")
- [Outbound data limits](#configure-aga-outbound-data-limits "#configure-aga-outbound-data-limits")
- [Enable AGA for a WorkSpaces directory](#enabling-aga-directory "#enabling-aga-directory")
- [Enable AGA for individual WorkSpaces](#enabling-aga-individual "#enabling-aga-individual")

## Requirements

- WorkSpaces use a range of public IPv4 addresses for the dedicated AWS Global Accelerator
  (AGA) endpoints. Make sure to configure your firewall policies for devices that access WorkSpaces through AGA.
  If the AGA endpoints are blocked by the firewall, WorkSpaces streaming traffic won't be routed through AGA.
  For more information about the AGA endpoint IP ranges in each AWS region, see [DCV gateway servers](workspaces-port-requirements.md#gateway_WSP "workspaces-port-requirements.md#gateway_WSP").
- To access WorkSpaces through AGA, users must use WorkSpaces client versions 5.23 or later.

## Limitations

- You can enable AGA for DCV WorkSpaces only. If you enable AGA at WorkSpaces directory level,
  it will only apply to the DCV WorkSpaces in the directory.
- You can't enable AGA for a directory (or the WorkSpaces in the directory) that has both
  FIPS and IP access control groups enabled. You must disable FIPS or IP access control groups before
  enabling AGA for the directory.

## Outbound data limits

The following are applicable data volume limits for WorkSpaces bundles.

- **Value, Standard, and Performance bundles:** Includes 20 GB of AGA outbound data per user per month.
- **Power, PowerPro, and Graphics bundles:** Includes 50 GB of AGA outbound data per user per month.

These outbound data limits are intended to cover the data usage of users streaming from their WorkSpaces.
Beyond the limits, the WorkSpaces service might restrict AGA usage and route WorkSpaces traffic off of
AGA on a case-by-case basis.

## Enable AGA for a WorkSpaces directory

You can configure AGA settings on a directory level. The settings will apply to all the DCV WorkSpaces
in the directory unless overridden by the individual WorkSpaces.

###### To enable AGA for a directory

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Under the **Directory ID** column, choose the directory ID of the directory you want to configure AGA settings for.
4. On the Directory Details page, scroll down to the AWS Global Accelerator (AGA) configuration section and choose **Edit**.
5. Choose **Enable AGA (automatic)**.
6. **Always use TCP with AGA** is selected by default. If you unselect it, your WorkSpaces client will determine
   whether TCP or UDP is used with AGA based on the DCV streaming protocol settings on your clients.
7. Choose **Save**.

After you enable AGA for a WorkSpaces directory, DCV WorkSpaces in the directory use AGA for streaming starting from the next session. No reboot is needed.

## Enable AGA for individual WorkSpaces

You can configure AGA settings for individual WorkSpaces, which overrides the settings inherited from the directory that the WorkSpaces are associated with.

###### To enable AGA for individual WorkSpaces

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **WorkSpaces**, **Personal**.
3. Under the **WorkSpace ID** column, choose the WorkSpace ID of the WorkSpace you want to configure AGA settings for.
4. On the WorkSpaces Details page, scroll down to the AWS Global Accelerator (AGA) configuration section and choose **Edit**.
5. Choose **Manually override AGA configurations for this WorkSpace**.
6. Choose **Enable AGA (automatic)**.
7. **Always use TCP with AGA** is selected by default. If you unselect it, your WorkSpaces client will determine whether TCP or UDP is used with AGA based on the DCV streaming protocol settings on your clients.
8. Choose **Save**.
