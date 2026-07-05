End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](../userguide/SunsetPlan.md "../userguide/SunsetPlan.md").

# Create an IAM Role for AMS to use

1. Obtain a JSON or YAML file that defines an IAM role for AMS to use to create your infrastructure. Either:

   - Your AMS cloud architect (CA) provides you with a JSON or YAML file.
   - You can download [onboarding\_iam\_roles.zip](samples/onboarding_iam_roles.zip.md "samples/onboarding_iam_roles.zip.md") and
     choose one of the following:

     - **onboarding\_role\_admin.json** (shorter, grants full admin access)
     - **onboarding\_role\_minimal.json** (longer, grants
       [least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege "https://en.wikipedia.org/wiki/Principle_of_least_privilege"))

2. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").

![](images/image1.png) 3. Choose **Create Stack**. You see the following page.

![](images/image2.png) 4. Choose **Upload a template file**, upload the JSON or YAML file of the IAM role,
and then choose **Next**. You see the following page.

![](images/image3.png) 5. Enter `ams-onboarding-role` into the **Stack name** section and
continue scrolling down and selecting next until you reach this page.

![](images/image4.png) 6. Make sure the check box is selected and then select **Create Stack**. 7. Make sure the stack was created successfully.
