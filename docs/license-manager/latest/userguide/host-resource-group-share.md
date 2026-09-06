

# Share a host resource group in License Manager
<a name="host-resource-group-share"></a>

You can use AWS Resource Access Manager to share your host resource groups through AWS Organizations. After you share a host resource group, member accounts can launch instances into the shared host resource group. The new hosts are allocated in the account that owns the host resource group. The member account owns the instances. For more information, see the [AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/).

If the host resource group requires license configurations, you must also share the associated self-managed license so that member accounts can launch instances that match the licensing requirements. If the host resource group does not require license configurations, member accounts can launch instances without license associations.