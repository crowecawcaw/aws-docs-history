

# Open TensorBoard through the SageMaker AI console
<a name="debugger-htb-access-tb-console"></a>

You can also use the SageMaker AI console UI to open the TensorBoard application. There are two options to open the TensorBoard application through the SageMaker AI console.

**Topics**
+ [Option 1: Launch TensorBoard from the domain details page](#debugger-htb-access-tb-console-domain-detail)
+ [Option 2: Launch TensorBoard from the TensorBoard landing page](#debugger-htb-access-tb-console-landing-pg)

## Option 1: Launch TensorBoard from the domain details page
<a name="debugger-htb-access-tb-console-domain-detail"></a>

**Navigate to the domain details page**

 The following procedure shows how to navigate to the domain details page. 

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **Admin configurations**.

1. Under **Admin configurations**, choose **domains**. 

1. From the list of domains, select the domain in which you want to launch the TensorBoard application.

**Launch a user profile application**

The following procedure shows how to launch a Studio Classic application that is scoped to a user profile. 

1. On the domain details page, choose the **User profiles** tab. 

1. Identify the user profile for which you want to launch the Studio Classic application. 

1. Choose **Launch** for your selected user profile, then choose **TensorBoard**. 

## Option 2: Launch TensorBoard from the TensorBoard landing page
<a name="debugger-htb-access-tb-console-landing-pg"></a>

The following procedure describes how to launch a TensorBoard application from the TensorBoard landing page. 

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **TensorBoard**.

1. Under **Get started**, select the domain in which you want to launch the Studio Classic application. If your user profile only belongs to one domain, you do not see the option for selecting a domain.

1. Select the user profile for which you want to launch the Studio Classic application. If there is no user profile in the domain, choose **Create user profile**. For more information, see [Add and Remove User Profiles](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-user-profile-add.html).

1. Choose **Open TensorBoard**.

The following screenshot shows the location of TensorBoard in the left navigation pane of the SageMaker AI console and the SageMaker AI with TensorBoard landing page in the main pane.

![The TensorBoard landing page.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/debugger/htb-landing-page.png)
