# Register an AWS IoT ExpressLink module to your account

To create an AWS IoT thing and add it to your account you must retrieve the AWS IoT ExpressLink
module Thing Name and its corresponding certificate. Follow these steps:

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/"). In the navigation
   pane choose **Manage** then choose **Things**. Choose
   **Create things**, select **Create single thing**,
   then choose **Next**.
2. Open the terminal application on your host machine and enter the command:

```
AT+CONF? ThingName
```

Copy the returned string (a sequence of alphanumeric characters) from the
terminal. 3. Return to the AWS IoT console, and on the **Specify thing properties**
page under **Thing properties**, paste the string you copied from the
terminal into the **Thing name** field. Leave other fields with their
default values, then choose **Next**. 4. In the terminal application, enter the command:

```
AT+CONF? Certificate pem
```

5. Copy the returned string (a longer sequence of alphanumeric symbols), and save it
   in a text file on your host machine as "`ThingName.cert.pem`".
6. In the AWS IoT console, on the **Configure device certificate**
   page, select **Use my certificate**, then select
   **CA is not registered with AWS IoT**.
7. Under **Certificate**, choose **Choose file**.
   Select the file "`ThingName.cert.pem`" that you created in
   a previous step, then choose **Open**.
8. Under **Certificate status**, select **Active**,
   then choose **Next**.
9. Under **Attach policies to certificate**, choose
   **Create policy**.
10. Enter a **Policy name** (for example, "IoTDevPolicy"), then
    under **Policy document** select **JSON**.
11. Copy the the following into the console **Policy document**:

###### Warning

The examples in this document are intended only for development environments.
All devices in your fleet must have credentials with privileges that authorize only
intended actions on specific resources. The specific permission policies can vary
for your use case. Identify the permission policies that best meet your business and
security requirements. For more information, see
[Example IAM identity-based policies](../../../IAM/latest/UserGuide/access_policies_examples.md "../../../IAM/latest/UserGuide/access_policies_examples.md") and
[Security Best practices](../../../IAM/latest/UserGuide/best-practices-use-cases.md "../../../IAM/latest/UserGuide/best-practices-use-cases.md") in the _IAM Identity and Access Management
User Guide_. 12. Choose **Create**. Return to the **Attach policies to
certificate** page and select the policy you just created (for example,
"IoTDevPolicy"), then choose **Create thing** to complete the
thing creation. 13. In the AWS IoT console, in the navigation pane, choose **Settings**.
Under **Device data endpoint** select the **Endpoint**
to make a copy of the endpoint for your account. 14. In the terminal application, type this command using the endpoint you just copied:

```
AT+CONF Endpoint=`your endpoint string here`
```

## Set up for Wi-Fi modules

AWS IoT ExpressLink modules that support Wi-Fi connectivity require access to a local
Wi-Fi router in order to connect to the internet. You can enter the required security
credentials with the following additional steps:

1. In the terminal application, enter the command:

```
AT+CONF SSID=`your router ssid`
```

2. In the terminal application, enter the command:

```
AT+CONF Passphrase=`your router passphrase`
```

###### Note

Your local router's SSID and passphrase are stored securely inside the AWS IoT
ExpressLink module. While the SSID can be retrieved later (for debugging purposes)
any attempt to retrieve the Passphrase will return an error.

## Completion

Congratulations! You have completed the registration of the evaluation kit as a thing
in your AWS IoT account. You will not need to repeat these steps the next time you connect,
as the AWS IoT ExpressLink module will remember its configuration and will be ready to
connect to your AWS account automatically.
