# Library management

You can use the library management widget in JupyterLab to manage the library
installations and configurations in your notebook.

To navigate to the library management of a notebook in Amazon SageMaker Unified Studio, complete the
following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to a project. You can do this by choosing a project from the project
   selector dropdown at the top of the page, or by
   creating a new project.
3. In the left navigation pane, under **IDEs**, choose
   **JupyterLab**.
4. Navigate to a notebook or create a new one by selecting **File**
   > **New** > **Notebook**.
5. Choose the library management icon from the notebook navigation bar.

![The Amazon SageMaker Unified Studio JupyterLab library icon.](images/library-icon.png)
The following library configurations are available:

## Jar

- **Maven artifacts**

- **S3 paths**

- **Disk location paths**

- **Other paths**

## Python

- **Conda packages**

- **PyPI packages**

- **S3 paths**

- **Disk location paths**

- **Other paths**

## Adding JupyterLab library configurations

1. Navigate to the JupyterLab library management page.
2. Select the configuration method you would like to add from the left navigation
   of the library management page.
3. Choose **Add**.
4. Input the URL, package name, coordinates, or other information as the fields
   indicate.
5. In the left navigation of the library management page, check the box
   **Apply the change to JupyterLab**.
6. Choose **Save all changes**.
