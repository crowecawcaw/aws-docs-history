

# Register an application
<a name="register-console"></a>

You can register SAP HANA and SAP ABAP applications using the AWS Console for SAP applications.

**Topics**
+ [Register SAP HANA database](#register-hana)
+ [Register SAP ABAP application](#register-abap)

## Register SAP HANA database
<a name="register-hana"></a>

Follow these steps to register an SAP HANA database as a Systems Manager for SAP application.

1. Open the [AWS Console for SAP applications](https://console.aws.amazon.com/awsforsap/home).

1. Choose **Register application**.

1. For Application type, select **SAP HANA**.

1. In **Application details**, enter a name for the application that you want to register.

1. In **SAP HANA workload**, provide details of your workload.

   1.  **Instance ID** – This is the Amazon EC2 instance ID where your workload is currently running. Choose **Browse instances**, and select the instance ID for your primary SAP HANA workload.

   1.  **SAP System Identifier (SID)** – This is the SAP System Identifier (`sapsid`) of your SAP HANA instance.

   1.  **SAP system number** – This is the system number of your SAP HANA instance.

   1.  **Credentials** – These are the credentials of your database.
**Note**  
If you do not see the credentials for the application you want to register in the **Secret ID** drop-down list, ensure that you have registered your credentials with AWS Secrets Manager. For more information, see [Register SAP HANA database credentials in AWS Secrets Manager](https://docs.aws.amazon.com/ssm-sap/latest/userguide/get-started.html#register-secrets).

       *Optional* Select **Add credentials** to add credentials for five databases.

1.  *Optional* In **Application tags**, you can add 100 tags associated to resources.

1. Choose **Create**.

On registration completion, you can see your application on the **Applications** page. For more information about the application details page, see [Application details](manage-console.md#application-details).

## Register SAP ABAP application
<a name="register-abap"></a>

**Important**  
You must register the SAP HANA database you want to connect to the SAP ABAP application before registering the SAP ABAP application.

Follow these steps to register either a single node or a multi node (distributed or high availability) SAP ABAP as a Systems Manager for SAP application.

1. Open the [AWS Console for SAP applications](https://console.aws.amazon.com/awsforsap/home).

1. Choose **Register application**.

1. For Application type, select **SAP ABAP**.

1. In **Application details**, enter a name for the application that you want to register.

1. Provide the following details of your workload.

   1.  **Instance ID** – This is the Amazon EC2 instance ID where your workload is currently running. Choose **Browse instances**, and select the instance ID for your primary SAP ABAP workload.

   1.  **SAP System Identifier (SID)** – This is the SAP System Identifier (`sapsid`) of your SAP ABAP instance.

   1.  **SAP HANA database Amazon Resource Name (ARN)** – This is the Amazon Resource Name (ARN) of the SAP HANA database you want to connect to your SAP ABAP application.
      + Select **Browse databases** to choose the database.
      + Select **Register a new application** to register an SAP HANA database to connect to the SAP ABAP application. You can refresh the database list on successful completion of the SAP HANA application.

1. (*Optional*). In **Connected Web Dispatcher components** you can provide the following details of up to 5 of your SAP Web Dispatcher resources that your application is using. SAP Web Dispatcher resources are only discoverable by Systems Manager for SAP after you input these details:

   1.  **SAP System Identifier (SID)** is the SAP System Identifier (`sapsid`) of your SAP Web Dispatcher resource.

   1.  **Instance ID** is the Amazon EC2 instance ID on which your SAP Web Dispatcher is currently running. Select **Browse instances** to find the instance ID.

1. (*Optional*). In **Application tags**, you can add 100 tags associated to resources.

1. Choose **Create**.

On registration completion, you can see your application on the **Applications** page. For more information about the application details page, see [Application details](manage-console.md#application-details).