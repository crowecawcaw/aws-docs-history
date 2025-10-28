# Create a new registration using the AWS End User Messaging SMS console

You can use the AWS End User Messaging SMS console to manage registrations for your AWS End User Messaging SMS account. If your
registration was already created as part of requesting a phone number or sender ID then you do
not need to create a new registration. You can view the resources associated with a registration
in the **Associated resources** tab, for more information see [View a registration associated resources in AWS End User Messaging SMS](registrations-associated-resource.md "registrations-associated-resource.md").

###### Important

Some registrations have multiple steps that need to be completed in exact order.

- To register a US 10DLC number, you must first register and complete a **US 10DLC Brand registration**, then apply for optional **US 10DLC Brand vetting** to increase your Messages per second
  (MPS), and then register a **US 10DLC Campaign
  registration**. If you require sending 10DLC SMS messages from more than one
  AWS Region and from a single account, you must re-registering all 10DLC resources for
  each AWS Region required. For more information about the process, see [United States 10DLC registration](registrations-10dlc.md "registrations-10dlc.md").
- To register a **Singapore sender ID registration** you must
  first obtain a Singapore Unique Entity Number (UEN), create and submit a Singapore
  sender ID registration, once the registration is approved then register the sender ID
  with Singapore Network Information Centre (SGNIC). For more information about the
  process, see [Singapore sender ID registration process](registrations-sg.md "registrations-sg.md").
- To register a **India sender ID registration** you must
  first register your company and use case with TRAI, create and submit a case with Support
  and then to send messages you must specify **Entity ID**
  and **Template ID** values that you received. For more
  information about the process, see [India sender ID registration process in
  AWS End User Messaging SMS](registrations-sms-senderid-india.md "registrations-sms-senderid-india.md").

###### Create a new registration

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Registrations**, choose **Create
   registration**.

###### Note

If you already created a registration when requesting the origination identity then you
should use that registration form. 3. For **Registration form name** enter a friendly name. 4. For **Registration type**, choose the registration form from the dropdown
list. Each **Registration type** has different forms depending on the
regulatory body the registration form is sent to. 5. (optional) Expand **Tags** to:

    * **Add a tag** – In **Manage tags**
     choose **Add new tag** to create a new blank key/value pair.
    * **Delete a tag** – In **Manage
     tags**, choose **Remove** next to the key/value pair.
    * **Edit a tag** – In **Manage tags**
     choose the **Key** or **Value** and edit the text.

6. Choose **Create**.
7. Your registration has now been created and you need to enter in all required information
   then submit.
   - **US toll-free number registration** – [US toll-free number registration form](registrations-tfn-register.md "registrations-tfn-register.md").
   - **US 10DLC Brand vetting** – The 10DLC brand has been
     submitting for vetting and you don't need to fill out any additional forms, see [10DLC brand vetting form](registrations-10dlc-vetting.md "registrations-10dlc-vetting.md").
   - **US 10DLC Brand registration** – [10DLC brand registration form](registrations-10dlc-company.md "registrations-10dlc-company.md").
   - **US-10DLC campaign registration** – [10DLC campaign registration form](registrations-10dlc-register-campaign.md "registrations-10dlc-register-campaign.md").
   - **Singapore sender ID registration** – [Singapore sender ID registration form](registrations-sg-form.md "registrations-sg-form.md").
