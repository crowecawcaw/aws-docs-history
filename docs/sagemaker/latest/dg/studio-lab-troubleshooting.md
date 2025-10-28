# Troubleshooting

The guide shows common errors that might occur when using Amazon SageMaker Studio Lab (Studio Lab). Each error
contains a description, as well as a solution to the error.

###### Note

You cannot share your password with multiple users or use Studio Lab to mine cryptocurrency.
We don’t recommend using Studio Lab for production tasks because of runtime limits.

**Dependency issues**

On August 8, 2025, Studio Lab migrated from JupyterLab 3 to JupyterLab 4. For information about
JupyterLab 4, see the [4.0.0 - Highlights](https://jupyterlab.readthedocs.io/en/4.0.x/getting_started/changelog.html#highlights "https://jupyterlab.readthedocs.io/en/4.0.x/getting_started/changelog.html#highlights") in the JupyterLab Changelog. If you installed JupyterLab
extensions in your Studio Lab environment before August 8, 2025, you might need to reinstall them
in the JupyterLab 4 environment.

**Can’t access account**

If you can’t access your account, verify that you are using the correct email and password.
If you have forgotten your password, use the following steps to reset your password. If you
still cannot access your account, you must request and register for a new account using the
instructions in [Onboard to Amazon SageMaker Studio Lab](studio-lab-onboard.md "studio-lab-onboard.md").

**Forgot password**

If you forget your password, you must reset it using the following steps.

1. Navigate to the [Studio Lab landing
   page](https://studiolab.sagemaker.aws "https://studiolab.sagemaker.aws").
2. Select **Sign in**.
3. Select **Forgot password?** to open a new page.
4. Enter the email address that you used to sign up for an account.
5. Select **Send reset link** to send an email with a password reset link.
6. From the password reset email, select **Reset your password**.
7. Enter your new password.
8. Select **Submit**.

**Can't launch project runtime**

If the Studio Lab project runtime does not launch, try launching it again. If this doesn't
work, switch the instance type from CPU to GPU (or in reverse). For more information, see [Change your compute type](studio-lab-manage-runtime.md#studio-lab-manage-runtime-change "studio-lab-manage-runtime.md#studio-lab-manage-runtime-change").

**Runtime stopped running unexpectedly**

If there is an issue with the environment used to run JupyterLab, then Studio Lab will
automatically recreate the environment. Studio Lab does not support manual activation of this
process.

**Conflicting versions**

Because you can add packages and modify your environment as needed, you may run into
conflicts between packages in your environment. If there are conflicts between packages in your
environment, you must remove the conflicting package.

**Environment build fails**

When you build an environment from a YAML file, a package-version conflict or file issue
might cause a build to fail. To resolve this, remove the environment by running the following
command. Do this before attempting to build it again.

```
conda remove --name `<YOUR_ENVIRONMENT>` --all
```

**Error message about allowing to download script from domain
\*.awswaf.com**

Studio Classic uses the web application firewall service AWS WAF to protect your resources,
which uses JavaScript. If you are using a browser security plugin that prevents JavaScript from
downloading, this error may pop up. To use Studio Classic, allow the JavaScript download from
\*.awswaf.com as a trusted domain. For more information on AWS WAF, see [AWS WAF](../../../waf/latest/developerguide/waf-chapter.md "../../../waf/latest/developerguide/waf-chapter.md") from the AWS WAF, AWS Firewall Manager, and
AWS Shield Advanced. Developer Guide.

**Disk space is full**

If you run into a notification saying mentioning that your disk space is full or
**File Load Error for `<FILE_NAME>`** while
attempting to open a file, you can remove files, directories, libraries, or environments to
increase space. For more information on managing your libraries and environments, see [Manage your environment](studio-lab-use-manage.md "studio-lab-use-manage.md").

\***\*Project runtime is in safe mode**
notification\*\*

If you run into a notification that **Project runtime is in safe mode**,
you must free up some disk space to resume using the Studio Lab project runtime. Follow the
instructions in the preceding troubleshoot item, **Disk space is
full**. Once up to at least 500 MB of space has been cleared, you may restart the
project runtime to use Studio Lab. This can be done by choosing **Amazon SageMaker Studio Lab** in
the top menu of Studio Lab and choosing **Restart JupyterLab...**.

git **Cannot import `cv2`**

If you run into an error when importing `cv2` after installing
`opencv-python`, you must uninstall `opencv-python` and install
`opencv-python-headless` as follows.

```
%pip uninstall opencv-python --yes
%pip install opencv-python-headless
```

You can then import `cv2` as expected.

**Studio Lab becomes unresponsive when opening large files**

The Studio Lab IDE may fail to render when large files are opened, resulting in blocked access
to Studio Lab resources. To resolve this, reset the Studio Lab workspace using the following
procedure.

1. After you open the IDE, copy the URL in your browser's address bar. This URL should be
   in the
   `https://xxxxxx.studio.us-east-2.sagemaker.aws/studiolab/default/jupyter/lab`
   format. Close the tab.
2. In a new tab, paste the URL and remove anything after
   `https://xxxxxx.studio.us-east-2.sagemaker.aws/studiolab/default/jupyter/lab`.
3. Add `?reset` to the end of the URL, so it is in the
   `https://xxxxxx.studio.us-east-2.sagemaker.aws/studiolab/default/jupyter/lab?reset`
   format.
4. Navigate to the updated URL. This resets the saved UI state and makes the Studio Lab IDE
   responsive.
