# Migrating workloads: Windows pre-ingestion validation

You can use the pre-WIGs validator script to validate that your instance is ready for ingestion into your AMS account. The workload ingest (WIGS)
pre-ingestion validation performs checks such as operating system type,
available disk space, the existence of conflicting third party software, and so on. When run, the WIGS pre-ingestion
validation produces an on-screen table and an optional log file.
The results provide a pass/fail status for each validation check along with the failure reason. In addition, you can customize the validation tests.

Frequently asked questions:

- **How do I use Windows WIGS pre-ingestion validation?**

You can run the validation from a GUI and web browser, or you can use Windows PowerShell, SSM Run Command, or SSM Session Manager.

**Option 1: Run from a GUI and web browser**

To run the Windows pre-WIGs validation from a GUI and web browser, do the following:

    1. Download a ZIP file with the validation scripts:


    [Windows WIGS Pre-ingestion Validation ZIP file](samples/windows-prewigs-validation.md "samples/windows-prewigs-validation.md").
    2. Unzip attached rules to a directory of your choice.
    3. Follow the instructions in the **README.md** file.

**Option 2: Run from Windows PowerShell, SSM Run Command, or SSM Session Manager**

**Windows 2016 and later**

    1. Download the ZIP file with the validation scripts.



    ```
    $DestinationFile = "$env:TEMP\WIGValidation.zip"

    $Bucket = 'https://docs.aws.amazon.com/managedservices/latest/appguide/samples/windows-prewigs-validation.zip'
    $DestinationFile = "$env:TEMP\WIGValidation.zip"
    $ScriptFolder = "$env:TEMP\AWSManagedServices.PreWigs.Validation"
    ```
    2. Remove existing files from `C:\Users\AppData\Local\Temp\AWSManagedServices.PreWigs.Validation`.



    ```
    Remove-Item $scriptFolder -Recurse -Force -ErrorAction Ignore
    ```
    3. Invoke the script.



    ```
    Invoke-WebRequest -Uri $bucket -OutFile $DestinationFile
    Add-Type -Assembly "system.io.compression.filesystem"
    ```
    4. Unzip attached files to a directory of your choice.



    ```
    [io.compression.zipfile]::ExtractToDirectory($DestinationFile, $env:TEMP)
    ```
    5. Run the validation script interactively and view the results.



    ```
    Import-Module .\AWSManagedServices.PreWigs.Validation.psm1 -force
    Invoke-PreWIGsValidation -RunWithoutExitCodes
    ```
    6. (Optional) To capture the error codes listed in the **Exit Codes** section, run the script without the `RunWithoutExitCodes` option. Note that this command terminates the active PowerShell session.



    ```
    Import-Module .\AWSManagedServices.PreWigs.Validation.psm1 -force
    Invoke-PreWIGsValidation
    ```

**Windows 2012 R2 and earlier**

If you're running Windows Server 2012R2 or below, you must set TLS before you download the zip file. To set TLS, complete the following steps:

    1. Download the ZIP file with the validation scripts.



    ```
    $DestinationFile = "$env:TEMP\WIGValidation.zip"

    $Bucket = 'https://docs.aws.amazon.com/managedservices/latest/appguide/samples/windows-prewigs-validation.zip'
    $DestinationFile = "$env:TEMP\WIGValidation.zip"
    $ScriptFolder = "$env:TEMP\AWSManagedServices.PreWigs.Validation"
    ```
    2. If there are existing validation files, then remove them.



    ```
    Remove-Item $scriptFolder -Recurse -Force -ErrorAction Ignore
    ```
    3. Set the TLS version.



    ```
    [System.Net.ServicePointManager]::SecurityProtocol = 'TLS12'
    ```
    4. Download WIG validation.



    ```
    Invoke-WebRequest -Uri $bucket -OutFile $DestinationFile
    Add-Type -Assembly "system.io.compression.filesystem"
    ```
    5. Unzip the attached rules to a directory of your choice.



    ```
    [io.compression.zipfile]::ExtractToDirectory($DestinationFile, $env:TEMP)
    ```
    6. Run the validation script interactively and view the results.



    ```
    Import-Module .\AWSManagedServices.PreWigs.Validation.psm1 -force
    Invoke-PreWIGsValidation -RunWithoutExitCodes
    ```
    7. (Optional) To capture the error codes listed in the **Exit Codes** section, run the script without the RunWithoutExitCodes option. Note that this command terminates the active PowerShell session.



    ```
    Import-Module .\AWSManagedServices.PreWigs.Validation.psm1 -force
    Invoke-PreWIGsValidation
    ```

###### Note

You can download and run the PowerShell scripts. To do this, download the [pre-wigs-validation-powershell-scripts.zip](samples/pre-wigs-validation-powershell-scripts.md "samples/pre-wigs-validation-powershell-scripts.md").

- **What validations are performed by the Windows WIGS Pre-Ingestion Validation?**

The AMS Windows WIGS pre-ingestion validation solution validates the following:

    1. There is at least 10 Gigabytes free on the boot volume.
    2. The operating system is supported by AMS.
    3. The instance has a specific instance profile.
    4. The instance does not contain antivirus software or virtualization software.
    5. DHCP is enabled on at least one network adapter.
    6. The instance is ready for Sysprep.




    	+ For 2008 R2 and 2012 Base and R2, Sysprep verifies that:




    		- There is an unattend.xml file
    		- The sppnp.dll file(if present) is not corrupt
    		- The Operating System has not been upgraded
    		- Sysprep has not run more than the maximum number of times per Microsoft guidelines
    	+ For 2016 and above, all of above checks are skipped as neither cause problems for that OS
    7. The Windows management instrumentation (WMI) subsystem is healthy.
    8. Required drivers are installed.
    9. The SSM Agent and is installed and running.
    10. Warning is given to verify if the machine is in grace period due to the RDS License Configuration.
    11. Required registry keys are set properly. For more details, see the README in the Pre-ingestion Validation zip file.

- **Why is there support for a custom configuration file?**

The scripts are designed to run on both on-premise physical servers and on AWS EC2 instances.
However, as shown in the list above, some tests will fail when run on-premises. For example, a
physical server in a datacenter would not have an instance profile. In cases like these, you can edit
the configuration file to skip the instance profile test to avoid confusion.

- **How do I ensure I have the latest version of the script?**

An up-to-date version of the Windows WIGS pre-ingestion validation solution will be available under
the **AMS Helper Files** section on the main Documentation page.

- **Is the script read-only?**

The script is designed to be read-only except for the log files it produces, but best practices
should be followed to run the script in a non-production environment.

- **Is WIGS Pre-Ingestion Validation available for Linux?**

Yes. The Linux version launched on 31 October, 2019. It is available under the
**AMS Helper Files** section on the main Documentation page.
