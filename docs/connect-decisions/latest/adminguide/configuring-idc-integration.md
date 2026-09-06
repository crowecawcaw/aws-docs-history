# Configuring AWS Identity Center Integration

To create an instance and use the Amazon Connect Decisions service, you need to either connect
an existing IAM Identity Center user profile or create a new one.

1. Open the [Amazon Connect Decisions
   console](https://console.aws.amazon.com/scn/home "https://console.aws.amazon.com/scn/home"). You can also search for "Amazon Connect Decisions" from the main
   AWS Management Console.
2. If necessary, change the **AWS Region** by selecting
   **Select a Region** located at the top of the console.
   Choose your Region from the drop-down list.
3. Select **Create Amazon Connect Decisions instance**. A
   notification will appear.

![](images/configuring-idc-integration-create-instance.png) 4. Enter your email address and select **Continue**. IdC
will verify if the email matches an existing user. 5. Do one of the following:

    * **If IdC matches the email address to a user**
     – Select **Connect your identity source and onboard
     your team**.


    ###### Note

    This can be used if your organization has an established IdC instance
     that you would like to use for Amazon Connect Decisions.
    * **If IdC does not find a match to an existing
     user** – A **Create a New User**
     notification appears. Proceed to the next step.

6. In the notification, enter the following then select **Continue**:

    * Email address
    * First name
    * Last name

IdC creates the user automatically and adds them as the Amazon Connect Decisions
administrator. 7. Do one of the following:

    * **To create an instance using standard
     configuration** – Select **Create**.
     See [Use
     standard configuration](../../../aws-supply-chain/latest/adminguide/create-instance-standard.md "../../../aws-supply-chain/latest/adminguide/create-instance-standard.md").
    * **To create an instance using a custom
     configuration** – Select **Edit in advanced
     setup**. See [Use
     advanced configuration](../../../aws-supply-chain/latest/adminguide/create-instance-advanced.md "../../../aws-supply-chain/latest/adminguide/create-instance-advanced.md").

When used in conjunction with IAM Identity Center, Amazon Connect Decisions retrieves the
'username' and 'email' fields from IAM Identity Center directory. None of these attributes
are stored natively in your Amazon Connect Decisions instance and are always retrieved at runtime.
Amazon Connect Decisions encrypts these identity attributes at rest using an AWS owned KMS key
by default. Customer managed KMS keys are not supported in Amazon Connect Decisions. If you delete
a user in your AWS IAM Identity Center instance, Amazon Connect Decisions deletes that user from
your instance as well.
