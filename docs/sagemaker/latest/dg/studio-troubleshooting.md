# Troubleshooting Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

This topic describes how to troubleshoot common Amazon SageMaker Studio Classic issues during setup and
use. The following are common errors that might occur while using Amazon SageMaker Studio Classic. Each error
is followed by its solution.

## Studio Classic application issues

The following issues occur when launching and using the Studio Classic
application.

- Screen not loading: Clearing workspace and waiting doesn't help

When launching the Studio Classic application, a pop-up displays the following
message. No matter which option is selected, Studio Classic does not load.

```
Loading...
The loading screen is taking a long time. Would you like to clear the workspace or keep waiting?
```

The Studio Classic application can have a launch delay if multiple tabs are open
in the Studio Classic workspace or several files are on Amazon EFS. This pop-up should
disappear in a few seconds after the Studio Classic workspace is ready.

If you continue to see a loading screen with a spinner after selecting either
of the options, there could be connectivity issues with the Amazon Virtual Private Cloud used by
Studio Classic. 

To resolve connectivity issues with the Amazon Virtual Private Cloud (Amazon VPC) used by Studio Classic,
verify the following networking configurations:

    + If your domain is set up in `VpcOnly` mode: Verify that
     there is an Amazon VPC endpoint for AWS STS, or a NAT Gateway for outbound
     traffic, including traffic over the internet. To do this, follow the
     steps in [Connect Studio notebooks in
     a VPC to external resources](studio-notebooks-and-internet-access.md "studio-notebooks-and-internet-access.md").
    + If your Amazon VPC is set up with a custom DNS instead of the DNS provided
     by Amazon: Verify that the routes are configured using Dynamic Host
     Configuration Protocol (DHCP) for each Amazon VPC endpoint added to the Amazon VPC
     used by Studio Classic. For more information about setting default and
     custom DHCP option sets, see [DHCP option sets in
     Amazon VPC](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md").

- **Internal Failure** when launching
  Studio Classic

When launching Studio Classic, you are unable to view the Studio Classic UI. You also
see an error similar to the following, with **Internal
Failure** as the error detail.

```
Amazon SageMaker Studio
The JupyterServer app default encountered a problem and was stopped.
```

This error can be caused by multiple factors. If completion of these steps
does not resolve your issue, create an issue with https://aws.amazon.com/premiumsupport/. 

    + Missing Amazon EFS mount target: Studio Classic uses Amazon EFS for storage.
     The Amazon EFS volume needs a mount target for each subnet that the Amazon SageMaker AI
     domain is created in. If this Amazon EFS mount target is deleted
     accidentally, the Studio Classic application cannot load because it cannot
     mount the user’s file directory. To resolve this issue, complete the
     following steps.


    ######  To verify or create mount targets.


    	1. Find the Amazon EFS volume that is associated with the domain by
    	 using the [DescribeDomain](../APIReference/API_DescribeDomain.md "../APIReference/API_DescribeDomain.md") API call.
    	2. Sign in to the AWS Management Console and open the Amazon EFS console at
    	 [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
    	3. From the list of Amazon EFS volumes, select the Amazon EFS volume that
    	 is associated with the domain.
    	4. On the Amazon EFS details page, select the
    	 **Network** tab. Verify that there are
    	 mount targets for all of the subnets that the domain is set up
    	 in.
    	5. If mount targets are missing, add the missing Amazon EFS mount
    	 targets. For instructions, see [Creating and managing
    	 mount targets and security groups](../../../efs/latest/ug/accessing-fs.md "../../../efs/latest/ug/accessing-fs.md").
    	6. After the missing mount targets are created, launch the
    	 Studio Classic application.
    + Conflicting files in the user’s
     `.local` folder: If you're using JupyterLab
     version 1 on Studio Classic, conflicting libraries in
     your `.local` folder can cause issues when launching the
     Studio Classic application. To resolve this, update your user profile's
     default JupyterLab version to JupyterLab 3.0. For more information about
     viewing and updating the JupyterLab version, see [JupyterLab Versioning in Amazon SageMaker Studio Classic](studio-jl.md "studio-jl.md").

- **ConfigurationError: LifecycleConfig**
  when launching Studio Classic

You can't view the Studio Classic UI when launching Studio Classic. This is caused by
issues with the default lifecycle configuration script attached to the
domain.

###### To resolve lifecycle configuration issues

    1. View the Amazon CloudWatch Logs for the lifecycle configuration to trace the
     command that caused the failure. To view the log, follow the steps
     in [Verify lifecycle configuration process from
     CloudWatch Logs](studio-lcc-debug.md#studio-lcc-debug-logs "studio-lcc-debug.md#studio-lcc-debug-logs").
    2. Detach the default script from the user profile or domain. For more
     information, see [Update and Detach Lifecycle Configurations in Amazon SageMaker Studio Classic](studio-lcc-delete.md "studio-lcc-delete.md").
    3. Launch the Studio Classic application.
    4. Debug your lifecycle configuration script. You can run the lifecycle
     configuration script from the system terminal to troubleshoot. When the
     script runs successfully from the terminal, you can attach the script to
     the user profile or the domain.

- SageMaker Studio Classic core functionalities are not
  available.

If you get this error message when opening Studio Classic, it may be due to Python
package version conflicts. This occurs if you used the following commands in a
notebook or terminal to install Python packages that have version conflicts with
SageMaker AI package dependencies.

```
!pip install
```

```
pip install --user
```

To resolve this issue, complete the following steps:

    1. Uninstall recently installed Python packages. If you’re not sure which
     package to uninstall, create an issue with https://aws.amazon.com/premiumsupport/.
    2. Restart Studio Classic:




    	1. Shut down Studio Classic from the **File**
    	 menu.
    	2. Wait for one minute.
    	3. Reopen Studio Classic by refreshing the page or opening it from
    	 the AWS Management Console.

The problem should be resolved if you have uninstalled the package which caused
the conflict. To install packages without causing this issue again, use `%pip
 install` without the `--user` flag.

If the issue persists, create a new user profile and set up your environment with
that user profile.

If these solutions don't fix the issue, create an issue with
https://aws.amazon.com/premiumsupport/.

- Unable to open Studio Classic from the
  AWS Management Console.

If you are unable to open Studio Classic and cannot make a new running instance
with all default settings, create an issue with https://aws.amazon.com/premiumsupport/.

## KernelGateway application issues

The following issues are specific to KernelGateway applications that are launched in
Studio Classic.

- Cannot access the Kernel session

When the user launches a new notebook, they are unable to connect to the
notebook session. If the KernelGateway application's status is `In
 Service`, you can verify the following to resolve the issue.

    + Check Security Group configurations


    If the domain is set up in `VPCOnly` mode, the security
     group associated with the domain must allow traffic between the ports in
     the range `8192-65535` for connectivity between the
     JupyterServer and KernelGateway apps.


    ###### To verify the security group rules


    	1. Get the security groups associated with the domain using the
    	 [DescribeDomain](../APIReference/API_DescribeDomain.md "../APIReference/API_DescribeDomain.md")
    	 API call.
    	2. Sign in to the AWS Management Console and open the Amazon VPC console at
    	 [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
    	3. From the left navigation, under **Security**,
    	 choose **Security Groups**.
    	4. Filter by the IDs of the security groups that are associated
    	 with the domain.
    	5. For each security group:



    		1. Select the security group.
    		2. From the security group details page, view
    		 the **Inbound rules**. Verify that
    		 traffic is allowed between ports in the range
    		 `8192-65535`.
    For more information about security group rules, see [Control traffic to resources using security groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md#working-with-security-group-rules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#working-with-security-group-rules"). For
     more information about requirements to use Studio Classic in
     `VPCOnly` mode, see [Connect Studio notebooks in
     a VPC to external resources](studio-notebooks-and-internet-access.md "studio-notebooks-and-internet-access.md").
    + Verify firewall and WebSocket
     connections


    If the KernelGateway apps have an `InService` status and
     the user is unable to connect to the Studio Classic notebook session, verify
     the firewall and WebSocket settings.



    	1. Launch the Studio Classic application. For more information, see
    	 [Launch Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
    	2. Open your web browser’s developer tools.
    	3. Choose the **Network** tab.
    	4. Search for an entry that matches the following format.



    	```
    	wss://<domain-id>.studio.<region>.sagemaker.aws/jupyter/default/api/kernels/<unique-code>/channels?session_id=<unique-code>
    	```

    	If the status or response code for the entry is
    	 anything other than `101`, then your network settings
    	 are preventing the connection between the Studio Classic application
    	 and the KernelGateway apps.


    	To resolve this issue, contact the team that manages your
    	 networking settings to allow list the Studio Classic URL and enable
    	 WebSocket connections.

- Unable to launch an app caused by exceeded resource
  quotas

When a user tries to launch a new notebook, the notebook creation fails with
either of the following errors. This is caused by exceeding resource quotas.

    + ```
    Unable to start more Apps of AppType [KernelGateway] and ResourceSpec(instanceType=[]) for UserProfile []. Please delete an App with a matching AppType and ResourceSpec, then try again
    ```

    Studio Classic supports up to four running KernelGateway apps on the same
     instance. To resolve this issue, you can do either of the following:




    	- Delete an existing KernelGateway application running on the instance, then restart the new
    	 notebook.
    	- Start the new notebook on a different instance type
     For more information, see [Change the Instance
     Type for an Amazon SageMaker Studio Classic Notebook](notebooks-run-and-manage-switch-instance-type.md "notebooks-run-and-manage-switch-instance-type.md").
    + ```
    An error occurred (ResourceLimitExceeded) when calling the CreateApp operation
    ```

    In this case, the account does not have sufficient limits to create a
     Studio Classic application on the specified instance type. To resolve this,
     navigate to the Service Quotas console at
     [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). In that console, request to increase the `Studio
     KernelGateway Apps running on
     `instance-type` instance` limit.
     For more information, see [AWS service
     quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").
