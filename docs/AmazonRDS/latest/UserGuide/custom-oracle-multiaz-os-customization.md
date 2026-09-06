

# Customizing the OS in an RDS Custom for Oracle Multi-AZ deployment
<a name="custom-oracle-multiaz-os-customization"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

With RDS Custom for Oracle Multi-AZ deployments, you can customize the operating system and install third-party software on both primary and standby EC2 instances. Unlike Amazon RDS, RDS Custom for Oracle provides administrative access to the database environment and underlying operating system, allowing you to install monitoring tools, security agents, or custom applications in addition to Oracle databases.

When you customize the OS on a Multi-AZ deployment, you're responsible for ensuring that customizations exist on both primary and standby instances. This approach ensures application continuity during Multi-AZ failover and maintains consistent functionality across both instances.

## Requirements for customizing the OS in an RDS Custom for Oracle Multi-AZ deployment
<a name="cfo-os-maz-reqs"></a>

Before you customize the OS in a Multi-AZ deployment, be aware of the following requirements:
+ Install third-party software only on the `/rdsdbdata` mount point. The data volume (`/rdsdbdata`) is the only data that is replicated in a Multi-AZ deployment. The root volume (`/`) is replaced during OS patching, and the binary volume (`/rdsdbbin`) is replaced during database patching. Software installed on the root and binary volumes is lost during patching.
+ Ensure all customizations comply with AWS and Oracle licensing terms and conditions.
+ Before you convert from Single-AZ to Multi-AZ, make sure the HugePages settings in `/etc/sysctl.conf` work correctly.

## Identifying EC2 instances in an RDS Custom for Oracle Multi-AZ deployment
<a name="cfo-os-maz-identify-instances"></a>

When customizing your Multi-AZ instances, identify which Amazon EC2 instances serve as the primary and standby for your RDS Custom for Oracle deployment.

**To identify primary and standby EC2 instances**

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Choose your Multi-AZ RDS Custom for Oracle DB instance.

1. In the **Configuration** section, note the **Resource ID** (format: `db-{{nnnnnnn}}`).

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. In the search box, enter the Resource ID from step 4.

1. The search results show two instances: your primary and secondary. The instance with the active RDS Custom for Oracle database is the primary.

## Customizing the OS before creating an RDS Custom for Oracle Multi-AZ deployment
<a name="cfo-os-maz-convert"></a>

In this scenario, your current deployment is a Single-AZ DB instance. You can customize the OS and then convert your DB instance to a Multi-AZ deployment. If you're installing third-party software, and you have modified files on multiple volumes, this technique is recommended.

**To customize the OS before converting your Single-AZ to Multi-AZ**

1. Connect to the EC2 instance in your Single-AZ deployment using AWS Systems Manager Session Manager or SSH.

1. Perform either of the following customizations:
   + Install third-party software on the data volume (`/rdsdbdata`).
   + Customize files on the root volume (`/`).

1. Test your software or root volume customizations to ensure they work correctly.

1. Convert the Single-AZ DB instance to a Multi-AZ deployment by following the instructions in [Converting a Single-AZ deployment to a Multi-AZ deployment in RDS Custom for Oracle](custom-oracle-multiaz-modify-single-to-multi.md).

1. Verify that your customizations exist on both instances in the Multi-AZ deployment. For more information, see [Identifying EC2 instances in an RDS Custom for Oracle Multi-AZ deployment](#cfo-os-maz-identify-instances).

## Customizing the OS after creating an RDS Custom for Oracle Multi-AZ deployment
<a name="cfo-maz-soft-root"></a>

If you have an exiting Multi-AZ deployment, you can deploy your customizations using AWS Systems Manager or using manual techniques.

### Customizing the OS in a Multi-AZ deployment using AWS Systems Manager
<a name="cfo-os-maz-systems-manager"></a>

For existing Multi-AZ DB instances, we recommend Systems Manager as the most reliable way to apply customizations simultaneously to both primary and standby instances. This approach ensures consistency. For a general introduction to this service, see [What is AWS Systems Manager?](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html). To learn how to install software on both DB instances simultaneously, see [Install or update Distributor packages](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-working-with-packages-deploy.html).

### Customizing the OS in a Multi-AZ deployment manually
<a name="cfo-os-maz-create"></a>

In this scenario, your Multi-AZ deployment already exists, but you don't use AWS Systems Manager to deploy the customizations. You can customize your OS manually in either of the following ways:

**Customize the OS on the primary instance and replicate the changes**  
Multi-AZ deployment automatically replicates the `rdsdbdata` volume. You can customize the OS in the following ways:  
+ Install third-party software directly on the `/rdsdbdata` mount point.
+ To modify files on the root volume (`/`), create files on the data volume and then create a symbolic link from the root volume files to the data volume files. 

**Customize the OS on the primary and standby instances separately**  
In this approach, you customize the OS on the primary instance. Then you perform the same customizations on the standby instance.

**To customize the OS on the primary instance so that they are replicated automatically**

1. Identify the primary and standby DB instances using the procedure in [Identifying EC2 instances in an RDS Custom for Oracle Multi-AZ deployment](#cfo-os-maz-identify-instances).

1. Connect to the primary EC2 instance using Session Manager or SSH.

1. Use either of the following techniques, depending on your business requirements:  
**Install third-party software**  
Install your software on the `/rdsdbdata` mount point.  

   ```
   sudo mkdir -p /rdsdbdata/custom-software
   cd /rdsdbdata/custom-software
   # Install your software here
   ```  
**Customize the root volume**  
Create symbolic links from OS configuration files on the root volume to files on the data volume. For example, create file `/rdsdbdata/customizations/sysctl.conf`, and then create a symbolic link at `/etc/sysctl.conf` that points to `/rdsdbdata/customizations/sysctl.conf`.  

   ```
   sudo mkdir -p /rdsdbdata/customizations
   sudo mv /etc/sysctl.conf /rdsdbdata/customizations/sysctl.conf
   sudo ln -sf /rdsdbdata/customizations/sysctl.conf /etc/sysctl.conf
   ```

1. Test your software or root volume customizations to ensure they work correctly.

1. Connect to the standby instance and verify that the synchronous replication has copied your software or root volume customizations to the `/rdsdbdata` directory.

## Customizing the binary volume in an RDS Custom for Oracle Multi-AZ deployment
<a name="cfo-os-maz-bin"></a>

You can apply a database patch to the binary volume (`/rdsdbbin`) in an RDS Custom for Oracle Multi-AZ deployment. You must apply the patch to the primary and standby instances. Consider the following guidelines:
+ When you perform a one-off patch, we recommend that you create a new CEV with the new one-off patch included in the manifest. 
+ To apply a one-off patch manually, make sure to unzip the one-off patch in both the primary and secondary EC2 instances. Applying the patch and running `datapatch` is required only on the primary Multi-AZ instance.
+ If you patch the database using a different CEV, the binary volume is replaced. Make sure to include the one-off patch in the manifest of the new CEV.

## Best practices for customizing the OS
<a name="cfo-os-maz-bp"></a>

Follow these best practices when customizing the OS on RDS Custom for Oracle Multi-AZ instances:

**Test in non-production environments**  
Always test customizations in a non-production environment before applying them to production instances.

**Document all changes**  
Maintain detailed documentation of all customizations for future reference and troubleshooting. We recommend that you store your customizations in a script that you can be applied anytime, just in case.

**Verify on both instances**  
Regularly verify that customizations are present and functioning correctly on both primary and standby instances.

**Use Systems Manager for consistency**  
Use Systems Manager for consistent application of changes across instances, especially for existing Multi-AZ deployments.