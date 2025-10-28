# Editing a scaling policy

You can edit a scaling policy using the AWS Management Console, the AWS CLI, or the Application
Auto Scaling API.

###### Editing a scaling policy using the AWS Management Console

You can only edit policies with type Predefined metrics by using the
AWS Management Console

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In the navigation pane, choose **Valkey** or **Redis OSS**
3. Choose the cluster that you want to add a policy to (choose the cluster
   name and not the button to its left).
4. Choose the **Auto Scaling policies** tab.
5. Under **Scaling policies**, choose the button to the left
   of the Auto Scaling policy you wish to change, and then choose
   **Modify**.
6. Make the requisite changes to the policy.
7. Choose **Modify**.
8. Make changes to the policy.
9. Choose **Modify**.
   **Editing a scaling policy using the AWS CLI or the Application
   Auto Scaling API**

You can use the AWS CLI or the Application Auto Scaling API to edit a scaling policy
in the same way that you apply a scaling policy:

- When using the Application Auto Scaling API, specify the name of the
  policy you want to edit in the `PolicyName` parameter. Specify
  new values for the parameters you want to change.
  For more information, see [Applying a scaling
  policy to an ElastiCache for Valkey and Redis OSS cluster](AutoScaling-Defining-Policy.md#AutoScaling-Applying-Policy "AutoScaling-Defining-Policy.md#AutoScaling-Applying-Policy").
