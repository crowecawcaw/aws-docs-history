

# Using training plans in Studio applications
<a name="training-plan-utilization-for-studio-apps"></a>

You can use SageMaker training plans with SageMaker Studio apps by specifying the training plan ARN in the resource specification when you create a Studio app. A Studio app can only use a training plan if it is in the `Active` status. Only `JupyterLab` and `CodeEditor` app types are supported with training plans.

**Important**  
Training plans are prepaid. You are not charged separately for compute time in the Studio app when running on training plan capacity. Standard charges for storage and other resources still apply.
The target resource of a training plan cannot be changed after purchase.
Plans purchased for Studio apps cannot be cancelled.
Apps running on training plan capacity are automatically shut down **30 minutes** before the capacity block expires. Make sure that all your work is saved before the automatic shutdown. You are not charged for this 30-minute shutdown period.

## Considerations with onboarding
<a name="training-plan-studio-app-onboarding-considerations"></a>
+ Ensure that your Studio instance type quotas for specific app types are sufficient, as app creation fails if the requested instance type exceeds your quota. For more information, see [SageMaker Studio quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html#limits_sagemaker).
+ To use training plans in Studio, add the following permissions to your Studio execution role:
  + `sagemaker:ListTrainingPlans` and `sagemaker:DescribeTrainingPlan` — required for the Studio UI
  + `sagemaker:DescribeTrainingPlan` — required for the API or AWS CLI

  For the Studio UI, add the following policy to your execution role:

  ```
  {
      "Version": "2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sagemaker:ListTrainingPlans",
                  "sagemaker:DescribeTrainingPlan"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

  For the API or AWS CLI only, add the following policy to your execution role:

  ```
  {
      "Version": "2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sagemaker:DescribeTrainingPlan"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

  For more information about updating your Studio execution role, see [Get your execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role) and [Edit domain settings](domain-edit.md).
+ Make sure that the VPC configuration in your domain includes a subnet in the Availability Zone (AZ) specified in your training plan, with at least one free IP address. For more information, see [Choose an Amazon VPC](onboard-vpc.md).

## Considerations for running Studio apps
<a name="training-plan-studio-app-running-considerations"></a>
+ The app launches successfully on reserved training plan capacity if the plan is `Active`. App creation fails if the training plan does not have sufficient capacity for the requested instance type.
+ For apps running on training plan capacity, Studio requires an additional instance from the training plan during maintenance. If no instances are available, maintenance fails and the app transitions to `Failed` status. To recover the app in case of maintenance failures, verify that your training plan has at least one available instance, then create the app again.
+ To use a training plan with an existing app, delete the app and create a new one by specifying the training plan ARN in the resource configuration.

**Note**  
When you create a new space, the storage volume may be placed in a different Availability Zone than your training plan. If this happens, app creation fails. Wait a few minutes and retry app creation to resolve this.

**Topics**
+ [Considerations with onboarding](#training-plan-studio-app-onboarding-considerations)
+ [Considerations for running Studio apps](#training-plan-studio-app-running-considerations)
+ [Create or update a Studio app with a training plan in the Studio UI](use-training-plan-for-studio-app-using-console.md)
+ [Create or update a Studio app with a training plan using the SageMaker API or AWS CLI](use-training-plan-for-studio-app-creation-using-api-cli-sdk.md)