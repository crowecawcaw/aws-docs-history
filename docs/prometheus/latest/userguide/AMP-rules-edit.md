# Edit or replace a rules configuration file

If you want to change the rules in a rule file that you have already uploaded to
Amazon Managed Service for Prometheus, you can either upload a new rules file to replace the existing configuration,
or you can edit the current configuration directly in the console. Optionally, you can
download the current file, edit it in a text editor, then upload the new version.

###### To use the Amazon Managed Service for Prometheus console to edit your rules configuration

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home "https://console.aws.amazon.com/prometheus/home").
2. In the upper left corner of the page, choose the menu icon, and then choose
   **All workspaces**.
3. Choose the workspace ID of the workspace, and then choose the **Rules
   management** tab.
4. Select the name of the rules configuration file that you want to edit.
5. (Optional) If you want to download the current rules configuration file,
   choose **Download** or **Copy**.
6. Choose **Modify** to edit the configuration directly within
   the console. Choose **Save** when complete.

Alternately, you can choose **Replace configuration** to
upload a new configuration file. If so, select the new rules definition file,
and choose **Continue** to upload it.

###### To use the AWS CLI to edit a rules configuration file

1. Base64 encode the contents of your rules file. On Linux, you can use the
   following command:

```
base64 `input-file` `output-file`
```

On macOS, you can use the following command:

```
openssl base64 `input-file` `output-file`
```

2. Enter one of the following commands to upload the new file.

On AWS CLI version 2, enter:

```
aws amp put-rule-groups-namespace --data file://`path_to_base_64_output_file` --name `namespace-name`  --workspace-id `my-workspace-id` --region `region`
```

On AWS CLI version 1, enter:

```
aws amp put-rule-groups-namespace --data fileb://`path_to_base_64_output_file` --name `namespace-name`  --workspace-id `my-workspace-id` --region `region`
```

3. It takes a few seconds for your rules file to become active. To check the
   status, enter the following command:

```
aws amp describe-rule-groups-namespace --workspace-id `workspace_id` --name `namespace-name` --region `region`
```

If the `status` is `ACTIVE`, your rules file has taken
effect. Until then, the previous version of this rules file is still
active.
