# Step 4: Prepare and Run the SAP Installation Prerequisites Check

1. Download the SAP installation media for SWPM (the latest appropriate version for your desired NetWeaver installation), your desired NetWeaver software version for Windows, the latest compatible SAP kernel, and any other required files (such as: the host agent, IGS, database client tools, SAP GUI, the SAPCAR archiving tool, and the SAP download manager) to an attached EBS volume as described in the prerequisites (usually from Amazon S3 using the AWS CLI tools).
2. Run the SAP prerequisite checker via SWPM on the desired host servers to ensure that you have met SAP’s technical prerequisites. When you first run SWPM, you may have to enter the sign-in credentials of the Windows user that you’re currently logged in as.
3. Launch SWPM by running the `sapinst.exe` executable. Specify `SAPINST_USE_HOSTNAME=<FQDN>` when launching to override the default DNS name if necessary, for example, with `<hostname>.local`.
4. Complete the recommended prerequisite steps as identified by the SAP prerequisite checker as per your specific requirements. Some common prerequisites for Windows Server operating systems are:
   1. Ensure that the hostname is ⇐ 13 characters in an alphanumeric string (hyphens can also be included). This can be done at the command line using Windows PowerShell by executing the following command:

   ```
    Rename-Computer <new-hostname>
   ```

   2. Optionally add the server to your Active Directory domain (this can be done with [AWS Systems Manager](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-systems-manager-dx-domain/ "https://aws.amazon.com/premiumsupport/knowledge-center/ec2-systems-manager-dx-domain/")).
   3. Pagefile size will have a minimum recommended value based on services selected.
   4. Continuous Availability feature on Windows Server 2012 R2 can result in long wait times. See [SAP note 1823833](https://launchpad.support.sap.com/#/notes/1823833 "https://launchpad.support.sap.com/#/notes/1823833") for a fix.
