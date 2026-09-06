

# Troubleshooting Amazon Neptune notebook issues
<a name="graph-notebook-troubleshooting"></a>

When working with Neptune notebooks in JupyterLab, you may occasionally run into issues related to browser behavior, JupyterLab itself, or Amazon SageMaker AI integration. The following sections describe the most common problems and how to resolve them.

## Widget state desynchronization
<a name="graph-notebook-troubleshooting-widget-state"></a>

Graph-notebook widgets can sometimes become desynchronized between the JupyterLab UI and the kernel backend. When this happens, you may see widget display errors or an error message like the following:

```
Model class 'OutputModel' from module '@jupyter-widgets/output' is loaded but cannot be instantiated
```

This typically occurs after long idle periods, when switching between notebook tabs, after clearing the browser cache, during unstable network connectivity, or when reopening a notebook that has unsaved widget outputs.

To resolve this, choose **Restart Kernel and Clear All Outputs** from the **Kernel** menu, and then re-run your notebook cells.

## JupyterLab 4.x initial loading screen delay
<a name="graph-notebook-troubleshooting-loading-delay"></a>

When opening a notebook for the first time after JupyterLab starts, you may see a persistent loading screen with the message: `Loading... The loading screen is taking a long time. Would you like to clear the workspace or keep waiting?`

This primarily affects Firefox and only occurs on the first notebook open in a session. You can resolve it by choosing **Clear Workspace**, refreshing the browser page, or simply reopening the notebook.

If you're using Firefox and encounter this repeatedly, try clearing the cookies and site data for your SageMaker AI domain in Firefox's **Privacy & Security** settings, and then refresh the JupyterLab page.

## Graph Explorer access issues
<a name="graph-notebook-troubleshooting-graph-explorer"></a>

After notebook restarts or when using cached credentials, you may have trouble accessing Graph Explorer. This can show up as authentication errors, access denied messages, or Graph Explorer failing to load entirely.

To work around this, try clearing your browser cache and cookies. You can also open JupyterLab or Jupyter Classic first to force a credential refresh, and then open Graph Explorer. If the problem persists, try using an incognito or private browser window.

## General tips
<a name="graph-notebook-troubleshooting-best-practices"></a>

Many notebook issues are browser-related. To minimize problems, consider the following:
+ Regularly clear your browser cache when working with Neptune notebooks.
+ Always use the most recent notebook session rather than reopening stale ones.
+ Use an incognito or private browser window if you encounter persistent issues.
+ Keep your JupyterLab and graph-notebook extensions up to date.