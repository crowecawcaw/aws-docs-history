# Create, Upload, and Deploy the Application

First, create a WordPress application bundle, and then use the CodeDeploy CTs to create and deploy the application.

1. Download WordPress, extract the files and create a ./scripts directory.

Linux command:

```
wget https://github.com/WordPress/WordPress/archive/master.zip
```

Windows: Paste `https://github.com/WordPress/WordPress/archive/master.zip` into a browser window and download the zip file.

Create a temporary directory in which to assemble the package.

Linux:

```
mkdir /tmp/WordPress
```

Windows: Create a "WordPress" directory, you will use the directory path later. 2. Extract the WordPress source to the "WordPress" directory and create a ./scripts directory.

Linux:

```
unzip master.zip -d /tmp/WordPress_Temp
cp -paf /tmp/WordPress_Temp/WordPress-master/* /tmp/WordPress
rm -rf /tmp/WordPress_Temp
rm -f master
cd /tmp/WordPress
mkdir scripts
```

Windows: Go to the "WordPress" directory that you created and create a "scripts" directory there.

If you are in a Windows environment, be sure to set the break type for the script files to Unix (LF). In Notepad ++, this is an option at the bottom
right of the window. 3. Create the CodeDeploy **appspec.yml** file, in the WordPress directory (if
copying the example, check the indentation, each space counts). IMPORTANT: Ensure that
the "source" path is correct for copying the WordPress files (in this case, in your
WordPress directory) to the expected destination (/var/www/html/WordPress). In the
example, the appspec.yml file is in the directory with the WordPress files, so only "/"
is needed. Also, even if you used a RHEL AMI for your Auto Scaling group, leave the "os:
linux" line as-is. Example appspec.yml file:

```
version: 0.0
os: linux
files:
  - source: /
    destination: /var/www/html/WordPress
hooks:
  BeforeInstall:
    - location: scripts/install_dependencies.sh
      timeout: 300
      runas: root
  AfterInstall:
    - location: scripts/config_wordpress.sh
      timeout: 300
      runas: root
  ApplicationStart:
    - location: scripts/start_server.sh
      timeout: 300
      runas: root
  ApplicationStop:
    - location: scripts/stop_server.sh
      timeout: 300
      runas: root
```

4. Create bash file scripts in the WordPress ./scripts directory.

First, create `config_wordpress.sh` with the following content (if you prefer, you can edit the wp-config.php file directly).

###### Note

Replace `DBName` with the value given in the HA Stack RFC (for example, `wordpress`).

Replace `DB_MasterUsername` with the `MasterUsername` value given in the HA Stack RFC (for example, `admin`).

Replace `DB_MasterUserPassword` with the `MasterUserPassword` value given in the HA Stack RFC (for example, `p4ssw0rd`).

Replace `DB_ENDPOINT` with the endpoint DNS name in the execution outputs of the HA Stack RFC (for example,
`srt1cz23n45sfg.clgvd67uvydk.us-east-1.rds.amazonaws.com`). You can find this with the [GetRfc](../ApiReference-cm/API_GetRfc.md "../ApiReference-cm/API_GetRfc.md") operation (CLI: get-rfc --rfc-id RFC_ID) or in the AMS
Console RFC details page for the HA Stack RFC that you previously submitted.

```
#!/bin/bash
chmod -R 755 /var/www/html/WordPress
cp /var/www/html/WordPress/wp-config-sample.php /var/www/html/WordPress/wp-config.php
cd /var/www/html/WordPress
sed -i "s/database_name_here/`DBName`/g" wp-config.php
sed -i "s/username_here/`DB_MasterUsername`/g" wp-config.php
sed -i "s/password_here/`DB_MasterUserPassword`/g" wp-config.php
sed -i "s/localhost/`DB_ENDPOINT`/g" wp-config.php
```

5. In the same directory create `install_dependencies.sh` with the following content:

```
#!/bin/bash
yum install -y php
yum install -y php-mysql
yum install -y mysql
service httpd restart
```

###### Note

HTTPS is installed as part of the user data at launch in order to allow health checks to work from the start. 6. In the same directory create `start_server.sh` with the following content:

    * For Amazon Linux instances, use this:



    ```
    #!/bin/bash
    service httpd start
    ```
    * For RHEL instances, use this (the extra commands are policies that allow SELINUX to accept WordPress):



    ```
    #!/bin/bash
    setsebool -P  httpd_can_network_connect_db 1
    setsebool -P  httpd_can_network_connect 1
    chcon -t httpd_sys_rw_content_t /var/www/html/WordPress/wp-content -R
    restorecon -Rv /var/www/html
    service httpd start
    ```

7. In the same directory create `stop_server.sh` with the following content:

```
#!/bin/bash
service httpd stop
```

8. Create the zip bundle.

Linux:

```
$ cd /tmp/WordPress
$ zip -r wordpress.zip .
```

Windows: Go to your "WordPress" directory and select all of the files and create a zip file, be sure to name it wordpress.zip.

1. Upload the application bundle to the S3 bucket.

The bundle needs to be in place in order to continue deploying the stack.

You automatically have access to any S3 bucket instance that you create. You can access it through your bastions, or through the S3 console, and upload the WordPress bundle
with drag-and-drop or browsing to and selecting the zip file.

You can also use the following command in a shell window; be sure that you have the correct path to the zip file:

```
aws s3 cp wordpress.zip s3://BUCKET_NAME/
```

2. Deploy the WordPress application bundle.

Gathering the following data before you begin will make the deployment go more quickly.

REQUIRED DATA:

    * `VPC-ID`: This value determines where your S3 Bucket will be. Use the same VPC ID that you used previously.
    * `CodeDeployApplicationName` and `CodeDeployApplicationName`: The `ApplicationName` value you used in the
     HA 2-Tier Stack RFC set the CodeDeployApplicationName and the CodeDeployDeploymentGroupName. The example uses "WordPress" but you may have used
     a different value.
    * `S3Location`: For `S3Bucket`, use the `BucketName` that you previously created.
     The `S3BundleType` and `S3Key` are from the bundle that you put on your S3 store.
    1. Output the execution parameters JSON schema for the CodeDeploy application deploy CT to a JSON file named DeployCDAppParams.json.



    ```
    aws amscm get-change-type-version --change-type-id "ct-2edc3sd1sqmrb" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeployCDAppParams.json
    ```
    2. Modify the schema as follows and save it as, you can delete and replace the contents.



    ```
    {
    "Description":                       "DeployWPCDApp",
    "VpcId":                             "`VPC_ID`",
    "Name":                              "WordPressCDAppDeploy",
    "TimeoutInMinutes":                  60,
    "Parameters":   {
        "CodeDeployApplicationName":                "`WordPress`",
        "CodeDeployDeploymentGroupName":            "`WordPress`",
        "CodeDeployIgnoreApplicationStopFailures":   false,
        "CodeDeployRevision": {
          "RevisionType": "S3",
          "S3Location": {
            "S3Bucket":     "`BUCKET_NAME`",
            "S3BundleType": "zip",
            "S3Key":        "wordpress.zip" }
            }
        }
    }
    ```
    3. Output the JSON template for CreateRfc to a file, in your current folder, named DeployCDAppRfc.json:



    ```
    aws amscm create-rfc --generate-cli-skeleton > DeployCDAppRfc.json
    ```
    4. Modify and save the DeployCDAppRfc.json file, you can delete and replace the contents. Note that
     `RequestedStartTime` and `RequestedEndTime` are now optional; excluding them creates an ASAP RFC
     that executes as soon as it is approved (which usually happens automatically). To submit a scheduled RFC, add those values.



    ```
    {
    "ChangeTypeVersion":    "1.0",
    "ChangeTypeId":         "ct-2edc3sd1sqmrb",
    "Title":                "CD-Deploy-For-WP-RFC"
    }
    ```
    5. Create the RFC, specifying the DeployCDAppRfc file and the DeployCDAppParams execution parameters file:



    ```
    aws amscm create-rfc --cli-input-json file://DeployCDAppRfc.json  --execution-parameters file://DeployCDAppParams.json
    ```

    You receive the RfcId of the new RFC in the response. Save the ID for subsequent steps.
    6. Submit the RFC:



    ```
    aws amscm submit-rfc --rfc-id `RFC_ID`
    ```

    If the RFC succeeds, you receive no output.
    7. To check RFC status, run



    ```
    aws amscm get-rfc --rfc-id `RFC_ID`
    ```
