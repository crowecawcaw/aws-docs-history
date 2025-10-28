# Connect to an EMR Serverless

application from Studio

Data scientists and data engineers can discover and then connect to an EMR Serverless
application directly from the Studio user interface. Before you begin, ensure that
you have created an EMR Serverless application by following the instructions in [Create EMR Serverless applications
from Studio](create-emr-serverless-application.md "create-emr-serverless-application.md").

You can connect an EMR Serverless application to a new JupyterLab notebook directly
from the Studio UI, or choose to initiate the connection in a notebook of a running
JupyterLab application.

###### Important

When using Studio, you can only discover and connect to EMR Serverless
applications for JupyterLab applications that are launched from private spaces.
Ensure that the EMR Serverless applications are located in the same AWS region as
your Studio environment. Your JupyterLab space must use a SageMaker Distribution
image version `1.10` or higher.

###### To connect an EMR Serverless application to a new JupyterLab notebook from the

Studio UI:

1. In the Studio UI, navigate to the left-side panel and select the
   **Data** node in the left navigation menu. Then, scroll and
   choose the **Amazon EMR applications and clusters** option. This
   opens up a page that displays the Amazon EMR applications that you can access from
   within the Studio environment, under the **Serverless
   applications** tab.

###### Note

If you or your administrator have configured the permissions to allow
cross-account access to EMR Serverless applications, you can view a
consolidated list of applications across all accounts that you have granted
access to Studio. 2. Select an EMR Serverless application you want to connect to a new notebook,
and then choose **Attach to notebook**. This opens up a modal
window displaying the list of your JupyterLab spaces. 3. _ Select the private space from which you want to launch a JupyterLab
application, and then choose **Open notebook**. This
launches a JupyterLab application from your chosen space and opens a
new notebook.
_ Alternatively, you can create a new private space by choosing the
**Create new space** button at the top of the modal
window. Enter a name for your space and then choose **Create
space and open notebook**. This creates a private space
with the default instance type and latest SageMaker distribution image
available, launches a JupyterLab application, and opens a new
notebook. 4. Choose the name of the IAM runtime execution role that your EMR Serverless
application can assume for the job run. Upon selection, a connection command
populates the first cell of your notebook and initiates the connection with the
EMR Serverless application.

###### Important

To successfully connect a JupyterLab notebook to an EMR Serverless
application, you must first associate the list of runtime roles with your
domain or user profile, as outlined in [Set up the permissions to enable
listing and launching Amazon EMR applications from SageMaker Studio](studio-emr-serverless-permissions.md "studio-emr-serverless-permissions.md"). Failing to complete this
step will prevent you from establishing the connection.

Once the connection succeeds, a message confirms the connection, starts your
EMR Serverless application, and initiates your Spark session.

###### Note

When you connect to an EMR Serverless application, its status transitions
from either `Stopped` or `Created` to
`Started`.

###### Alternatively, you can connect to a cluster from a JupyterLab notebook.

1. Choose the **Cluster** button at the top right of your
   notebook. This opens a modal window listing the EMR Serverless applications
   that you can access. You can see the applications in the **Serverless
   applications** tab.
2. Select the application to which you want to connect, then choose
   **Connect**.
3. EMR Serverless supports runtime IAM roles that were preloaded when setting
   the required permissions as outlined in [Set up the permissions to enable
   listing and launching Amazon EMR applications from SageMaker Studio](studio-emr-serverless-permissions.md "studio-emr-serverless-permissions.md"). Failing to complete this step
   will prevent you from establishing the connection.

You can select your role from the **Amazon EMR execution role**
drop down menu. When you connect to an EMR Serverless, Studio adds a code
block to an active cell of your notebook to establish the connection. 4. An active cell populates and runs. This cell contains the connection magic
command to connect your notebook to your application.

Once the connection succeeds, a message confirms the connection and the start
of the Spark application. You can begin submitting your data processing jobs to
your EMR Serverless application.
