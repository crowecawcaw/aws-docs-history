# Creating a new space

To create a space, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project you want to create a space in.
   You can do this by choosing **Browse all projects** from the center menu.
3. In the **Build** menu, choose **Spaces** to navigate to the **Spaces** tab on the **Compute** page.
4. Choose **Create space**.
5. Under **Name**, enter a name for the space. This name must be unique.
   No spaces in the project can use the same name.
6. Under **Application**, choose the IDE application you want to use with the space.
7. Under **Instance**, choose an Amazon EC2 instance that is most compatible with your use case.

###### Note

If you use a GPU instance type when configuring your Code Editor application, you must also use a GPU-based image.
Within a space, your data is stored in an Amazon EBS volume that persists independently from the life of an instance.
You won't lose your data when you change instances. 8. Under **Image**, choose the image you want to use. 9. Under **EBS space storage**, enter a value from 16 to 100 to choose a storage size. 10. (Optional) Choose the lifecycle configuration for the space.

    1. Find your domain ID. For instructions, see [Get project details](view-project-details.md "view-project-details.md").
    2. Find your user profile ID:


    	1. In the **Compute** panel, choose the **Spaces** tab.
    	2. The user profile ID is the string following `default-` of the default JupyterLab space.
    3. [Create a lifecycle configuration](../../../sagemaker/latest/dg/jl-lcc-create.md#jl-lcc-create-console "../../../sagemaker/latest/dg/jl-lcc-create.md#jl-lcc-create-console") for Amazon SageMaker Unified Studio and reference your ID values from step b.


    ###### Note

    Attaching the lifecycle configuration to your Amazon SageMaker AI domain and user profile through the AWS CLI is not currently supported. Use the console to create lifecycle configurations.
    4. Under **Lifecycle configuration**, choose the lifecycle you created.

11. Under **Idle time**, enter the amount of time before the space will time out and stop running.
12. (Optional) Attach a custom file system to your space.
    1.  To attatch a custom file system to a domain see [Attaching a custom file system to a domain with the AWS CLI](../../../sagemaker/latest/dg/domain-custom-file-system.md#domain-custom-file-system-cli "../../../sagemaker/latest/dg/domain-custom-file-system.md#domain-custom-file-system-cli"), and reference your ID values from step 10.
    2.  Under **Attach custom file system**, attach the file system.

13. Choose **Create and start space** to create the space and have it start running.
    It might take up to 5 minutes for Amazon SageMaker Unified Studio to finish creating the space. After the space is created, you can view it in the list on the **Spaces** tab and
    choose **Open** to launch the IDE in your browser.

You can then perform various actions using the three-dot **Actions** menu on the **Spaces** tab in Amazon SageMaker Unified Studio. You can edit the space, start or stop
running the application, delete the space, or view information about the space.
