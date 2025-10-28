# Step 2: Create the AWS IoT thing,

certificate, and private key

Create a thing in the AWS IoT registry to represent your Raspberry Pi.

1. In the [AWS IoT
   console](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home"), in the navigation pane, choose
   **Manage**, and then choose
   **Things**.
2. If a **You don't have any things yet** dialog box is
   displayed, choose **Register a thing**. Otherwise, choose
   **Create**.
3. On the **Creating AWS IoT things** page, choose
   **Create a single thing**.
4. On the **Add your device to the device registry** page,
   enter a name for your IoT thing (for example,
   `RaspberryPi`), and then choose
   **Next**. You can't change the name of a thing after
   you create it. To change a thing's name, you must create a new thing, give
   it the new name, and then delete the old thing.
5. On the **Add a certificate for your thing** page, choose
   **Create certificate**.
6. Choose the **Download** links to download the
   certificate, private key, and root CA certificate.

###### Important

This is the only time you can download your certificate and private
key. 7. To activate the certificate, choose **Activate**. The
certificate must be active for a device to connect to AWS IoT. 8. Choose **Attach a policy**. 9. For **Add a policy for your thing**, choose
**MoistureSensorPolicy**, and then choose
**Register Thing**.
