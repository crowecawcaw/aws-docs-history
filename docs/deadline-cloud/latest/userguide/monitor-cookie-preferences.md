

# Manage cookie preferences in the Deadline Cloud monitor
<a name="monitor-cookie-preferences"></a>

The AWS Deadline Cloud monitor uses browser storage to save your UI preferences, such as table column layouts, your active farm selection, dashboard layouts, and your download location. You can control whether the monitor stores these preferences by managing your cookie preferences.

If you are in the European Union, a consent banner prompts you to choose your preferences the first time you open the monitor. In other locations, all cookie categories are active by default and no banner appears. You can review and change your choices at any time using the following steps.

**Topics**
+ [Cookie categories](#monitor-cookie-preferences-categories)
+ [Withdrawing functional cookie consent](#monitor-cookie-preferences-withdrawing-consent)

**To change your cookie preferences**

1. Open the Deadline Cloud monitor. For more information, see [Open the Deadline Cloud monitor](open-deadline-cloud-monitor.md).

1. In the left navigation, choose **Cookie preferences**.

   If the navigation is collapsed, choose **Menu**, then choose **Cookie preferences**.

1. In the dialog, select the categories of cookies that you want to allow.

1. Choose **Save preferences**.

**Note**  
The monitor saves your cookie preference for each browser on the web and for each profile in the desktop application. It does not follow your AWS account. If you use a different browser or create a new desktop profile, you must set your preferences again. Cookie preferences expire after one year, at which point the monitor prompts you to choose again.

## Cookie categories
<a name="monitor-cookie-preferences-categories"></a>

The cookie preferences dialog shows the following categories:

Essential  
Essential cookies are required for the monitor to function, including authentication and session management. You cannot turn off essential cookies.

Functional  
With functional cookies, the monitor remembers your UI preferences between sessions, such as your table column layouts, active farm selection, and dashboard arrangements.

Performance  
Performance cookies collect anonymous statistics about how you navigate the site. The monitor does not use performance cookies at this time.

Advertising  
Advertising cookies help deliver relevant marketing content. The monitor does not use advertising cookies at this time.

## Withdrawing functional cookie consent
<a name="monitor-cookie-preferences-withdrawing-consent"></a>

**Important**  
If you decline or withdraw consent for functional cookies, the monitor deletes your saved preferences. The next time you open or refresh the monitor, it uses the default settings. Affected settings include table column layouts, your active farm selection, job monitor board layout, your download location, and unsaved job submission content.

The monitor deletes preferences because it cannot retain UI settings in your browser without functional cookie consent. If you later re-enable functional cookies, the monitor begins saving your preferences again, but it does not restore your previous settings.