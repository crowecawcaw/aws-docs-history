

# Enable Amazon Braket
<a name="braket-enable-overview"></a>

**Tip**  
**Learn the foundations of quantum computing with AWS\!** Enroll in the [Amazon Braket Digital Learning Plan](https://skillbuilder.aws/learning-plan/EH35DWGU3R/amazon-braket--knowledge-badge-readiness-path-includes-labs) and earn your own Digital badge after completing a series of learning courses and a digital assessment.

You can enable Amazon Braket in your account through the [AWS console](http://console.aws.amazon.com/).

**Topics**
+ [Prerequisites](#braket-enable-prereqs)
+ [Steps to enable Amazon Braket](#braket-enable-steps)

## Prerequisites
<a name="braket-enable-prereqs"></a>

To enable and run Amazon Braket, you must have a user or role with permission to initiate Amazon Braket actions. These permissions are included in the  **AmazonBraketFullAccess**  IAM policy (arn:aws:iam::aws:policy/AmazonBraketFullAccess).

**Note**  
 *If you are an administrator:*   
To give other users access to Amazon Braket, grant users permissions by attaching the *AmazonBraketFullAccess* policy or by attaching a custom policy that you create. To learn more about the permissions necessary to use Amazon Braket, see [Managing access to Amazon Braket ](braket-manage-access.md).

## Steps to enable Amazon Braket
<a name="braket-enable-steps"></a>

1. Sign in to the [Amazon Braket console](https://console.aws.amazon.com/braket/) with your AWS account.

1. Open the Amazon Braket console.

1. From the Braket landing page, click Get Started to be taken to the **Service Dashboard ** page. The alert at the top of your service dashboard will walk you through the following three steps:

   1. Creating [service-linked roles (SLR)](braket-slr.md)

   1. Enabling access to third-party quantum computers

   1. Creating a new Jupyter notebook instance

In order to use third-party quantum devices, you need to agree to certain conditions regarding data transfer between yourself, AWS, and those devices. The terms and conditions of this agreement are provided on the **General** tab of the **Permissions and settings** page in the Amazon Braket console.

**Note**  
Quantum devices that don't involve any third-parties, such as the Braket local simulators or on-demand simulators, can be used without agreeing to the **Enable third-party devices** agreement.  
Accepting these terms to enable use of third-party devices only needs to be done **once per account** if you are accessing third-party hardware. 