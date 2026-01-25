# When the service fails to connect

to Amazon RDS or downstream service

There may be a network configuration issue with your service if it fails to connect to an
Amazon RDS database or other downstream application or service. This topic walks you through some
steps to determine if there are any issues with your network configuration and the options to
correct them. To learn more about outbound traffic configuration for App Runner, see [Enabling VPC access for outgoing traffic](network-vpc.md "network-vpc.md") .

###### Note

To view your VPC Connector configuration, from the App Runner console left navigation pane, select **Network configuration**.
Then select the **Outgoing traffic** tab. Select a VPC Connector. The next page displays details about the VPC Connector.
From this page you can view and drill down into the following: **Subnets**, **Security groups**,
and **App Runner services** that use the VPC.

###### To narrow down the cause of your application’s inability to connect to another downstream

service

1. Ensure that the subnets used in the VPC Connectors are private subnets. If a connector
   is configured with a public subnet your service will encounter errors, because the
   underlying Hyperplane ENIs (elastic network interfaces) for each subnet don’t have a public
   IP space.

If your VPC connectors are using public subnets, you have the following options to
correct this configuration:

    1. Create a new private subnet, and use it instead of the public subnet for the VPC
     Connector. For more information, see [Subnets for your VPC](../../../vpc/latest/userguide/configure-subnets.md "../../../vpc/latest/userguide/configure-subnets.md") in the
     Amazon VPC User Guide.
    2. Route the existing public subnet via NAT gateways. For more information see [NAT
     gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the Amazon VPC User Guide.

2. Verify that the security group ingress and egress rules for the VPC Connector are correct. From the App Runner console left navigation pane, select
   **Network configuration** > **Outgoing traffic**. Select the VPC Connector from the list.
   The next page lists the **Security groups** that you can select to inspect.
3. Verify that the security group inbound and outbound rules are correct for the RDS
   instance or other downstream service that you’re attempting connection to. For more
   information, see the service guide for the downstream service to which your App Runner application
   is trying to connect.
4. To confirm that there isn’t some other type of network setup issue outside of your App Runner configurations, try connecting to the RDS or downstream
   service outside of App Runner:
   1. From an Amazon EC2 instance in the same VPC, try connecting to the RDS instance or
      service.
   2. If you’re trying to connect to a service VPC endpoint, verify connectivity by
      accessing the same endpoint from an EC2 instance in the same VPC.

5. If either of the connection tests in _Step 4_ fail, more than likely there’s an issue outside of your App Runner
   configurations with another resource in your AWSaccount. Contact AWS Support for assistance to further isolate and fix the issue with your other
   network configurations.
6. If you successfully connect to the RDS instance or downstream service by doing the
   instructions in _Step 4_, then proceed with the instructions in this
   step. We’ll check if traffic is entering the ENI by enabling and inspecting the Hyperplane
   ENI flow logs.

###### Note

To be able to complete these steps and obtain the required ENI flow log information,
the connection attempt to the RDS or downstream service must occur after your App Runner service
has started up successfully. Your application must perform the connect operation to the
RDS or downstream service when it’s in a Running state. Otherwise, the ENIs could be
cleaned up as part of App Runner's rollback workflows. This approach ensures that the ENIs
remain available for further investigation.

    1. From the AWS console, launch the EC2 console.
    2. From the left navigation pane, in the **Network &
     Security** grouping, select **Network
     Interfaces**.
    3. Scroll over to the **Interface Type** and **Description** columns to locate the ENIs in the subnets
     associated with the VPC Connector. They will have the following naming patterns.




    	* **Interface Type:**
    	*fargate*
    	* **Description:**  begins with
    	 *AWSAppRunner ENI* (example:
    	 *AWSAppRunner ENI -
    	 abcde123-abcd-1234-1234-abcde1233456*)
    4. Use the check boxes at the beginning of the rows to select the ENIs that
     apply.
    5. From the **Actions** menu select **Create flow log**.
    6. Enter the information in the prompts and select **Create flow
     flog** at the bottom of the page.
    7. Inspect the generated flow log.




    	* If traffic was entering the ENI when you were testing the connection, then the
    	 issue is not related to the ENI setup. There may be network configuration issues
    	 with another resource in your AWS Account besides App Runner services. Contact AWS
    	 Support for further assistance.
    	* If traffic was not entering the ENI when you were testing the connection, we
    	 advise that you contact AWS Support to see if there are any known issues with the
    	 Fargate service.
    8. Use the network *Reachability Analyzer* tool. This
     tool helps determine network misconfigurations by identifying blocking components when a
     source in the virtual network path isn't reachable. For more information, see [What is Reachability Analyzer?](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md") in the *Amazon VPC Reachability Analyzer
     Guide*.


    Enter the App Runner ENI as the source, and the RDS ENI as the destination.

7. If you're unable to narrow down the issue further, or if you’re still unable to connect to the RDS or downstream service after completing the prior
   steps, we advise that you contact AWS Support for further assistance.
