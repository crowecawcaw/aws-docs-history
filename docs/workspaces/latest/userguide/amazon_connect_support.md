

# Connect Customer audio optimization for WorkSpaces
<a name="amazon_connect_support"></a>

Amazon WorkSpaces allows you to add Connect Customer Contact Control Panel (CCP) to your WorkSpace so you can use Connect Customer audio optimization.

To use Connect Customer audio optimization with your WorkSpace:
+ You must have a supported WorkSpaces client installed:
  + Windows client version 5.33.0 or later
  + macOS client version 5.31.0 or later
  + Linux client version 2026.0 or later on Ubuntu 22 and Ubuntu 24 (x86\_64)
  + Web client (Chrome and Edge)
+ You must have a web browser installed onto the WorkSpaces client endpoint that's supported by Connect Customer. For the list of supported browsers, see [Browsers supported by Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/browsers.html).
**Note**  
If you do not have a supported web browser, you will be asked to install a supported browser.
+ You must have an existing Connect Customer account.

## Log in to your WorkSpace and Connect Customer Contact Control Panel (CCP)
<a name="ccp-login"></a>

**Log in to your WorkSpace and Connect Customer Contact Control Panel (CCP)**

After your administrator has enabled Connect Customer Contact Control Panel (CCP) audio optimization, log in to your WorkSpace and the CCP.

1. Open the WorkSpaces client and log in to your WorkSpace.

1. A web browser opens locally and displays your CCP login page. Log in to CCP in your WorkSpace to control the call.

1. Log in to your CCP in the local device browser window to enable audio optimization. After you log in, CCP audio optimization is enabled.

1. Switch back to your WorkSpaces window, but keep the local browser window running in the background.
**Warning**  
If you close the local browser window that you used to log in to CCP, you will lose your CCP audio (though your WorkSpaces client will continue running).
If you close your WorkSpaces window, your local browser window will also close, and your CCP audio will stop.

If you accidentally close your local browser CCP window or if it crashes, you can restart it. Go to the menu bar, select **Add-in**, and then select the administrator-given CCP name.

For more information about using Amazon Connect, go to the [Agent training guide](https://docs.aws.amazon.com/connect/latest/adminguide/agent-user-guide.html).