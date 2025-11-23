# Step 8: Clean up

To avoid further charges for resources you used during this tutorial, you must terminate
the Amazon EC2 instance and its associated resources. Optionally, you can delete the CodeDeploy
deployment component records associated with this tutorial. If you were using a GitHub
repository just for this tutorial, you can delete it now, too.

## To delete a CloudFormation stack

(if you used the CloudFormation template to create an Amazon EC2 instance)

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. In the **Stacks** column, choose the stack starting with
   `CodeDeploySampleStack`.
3. Choose **Delete**.
4. When prompted, choose **Delete stack**. The Amazon EC2 instance and the
   associated IAM instance profile and service role are deleted.

## To manually deregister and

clean up an on-premises instance (if you provisioned an on-premises instance)

1. Use the AWS CLI to call the [deregister](../../../cli/latest/reference/deploy/deregister.md "../../../cli/latest/reference/deploy/deregister.md") command against the on-premises
   instance represented here by `your-instance-name` and the
   associated region by `your-region`:

```
aws deploy deregister --instance-name `your-instance-name` --no-delete-iam-user --region `your-region`
```

2. From the on-premises instance, call the [uninstall](../../../cli/latest/reference/deploy/uninstall.md "../../../cli/latest/reference/deploy/uninstall.md") command:

```
aws deploy uninstall
```

## To manually terminate an Amazon EC2

instance (if you manually launched an Amazon EC2 instance)

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Instances**, choose
   **Instances**.
3. Select the box next to the Amazon EC2 instance you want to terminate. In the
   **Actions** menu, point to **Instance State**, and
   then choose **Terminate**.
4. When prompted, choose **Yes, Terminate**.

## To delete the CodeDeploy

deployment component records

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, then choose **Applications**. 3. Choose **CodeDeployGitHubDemo-App**. 4. Choose **Delete application**. 5. When prompted, enter `Delete`, and then choose
**Delete**.

## To delete your GitHub

repository

See [Deleting a
repository](https://help.github.com/articles/deleting-a-repository/ "https://help.github.com/articles/deleting-a-repository/") in [GitHub help](https://help.github.com "https://help.github.com").
