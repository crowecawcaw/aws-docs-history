On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Create code scans in the console

This section explains how to create code scans and re-run code scans on revised files in
the CodeGuru Security console.

## Create a new code scan

The following steps show how to upload your code resources and scan them in the console.

1. Open the Scans page in the CodeGuru Security console at [https://console.aws.amazon.com/codeguru/security/scans/](https://console.aws.amazon.com/codeguru/security/scans/ "https://console.aws.amazon.com/codeguru/security/scans/").
2. Choose **Create new scan**.
3. Choose **Choose file** and upload the code file you want to
   scan.
4. For **Scan name**, enter a unique name for the scan. If you
   don’t enter a name, a name will be generated for you with the name of the file, the date, and
   the time.
5. Choose **Create scan**.
6. Your scan name appears in the **Scans** panel. Under
   **Scan status**, it displays **In
   progress** while the scan runs. Once the scan is complete, the status will update to
   **Complete**.

If your scan fails, Scan status says **Failed**. .

## Scan a revised file

The following steps show how to re-run a scan on revised code files. Be sure to
select the appropriate scan name and to upload the corrected version of the
code you previously scanned to make sure that vulnerabilities are properly tracked across
scans.

1. Choose the scan you want to rerun on the Scans page in the CodeGuru Security console.
2. Choose **Scan revised file** on the top right of the page.
3. Choose **Choose file** and upload the code file you want to
   scan. Upload the revised version of the file you previously scanned to make sure that
   vulnerabilities are properly tracked across scans.

You can’t edit the scan name when re-running a scan, since the scan name is used to track
findings across revisions to a file. 4. Choose **Create scan**. 5. After the scan is complete, select the scan name to view updated scan metrics based on
your revised file.
