

# Removing private image replication settings in Amazon ECR
<a name="registry-settings-remove"></a>

To remove or disable replication settings for your private registry, you need to configure an empty replication configuration. There is no dedicated removal command in the AWS CLI.

## To remove registry replication settings (AWS Management Console)
<a name="registry-settings-remove-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region to remove your registry replication settings from.

1. In the navigation pane, choose **Private registry**.

1. On the **Private registry** page, choose ** Settings** and then choose **Edit** under **Replication configuration**.

1. Remove all existing replication rules by choosing the delete option for each rule.

1. Choose **Save** to apply the empty replication configuration.

## To remove registry replication settings (AWS CLI)
<a name="registry-settings-remove-cli"></a>

1. Create a JSON file with an empty rules array to remove all replication settings.

   ```
   {
       "rules": []
   }
   ```

1. Apply the empty replication configuration to your registry.

   ```
   aws ecr put-replication-configuration \
        --replication-configuration file://{{empty-replication-settings.json}} \
        --region {{us-west-2}}
   ```

1. Confirm that replication settings have been removed.

   ```
   aws ecr describe-registry \
        --region {{us-west-2}}
   ```

   The output should show an empty `replicationConfiguration` with no rules.

**Important**  
Removing replication settings does not delete any previously replicated repositories or images. You must manually delete replicated content if it is no longer needed.