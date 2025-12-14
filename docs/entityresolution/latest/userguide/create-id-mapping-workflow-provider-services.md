# Creating an ID mapping

workflow (provider services)

After completing the [prerequisites](create-idmw-two-accounts-prerequisite.md "create-idmw-two-accounts-prerequisite.md"), you can create
one or more ID mapping workflows using the LiveRamp provider service. LiveRamp translates a
set of source RampIDs to another set using either maintained or derived RampIDs.

###### To create an ID mapping workflow using the provider service

1.  Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/ "https://console.aws.amazon.com/entityresolution/").
2.  In the left navigation pane, under **Workflows**, choose
    **ID mapping**.
3.  On the **ID mapping workflows** page, in the upper right corner,
    choose **Create ID mapping workflow**.
4.  For **Step 1: Specify ID mapping workflow details**, do the
    following.
    1. Enter an **ID mapping workflow name** and an optional
       **Description**.

    ![The Name and Description fields on the Specify ID mapping workflow details page](images/specify-ID-mapping-details-name.png) 2. For the **ID mapping method**, choose **Provider
    services**.

    AWS Entity Resolution currently offers the LiveRamp provider service as an ID mapping method. If
    you have a subscription to LiveRamp, then the status appears as
    **Subscribed**. For more information about how to subscribe to
    LiveRamp, see [Step 1: Subscribe to a provider service on
    AWS Data Exchange](prepare-third-party-input-data.md#subscribe-provider-service "prepare-third-party-input-data.md#subscribe-provider-service").

    ![The Subscribed status for the LiveRamp ID mapping method on the Specify ID mapping workflow page](images/id-mapping-method.PNG)

    ###### Note

    Ensure that your data input file format aligns with the provider service's
    guidelines. For more information about LiveRamp's input file formatting
    guidelines, see [Perform Translation Through ADX](https://docs.liveramp.com/identity/en/perform-transcoding-through-adx.html "https://docs.liveramp.com/identity/en/perform-transcoding-through-adx.html") on the LiveRamp documentation
    website. 3. For **LiveRamp configuration**, enter the following values that
    LiveRamp provides:

        * **Client ID manager ARN**
        * **Client secret manager ARN**

    ![The LiveRamp configuration fields on the Specify ID mapping workflow page](/images/entityresolution/latest/userguide/images/liveramp-configuration.PNG) 4. (Optional) To enable **Tags** for the resource, choose
    **Add new tag**, and then enter the **Key** and
    **Value** pair. 5. Choose **Next**.

5.  For **Step 2: Specify source and target**, do the following.
    1. Turn on **Advanced options**.
    2. For **Source**, choose **ID
       namespace**.

    ![The Source fields on the Specify source and target page](images/specify-source-id-namespace.PNG) 3. For ID namespace, identify where the ID namespace is located, and then take the
    recommended action.

    | Location of ID namespace   | Recommended action                                                                                                   |
    | -------------------------- | -------------------------------------------------------------------------------------------------------------------- |
    | Your own AWS account       | 1. Choose **Your AWS account**.<br>2. Select the ID namespace from the \*_Your ID<br>namespaces_<br>• dropdown list. |
    | Someone else's AWS account | 1. Choose **Another AWS account**.<br>2. Enter the **ID namespace ARN**.                                             |
    4. For **Target**, choose **ID
       namespace**.

    ![The Target field on the Specify source and target page](images/specify-target-id-namespace.PNG) 5. To specify the **Service access** permissions, choose an option
    and take the recommended action.

    ![The Service access options on the Specify source and target page](images/specify-source-target-service-access.PNG)

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

    ![The Data output destination fields on the Specify data output location page](images/specify-data-ouput-IDM.PNG)

8.  For **Step 4: Review and create**, do the following.

        1. Review the selections that you made for the previous steps and edit them if
         necessary.
        2. Choose **Create**.


        A message appears, indicating that the ID mapping workflow has been
         created.

    After you create the ID mapping workflow, you're ready to [run an ID
    mapping workflow](run-id-mapping-workflow.md "run-id-mapping-workflow.md").
