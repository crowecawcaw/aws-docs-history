# Launching Data Wrangler from Amazon Personalize

To launch Data Wrangler from Amazon Personalize, you use the Amazon Personalize console to configure a SageMaker AI domain and launch Data Wrangler.

###### To launch Data Wrangler from Amazon Personalize

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your account.
2. On the **Dataset groups** page, choose your dataset group.
3. In **Set up datasets** choose **Create dataset** and
   choose the type of dataset to create. You can't use Data Wrangler to
   prepare an Actions dataset or Action interactions dataset.
4. Choose **Import data using Data Wrangler** and choose **Next**.
5. For **SageMaker domain**, choose to use an existing domain or create a new one. You need a SageMaker AI
   Domain to access Data Wrangler in SageMaker AI Studio Classic. For information about domains and user profiles, see [SageMaker AI Domain](../../../sagemaker/latest/dg/sm-domain.md "../../../sagemaker/latest/dg/sm-domain.md") in the _Amazon SageMaker AI Developer Guide_.
6. To use an existing domain, choose a **SageMaker AI domain** and **User profile** to
   configure the domain.
7. To create a new domain:
   - Give the new domain a name.
   - Choose a **User profile name**.
   - For **Execution role**, choose the role you created in [Setting up permissions](dw-data-prep-minimum-permissions.md "dw-data-prep-minimum-permissions.md"). Or, if you have
     CreateRole permissions, create a new role using the role creation wizard. The role you use must have the
     `AmazonSageMakerFullAccess` policy attached.

8. Choose **Next**. If you are creating a new domain, SageMaker AI starts creating your domain. This can take
   up to ten minutes.
9. Review the details for your SageMaker AI domain.
10. Choose **Import data with Data Wrangler**. SageMaker AI Studio Classic starts creating your environment, and when complete,
    the **Data flow** page of Data Wrangler in SageMaker AI Studio Classic opens in a new tab. It can take up to five minutes for SageMaker AI Studio Classic to finish creating your environment. When it
    finishes, you are ready to start importing data into Data Wrangler. For more information, see [Importing data into Data Wrangler](dw-import-data.md "dw-import-data.md").
