# Migrating workloads: Linux pre-ingestion validation

You can validate that your instance is ready for ingestion into your AMS account. The workload ingest (WIGS)
pre-ingestion validation performs checks such as operating system type,
available disk space, the existence of conflicting third party software, etc. When executed, the WIGS pre-ingestion
validation produces an on-screen table, with an optional log file.
The results provide a pass/fail status for each validation check along with the reason for any failures. In addition,
you can customize the validation tests to suit your needs.

Frequently asked questions:

- **How do I use Linux WIGS pre-ingestion validation?**

Follow these steps to download and use the AMS Linux WIGS pre-ingestion validation scripts:

    1. Download a ZIP file with the validation scripts


    [Linux WIGS Pre-ingestion Validation zip file](samples/linux-prewigs-validation.md "samples/linux-prewigs-validation.md").
    2. Unzip attached rules to a directory of your choice.
    3. Follow the instructions in the **readme.md** file.

- **What validations are performed by the Linux WIGS pre-ingestion validation?**

The AMS Linux WIGS pre-ingestion validation solution validates the following:

    1. There are at least 5 Gigabytes free on the boot volume.
    2. The operating system is supported by AMS.
    3. The instance has a specific instance profile.
    4. The instance does not contain Antivirus software or Virtualization software.
    5. SSH is properly configured.
    6. The instance has access to Yum Repositories.
    7. Enhanced networking drivers are installed.
    8. The instance has the SSM Agent and it is running.

- **Why is there support for a custom configuration file?**

The scripts are designed to run on both on-premise physical servers and on AWS EC2 instances.
However, as shown in the list above, some tests will fail when run on-premises. For example, a
physical server in a datacenter would not have an instance profile. In cases like these,
you can edit the configuration file to skip the instance profile test to avoid confusion.

- **How do I ensure I have the latest version of the script?**

An up-to-date version of the Linux WIGS Pre-Ingestion Validation solution will be available
under **AMS Helper Files** section on the main Documentation page.

- **Is the script read-only?**

The script is designed to be read-only except for the log files it produces, but best practices
should be followed to run the script in a non-production environment.

- **Is WIGS pre-ingestion validation available for Windows?**

Yes. It is available under the **AMS Helper Files** section on the main
Documentation page.
