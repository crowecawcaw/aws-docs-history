# Install the AWS IoT Greengrass Secret Manager

component on the device

The Amazon Kinesis Video Streams Edge Agent requires the AWS IoT Greengrass Secret Manager component to be installed on
the device first.

###### Install the Secret Manager component

1. Sign in to the AWS Management Console and open the AWS IoT Core console at
   [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/"). Verify that the appropriate Region is selected.
2. In the left navigation, choose **Greengrass devices**,
   **Deployments**.

Choose the deployment with the same target as the thing we created in
[Set up the AWS IoT Greengrass V2 core device on the device](gs-setup-gg.md "gs-setup-gg.md"). 3. In the **Actions** dropdown in the top right corner,
choose **Revise**.

In the pop-up that appears, choose **Revise
deployment**. 4. Complete the following sections:

    * **Step 1: Specify target**. Choose
     **Next**.
    * **Step 2: Select components**.




    	+ Verify that the **aws.greengrass.Cli**
    	 component is selected. Do not uninstall this
    	 component.
    	+ Toggle the **Show only selected
    	 components** switch and search for **aws.greengrass.SecretManager**.
    	+ Check the box next to **aws.greengrass.SecretManager**, then choose
    	 **Next**.
    * **Step 3: Configure components**. Configure the
     AWS IoT Greengrass Secret Manager component to download the secrets from within
     the AWS IoT Greengrass environment.


    Select the **aws.greengrass.SecretManager**
     component, then choose **Configure
     component**.


    In the screen that appears, update the
     AWS Secrets Manager ARNs in the **Configuration to
     merge** box.


    ###### Note

    Replace `arn:aws:secretsmanager:*:*:secret:*` with
     the ARNs of the secrets that you created in [Create the Amazon Kinesis Video Streams and
     AWS Secrets Manager resources for your IP camera RTSP URLs](gs-create-resources.md "gs-create-resources.md").



    ```
    {
     "cloudSecrets": [
          {
            "arn": "`arn:aws:secretsmanager:*:*:secret:*`"
          },
          {
            "arn": "`arn:aws:secretsmanager:*:*:secret:*`"
          }
        ]
    }
    ```

    ###### Note

    `cloudSecrets` is a list of objects with the key
     `arn`. For more information, see the [Secret manager configuration](../../../greengrass/v2/developerguide/secret-manager-component.md#secret-manager-component-configuration "../../../greengrass/v2/developerguide/secret-manager-component.md#secret-manager-component-configuration") section in the
     AWS IoT Greengrass Version 2 Developer Guide.


    When you're done, select **Confirm**, then choose
     **Next**.
    * **Step 4: Configure advanced settings**. Select
     **Next**.
    * **Step 5: Review**. Select
     **Deploy**.

5. Confirm that the AWS Secrets Manager component and permissions
   were installed correctly.

On the Ubuntu Amazon EC2 instance, type `sudo
 /greengrass/v2/bin/greengrass-cli component details --name
 aws.greengrass.SecretManager` to verify that the component
received the updated configuration. 6. Inspect the AWS IoT Greengrass core logs.

Type `sudo less /greengrass/v2/logs/greengrass.log`.

Review for deployment errors.

If there was an error, revise the deployment to remove the
`aws.greengrass.SecretManager` component.

Type `sudo service greengrass restart` to restart the AWS IoT Greengrass core
service.

If the deployment error was related to missing permissions, review the
[Add permissions to the token exchange service
(TES) role](gs-add-permissions.md "gs-add-permissions.md") section to make sure that the TES
role has the proper permissions. Then, repeat this section. 7. **Update the secrets on the AWS IoT Greengrass Secret Manager component**

###### Important

The AWS IoT Greengrass Secret Manager component fetches and caches
secrets only when the deployment is updated.

In order to update the secrets on the AWS IoT Greengrass Secret Manager
component, follow the preceding steps 1–6, with the
following change.

**Step 3: Configure components**. Configure
the AWS IoT Greengrass Secret Manager component to download the secrets from
within the AWS IoT Greengrass environment.

Select the **aws.greengrass.SecretManager**
component, then choose **Configure
component**.

In the screen that appears, paste `[""]` in the
**Reset paths** box, and update the
AWS Secrets Manager ARNs in the
**Configuration to merge** box.

For more information, see [Reset updates](../../../greengrass/v2/developerguide/update-component-configurations.md#reset-configuration-update "../../../greengrass/v2/developerguide/update-component-configurations.md#reset-configuration-update").
