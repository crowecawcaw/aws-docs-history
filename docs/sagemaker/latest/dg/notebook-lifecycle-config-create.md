

# Create a lifecycle configuration script
<a name="notebook-lifecycle-config-create"></a>

The following procedure shows how to create a lifecycle configuration script for use with an Amazon SageMaker notebook instance. For more information about creating a notebook instance, see [Create an Amazon SageMaker notebook instance](howitworks-create-ws.md).

**To create a lifecycle configuration**

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/). 

1. On the left navigation pane, choose **Admin configurations**.

1. Under **Admin configurations**, choose **Lifecycle configurations**. 

1. From the **Lifecycle configurations** page, choose the **Notebook Instance** tab.

1. Choose **Create configuration**.

1. For **Name**, type a name using alphanumeric characters and "-", but no spaces. The name can have a maximum of 63 characters.

1. (Optional) To create a script that runs when you create the notebook and every time you start it, choose **Start notebook**.

1. In the **Start notebook** editor, type the script.

1. (Optional) To create a script that runs only once, when you create the notebook, choose **Create notebook**.

1. In the **Create notebook** editor, type the script configure networking.

1. Choose **Create configuration**.