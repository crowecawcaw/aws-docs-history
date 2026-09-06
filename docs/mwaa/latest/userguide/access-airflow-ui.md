

# Accessing Apache Airflow
<a name="access-airflow-ui"></a>

Amazon MWAA lets you access your Apache Airflow environment using multiple methods: the Apache Airflow user interface (UI) console, the Apache Airflow CLI, and the Apache Airflow REST API. You can use the Amazon MWAA console to access and invoke a DAG in your Apache Airflow UI, or use Amazon MWAA APIs to get a token and invoke a DAG. This section describes the permissions needed to access the Apache Airflow UI, how to generate a token to make Amazon MWAA API calls directly in your command shell, and the supported commands in the Apache Airflow CLI.

**Topics**
+ [Prerequisites](#access-airflow-ui-prereqs)
+ [Open the Apache Airflow UI](#access-airflow-ui-onconsole)
+ [Log in to Apache Airflow](#airflow-access-and-login)
+ [Create a Apache Airflow webserver access token](call-mwaa-apis-web.md)
+ [Setting up a custom domain for the Apache Airflow webserver](configuring-custom-domain.md)
+ [Creating an Apache Airflow CLI token](call-mwaa-apis-cli.md)
+ [Using the Apache Airflow REST API](access-mwaa-apache-airflow-rest-api.md)
+ [Apache Airflow CLI command reference](airflow-cli-command-reference.md)

## Prerequisites
<a name="access-airflow-ui-prereqs"></a>

The following section describes the preliminary steps required to use the commands and scripts in this section.

### Access
<a name="access-airflow-ui-prereqs-access"></a>
+ AWS account access in AWS Identity and Access Management (IAM) to the Amazon MWAA permissions policy in [Apache Airflow UI access policy: AmazonMWAAWebServerAccess](access-policies.md#web-ui-access).
+ AWS account access in AWS Identity and Access Management (IAM) to the Amazon MWAA permissions policy [Full API and console access policy: AmazonMWAAFullApiAccess](access-policies.md#full-access-policy).

### AWS CLI
<a name="access-airflow-ui-prereqs-cli"></a>

The AWS Command Line Interface (AWS CLI) is an open source tool that you can use to interact with AWS services using commands in your command-line shell. To complete the steps on this page, you need the following:
+ [AWS CLI – Install version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
+ [AWS CLI – Quick configuration with `aws configure`](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).

## Open the Apache Airflow UI
<a name="access-airflow-ui-onconsole"></a>

The following image displays the link to your Apache Airflow UI on the Amazon MWAA console.

![This image displays the link to your Apache Airflow UI on the Amazon MWAA console.](http://docs.aws.amazon.com/mwaa/latest/userguide/images/mwaa-console-aa-ui.png)


## Log in to Apache Airflow
<a name="airflow-access-and-login"></a>

You need [Apache Airflow UI access policy: AmazonMWAAWebServerAccess](access-policies.md#web-ui-access) permissions for your AWS account in AWS Identity and Access Management (IAM) to access your Apache Airflow UI.

**To access your Apache Airflow UI**

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments) page on the Amazon MWAA console.

1. Choose an environment.

1. Choose **Open Airflow UI**.