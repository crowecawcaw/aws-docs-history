# Creating an ID namespace

source (provider services)

This topic describes the process of creating an ID namespace source using the
**Provider services** method. This method uses a provider service called
LiveRamp. LiveRamp translates third-party encoded data from a source to a target during an
ID mapping workflow.

###### Note

If the input data is the source, then it must have a schema mapping and an associated
AWS Glue database.

###### To create an ID namespace source (provider services)

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/ "https://console.aws.amazon.com/entityresolution/").
2. In the left navigation pane, under **Data preparation**, choose
   **ID namespaces**.
3. On the **ID namespaces** page, in the upper right corner, choose
   **Create ID namespace**.
4. For **Details**, do the following:
   1. For **ID namespace name**, enter a unique name.
   2. (Optional) For **Description**, enter an optional
      description.
   3. For **ID namespace type**, choose
      **Source**.

5. For the **ID namespace method**, choose **Provider
   services**.

###### Note

AWS Entity Resolution currently offers the LiveRamp provider service as an ID namespace method. If
you have a subscription to LiveRamp, then the status appears as
**Subscribed**. For more information about how to subscribe to
LiveRamp, see [Step 1: Subscribe to a provider service on
AWS Data Exchange](prepare-third-party-input-data.md#subscribe-provider-service "prepare-third-party-input-data.md#subscribe-provider-service"). 6. For **Data input**, choose the **AWS Region**,
**AWS Glue database**, the **AWS Glue table**, and the
**Schema mapping** from the dropdown list.

You can add up to 20 data inputs. 7. To specify the **Service access** permissions, choose an option and
take the recommended action.

| Option                                | Recommended action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Create and use a new service role** | • AWS Entity Resolution creates a service role with the required policy for this<br>table.<br>• The default **Service role name** name is<br>`entityresolution-id-mapping-workflow-<timestamp>`.<br>• You must have permissions to create roles and attach policies.<br>• If your input data is encrypted, choose the **This data is<br>encrypted by a KMS key\*<br>• option. Then, enter an **AWS KMS<br>key\*<br>• that is used to decrypt your data input.                                                                                                                                                            |
| **Use an existing service role**      | 1. Choose an **Existing service role name\*<br>• from the<br>dropdown list.<br>The list of roles are displayed if you have permissions to list<br>roles.<br>If you don't have permissions to list roles, you can enter the Amazon<br>Resource Name (ARN) of the role that you want to use.<br>If there are no existing service roles, the option to **Use an<br>existing service role*<br>• is unavailable.<br>2. View the service role by choosing the \*\*View in<br>IAM*<br>• external link.<br>By default, AWS Entity Resolution doesn't attempt to update the existing role<br>policy to add necessary permissions. |

8. (Optional) To enable **Tags** for the resource, choose
   **Add new tag**, and then enter the **Key** and
   **Value** pair.
9. Choose **Create ID namespace**.
   The ID namespace source is created. You are now ready to [create an
   ID namespace target](create-id-namespace-target.md "create-id-namespace-target.md").
