

# Monitor environment status

You can monitor the status of your Amazon Elastic VMware Service environment and its underlying AWS resources with the Amazon EVS console or the AWS CLI. The environment status tells you whether the environment has issues that need your attention. Which status checks Amazon EVS runs depends on the deployment mode and on the connectors that you create.

**Note**  
You monitor VMware Cloud Foundation (VCF) components with VCF tools, not with the Amazon EVS console or AWS CLI.

In EVS-deployed environments (VCF 5.2.x), you use SDDC Manager. For more information, see [Getting started with SDDC Manager](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/getting-started-with-sddc-manager-admin.html) in the Broadcom documentation. For how AWS monitoring compares with VCF Operations, see [Monitor hosts and VCF](monitor-observability.md).

## Environment status checks
<a name="evs-env-status-checks-ref"></a>

The environment status is one of `PASSED`, `FAILED`, or `UNKNOWN`. Each check also reports `PASSED`, `FAILED`, or `UNKNOWN`, and a failed check shows when the impairment began.

The following table lists the checks. The columns show the check type and what it verifies. Connector checks apply only after you create a connector of that type.


| Check type | What it verifies | 
| --- | --- | 
|  `KEY_REUSE`  | The VCF license key is not used by another Amazon EVS environment. | 
|  `KEY_COVERAGE`  | The VCF license key allocates enough vCPU cores for all deployed hosts. | 
|  `REACHABILITY`  | The Amazon EVS control plane has a persistent connection to SDDC Manager. | 
|  `HOST_COUNT`  | The environment meets the minimum host count. | 
|  `SDDC_MANAGER_REACHABILITY`  | Amazon EVS reaches SDDC Manager through the SDDC Manager connector. | 
|  `SDDC_MANAGER_HOST_COUNT`  | The host count that SDDC Manager reports meets the Amazon EVS minimum. | 
|  `SDDC_MANAGER_KEY_COVERAGE`  | The VCF license key in SDDC Manager covers all deployed hosts. | 
|  `SDDC_MANAGER_KEY_REUSE`  | The VCF license key in SDDC Manager is not used by another Amazon EVS environment. | 
|  `OPERATIONS_MANAGER_REACHABILITY`  | Amazon EVS reaches VCF Operations through the Operations Manager connector. | 
|  `VCENTER_REACHABILITY`  | Amazon EVS reaches vCenter Server through the vCenter connector. | 
|  `VCENTER_VM_SYNC`  | The vCenter connector can synchronize the VM inventory from vCenter Server. | 
|  `VCENTER_VM_EVENT`  | The vCenter connector can receive VM lifecycle events from vCenter Server. | 
|  `CONNECTOR_HEALTH`  | The combined health of all connectors in the environment. | 

The SDDC Manager connector applies to VCF 5.2.x, and the Operations Manager connector applies to VCF 9.0 and 9.1. For the connector types, see [Manage connectors and credentials](connectors-overview.md). For the definitions of the check types, see [Check](https://docs.aws.amazon.com/evs/latest/APIReference/API_Check.html) in the *Amazon Elastic VMware Service API Reference*.

In a Self-deployed environment that has no connector, the environment status can show `UNKNOWN` with no check results. After you create a connector and its state is `ACTIVE`, its reachability check changes from `UNKNOWN` to `PASSED` or `FAILED` within 10 minutes. For more information, see [Step 6: Create connectors](self-deployed-create-connectors.md).

## View environment status and resources
<a name="evs-env-view-status"></a>

To check your environment status and view the underlying resources in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Choose your environment ID to open the environment details page.

1. Under **Details**, view the **Environment status**.

   If your environment is healthy, the status shows as **Passed**. If there are issues, the status shows as **Failed**. When the status is **Failed**, open the popover to see the result of each check.

1. To view the resources in your environment, choose one of the following tabs.
   +  **Hosts** shows the hosts in your environment.
   +  **Networks & connectivity** shows the VPC, Amazon EVS VLAN subnets, and VPC Route Server resources of your environment.
   +  **Management appliances** shows the VCF management appliances in your environment with their DNS host names and related credentials.
   +  **Connectors** shows the connectors of your environment, their state, and their reachability check result.
   +  **Tags** shows the tags of your environment.

1. To list all environments with their state and status, run the following command.

   ```bash
   aws evs list-environments \
       --query 'environmentSummaries[*].[environmentId,environmentState,environmentStatus]' \
       --output table
   ```

1. To view the status and check results of one environment, run the following command.

   ```bash
   aws evs get-environment \
       --environment-id env-abcde12345 \
       --query 'environment.[environmentStatus,checks]'
   ```

1. To list the hosts of the environment, run the following command.

   ```bash
   aws evs list-environment-hosts \
       --environment-id env-abcde12345
   ```

1. To list the VLANs of the environment, run the following command.

   ```bash
   aws evs list-environment-vlans \
       --environment-id env-abcde12345
   ```

1. To list the connectors of the environment with their state and reachability check result, run the following command.

   ```bash
   aws evs list-environment-connectors \
       --environment-id env-abcde12345
   ```

For more information about the API operations, see [ListEnvironments](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListEnvironments.html), [GetEnvironment](https://docs.aws.amazon.com/evs/latest/APIReference/API_GetEnvironment.html), [ListEnvironmentHosts](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListEnvironmentHosts.html), and [ListEnvironmentVlans](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListEnvironmentVlans.html) in the *Amazon Elastic VMware Service API Reference*.

You have viewed the status, the check results, and the resources of your environment. If a check fails, see [Troubleshoot environment status checks](troubleshoot-status-checks.md). To get notified when Amazon EVS reports impaired environment health, see [Get notified about host events](monitor-notifications.md).