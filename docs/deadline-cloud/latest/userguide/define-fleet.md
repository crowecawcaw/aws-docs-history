

# (Optional) Step 4: Define fleet details
<a name="define-fleet"></a>

A fleet allocates workers to execute your rendering tasks. If you need a fleet for your rendering tasks, check the box for **Create fleet**.

1. **Fleet details**

   1. Provide both a **Name** and optional **Description** for your fleet.

   1. Review the fleet type and operating system for awareness.

1. In the **Instance market type** section, choose either **Spot**, **On-demand**, or **Wait and Save Instance**. Amazon EC2 On-demand instances provide faster availability and Amazon EC2 Spot and Wait and Save instances are better for cost saving efforts.

1. For **Auto scaling** the number of instances in your fleet, choose both a **Minimum** number of instances and a **Maximum** number of instances.

   We strongly recommend to always set the minimum number of instances to **0** to avoid incurring extra costs. 

1. Review the worker capabilities for awareness.

1. (optional) Choose **Additional fleet settings**

   1. Your fleet requires permission to write to CloudWatch on your behalf. We recommend you create a new service role for every fleet.

      1. For a new role, complete the following steps.

         1. Select **Create and use a new service role**.

         1. Enter a **Role name** for your fleet role or use the provided role name.

         1. (Optional) Add a fleet role **Description**.

         1. To view the IAM permissions for the fleet role, choose **View permission details**.

      1. Alternatively, you can use an existing service role.

   1. (Optional) Add tags for the fleet using key and value pairs.

After you enter all the fleet details, choose **Next**.