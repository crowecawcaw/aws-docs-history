# Create a lifecycle configuration

script

The following procedure shows how to create a lifecycle configuration script for
use with an Amazon SageMaker notebook instance. For more information about creating a
notebook instance, see [Create an Amazon SageMaker notebook instance](howitworks-create-ws.md "howitworks-create-ws.md").

###### To create a lifecycle configuration

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin
   configurations**.
3. Under **Admin configurations**, choose
   **Lifecycle configurations**.
4. From the **Lifecycle configurations** page, choose the
   **Notebook Instance** tab.
5. Choose **Create configuration**.
6. For **Name**, type a name using alphanumeric characters
   and "-", but no spaces. The name can have a maximum of 63 characters.
7. (Optional) To create a script that runs when you create the notebook and
   every time you start it, choose **Start notebook**.
8. In the **Start notebook** editor, type the script.
9. (Optional) To create a script that runs only once, when you create the
   notebook, choose **Create notebook**.
10. In the **Create notebook** editor, type the script
    configure networking.
11. Choose **Create configuration**.
