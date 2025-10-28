# Step 8: Test the end user experience

To verify the end user can successfully access the end user console view and launch your
product, sign in to AWS as the end user and perform those tasks.

###### To verify that the end user can access the end user console

1. Follow the instructions to [Sign in as an IAM user](../../../IAM/latest/UserGuide/console.md "../../../IAM/latest/UserGuide/console.md") in the
   _IAM User guide_.
2. In the menu bar, choose the AWS Region in which you created the
   `Engineering Tools` portfolio. For this tutorial, choose **us-east-1 region**.
3. Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/") to see:
   - **Products** – The products that the user can use.
   - **Provisioned products** – The provisioned
     products that the user has launched.

###### To verify the end user can launch the Linux Desktop product

Note that for this tutorial, choose **us-east-1
region**.

1. In the **Products** section of the console, choose
   **Linux Desktop**.
2. Choose **Launch product** to start the wizard that configures your product.
3. On the **Launch: Linux Desktop** page, enter
   `Linux-Desktop` for the provisioned product name.
4. On the **Parameters** page, enter the following and choose
   **Next**:
   - **Server size** – Choose `t2.micro`.
   - **Key pair** – Select the key pair that you created in [Step 2: Create a key pair](getstarted-keypair.md "getstarted-keypair.md").
   - **CIDR range** – Enter a valid CIDR range for the IP address to
     connect to the instance. You can use the default value (0.0.0.0/0) to allow access from
     any IP address, then your IP address, followed by `/32` to restrict
     access to your IP address only, or something in between.

5. Choose **Launch product** to launch the stack. The console
   displays the stack details page for the Linux-Desktop stack. The initial status of the
   product is **Under change**. It takes several minutes for AWS Service Catalog to launch the product. To see the current status, refresh your browser.
   After the product launches, the status is A**vailable**.
