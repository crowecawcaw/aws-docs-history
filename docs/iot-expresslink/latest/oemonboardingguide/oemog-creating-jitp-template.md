

# Appendix C - Create a JITP template
<a name="oemog-creating-jitp-template"></a>

 Create a JITP template so that new devices directed to the account are automatically associated with a desired policy, and given a proper thing-name on the AWS console. Follow the steps below to create a template. 

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot/home).  
![AWS IoT Core service console search results showing AWS IoT offerings.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss06.png)

1. In the left navigation pane, select **Connect many devices** then select **Provisioning templates** in the drop-down sub-menu.   
![AWS IoT console overview showing options to connect devices, and test device configurations.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss07.png)

1. On the provisioning templates management page, select **Create provisioning template**.   
![AWS IoT service connect many devices workflow with steps to create provisioning template.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss08.png)

1. On the **Create provisioning template** page, choose **Provisioning devices with unique certificate (JITP) - *recommended***, then select **Next**.  
![AWS IoT template for provisioning devices with unique certificates at initial connect.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss09.png)

1. In the JITP template creation wizard, under **Describe provisioning template**, enter the information for the **Provisioning template properties**:

   1. Under **Provisioning template status**, choose **Active**.

   1. Enter a **Provisioning template name**.

   1. (Optional) Enter a **Description** for the template.  
![AWS IoT provisioning template configuration screen with options to set template status as active or inactive.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss10.png)

1. Under **Provisioning role**, make sure **Attach managed policy to IAM role** is checked. (This ensures the IAM role created here and used in device provisioning will have the needed privileges.) Then select **Create new role**.   
![Choose an IAM role and create new role button for provisioning AWS IoT access to resources.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss11.png)

   (Optional) Instead of creating a new role, you can choose a role that you have previously made. However, to make sure that the role has enough privileges to provision your ExpressLink modules, you must make sure that the role has the AWS managed policies "`AWSIoTThingsRegistration`", "`AWSIoTLogging`", and "`AWSIoTRuleActions`" attached, or that it has an inline policy with equivalent or greater permissions. See [AWS managed policies for AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/security-iam-awsmanpol.html) for more information.

1. In the **Create role** pop-up window, enter a **Role name**, then select **Create**.  
![Create role dialog with role name field and instructions to enter unique role name without spaces.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss12.png)

1. Under **CA certificate configuration**, for **Automatic certificate registration**, choose **On**. Above that, under **CA certificate** select the **Choose the CA certificates to use** dropdown menu.  
![CA certificate configuration options to choose certificates to use, toggle automatic certificate registration.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss13.png)

1. In the dropdown menu, choose the checkbox in front of the CA certificate ID that was listed in the output of the `aws iot register-ca-certificate` AWS CLI command that you ran in the previous section. After the CA certificate ID appears on the page, select **Next**.  
![CA certificate selection interface showing a search bar and a pre-selected CA certificate ID.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss14.png)  
![CA certificate configuration page showing options to manage CA certificates.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss15.png)

1. Under **Set provisioning actions**, toggle on **Automatically create a thing resource when provisioning a device**. 

   (Optional) You can also choose **Additional configurations** for the [ Thing type](https://docs.aws.amazon.com/iot/latest/developerguide/thing-types.html), [ Searchable thing attributes](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html), [ Thing groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html), and [ Billing groups](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-billing-groups.html).

   Select **Next**.  
![AWS IoT console showing provisioning steps to automatically create a thing resource and additional configurations.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss16.png)

1. Under **Set device permissions**, select **Create policy** to create a new policy for those ExpressLink modules you want to provision. This policy determines the actions that can be run by the ExpressLink modules on AWS IoT Core under your AWS account.   
![Set device permissions screen with list of AWS IoT policies to authorize devices accessing resources like MQTT topics and Device Shadows.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss17.png)

1. On the **Create policy** page, enter a **Policy name**.

   On the **Policy statements** tab, under **Policy document**, for convenience you can enter "\*" for both the **Policy action** and **Policy resource**. However, this policy will allow any and all actions on any AWS IoT Core resources accessible through MQTT. We recommend that you use a more restrictive policy. The **Policy examples** tab contains numerous example policy documents that can be applied for different use cases. See the policy documents under that tab or refer to [AWS IoT Core policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) for additional information.  
![AWS IoT Core policy creation console with fields to enter policy details.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss18.png)

1. Select **Create** to create the policy.

1. On the **Set device permissions** page, refresh your browser (select the icon that looks like a circular arrow pointing to its own starting point). Your policy should now show up in the list under **Policies**. Choose the checkbox in front of your policy, then select **Next**.  
![Set device permissions page showing Policies section with a policy named "your_policy_name" selected.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss19.png)

1. Review the information you have entered to make sure it is correct. In particular, make sure that the CA certificate shown under **CA certificate configuration** has the same CA certificate ID returned by the AWS CLI command that you ran in a previous step. You can edit a particular section if the information is incorrect. After you verify the information you entered, scroll to the bottom and select **Create template**.   
![Set provisioning actions interface showing automatic thing creation options.](http://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/images/ss20.png)

1. Your JITP template is now created and ready to be applied whenever an ExpressLink module issues a connect request to your AWS account's IoT Core endpoint during onboarding-by-claim. 