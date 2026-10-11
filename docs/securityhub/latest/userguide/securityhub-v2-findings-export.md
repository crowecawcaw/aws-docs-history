

# Exporting findings from Security Hub to Amazon S3
<a name="securityhub-v2-findings-export"></a>

 You can export findings from AWS Security Hub to an Amazon Simple Storage Service (Amazon S3) bucket that you own. An export captures the findings that match the filters on the page you start it from and writes them to your bucket as a CSV file or as JSON in the Open Cybersecurity Schema Framework (OCSF) format. Use exports to share findings with teams that do not use the Security Hub console, load findings into a data warehouse or business intelligence tool, or keep a point in time record for audits. 

 Exports are on demand. You start an export, Security Hub runs it in the background, and the files appear in your bucket when it finishes. You can track every export from the **Exports** page in the Security Hub console. 

## How findings export works
<a name="findings-export-how-it-works"></a>

 You start an export from one of the findings pages in the Security Hub console: **All findings**, **Exposure**, **Threats**, **Vulnerabilities**, **Sensitive data**, or **Posture management**. The export uses the page as its scope and carries over the filters you applied on that page. For example, if you filter the **Vulnerabilities** page to critical findings with the status `New`, the export contains only those findings. 

 Security Hub writes the export to the Amazon S3 bucket and prefix you choose and encrypts every object with the AWS Key Management Service (AWS KMS) key you choose. 

**Note**  
 Only one export can run at a time in an account. To start another export, wait for the running export to finish or cancel it from the **Exports** page. 

## Prerequisites
<a name="findings-export-prerequisites"></a>

 Before you create an export, you need an Amazon S3 bucket, an AWS KMS key, policies on both that allow Security Hub to write to them, and IAM permissions for the identity that creates the export. 

## Creating an export
<a name="findings-export-create"></a>

**To create an export**

1.  Open the Security Hub console and choose the findings page you want to export from: **All findings**, **Exposure**, **Threats**, **Vulnerabilities**, **Sensitive data**, or **Posture management**. 

1. Apply the filters you want the export to use.

1. Choose **Export**. The **Create export** page opens.

1.  Under **Scope**, review the scope. It reads **All findings, using the filters carried over from the Vulnerabilities page** (or the name of the page you came from). To change the scope or filters, return to the findings page and adjust them there. 

    Filters are applied to OCSF fields. If a filter on the source page does not apply to findings, the console shows a warning that names the filters it did not carry over. 

1. Under **Export settings**, do the following:
   +  **Export name** – Enter a name so you can find the export later on the exports list. The console suggests a name made from the source page and the current time, for example `vulnerabilities-202610081601`. 
   +  **Export format** – Choose **CSV** or **JSON (OCSF)**. 
   +  **CSV columns** (CSV only) – Each option shows the column name and the OCSF field path it comes from, for example **Finding account** (`cloud.account.uid`). Fields are grouped by OCSF object, such as Finding info, Cloud, Resources, Compliance, Vulnerabilities, and Evidences. The default set contains nine columns: Finding title, Severity, Resource ID, Created at, Status, Finding account, Finding region, Product vendor name, and Finding type. 

      JSON (OCSF) exports always contain the complete finding, so there is no column selection. 

1. Under **Export location**, select your Amazon S3 bucket and add your AWS KMS key for encryption.

1. Choose **Create export**.

 If an export is already running in your account, the console shows the **Export in progress** dialog. You can wait for that export to finish, or choose **Cancel export and create new** to cancel it and start this one. 