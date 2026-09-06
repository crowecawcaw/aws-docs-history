

# Adding existing databases and catalogs using AWS Lake Formation permissions
<a name="lakehouse-add-catalog"></a>

You can add existing databases and catalogs to the lakehouse architecture.

**To add existing databases and catalogs using AWS Lake Formation permissions**

1. Sign in to the lakehouse architecture by using the link your administrator gave you. If you don't have access to it, contact your administrator.

1. Choose a project to open the project page.

1. On the left navigation, choose **Project overview**. On **Project details**, copy the project role ARN.

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. On the left navigation, from **Data catalog**, choose **Catalogs**.

1. On the **Catalogs** list view, choose a catalog you want to add to lakehouse architecture. From **Actions** on the right, choose **Grant**.

1. On the **Grant data lake permissions** page, choose **IAM users and roles** from **Principals**. Paste the IAM role you copied in the step 3.

1. On **Catalog permissions**, choose **Super user**. Choose **Grant**.

After you complete all the steps successfully, go back to the project page in the lakehouse architecture. You should see the Lake Formation catalog added to your lakehouse.