# Upload a rules configuration file to

Amazon Managed Service for Prometheus

Once you know what rules you want in your rules configuration file, you can either
create and edit it within the console, or you can upload a file with the console or
AWS CLI.

###### Note

If you are running an Amazon EKS cluster, you can also upload a rule configuration file
using [AWS Controllers for
Kubernetes](integrating-ack.md "integrating-ack.md").

###### To use the Amazon Managed Service for Prometheus console to edit or replace your rules configuration and

create the namespace

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home "https://console.aws.amazon.com/prometheus/home").
2. In the upper left corner of the page, choose the menu icon, and then choose
   **All workspaces**.
3. Choose the workspace ID of the workspace, and then choose the **Rules
   management** tab.
4. Choose **Add namespace**.
5. Choose **Choose file**, and select the rules definition
   file.

Alternately, you can create and edit a rules definition file directly in the
Amazon Managed Service for Prometheus console by selecting **Define configuration**. This
will create a sample default definition file that you edit before
uploading. 6. (Optional) To add tags to the namespace, choose **Add new
tag**.

Then, for **Key**, enter a name for the tag. You can add an
optional value for the tag in **Value**.

To add another tag, choose **Add new tag**. 7. Choose **Continue**. Amazon Managed Service for Prometheus creates a new namespace with
the same name as the rules file that you selected.

###### To use the AWS CLI to upload an alert manager configuration to a workspace in a new

namespace

1. Base64 encode the contents of your alert manager file. On Linux, you can use
   the following command:

```
base64 `input-file` `output-file`
```

On macOS, you can use the following command:

```
openssl base64 `input-file` `output-file`
```

2. Enter one of the following commands to create the namespace and upload the
   file.

On AWS CLI version 2, enter:

```
aws amp create-rule-groups-namespace --data file://`path_to_base_64_output_file` --name `namespace-name`  --workspace-id `my-workspace-id` --region `region`
```

On AWS CLI version 1, enter:

```
aws amp create-rule-groups-namespace --data fileb://`path_to_base_64_output_file` --name `namespace-name`  --workspace-id `my-workspace-id` --region `region`
```

3. It takes a few seconds for your alert manager configuration to become active.
   To check the status, enter the following command:

```
aws amp describe-rule-groups-namespace --workspace-id `workspace_id` --name `namespace-name` --region `region`
```

If the `status` is `ACTIVE`, your rules file has taken
effect.
