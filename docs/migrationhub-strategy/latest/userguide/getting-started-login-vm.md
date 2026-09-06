

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Step 3: Sign in to the Strategy Recommendations collector
<a name="getting-started-login-vm"></a>

This section describes how to sign in to the deployed Migration Hub Strategy Recommendations application data collector. How you sign in to the collector depends on how you deployed it.
+  [Sign in to the collector deployed in the vCenter based environment](#getting-started-login-vcenter)
+ [Sign in to the collector deployed as an Amazon EC2 instance](#getting-started-login-ec2)

## Sign in to the collector deployed in the vCenter based environment
<a name="getting-started-login-vcenter"></a>

**To sign in to the Strategy Recommendations collector deployed in the vCenter based environment**

1. Use the following command to connect to the collector using an SSH client.

   ```
   ssh ec2-user@CollectorIPAddress
   ```

1. When prompted for a password, enter the default password **aq1@WSde3**. You must change the password the first time you sign in.

## Sign in to the collector deployed as an Amazon EC2 instance
<a name="getting-started-login-ec2"></a>

**To sign in to the Strategy Recommendations collector deployed as an Amazon EC2 instance**
+ Use the following command to connect to the collector using an SSH client.

  ```
  ssh -i "{{Keyname.pem}}" ec2-user@CollectorIPAddress
  ```

  Keyname.pem is the private key that was generated when you launched the Amazon EC2 instance from the collector AMI.

## Next step
<a name="getting-started-login-vm-next"></a>

 [Step 4: Set up the Strategy Recommendations collector](getting-started-collector-setup.md) 