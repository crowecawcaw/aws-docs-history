

# Updating your AD Connector service account credentials in AWS Management Console
<a name="ad_connector_update_creds"></a>

The AD Connector credentials you provide in Directory Service represent the service account that is used to access your existing on-premises directory. You can modify the service account credentials in Directory Service by performing the following steps.

**Note**  
If AWS IAM Identity Center is enabled for the directory, Directory Service must transfer the service principal name (SPN) from the current service account to the new service account. If the current service account does not have permission to delete the SPN or the new service account does not have permission to add the SPN, you are prompted for the credentials of a directory account that does have permission to perform both actions. These credentials are only used to transfer the SPN and are not stored by the service.

**To update your AD Connector service account credentials in Directory Service**

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/) navigation pane, under **Active Directory**, choose **Directories**.

1. Choose the directory ID link for your directory.

1. On the **Directory details** page, scroll down to the **Service account credentials** section.

1. In the **Service account credentials** section, choose **Update**. 

1. In the **Update service account credentials** dialog box, type the service account username and password. Reenter the password to confirm it and then choose **Update**.