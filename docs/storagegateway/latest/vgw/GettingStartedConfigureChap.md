# Configuring CHAP authentication for your

volumes

In Storage Gateway, your iSCSI initiators connect to your volumes as iSCSI targets. Storage Gateway
uses Challenge-Handshake Authentication Protocol (CHAP) to authenticate iSCSI and initiator
connections. CHAP provides protection against playback attacks by requiring authentication
to access storage volume targets. For each volume target, you can define one or more CHAP
credentials. You can view and edit these credentials for the different initiators in the
Configure CHAP credentials dialog box.

###### To configure CHAP credentials

1. In the Storage Gateway Console, choose **Volumes** and select the volume
   for which you want to configure CHAP credentials.
2. For **Actions**, choose **Configure CHAP
   authentication**.
3. For **Initiator name**, type the name of your initiator. The name
   must be at least 1 character and at most 255 characters long.
4. For **Initiator secret**, provide the secret phrase you want to
   use to authenticate your iSCSI initiator. The initiator secret phrase must be at
   least 12 characters and at most 16 characters long.
5. For **Target secret**, provide the secret phrase you want used to
   authenticate your target for mutual CHAP. The target secret phrase must be at least
   12 characters and at most 16 characters long.
6. Choose **Save** to save your entries.
   To view or update CHAP credentials, you must have the necessary IAM role permissions that
   allow you to perform that operation.

## Viewing and editing CHAP credentials

You can add, remove or update CHAP credentials for each user. You must have the
necessary IAM role permissions to view or edit CHAP credentials, and initiator target
must be attached to a functioning gateway.

###### To add CHAP credentials

1. In the Storage Gateway Console, choose **Volumes** and select the
   volume for which you want to add CHAP credentials.
2. For **Actions**, choose **Configure CHAP
   authentication**.
3. In the Configure CHAPS page, provide the **Initiator name**,
   **Initiator secret**, and **Target
   secret** in the respective boxes and choose
   **Save**.

###### To remove CHAP credentials

1. In the Storage Gateway Console, choose **Volumes** and select the
   volume for which you want to remove CHAP credentials.
2. For **Actions**, choose **Configure CHAP
   authentication**.
3. Click the **X** next to the credentials you want to remove
   and choose **Save**.

###### To update CHAP credentials

1. In the Storage Gateway Console, choose **Volumes** and select the
   volume for which you want to update CHAP.
2. For **Actions**, choose **Configure CHAP
   authentication**.
3. In Configure CHAP credentials page, change the entries for the credentials you
   to update.
4. Choose **Save**.
