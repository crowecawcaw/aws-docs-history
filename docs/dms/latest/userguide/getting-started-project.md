

# Create a migration project in DMS Schema Conversion
<a name="getting-started-project"></a>

Now you can create a migration project. In the migration project, you specify your source and target data providers, and your instance profile.

**To create a migration project**

1. Choose **Migration projects**, and then choose **Create migration project**.

1. For **Name**, enter a unique name for your migration project. For example, enter **sc-project**.

1. For **Instance profile**, choose **sc-instance**.

1. For **Source**, choose **Browse**, and then choose **sc-source**.

1. For **Secret ID**, choose **sc-source-secret**.

1. For **IAM role**, choose **sc-source-secret-role**.

1. For **Target**, choose **Browse**, and then choose **sc-target**.

1. For **Secret ID**, choose **sc-target-secret**.

1. For **IAM role**, choose **sc-target-secret-role**.

1. Choose **Create migration project**.

**Note**  
If your source or target data provider has **Virtual Mode** turned on, the **Secret ID** and **IAM role** are optional for that data provider. Provide them only if you want to. If you do choose a **Secret ID** for a data provider in **Virtual Mode**, it must meet the requirements in [Create Secrets Manager secrets](set-up.md#set-up-secrets). For more information, see [Virtual mode for offline source and virtual target](virtual-data-provider.md).