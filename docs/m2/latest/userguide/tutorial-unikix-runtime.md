

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Tutorial: Deploy CardDemo application on NTT DATA
<a name="tutorial-unikix-runtime"></a>

This page guides you through the step-by-step process for deploying the CardDemo sample application on the AWS Mainframe Modernization replatform with NTT DATA Unikix runtime.

The CardDemo sample application is a simplified mainframe application designed and developed to test and showcase AWS and partner technology for mainframe migration and modernization use-cases. 

For more information about this application, see, [GitHub repository for CardDemo](https://github.com/aws-samples/aws-mainframe-modernization-carddemo).

**Topics**
+ [Deployment flow diagram](#tutorial-unikix-workflow)
+ [Prerequisites](#tutorial-unikix-prerequisites)
+ [Step 1: Prepare the environment](#tutorial-unikix-prepare)
+ [Step 2: Create a TPE region](#tutorial-unikix-tpe)
+ [Step 3: Create the BPE node and subsystem](#tutorial-unikix-bpe)
+ [Step 4: Compile and deploy CardDemo application](#tutorial-unikix-compile)
+ [Step 5: Import BPE and TPE catalog](#tutorial-unikix-import)
+ [Step 6: Start and connect TPE with BPE](#unikix-tutorial-connect)
+ [Step 7: Run the CardDemo application](#unikix-tutorial-run-application)
+ [Troubleshooting](#tutorial-unikix-troubleshoot)

## Deployment flow diagram
<a name="tutorial-unikix-workflow"></a>

The following diagram shows each step in the workflow for deploying an application on the NTT DATA Unikix runtime.

![The overall workflow of deploying the application on NTT DATA Unikix runtime.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-process.png)


## Prerequisites
<a name="tutorial-unikix-prerequisites"></a>
+ Follow the instructions provided in the [AWS Mainframe Modernization replatforming with NTT DATA](unikix.md) using the [NTT DATA UniKix Marketplace AMI](https://aws.amazon.com/marketplace/pp/prodview-eg227ymldsnx2).
+ Modify the instance metadata option **IMDSv2** to **Optional** as mentioned in [Restore the use of IMDSv1](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-existing-instances.html) in the *Amazon EC2 user guide*.
+ Download CardDemo runtime components for NTT DATA UniKix from the 

  [GitHub repository](https://github.com/aws-samples/aws-mainframe-modernization-carddemo/blob/main/samples/m2/unikix/UniKix_CardDemo_runtime_v1.zip).
+ Log in to UniKix runtime EC2 instance as `ec2-user`.
+ Extract the downloaded CardDemo runtime components using this link: [UniKix\_CardDemo\_runtime\_v1.zip](https://github.com/aws-samples/aws-mainframe-modernization-carddemo/blob/main/samples/m2/unikix/UniKix_CardDemo_runtime_v1.zip).
  + The extracted directory should contain `bin` and `migrated_app` directories.
  + Move both `bin` and `migrated_app` directories under your `$HOME` directory. The path would look like `/home/ec2-user`.
  + You should have the following directories in your `$HOME`:
    + `/home/ec2-user/bin`
    + `/home/ec2-user/migrated_app`
  + Move all the files inside the $HOME/bin directory the following command:
  + 
    + `chmod +x $HOME/bin/*`

## Step 1: Prepare the environment
<a name="tutorial-unikix-prepare"></a>

After completing the prerequisites, the first step is to prepare the environment where you want to deploy the CardDemo application.

1. Log in to UniKix runtime EC2 instance as `ec2-user`.

1. Observe the list of UniKix software that are prepackaged within the AMI, such as TPE, BPE, and COBOL, along with others from the NTT DATA UniKix product location by using the following command in your EC2 instance:

   ```
   ls -l /opt/software/
   ```

1. Examine the migrated CardDemo application. You will see all the source code, including BMS maps, COBOL programs, COBOL Copybooks, and JCLs. You will also find the export of BPE and TPE catalogs, CICS resource definitions, and the migrated data such as sequential files and VSAM files by doing this:

   ```
   ls  $HOME/migrated_app/*/*
   ```

1. Create folder structure by running the `create_project` script with the following command:

   ```
   sh $HOME/bin/create_project
   ```

1. Activate the CardDemo environment by sourcing the `carddemo.env` setup file using:

   ```
   source $HOME/bin/carddemo.env
   ```

## Step 2: Create a TPE region
<a name="tutorial-unikix-tpe"></a>

Once you have activated the environment where you want to deploy the application, you need to create a TPE region.

1. Create a TPE region using the `kixregion createRegion` command which requires inputs such as `$KIXSYS`, `$JAVA_HOME`, and `$KIXLICDIR`. These environment variables are already setup in the `carddemo.env` setup file.

   ```
   kixregion createRegion $KIXSYS $JAVA_HOME $KIXLICDIR
   ```

1. Configure the TPE region using the `kixregion setAttr` command.

   ```
   kixregion setAttr $KIXSYS server.tx.languages.cobol.enabled true
   kixregion setAttr $KIXSYS server.tx.languages.cobol.flavor vcobol
   kixregion setAttr $KIXSYS server.tx.languages.cobol.home $VCOBOL
   kixregion setAttr $KIXSYS maps.location $PROJECT_ROOT/maps
   kixregion setAttr $KIXSYS programs.location $PROJECT_ROOT/loadlib
   kixregion setAttr $KIXSYS environment.KIXDATA $KIXDATA
   kixregion setAttr $KIXSYS td.jobq.submission.node $EBMHOME
   kixregion setAttr $KIXSYS td.jobq.submission.subsys $EBMSYS
   ```

1. Generate the user environment file specific to this TPE region by executing the `kixregion createScript` command. This command creates or updates `$KIXSYS/bin/userenv` based on the TPE region configuration.

   ```
   kixregion createScript $KIXSYS
   ```

1. Activate TPE region by sourcing the user environment file (`$KIXSYS/bin/userenv`).

   ```
   source $KIXSYS/bin/userenv
   ```

1. Build the TPE region by running the `kixinstall2` command.

   ```
   kixinstall2
   ```

## Step 3: Create the BPE node and subsystem
<a name="tutorial-unikix-bpe"></a>

After creating a TPE region, you need to create the BPE node and subsystem by following these steps.

1. Change the ownership and permissions of `INSTEBM`.

   ```
   sudo chown root $INSTEBM 
   sudo chmod 4755 $INSTEBM
   ```

1. Create a BPE node using the `INSTEBM` command. The BPE node directory is provided as the input parameter.

   ```
   $INSTEBM $EBMHOME
   ```

1. Activate the batch environment by sourcing the `batchenv` file from the newly created BPE node.

   ```
   source $EBMHOME/batchenv
   ```

1. Create the BPE subsystem within this node using the Batch Administration Manager (bam). The `bam` command will open the Batch Administration Manager interface.

   ```
   bam
   ```

   1. Start the BPE node using the BAM interface. Choose option 2, **System Environments** from the main menu.  
![In Batch Administrator Manager, choose option 2 System Environments.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-1.png)

   1. Choose option 2, **Start/(Stop) Batch Node** to start the BPE node.   
![In System Environments, choose option 2 Start/Stop batch node.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-2.png)

   1. Once started, press the **Return key** twice to return to the BAM main menu.  
![Batch Node Startup completed screen.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-3.png)

   1. To create the BPE subsystem, choose option 3, **Applications & Subsystems**.  
![Option 3 Applications and Subsystems selected on the Batch Administrator Manager page.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-4.png)

   1. Then choose option 3, **Create a Subsystem**.  
![Option 3 Create a Subsystem selected on the Applications and Subsystems screen.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-5.png)

   1. Enter the subsystem name as `sys1`.  
![Entered sys1 on the Create screen.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-6.png)

   1. Choose option 3, **Data Management**.  
![Chose option 3 Data Management on the Create screen in Applications and Subsystem.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-7.png)

   1. Choose option 5, as the CardDemo application involves both sequential and VSAM files.  
![Choose option 5 to include sequential and VSAM files.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-8.png)

   1. (Optional). Press "R" to return to the **Create Menu** page, review the different configuration options available.

   1. On the **Create** page, enter "C" to create the subsystem `sys1`.  
![Press "C" on the keyboard to create subsystem sys1.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-9.png)

   1. Review the settings, and enter "C" to continue for the rest of the environment settings. These environment settings are pre populated due to the necessary environment variables defined in the `carddemo.env` setup file and the recommended folder structure being in place.

   1. Enter "y" to confirm and save the current environment settings.  
![Displays sys1 subsystem's environment setting completed. Also type "y" to save current settings.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-10.png)

   1. Enter "y" to display the log when building the subsystem.  
![Shows building sys1's NTT DATA COBOL runtime system on the screen.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-11.png)

   1. Press the **Return key** until you go back to the Main Menu and exit the BAM interface by selecting the **Quit** option.  
![Displays COBOL runtime system created. Also prompts to press Return to continue.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-12.png)  
![Returns to the Create menu and shows subsystem sys1 is created. And configuration is updated. Prompts to press return to continue.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-13.png)  
![Main Menu for Batch Administrator. Prompts to enter Q to quit this menu.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-bpe-14.png)

1. Activate the BPE subsystem by sourcing the `batchenv` with the subsystem name `sys1`.

   ```
   source $EBMHOME/batchenv sys1
   ```

## Step 4: Compile and deploy CardDemo application
<a name="tutorial-unikix-compile"></a>

In this step, you compile the COBOL programs and deploy application artifacts such as JCL, procedures, data files, and CICS resource definitions.

1. Activate the CardDemo environment again by sourcing the `carddemo.env` setup file.

   ```
   source $HOME/bin/carddemo.env
   ```

1. Navigate to the COBOL source directory.

   ```
   cd $MIGAPP_DIR/cbl
   ```

1. Compile Cobol program `CBACT01C.cbl` using `compile` script.

   ```
   compile CBACT01C.cbl
   ```

1. Compile all Cobol programs using `compile.all` script.

   ```
   compile.all
   ```

1. Navigate to BMS maps source directory.

   ```
   cd $MIGAPP_DIR/bms
   ```

1. Compile BMS map `COACTUP.bms` using `compbms` script.

   ```
   compbms COACTUP.bms
   ```

1. Compile all BMS maps using `compbms.all` script.

   ```
   compbms.all
   ```

1. Verify compiled binaries for COBOL and BMS maps.

   ```
   ls $PROJECT_ROOT/loadlib
   ls $PROJECT_ROOT/maps
   ```

1. Deploy other application artifacts such as JCL, procedures, data files, and CICS resource definitions using the `deploy_app` script.

   ```
   deploy_app
   ```

1. Navigate to the project JCL directory.

   ```
   cd $PROJECT_ROOT/jcl
   ```

1. Translate JCL ACCTFILE to BPE JCL Macro. Use the `mvstrans` command, utilizing the "-v" option for JCL verification, and the "-f" option to create the macro.

   ```
   mvstrans ACCTFILE -v
   mvstrans ACCTFILE -f
   ```

1. Translate JCL procedure REPROC to BPE JCL procedure Macro. Use the `mvstrans` command with the "-p" option along with the "-v" option for verification, and the "-f" option to create the macro.

   ```
   mvstrans REPROC -v -p
   mvstrans REPROC -f -p
   ```

1. Translate all JCLs and JCL procedures.

   ```
   for file in "./jmvs/*"; do mvstrans $file -f; done > jmvs.out
   for file in "./mvsp/*"; do mvstrans $file -p -f; done > mvsp.out
   ```

## Step 5: Import BPE and TPE catalog
<a name="tutorial-unikix-import"></a>

In this step, you import the BPE and TPE catalog using different commands.

1. Import BPE catalog using `loadcat` command.

   ```
   loadcat $MIGAPP_DIR/catlg/bpe/BPECAT*
   ```

1. Navigate to $KIXSYS directory.

   ```
   cd $KIXSYS
   ```

1. Import TPE catalog using `kiximpcat` command.

   ```
   kiximpcat -c CATALOG -l CATALOG.lst
   ```

1. Import CICS resource definitions using kiximptbl command.

   ```
   kiximptbl
   ```

## Step 6: Start and connect TPE with BPE
<a name="unikix-tutorial-connect"></a>

In this step, you need to start the previously created TPE region along with the BPE manager and connect these to be able to run the sample CardDemo application.

1. Run the `kixverify` command against all VSAM files to ensure they are reset and any previously opened files are closed.

   ```
   kixverify -r ALL
   ```

1. Start the TPE region.

   ```
   kixregion start $KIXSYS
   ```

1. Ensure that both BPE and TPE are connected. This is crucial as the VSAM files are owned by TPE, and any batch operation accessing the VSAM will require a connection to TPE.

   ```
   ebmsys -t
   ```  
![Displays the Subsystem name as sys1. TPE is connected and the TPE user is ec2-user.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-start-1.png)

## Step 7: Run the CardDemo application
<a name="unikix-tutorial-run-application"></a>

In this step, you run the CardDemo application in the TN3270 terminal emulator.

The UniKix runtime AMI comes with TN3270 terminal emulator that you can launch directly from the UniKix EC2 instance.

**Connect to TPE using TN3270 terminal emulator**
+ Launch TN3270 terminal using the `kixterm` command.

  ```
  kixterm
  ```  
![The main screen of TPE UniKix CardDemo sample application for mainframe.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-carddemo-00.png)

(Optional). If you want to use your own terminal emulator:

1. Get IP address of UniKix runtime instance from the Amazon EC2 console.

1. Get the port number for connecting to the TPE region using the TN3270 terminal emulator. You can find this at TNServer ListenPort from unikixrc.cfg file.

   ```
   cat $KIXSYS/unikixrc.cfg
   ```  
![Displays the details of the UniKix unikixrc.cfg file with the listener port as 15440.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-carddemo-1.png)

1. Configure your TN3270 terminal emulator to use IP address of UniKix runtime instance and port number 15440.

**Online Transactions**

This section assumes that you have connected to the TN3270 terminal emulator using the `kixterm` command.

1. After connecting from TN3270 terminal emulator, press "Enter" key to clear the TPE screen and enter the initial transaction.

1. On the initial transaction CC00 (logon screen) enter `USER001` for username and `PASSWORD` for the password.  
![Main screen for CardDemo. Displays that this is a Credit CardDemo application for Mainframe Modernization. Asks to enter your user ID and password.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-carddemo-2.png)

1. Choose option “01” from the **Main Menu** to view accounts.  
![CardDemo application's main menu in the emulator with selected option as 1.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-carddemo-3.png)

1. In the **View Account** screen, enter an account number (e.g., 00000000010). You should see the account information populated from the migrated data.  
![Details of the CardDemo application with entered account number as 00000000010.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-carddemo-4.png)

1. Press “PF03” key twice to go back to Log in screen, and exit the TN3270 terminal by pressing "Ctrl\+C" (Windows) or "Cmd\+C" (Macbook).

**Batch jobs**

1. Navigate to the JCL directory.

   ```
   cd $MBMSUB
   ```

1. Submit the job `MFCATGL1` and observe the job log output.

   ```
   BPESUB READCARD
   ```

1. Optionally, you could view the job logs from the `$SUBSYS_OUTDIR` directory.

   ```
   ls -lrt $SUBSYS_OUTDIR/*
   ```

You have now successfully deployed the CardDemo application onto NTT DATA UniKix runtime and verified the running application by navigating through a few CICS online screens and batch jobs.

## Troubleshooting
<a name="tutorial-unikix-troubleshoot"></a>

Following are some common errors you may find when setting up the CardDemo application.

### Error: Licensing error
<a name="tutorial-unikix-troubleshoot-license-issue"></a>

If you receive a license failure error during when following this tutorial, it could be that the **IMDSv2** is enabled in your EC2. You can resolve this issue by modifying the instance metadata option **IMDSv2** to **Optional** as mentioned in [Restore the use of IMDSv1](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-existing-instances.html) in the *Amazon EC2 user guide*.

### Error: TPE is not connected to BPE
<a name="tutorial-unikix-troubleshoot-tpe-connection"></a>

If the TPE is not connected to BPE, make sure the **VSAM Configuration Table** is configured correctly with BPE Node directory. To access the VSAM Configuration Table, launch TN3270 terminal emulator using the following command:

```
kixterm
```

1. Enter transaction name as `CTBL`.

1. In the **Table Manager** menu, choose the option **Standard Tables**.

1. On the Standard tables screen, choose the option **VSAM Configuration Table**.

1. Check if **Connect to batch node?** is set to "**Y** and the Node Directory is correct.

![VSAM Configuration Table in the TN3270 terminal emulator. Displaying values for each of the fields in the table.](http://docs.aws.amazon.com/m2/latest/userguide/images/unikix-troubleshoot.png)
