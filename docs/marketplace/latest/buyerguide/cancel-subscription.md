# Canceling product subscriptions

The steps in the following sections explain how to cancel Amazon Machine Image (AMI),
container product, machine learning, and software as a service (SaaS) products.

###### Topics

- [Canceling your AMI subscription](#cancel-ami-subscription "#cancel-ami-subscription")
- [Canceling a container subscription](#cancel-container-subscription "#cancel-container-subscription")
- [Canceling your machine learning
  subscription](#cancel-machine-learning-subscription "#cancel-machine-learning-subscription")
- [Canceling your SaaS subscription](#cancel-saas-subscription "#cancel-saas-subscription")

## Canceling your AMI subscription

You use the AWS Marketplace console to cancel an AMI subscription, and you then use the Amazon EC2
console to terminate all running instances of the subscription.

###### Warning

You must terminate all
instances in order to stop billing for the subscription.

After you cancel your subscription, you lose access to the software.

The following sets of steps explain how to cancel a subscription and terminate all
instances.

###### To cancel a subscription

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace "https://console.aws.amazon.com/marketplace").

The **Manage subscriptions** page appears. 2. Open the **Delivery method** list and choose **Amazon
Machine Image**. 3. Choose the subscription that you want to cancel. 4. Under **Agreement**, open the **Actions** list and
choose **Cancel subscription**. 5. In the **Cancel subscription** dialog box, enter
`confirm`, then choose **Yes, cancel
subscription**. 6. Complete the next steps to terminate all instances of the subscription. Otherwise,
you may be billed.

###### To terminate instances

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the Amazon EC2 Dashboard page, under **Resources**, choose
   **Instances**.
3. Select the check boxes for all the instances.

###### Important

You must terminate all instances in order to stop billing for the
subscription. 4. Open the **Instance state** list and choose **Terminate
(delete) instance**. 5. On the **Terminate (delete) instance** dialog box, choose
**Terminate (delete)**.

###### Warning

You can't recover a deleted Amazon EC2 instance. If a deleted instance uses ephemeral data storage, you can't recover that data.

## Canceling a container subscription

The following steps explain how to cancel a container subscription.

###### To cancel a subscription

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace "https://console.aws.amazon.com/marketplace").

The **Manage subscriptions** page appears. 2. Open the **Delivery method** list and choose **Container
Image**. 3. Choose the subscription that you want to cancel. 4. Under **Agreement**, open the **Actions** list and
choose **Cancel subscription**. 5. In the **Cancel subscription** dialog box, enter
`confirm`, then choose **Yes, cancel
subscription**.

## Canceling your machine learning

subscription

Before you cancel your machine learning subscription, take the following actions:

- For ML algorithms – Sign in to the AWS Management Console and open the [Amazon SageMaker AI](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") console. Terminate any running
  training jobs for your algorithm. If you created a model package from your algorithm,
  you can't launch a real-time endpoint or create a batch inference job after you cancel
  the subscription.
- For ML model packages or models created from your algorithms – Sign in to the
  AWS Management Console and open the [Amazon SageMaker AI](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") console.
  Terminate any running real-time endpoints for your models, or terminate any running
  batch inference jobs.

###### Warning

To stop billing for the subscription, you must terminate the jobs and endpoints.
Otherwise, billing continues.

###### To cancel a machine learning subscription

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace "https://console.aws.amazon.com/marketplace").
2. On the **Manage subscriptions** page, select the subscription that
   you want to cancel.
3. Under **Agreement**, open the **Actions** list and
   choose **Cancel subscription**.
4. In the **Cancel subscription** dialog box, enter
   `confirm`, then choose **Yes, cancel
   subscription**.

After you cancel, you can't launch your algorithm or model.

## Canceling your SaaS subscription

The process for canceling your SaaS subscription varies depending on the type of
subscription you signed up for.

###### To cancel your SaaS subscription agreement

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace "https://console.aws.amazon.com/marketplace").

The **Manage subscriptions** page appears. 2. Open the **Delivery method** list and choose
**SaaS**. 3. Choose the subscription that you want to cancel. 4. Under **Agreement**, open the **Actions** list and
choose **Cancel subscription**. 5. In the **Cancel subscription** dialog box, enter
`confirm`, then choose **Yes, cancel
subscription**.

###### To cancel auto-renewal for your SaaS contract agreement

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace "https://console.aws.amazon.com/marketplace").
2. Go to the **Product detail** page.
3. Choose **Continue** to get to the ordering page.
4. Choose the **Modify renewal** tab, then choose **Cancel
   renewal**.
