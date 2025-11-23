# Connect service-managed fleets to a custom license server

You can bring your own license server to use with a Deadline Cloud service-managed fleet. To bring
your own license, you can configure a license server using a queue environment in your farm. To
configure your license server, you should already have a farm and queue set up.

How you connect to a software license server depends on the configuration of your fleet and
the requirements of the software vendor. Typically, you access the server in one of two
ways:

- Directly to the license server. Your workers obtain a license from software vendor's
  license server using the Internet. All of your workers must be able to connect to the
  server.
- Through a license proxy. Your workers connect to a proxy server in your local network.
  Only the proxy server is allowed to connect to the vendor's license server over the
  Internet.
  With the instructions below, you use Amazon EC2 Systems Manager (SSM) to forward ports from a worker
  instance to your license server or proxy instance.

###### Topics

- [Step 1: Configure the queue environment](#configure-queue-environment "#configure-queue-environment")
- [Step 2: (Optional) License proxy instance setup](#license-proxy "#license-proxy")
- [Step 3: CloudFormation template setup](#byol-cfn-template "#byol-cfn-template")

## Step 1: Configure the queue environment

You can configure a queue environment in your queue to access your license server. First,
ensure that you have an AWS instance configured with license server access using one of the
following methods:

- License server – The instance hosts the license servers directly.
- License proxy – The instance has network access to the license server, and
  forwards license server ports to the license server. For details on how to configure a
  license proxy instance, see [Step 2: (Optional) License proxy instance setup](#license-proxy "#license-proxy").

###### To add required permissions to the queue role

1. From the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home"),
   choose **Go to Dashboard**.
2. From the dashboard, select the farm, and then the queue you want to configure.
3. From queue details > service role, select the role.
4. Choose **Add permission**, and then choose **Create inline
   policy**.
5. Select the JSON policy editor, and then copy and paste the following text into the
   editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession"
 ],
 "Resource": [
 "arn:aws:ssm:`us-east-1`::document/AWS-StartPortForwardingSession",
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/`instance_id`"
 ]
 }
 ]
}`

```

6. Before saving the new policy, replace the following values in the policy text:
   - Replace `region` with the AWS Region where your farm is
     located
   - Replace `instance_id` with the instance ID for the license server or
     proxy instance you're using
   - Replace `account_id` with the AWS account number containing your
     farm

7. Choose **Next**.
8. For the Policy name, enter `LicenseForwarding`.
9. Choose **Create policy** to save your changes and create the policy
   with the required permissions.

###### To add a new queue environment to the queue

1. From the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home"),
   choose **Go to Dashboard** if you haven't already.
2. From the dashboard, select the farm, and then the queue you want to configure.
3. Choose **Queue Environments** > **Actions** >
   **Create new with YAML**.
4. Copy and paste the following text into the YAML script editor.

Windows

```
`specificationVersion: "environment-2023-09"
parameterDefinitions:
 - name: LicenseInstanceId
 type: STRING
 description: >
 The Instance ID of the license server/proxy instance
 default: ""
 - name: LicenseInstanceRegion
 type: STRING
 description: >
 The region containing this farm
 default: ""
 - name: LicensePorts
 type: STRING
 description: >
 Comma-separated list of ports to be forwarded to the license server/proxy instance.
 Example: "2700,2701,2702"
 default: ""
environment:
 name: BYOL License Forwarding
 variables:
 example_LICENSE: 2700@localhost
 script:
 actions:
 onEnter:
 command: powershell
 args: [ "{{Env.File.Enter}}"]
 onExit:
 command: powershell
 args: [ "{{Env.File.Exit}}" ]
 embeddedFiles:
 - name: Enter
 filename: enter.ps1
 type: TEXT
 runnable: True
 data: |
 $ZIP_NAME="SessionManagerPlugin.zip"
 Invoke-WebRequest -Uri "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/windows/$ZIP_NAME" -OutFile $ZIP_NAME
 Expand-Archive -Path $ZIP_NAME
 Expand-Archive -Path .\SessionManagerPlugin\package.zip
 conda activate
 python {{Env.File.StartSession}} {{Session.WorkingDirectory}}\package\bin\session-manager-plugin.exe
 - name: Exit
 filename: exit.ps1
 type: TEXT
 runnable: True
 data: |
 Write-Output "Killing SSM Manager Plugin PIDs: $env:BYOL_SSM_PIDS"
 "$env:BYOL_SSM_PIDS".Split(",") | ForEach {
 Write-Output "Killing $_"
 Stop-Process -Id $_ -Force
 }
 - name: StartSession
 type: TEXT
 data: |
 import boto3
 import json
 import subprocess
 import sys

 instance_id = "{{Param.LicenseInstanceId}}"
 region = "{{Param.LicenseInstanceRegion}}"
 license_ports_list = "{{Param.LicensePorts}}".split(",")

 ssm_client = boto3.client("ssm", region_name=region)
 pids = []

 for port in license_ports_list:
 session_response = ssm_client.start_session(
 Target=instance_id,
 DocumentName="AWS-StartPortForwardingSession",
 Parameters={"portNumber": [port], "localPortNumber": [port]}
 )

 cmd = [
 sys.argv[1],
 json.dumps(session_response),
 region,
 "StartSession",
 "",
 json.dumps({"Target": instance_id}),
 f"https://ssm.{region}.amazonaws.com"
 ]

 process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
 pids.append(process.pid)
 print(f"SSM Port Forwarding Session started for port {port}")

 print(f"openjd_env: BYOL_SSM_PIDS={','.join(str(pid) for pid in pids)}")`

```

Linux

```
`specificationVersion: "environment-2023-09"
parameterDefinitions:
 - name: LicenseInstanceId
 type: STRING
 description: >
 The Instance ID of the license server/proxy instance
 default: ""
 - name: LicenseInstanceRegion
 type: STRING
 description: >
 The region containing this farm
 default: ""
 - name: LicensePorts
 type: STRING
 description: >
 Comma-separated list of ports to be forwarded to the license server/proxy instance.
 Example: "2700,2701,2702"
 default: ""
environment:
 name: BYOL License Forwarding
 variables:
 example_LICENSE: 2700@localhost
 script:
 actions:
 onEnter:
 command: bash
 args: [ "{{Env.File.Enter}}"]
 onExit:
 command: bash
 args: [ "{{Env.File.Exit}}" ]
 embeddedFiles:
 - name: Enter
 type: TEXT
 runnable: True
 data: |
 curl https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_64bit/session-manager-plugin.rpm -Ls | rpm2cpio - | cpio -iv --to-stdout ./usr/local/sessionmanagerplugin/bin/session-manager-plugin > {{Session.WorkingDirectory}}/session-manager-plugin
 chmod +x {{Session.WorkingDirectory}}/session-manager-plugin
 conda activate
 python {{Env.File.StartSession}} {{Session.WorkingDirectory}}/session-manager-plugin
 - name: Exit
 type: TEXT
 runnable: True
 data: |
 echo Killing SSM Manager Plugin PIDs: $BYOL_SSM_PIDS
 for pid in ${BYOL_SSM_PIDS//,/ }; do kill $pid; done
 - name: StartSession
 type: TEXT
 data: |
 import boto3
 import json
 import subprocess
 import sys

 instance_id = "{{Param.LicenseInstanceId}}"
 region = "{{Param.LicenseInstanceRegion}}"
 license_ports_list = "{{Param.LicensePorts}}".split(",")

 ssm_client = boto3.client("ssm", region_name=region)
 pids = []

 for port in license_ports_list:
 session_response = ssm_client.start_session(
 Target=instance_id,
 DocumentName="AWS-StartPortForwardingSession",
 Parameters={"portNumber": [port], "localPortNumber": [port]}
 )

 cmd = [
 sys.argv[1],
 json.dumps(session_response),
 region,
 "StartSession",
 "",
 json.dumps({"Target": instance_id}),
 f"https://ssm.{region}.amazonaws.com"
 ]

 process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
 pids.append(process.pid)
 print(f"SSM Port Forwarding Session started for port {port}")

 print(f"openjd_env: BYOL_SSM_PIDS={','.join(str(pid) for pid in pids)}")`

```

5. Before saving the queue environment, make the following changes to the environment
   text as needed:
   - Update the default values for the following parameters to reflect your
     environment:
     - **LicenseInstanceID** – The Amazon EC2 instance ID of your
       license server or proxy instance
     - **LicenseInstanceRegion** – The AWS Region containing
       your farm
     - **LicensePorts** – A comma-separated list of ports to
       be forwarded to the license server or proxy instance (for example
       2700,2701)

   - Add any required licensing environment variables to the variables section. These
     variables should direct the DCCs to localhost on the license server port. For example,
     if your Foundry license server is listening on port 6101, you would add the variable
     as `foundry_LICENSE: 6101@localhost`.

6. (Optional) You can leave **Priority** set to **0**,
   or you can change it to order the priority differently among multiple queue
   environments.
7. Choose **Create queue environment** to save the new
   environment.

With the queue environment set, jobs submitted to this queue will retrieve licenses
from the configured license server.

## Step 2: (Optional) License proxy instance setup

As an alternative to using a license server, you can use a license proxy. To create a
license proxy, create a new Amazon Linux 2023 instance that has network access to the license
server. If needed, you can configure this access using a VPN connection. For more information,
see [VPN
connections](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md") in the _Amazon VPC User Guide_.

To set up a license proxy instance for Deadline Cloud, follow the steps in this procedure.
Perform the following configuration steps on this new instance to enable forwarding of
license traffic to your license server

1. To install the HAProxy package, enter

```
`sudo yum install haproxy`
```

2. Update the listen license-server section of the
   **/etc/haproxy/haproxy.cfg** configuration file with the
   following:
   1. Replace **LicensePort1** and **LicensePort2**
      with the port numbers to be forwarded to the license server. Add or remove
      comma-separated values to accommodate the required number of ports.
   2. Replace **LicenseServerHost** with the host name or IP address of
      the license server.

```
`lobal
 log 127.0.0.1 local2
 chroot /var/lib/haproxy
 user haproxy
 group haproxy
 daemon

defaults
 timeout queue 1m
 timeout connect 10s
 timeout client 1m
 timeout server 1m
 timeout http-keep-alive 10s
 timeout check 10s

listen license-server
 bind *:`LicensePort1`,*:`LicensePort2`
 server license-server `LicenseServerHost``
```

3. To enable and start the HAProxy service, run the following commands:

```
`sudo systemctl enable haproxy`
`sudo service haproxy start`
```

After completing the steps, license requests sent to localhost from the forwarding queue
environment should be forwarded to the specified license server.

## Step 3: CloudFormation template setup

You can use a CloudFormation template to configure an entire farm to use your own
licensing.

1. Modify the template provided in the next step to add any required licensing
   environment variables to the **variables** section under
   **BYOLQueueEnvironment**.
2. Use the following CloudFormation template.

```

AWSTemplateFormatVersion: 2010-09-09
Description: "Create Deadline Cloud resources for BYOL"

Parameters:
  LicenseInstanceId:
    Type: AWS::EC2::Instance::Id
    Description: Instance ID for the license server/proxy instance
  LicensePorts:
    Type: String
    Description: Comma-separated list of ports to forward to the license instance

Resources:
  JobAttachmentBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub byol-example-ja-bucket-${AWS::AccountId}-${AWS::Region}
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: AES256

  Farm:
    Type: AWS::Deadline::Farm
    Properties:
      DisplayName: BYOLFarm

  QueuePolicy:
    Type: AWS::IAM::ManagedPolicy
    Properties:
      ManagedPolicyName: BYOLQueuePolicy
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Action:
              - s3:GetObject
              - s3:PutObject
              - s3:ListBucket
              - s3:GetBucketLocation
            Resource:
              - !Sub ${JobAttachmentBucket.Arn}
              - !Sub ${JobAttachmentBucket.Arn}/job-attachments/*
            Condition:
              StringEquals:
                aws:ResourceAccount: !Sub ${AWS::AccountId}
          - Effect: Allow
            Action: logs:GetLogEvents
            Resource: !Sub arn:aws:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/deadline/${Farm.FarmId}/*
          - Effect: Allow
            Action:
              - s3:ListBucket
              - s3:GetObject
            Resource:
              - "*"
            Condition:
              ArnLike:
                s3:DataAccessPointArn:
                  - arn:aws:s3:*:*:accesspoint/deadline-software-*
              StringEquals:
                s3:AccessPointNetworkOrigin: VPC

  BYOLSSMPolicy:
    Type: AWS::IAM::ManagedPolicy
    Properties:
      ManagedPolicyName: BYOLSSMPolicy
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Action:
              - ssm:StartSession
            Resource:
              - !Sub arn:aws:ssm:${AWS::Region}::document/AWS-StartPortForwardingSession
              - !Sub arn:aws:ec2:${AWS::Region}:${AWS::AccountId}:instance/${LicenseInstanceId}


  WorkerPolicy:
    Type: AWS::IAM::ManagedPolicy
    Properties:
      ManagedPolicyName: BYOLWorkerPolicy
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Action:
              - logs:CreateLogStream
            Resource: !Sub arn:aws:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/deadline/${Farm.FarmId}/*
            Condition:
              ForAnyValue:StringEquals:
                aws:CalledVia:
                  - deadline.amazonaws.com
          - Effect: Allow
            Action:
              - logs:PutLogEvents
              - logs:GetLogEvents
            Resource: !Sub arn:aws:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/deadline/${Farm.FarmId}/*


  QueueRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: BYOLQueueRole
      ManagedPolicyArns:
        - !Ref QueuePolicy
        - !Ref BYOLSSMPolicy
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Action:
              - sts:AssumeRole
            Principal:
              Service:
                - credentials.deadline.amazonaws.com
                - deadline.amazonaws.com
            Condition:
              StringEquals:
                aws:SourceAccount: !Sub ${AWS::AccountId}
              ArnEquals:
                aws:SourceArn: !Ref Farm

  WorkerRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: BYOLWorkerRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AWSDeadlineCloud-FleetWorker
        - !Ref WorkerPolicy
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Action:
              - sts:AssumeRole
            Principal:
              Service: credentials.deadline.amazonaws.com


  Queue:
    Type: AWS::Deadline::Queue
    Properties:
      DisplayName: BYOLQueue
      FarmId: !GetAtt Farm.FarmId
      RoleArn: !GetAtt QueueRole.Arn
      JobRunAsUser:
        Posix:
          Group: ""
          User: ""
        RunAs: WORKER_AGENT_USER
      JobAttachmentSettings:
        RootPrefix: job-attachments
        S3BucketName: !Ref JobAttachmentBucket

  Fleet:
    Type: AWS::Deadline::Fleet
    Properties:
      DisplayName: BYOLFleet
      FarmId: !GetAtt Farm.FarmId
      MinWorkerCount: 1
      MaxWorkerCount: 2
      Configuration:
        ServiceManagedEc2:
          InstanceCapabilities:
            VCpuCount:
              Min: 4
              Max: 16
            MemoryMiB:
              Min: 4096
              Max: 16384
            OsFamily: LINUX
            CpuArchitectureType: x86_64
          InstanceMarketOptions:
            Type: on-demand
      RoleArn: !GetAtt WorkerRole.Arn

  QFA:
    Type: AWS::Deadline::QueueFleetAssociation
    Properties:
      FarmId: !GetAtt Farm.FarmId
      FleetId: !GetAtt Fleet.FleetId
      QueueId: !GetAtt Queue.QueueId

  CondaQueueEnvironment:
    Type: AWS::Deadline::QueueEnvironment
    Properties:
      FarmId: !GetAtt Farm.FarmId
      Priority: 5
      QueueId: !GetAtt Queue.QueueId
      TemplateType: YAML
      Template: |
        specificationVersion: 'environment-2023-09'
        parameterDefinitions:
        - name: CondaPackages
          type: STRING
          description: >
            This is a space-separated list of Conda package match specifications to install for the job.
            E.g. "blender=3.6" for a job that renders frames in Blender 3.6.

            See https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/pkg-specs.html#package-match-specifications
          default: ""
          userInterface:
            control: LINE_EDIT
            label: Conda Packages
        - name: CondaChannels
          type: STRING
          description: >
            This is a space-separated list of Conda channels from which to install packages. Deadline Cloud SMF packages are
            installed from the "deadline-cloud" channel that is configured by Deadline Cloud.

            Add "conda-forge" to get packages from the https://conda-forge.org/ community, and "defaults" to get packages
            from Anaconda Inc (make sure your usage complies with https://www.anaconda.com/terms-of-use).
          default: "deadline-cloud"
          userInterface:
            control: LINE_EDIT
            label: Conda Channels
        environment:
          name: Conda
          script:
            actions:
              onEnter:
                command: "conda-queue-env-enter"
                args: ["{{Session.WorkingDirectory}}/.env", "--packages", "{{Param.CondaPackages}}", "--channels", "{{Param.CondaChannels}}"]
              onExit:
                command: "conda-queue-env-exit"

  BYOLQueueEnvironment:
    Type: AWS::Deadline::QueueEnvironment
    Properties:
      FarmId: !GetAtt Farm.FarmId
      Priority: 10
      QueueId: !GetAtt Queue.QueueId
      TemplateType: YAML
      Template: !Sub |
        specificationVersion: "environment-2023-09"
        parameterDefinitions:
          - name: LicenseInstanceId
            type: STRING
            description: >
              The Instance ID of the license server/proxy instance
            default: "${LicenseInstanceId}"
          - name: LicenseInstanceRegion
            type: STRING
            description: >
              The region containing this farm
            default: "${AWS::Region}"
          - name: LicensePorts
            type: STRING
            description: >
              Comma-separated list of ports to be forwarded to the license server/proxy instance.
              Example: "2700,2701,2702"
            default: "${LicensePorts}"
        environment:
          name: BYOL License Forwarding
          variables:
            example_LICENSE: 2700@localhost
          script:
            actions:
              onEnter:
                command: bash
                args: [ "{{Env.File.Enter}}"]
              onExit:
                command: bash
                args: [ "{{Env.File.Exit}}" ]
            embeddedFiles:
              - name: Enter
                type: TEXT
                runnable: True
                data: |
                  curl https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_64bit/session-manager-plugin.rpm -Ls | rpm2cpio - | cpio -iv --to-stdout ./usr/local/sessionmanagerplugin/bin/session-manager-plugin > {{Session.WorkingDirectory}}/session-manager-plugin
                  chmod +x {{Session.WorkingDirectory}}/session-manager-plugin
                  conda activate
                  python {{Env.File.StartSession}} {{Session.WorkingDirectory}}/session-manager-plugin
              - name: Exit
                type: TEXT
                runnable: True
                data: |
                  echo Killing SSM Manager Plugin PIDs: $BYOL_SSM_PIDS
                  for pid in ${!BYOL_SSM_PIDS//,/ }; do kill $pid; done
              - name: StartSession
                type: TEXT
                data: |
                  import boto3
                  import json
                  import subprocess
                  import sys

                  instance_id = "{{Param.LicenseInstanceId}}"
                  region = "{{Param.LicenseInstanceRegion}}"
                  license_ports_list = "{{Param.LicensePorts}}".split(",")

                  ssm_client = boto3.client("ssm", region_name=region)
                  pids = []

                  for port in license_ports_list:
                    session_response = ssm_client.start_session(
                      Target=instance_id,
                      DocumentName="AWS-StartPortForwardingSession",
                      Parameters={"portNumber": [port], "localPortNumber": [port]}
                    )

                    cmd = [
                      sys.argv[1],
                      json.dumps(session_response),
                      region,
                      "StartSession",
                      "",
                      json.dumps({"Target": instance_id}),
                      f"https://ssm.{region}.amazonaws.com"
                    ]

                    process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    pids.append(process.pid)
                    print(f"SSM Port Forwarding Session started for port {port}")

                  print(f"openjd_env: BYOL_SSM_PIDS={','.join(str(pid) for pid in pids)}")

```

3. When deploying the CloudFormation template, provide the following parameters:
   - Update the **LicenseInstanceID** with the Amazon EC2 Instance ID of
     your license server or proxy instance
   - Update the **LicensePorts** with a comma-separated list of ports
     to be forwarded to the license server or proxy instance (for example 2700,2701)

4. Deploy the template to setup your farm with bring your own license capability.
