# Stop SAP application

Follow along these steps to stop Systems Manager for SAP application using AWS Management Console.

1. Go to https://console.aws.amazon.com/systems-manager/ > **Application Tools** > **Application Manager**.
2. From the list of registered applications, choose the application you want to stop.
3. Select **Actions** > **Stop application**.
   1. When sttopping an SAP HANA application, you can also stop the associated EC2 instance where the SAP HANA application is running.
   2. When stopping an SAP ABAP application, you can also stop the connected SAP HANA application, and/or stop the associated EC2 instance where the SAP ABAP and SAP HANA applications are running.

   ###### Note

   You can stop the EC2 instance only if you have selected the option to stop the connected SAP HANA application.

4. Select **Stop**.
   You can monitor the task status using the _operation ID_ provided in the flash banner or by selecting **Actions** > **View operations**.
