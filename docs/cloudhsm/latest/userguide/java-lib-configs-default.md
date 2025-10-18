# Configure the AWS CloudHSM`CloudHsmProvider` class with a file (Default
 configuration)

The default way to configure the AWS CloudHSM `CloudHsmProvider` class is with a file.

When you instantiate `CloudHsmProvider` using default constructor, by default it will look for configuration file in `/opt/cloudhsm/etc/cloudhsm-jce.cfg` path in Linux. 
 This configuration file can be configured using the `configure-jce`. 

An object created using the default constructor will use the default CloudHSM provider name `CloudHSM`. The provider name is useful to interact with JCE to let it know which provider to use for various operation. 
 An example to use CloudHSM provider name for Cipher operation is as below:


```
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding", "CloudHSM");
```
