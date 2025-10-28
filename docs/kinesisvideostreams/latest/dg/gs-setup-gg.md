# Set up the AWS IoT Greengrass V2 core device on the device

Follow these procedures to install the AWS IoT Greengrass core nucleus software on the Amazon EC2
instance.

###### Set up the AWS IoT Greengrass core device

1. Sign in to the AWS Management Console, [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").

Verify that the appropriate Region is selected. 2. In the left navigation, select **Greengrass devices**,
**Core devices**. 3. Choose **Set up one core device**. 4. Complete the steps on the screen.

    * **Step 1: Register a Greengrass core device**.
     Type a name for the device.
    * **Step 2: Add to a thing group to apply a continuous
     deployment**. Select **No
     group**.
    * **Step 3: Install the Greengrass Core software**.
     Select **Linux**.




    	+ **Step 3.1: Install Java on the
    	 device**


    	Java is installed as part of [Create an Ubuntu Amazon EC2 instance](gs-ubuntu.md "gs-ubuntu.md").
    	 Return to that step if you don't have Java installed
    	 yet.
    	+ **Step 3.2: Copy AWS credentials onto the
    	 device**


    	Open the `bash/zsh` option and paste the export
    	 commands in the Amazon EC2 instance.
    	+ **Step 3.3: Run the installer**




    		1. Copy and run the **Download the
    		 installer** and **Run the
    		 installer** commands in the Ubuntu Amazon EC2
    		 instance.


    		###### Note

    		The **Run the installer**
    		 command will automatically update based on the
    		 name you chose in a previous step.
    		2. Make note of the token exchange service (TES) role
    		 that is created. You need it later.
    	###### Note

    	By default, the role created is called
    	 **GreengrassV2TokenExchangeRole**.
