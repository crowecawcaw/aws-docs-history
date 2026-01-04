# Creating an ID mapping workflow

(rule-based)

After you've completed the [prerequisites](create-idmw-two-accounts-prerequisite.md "create-idmw-two-accounts-prerequisite.md"), you can create
one or more ID mapping workflows to use matching rules to translate first-party data from a
source to a target.

###### To create a rule-based ID mapping workflow across two AWS accounts

1.  Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/ "https://console.aws.amazon.com/entityresolution/").
2.  In the left navigation pane, under **Workflows**, choose
    **ID mapping**.
3.  On the **ID mapping workflows** page, in the upper right corner,
    choose **Create ID mapping workflow**.
4.  For **Step 1: Specify ID mapping workflow details**, do the
    following.
    1. Enter an **ID mapping workflow name** and an optional
       **Description**.

    ![The Name and Description fields on the Specify ID mapping workflow details page](images/specify-ID-mapping-details-name.png) 2. For the **ID mapping method**, choose
    **Rule-based**. 3. (Optional) To process only new, updated, or deleted records in the workflow,
    select **Enable incremental processing**.

    ![The ID mapping section of the Specify ID mapping workflow page with the Enable incremental process checkbox selected.](/images/entityresolution/latest/userguide/images/id-mapping-method-enable-inc-proc.png)

    AWS Entity Resolution processes only new, updated, or deleted records in either the Source or
    Target ID namespace, rather than recreating the entire ID mapping table.

    When you choose incremental processing and your data table has a DELETE column,
    AWS Entity Resolution handles records differently based on the DELETE column value.

        * Records marked as `true` in the DELETE column are removed from
         the ID mapping table.
        * Records marked as `false` in the DELETE column are ingested into
         Amazon S3.

    If you leave this option unselected, AWS Entity Resolution runs the default batch processing ID
    mapping workflow on the ID mapping table. 4. (Optional) To enable **Tags** for the resource, choose
    **Add new tag**, and then enter the **Key** and
    **Value** pair. 5. Choose **Next**.

5.  For **Step 2: Specify source and target**, do the following.
    1. Turn on **Advanced options**.
    2. For **Source**, choose **Matching workflow**,
       and then select the existing **Matching workflow** from the
       dropdown list.
    3. For **Target**, choose **Matching workflow**,
       and then select the existing **Matching workflow** from the
       dropdown list.
    4. For **Rule parameters**, specify the **Rule
       controls** by choosing whether a **Source** or a
       **Target** can provide rules in an ID mapping workflow.

    Rule controls must be compatible between the source and the target to be used in
    an ID mapping workflow. For example, if a source ID namespace limits rules to the
    target but the target ID namespace limits rules to the source, this results in an
    error. 5. For **Comparison and matching parameters**, do the
    following.

        1. Specify the **Comparison type** by choosing an option based
         on your goal.




        | Your goal | Recommended option |
        | --- | --- |
        | Find any combination of matches across data stored in multiple<br>input fields, regardless of whether the data is in the same or different<br>input field. | **Multiple input fields** |
        | Limit comparison within a single input field, when similar data<br>stored across multiple input fields shouldn't be matched. | **Single input field** |
        2. Specify the **Record matching type** by choosing an option
         based on your goal.




        | Your goal | Recommended option |
        | --- | --- |
        | Limit the record matching type to store only one matching record in<br>the source for each matched record in the target when you create the ID<br>mapping workflow. | **One source to one target** |
        | Limit the record matching type to store all matching records in the<br>source for each matched record in the target when you create the ID<br>mapping workflow. | **Many sources to one target** |


        ###### Note

        You must specify compatible limitations for the source and target ID
         namespaces.

    6. To specify the **Service access** permissions, choose an option
       and take the recommended action.

    ![The Service access options on the Specify source and target page](/images/entityresolution/latest/userguide/images/specify-source-target-service-access.PNG)

    | Option                                | Recommended action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Create and use a new service role** | • AWS Entity Resolution creates a service role with the required policy for this<br>table.<br>• The default **Service role name** is<br>`entityresolution-id-mapping-workflow-<timestamp>`.<br>• You must have permissions to create roles and attach<br>policies.<br>• If your input data is encrypted, choose the **This data is<br>encrypted by a KMS key\*<br>• option. Then, enter an<br>**AWS KMS key\*<br>• that is used to decrypt your data<br>input.                                                                                                                                                              |
    | **Use an existing service role**      | 1. Choose an **Existing service role name\*<br>• from the<br>dropdown list.<br>The list of roles are displayed if you have permissions to list<br>roles.<br>If you don't have permissions to list roles, you can enter the<br>Amazon Resource Name (ARN) of the role that you want to use.<br>If there are no existing service roles, the option to<br>**Use an existing service role*<br>• is<br>unavailable.<br>2. View the service role by choosing the \*\*View in<br>IAM*<br>• external link.<br>By default, AWS Entity Resolution doesn't attempt to update the existing role<br>policy to add necessary permissions. |

6.  Choose **Next**.
7.  For **Step 3: Specify data output location – _optional_**, do the following.
    1. For **Data output destination**, do the following.
       1. Choose the **Amazon S3 location** for the data output.
       2. For **Encryption**, if you choose to **Customize
          encryption settings**, then enter the **AWS KMS key**
          ARN or choose **Create an AWS KMS key**.

    2. View the **LiveRamp generated output**.
    3. Choose **Next**.

8.  For **Step 4: Review and create**, do the following.

        1. Review the selections that you made for the previous steps and edit them if
         necessary.
        2. Choose **Create**.


        A message appears, indicating that the ID mapping workflow has been
         created.

    After you create the ID mapping workflow, you're ready to [run an ID
    mapping workflow](run-id-mapping-workflow.md "run-id-mapping-workflow.md").
