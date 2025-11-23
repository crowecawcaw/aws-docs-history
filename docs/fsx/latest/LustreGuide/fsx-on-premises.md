# Using Amazon FSx with your on-premises data

You can use FSx for Lustre to process your on-premises data with in-cloud compute instances.
FSx for Lustre supports access over Direct Connect and VPN, enabling you to mount your file systems
from on-premises clients.

###### To use FSx for Lustre with your on-premises data

1. Create a file system. For more information, see [Step 1: Create your FSx for Lustre file system](getting-started.md#getting-started-step1 "getting-started.md#getting-started-step1") in the getting started exercise.
2. Mount the file system from on-premises clients. For more information, see [Mounting Amazon FSx file systems from on-premises or a peered Amazon VPC](mounting-on-premises.md "mounting-on-premises.md").
3. Copy the data that you want to process into your FSx for Lustre file system.
4. Run your compute-intensive workload on in-cloud Amazon EC2 instances mounting your file
   system.
5. When you're finished, copy the final results from your file system back to your
   on-premises data location, and delete your FSx for Lustre file system.
