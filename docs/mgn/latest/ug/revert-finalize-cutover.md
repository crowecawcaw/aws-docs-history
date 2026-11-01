

# Reverting a cutover
<a name="revert-finalize-cutover"></a>

Once you have launched your cutover instances, open the Amazon EC2 console and SSH or RDP into your cutover instances to ensure that they function correctly. Validate connectivity and perform acceptance tests for your application. 

**Note**  
Enabling termination protection on your test instances can prevent AWS Transform MGN from cleaning up those instances when you're done with them. If you want to use termination protection for your cutover instances, you can either enable the `DisableApiTermination` attribute in the Amazon EC2 launch template before you launch the cutover instance, or enable termination protection on the running cutover instance after you launch it. For more information, see [Change instance termination protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_ChangingDisableAPITermination.html) in the *Amazon EC2 User Guide*.

If you encounter any issues and want to launch new cutover instances, you can revert the cutover. This reverts your source servers' **Migration lifecycle** status to **Ready for cutover**, indicating that these servers have not undergone cutover. During a revert, you also have the option to delete your Cutover instances for cost-saving purposes.

To revert a cutover take the following steps:

1. Check the box to the left of every source server that has a launched cutover instance you want to revert.

1. Open the **Test and cutover** menu. 

1. Under **Cutover**, choose **Revert to "ready for cutover"**.

1. This reverts your source servers' **Migration lifecycle** status to **Ready for cutover**, indicating that these servers have not undergone cutover. 

   When the **Revert cutover for X servers** dialog appears, choose **Revert**. 