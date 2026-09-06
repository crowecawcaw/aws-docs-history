

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Deploy an AWS Mainframe Modernization application
<a name="applications-m2-deploy"></a>

Use the AWS Mainframe Modernization console to deploy an AWS Mainframe Modernization application. You need to deploy your applications on a runtime environment before performing tasks.

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md).

## Deploy an application
<a name="applications-m2-deploy-console"></a>

To run an AWS Mainframe Modernization application, you must first deploy it to a runtime environment. An application can have more than one version. Each version of an application has its own application definition. To deploy an application, you must specify the version that you want to deploy.

You can deploy only one version of a given application at a time. If you deploy a version of an application, then decide to deploy a different version instead, you must first stop the application if it is running.

**To deploy an application**

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/).

1. In the AWS Region selector, choose the Region where you want to create the application.

1. On the **Applications** page, choose the application that you want to deploy.

1. Choose **Deploy application**.

1. In the **Available versions** section, choose the version that you want to deploy.

1. In the **Environments** section, choose a runtime environment where you want your application to run.

1. Choose **Deploy**.

**To deploy a different version of a deployed application**

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/).

1. In the AWS Region selector, choose the Region where you want to create the application.

1. On the **Applications** page, choose the application that you want to deploy.

1. From the **Actions** menu, choose **Stop application**.

1. After the application stops, choose **Deploy application**.

1. In the **Available versions** section, choose the version that you want to deploy. In the **Environments** section, the environment that the application is already deployed in is preselected.

1. Choose **Deploy**.