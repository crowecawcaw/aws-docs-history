

# Using Amazon Q Developer with JupyterLab
<a name="jupyterlab-setup"></a>

This page describes how to set up and activate Amazon Q Developer for JupyterLab. Once activated, Amazon Q can make code recommendations automatically as you write your code.

**Note**  
Python is the only programming language that Amazon Q supports in JupyterLab.

## Installing JupyterLab
<a name="jupyterlab-setup-itself"></a>

Install [JupyterLab](https://pypi.org/project/jupyterlab) on your computer or if you already have JupyterLab installed, check its version by running the following command.

```
pip show jupyterlab
```

Note the version in the response, and follow the corresponding directions in one of the following sections.

## Installation using pip for Jupyter Lab version >= 4.0
<a name="jupyterlab-setup-pip-v4"></a>

You can install and enable the Amazon Q extension for JupyterLab 4 with the following commands.

```
# JupyterLab 4
pip install amazon-q-developer-jupyterlab-ext
```

## Installation using pip for Jupyter Lab version >= 3.6 and < 4.0
<a name="jupyterlab-setup-pip-v3"></a>

You can install and enable the Amazon Q extension for JupyterLab 3 with the following commands.

```
# JupyterLab 3
pip install amazon-q-developer-jupyterlab-ext~=3.0
jupyter server extension enable amazon-q-developer-jupyterlab-ext
```

## Authenticating with AWS Builder ID
<a name="jupyterlab-setup-bid"></a>

In the following procedure, you will set up Builder ID, which you will use to authenticate when you enable Amazon Q.

1. Refresh the browser tab on which you are using JupyterLab.

1. From the Amazon Q panel, choose **Get Started**.

1. From the pop-up window, choose **Copy Code and Proceed**.

1. On the **Get started** page, sign in or sign up for a Builder ID using your email address or Google account. For more information, see [Getting started with a personal account (Builder ID)](getting-started-builderid.md).

   If you already have a Builder ID, skip to the step about the **Authorize request** page.

1. After you receive your email verification code, enter it in the blank field and choose **Verify**.

1. On the next screen, choose and confirm a password, then choose **Create AWS Builder ID**

1. On the next page choose **Allow** to allow Amazon Q to access your data.

Now you should be logged into Amazon Q in JupyterLab with Builder ID.

To begin coding, see [Using shortcut keys](actions-and-shortcuts.md).

![An example of Amazon Q in use with JupyterLab.](http://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/images/qdev-demo-example.png)
