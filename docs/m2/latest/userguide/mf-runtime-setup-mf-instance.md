AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Launch an AWS Mainframe Modernization Rocket Software (formerly Micro Focus)

instance

After creating endpoints, IAM policy, IAM role, and subscribing to AMIs, you are ready
to launch an AWS Mainframe Modernization Rocket Software (Micro Focus) instance in the AWS Management Console.

1. Navigate to AWS Marketplace Subscriptions in the AWS Management Console.
2. Locate the AMI to be launched and choose **Launch New Instance**.

![Manage subscriptions with Enterprise Server and Enterprise Analyzer ready to launch.](images/mf-launch-instance_1.png) 3. In the launch new instance dialog, ensure the allowlisted region is selected. 4. Press **Continue to launch through EC2**.

###### Note

The following example shows a launch of an Enterprise Developer AMI, but the process is the same for all the AWS Mainframe Modernization AMIs.

![Launch new instance.](images/mf-launch-instance_2.png) 5. Enter a name for the server. 6. Choose an instance type.

The Instance type selected should be determined by the project performance and cost requirements.
The following are suggested starting points:

    * For Enterprise Analyzer, an r6i.xlarge
    * For Enterprise Developer, an r6i.large
    * For a standalone instance of Enterprise Server, an r6i.xlarge
    * For Rocket Software Performance Availability Cluster (PAC) with scale-out, an r6i.large


    ###### Note

    The Application and OS Images section has been collapsed for the screen shot.



    ![Launch an instance with name and instance type entered.](images/mf-launch-instance_3.png)

7. Choose or create (and save) a key-pair (not shown).

For more information on key pairs for Linux instances, see [Amazon EC2 key pairs and Linux instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").

For more information on key pairs for Windows instances, see [Amazon EC2 key pairs and Windows instances](../../../AWSEC2/latest/WindowsGuide/ec2-key-pairs.md "../../../AWSEC2/latest/WindowsGuide/ec2-key-pairs.md"). 8. Edit the Network settings and **choose the allowlisted VPC** and appropriate Subnet. 9. **Choose or create a Security Group**. If this is an Enterprise Server
EC2 instance it is typical to allow TCP traffic to ports 86 and 10086 to administer the Rocket Software
configuration. 10. Optionally configure the storage for the Amazon EC2 instance. 11. Important - Expand Advanced details and under IAM instance profile choose the Licensing role created earlier, for example “Micro-Focus-Licensing-role”.

###### Note

If this step is missed, after the instance is created you can modify the IAM role from the Security option of the Action menu for the EC2 instance.

![Advanced Details with IAM instance profile entered.](images/mf-launch-instance_4.png) 12. Review the Summary and push **Launch Instance**.

![Summary with selected options.](images/mf-launch-instance_5.png) 13. The instance launch will fail if an invalid virtual server type is chosen.

If this happens, choose **Edit instance config** and change the instance type.

![Launching instance progress message.](images/mf-launch-instance_6.png) 14. Once the “Success” message is shown choose **Connect to instance** to get connection details.

![Instance launch success message.](images/mf-launch-instance_7.png) 15. Alternatively, navigate to **EC2** in the AWS Management Console. 16. Choose **Instances** to see the status of the new instance.

![List of instances with status.](images/mf-launch-instance_8.png)
