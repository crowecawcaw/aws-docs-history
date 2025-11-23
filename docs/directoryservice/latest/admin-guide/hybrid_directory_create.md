# Creating a hybrid directory

Before creating a hybrid directory, you must create and successfully pass a directory assessment that verifies
connectivity and interoperability with your self-managed Active Directory

## Creating a hybrid directory with your

self-managed AD

Follow these steps to create a hybrid directory with your self-managed AD:

###### To create a hybrid directory

1. Open the Directory Service console for your desired Region.
2. On the **Select directory type** page, choose
   **AWS Managed Microsoft AD**.
3. Under **Getting started with AWS Managed Microsoft AD**, select
   **Extend your AD domain with a hybrid directory – new**
   and then choose **Next**. This directs you to the
   **Create directory assessment** page.
4. Before you can create a hybrid directory, you must first create and successfully
   pass a directory assessment. To create a directory assessment, follow the steps in [Creating directory assessments](create_directory_assessment.md "create_directory_assessment.md"). Once you have successfully
   passed a directory assessment, you can continue with this procedure.
5. Once you have successfully passed a directory assessment, navigate to the
   **Directories** page.
6. On the **Directories** page, under **Trial hybrid
   directory assessments** choose an **Assessment
   ID** with a **Status** of `SUCCESS`.
   Then select **Create hybrid directory**, which directs you to
   the assessment details page
7. On the assessment details page confirm this action by selecting
   **Create hybrid directory**, which opens the
   **Create hybrid directory using assessment-id**
   page.
8. On the **Create hybrid directory using assessment-id** page,
   **Review the self-managed Active Directory information**. After
   confirming the information, select **Create
   hybrid directory**.

After choosing **Create hybrid directory**, AWS runs another
directory assessment based on this information to confirm that your self-managed AD
configuration is still valid. If the directory assessment passes successfully, then we create
the hybrid directory. 9. Choosing **Create hybrid directory** returns you to the
**Directories** page.

    1. A green banner will appear once the hybrid directory is created
     successfully.
    2. A red banner will appear if the hybrid directory creation fails. Clean up
     hybrid directory creation failures by completing the following:




    	1. Delete the failed hybrid directory in the console.
    	2. Delete any remaining AWS Reserved OUs in your
    	 self-managed AD.**More information**




    * [Deleting a hybrid directory](hybrid_directory_delete.md "hybrid_directory_delete.md")
    * [Troubleshooting](hybrid_directory_troubleshooting.md "hybrid_directory_troubleshooting.md")
