

# Manage SiteWise Edge gateways
<a name="manage-gateways-ggv2"></a>

You can use the AWS IoT SiteWise console and API operations to manage AWS IoT SiteWise Edge gateways. You can also use the [AWS OpsHub for AWS IoT SiteWise for Windows](https://aws-iot-sitewise.s3.amazonaws.com/gateway/OpsHub+for+AWS+IoT+SiteWise.exe) application to manage some aspects of your SiteWise Edge gateway from your local device.

We highly recommend that you use the AWS OpsHub for AWS IoT SiteWise application to monitor the disk usage on your local device. You can also monitor the `Gateway.AvailableDiskSpace` and `Gateway.UsedPercentageDiskSpace` Amazon CloudWatch metrics and create alarms to get notified when the disk space is getting low. For more information about Amazon CloudWatch alarms, see [Create a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html).

Make sure that your device has enough space for upcoming data. When you're about to run out of space on your local device, the service automatically deletes a small amount of data with the oldest timestamps to make room for upcoming data.

To check if the service deleted your data, do the following:

1. Sign in to the AWS OpsHub for AWS IoT SiteWise application.

1. Choose **Settings**.

1. For **Logs**, specify a time range, and then choose **Download**.

1. Unzip the log file.

1. If the log file contains the following message, the service deleted your data:  {{number}} bytes of data have been deleted to prevent SiteWise Edge gateway storage from running out of space.  

## Manage your SiteWise Edge gateway with the AWS IoT SiteWise console
<a name="cloud-console"></a>

You can use the AWS IoT SiteWise console to configure, update, and monitor all SiteWise Edge gateways in your AWS account. 

You can view your SiteWise Edge gateways by navigating to the **Edge Gateways** page in the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/). To access the **Edge gateway details** page for a specific gateway, choose the name of an Edge gateway.

From the **Overview** tab of the **Edge gateway details** page, you can do the following:
+ In the **Data sources** section, update data source configuration and configure additional data sources
+ Choose **Open CloudWatch metrics** to view the number of data points ingested per data source in the CloudWatch metrics console
+ In the **Edge capabilities** section, add data packs to your SiteWise Edge gateway by clicking **Edit**
+ In the **Gateway configuration** section, view the connectivity status of your SiteWise Edge gateways
+ In the **Publisher configuration** section, view the SiteWise Edge gateway sync status and configuration of the AWS IoT SiteWise publisher component

From the **Updates** tab of the **Edge gateway details** page, you can see the current component and pack versions that are deployed to the Edge gateway. This is also where you deploy new versions, when they're available.

## Manage SiteWise Edge gateways using AWS OpsHub for AWS IoT SiteWise
<a name="opshub-app"></a>

You use the AWS OpsHub for AWS IoT SiteWise application to manage and monitor your self-hosted SiteWise Edge gateways. This application provides the following monitoring and management options:
+ Under **Overview**, you can do the following:
  + View SiteWise Edge gateway details that help you get insights into your SiteWise Edge gateway device data, identify issues, and improve the SiteWise Edge gateway's performance.
  + View SiteWise Monitor portals that monitor the data from local servers and equipment at the edge. For more information, see [What is AWS IoT SiteWise Monitor](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/what-is-monitor-app.html) in the *AWS IoT SiteWise Monitor Application Guide*.
+ Under **Health**, there's a dashboard that displays data from your SiteWise Edge gateway. Domain experts, such as process engineers, can use the dashboard to see an overview of SiteWise Edge gateway behavior.
+ Under **Assets**, view assets deployed to the local device and the last value collected or computed for asset properties.
+ Under **Settings**, you can do the following:
  + If the Data Processing Pack is installed, view the SiteWise Edge gateway configuration information and sync resources with the AWS Cloud.
  + Download the authentication files that you can use to access the SiteWise Edge gateway by using other tools. 
  + Download logs that you can use to troubleshoot the SiteWise Edge gateway.
  + View the AWS IoT SiteWise components deployed to the SiteWise Edge gateway.

**Important**  
The following are required to use AWS OpsHub for AWS IoT SiteWise:  
Your local device and the AWS OpsHub for AWS IoT SiteWise application must be connected to the same network.
The data processing pack must be enabled.

**To manage SiteWise Edge gateways using AWS OpsHub**

1. Download and install the [AWS OpsHub for AWS IoT SiteWise for Windows](https://aws-iot-sitewise.s3.amazonaws.com/gateway/OpsHub+for+AWS+IoT+SiteWise.exe) application.

1. Open the application.

1. If you don't have local credentials set up for your gateway, follow the steps under [Access your SiteWise Edge gateway using local operating system credentials](#create-user-pool) to set them up.

1. You can sign in to your SiteWise Edge gateway with your Linux or Lightweight Directory Access Protocol (LDAP) credentials. To sign in to your SiteWise Edge gateway, do one of the following:

------
#### [ Linux ]

   1. For **Hostname or IP address**, enter the hostname or IP address of your local device.

   1. For **Authentication**, choose **Linux**.

   1. For **User name**, enter the user name of your Linux operating system.

   1. For **Password**, enter the password of your Linux operating system.

   1. Choose **Sign in**.

------
#### [ LDAP ]

   1. For **Hostname or IP address**, enter the hostname or IP address of your local device.

   1. For **Authentication**, choose **LDAP**.

   1. For **User name**, enter your LDAP's user name.

   1. For **Password**, enter your LDAP's password.

   1. Choose **Sign in**.

------

## Access your SiteWise Edge gateway using local operating system credentials
<a name="create-user-pool"></a>

Besides Lightweight Directory Access Protocol (LDAP), you can use the Linux or Windows credentials to access your self-hosted SiteWise Edge gateway.

**Important**  
To access your SiteWise Edge gateway with Linux credentials, you must activate the data processing pack for your SiteWise Edge gateway.

### Access your SiteWise Edge gateway using Linux operating system credentials
<a name="linux-user-pool"></a>

 The following steps assume that you use a device with Ubuntu. If you use a different Linux distribution, consult the relevant documentation for your device.

**To create a Linux user pool**

1. To create an admin group, run the following command.

   ```
   sudo groupadd --system SWE_ADMIN_GROUP
   ```

   Users in the `SWE_ADMIN_GROUP` group can allow admin access for the SiteWise Edge gateway.

1. To create a user group, run the following command.

   ```
   sudo groupadd --system SWE_USER_GROUP
   ```

   Users in the `SWE_USER_GROUP` group can allow read-only access for the SiteWise Edge gateway.

1. To add a user to the admin group, run the following command. Replace {{user-name}} and {{password}} with the user name and password that you want to add.

   ```
   sudo useradd -p $(openssl passwd -1 {{password}}) {{user-name}}
   ```

1. To add a user to either `SWE_ADMIN_GROUP` or `SWE_USER_GROUP`, replace {{user-name}} with the the user name that you added in the previous step.

   ```
   sudo usermod -a -G SWE_ADMIN_GROUP {{user-name}}
   ```

You can now use the user name and password to sign in to the SiteWise Edge gateway on the AWS OpsHub for AWS IoT SiteWise application.

### Access your SiteWise Edge gateway using Windows credentials
<a name="windows-user-pool"></a>

 The following steps assume that you use a device with Windows.

**Important**  
Security is a shared responsibility between AWS and you. Create a strong password policy with at least 12 characters and a combination of uppercase, lowercase, numbers, and symbols. Additionally, set the Windows Firewall rules to allow incoming traffic on port 443 and to block incoming traffic on all other ports.

**To create a Windows Server user pool**

1. Run PowerShell as the administrator.

   1. On the Windows server where you want to install SiteWise Edge Gateway, log in as administrator.

   1. Enter **PowerShell** in the Windows search bar.

   1. In the search results, right click on the Windows PowerShell app. Choose **Run as Administrator**.

1. To create an admin group, run the following command.

   ```
   net localgroup SWE_ADMIN_GROUP /add
   ```

   You must be a user in the `SWE_ADMIN_GROUP` group to allow admin access for the SiteWise Edge gateway.

1. To create a user group, run the following command.

   ```
   net localgroup SWE_USER_GROUP /add
   ```

   You must be a user in the `SWE_USER_GROUP` group to allow ready-only access for the SiteWise Edge gateway.

1. To add user, run the following command. Replace {{user-name}} and {{password}} with the user name and the password that you want to create.

   ```
   net user {{user-name password}} /add
   ```

1. To add a user to the admin group, run the following command. Replace {{user-name}} with the user name that you want to add.

   ```
   net localgroup SWE_ADMIN_GROUP {{user-name}} /add
   ```

You can now use the user name and password to sign in to the SiteWise Edge gateway on the AWS OpsHub for AWS IoT SiteWise application.

## Manage the SiteWise Edge gateway certificate
<a name="manage-gateway-certificate"></a>

You can use SiteWise Monitor and third-party applications, such as Grafana, on your SiteWise Edge gateway devices. These applications require a TLS connection to the service. SiteWise Edge gateways currently use a self-signed certificate. If you use a browser to open the applications, such as a SiteWise Monitor portal, you might receive a warning for untrusted certificate.

The following shows how to download the trusted certificate from the AWS OpsHub for AWS IoT SiteWise application.

1. Sign in to the application.

1. Choose **Settings**.

1. For **Authentication**, choose **Download certificate**.

The following assumes that you use Google Chrome or FireFox. If you use a different browser, consult the relevant documentation for your browser. To add the certificate that you downloaded in the previous step to a browser, do one of the following:
+ If you use Google Chrome, follow the [Set up certificates](https://support.google.com/chrome/a/answer/3505249?hl=en) in the *Google Chrome Enterprise Help documentation*.
+ If you use Firefox, follow the [To Load the Certificate into the Mozilla or Firefox Browser](https://docs.oracle.com/cd/E19528-01/819-4639/gaesv/index.html) in the *Oracle documentation*.

## Change the version of SiteWise Edge gateway component packs
<a name="manage-gateway-update-packs"></a>

You can use the AWS IoT SiteWise console to change the version of component packs on your SiteWise Edge gateways.

**To change the version of a SiteWise Edge gateway component pack**

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the left navigation pane, choose **Gateways**.

1. Select the SiteWise Edge gateway that you would like to change the pack versions for.

1. Under **Gateway configuration**, choose **View software versions**.

1. On the **Edit software versions** page, for the pack you want to update the version of, select the version you want to deploy and choose **Deploy**.

1. Choose **Done**.

## List SiteWise Edge gateways
<a name="manage-gateway-list-gateways"></a>

------
#### [ Console ]

**To list SiteWise Edge gateways**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the navigation pane, choose **Edge gateways**.

1. View the list of all your SiteWise Edge gateways.

------
#### [ AWS CLI ]

To list your gateways using AWS CLI, follow these steps:
+ Use the list-gateways command to view all your gateways:

  ```
  aws iotsitewise list-gateways
  ```

  This command returns a list of your gateways with their IDs, names, and other information.

  You can also specify pagination parameters:

  ```
  aws iotsitewise list-gateways --max-results {{10}} --next-token {{your-token}}
  ```

For more information, see [list-gateways](https://docs.aws.amazon.com/cli/latest/reference/iotsitewise/list-gateways.html) in the AWS CLI Command Reference.

------

## Describe a SiteWise Edge gateway
<a name="manage-gateway-describe-gateway"></a>

------
#### [ Console ]

**To view gateway details**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the navigation pane, choose **Edge gateways**.

1. Choose the name of the gateway you want to view details for.

1. View the gateway details on the **Edge gateway details** page.

------
#### [ AWS CLI ]

To get detailed information about a specific gateway using AWS CLI, follow these steps:
+ Use the describe-gateway command with the gateway ID:

  ```
  aws iotsitewise describe-gateway --gateway-id {{a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE}}
  ```

  This command returns detailed information about the gateway.

For more information, see [describe-gateway](https://docs.aws.amazon.com/cli/latest/reference/iotsitewise/describe-gateway.html) in the AWS CLI Command Reference.

------

## Create a SiteWise Edge gateway
<a name="manage-gateway-create-gateway"></a>

------
#### [ Console ]

**To create a SiteWise Edge gateway**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the navigation pane, choose **Edge gateways**.

1. Choose **Create gateway**.

1. Enter a name for your gateway.

1. Select the Greengrass group for your gateway.

1. Optionally, add tags to your gateway.

1. Choose **Create**.

------
#### [ AWS CLI ]

To create a new IoT SiteWise gateway using AWS CLI, follow these steps:
+ Use the create-gateway command to create a new gateway:

  ```
  aws iotsitewise create-gateway \
      --gateway-name "NewSiteWiseGateway" \
      --gateway-platform '{
          "greengrass": {
              "groupArn": "arn:aws:greengrass:us-east-1:123456789012:group/a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE"
          }
      }' \
      --tags '{
          "Environment": "Production",
          "Location": "Factory1"
      }'
  ```

  This command returns the new gateway's ID and ARN:

  ```
  {
      "gatewayId": "a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE",
      "gatewayArn": "arn:aws:iotsitewise:us-east-1:123456789012:gateway/a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE"
  }
  ```

For more information, see [create-gateway](https://docs.aws.amazon.com/cli/latest/reference/iotsitewise/create-gateway.html) in the AWS CLI Command Reference.

------

## Update a SiteWise Edge gateway
<a name="manage-gateway-update-gateway"></a>

------
#### [ Console ]

**To update a SiteWise Edge gateway**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the navigation pane, choose **Edge gateways**.

1. Select the gateway you want to update.

1. Choose **Edit**.

1. Update the gateway name or other settings as needed.

1. Choose **Save**.

------
#### [ AWS CLI ]

To update an existing gateway using AWS CLI, follow these steps:
+ Use the update-gateway command to update a gateway's name:

  ```
  aws iotsitewise update-gateway \
      --gateway-id a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE \
      --gateway-name "UpdatedGatewayName"
  ```

  This command produces no output when successful.

For more information, see [update-gateway](https://docs.aws.amazon.com/cli/latest/reference/iotsitewise/update-gateway.html) in the AWS CLI Command Reference.

------

## Update gateway capability configuration
<a name="manage-gateway-update-capability"></a>

------
#### [ Console ]

**To update gateway capability configuration**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the navigation pane, choose **Edge gateways**.

1. Choose the name of the gateway you want to update.

1. In the **Data sources** section, choose **Edit**.

1. Update the data source configuration as needed.

1. Choose **Save**.

------
#### [ AWS CLI ]

To update a gateway's capability configuration using AWS CLI, follow these steps:
+ Use the update-gateway-capability-configuration command to update the capability configuration:

  ```
  aws iotsitewise update-gateway-capability-configuration \
      --gateway-id a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE \
      --capability-namespace "iotsitewise:opcuacollector:1" \
      --capability-configuration '{
          "sources": [
              {
                  "name": "OPC-UA Server",
                  "endpoint": {
                      "certificateTrust": {
                          "type": "TrustAny"
                      },
                      "endpointUri": "opc.tcp://10.0.0.1:4840",
                      "securityPolicy": "NONE",
                      "messageSecurityMode": "NONE",
                      "identityProvider": {
                          "type": "Anonymous"
                      }
                  },
                  "measurementDataStreamPrefix": ""
              }
          ]
      }'
  ```

  This command returns the capability namespace and sync status:

  ```
  {
      "capabilityNamespace": "iotsitewise:opcuacollector:1",
      "capabilitySyncStatus": "CONFIGURING"
  }
  ```

For more information, see [update-gateway-capability-configuration](https://docs.aws.amazon.com/cli/latest/reference/iotsitewise/update-gateway-capability-configuration.html) in the AWS CLI Command Reference.

------

## Tag gateway resources
<a name="manage-gateway-tag-resources"></a>

------
#### [ Console ]

**To tag a gateway resource**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the navigation pane, choose **Edge gateways**.

1. Choose the name of the gateway you want to tag.

1. Choose the **Tags** tab.

1. Choose **Manage tags**.

1. Choose **Add new tag** and enter a key and value for each tag.

1. Choose **Save**.

------
#### [ AWS CLI ]

To add tags to a gateway using AWS CLI, follow these steps:
+ Use the tag-resource command to add tags to a gateway:

  ```
  aws iotsitewise tag-resource \
      --resource-arn "arn:aws:iotsitewise:us-east-1:123456789012:gateway/a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE" \
      --tags '{
          "Department": "Operations",
          "Project": "FactoryAutomation"
      }'
  ```

  This command produces no output when successful.

For more information, see [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/iotsitewise/tag-resource.html) in the AWS CLI Command Reference.

------

## List tags for a gateway
<a name="manage-gateway-list-tags"></a>

------
#### [ Console ]

**To list tags for a gateway**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the navigation pane, choose **Edge gateways**.

1. Choose the name of the gateway you want to view tags for.

1. Choose the **Tags** tab.

1. View the list of tags associated with the gateway.

------
#### [ AWS CLI ]

To list the tags associated with a gateway using AWS CLI, follow these steps:
+ Use the list-tags-for-resource command to list tags for a gateway:

  ```
  aws iotsitewise list-tags-for-resource \
      --resource-arn "arn:aws:iotsitewise:us-east-1:123456789012:gateway/a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE"
  ```

  This command returns the tags associated with the gateway:

  ```
  {
      "tags": {
          "Environment": "Production",
          "Location": "Factory1",
          "Department": "Operations",
          "Project": "FactoryAutomation"
      }
  }
  ```

For more information, see [list-tags-for-resource](https://docs.aws.amazon.com/cli/latest/reference/iotsitewise/list-tags-for-resource.html) in the AWS CLI Command Reference.

------

## Remove tags from a gateway
<a name="manage-gateway-untag-resources"></a>

------
#### [ Console ]

**To remove tags from a gateway**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the navigation pane, choose **Edge gateways**.

1. Choose the name of the gateway you want to remove tags from.

1. Choose the **Tags** tab.

1. Choose **Manage tags**.

1. Choose the remove icon (X) next to each tag you want to remove.

1. Choose **Save**.

------
#### [ AWS CLI ]

To remove tags from a gateway using AWS CLI, follow these steps:
+ Use the untag-resource command to remove tags from a gateway:

  ```
  aws iotsitewise untag-resource \
      --resource-arn "arn:aws:iotsitewise:us-east-1:123456789012:gateway/a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE" \
      --tag-keys '["Project", "Department"]'
  ```

  This command produces no output when successful.

For more information, see [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/iotsitewise/untag-resource.html) in the AWS CLI Command Reference.

------

## Update the version of an AWS IoT SiteWise component
<a name="update-component-version"></a>

Update the AWS IoT SiteWise gateway component on your AWS IoT Greengrass core device to ensure your access to the latest features, performance improvements, and security patches.

**To update an AWS IoT SiteWise component on AWS IoT Greengrass**

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the left navigation pane, choose **Edge gateways**.

1. Select the gateway to edit and choose **Edit**.

1. In **Edge Capabilities**, under **Software versions**, choose **Software updates available**. The **Edit software versions** page appears.

1. Choose the component version.
**Note**  
It's recommend to select the latest version available. Keeping gateway components up-to-date helps you maintain optimal functionality for industrial data collection and processing.

1. Choose **Deploy**. This starts an AWS IoT Greengrass V2 deployment to update the AWS IoT SiteWise component on the gateway.

## Delete a SiteWise Edge gateway
<a name="manage-gateway-delete-gateway"></a>

------
#### [ Console ]

**To delete the SiteWise Edge gateway**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the navigation pane, choose **Edge gateways**.

1. Choose the gateway you want to delete.

1. Choose **Delete**.

1. To confirm you want to delete the gateway, type "delete" and then choose **Delete** in the window that appears.

------
#### [ AWS CLI ]

To delete a gateway using AWS CLI, follow these steps:

1. List your gateways to identify the gateway ID of the gateway you want to delete.

   ```
   aws iotsitewise list-gateways
   ```

   This command returns a list of your gateways with their IDs, names, and other information:

   ```
   {
       "gatewaySummaries": [
           {
               "gatewayId": "a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE",
               "gatewayName": "ExampleCorpGateway",
               "gatewayCapabilitySummaries": [
                   {
                       "capabilityNamespace": "iotsitewise:opcuacollector:1",
                       "capabilitySyncStatus": "IN_SYNC"
                   }
               ],
               "creationDate": 1588369971.457,
               "lastUpdateDate": 1588369971.457
           }
       ]
   }
   ```

1. Delete the gateway by specifying its ID:

   ```
   aws iotsitewise delete-gateway --gateway-id a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE
   ```

   This command produces no output when successful.
**Note**  
When you delete a gateway, some of the gateway's files remain in your gateway's file system.

1. To verify that the gateway has been deleted, you can list your gateways again:

   ```
   aws iotsitewise list-gateways
   ```

   The deleted gateway should no longer appear in the list.

For more information, see [delete-gateway](https://docs.aws.amazon.com/cli/latest/reference/storagegateway/delete-gateway.html) in the AWS CLI Command Reference.

------