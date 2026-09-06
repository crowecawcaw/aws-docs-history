

# Configuring lifecycle policies
<a name="enable-lifecycle-management"></a>

When you create an EFS file system that has the recommended settings using the AWS Management Console, the file system is automatically configured with the following default lifecycle configuration:
+ **Transition into IA** is set to **30 days since last access**.
+ **Transition into Archive** is set to **90 days since last access**.
+ **Transition into Standard** is set to **None**.

You can change the default lifecycle policies when creating a file system with customized settings using the AWS Management Console or when creating a file system using the AWS CLI. Alternately, you can change the policies after the file system is created, as described in the following procedures.

## Using the console
<a name="console2-enable-lifemgnt-filesystem"></a>

You can use the AWS Management Console to set the lifecycle policies for an existing file system.

1. Sign in to the AWS Management Console and open the Amazon EFS console at [ https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/).

1. Choose **File systems** to display the list of file systems in your account.

1. Choose the file system on which you want to modify lifecycle policies.

1. On the file system details page, in the **General** section, choose **Edit**. The **Edit** page displays.

1. For Lifecycle management, configure the lifecycle policies:
   + Set **Transition into IA** to one of the available options. To stop moving files into IA storage, choose **None**.
   + Set **Transition into Archive** to one of the available options. To stop moving files into Archive storage, choose **None**.
   + Set **Transition into Standard** to **On first access** to move files that are in IA storage to standard storage when they're accessed for non-metadata operations.

     To stop moving files from IA or Archive to Standard storage on first access, select **None**.

1. Choose **Save changes** to save your changes.

## Using the AWS CLI
<a name="lifecycle-mgnt-cli"></a>

You can use the AWS CLI to set or modify a file system's lifecycle policies.
+ Run the [`put-lifecycle-configuration`](https://docs.aws.amazon.com/cli/latest/reference/efs/put-lifecycle-configuration.html) AWS CLI command or the [PutLifecycleConfiguration](https://docs.aws.amazon.com/efs/latest/APIReference/API_PutLifecycleConfiguration.html) API command, specifying the file system ID of the file system for which you are managing lifecycle management.

  ```
  $  aws efs put-lifecycle-configuration \
  --file-system-id {{File-System-ID}} \
  --lifecycle-policies "[{\"TransitionToIA\":\"AFTER_60_DAYS\"},{\"TransitionToPrimaryStorageClass\":\"AFTER_1_ACCESS\"},{\"TransitionToArchive\":\"AFTER_90_DAYS\"}]" \
  --region us-west-2 \
  --profile adminuser
  ```

  You get the following response.

  ```
  {
      "LifecyclePolicies": [
          {
              "TransitionToIA": "AFTER_60_DAYS"
          },
          {
              "TransitionToPrimaryStorageClass": "AFTER_1_ACCESS"
          },
          {
              "TransitionToArchive": "AFTER_90_DAYS"
          }
      ]
  }
  ```

**To stop lifecycle management for an existing file system (CLI)**
+  Run the `put-lifecycle-configuration` command specifying the file system ID of the file system for which you are stopping lifecycle management. Keep the `--lifecycle-policies` property empty.

  ```
  $  aws efs put-lifecycle-configuration \
  --file-system-id {{File-System-ID}} \
  --lifecycle-policies \
  --region us-west-2 \
  --profile adminuser
  ```

  You get the following response.

  ```
  {
      "LifecyclePolicies": []
  }
  ```