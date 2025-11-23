# Step 1. Launch the stack

The CloudFormation template in this section deploys _Customizations for
AWS Control Tower_ (CfCT) in your account.

###### Note

You are responsible for the cost of the AWS services used while you run CfCT.
For more details, see [Cost](cost.md "cost.md").

1. To launch _Customizations for AWS Control Tower_,
   [download the template from GitHub](https://github.com/aws-solutions/aws-control-tower-customizations/blob/main/customizations-for-aws-control-tower.template "  https://github.com/aws-solutions/aws-control-tower-customizations/blob/main/customizations-for-aws-control-tower.template") and then launch it from [AWS CloudFormation](https://console.aws.amazon.com/cloudformation/home?region=us-east-1 "https://console.aws.amazon.com/cloudformation/home?region=us-east-1").
2. The template launches in the US East (N. Virginia) Region by default. To launch CfCT in a
   different AWS Region, use the Region selector in the console navigation
   bar.

###### Note

CfCT must be launched in the same Region and account where you deployed
your AWS Control Tower landing zone, which is your home Region. 3. On the **Create stack** page, verify that the correct
template URL shows in the **URL** text box
and choose **Next**. 4. On the **Specify stack details** page, assign a name to your
CfCT stack. 5. Under **Parameters**, review the following parameters and
modify them in the template, if necessary.

| Pipeline Configuration                 |
| -------------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Parameter                              | Default                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Pipeline Approval<br>Stage**         | `No`                                 | Choose whether to change the pipeline configuration from<br>the default automated approval stage to a manual approval<br>stage. For more information, see [CfCT customization guide](cfct-customizations-dev-guide.md "cfct-customizations-dev-guide.md").                                                                                                                                                                                                            |
| **Pipeline Approval Email<br>Address** | <Optional Input>                     | The email address for approval notifications. To use this<br>parameter, you must set the \*_Pipeline<br>Approval Stage_<br>• parameter to<br>`Yes`.                                                                                                                                                                                                                                                                                                                   |
| **AWS CodePipeline<br>Source**         | `Amazon S3`                          | The source for AWS CodePipeline to help you select where<br>to store and configure the CfCT customizations.                                                                                                                                                                                                                                                                                                                                                           |
| AWS CodeCommit Setup                   |
| ---                                    |
| Parameter                              | Default                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Existing CodeCommit<br>Repository?** | `No`                                 | Choose whether to use an existing CodeCommit Git<br>repository. If you choose `Yes`, you must set the<br>**CodePipeline Source**<br>parameter to `AWS CodeCommit`.                                                                                                                                                                                                                                                                                                    |
| **CodeCommit Repository<br>Name**      | `custom-control-tower-configuration` | If<br>you provide the name of an existing Git repository, you must<br>set the \*_Existing CodeCommit<br>Repository?_<br>• parameter to `Yes` and<br>enter the exact name of that repository.                                                                                                                                                                                                                                                                          |
| **CodeCommit Branch<br>Name**          | `main`                               | The Git branch where the customization package is stored.<br>To use this parameter, you must set the \*_CodePipeline Source_<br>• parameter to<br>`AWS CodeCommit`.                                                                                                                                                                                                                                                                                                   |
| CloudFormation StackSets Configuration |
| ---                                    |
| Parameter                              | Default                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Region Concurrency<br>Type**         | `PARALLEL`                           | Select the concurrency type of deploying StackSets<br>operations in Regions. This setting is applicable for<br>create, update, and delete workflows. Other allowed value is<br>`SEQUENTIAL`.                                                                                                                                                                                                                                                                          |
| **Max Concurrent<br>Percentage**       | `100`                                | The maximum percentage of accounts in which to perform<br>this operation at one time. The max allowed value is 100.<br>For more information, refer to [Stack Set operation options](../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md#stackset-ops-options "../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md#stackset-ops-options").                                                                                                 |
| **Failure Tolerance<br>Percentage**    | `10`                                 | The percentage of accounts, per Region, for which this<br>stack operation can fail before AWS CloudFormation stops the<br>operation in that Region. The minimum allowed value is 0 and<br>max allowed value is 100. For more information, refer to<br>[Stack Set operation options](../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md#stackset-ops-options "../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md#stackset-ops-options"). |

6. Choose **Next**.
7. On the **Configure stack options** page, choose
   **Next**.
8. On the **Review** page, review and confirm the settings. Be
   sure to check the box acknowledging that the template will create AWS Identity and Access Management
   (IAM) resources.
9. Choose **Create stack** to deploy the stack.

You can view the status of the stack in the CloudFormation console in the
**Status** column. You should see a status of
**CREATE_COMPLETE** in approximately 15 minutes.
