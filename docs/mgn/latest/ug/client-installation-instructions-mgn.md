

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# MGN vCenter Client installation instructions
<a name="client-installation-instructions-mgn"></a>

To install the MGN vCenter Client, follow these steps:



1. Download the MGN vCenter Client installer onto a VM within your vCenter environment. You can download the client from this URL: `https://aws-application-migration-service-(region).s3.(region).amazonaws.com/latest/vcenter-client/linux/aws-vcenter-client-installer-init.py` Replace `(region)` with the AWS Region into which you are replicating. 

   This is an example of the installer link for us-east-1: `https://aws-application-migration-service-us-east-1.s3.us-east-1.amazonaws.com/latest/vcenter-client/linux/aws-vcenter-client-installer-init.py`

   If you need to validate the installer hash, the correct hash can be found here: `https://aws-application-migration-service-hashes-(region).s3.(region).amazonaws.com/latest/vcenter-client/linux/aws-vcenter-client-installer-init.py.sha512 `

   This is an example of the installer hash link for us-east-1: `https://aws-application-migration-service-hashes-us-east-1.s3.us-east-1.amazonaws.com/latest/vcenter-client/linux/aws-vcenter-client-installer-init.py.sha512`

1. In command prompt, navigate to the directory where you downloaded the MGN vCenter Client installer and run the installer with this command: `sudo python3 aws-vcenter-client-installer-init.py`  
![Command prompt showing execution of Python script for AWS vCenter Client installer.](http://docs.aws.amazon.com/mgn/latest/ug/images/agentless3.png)

1. The installer prompts you for your credentials, enter the required info in each field and then press **Enter**:   
![Terminal window displaying AWS access key details and endpoint information.](http://docs.aws.amazon.com/mgn/latest/ug/images/agentless4.png)
   + AWS Access Key ID – Enter the AWS Access Key ID you generated in the previous section.
   + AWS Secret Access Key – Enter the AWS Secret Access Key you generated in the previous section.
   + AWS Region name – The AWS Region of your account (for example, eu-west-1).
   + The Private Link endpoint for AWS Transform MGN (optional, leave blank if not using Private Link).
   + The VPC endpoint for Amazon S3 (optional, leave blank if not using a VPC endpoint).

1. The installer then prompts you to enter your vCenter information, enter the required info in each field and then press **Enter**:   
![Command line interface prompting for vCenter connection details including IP, port, and credentials.](http://docs.aws.amazon.com/mgn/latest/ug/images/agentless5.png)

   
   + vCenter IP or hostname
   + vCenter port (press Enter to use the default TCP Port 443)
   + vCenter username
   + vCenter password
   + Path to vCenter root CA certificate (optional) - To use SSL certificate validation, download the certificates from `https://<vcenter-ip>/certs/download.zip` ( example: `wget https://<vcenter-ip>/certs/download.zip --no-check-certificate`) then enter the path of the certificate (example: `/usr/local/src/lin/f7f2bd6e.0)`). Otherwise, press **Enter** to deactivate SSL certificate validation. 
**Note**  
The certificate must be located in a file that's readable to the vCenter client user, such as a shared directory. If the certificate is not located in a shared directory, you see a permission error in the logs (Error 13).
To use a certificate in your vCenter environment, you must setup a connection using a hostname. Using an IP does not work with a certificate.
It's a security best practice to use certificates. Customers that do not use certificated authentication are responsible for any security issues that may arise. 
   + Path to VDDK tarball - Provide the path to the VDDK tarball that you previously downloaded onto the VM. (example: `path/to/VMware-vix-disklib-7.0.3-21933544.x86_64.tar.gz`). You can download VDDK tarball from your Broadcom account.
   + Resource tags for the AWS vCenter client (optional) - Use this format for tagging: 

     KEY=VALUE [KEY=VALUE ...] add resource tags to the AWS vCenter client; use a space to separate each tag (e.g., --vcenter-client-tags tag1=val1 tag2=val2 tag3=val3)
   + Resource tags for source servers to be discovered by the AWS vCenter client (optional) - Use this format for tagging: 

     KEY=VALUE [KEY=VALUE ...] add resource tags to the source servers added by discovery; use a space to separate each tag (e.g., --vcenter-client-tags tag1=val1 tag2=val2 tag3=val3)

1. The installer downloads and installs the AWS vCenter client and registers it with AWS Transform MGN.  
![Terminal output showing successful download and installation of AWS vCenter client.](http://docs.aws.amazon.com/mgn/latest/ug/images/agentless6.png)

1. Once the AWS vCenter client has been installed, all of the VMs in your vCenter are added to AWS Transform MGN. The VMs are added in the DISCOVERED state.
**Note**  
If you have a significant number of VMs in your vCenter environment, it may take some time for all of the VMs to become visible in the MGN console. 
The MGN vCenter Appliance is excluded from the discovered servers list.

You can configure transparent proxy either by using an environment variable prior to the installation (Linux and Windows), or by using the --proxy-address flag in the Linux installer:
+ Using the installer: ./aws-vcenter-client-installer-init.py --proxy-address http://PROXY:PORT/
+ Using environment variable: export https\_proxy=http://PROXY:PORT/; ./aws-vcenter-client-installer-init.py

Make sure the proxy has a trailing forward slash.