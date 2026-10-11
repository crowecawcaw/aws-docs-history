

# Using the Amazon Inspector Jenkins plugin
<a name="cicd-jenkins"></a>

 The Amazon Inspector Jenkins plugin adds Amazon Inspector vulnerability scans to your Jenkins builds. The plugin runs the [Amazon Inspector SBOM Generator](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator.html#sbomgen-supported) to create a software bill of materials (SBOM) for a container image. It sends the SBOM to the Amazon Inspector Scan API and produces detailed reports at the end of your build, so you can investigate and remediate risk before deployment. You can fail the build based on the number and severity of vulnerabilities, Exploit Prediction Scoring System (EPSS) scores, specific common vulnerabilities and exposures (CVEs), or malicious packages. For the latest version of the plugin, see [Amazon Inspector Scanner](https://plugins.jenkins.io/amazon-inspector-image-scanner/) on the Jenkins plugins website. The following steps describe how to set up the Amazon Inspector Jenkins plugin. 

**Important**  
 The plugin requires Jenkins 2.541.3 or later. The Amazon Inspector SBOM Generator is available only for Linux, so run your builds on Linux with an x86\_64 (amd64) or arm64 CPU. With the **Automatic** installation method, the Jenkins controller must also run Linux. 

## Step 1. Set up an AWS account
<a name="cicd-jenkins-enable"></a>

 Configure an AWS account with an IAM role that allows access to the Amazon Inspector Scan API. For instructions, see [Setting up an AWS account to use the Amazon Inspector CI/CD integration](configure-cicd-account.md). 

## Step 2. Install the Amazon Inspector Jenkins plugin
<a name="cicd-jenkins-install-jenkins-plugin"></a>

 The following procedure describes how to install the Amazon Inspector Jenkins plugin from the Jenkins dashboard. 

1.  From the Jenkins dashboard, choose **Manage Jenkins**, and then choose **Plugins**. 

1.  Choose **Available plugins**. 

1.  Search for **Amazon Inspector Scanner**, select it, and then choose **Install**. 

## (Optional) Step 3. Add Docker credentials to Jenkins
<a name="cicd-jenkins-add-jenkins"></a>

**Note**  
 Only add Docker credentials if the image is in a private repository. Otherwise, skip this step. 

 The following procedure describes how to add Docker credentials to Jenkins from the Jenkins dashboard. 

1.  From the Jenkins dashboard, choose **Manage Jenkins**, **Credentials**, and then **System**. 

1.  Choose **Global**, and then choose **Add Credentials**. 

1.  Select **Username with password**, and then choose **Next**. 

1.  For **Scope**, select **Global (Jenkins, nodes, items, all child items, etc)**. 

1.  Enter the user name and password for your registry, and then choose **Create**. If your registry supports access tokens, we recommend that you use a read-only token as the password instead of your account password. 

## (Optional) Step 4. Add AWS credentials to Jenkins
<a name="cicd-jenkins-add-aws-credentials"></a>

 The plugin calls the Amazon Inspector Scan API from the Jenkins controller. When you configure the build step in [Step 6](#cicd-jenkins-add-inspector-scan), you choose one of the following ways for the plugin to authenticate: 
+  **(Recommended) IAM role** – The plugin assumes the role that you created in [Step 1](#cicd-jenkins-enable). To assume the role, the plugin uses the credentials that the Jenkins controller already has, such as an Amazon EC2 instance profile. Those credentials need permission to call `sts:AssumeRole` on the role. The plugin can also assume the role with an OpenID Connect (OIDC) ID token that Jenkins issues. OIDC doesn't require you to store long-term AWS credentials in Jenkins. 
+  **AWS credentials** – An access key for an IAM user, stored in Jenkins. 
+  **AWS profile name** – A named profile in the AWS configuration files of the user that runs the Jenkins controller. 

 If you don't configure any of these, the plugin uses the default credential provider chain on the Jenkins controller, such as environment variables or an Amazon EC2 instance profile. Any job that uses the build step can use those credentials, so give them only the permissions of the role that you created in [Step 1](#cicd-jenkins-enable). You only need to add credentials to Jenkins to use an access key or OIDC. Otherwise, skip this step. 

**Warning**  
This scenario requires IAM users with programmatic access and long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed. Access keys can be updated if necessary. For more information, see [Update access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id-credentials-access-keys-update.html) in the *IAM User Guide*.

**To add an access key**

1.  From the Jenkins dashboard, choose **Manage Jenkins**, **Credentials**, and then **System**. 

1.  Choose **Global**, and then choose **Add Credentials**. 

1.  Select **AWS Credentials**, and then choose **Next**. 

1.  Enter your **Access Key ID** and **Secret Access Key**, and then choose **Create**. 

**To add an OIDC credential**

1.  From the Jenkins dashboard, choose **Manage Jenkins**, **Credentials**, and then **System**. 

1.  Choose **Global**, and then choose **Add Credentials**. 

1.  Select **OpenID Connect id token**, and then choose **Next**. 

1.  For **Audience**, enter `sts.amazonaws.com`, and then choose **Create**. To see the issuer URI of the credential, open it and choose **Update credential**. 

1.  In IAM, create an OIDC identity provider with the issuer URI as the provider URL and `sts.amazonaws.com` as the audience. For more information, see [Create an OpenID Connect (OIDC) identity provider in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html). 

1.  Add a statement to the trust policy of the role that you created in [Step 1](#cicd-jenkins-enable) that allows the provider to call `sts:AssumeRoleWithWebIdentity`. Include a condition on the provider's `aud` key with the value `sts.amazonaws.com`. To allow only specific jobs to assume the role, also add a condition on the `sub` key, which contains the URL of the job by default. The following example statement allows only the job {{my-job}} on a Jenkins controller at {{jenkins.example.com}} to assume the role. 

   ```
   {
       "Effect": "Allow",
       "Principal": {
           "Federated": "arn:aws:iam::{{111122223333}}:oidc-provider/{{jenkins.example.com}}/oidc"
       },
       "Action": "sts:AssumeRoleWithWebIdentity",
       "Condition": {
           "StringEquals": {
               "{{jenkins.example.com}}/oidc:aud": "sts.amazonaws.com",
               "{{jenkins.example.com}}/oidc:sub": "https://{{jenkins.example.com}}/job/{{my-job}}/"
           }
       }
   }
   ```

**Note**  
 AWS must be able to reach the issuer URI over HTTPS, and the URI shouldn't include a port number. If your Jenkins controller isn't reachable from the internet, or its URL includes a port, use a different issuer. For more information, see [Picking an issuer](https://github.com/jenkinsci/oidc-provider-plugin#picking-an-issuer) in the OpenID Connect Provider plugin documentation on the GitHub website. 

## Step 5. Allow Jenkins to display the HTML report
<a name="cicd-jenkins-add-css-support"></a>

 The plugin creates an HTML report that uses inline CSS and JavaScript. By default, Jenkins serves build artifacts with a Content Security Policy (CSP) that blocks both. As a result, the report has no styling and shows zero findings, even when the scan found vulnerabilities. Use one of the following options so that the report displays correctly. 
+  **(Recommended) Serve build artifacts from another domain** – Choose **Manage Jenkins** and then **System**. Under **Serve resource files from another domain**, enter a **Resource Root URL** that points to your Jenkins controller with a different host name than your Jenkins URL. Jenkins doesn't apply the CSP to files that it serves from this URL. For more information, see [Resource Root URL](https://www.jenkins.io/doc/book/security/user-content/#resource-root-url) in the Jenkins documentation. 
+  **Remove the CSP** – Set the `hudson.model.DirectoryBrowserSupport.CSP` system property to an empty value. To apply the change immediately, choose **Manage Jenkins** and then **Script Console**, run `System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")`, and then reload the report. Only Jenkins administrators can use the Script Console. This change lasts until Jenkins restarts. To keep it, start Jenkins with the Java option `-Dhudson.model.DirectoryBrowserSupport.CSP=`. 

**Warning**  
 Removing the CSP allows any HTML file in a workspace or build artifact to run scripts in the browsers of your Jenkins users. Only remove it if you trust everyone who can change files in your builds, and all of your build agents. For more information, see [Configuring Content Security Policy](https://www.jenkins.io/doc/book/security/configuring-content-security-policy/) in the Jenkins documentation. 

## Step 6. Add Amazon Inspector Scan to your build
<a name="cicd-jenkins-add-inspector-scan"></a>

 You can add Amazon Inspector Scan as a build step in a freestyle project, or as a step in a Jenkins pipeline. 

### Add Amazon Inspector Scan as a build step
<a name="cicd-jenkins-add-build-step"></a>

1.  On the configuration page of your project, under **Build Steps**, choose **Add build step**, and then choose **Amazon Inspector Scan**. 

1.  For **Inspector-sbomgen Installation Method**, choose one of the following: 
   +  **Automatic** – The plugin downloads the latest version of the Amazon Inspector SBOM Generator at the start of each build. The Jenkins controller must run Linux and be able to reach `amazon-inspector-sbomgen.s3.amazonaws.com` over HTTPS. 
   +  **Manual** – Enter the full path to an `inspector-sbomgen` binary that you downloaded, such as `/opt/inspector/inspector-sbomgen`. Choose this option to use a specific version of the Amazon Inspector SBOM Generator, or if the Jenkins controller can't download it. The plugin checks the path on the Jenkins controller, but runs the binary on the machine that runs the build. If these are different machines, put the binary at the same path on both. For download links, see [Installing Sbomgen](sbom-generator.md#install-sbomgen). 

1.  For **Image ID**, enter the image to scan. The image can be local, remote, or archived, and its name must follow the Docker naming convention: 
   +  For a local or remote image: `NAME[:TAG|@DIGEST]` 
   +  For an image exported to a tar file: `/path/to/image.tar` 

1.  (Optional) For **Report Artifact Name**, enter a prefix for the file name of the SBOM that the build archives. The default is `default-report`. The name can contain up to 255 letters, numbers, periods (.), underscores (\_), and hyphens (-). 

1.  (Optional) For **Skip Files**, enter the files and directories to exclude from the scan, one per line or separated by commas without spaces. Consider this option for large directories that don't need to be scanned. 

1.  (Optional) For **Docker Credentials**, choose the credentials that you added in [Step 3](#cicd-jenkins-add-jenkins). 

1.  For **AWS Region**, choose the Region to send the scan request to. 

1.  Under **AWS Authentication Options (Choose One)**, configure one of the following options. If you leave all of them empty, the plugin uses the default credential provider chain on the Jenkins controller. 
   +  For **IAM Role**, enter the Amazon Resource Name (ARN) of the role that you created in [Step 1](#cicd-jenkins-enable), such as `arn:aws:iam::{{111122223333}}:role/{{InspectorCICDscan-role}}`. To assume the role with OIDC, also choose the credential that you added in [Step 4](#cicd-jenkins-add-aws-credentials) for **OIDC Credentials**. 
   +  For **AWS Credentials**, choose the access key that you added in [Step 4](#cicd-jenkins-add-aws-credentials). 
   +  For **AWS Profile Name**, enter the name of a profile on the Jenkins controller. 

    If you configure more than one option, the plugin uses the first one in this order: **AWS Credentials**, **IAM Role** with **OIDC Credentials**, **IAM Role**, and then **AWS Profile Name**. 

1.  (Optional) Under **Scan Output Filters**, choose the checks that can fail the build. For a description of each option, see [Scan output filters](#cicd-jenkins-scan-output-filters). 

1.  Choose **Save**. 

### Add Amazon Inspector Scan to a Jenkins pipeline
<a name="cicd-jenkins-add-pipeline-step"></a>

 The following declarative pipeline downloads the Amazon Inspector SBOM Generator automatically and authenticates with an IAM role. It fails the build if the scan finds more vulnerabilities than the severity thresholds allow. Replace {{IMAGE\_ID}} with your image, such as `alpine:latest`, and {{REGION}} with your AWS Region, such as `us-east-1`. Replace {{IAM\_ROLE\_ARN}} with the ARN of the role that you created in [Step 1](#cicd-jenkins-enable). 

```
pipeline {
    agent any
    stages {
        stage('Amazon Inspector scan') {
            steps {
                script {
                    step([
                        $class: 'com.amazon.inspector.jenkins.amazoninspectorbuildstep.AmazonInspectorBuilder',
                        sbomgenSelection: 'automatic',
                        archivePath: '{{IMAGE_ID}}',
                        awsRegion: '{{REGION}}',
                        iamRole: '{{IAM_ROLE_ARN}}',
                        credentialId: '',
                        isSeverityThresholdEnabled: true,
                        countCritical: 0,
                        countHigh: 0,
                        countMedium: 5,
                        countLow: 10
                    ])
                }
            }
        }
    }
}
```

 To use an `inspector-sbomgen` binary that you installed, replace `sbomgenSelection: 'automatic'` with the following lines. Replace {{SBOMGEN\_PATH}} with the full path to the binary, such as `/opt/inspector/inspector-sbomgen`. 

```
sbomgenSelection: 'manual',
sbomgenPath: '{{SBOMGEN_PATH}}',
```

 The step accepts the following parameters. Each parameter matches an option of the build step. 


**Amazon Inspector Scan pipeline parameters**  

| **Parameter** | **Description** | 
| --- | --- | 
| archivePath | Required. The image to scan (Image ID). | 
| awsRegion | Required. The AWS Region to send the scan request to. | 
| sbomgenSelection | automatic (default) or manual. Any other value uses automatic. | 
| sbomgenPath | The full path to the inspector-sbomgen binary. Required when sbomgenSelection is manual. | 
| iamRole | The ARN of the IAM role to assume. | 
| oidcCredentialId | The ID of the OIDC credential that the plugin uses to assume iamRole. | 
| awsCredentialId | The ID of the access key credential that you added in [Step 4](#cicd-jenkins-add-aws-credentials). | 
| awsProfileName | The name of a profile on the Jenkins controller. | 
| credentialId | The ID of the Docker credentials for a private repository. Use an empty value ('') for a public image. | 
| reportArtifactName | A prefix for the file name of the SBOM that the build archives. The default is default-report. | 
| sbomgenSkipFiles | The files and directories to exclude from the scan, one per line or separated by commas without spaces. | 
| isSeverityThresholdEnabled, countCritical, countHigh, countMedium, countLow | Severity thresholds. A count that you don't set is 0. | 
| isEpssThresholdEnabled, epssThreshold | EPSS threshold. If you enable it without setting epssThreshold, the plugin skips the check. | 
| isSuppressedCveEnabled, suppressedCveList | CVE suppression list. | 
| isAutoFailCveEnabled, autoFailCveList | CVE auto-fail list. | 
| isMaliciousPackageBlockingEnabled | Malicious package blocking. | 
| isLicenseCollectionEnabled | License collection. | 

 For a description of the threshold and filter parameters, see [Scan output filters](#cicd-jenkins-scan-output-filters). 

**Note**  
 The plugin still accepts the earlier parameter names `isThresholdEnabled` and `isEpssEnabled`, but logs a warning that suggests the current names, `isSeverityThresholdEnabled` and `isEpssThresholdEnabled`. 

### Scan output filters
<a name="cicd-jenkins-scan-output-filters"></a>

 The following options control when the scan fails the build. Each option is off by default. When you turn on more than one, the build fails if any of them fails. The console output of the build shows which options are on and why the build failed. 

**Enable severity thresholds** (`isSeverityThresholdEnabled`)  
 Fails the build if the number of findings of a severity is greater than its threshold. You can set a threshold for **Critical** (`countCritical`), **High** (`countHigh`), **Medium** (`countMedium`), and **Low** (`countLow`). The counts include Dockerfile findings, and each finding counts once, at its highest severity rating. A threshold of `0` fails the build if the scan finds anything of that severity. Findings with other severities don't count toward the thresholds. 

**Enable EPSS threshold** (`isEpssThresholdEnabled`, `epssThreshold`)  
 Fails the build if any vulnerability has an EPSS score greater than or equal to the threshold. Vulnerabilities without an EPSS score don't count. Enter a value from 0 to 1, such as `0.7`. 

**Enable CVE suppression list** (`isSuppressedCveEnabled`, `suppressedCveList`)  
 Excludes the CVEs that you list from the severity thresholds and the EPSS threshold, for example false positives that you reviewed. Suppressed CVEs still appear in the reports. Separate CVE IDs with commas or line breaks, such as `CVE-2023-1234,CVE-2023-5678`. 

**Enable CVE auto-fail list** (`isAutoFailCveEnabled`, `autoFailCveList`)  
 Fails the build if the scan finds any CVE that you list, regardless of your other settings, including the CVE suppression list. Use this list for vulnerabilities that must never be deployed. Separate CVE IDs with commas or line breaks, such as `CVE-2024-9999`. 

**Enable malicious package blocking** (`isMaliciousPackageBlockingEnabled`)  
 Fails the build if Amazon Inspector identifies any malicious packages in the image, regardless of your other settings. If the scan result doesn't include malicious package information, the plugin skips this check with a message in the console output and doesn't fail the build. This option is available in plugin version 649.v0fe6e5596568 and later. For information about how Amazon Inspector identifies malicious packages, see [Amazon Inspector Security Research](security-research.md). 

**Enable license collection** (`isLicenseCollectionEnabled`)  
 Adds package license information to the SBOM that the build archives. This option doesn't fail the build. With the **Manual** installation method, it requires Amazon Inspector SBOM Generator version 1.8.0 or later. For more information, see [Amazon Inspector SBOM Generator license collection](sbom-generator-license-collection.md). 

## Step 7. View your Amazon Inspector vulnerability report
<a name="cicd-jenkin-view-vulnerability-report"></a>

1.  Run a build of your project. 

1.  Open the build. When the scan completes, the console output ends with a security assessment summary and whether the build passed. 

1.  Under **Build Artifacts**, choose `index.html` to open the HTML report. The build also archives the following files: 
   +  The SBOM that the Amazon Inspector SBOM Generator created, in JSON format. 
   +  A CSV file with the vulnerability findings, if the scan found any. 
   +  A CSV file with the Dockerfile findings, if the scan found any. 

    The report shows the scanned image, the number of findings for each severity, and a table that lists each vulnerability with its ID, severity, and affected package. The following image shows an example report. 

![An Amazon Inspector vulnerability report that shows the number of findings by severity and a table of vulnerabilities.](https://docs.aws.amazon.com/inspector/latest/user/images/report.png)


## Troubleshooting
<a name="jenkins-troubleshooting"></a>

 The following are common errors you can encounter when using the Amazon Inspector Jenkins plugin. If the plugin fails, the build fails, and the console output shows `Plugin execution failed.` followed by the error. 

### Unable to load credentials error
<a name="w2aac41c19c21b5"></a>

**Error:**  
 `software.amazon.awssdk.core.exception.SdkClientException: Unable to load credentials from any of the providers in the chain`, followed by the list of credential providers that the plugin tried. If you didn't set an **IAM Role**, the last error can instead be `Profile file contained no credentials for profile 'default'`. 

 Earlier versions of the plugin can show this error as `InstanceProfileCredentialsProvider(): Failed to load credentials or sts exception.` 

**Resolution:**  
 The plugin couldn't get AWS credentials on the Jenkins controller. Configure one of the authentication options in the build step, as described in [Step 4](#cicd-jenkins-add-aws-credentials) and [Step 6](#cicd-jenkins-add-inspector-scan). Alternatively, make credentials available to the controller, for example with an Amazon EC2 instance profile. If the scan request fails, the plugin tries once more without the access key, OIDC token, or profile name. If you set an **IAM Role**, it assumes the role with the controller's own credentials. Otherwise, it uses the `default` profile on the controller. Because of this retry, the first error in the console output usually shows the cause. 

### Failed to load image from tarball, local, or remote sources
<a name="w2aac41c19c21b7"></a>

**Error:**  
 `[ImageDownloadFailed]: failed to load image from tarball, local, or remote sources.` 

 Depending on the cause, the Amazon Inspector SBOM Generator can instead report a more specific error, such as `[ImageDownloadManifestUnknown]` or `[ImageRegistryAccessUnauthorized]`. The console output shows `Exception:com.amazon.inspector.jenkins.amazoninspectorbuildstep.exception.MalformedScanOutputException: Sbom scanning output formatted incorrectly.`, followed by `Sbom Content:` and the Amazon Inspector SBOM Generator error. 

**Resolution:**  
 Verify the following: 
+  The user that runs the build has read permissions to the image you want to scan. 
+  For a local image, the image is present in the Docker engine on the machine that runs the build. 
+  The image name is correct. 
+  For an image in a private repository, the build step uses the Docker credentials from [Step 3](#cicd-jenkins-add-jenkins). 

### Inspector-sbomgen path error
<a name="w2aac41c19c21b9"></a>

**Error:**  
 `Exception:java.lang.IllegalArgumentException: Provided SBOMgen path is invalid or not executable: /opt/inspector/inspector-sbomgen` 

 Earlier versions of the plugin show the following error instead: `Exception:com.amazon.inspector.jenkins.amazoninspectorbuildstep.exception.SbomgenNotFoundException: There was an issue running inspector-sbomgen, is /opt/inspector/inspector-sbomgen the correct path?` 

**Resolution:**  
 Complete the following procedure to resolve the issue. 

1.  Download the Amazon Inspector SBOM Generator for the CPU architecture of the machine that runs the build. For more information, see [Installing Sbomgen](sbom-generator.md#install-sbomgen). 

1.  Make the binary executable by running the following command: `chmod +x inspector-sbomgen`. 

1.  In the build step, enter the full path to the binary, such as `/opt/inspector/inspector-sbomgen`. The plugin checks the path on the Jenkins controller, so if the build runs on an agent, the binary must be at the same path on both. 

1.  Save the configuration, and run the build again. 

 If the error is `Invalid sbomgen path: {{path}}`, the path contains a character that isn't allowed. The path can contain only letters, numbers, spaces, periods (.), underscores (\_), hyphens (-), colons (:), and forward slashes (/). 

### Unsupported OS or unsupported architecture error
<a name="w2aac41c19c21c11"></a>

**Error:**  
 `Exception:java.lang.UnsupportedOperationException: Unsupported OS: mac os x` 

 The error can also be `Exception:java.lang.UnsupportedOperationException: Unsupported architecture: {{architecture}}`. 

**Resolution:**  
 The Amazon Inspector SBOM Generator is available only for Linux with an x86\_64 (amd64) or arm64 CPU. With the **Automatic** installation method, the plugin checks the operating system of the Jenkins controller and the CPU of the machine that runs the build. Run the controller on Linux, and run your build on Linux with a supported CPU. 

### HTML report has no styling or shows zero findings
<a name="w2aac41c19c21c13"></a>

**Error:**  
 The HTML report has no styling and shows zero findings. The top of the report shows `Jenkins may be blocking CSS/JS, visit https://www.jenkins.io/doc/book/security/configuring-content-security-policy/ for a possible fix.` 

**Resolution:**  
 Jenkins is blocking the CSS and JavaScript in the report. To allow the report to display, see [Step 5. Allow Jenkins to display the HTML report](#cicd-jenkins-add-css-support). The CSV files show the findings even when the HTML report doesn't display. 