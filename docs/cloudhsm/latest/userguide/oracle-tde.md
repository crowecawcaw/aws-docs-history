

# Oracle database transparent data encryption (TDE) with AWS CloudHSM
<a name="oracle-tde"></a>

Transparent Data Encryption (TDE) is used to encrypt database files. Using TDE, database software encrypts data before storing it on disk. The data in the database's table columns or tablespaces are encrypted with a table key or tablespace key. Some versions of Oracle's database software offer TDE. In Oracle TDE, these keys are encrypted with a TDE master encryption key. You can achieve greater security by storing the TDE master encryption key in the HSMs in your AWS CloudHSM cluster.

![Store the Oracle TDE master encryption key in AWS CloudHSM.](http://docs.aws.amazon.com/cloudhsm/latest/userguide/images/tde-master-key-in-hsm.png)


In this solution, you use Oracle Database installed on an Amazon EC2 instance. Oracle Database integrates with the [AWS CloudHSM software library for PKCS \#11](pkcs11-library.md) to store the TDE master key in the HSMs in your cluster.

**Important**  
 We recommend installing Oracle Database on an Amazon EC2 instance.

Complete the following steps to accomplish Oracle TDE integration with AWS CloudHSM.

**Topics**
+ [Step 1. Set up the prerequisites](#oracle-tde-prerequisites)
+ [Step 2: Update the Oracle database configuration](#oracle-tde-configure-database-and-generate-master-key)
+ [Step 3: Generate the Oracle TDE master encryption key](#oracle-tde-generate-master-key)

## Step 1. Set up the prerequisites
<a name="oracle-tde-prerequisites"></a>

To accomplish Oracle TDE integration with AWS CloudHSM, you need the following:
+ An active AWS CloudHSM cluster with at least one HSM.
+ An Amazon EC2 instance running the Amazon Linux operating system with the following software installed:
  + The AWS CloudHSM client and command line tools.
  + The AWS CloudHSM software library for PKCS \#11.
  + Oracle Database. AWS CloudHSM supports Oracle TDE integration. Client SDK 5.6 and higher support Oracle TDE for Oracle Database 19c. Client SDK 3 supports Oracle TDE for Oracle Database versions 11g and 12c.
+ A cryptographic user (CU) to own and manage the TDE master encryption key on the HSMs in your cluster.

Complete the following steps to set up all of the prerequisites.

**To set up the prerequisites for Oracle TDE integration with AWS CloudHSM**

1. Complete the steps in [Getting started](getting-started.md). After you do so, you'll have an active cluster with one HSM. You will also have an Amazon EC2 instance running the Amazon Linux operating system. The AWS CloudHSM client and command line tools will also be installed and configured. 

1. (Optional) Add more HSMs to your cluster. For more information, see [Adding an HSM to an AWS CloudHSM cluster](add-hsm.md). 

1. Connect to your Amazon EC2 client instance and do the following:

   1. [Install the AWS CloudHSM software library for PKCS \#11](pkcs11-library-install.md).

   1. Install Oracle Database. For more information, see the [Oracle Database documentation](https://docs.oracle.com/en/database/). Client SDK 5.6 and higher support Oracle TDE for Oracle Database 19c. Client SDK 3 supports Oracle TDE for Oracle Database versions 11g and 12c.

   1. Use the cloudhsm\_mgmt\_util command line tool to create a cryptographic user (CU) on your cluster. For more information about creating a CU, see [How to Manage HSM Users with CMU](create-users-cmu.md) and [HSM users](manage-hsm-users.md). 

## Step 2: Update the Oracle database configuration
<a name="oracle-tde-configure-database-and-generate-master-key"></a>

To update the Oracle Database configuration to use an HSM in your cluster as the *external security module*, complete the following steps. For information about external security modules, see [ Introduction to Transparent Data Encryption ](https://docs.oracle.com/database/122/ASOAG/introduction-to-transparent-data-encryption.htm) in the *Oracle Database Advanced Security Guide*. 

**To update the Oracle configuration**

1. Connect to your Amazon EC2 client instance. This is the instance where you installed Oracle Database.

1. Make a backup copy of the file named `sqlnet.ora`. For the location of this file, see the Oracle documentation. 

1. Use a text editor to edit the file named `sqlnet.ora`. Add the following line. If an existing line in the file begins with `encryption_wallet_location`, replace the existing line with the following one.

   ```
   encryption_wallet_location=(source=(method=hsm))
   ```

   Save the file.

1. Run the following command to create the directory where Oracle Database expects to find the library file for the AWS CloudHSM PKCS \#11 software library. 

   ```
   sudo mkdir -p /opt/oracle/extapi/64/hsm
   ```

1. Run the following command to copy the AWS CloudHSM software library for PKCS \#11 file to the directory that you created in the previous step. 

   ```
   sudo cp /opt/cloudhsm/lib/libcloudhsm_pkcs11.so /opt/oracle/extapi/64/hsm/
   ```
**Note**  
The `/opt/oracle/extapi/64/hsm` directory must contain only one library file. Remove any other files that exist in that directory. 

1. Run the following command to change the ownership of the `/opt/oracle` directory and everything inside it.

   ```
   sudo chown -R oracle:dba /opt/oracle
   ```

1. Start the Oracle Database.

## Step 3: Generate the Oracle TDE master encryption key
<a name="oracle-tde-generate-master-key"></a>

To generate the Oracle TDE master key on the HSMs in your cluster, complete the steps in the following procedure.

**To generate the master key**

1. Use the following command to open Oracle SQL\*Plus. When prompted, type the system password that you set when you installed Oracle Database. 

   ```
   sqlplus / as sysdba
   ```
**Note**  
For Client SDK 3, you must set the `CLOUDHSM_IGNORE_CKA_MODIFIABLE_FALSE` environment variable each time you generate a master key. This variable is only needed for master key generation. For more information, see "Issue: Oracle sets the PCKS \#11 attribute `CKA_MODIFIABLE` during master key generation, but the HSM does not support it" in [Known Issues for Integrating Third-Party Applications](ki-third-party.md). 

1. Run the SQL statement that creates the master encryption key, as shown in the following examples. Use the statement that corresponds to your version of Oracle Database. Replace {{<CU user name>}} with the user name of the cryptographic user (CU). Replace {{<password>}} with the CU password. 
**Important**  
Run the following command only once. Each time the command is run, it creates a new master encryption key. 
   + For Oracle Database version 11, run the following SQL statement.

     ```
     SQL> alter system set encryption key identified by "{{<CU user name>}}:{{<password>}}";
     ```
   + For Oracle Database version 12 and version 19c, run the following SQL statement.

     ```
     SQL> administer key management set key identified by "{{<CU user name>}}:{{<password>}}";
     ```

   If the response is `System altered` or `keystore altered`, then you successfully generated and set the master key for Oracle TDE. 

1. (Optional) Run the following command to verify the status of the *Oracle wallet*.

   ```
   SQL> select * from v$encryption_wallet;
   ```

   If the wallet is not open, use one of the following commands to open it. Replace {{<CU user name>}} with the name of the cryptographic user (CU). Replace {{<password>}} with the CU password. 
   + For Oracle 11, run the following command to open the wallet.

     ```
     SQL> alter system set encryption wallet open identified by "{{<CU user name>}}:{{<password>}}";
     ```

     To manually close the wallet, run the following command.

     ```
     SQL> alter system set encryption wallet close identified by "{{<CU user name>}}:{{<password>}}";
     ```
   + For Oracle 12 and Oracle 19c, run the following command to open the wallet.

     ```
     SQL> administer key management set keystore open identified by "{{<CU user name>}}:{{<password>}}";
     ```

     To manually close the wallet, run the following command.

     ```
     SQL> administer key management set keystore close identified by "{{<CU user name>}}:{{<password>}}";
     ```