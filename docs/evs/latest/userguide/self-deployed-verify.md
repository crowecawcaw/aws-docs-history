

# Step 7: Verify the environment

After you have added hosts, installed VMware Cloud Foundation (VCF), configured NSX networking, and created at least one connector, verify that the environment works. You can check the Amazon Elastic VMware Service resources with the Amazon EVS console or the AWS CLI. These checks apply to hosts with local storage and to diskless hosts.

## Check the hosts and connectors
<a name="self-deployed-verify-evs"></a>

To check the hosts and connectors, do the following.

1. Confirm that your hosts are in the `CREATED` state. In the Amazon EVS console, choose **Environments**, choose your environment, and then choose the **Hosts** tab. You can also run `aws evs list-environment-hosts --environment-id <environment-id>`.

1. Confirm that the connectors that you created are in the `ACTIVE` state and that their reachability checks are `PASSED`. In the Amazon EVS console, choose the **Connectors** tab. You can also run `aws evs list-environment-connectors --environment-id <environment-id>`.

1. If you created an Operations Manager connector, confirm that its `OPERATIONS_MANAGER_REACHABILITY` check shows `PASSED`. The **Environment status** of a Self-deployed environment can show `UNKNOWN`. For what this means and how to read connector health, see [Monitor environment status](evs-env-status-check.md).

## Check the VCF appliances and connectivity
<a name="self-deployed-verify-vcf"></a>

To check the VCF appliances and connectivity, do the following.

1. Confirm that your VCF management appliances, such as vCenter Server, NSX Manager, SDDC Manager, and VCF Operations, are reachable from the management VLAN.

1. In NSX Manager, confirm that the Border Gateway Protocol (BGP) neighbors of the Tier-0 gateway show status **Established**.

1. In the Amazon VPC console, confirm that NSX overlay routes appear in the Amazon VPC Route Server routes. For instructions, see [Verify BGP peering](self-deployed-nsx-edge.md#sd-nsx-verify).

For diskless hosts, also complete the storage and cluster checks in [Step 4b (diskless): Create the specification and deploy](deploy-diskless-spec.md).

You have verified the environment. If a check fails, see [Troubleshoot Self-deployed deployments](troubleshoot-self-deployed.md).

Next step: To migrate your workloads to the environment, see [Migrate workloads with HCX](migrate-evs-hcx.md).