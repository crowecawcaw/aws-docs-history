# Using the Amazon Inspector Jenkins plugin

The Jenkins plugin leverages the [Amazon Inspector SBOM Generator](sbom-generator.md#sbomgen-supported "sbom-generator.md#sbomgen-supported") binary and Amazon Inspector Scan API to produce detailed reports at the end of your build, so you can investigate and remediate risk before deployment.
With the Amazon Inspector Jenkins plugin, you can add Amazon Inspector vulnerability scans to your Jenkins pipeline.
Amazon Inspector vulnerability scans can be configured to pass or fail pipeline executions based on the number and severity of vulnerabilities detected.
You can view the latest version of the Jenkins plugin in the Jenkins marketplace at [https://plugins.jenkins.io/amazon-inspector-image-scanner/](https://plugins.jenkins.io/amazon-inspector-image-scanner/ "https://plugins.jenkins.io/amazon-inspector-image-scanner/").
The following steps describe how to set up the Amazon Inspector Jenkins plugin.

###### Important

Before completing the following steps, you must upgrade Jenkins to version 2.387.3 or higher for the plugin to run.

## Step 1. Set up an AWS account

Configure an AWS account with an IAM role that allows access to the Amazon Inspector Scan API.
For instructions, see [Setting up an AWS account to use the Amazon Inspector CI/CD integration](configure-cicd-account.md "configure-cicd-account.md").

## Step 2. Install the Amazon Inspector Jenkins Plugin

The following procedure describes how to install the Amazon Inspector Jenkins plugin from the Jenkins dashboard.

1. From the Jenkins dashboard, choose **Manage Jenkins**, and then choose **Manage Plugins**.
2. Choose **Available**.
3. From the **Available** tab, search for **Amazon Inspector Scans**, and then install the plugin.

## (Optional) Step 3. Add docker credentials to Jenkins

###### Note

Only add docker credentials if the docker image is in a private repository. Otherwise, skip this step.

The following procedure describes how to add docker credentials to Jenkins from the Jenkins dashboard.

1. From the Jenkins dashboard, choose **Manage Jenkins**, **Credentials**, and then **System**.
2. Choose **Global credentials** and then **Add credentials**.
3. For **Kind**, select **Username with password**.
4. For **Scope**, select **Global (Jenkins, nodes, items, all child items, etc)**.
5. Enter your details, and then choose **OK**.

## (Optional) Step 4. Add AWS credentials

###### Note

Only add AWS credentials if you want to authenticate based on an IAM user.
Otherwise, skip this step.

The following procedure describes how to add AWS credentials from the Jenkins dashboard.

1. From the Jenkins dashboard, choose **Manage Jenkins**, **Credentials**, and then **System**.
2. Choose **Global credentials** and then **Add credentials**.
3. For **Kind**, select **AWS Credentials**.
4. Enter your details, including your **Access Key ID** and **Secret Access Key**, and then choose **OK**.

## Step 5. Add CSS support in a Jenkins script

The following procedure describes how to add CSS support in a Jenkins script.

1. Restart Jenkins.
2. From the Dashboard, choose **Manage Jenkins**, **Nodes**, **Built-In Node**, and then **Script Console**.
3. In the text box, add the line `System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")`, and then choose **Run**.

## Step 6. Add Amazon Inspector Scan to your build

You can add Amazon Inspector Scan to your build by adding a build step in your project or by using the Jenkins declarative pipeline.

### Amazon Inspector Scan to your build by adding a build step in your project

1. On the configuration page, scroll down to **Build Steps**, and choose **Add build step**.
   Then select **Amazon Inspector Scan**.
2. Choose between two inspector-sbomgen installation methods: **Automatic** or **Manual**.
   The automatic option allows the plugin to download the most recent version.
   It also makes sure you always have the latest features, security updates, and bug fixes.
   1. (Option 1) Choose **Automatic** to download the latest version of inspector-sbomgen.
      This option automatically detects the operating system and CPU architecture that's currently in use.
   2. (Option 2) Choose **Manual** if you want to set up the Amazon Inspector SBOM Generator binary for scanning.
      If you choose this method, make sure to provide the full path to a previously downloaded version of inspector-sbomgen.
      For more information, see [Installing Amazon Inspector SBOM Generator (Sbomgen)](sbom-generator.md#install-sbomgen "sbom-generator.md#install-sbomgen") in [Amazon Inspector SBOM Generator](sbom-generator.md "sbom-generator.md").

3. Complete the following to finish configuring the Amazon Inspector Scan build step:
   1. Input your **Image Id**.
      The image can be local, remote, or archived.
      Image names should follow the Docker naming convention.
      If analyzing an exported image, provide the path to the expected tar file.
      See the following example Image Id paths:
      1. For local or remote containers: `NAME[:TAG|@DIGEST]`
      2. For a tar file: `/path/to/image.tar`

   2. Select an **AWS Region** to send the scan request through.
   3. (Optional) For **Report Artifact Name**, enter a custom name for the artifacts generated during the build process.
      This helps uniquely identify and manage them.
   4. (Optional) For **Skip files**, specify one or more directories you want to exclude from scanning.
      Consider this option for directories that do not need to be scanned due to size.
   5. (Optional) For **Docker credentials**, select your Docker username. Do this only if your container image is in a private repository.
   6. (Optional) You can provide the following supported AWS authentication methods:
      1. (Optional) For **IAM role**, provide a role ARN (arn:aws:iam::`AccountNumber`:role/`RoleName`).
      2. (Optional) For **AWS credentials**, specify AWS credentials to authenticate based on an IAM user.
      3. (Optional) For **AWS profile name**, provide the name of a profile to authenticate using a profile name.

   7. (Optional) Select **Enable vulnerability thresholds**.
      With this option, you can determine whether your build fails if a scanned vulnerability exceeds a value.
      If all values equal `0`, the build succeeds, regardless of how many vulnerabilities are scanned.
      For the EPSS score, the value can be from 0 to 1.
      If a scanned vulnerability exceeds a value, the build fails, and all CVEs with an EPSS score above the value show in the console.

4. Choose **Save**.

### Add Amazon Inspector Scan to your build using the Jenkins declarative pipeline

You can add Amazon Inspector Scan to your build using the Jenkins declarative pipeline automatically or manually.

###### To automatically download the SBOMGen declarative pipeline

- To add Amazon Inspector Scan to a build, use the following example syntax.

Replace `IMAGE_PATH` with the path to your image (such as `alpine:latest`), `IAM_ROLE` with the ARN of the IAM role you configured in step 1, and `ID` with your Docker credential ID if you are using a private repository.
You can optionally enable vulnerability thresholds and specify values for each severity.

```
pipeline {
    agent any
    stages {
        stage('amazon-inspector-image-scanner') {
            steps {
                script {
                step([
                $class: 'com.amazon.inspector.jenkins.amazoninspectorbuildstep.AmazonInspectorBuilder',
                archivePath: 'IMAGE_PATH', // Path to your container image or tar file
                awsRegion: 'REGION', // AWS region for scan requests
                iamRole: 'IAM ROLE', // IAM role ARN for authentication
                credentialId: 'Id', // Docker credentials (empty if public repo)
                awsCredentialId: 'AWS ID', // AWS credential ID for authentication
                awsProfileName: 'Profile Name', // AWS profile name to use
                sbomgenSkipFiles: '*.log,node_modules,/tmp/*', // Files/directories to exclude from scanning

                // Vulnerability threshold settings (updated parameter names)
                isSeverityThresholdEnabled: false, // Enable/disable build failure on vulnerability count
                countCritical: 0, // Max critical vulnerabilities before build fails
                countHigh: 0, // Max high vulnerabilities before build fails
                countMedium: 5, // Max medium vulnerabilities before build fails
                countLow: 10, // Max low vulnerabilities before build fails

                // EPSS (Exploit Prediction Scoring System) settings
                isEpssThresholdEnabled: false, // Enable/disable EPSS-based failure threshold
                epssThreshold: 0.7, // EPSS score threshold (0.0 to 1.0)

                // NEW FEATURE: CVE Suppression - ignore specific false positives
                isSuppressedCveEnabled: false, // Enable CVE suppression feature
                suppressedCveList: '', // Comma-separated list of CVEs to ignore in thresholds

                // NEW FEATURE: Auto-Fail CVEs - always fail on critical security issues
                isAutoFailCveEnabled: false, // Enable auto-fail CVE feature
                autoFailCveList: '' // Comma-separated list of CVEs that always fail build
                ])
            }
        }
    }
}
```

######

To manually download the SBOMGen declarative pipeline

- To add Amazon Inspector Scan to a build, use the following example syntax.
  Replace `SBOMGEN_PATH` with the path to the Amazon Inspector SBOM Generator you installed in step 3, `IMAGE_PATH` with the path to your image (such as `alpine:latest`), `IAM_ROLE` with the ARN of the IAM role you configured in step 1, and `ID` with your Docker credential ID if you are using a private repository.
  You can optionally enable vulnerability thresholds and specify values for each severity.

###### Note

Place Sbomgen in the Jenkins directory, and provide the path to the Jenkins directory in the plugin (such as `/opt/folder/arm64/inspector-sbomgen`).

```
pipeline {
    agent any
    stages {
        stage('amazon-inspector-image-scanner') {
            steps {
                script {
                step([
                $class: 'com.amazon.inspector.jenkins.amazoninspectorbuildstep.AmazonInspectorBuilder',
                archivePath: 'IMAGE_PATH', // Path to your container image or tar file
                awsRegion: 'REGION', // AWS region for scan requests
                iamRole: 'IAM ROLE', // IAM role ARN for authentication
                credentialId: 'Id', // Docker credentials (empty if public repo)
                awsCredentialId: 'AWS ID', // AWS credential ID for authentication
                awsProfileName: 'Profile Name', // AWS profile name to use
                sbomgenSkipFiles: '*.log,node_modules,/tmp/*', // Files/directories to exclude from scanning

                // Vulnerability threshold settings (updated parameter names)
                isSeverityThresholdEnabled: false, // Enable/disable build failure on vulnerability count
                countCritical: 0, // Max critical vulnerabilities before build fails
                countHigh: 0, // Max high vulnerabilities before build fails
                countMedium: 5, // Max medium vulnerabilities before build fails
                countLow: 10, // Max low vulnerabilities before build fails

                // EPSS (Exploit Prediction Scoring System) settings
                isEpssThresholdEnabled: false, // Enable/disable EPSS-based failure threshold
                epssThreshold: 0.7, // EPSS score threshold (0.0 to 1.0)

                // NEW FEATURE: CVE Suppression - ignore specific false positives
                isSuppressedCveEnabled: false, // Enable CVE suppression feature
                suppressedCveList: '', // Comma-separated list of CVEs to ignore in thresholds

                // NEW FEATURE: Auto-Fail CVEs - always fail on critical security issues
                isAutoFailCveEnabled: false, // Enable auto-fail CVE feature
                autoFailCveList: '' // Comma-separated list of CVEs that always fail build
                ])
            }
        }
    }
}
```

The plugin includes features for managing security vulnerabilities.

###### Suppressed CVE List

Scans can occasionally detect vulnerabilities that aren't actual threats.
To prevent these false positives from stopping your build, you can add them to a _suppressed_ list.

```
isSuppressedCveEnabled: true,
suppressedCveList: 'CVE-2023-1234,CVE-2023-5678'

```

This ignores specific CVEs when checking if your build should fail.
You should only add false positives to the suppressed list if you addressed them.
After you add these vulnerabilities to the suppressed list, the CVEs still appear in your security report, but they won't cause build failures.

###### Auto-Fail CVE List

For critical security vulnerabilities, you can create a list that always causes your build to fail.

```
isAutoFailCveEnabled: true,
autoFailCveList: 'CVE-2024-9999'

```

This always causes your builds to fail, no matter which settings you enabled.
You should only create this list for high-priority security issues that should never be deployed.
The list overrides all other threshold settings for maximum security.

## Step 7. View your Amazon Inspector vulnerability report

1. Complete a new build of your project.
2. After the build completes, select an output format from the results.
   If you select HTML, you have the option to download a JSON SBOM or CSV version of the report.
   The following shows an example of an HTML report:

![Sample of an Amazon Inspector vulnerability report.](images/report.png)

###### Note

You can use older scripts, as the plugin supports old parameter names.
However, you will encounter warnings in the console suggesting you update these parameters to newer ones.
For example, if you use `isThresholdEnabled`, you will encounter a warning suggesting you update the parameter to `isSeverityThresholdEnabled`.

## Troubleshooting

The following are common errors you can encounter when using the Amazon Inspector Scan plugin for Jenkins.

### Failed to load credentials or sts exception error

###### Error:

`InstanceProfileCredentialsProvider(): Failed to load credentials or sts exception.`

###### Resoultion

Get `aws_access_key_id` and `aws_secret_access_key` for your AWS account.
Set up `aws_access_key_id` and `aws_secret_access_key` in `~/.aws/credentials`.

### Failed to load image from tarball, local, or remote sources

###### Error:

`2024/10/16 02:25:17 [ImageDownloadFailed]: failed to load image from tarball, local, or remote sources.`

###### Note

This error can occur if the Jenkins plugin cannot read the container image, the container image isn't found in the Docker engine, and the container image isn't found in the remote container registry.

###### Resolution:

Verify the following;

- The Jenkins plugin user has read permissions to the image you wish to scan.
- The image you wish to scan is present in Docker engine.
- Your remote image URL is correct.
- You are authenticated to the remote registry (if applicable).

### Inspector-sbomgen path error

###### Error:

`Exception:com.amazon.inspector.jenkins.amazoninspectorbuildstep.exception.SbomgenNotFoundException: There was an issue running inspector-sbomgen, is /opt/inspector/inspector-sbomgen the correct path?`

###### Resolution:

Complete the following procedure to resolve the issue.

1. Place correct OS architecture Inspector-sbomgen in Jenkins directory
   For more information, see [Amazon Inspector SBOM Generator](sbom-generator.md "sbom-generator.md").
2. Grant executable permissions to the binary using the following command: `chmod +x inspector-sbomgen`.
3. Provide correct Jenkins machine path in plugin, such as `/opt/folder/arm64/inspector-sbomgen`.
4. Save config, and execute Jenkins job.
