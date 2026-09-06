

# Open the SageMaker Profiler UI application
<a name="profiler-access-smprofiler-ui"></a>

**Note**  
End of support notice: On June 30, 2027, AWS will end support for Amazon SageMaker Profiler. After June 30, 2027, you will no longer be able to access the Profiler console or Profiler resources. For more information, see [Profiler availability change](profiler-availability-change.md).

You can access the SageMaker Profiler UI application through the following options.

**Topics**
+ [Option 1: Launch the SageMaker Profiler UI from the domain details page](#profiler-access-smprofiler-ui-console-smdomain)
+ [Option 2: Launch the SageMaker Profiler UI application from the SageMaker Profiler landing page in the SageMaker AI console](#profiler-access-smprofiler-ui-console-profiler-landing-page)
+ [Option 3: Use the application launcher function in the SageMaker AI Python SDK](#profiler-access-smprofiler-ui-app-launcher-function)

## Option 1: Launch the SageMaker Profiler UI from the domain details page
<a name="profiler-access-smprofiler-ui-console-smdomain"></a>

If you have access to the SageMaker AI console, you can take this option.

**Navigate to the domain details page**

 The following procedure shows how to navigate to the domain details page. 

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **domains**. 

1. From the list of domains, select the domain in which you want to launch the SageMaker Profiler application.

**Launch the SageMaker Profiler UI application**

The following procedure shows how to launch the SageMaker Profiler application that is scoped to a user profile. 

1. On the domain details page, choose the **User profiles** tab. 

1. Identify the user profile for which you want to launch the SageMaker Profiler UI application. 

1. Choose **Launch** for the selected user profile, and choose **Profiler**. 

## Option 2: Launch the SageMaker Profiler UI application from the SageMaker Profiler landing page in the SageMaker AI console
<a name="profiler-access-smprofiler-ui-console-profiler-landing-page"></a>

The following procedure describes how to launch the SageMaker Profiler UI application from the SageMaker Profiler landing page in the SageMaker AI console. If you have access to the SageMaker AI console, you can take this option.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **Profiler**.

1. Under **Get started**, select the domain in which you want to launch the Studio Classic application. If your user profile only belongs to one domain, you do not see the option for selecting a domain.

1. Select the user profile for which you want to launch the SageMaker Profiler UI application. If there is no user profile in the domain, choose **Create user profile**. For more information about creating a new user profile, see [Add user profiles](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-user-profile-add.html).

1. Choose **Open Profiler**.

## Option 3: Use the application launcher function in the SageMaker AI Python SDK
<a name="profiler-access-smprofiler-ui-app-launcher-function"></a>

If you are a SageMaker AI domain user and have access only to SageMaker Studio, you can access the SageMaker Profiler UI application through SageMaker Studio Classic by running the [`sagemaker.interactive_apps.detail_profiler_app.DetailProfilerApp`](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_core.html) function.

Note that SageMaker Studio Classic is the previous Studio UI experience before re:Invent 2023, and is migrated as an application into a newly designed Studio UI at re:Invent 2023. The SageMaker Profiler UI application is available at SageMaker AI domain level, and thus requires your domain ID and user profile name. Currently, the `DetailedProfilerApp` function only works within the SageMaker Studio Classic application; the function properly takes in the domain and user profile information from SageMaker Studio Classic.

For domain, domain users, and Studio created before re:Invent 2023, Studio Classic would be the default experience unless you have updated it following the instructions at [Migrating from Amazon SageMaker Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-migrate.html). If this is your case, there's no further action needed, and you can directly launch the SageMaker Profiler UI application by running the `DetailProfilerApp` funciton.

If you created a new domain and Studio after re:Invent 2023, launch the Studio Classic application within the Studio UI and then run the `DetailProfilerApp` function to launch the SageMaker Profiler UI application.

Note that the `DetailedProfilerApp` function doesn’t work in other SageMaker AI machine learning IDEs, such as the SageMaker Studio JupyterLab application, the SageMaker Studio Code Editor application, and SageMaker Notebook instances. If you run the `DetailedProfilerApp` function in those IDEs, it returns a URL to the Profiler landing page in the SageMaker AI console, instead of a direct link to open the Profiler UI application.