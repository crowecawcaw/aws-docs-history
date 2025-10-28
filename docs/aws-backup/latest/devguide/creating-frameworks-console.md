# Creating frameworks using the AWS Backup

console

After turning on resource tracking, create a framework using the following steps.

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the left navigation pane, choose **Frameworks**.
3. Choose **Create Framework**.
4. For **Framework name**, enter a unique name. The framework name
   must be between 1 and 256 characters, starting with a letter, and consisting of letters
   (a-z, A-Z), numbers (0-9), and underscores (\_).
5. (Optional) Enter a **Framework description**.
6. In **Controls**, your active controls will be displayed. By default, all
   controls eligible for a resource are listed.

To change which controls are active, click **Edit controls**.

    1. The first check box indicates if the control is turned on. To turn off a control,
     uncheck the box.
    2. Under **Choose resources to evaluate**, you can select how
     to choose resources, either by type, by tags, or by a single resource.The list of [AWS Backup Audit Manager controls](controls-and-remediation.md "controls-and-remediation.md") describes the customization options for each

control. 7. (Optional) Tag your framework by choosing **Add new tag**. You can
use tags to search and filter your frameworks or track your costs. 8. Choose **Create framework**.
AWS Backup Audit Manager might take several minutes to create the framework.

If the error `AlreadyExists` occurs, a framework with the same
controls and parameters already exists. To successfully create a new framework, at least
one control or parameter must be different from existing frameworks.
