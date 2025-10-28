# Launch your Amazon SageMaker Studio Lab project runtime

The Amazon SageMaker Studio Lab project runtime lets you write and run code directly from your browser. It
is based on JupyterLab and has an integrated terminal and console. For more information about
JupyterLab, see the [JupyterLab
Documentation](https://jupyterlab.readthedocs.io/en/stable/ "https://jupyterlab.readthedocs.io/en/stable/").

The following topic gives information about how to manage your project runtime. These
topics require that you sign in to your Amazon SageMaker Studio Lab account. For more information about signing
in, see [Sign in to Studio Lab](studio-lab-onboard.md#studio-lab-onboard-signin "studio-lab-onboard.md#studio-lab-onboard-signin").
For more information about your project, see [Amazon SageMaker Studio Lab components overview](studio-lab-overview.md "studio-lab-overview.md").

###### Topics

- [Start your project runtime](#studio-lab-manage-runtime-start "#studio-lab-manage-runtime-start")
- [Stop your project runtime](#studio-lab-manage-runtime-stop "#studio-lab-manage-runtime-stop")
- [View remaining compute time](#studio-lab-manage-runtime-view "#studio-lab-manage-runtime-view")
- [Change your compute type](#studio-lab-manage-runtime-change "#studio-lab-manage-runtime-change")

## Start your project runtime

To use Studio Lab, you must start your project runtime. This runtime gives you access to the
JupyterLab environment.

1. Navigate to the Studio Lab project overview page. The URL takes the following
   format.

```
https://studiolab.sagemaker.aws/users/`<YOUR_USER_NAME>`
```

2. Under **My Project**, select a compute type. For more information
   about compute types, see [Compute instance type](studio-lab-overview.md#studio-lab-overview-project-compute "studio-lab-overview.md#studio-lab-overview-project-compute").
3. Select **Start runtime**.

You might be asked to solve a CAPTCHA puzzle. For more information on CAPTCHA, see
[What is a CAPTCHA puzzle?](../../../waf/latest/developerguide/waf-captcha-puzzle.md "../../../waf/latest/developerguide/waf-captcha-puzzle.md") 4. One time setup, for first time starting runtime using your Studio Lab account:

    1. Enter a mobile phone number to associate with your Amazon SageMaker Studio Lab account and choose
     **Continue**.


    For information on supported countries and regions, see [Supported countries and regions (SMS channel)](../../../pinpoint/latest/userguide/channels-sms-countries.md "../../../pinpoint/latest/userguide/channels-sms-countries.md").
    2. Enter the 6-digit code sent to the associated mobile phone number and choose
     **Verify**.

5. After the runtime is running, select **Open project** to open the
   project runtime environment in a new browser tab.

## Stop your project runtime

When you stop your project runtime, your files are not automatically saved. To ensure that
you don't lose your work, save all of your changes before stopping your project
runtime.

- Under **My Project**, select **Stop runtime**.

## View remaining compute time

Your project runtime has limited compute time based on the compute type that you select.
For more information about compute time in Studio Lab, see [Compute instance type](studio-lab-overview.md#studio-lab-overview-project-compute "studio-lab-overview.md#studio-lab-overview-project-compute").

- Under **My Project**, view **Time remaining**.

## Change your compute type

You can switch your compute type based on your workflow. For more information about
compute types, see [Compute instance type](studio-lab-overview.md#studio-lab-overview-project-compute "studio-lab-overview.md#studio-lab-overview-project-compute").

1. Save any project files before changing the compute type.
2. Navigate to the Studio Lab project overview page. The URL takes the following
   format.

```
https://studiolab.sagemaker.aws/users/`<YOUR_USER_NAME>`
```

3. Under **My Project**, select the desired compute type (CPU or GPU).
4. Confirm your choice by selecting **Restart** in the **Restart
   project runtime?** dialog box. Studio Lab stops your current project runtime, then
   starts a new project runtime with your updated compute type.
5. After your project runtime has started, select **Open project**. This
   opens your project runtime environment in a new browser tab. For information about using
   your project runtime environment, see [Use the Amazon SageMaker Studio Lab project runtime](studio-lab-use.md "studio-lab-use.md").
