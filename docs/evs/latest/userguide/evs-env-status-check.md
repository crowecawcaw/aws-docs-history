# Monitor your environment's status and resources

You can monitor various aspects of your Amazon EVS environment and underlying AWS resources using the Amazon EVS console or AWS CLI.

###### Note

VMware Cloud Foundation (VCF) components are monitored in SDDC Manager.
You cannot monitor VCF components using the Amazon EVS console or AWS CLI.
For information about using SDDC Manager to monitor VMware Cloud Foundation (VCF) components, see [Getting started with SDDC Manager](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/getting-started-with-sddc-manager-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/getting-started-with-sddc-manager-admin.html").

## View environment status and resources

The environment status helps you determine if your environment is experiencing issues that require attention.
Follow this procedure to check your environment’s status and view underlying resources.

Amazon EVS console

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs "https://console.aws.amazon.com/evs").
2. In the navigation pane, choose **Environments**.
3. Choose your environment ID to open the environment details page.
4. Under **Details**, view the **Environment status**.

If your environment is healthy, the status shows as **Passed**.
If there are issues, the status shows as **Failed**.
When the status is **Failed**, you can view a popover that shows the results of four environment status checks:

    * **Key re-use** - Shows **Passed** or **Failed** to indicate if the VCF license key is valid.
    * **Host count** - Shows **Unknown**, **Passed**, or **Failed** to indicate the status of host connectivity.
    * **Key coverage** - Shows **Passed** or **Failed** to indicate if the VCF license key covers all hosts.
    * **Reachability** - Shows **Passed** or **Failed** to indicate reachability to SDDC Manager.


    For information about troubleshooting environment status check failures, see [Troubleshooting](troubleshooting.md "troubleshooting.md").



    **To view the resources in your environment**



    Choose one of the following tabs:
    * **Hosts** - Shows the hosts in your environment.
    * **Networks & connectivity** - Shows the VPC, EVS subnets, and VPC Route Server resources associated with your environment.
    * **Management appliances** - Shows the VCF management appliances in your environment with their DNS hostnames and related credentials.
    * **Tags** - Shows the tags associated with your environment.

AWS CLI

You can use the AWS CLI to check your environment status and resources.

**To list all environments and their status**

```
aws evs list-environments
```

###### Tip

Use the `--query` parameter to filter the output. For example:

```
aws evs list-environments --query 'Environments[*].[EnvironmentId,Status]'
```

**To list environment hosts**

```
aws evs list-environment-hosts \
    --environment-id environment-id
```

**To list environment VLANs**

```
aws evs list-environment-vlans \
    --environment-id environment-id
```

For more information about the API operations, see the following in the _Amazon EVS API Reference Guide_:

- [ListEnvironments](../APIReference/API_ListEnvironments.md "../APIReference/API_ListEnvironments.md")
- [ListEnvironmentHosts](../APIReference/API_ListEnvironmentHosts.md "../APIReference/API_ListEnvironmentHosts.md")
- [ListEnvironmentVlans](../APIReference/API_ListEnvironmentVlans.md "../APIReference/API_ListEnvironmentVlans.md")
