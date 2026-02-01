• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Tutorial: Patching a

server in an IPv6 only environment

Patch Manager supports the patching of nodes in environments that only have IPv6. By
updating the SSM Agent configuration, patching operations can be configured to only
make calls to IPv6 service endpoints.

###### To patch a server in an IPv6 only environment

1.  Ensure that SSM Agent version 3.3270.0 or later is installed on the managed
    node.
2.  On the managed node, navigate to the SSM Agent configuration file. You can
    find the `amazon-ssm-agent.json` file in the following
    directories:

        * Linux: `/etc/amazon/ssm/`
        * macOS: `/opt/aws/ssm/`
        * Windows Server: `C:\Program Files\Amazon\SSM`

    If `amazon-ssm-agent.json` doesn't exist yet, copy the
    contents of `amazon-ssm-agent.json.template` under the
    same directory to `amazon-ssm-agent.json`.

3.  Update the following entry to set the correct Region and set
    `UseDualStackEndpoint` to `true`:

```
{
 --------
    "Agent": {
        "Region": "region",
        "UseDualStackEndpoint": true
    },
--------
}
```

4.  Restart the SSM Agent service using the appropriate command for your
    operating system:

        * Linux: `sudo systemctl restart amazon-ssm-agent`
        * Ubuntu Server using Snap: `sudo snap restart
         amazon-ssm-agent`
        * macOS: `sudo launchctl stop com.amazon.aws.ssm`
         followed by `sudo launchctl start
         com.amazon.aws.ssm`
        * Windows Server: `Stop-Service AmazonSSMAgent` followed by
         `Start-Service AmazonSSMAgent`

    For the full list of commands per operating system, see [Checking SSM Agent status and starting the
    agent](ssm-agent-status-and-restart.md "ssm-agent-status-and-restart.md").

5.  Execute any patching operation to verify patching operations succeed in
    your IPv6-only environment. Ensure that the nodes being patched have
    connectivity to the patch source. You can check the Run Command output from the
    patching execution to check for warnings about inaccessible repositories.
    When patching a node that is running in an IPv6 only environment, ensure
    that the node has connectivity to the patch source. You can check the
    Run Command output from the patching execution to check for warnings about
    inaccessible repositories. For DNF-based operating systems, it is possible
    to configure unavailable repositories to be skipped during patching if the
    `skip_if_unavailable` option is set to `True`
    under `/etc/dnf/dnf.conf`. DNF-based operating systems
    include Amazon Linux 2023, Red Hat Enterprise Linux 8 and later versions, Oracle Linux 8 and
    later versions, Rocky Linux, AlmaLinux, & CentOS 8 and later versions. On
    Amazon Linux 2023, the `skip_if_unavailable` option is set to
    `True` by default.

###### Note

When using the Install Override List or Baseline Override features,
ensure that the provided URL is reachable from the node. If the SSM Agent
config option `UseDualStackEndpoint` is set to
`true`, then a dualstack S3 client is used when an S3 URL
is provided.
