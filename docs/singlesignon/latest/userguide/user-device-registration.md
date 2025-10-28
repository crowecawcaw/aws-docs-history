# Registering your device for MFA

For users in the Identity Center directory, use the following procedure within the
AWS access portal to register your new device for multi-factor authentication (MFA).

###### Important

MFA in IAM Identity Center is currently not supported for [external identity providers](manage-your-identity-source-idp.md "manage-your-identity-source-idp.md").

## Before you begin

We recommend that you first download the appropriate Authenticator app onto your device
before starting the steps in this procedure. For a list of apps that you can use for MFA
devices, see [Virtual authenticator apps](mfa-types.md#mfa-types-apps "mfa-types.md#mfa-types-apps").

## Register your device

###### To register your device for use with MFA

1. Sign in to your AWS access portal. For more information, see [Signing in to the AWS access portal](howtosignin.md "howtosignin.md").
2. Near the top-right of the page, choose **MFA devices**.
3. On the **Multi-factor authentication (MFA) devices** page, choose
   **Register device**.

###### Note

If the **Register MFA device** option is grayed out, contact your
administrator for assistance with registering your device. 4. On the **Register MFA device** page, select one of the following MFA
device types, and follow the instructions:

    * **Authenticator app**




    	1. On the **Set up the authenticator app** page, you might
    	 notice configuration information for the new MFA device, including a QR code
    	 graphic. The graphic is a representation of the secret key that is available for
    	 manual entry on devices that do not support QR codes.
    	2. Using the physical MFA device, do the following:




    		1. Open a compatible MFA authenticator app. For a list of tested apps that
    		 you can use with MFA devices, see [Virtual authenticator apps](mfa-types.md#mfa-types-apps "mfa-types.md#mfa-types-apps"). If the MFA app supports multiple accounts
    		 (multiple MFA devices), choose the option to create a new account (a new MFA
    		 device).
    		2. Determine whether the MFA app supports QR codes, and then do one of the
    		 following on the **Set up the authenticator app**
    		 page:




    			1. Choose **Show QR code**, and then use the app to scan
    			 the QR code. For example, you might choose the camera icon or choose an
    			 option similar to **Scan code**. Then use the device's
    			 camera to scan the code.
    			2. Choose **show secret key**, and then enter that
    			 secret key into your MFA app.


    			###### Important

    			When you configure an MFA device for IAM Identity Center, we recommend that you
    			 save a copy of the QR code or secret key *in a
    			 secure place*. This can help if you lose the phone or have
    			 to reinstall the MFA authenticator app. If either of those things
    			 happen, you can quickly reconfigure the app to use the same MFA
    			 configuration.
    	3. On the **Set up the authenticator app** page, under
    	 **Authenticator code**, enter the one-time password that
    	 currently appears on the physical MFA device.


    	###### Important

    	Submit your request immediately after generating the code. If you generate
    	 the code and then wait too long to submit the request, the MFA device is
    	 successfully associated with your user, but the MFA device is out of sync. This
    	 happens because time-based one-time passwords (TOTP) expire after a short period
    	 of time. If this happens, you can sync the device again.
    	4. Choose **Assign MFA**. The MFA device can now start
    	 generating one-time passwords and is now ready for use with AWS.


    * **Security key** or **Built-in
     authenticator**




    	1. On the **Register your user's security key** page, follow the
    	 instructions provided by your browser or platform.


    	###### Note

    	The experience varies based on the browser or platform. After your device is
    	 successfully registered, you can associate a friendly display name with your
    	 newly enrolled device. To to change the name, choose
    	 **Rename**, enter the new name, and then choose
    	 **Save**.
