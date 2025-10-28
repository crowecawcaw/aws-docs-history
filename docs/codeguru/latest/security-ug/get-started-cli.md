On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Automate scans with the AWS CLI

The following steps show you how to automate code scanning in the AWS CLI with Amazon CodeGuru Security. The
bash script you download from the console uploads your code resources, creates a scan, and
outputs findings to a file with a single command. For information on manually creating and
configuring code scans with the AWS CLI, see [Create code scans with the AWS CLI and AWS SDKs](create-scans-cli-sdk.md "create-scans-cli-sdk.md").

###### Integrate with the AWS CLI

1. Go to the
   **Integrations** page in the
   [CodeGuru Security
   console](https://console.aws.amazon.com/codeguru/security/integrations "https://console.aws.amazon.com/codeguru/security/integrations").
2. On the AWS CLI panel, choose **Integrate with the AWS CLI**.
3. Follow the instructions on the page. If you haven't already, install the AWS CLI and
   `jq` in order to run the script. See
   [Get
   started with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md")
   and [Download jq](https://jqlang.github.io/jq/download/ "https://jqlang.github.io/jq/download/") for instructions.
4. Download the `run_codeguru_security.sh` file from the console.
5. To automatically upload a code resource and scan it, open a command prompt window and run
   the following command. Replace `scanName` with the name of the scan,
   `uploadFolder` with the name of the folder where your
   code resource is stored, and `region` with the
   AWS Region you want to run scans in.

```
./run_codeguru_security.sh `scanName` `uploadFolder` `region`
```

6. After you've scanned your resource, your findings are written to an output file. You can
   also view findings with the [`GetFindings`](../security-api/API_GetFindings.md "../security-api/API_GetFindings.md") API
   or on the Findings page in the console.

To address findings, update your code based on the suggested remediation and re-run the
command from Step 5 with the same scan name and the name of the folder that contains your
updated code.
