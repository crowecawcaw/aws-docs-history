# Get started with Apache Spark on Amazon Athena

###### Note

For the release version Apache Spark version 3.5, following the Getting Started guide in
[SageMaker Notebooks](../../../sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.md "../../../sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.md").
Use this guide for the release version Pyspark engine version 3.

To get started with Apache Spark on Amazon Athena, you must first create a Spark enabled
workgroup. After you switch to the workgroup, you can create a notebook or open an existing
notebook. When you open a notebook in Athena, a new session is started for it automatically
and you can work with it directly in the Athena notebook editor.

###### Note

Make sure that you create a Spark enabled workgroup before you attempt to create a
notebook.

## Step 1: Create a Spark enabled workgroup in Athena

You can use [workgroups](workgroups-manage-queries-control-costs.md "workgroups-manage-queries-control-costs.md") in
Athena to group users, teams, applications, or workloads, and to track costs. To use
Apache Spark in Amazon Athena, you create an Amazon Athena workgroup that uses a Spark
engine.

###### Note

Apache Spark enabled workgroups can use the Athena notebook editor, but not the
Athena query editor. Only Athena SQL workgroups can use the Athena query editor.

###### To create a Spark enabled workgroup in Athena

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home")
2. If the console navigation pane is not visible, choose the expansion menu
   on the left.

![Choose the expansion menu.](images/nav-pane-expansion.png) 3. In the navigation pane, choose **Workgroups**. 4. On the **Workgroups** page, choose **Create
workgroup**. 5. For **Workgroup name**, enter a name for your Apache Spark
workgroup. 6. (Optional) For **Description**, enter a description for your
workgroup. 7. For **Analytics engine**, choose **Apache
Spark**.

###### Note

After you create a workgroup, the workgroup's type of analytics engine
cannot be changed. For example, an Athena engine version 3 workgroup cannot be changed to a
PySpark engine version 3 workgroup. 8. For the purposes of this tutorial, select **Turn on example
notebook**. This optional feature adds an example notebook with the
name
`example-notebook-`random_string``
to your workgroup and adds AWS Glue-related permissions that the notebook uses to
create, show, and delete specific databases and tables in your account, and read
permissions in Amazon S3 for the sample dataset. To see the added permissions, choose
**View additional permissions details**.

###### Note

Running the example notebook may incur some additional cost. 9. For **Calculation result settings**choose from the following
options:

    * Create a new S3 bucket – This
     option creates an Amazon S3 bucket in your account for your calculation
     results. The bucket name has the format
     ``account_id`-`region`-athena-results-bucket-`alphanumeric_id``
     and uses the settings ACLs disabled, public access blocked, versioning
     disabled, and bucket owner enforced.
    * Choose an existing S3 location –
     For this option, do the following:




    	+ Enter the S3 path to an existing the location in the search
    	 box, or choose **Browse S3** to choose a bucket
    	 from a list.


    	###### Note

    	When you select an existing location in Amazon S3, do not
    	 append a forward slash (`/`) to the location.
    	 Doing so causes the link to the calculation results location
    	 on the [calculation details page](#notebooks-spark-getting-started-viewing-session-and-calculation-details "#notebooks-spark-getting-started-viewing-session-and-calculation-details") to point to the
    	 incorrect directory. If this occurs, edit the workgroup's
    	 results location to remove the trailing forward slash.
    	+ (Optional) Choose **View** to open the
    	 **Buckets** page of the Amazon S3 console where
    	 you can view more information about the existing bucket that you
    	 chose.
    	+ (Optional) For **Expected bucket owner**,
    	 enter the AWS account ID that you expect to be the owner of
    	 your query results output location bucket. We recommend that you
    	 choose this option as an added security measure whenever
    	 possible. If the account ID of the bucket owner does not match
    	 the ID that you specify, attempts to output to the bucket will
    	 fail. For in-depth information, see [Verifying bucket ownership with bucket owner
    	 condition](../../../AmazonS3/latest/userguide/bucket-owner-condition.md "../../../AmazonS3/latest/userguide/bucket-owner-condition.md") in the *Amazon S3 User Guide*.
    	+ (Optional) Select **Assign bucket owner full control
    	 over query results** if your calculation result
    	 location is owned by another account and you want to grant full
    	 control over your query results to the other account.

10. (Optional) Choose **Encrypt query results** if you want your
    query results to be encrypted.
    - For **Encryption type**, choose one of the following
      options:
      - **SSE_S3** – This option uses
        server-side encryption (SSE) with Amazon S3-managed encryption
        keys.
      - **SSE_KMS** – This option uses
        server-side encryption (SSE) with AWS KMS-managed keys.

      For **Choose an AWS KMS key**, choose one of
      the following options.

          - Use AWS owned key
           – The AWS KMS key is owned and managed by AWS.
           You are not charged an additional fee for using this
           key.
          - Choose a different AWS KMS key
           (advanced) – For this option, do one
           of the following:




          	* To use an existing key, use the search box to
          	 choose an AWS KMS or enter a key ARN.
          	* To create a key in the AWS KMS console, choose
          	 **Create an AWS KMS key**. Your
          	 execution role must have permission to use the key
          	 that you create. After you finish creating the key
          	 in the KMS console, return to the **Create
          	 workgroup** page in Athena console, and
          	 then use the **Choose an AWS KMS key or
          	 enter an ARN** search box to choose the
          	 key that you just created.

    ###### Important

    When you change the [AWS KMS key](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") for a workgroup, notebooks managed
    before the update still reference the old KMS key. Notebooks
    managed after the update use the new KMS key. To update the old
    notebooks to reference the new KMS key, export and then import
    each of the old notebooks. If you delete the old KMS key before
    you update the old notebook references to the new KMS key, the old
    notebooks are no longer decryptable and cannot be recovered.

    This behavior also applies for updates to [aliases](../../../kms/latest/developerguide/kms-alias.md "../../../kms/latest/developerguide/kms-alias.md"),
    which are friendly names for KMS keys. When you update a KMS key
    alias to point to a new KMS key, notebooks managed before the
    alias update still reference the old KMS key, and notebooks
    managed after the alias update use the new KMS key. Consider these
    points before updating your KMS keys or aliases.

11. For **Additional configurations**, choose **Use
    defaults**. This option helps you get started with your
    Spark-enabled workgroup. When you use the defaults, Athena creates an IAM role
    and calculation results location in Amazon S3 for you. The name of the IAM role and
    the S3 bucket location to be created are displayed in the box below the
    **Additional configurations** heading.

If you do not want to use the defaults, continue with the steps in the [(Optional) Specify your own workgroup configurations](#notebooks-spark-getting-started-workgroup-configuration "#notebooks-spark-getting-started-workgroup-configuration")
section to configure your workgroup manually. 12. (Optional) **Tags** – Use this option to add tags to
your workgroup. For more information, see [Tag Athena resources](tags.md "tags.md"). 13. Choose **Create workgroup**. A message informs you that the
workgroup was created successfully, and the workgroup shows in the list of
workgroups.

### (Optional) Specify your own workgroup configurations

If you want to specify your own IAM role and calculation results location for
your notebook, follow the steps in this section. If you chose **Use
defaults** for the **Additional configurations**
option, skip this section and go directly to [Step 2: Open notebook explorer and switch workgroups](#notebooks-spark-getting-started-switching-workgroups-and-opening-notebook-explorer "#notebooks-spark-getting-started-switching-workgroups-and-opening-notebook-explorer").

The following procedure assumes you have completed steps 1 to 9 of the
**To create a Spark enabled workgroup in Athena** procedure in
the previous section.

###### To specify your own workgroup configurations

1. If you want to create or use your own IAM role or configure notebook
   encryption, expand **IAM role configuration**.
   - For **Service Role to authorize Athena**, choose
     one of the following:
     - Create and use a new service
       role – Choose this option to have Athena
       create a service role for you. To see the permissions the
       role grants, choose **View permission
       details**.
     - Use an existing service
       role – From the drop down menu, choose
       an existing role. The role that you choose must include the
       permissions in the first option. For more information about
       permissions for notebook-enabled workgroups, see [Troubleshoot Spark-enabled workgroups](notebooks-spark-troubleshooting-workgroups.md "notebooks-spark-troubleshooting-workgroups.md").

   - For **Notebook and calculation code encryption key
     management**, choose one of the following
     options:
     - Encrypt using AWS owned key
       (Default) – The AWS KMS key is owned and
       managed by AWS. You are not charged an additional fee for
       using this key.
     - Encrypt using your own AWS KMS
       key – For this option, do one of the
       following:
       - To use an existing key, use the search box to
         choose an AWS KMS or enter a key ARN.
       - To create a key in the AWS KMS console, choose
         **Create an AWS KMS key**. Your
         execution role must have permission to use the key
         that you create. After you finish creating the key
         in the KMS console, return to the **Create
         workgroup** page in Athena console, and
         then use the **Choose an AWS KMS key or enter
         an ARN** search box to choose the key
         that you just created.

   ###### Important

   When you change the [AWS KMS key](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") for a workgroup, notebooks managed
   before the update still reference the old KMS key. Notebooks
   managed after the update use the new KMS key. To update the
   old notebooks to reference the new KMS key, export and then
   import each of the old notebooks. If you delete the old
   KMS key before you update the old notebook references to the
   new KMS key, the old notebooks are no longer decryptable and
   cannot be recovered.

   This behavior also applies for updates to [aliases](../../../kms/latest/developerguide/kms-alias.md "../../../kms/latest/developerguide/kms-alias.md"), which are friendly names for KMS keys.
   When you update a KMS key alias to point to a new KMS key,
   notebooks managed before the alias update still reference the
   old KMS key, and notebooks managed after the alias update use
   the new KMS key. Consider these points before updating your
   KMS keys or aliases.

2. (Optional) **Other settings** – Expand this option
   to enable or disable the **Publish CloudWatch metrics** option
   for the workgroup. This field is selected by default. For more information,
   see [Monitor Apache Spark with CloudWatch metrics](notebooks-spark-metrics.md "notebooks-spark-metrics.md").
3. (Optional) **Tags** – Use this option to add tags
   to your workgroup. For more information, see [Tag Athena resources](tags.md "tags.md").
4. Choose **Create workgroup**. A message informs you that
   the workgroup was created successfully, and the workgroup shows in the list
   of workgroups.

## Step 2: Open notebook explorer and switch workgroups

Before you can use the Spark enabled workgroup that you just created, you must switch
to the workgroup. To switch Spark enabled workgroups, you can use the
**Workgroup** option in Notebook explorer or Notebook
editor.

###### Note

Before you start, check that your browser does not block third-party cookies. Any
browser that blocks third party cookies either by default or as a user-enabled
setting will prevent notebooks from launching. For more information on managing
cookies, see:

- [Chrome](https://support.alertlogic.com/hc/en-us/articles/360018127132-Turn-Off-Block-Third-Party-Cookies-in-Chrome-for-Windows "https://support.alertlogic.com/hc/en-us/articles/360018127132-Turn-Off-Block-Third-Party-Cookies-in-Chrome-for-Windows")
- [Firefox](https://support.mozilla.org/en-US/kb/third-party-cookies-firefox-tracking-protection "https://support.mozilla.org/en-US/kb/third-party-cookies-firefox-tracking-protection")
- [Safari](https://support.apple.com/guide/safari/manage-cookies-sfri11471/mac "https://support.apple.com/guide/safari/manage-cookies-sfri11471/mac")

###### To open notebook explorer and switch workgroups

1. In the navigation pane,choose **Notebook explorer**.
2. Use the **Workgroup** option on the upper right of the
   console to choose the Spark enabled workgroup that you created. The example
   notebook is shown in the list of notebooks.

You can use the notebook explorer in the following ways:

    * Choose the linked name of a notebook to open the notebook in a new
     session.
    * To rename, delete, or export your notebook, use the
     **Actions** menu.
    * To import a notebook file, choose **Import
     file**.
    * To create a notebook, choose **Create
     notebook**.

## Step 3: Run the example notebook

The sample notebook queries data from a publicly available New York City taxi trip
dataset. The notebook has examples that show how to work with Spark DataFrames, Spark
SQL, and the AWS Glue Data Catalog.

###### To run the example notebook

1. In Notebook explorer, choose the linked name of the example notebook.

This starts a notebook session with the default parameters and opens the
notebook in the notebook editor. A message informs you that a new Apache Spark
session has been started using the default parameters (20 maximum DPUs). 2. To run the cells in order and observe the results, choose the
**Run** button once for each cell in the notebook.

    * Scroll down to see the results and bring new cells into view.
    * For the cells that have a calculation, a progress bar shows the
     percentage completed, the time elapsed, and the time remaining.
    * The example notebook creates a sample database and table in your
     account. The final cell removes these as a clean-up step.

###### Note

If you change folder, table, or database names in the example notebook, make sure
those changes are reflected in the IAM roles that you use. Otherwise, the notebook
can fail to run due to insufficient permissions.

## Step 4: Edit session details

After you start a notebook session, you can edit session details like table format,
encryption, session idle timeout, and the maximum concurrent number of data processing
units (DPUs) that you want to use. A DPU is a relative measure of processing power that
consists of 4 vCPUs of compute capacity and 16 GB of memory.

###### To edit session details

1. In the notebook editor, from the **Session** menu on the
   upper right, choose **Edit session**.
2. In the **Edit session details** dialog box, in the
   **Spark properties** section, choose or enter values for
   the following options:
   - Additional table format – Choose
     **Linux Foundation Delta Lake**, **Apache
     Hudi**, **Apache Iceberg**, or
     **Custom**.
     - For the **Delta**, **Hudi**,
       or **Iceberg** table options, the required
       table properties for the corresponding table format are
       automatically provided for you in the **Edit in
       table** and **Edit in JSON**
       options. For more information about using these table formats,
       see [Use non-Hive table formats in Athena for Spark](notebooks-spark-table-formats.md "notebooks-spark-table-formats.md").
     - To add or remove table properties for the
       **Custom** or other table types, use the
       **Edit in table** and **Edit in
       JSON** options.
     - For the **Edit in table** option, choose
       **Add property** to add a property, or
       **Remove** to remove a property. To enter
       property names and their values, use the
       **Key** and **Value**
       boxes.
     - For the **Edit in JSON** option, use the JSON
       text editor to edit the configuration directly.
       - To copy the JSON text to the clipboard, choose
         **Copy**.
       - To remove all text from the JSON editor, choose
         **Clear**.
       - To configure line wrapping or choose a color theme for
         the JSON editor, choose the settings (gear) icon.

   - Turn on Spark encryption - –
     Select this option to encrypt data that is written to disk and sent
     through Spark network nodes. For more information, see [Enable Apache Spark encryption](notebooks-spark-encryption.md "notebooks-spark-encryption.md").

3. In the **Session parameters** section, choose or enter values
   for the following options:
   - **Session idle timeout** - Choose or enter a value
     between 1 and 480 minutes. The default is 20.
   - **Coordinator size** - A
     _coordinator_ is a special executor that
     orchestrates processing work and manages other executors in a notebook
     session. Currently, 1 DPU is the default and only possible value.
   - **Executor size** - An _executor_
     is the smallest unit of compute that a notebook session can request from
     Athena. Currently, 1 DPU is the default and only possible value.
   - **Max concurrent value** - The maximum number of DPUs
     that can run concurrently. The default is 20, the minimum is 3, and the
     maximum is 60. Increasing this value does not automatically allocate
     additional resources, but Athena will attempt to allocate up to the
     maximum specified when the compute load requires it and when resources
     are available.

4. Choose **Save**.
5. At the **Confirm edit** prompt, choose
   **Confirm**.

Athena saves your notebook and starts a new session with the parameters that
you specified. A banner in the notebook editor informs you that a new session
has started with the modified parameters.

###### Note

Athena remembers your session settings for the notebook. If you edit a
session's parameters and then terminate the session, Athena uses the session
parameters that you configured the next time you start a session for the
notebook.

## Step 5: View session and calculation details

After you run the notebook, you can view your session and calculation details.

###### To view session and calculation details

1. From the **Session** menu on the upper right, choose
   **View details**.
   - The **Current session** tab shows information about
     the current session, including session ID, creation time, status, and
     workgroup.
   - The **History** tab lists the session IDs for
     previous sessions. To view details for a previous session, choose the
     **History** tab, and then choose a session ID in
     the list.
   - The **Calculations** section shows a list of
     calculations that ran in the session.

2. To view the details for a calculation, choose the calculation ID.
3. On the **Calculation details** page, you can do the
   following:
   - To view the code for the calculation, see the
     **Code** section.
   - To see the results for the calculation, choose the
     **Results** tab.
   - To download the results that you see in text format, choose
     **Download results**.
   - To view information about the calculation results in Amazon S3, choose
     **View in S3**.

## Step 6: Terminate the session

###### To end the notebook session

1. In the notebook editor, from the **Session** menu on the
   upper right, choose **Terminate**.
2. At the **Confirm session termination** prompt, choose
   **Confirm**. Your notebook is saved and you are returned to
   the notebook editor.

###### Note

Closing a notebook tab in the notebook editor does not by itself terminate the
session for an active notebook. If you want to ensure that the session is
terminated, use the **Session**, **Terminate**
option.

## Step 7: Create your own notebook

After you have created a Spark enabled Athena workgroup, you can create your own
notebook.

###### To create a notebook

1. If the console navigation pane is not visible, choose the expansion menu on
   the left.
2. In the Athena console navigation pane, choose **Notebook
   explorer** or **Notebook editor**.
3. Do one of the following:
   - In **Notebook explorer**, choose **Create
     notebook**.
   - In **Notebook editor**, choose **Create
     notebook**, or choose the plus icon
     (**+**) to add a notebook.

4. In the **Create notebook** dialog box, for **Notebook
   name**, enter a name.
5. (Optional) Expand **Spark properties**, and then choose or
   enter values for the following options:
   - Additional table format – Choose
     **Linux Foundation Delta Lake**, **Apache
     Hudi**, **Apache Iceberg**, or
     **Custom**.
     - For the **Delta**, **Hudi**,
       or **Iceberg** table options, the required
       table properties for the corresponding table format are
       automatically provided for you in the **Edit in
       table** and **Edit in JSON**
       options. For more information about using these table formats,
       see [Use non-Hive table formats in Athena for Spark](notebooks-spark-table-formats.md "notebooks-spark-table-formats.md").
     - To add or remove table properties for the
       **Custom** or other table types, use the
       **Edit in table** and **Edit in
       JSON** options.
     - For the **Edit in table** option, choose
       **Add property** to add a property, or
       **Remove** to remove a property. To enter
       property names and their values, use the
       **Key** and **Value**
       boxes.
     - For the **Edit in JSON** option, use the JSON
       text editor to edit the configuration directly.
       - To copy the JSON text to the clipboard, choose
         **Copy**.
       - To remove all text from the JSON editor, choose
         **Clear**.
       - To configure line wrapping or choose a color theme for
         the JSON editor, choose the settings (gear) icon.

   - Turn on Spark encryption - –
     Select this option to encrypt data that is written to disk and sent
     through Spark network nodes. For more information, see [Enable Apache Spark encryption](notebooks-spark-encryption.md "notebooks-spark-encryption.md").

6. (Optional) Expand **Session parameters**, and then choose or
   enter values for the following options:
   - **Session idle timeout** - choose or enter a value
     between 1 and 480 minutes. The default is 20.
   - **Coordinator size** - A
     _coordinator_ is a special executor that
     orchestrates processing work and manages other executors in a notebook
     session. Currently, 1 DPU is the default and only possible value. A DPU
     (data processing unit) is a relative measure of processing power that
     consists of 4 vCPUs of compute capacity and 16 GB of memory.
   - **Executor size** - An _executor_
     is the smallest unit of compute that a notebook session can request from
     Athena. Currently, 1 DPU is the default and only possible value.
   - **Max concurrent value** - The maximum number of DPUs
     that can run concurrently. The default is 20 and the maximum is 60.
     Increasing this value does not automatically allocate additional
     resources, but Athena will attempt to allocate up to the maximum
     specified when the compute load requires it and when resources are
     available.

7. Choose **Create**. Your notebook opens in a new session in
   the notebook editor.

For information about managing your notebook files, see [Manage notebook files](notebooks-spark-managing.md "notebooks-spark-managing.md").
