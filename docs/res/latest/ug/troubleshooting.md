# Troubleshooting

This section contains information about how to monitor the system and how to
troubleshoot specific issues that may occur.

###### Topics

- [General Debugging and Monitoring](res-troubleshooting-general.md "res-troubleshooting-general.md")
- [Issue RunBooks](res-troubleshooting-issue-runbooks.md "res-troubleshooting-issue-runbooks.md")
- [Known Issues](res-troubleshooting-known-issues.md "res-troubleshooting-known-issues.md")
  Detailed contents:

- [General Debugging and Monitoring](res-troubleshooting-general.md "res-troubleshooting-general.md")
  - [Useful log and event information sources](res-troubleshooting-general.md#res-troubleshooting-general-info "res-troubleshooting-general.md#res-troubleshooting-general-info")
    - [Where to find environment variables](res-troubleshooting-general.md#res-troubleshooting-general-info-env-vars "res-troubleshooting-general.md#res-troubleshooting-general-info-env-vars")
    - [Log files on the environment Amazon EC2
      instances](res-troubleshooting-general.md#res-troubleshooting-general-info-logs "res-troubleshooting-general.md#res-troubleshooting-general-info-logs")
    - [CloudFormation Stacks](res-troubleshooting-general.md#res-troubleshooting-cf-stacks "res-troubleshooting-general.md#res-troubleshooting-cf-stacks")
    - [System failures due to an issue and
      reflected by Amazon EC2 Auto Scaling Group Activity](res-troubleshooting-general.md#res-troubleshooting-asg-activity "res-troubleshooting-general.md#res-troubleshooting-asg-activity")

  - [Typical Amazon EC2 Console Appearance](res-troubleshooting-general.md#res-troubleshooting-ec2-console "res-troubleshooting-general.md#res-troubleshooting-ec2-console")
    - [Infrastructure hosts](res-troubleshooting-general.md#res-troubleshooting-ec2-console-infra "res-troubleshooting-general.md#res-troubleshooting-ec2-console-infra")
    - [Infrastructure hosts and
      virtual desktops](res-troubleshooting-general.md#res-troubleshooting-ec2-console-virtual "res-troubleshooting-general.md#res-troubleshooting-ec2-console-virtual")
    - [Hosts in a terminated state](res-troubleshooting-general.md#res-troubleshooting-ec2-console-hosts-terminated "res-troubleshooting-general.md#res-troubleshooting-ec2-console-hosts-terminated")
    - [Useful Active Directory (AD)
      related commands for reference](res-troubleshooting-general.md#res-troubleshooting-ec2-console-active-dir "res-troubleshooting-general.md#res-troubleshooting-ec2-console-active-dir")

  - [Windows DCV debugging](res-troubleshooting-general.md#res-troubleshooting-windows-dcv "res-troubleshooting-general.md#res-troubleshooting-windows-dcv")
  - [Find Amazon DCV Version Information](res-troubleshooting-general.md#res-troubleshooting-find-nice-dcv "res-troubleshooting-general.md#res-troubleshooting-find-nice-dcv")

- [Issue RunBooks](res-troubleshooting-issue-runbooks.md "res-troubleshooting-issue-runbooks.md")
  - [Installation issues](res-troubleshooting-issue-runbooks.md#installation-issues "res-troubleshooting-issue-runbooks.md#installation-issues")
    - [AWS CloudFormation stack fails to create with message "WaitCondition
      received failed message. Error:States.TaskFailed"](res-troubleshooting-issue-runbooks.md#cf-stack-fails "res-troubleshooting-issue-runbooks.md#cf-stack-fails")
    - [Email notification not received after AWS CloudFormation
      stacks created successfully](res-troubleshooting-issue-runbooks.md#email-invitation-not-received "res-troubleshooting-issue-runbooks.md#email-invitation-not-received")
    - [Instances cycling or vdc-controller in failed state](res-troubleshooting-issue-runbooks.md#instances-cycling "res-troubleshooting-issue-runbooks.md#instances-cycling")
    - [Environment CloudFormation stack fails to delete due to dependent object error](res-troubleshooting-issue-runbooks.md#object-error "res-troubleshooting-issue-runbooks.md#object-error")
    - [Error encountered for CIDR block parameter during environment creation](res-troubleshooting-issue-runbooks.md#cidr-block-error "res-troubleshooting-issue-runbooks.md#cidr-block-error")
    - [CloudFormation stack creation failure during environment creation](res-troubleshooting-issue-runbooks.md#cf-stack-creation-fails "res-troubleshooting-issue-runbooks.md#cf-stack-creation-fails")
    - [Creation of external resources (demo) stack
      fails with AdDomainAdminNode CREATE_FAILED](res-troubleshooting-issue-runbooks.md#demo-environment-stack-fails "res-troubleshooting-issue-runbooks.md#demo-environment-stack-fails")

  - [Identity management issues](res-troubleshooting-issue-runbooks.md#troubleshooting-identity-management "res-troubleshooting-issue-runbooks.md#troubleshooting-identity-management")
    - [I am not authorized to
      perform iam:PassRole](res-troubleshooting-issue-runbooks.md#res-troubleshooting-issue-runbooks-unauth-passrole "res-troubleshooting-issue-runbooks.md#res-troubleshooting-issue-runbooks-unauth-passrole")
    - [I want to allow people
      outside of my AWS account to access my Research and Engineering Studio on AWS
      resources](res-troubleshooting-issue-runbooks.md#res-troubleshooting-issue-runbooks-outside-acct "res-troubleshooting-issue-runbooks.md#res-troubleshooting-issue-runbooks-outside-acct")
    - [When logging into the environment, I immediately return
      to the login page](res-troubleshooting-issue-runbooks.md#return-to-login "res-troubleshooting-issue-runbooks.md#return-to-login")
    - ["User not found" error when trying to log in](res-troubleshooting-issue-runbooks.md#user-not-found "res-troubleshooting-issue-runbooks.md#user-not-found")
    - [User added in Active Directory, but missing from RES](res-troubleshooting-issue-runbooks.md#user-missing "res-troubleshooting-issue-runbooks.md#user-missing")
    - [User unavailable when creating a session](res-troubleshooting-issue-runbooks.md#session-user-unavailable "res-troubleshooting-issue-runbooks.md#session-user-unavailable")
    - [Size limit exceeded error in CloudWatch cluster-manager
      log](res-troubleshooting-issue-runbooks.md#sizelimit-exceeded-error "res-troubleshooting-issue-runbooks.md#sizelimit-exceeded-error")

  - [Storage](res-troubleshooting-issue-runbooks.md#res-troubleshooting-storage "res-troubleshooting-issue-runbooks.md#res-troubleshooting-storage")
    - [I created file system through RES
      but it doesn't mount on the VDI hosts](res-troubleshooting-issue-runbooks.md#res-troubleshooting-storage-created "res-troubleshooting-issue-runbooks.md#res-troubleshooting-storage-created")
    - [I onboarded a file system through
      RES but it doesn't mount on the VDI hosts](res-troubleshooting-issue-runbooks.md#res-troubleshooting-storage-onboarded "res-troubleshooting-issue-runbooks.md#res-troubleshooting-storage-onboarded")
    - [I am not able to read/write on
      from VDI hosts](res-troubleshooting-issue-runbooks.md#res-troubleshooting-storage-rw "res-troubleshooting-issue-runbooks.md#res-troubleshooting-storage-rw")
      - [Example permission handling
        use cases](res-troubleshooting-issue-runbooks.md#res-troubleshooting-storage-rw-example "res-troubleshooting-issue-runbooks.md#res-troubleshooting-storage-rw-example")

    - [I created Amazon FSx for NetApp ONTAP from RES
      but it did not join my domain](res-troubleshooting-issue-runbooks.md#res-troubleshooting-storage-join "res-troubleshooting-issue-runbooks.md#res-troubleshooting-storage-join")

  - [Snapshots](res-troubleshooting-issue-runbooks.md#res-troubleshooting-snapshots "res-troubleshooting-issue-runbooks.md#res-troubleshooting-snapshots")
    - [A Snapshot has a status of Failed](res-troubleshooting-issue-runbooks.md#res-troubleshooting-snapshots-failed "res-troubleshooting-issue-runbooks.md#res-troubleshooting-snapshots-failed")
    - [A Snapshot fails to apply
      with logs indicating that the tables could not be imported.](res-troubleshooting-issue-runbooks.md#res-troubleshooting-snapshots-not-imported "res-troubleshooting-issue-runbooks.md#res-troubleshooting-snapshots-not-imported")

  - [Infrastructure](res-troubleshooting-issue-runbooks.md#res-troubleshooting-infrastructure "res-troubleshooting-issue-runbooks.md#res-troubleshooting-infrastructure")
    - [Load balancer target
      groups without healthy instances](res-troubleshooting-issue-runbooks.md#res-troubleshooting-infrastructure-load-balancer "res-troubleshooting-issue-runbooks.md#res-troubleshooting-infrastructure-load-balancer")

  - [Launching Virtual Desktops](res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops "res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops")
    - [I need to launch / resume a large number
      of VDIs in the RES web portal](res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-resume-vdis "res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-resume-vdis")
    - [Login account for Windows
      Virtual Desktop is set to Administrator](res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-windows-admin "res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-windows-admin")
    - [Certificate expires
      when using external resource CertificateRenewalNode](res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-certificate-expires "res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-certificate-expires")
    - [A virtual desktop that
      was previously working is no longer able to connect successfully](res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-was-working "res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-was-working")
    - [I am only able to launch
      5 virtual desktops](res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-only-five "res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-only-five")
    - [Desktop Windows
      connect attempts fail with "The connection has been closed. Transport error"](res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-transport-error "res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-transport-error")
    - [VDIs stuck in Provisioning
      state](res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-stuck-prov "res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-stuck-prov")
    - [VDIs get into Error
      state after launching](res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-error-after "res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-error-after")
    - [VDI session goes to a blank screen
      after logging in](res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-vdi-blank-screen "res-troubleshooting-issue-runbooks.md#res-troubleshooting-virtual-desktops-vdi-blank-screen")

  - [Virtual Desktop Component](res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component "res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component")
    - [Amazon EC2 instance is repeatedly
      showing terminated in the console](res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component-ec2-terminated "res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component-ec2-terminated")
    - [vdc-controller instance is
      cycling due to failing to join AD / eVDI module shows Failed API Health Check](res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component-cycling "res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component-cycling")
    - [Project does not appear
      in the pull down when editing the Software Stack to add it](res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component-not-in-pulldown "res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component-not-in-pulldown")
    - [cluster-manager Amazon CloudWatch
      log shows "<user-home-init> account not available yet. waiting for user to be synced"
      (where the account is a user name)](res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component-acct-unavailable "res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component-acct-unavailable")
    - [Windows desktop on login attempt
      says "Your account has been disabled. Please see your administrator"](res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component-acct-disabled "res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component-acct-disabled")
    - [DHCP Options issues with
      external/customer AD configuration](res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component-dhcp "res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-component-dhcp")
    - [Firefox error MOZILLA_PKIX_ERROR_REQUIRED_TLS_FEATURE_MISSING](res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-firefox "res-troubleshooting-issue-runbooks.md#res-troubleshooting-vd-firefox")

  - [Env deletion](res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion "res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion")
    - [res-xxx-cluster stack in
      "DELETE_FAILED" state and cannot be deleted manually due to "Role is invalid or cannot
      be assumed" error](res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion-role-invalid "res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion-role-invalid")
    - [Collecting Logs](res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion-collect-logs "res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion-collect-logs")
    - [Downloading VDI Logs](res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion-download-logs "res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion-download-logs")
    - [Downloading logs from Linux
      EC2 instances](res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion-linux-ec2-logs "res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion-linux-ec2-logs")
    - [Downloading logs from
      Windows EC2 instances](res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion-windows-ec2-logs "res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion-windows-ec2-logs")
    - [Collecting ECS logs for
      the WaitCondition error](res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion-waitcondition "res-troubleshooting-issue-runbooks.md#res-troubleshooting-env-deletion-waitcondition")

  - [Demo environment](res-troubleshooting-issue-runbooks.md#res-troubleshooting-demo-env "res-troubleshooting-issue-runbooks.md#res-troubleshooting-demo-env")
    - [Demo environment login error when handling
      authentication request to identity provider](res-troubleshooting-issue-runbooks.md#demo-environment-login-error "res-troubleshooting-issue-runbooks.md#demo-environment-login-error")
    - [Demo stack keycloak not working](res-troubleshooting-issue-runbooks.md#demo-environment-stack-keycloak "res-troubleshooting-issue-runbooks.md#demo-environment-stack-keycloak")

  - [Active Directory issues](res-troubleshooting-issue-runbooks.md#active-directory-issues "res-troubleshooting-issue-runbooks.md#active-directory-issues")
    - [My VDI is stuck in the provisioning state for
      a long time, or I cannot login my VDI as an AD user after the VDI is ready](res-troubleshooting-issue-runbooks.md#active-directory-issues-vdi-stuck "res-troubleshooting-issue-runbooks.md#active-directory-issues-vdi-stuck")
    - [I cannot login the RES web portal after configuring SSO](res-troubleshooting-issue-runbooks.md#active-directory-issues-res-web-portal "res-troubleshooting-issue-runbooks.md#active-directory-issues-res-web-portal")
    - [AD user cannot access the
      home directory using File Browser even after launching Linux VDIs successfully](res-troubleshooting-issue-runbooks.md#active-directory-issues-home-directory-access "res-troubleshooting-issue-runbooks.md#active-directory-issues-home-directory-access")
    - [AD admin user cannot access the
      Bastion Host after SSH access is enabled](res-troubleshooting-issue-runbooks.md#active-directory-issues-bastion-host-access "res-troubleshooting-issue-runbooks.md#active-directory-issues-bastion-host-access")
    - [View and manage my Active
      Directory deployed by RES external resource stack](res-troubleshooting-issue-runbooks.md#active-directory-issues-external-resource-stack "res-troubleshooting-issue-runbooks.md#active-directory-issues-external-resource-stack")

- [Known Issues 2024.x](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x")
  - [Known Issues 2024.x](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x")
    - [(2024.12 and 2024.12.01)
      Regex failure when registering a new Cognito user](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-regex-failure-cognito "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-regex-failure-cognito")
    - [(2024.12.01 and earlier)
      Invalid bad cert error when connecting to VDI using a custom domain](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-invalid-bad-cert "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-invalid-bad-cert")
    - [(2024.12 and 2024.12.01)
      Active Directory users cannot SSH to Bastion Host](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-ad-users-cannot-ssh "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-ad-users-cannot-ssh")
    - [(2024.10) VDI
      auto stop broken for RES environments deployed in isolated VPCs](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-vdi-auto-stop-broken "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-vdi-auto-stop-broken")
    - [(2024.10 and earlier) Failure to launch
      VDI for Graphic enhanced instance types](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-fail-to-launch-vdi "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-fail-to-launch-vdi")
    - [(2024.08) Preparing
      Infrastructure AMI Failure](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-prep-infra-ami-fail "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-prep-infra-ami-fail")
    - [(2024.08)
      Virtual desktops fail to mount read/write Amazon S3 bucket with root bucket ARN and custom
      prefixing](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-vdi-fails-to-mount-s3 "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-vdi-fails-to-mount-s3")
    - [(2024.06) Apply
      snapshot fails when the AD group name contains spaces](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-apply-snapshot-fails "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-apply-snapshot-fails")
    - [(2024.06 and earlier)
      Group members not synced to RES during AD sync](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-group-not-synced "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-group-not-synced")
    - [(2024.06 and earlier)
      CVE-2024-6387, RegreSSHion, Security Vulnerability in RHEL9 and Ubuntu VDIs](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-regresshion "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-regresshion")
    - [(2024.04-2024.04.02)
      Provided IAM Permission Boundary not attached to the VDI instances' role](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-iam-boundary "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-iam-boundary")
    - [(2024.04.02 and earlier)
      Windows NVIDIA instances in ap-southeast-2 (Sydney) fail to launch](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-nvidia-instances "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-nvidia-instances")
    - [(2024.04 and 2024.04.01)
      RES delete failure in GovCloud](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-delete-fail "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-delete-fail")
    - [(2024.04 - 2024.04.02)
      Linux virtual desktop may be stuck in the "RESUMING" status on reboot](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-linux-stuck-resuming "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-linux-stuck-resuming")
    - [(2024.04.02 and earlier)
      Fails to sync AD users whose SAMAccountName attribute includes capital letters or special
      characters](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-samaccountname "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-samaccountname")
    - [(2024.04.02 and earlier)
      Private key for accessing the bastion host is invalid](res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-private-key "res-troubleshooting-known-issues.md#res-troubleshooting-known-issues-2024x-private-key")
