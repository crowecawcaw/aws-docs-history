# Use the AWS IoT SiteWise demo

You can easily explore AWS IoT SiteWise by using the AWS IoT SiteWise demo. AWS IoT SiteWise provides the demo as an
CloudFormation template that you can deploy to create asset models, assets, and a SiteWise Monitor portal,
and generate sample data for up to a week.

###### Important

Once you create the demo, you will start being charged for the resources that this demo creates and consumes.

###### Topics

- [Create the AWS IoT SiteWise demo](#create-getting-started-demo "#create-getting-started-demo")
- [Delete the AWS IoT SiteWise demo](#delete-getting-started-demo "#delete-getting-started-demo")

## Create the AWS IoT SiteWise demo

You can create the AWS IoT SiteWise demo from the AWS IoT SiteWise console.

###### Note

The demo creates Lambda functions, one CloudWatch Events rule, and the AWS Identity and Access Management (IAM)
roles required for the demo. You might see these resources in your AWS account. We
recommend that you keep these resources until you're done with the demo. If you delete the
resources, the demo might stop working correctly.

###### To create the demo in the AWS IoT SiteWise console

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/") and find the **SiteWise demo** in
   the upper-right corner of the page.
2. (Optional) Under **SiteWise demo**, change the **Days to
   keep demo assets** field to specify how many days to keep the demo before
   deleting it.
3. (Optional) To create a SiteWise Monitor portal to monitor sample data, do the following.

###### Note

You will be charged for the SiteWise Monitor resources that this demo creates and consumes.
For more information, see [SiteWise Monitor](https://aws.amazon.com/iot-sitewise/pricing/ "https://aws.amazon.com/iot-sitewise/pricing/")
in the _AWS IoT SiteWise Pricing_.

    1. Choose **Monitor Resources**.
    2. Choose **Permission**.
    3. Choose an existing IAM role that grants your federated IAM users access to the portal.


    ###### Important

    Your IAM role must have the following permissions.


    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Action": [
     "iotsitewise:Describe*",
     "iotsitewise:List*",
     "iotsitewise:Get*",
     "cloudformation:DescribeStacks",
     "iam:GetPolicyVersion",
     "iam:GetPolicy",
     "iam:ListAttachedRolePolicies",
     "sso:DescribeRegisteredRegions",
     "organizations:DescribeOrganization"
     ],
     "Resource": "*"
     }
     ]
    }`

    ```For more information about how to work with SiteWise Monitor, see [What is AWS IoT SiteWise Monitor?](../appguide/what-is-monitor-app.md "../appguide/what-is-monitor-app.md")

in the _AWS IoT SiteWise Monitor Application Guide_. 4. Choose **Create demo**.

The demo takes around 3 minutes to create. If the demo fails to create, your account
might have insufficient permissions. Switch to an account that has administrative
permissions, or use the following steps to delete the demo and try again:

    1. Choose **Delete demo**.


    The demo takes around 15 minutes to delete.
    2. If the demo doesn't delete, open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/"), choose the stack
     named **IoTSiteWiseDemoAssets**, and choose
     **Delete** in the upper-right corner.
    3. If the demo fails to delete again, follow the steps in the CloudFormation console to skip
     the resources that failed to delete, and try again.

5. After the demo creates successfully, you can explore the demo assets and data in the
   [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").

## Delete the AWS IoT SiteWise demo

The AWS IoT SiteWise demo deletes itself after a week, or the number of days you chose if you
created the demo stack from the CloudFormation console. You can delete the demo before if you're done
using the demo resources. You can also delete the demo if the demo fails to create. Use the
following steps to delete the demo manually.

###### To delete the AWS IoT SiteWise demo

1. Navigate to the [CloudFormation
   console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").
2. Choose **IoTSiteWiseDemoAssets** from the list of
   **Stacks**.
3. Choose **Delete**.

When you delete the stack, all of the resources created for the demo are
deleted. 4. In the confirmation dialog, choose **Delete stack**.

The stack takes around 15 minutes to delete. If the demo fails to delete, choose
**Delete** in the upper-right corner again. If the demo fails to
delete again, follow the steps in the CloudFormation console to skip the resources that failed to
delete, and try again.
