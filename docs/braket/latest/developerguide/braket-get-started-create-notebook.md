# Create an Amazon Braket notebook

instance

###### Tip

**Learn the foundations of quantum computing with AWS!**
Enroll in the [Amazon Braket Digital Learning Plan](https://skillbuilder.aws/learning-plan/EH35DWGU3R/amazon-braket--knowledge-badge-readiness-path-includes-labs "https://skillbuilder.aws/learning-plan/EH35DWGU3R/amazon-braket--knowledge-badge-readiness-path-includes-labs")
and earn your own Digital badge after completing a series of learning courses and a digital assessment.

Amazon Braket provides fully managed Jupyter notebooks to get you started.
The Amazon Braket notebook instances are based on
[Amazon SageMaker AI
notebook instances](../../../sagemaker/latest/dg/nbi.md "../../../sagemaker/latest/dg/nbi.md"). The following steps outline how to create a new
notebook instance for new and existing customers.

**New Amazon Braket customers:**

1.  Open the [Amazon Braket
    console](https://console.aws.amazon.com/braket/home "https://console.aws.amazon.com/braket/home") and navigate to the **Dashboard** page in the left pane.
2.  Click **Get Started** on the
    **Welcome to Amazon Braket** modal in the center of your dashboard page.
    Provide a notebook name to create a default Jupyter notebook.

        1. It may take several minutes to create your notebook.
        2. Your notebook
         will be listed on the **Notebooks** page with a
         status of **Pending**.
        3. When your notebook instance
         is ready to use, the status changes to **InService**.
        4. Refresh the page to display the updated status for the notebook.

    **Existing Amazon Braket customers:**

3.  Open the [Amazon Braket
    console](https://console.aws.amazon.com/braket/home "https://console.aws.amazon.com/braket/home") and select **Notebooks** in the left pane.
4.  Select **Create notebook instance**.
    1. If you have zero notebooks, select the **Standard setup** to create a default Jupyter notebook.

5.  Enter a **Notebook instance name**, using only alphanumeric and hyphen characters,
    and select your preferred **Visual Mode**.
6.  Enable or disable the **Notebook inactivity manager** for your notebook.
    1. If enabled, select the desired idle duration time before the notebook is reset. When a notebook is reset,
       the compute charges stop incurring, but the storage charges will continue.
    2. To check how much idle time remains for your notebook instance, navigate to the command bar, select
       the **Braket** tab, and then the **Inactivity
       Manager** tab.

###### Note

To save your work, integrate your
[SageMaker AI notebook instance with a Git repository](../../../sagemaker/latest/dg/nbi-git-repo.md "../../../sagemaker/latest/dg/nbi-git-repo.md").
Alternately, move your work outside of the `/Braket Algorithms` and `/Braket Examples`
folders so they are not overwritten by the notebook instance restarting. 5. (Optional) With **Advanced setup**, you can create a notebook with
access permissions, additional configurations, and network access settings:

    1. In **Notebook configuration** choose your instance type.




    	1. The standard, cost-effective instance type, **ml.t3.medium**
    	 is chosen by default. To learn more about instance pricing, see
    	 [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").
    2. To associate a public Github repository with your notebook instance, click on the
     **Git repository** dropdown and select
     **Clone a public git repository from url** from the
     **Repository** dropdown menu. Enter the URL of the repo in the
     **Git repository URL** text bar.
    3. In **Access permissions**, configure any optional IAM roles,
     root access, and encryption keys.
    4. In **Network access**, configure custom network and access settings
     for your Jupyter Notebook instance.

6. Review your settings, and set any tags to identify your notebook instance. Click
   **Launch**.

###### Note

View and manage your Amazon Braket notebook instances in the
Amazon Braket and Amazon SageMaker AI consoles. Additional
Amazon Braket notebook settings are available through the [SageMaker console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").

If you are working in the Amazon Braket console within AWS the Amazon Braket SDK and plugins are preloaded in the
notebooks you created. To run on your own machine, install the SDK
and plugins when you run the command `pip install amazon-braket-sdk` or when you
run the command `pip install amazon-braket-pennylane-plugin` for PennyLane plugins.
