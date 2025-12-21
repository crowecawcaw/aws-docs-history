#

Add cross-account endpoints in AWS Global Accelerator

Follow the steps in this section to add a cross-account endpoints using the Global Accelerator console.

This section explains how to add cross-account endpoints by using
the AWS Global Accelerator console. To learn about using API operations with Global Accelerator, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

# To add a cross-account endpoint

1. When you create or update an accelerator, in the **Endpoints** section, choose **Add endpoint**.
2. On the **Add endpoints** page, select **Add a resource specified
   in a cross-account attachment**.
3. In the drop-down menu, select an AWS account that has created a cross-account attachment that
   includes you or the accelerator as a principal.
4. For **Endpoint type**, choose the type of resource that you want to add.

Note that only the resource types included in the cross-account attachment appear in the
drop-down menu. 5. For **Endpoint**, choose resource that you want to add.

Note that only resources that are included in the cross-account attachment appear in the
drop-down menu. To see resources that are not enabled by a cross-account attachment,
clear the **Add a resource specified in a cross-account attachment** check box.
