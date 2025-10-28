# Configure a device instance for

activation

After a device instance is created, you configure the device instance with a
previously created configuration template (see [Create a configuration template](create-config-template.md "create-config-template.md")), or you can add configurations manually.

###### To configure a device instance for activation

1.  Open the Amazon One console at [https://console.aws.amazon.com/one-enterprise](https://console.aws.amazon.com/one-enterprise/ "https://console.aws.amazon.com/one-enterprise/").
2.  In the navigation
    pane, choose **Device instances**. Make sure you are on the
    **Unactivated instances** tab.
3.  Select one or more instances to configure.
4.  Choose **Configure**.
5.  Under
    **Device Configurations**, select one of the two input
    methods:
    1. For the **Use template** option, choose a
       template from the
       drop-down.
       Review or make changes to this imported configuration
       information.

    For the **Create template** option, see [Create a configuration template](create-config-template.md "create-config-template.md"). 2. For the **Manually input** option, select an
    **Operating
    mode**.

    To configure Enrollment operating mode

        1. (Optional) Under **Wifi
         configuration**, provide a **Wifi
         credential**.
        2. (Optional) To add a tag to the site, enter a
         key-value pair under **Tags**,
         and then choose **Add new tag**.
         To remove this tag before creating the site,
         choose **Remove**.
        3. Choose **Configure**.

    To configure Entry operating mode

        1. Under **Control panel
         settings**, provide the communication
         settings for Amazon One devices to communicate with
         your control panel.
        2. Under **Badge format
         settings**, provide the configuration
         settings that specify the layout of your company
         badge format.
        3. (Optional) Under **Wifi
         configuration**, provide a **Wifi
         credential**.
        4. (Optional) To add a tag to the site, enter a
         key-value pair under **Tags**,
         and then choose **Add new tag**.
         To remove this tag before creating the site,
         choose **Remove**.
        5. Choose **Configure**.

6.  Under
    the **Unactivated instances** table, the Instance state
    should show
    ![Green checkmark icon with text "Ready for activation" indicating a successful status.](images/instance state.png)
    .
7.  Validate that activation QR codes are available for activation. In the
    navigation pane, choose **Activation QR
    Code**.
8.  From the **Select a site** drop-down list, select a
    **Site**.
9.  Under **Site information**, validate the Site
    address.
10. Under **Activation QR codes**, each device instance has a
    corresponding QR code. Choose **Get QR code** to show the
    activation QR codes.

###### Important

You must configure at least one Enrollment device and one Entry device to
enable the full capabilities of Amazon One for secure access.
