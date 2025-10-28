# Amplitude

The following are the requirements and connection instructions for using Amplitude with
Amazon AppFlow.

###### Note

You can use Amplitude as a source only.

###### Topics

- [Requirements](#amplitude-requirements "#amplitude-requirements")
- [Connection instructions](#amplitude-setup "#amplitude-setup")
- [Notes](#amplitude-notes "#amplitude-notes")
- [Supported destinations](#amplitude-destinations "#amplitude-destinations")
- [Related resources](#amplitude-resources "#amplitude-resources")

## Requirements

You must provide Amazon AppFlow with the API key and secret key for the project with the data
that you want to transfer. Your API key can be found on the Settings page of the Amplitude
dashboard. For more information about how to retrieve this information from Amplitude, see [Settings](https://help.amplitude.com/hc/en-us/articles/235649848#project-general-settings "https://help.amplitude.com/hc/en-us/articles/235649848#project-general-settings") in the Amplitude documentation.

## Connection instructions

###### To connect to Amplitude while creating a flow

1.  Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2.  Choose **Create flow**.
3.  For **Flow details**, enter a name and description for the flow.
4.  (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose
    **Data encryption**, **Customize encryption settings** and
    then choose an existing CMK or create a new one.
5.  (Optional) To add a tag, choose **Tags**, **Add tag**
    and then enter the key name and value.
6.  Choose **Next**.
7.  Choose **Amplitude** from the **Source name** dropdown
    list.
8.  Choose **Connect** to open the **Connect to Amplitude**
    dialog box.

        1. Under **API key**, enter your API key.
        2. Under **Secret key**, enter your secret key.
        3. Under **Data encryption**, enter your AWS KMS key.
        4. Under **Connection name**, specify a name for your connection.
        5. Choose **Connect**.

    ![Connection form for Amplitude with fields for API key, secret key, and connection name.](images/connection_setup-amplitude-console.png)

9.  You will be redirected to the Amplitude login page. When prompted, grant Amazon AppFlow
    permissions to access your Amplitude account.

Now that you are connected to your Amplitude account, you can continue with the flow
creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

###### Tip

If you aren’t connected successfully, ensure that you have followed the instructions in the
[Requirements](#amplitude-requirements "#amplitude-requirements").

## Notes

- When you use Amplitude as a source, you can run schedule-triggered flows at a maximum
  frequency of one flow run per day.
- Amplitude can process 25 MB of data as part of a single flow run.

## Supported destinations

When you create a flow that uses Amplitude as the data source, you can set the destination to any of the following connectors:

- Lookout for Metrics
- Amazon S3

You can also set the destination to any custom connectors that you
create with the Amazon AppFlow Custom Connector SDKs for [Python](https://github.com/awslabs/aws-appflow-custom-connector-python "https://github.com/awslabs/aws-appflow-custom-connector-python") or [Java](https://github.com/awslabs/aws-appflow-custom-connector-java "https://github.com/awslabs/aws-appflow-custom-connector-java") . You can download these SDKs from GitHub.

## Related resources

- [Settings](https://help.amplitude.com/hc/en-us/articles/235649848#project-general-settings "https://help.amplitude.com/hc/en-us/articles/235649848#project-general-settings") in the Amplitude documentation
- [Breaking Data Silos
  with Amazon AppFlow and Amplitude](https://amplitude.com/blog/aws-appflow-amplitude-announcement "https://amplitude.com/blog/aws-appflow-amplitude-announcement") from _Inside Amplitude_
