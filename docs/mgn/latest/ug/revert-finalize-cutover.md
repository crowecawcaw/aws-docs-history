

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Reverting a cutover
<a name="revert-finalize-cutover"></a>

Once you have launched your cutover instances, open the Amazon EC2 console and SSH or RDP into your cutover instances to ensure that they function correctly. Validate connectivity and perform acceptance tests for your application. 

**Note**  
You should turn on Termination Protection after you have completed your testing and before you are ready to finalize the cutover. Learn more about enabling termination protection in [this Amazon EC2 article](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination).

If you encounter any issues and want to launch new cutover instances, you can revert the cutover. This reverts your source servers' **Migration lifecycle** status to **Ready for cutover**, indicating that these servers have not undergone cutover. During a revert, you also have the option to delete your Cutover instances for cost-saving purposes.

To revert a cutover take the following steps:

1. Check the box to the left of every source server that has a launched cutover instance you want to revert.

1. Open the **Test and cutover** menu. 

1. Under **Cutover**, choose **Revert to "ready for cutover"**.

1. This reverts your source servers' **Migration lifecycle** status to **Ready for cutover**, indicating that these servers have not undergone cutover. 

   When the **Revert cutover for X servers** dialog appears, choose **Revert**. 