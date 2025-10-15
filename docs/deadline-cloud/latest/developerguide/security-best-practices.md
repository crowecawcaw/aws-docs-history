# Security best practices for Deadline Cloud

AWS Deadline Cloud (Deadline Cloud) provides a number of security features to consider as you develop and
 implement your own security policies. The following best practices are general guidelines and
 don’t represent a complete security solution. Because these best practices might not be
 appropriate or sufficient for your environment, treat them as helpful considerations rather
 than prescriptions.

###### Note

For more information about the importance of many security topics, see the [Shared
 Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").


## Data protection


For data protection purposes, we recommend that you protect AWS account credentials
 and set up individual accounts with AWS Identity and Access Management (IAM). That way, each user is given only
 the permissions necessary to fulfill their job duties. We also recommend that you secure
 your data in the following ways:



* Use multi-factor authentication (MFA) with each account.
* Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend
 TLS 1.3.
* Set up API and user activity logging with AWS CloudTrail.
* Use AWS encryption solutions, along with all default security controls within
 AWS services.
* Use advanced managed security services such as Amazon Macie, which assists in
 discovering and securing personal data that is stored in Amazon Simple Storage Service (Amazon S3).
* If you require FIPS 140-2 validated cryptographic modules when accessing AWS
 through a command line interface or an API, use a FIPS endpoint. For more information
 about the available FIPS endpoints, see [Federal Information Processing
 Standard (FIPS) 140-2](http://aws.amazon.com/compliance/fips/ "http://aws.amazon.com/compliance/fips/").

We strongly recommend that you never put sensitive identifying information, such as your
 customers' account numbers, into free-form fields such as a **Name**
 field. This includes when you work with AWS Deadline Cloud or other AWS services using the
 console, API, AWS CLI, or AWS SDKs. Any data that you enter into Deadline Cloud or other services
 might get picked up for inclusion in diagnostic logs. When you provide a URL to an external
 server, don’t include credentials information in the URL to validate your request to that
 server.


## AWS Identity and Access Management permissions


Manage access to AWS resources using users, AWS Identity and Access Management (IAM) roles, and by granting
 the least privilege to users. Establish credential management policies and procedures for
 creating, distributing, rotating, and revoking AWS access credentials. For more
 information, see [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPractices.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPractices.html") in the
 *IAM User Guide*.


## Run jobs as users and groups


When using queue functionality in Deadline Cloud, it’s a best practice to specify an operating
 system (OS) user and its primary group so that the OS user has least-privilege permissions
 for the queue’s jobs.


When you specify a “Run as user” (and group), any processes for jobs submitted to the
 queue will be run using that OS user and will inherit that user’s associated OS
 permissions.


The fleet and queue configurations combine to establish a security posture. On the queue
 side, the “Job run as user” and IAM role can be specified to use the OS and AWS
 permissions for the queue’s jobs. The fleet defines the infrastructure (worker hosts,
 networks, mounted shared storage) that, when associated to a particular queue, run jobs
 within the queue. The data available on the worker hosts needs to be accessed by jobs from
 one or more associated queues. Specifying a user or group helps protect the data in jobs
 from other queues, other installed software, or other users with access to the worker
 hosts. When a queue is without a user, it runs as the agent user which can impersonate
 (`sudo`) any queue user. In this way, a queue without a user can escalate
 privileges to another queue.


## Networking


To prevent traffic from being intercepted or redirected, it's essential to secure how
 and where your network traffic is routed.


We recommend that you secure your networking environment in the following ways:



* Secure Amazon Virtual Private Cloud (Amazon VPC) subnet route tables to control how IP layer traffic is
 routed.
* If you are using Amazon Route 53 (Route 53) as a DNS provider in your farm or workstation
 setup, secure access to the Route 53 API.
* If you connect to Deadline Cloud outside of AWS such as by using on-premises workstations
 or other data centers, secure any on-premises networking infrastructure. This
 includes DNS servers and route tables on routers, switches, and other networking
 devices.

## Jobs and job data


Deadline Cloud jobs run within sessions on worker hosts. Each session runs one or more processes
 on the worker host, which generally require that you input data to produce output. 


To secure this data, you can configure operating system users with queues. The worker
 agent uses the queue OS user to run session sub-processes. These sub-processes inherit the
 queue OS user's permissions.


We recommend that you follow best practices to secure access to the data these
 sub-processes access. For more information, see [Shared
 responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").


## Farm structure


You can arrange Deadline Cloud fleets and queues many ways. However, there are security
 implications with certain arrangements.


A farm has one of the most secure boundaries because it can't share Deadline Cloud resources with
 other farms, including fleets, queues, and storage profiles. However, you can share
 external AWS resources within a farm, which compromises the security boundary.


You can also establish security boundaries between queues within the same farm using the
 appropriate configuration.


Follow these best practices to create secure queues in the same farm:



* Associate a fleet only with queues within the same security boundary. Note the
 following:




	+ After job runs on the worker host, data may remain behind, such as in a
	 temporary directory or the queue user's home directory.
	+ The same OS user runs all the jobs on a service-owned fleet worker host,
	 regardless of which queue you submit the job to.
	+ A job might leave processes running on a worker host, making it possible for
	 jobs from other queues to observe other running processes.
* Ensure that only queues within the same security boundary share an Amazon S3 bucket for
 job attachments.
* Ensure that only queues within the same security boundary share an OS user.
* Secure any other AWS resources that are integrated into the farm to the
 boundary.

## Job attachment queues


Job attachments are associated with a queue, which uses your Amazon S3
 bucket.



* Job attachments write to and read from a root prefix in the Amazon S3 bucket. You
 specify this root prefix in the `CreateQueue` API call.
* The bucket has a corresponding `Queue Role`, which specifies the role
 that grants queue users access to the bucket and root prefix. When creating a queue,
 you specify the `Queue Role` Amazon Resource Name (ARN) alongside the job
 attachments bucket and root prefix.
* Authorized calls to the `AssumeQueueRoleForRead`,
 `AssumeQueueRoleForUser`, and `AssumeQueueRoleForWorker` API
 operations return a set of temporary security credentials for the `Queue
 Role`.

If you create a queue and reuse an Amazon S3 bucket and root prefix, there is a risk of
 information being disclosed to unauthorized parties. For example, QueueA and QueueB share
 the same bucket and root prefix. In a secure workflow, ArtistA has access to QueueA but not
 QueueB. However, when multiple queues share a bucket, ArtistA can access the data in QueueB
 data because it uses the same bucket and root prefix as QueueA.


The console sets up queues that are secure by default. Ensure that the queues have a
 distinct combination of Amazon S3 bucket and root prefix unless they're part of a common
 security boundary.
 


To isolate your queues, you must configure the `Queue Role` to only allow
 queue access to the bucket and root prefix. In the following example, replace each
 `placeholder` with your resource-specific information.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:s3:::`JOB_ATTACHMENTS_BUCKET_NAME`",
 "arn:aws:s3:::`JOB_ATTACHMENTS_BUCKET_NAME`/`JOB_ATTACHMENTS_ROOT_PREFIX`/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "`111122223333`"
 }
 }
 },
 {
 "Action": [
 "logs:GetLogEvents"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws/deadline/`FARM_ID`/*"
 }
 ]
}`

```





You must also set a trust policy on the role. In the following example, replace the
 `placeholder` text with your resource-specific
 information.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Action": [
 "sts:AssumeRole"
 ],
 "Effect": "Allow",
 "Principal": {
 "Service": "deadline.amazonaws.com"
 },
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:deadline:`us-east-1`:`111122223333`:farm/`FARM_ID`"
 }
 }
 },
 {
 "Action": [
 "sts:AssumeRole"
 ],
 "Effect": "Allow",
 "Principal": {
 "Service": "credentials.deadline.amazonaws.com"
 },
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:deadline:`us-east-1`:`111122223333`:farm/`FARM_ID`"
 }
 }
 }
 ]
}`

```





## Custom software Amazon S3 buckets


You can add the following statement to your `Queue Role` to access custom
 software in your Amazon S3 bucket. In the following example, replace
 `SOFTWARE_BUCKET_NAME` with the name of your S3 bucket.



```
"Statement": [ 
    {
        "Action": [
            "s3:GetObject",
            "s3:ListBucket"
        ],
        "Effect": "Allow",
        "Resource": [
            "arn:aws:s3:::`SOFTWARE_BUCKET_NAME`",
            "arn:aws:s3:::`SOFTWARE_BUCKET_NAME`/*"
        ]
    }
]
```

For more information about Amazon S3 security best practices, see [Security best practices for Amazon S3](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md") in the *Amazon Simple Storage Service User Guide*.


## Worker hosts


Secure worker hosts to help ensure that each user can only perform operations for their
 assigned role. 


We recommend the following best practices to secure worker hosts: 



* Using a *host configuration script* can change the security and operations of a 
 worker. An incorrect configuration may cause the worker to be unstable or to stop
 working. It is your responsibility to debug such failures.
* Don’t use the same `jobRunAsUser` value with multiple queues unless
 jobs submitted to those queues are within the same security boundary.
* Don’t set the queue `jobRunAsUser` to the name of the OS user that the
 worker agent runs as.
* Grant queue users least-privileged OS permissions required for the intended queue
 workloads. Ensure that they don't have filesystem write permissions to work agent
 program files or other shared software.
* Ensure only the root user on Linux and the `Administrator` owns
 account on Windows owns and can modify the worker agent program files.
* On Linux worker hosts, consider configuring a `umask` override in
 `/etc/sudoers` that allows the worker agent user to launch processes as
 queue users. This configuration helps ensure other users can't access files written
 to the queue.
* Grant trusted individuals least-privileged access to worker hosts.
* Restrict permissions to local DNS override configuration files
 (`/etc/hosts` on Linux and `C:\Windows\system32\etc\hosts`
 on Windows), and to route tables on workstations and worker host operating
 systems.
* Restrict permissions to DNS configuration on workstations and worker host
 operating systems.
* Regularly patch the operating system and all installed software. This approach
 includes software specifically used with Deadline Cloud such as submitters, adaptors, worker
 agents, OpenJD packages, and others.
* Use strong passwords for the Windows queue `jobRunAsUser`.
* Regularly rotate the passwords for your queue `jobRunAsUser`.
* Ensure least privilege access to the Windows password secrets and delete unused
 secrets.
* Don't give the queue `jobRunAsUser` permission the schedule commands to
 run in the future:




	+ On Linux, deny these accounts access to `cron` and
	 `at`.
	+ On Windows, deny these accounts access to the Windows task
	 scheduler.

###### Note

For more information about the importance of regularly patching the operating system
 and installed software, see the [Shared
 Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").


## Host configuration script



* Using a host configuration script can change the security and operations of a 
 worker. An incorrect configuration may cause the worker to be unstable or to stop
 working. It is your responsibility to debug such failures.

## Workstations


It's important to secure workstations with access to Deadline Cloud. This approach helps ensure
 that any jobs you submit to Deadline Cloud can't run arbitrary workloads billed to your
 AWS account. 


We recommend the following best practice to secure artist workstations. For more
 information, see the [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").



* Secure any persisted credentials that provide access to AWS, including Deadline Cloud.
 For more information, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#securing_access-keys "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#securing_access-keys") in the *IAM User Guide*.
* Only install trusted, secure software.
* Require users federate with an identity provider to access AWS with temporary
 credentials.
* Use secure permissions on Deadline Cloud submitter program files to prevent
 tampering.
* Grant trusted individuals least-privileged access to artist workstations.
* Only use submitters and adaptors that you obtain through the Deadline Cloud Monitor.
* Restrict permissions to local DNS override configuration files
 (`/etc/hosts` on Linux and macOS, and
 `C:\Windows\system32\etc\hosts` on Windows), and to route tables on
 workstations and worker host operating systems.
* Restrict permissions to `/etc/resolve.conf` on workstations and worker
 host operating systems.
* Regularly patch the operating system and all installed software. This approach
 includes software specifically used with Deadline Cloud such as submitters, adaptors, worker
 agents, OpenJD packages, and others.

## Verify the authenticity of downloaded software


Verify your software's authenticity after downloading the installer to protect against
 file tampering. This procedure works for both Windows and Linux systems.



Windows
To verify the authenticity of your downloaded files, complete the following
 steps.


1. In the following command, replace
 ``file`` with the file that you want
 to verify. For example, ``C:\PATH\TO\MY\`DeadlineCloudSubmitter-windows-x64-installer.exe` . Also, replace
 ``signtool-sdk-version`` with the
 version of the SignTool SDK installed. For example,
 `10.0.22000.0`.


`"C:\Program Files (x86)\Windows
 Kits\10\bin\`signtool-sdk-version`\x86\signtool.exe"
 verify /v`file``
2. For example, you can verify the Deadline Cloud submitter installer file by running
 the following command:


`"C:\Program Files (x86)\Windows
 Kits\10\bin\10.0.22000.0\x86\signtool.exe" verify /v
 DeadlineCloudSubmitter-windows-x64-installer.exe`


Linux
To verify the authenticity of your downloaded files, use the `gpg`
 command line tool.


1. Import the `OpenPGP` key by running the following
 command:



```
 gpg --import --armor <<EOF
-----BEGIN PGP PUBLIC KEY BLOCK-----

mQINBGX6GQsBEADduUtJgqSXI+q76O6fsFwEYKmbnlyL0xKvlq32EZuyv0otZo5L
le4m5Gg52AzrvPvDiUTLooAlvYeozaYyirIGsK08Ydz0Ftdjroiuh/mw9JSJDJRI
rnRn5yKet1JFezkjopA3pjsTBP6lW/mb1bDBDEwwwtH0x9lV7A03FJ9T7Uzu/qSh
qO/UYdkafro3cPASvkqgDt2tCvURfBcUCAjZVFcLZcVD5iwXacxvKsxxS/e7kuVV
I1+VGT8Hj8XzWYhjCZxOLZk/fvpYPMyEEujN0fYUp6RtMIXve0C9awwMCy5nBG2J
eE2Ol5DsCpTaBd4Fdr3LWcSs8JFA/YfP9auL3NczOozPoVJt+fw8CBlVIXO0J7l5
hvHDjcC+5v0wxqAlMG6+f/SX7CT8FXK+L3iOJ5gBYUNXqHSxUdv8kt76/KVmQa1B
Akl+MPKpMq+lhw++S3G/lXqwWaDNQbRRw7dSZHymQVXvPp1nsqc3hV7KlOM+6s6g
1g4mvFY4lf6DhptwZLWyQXU8rBQpojvQfiSmDFrFPWFi5BexesuVnkGIolQoklKx
AVUSdJPVEJCteyy7td4FPhBaSqT5vW3+ANbr9b/uoRYWJvn17dN0cc9HuRh/Ai+I
nkfECo2WUDLZ0fEKGjGyFX+todWvJXjvc5kmE9Ty5vJp+M9Vvb8jd6t+mwARAQAB
tCxBV1MgRGVhZGxpbmUgQ2xvdWQgPGF3cy1kZWFkbGluZUBhbWF6b24uY29tPokC
VwQTAQgAQRYhBLhAwIwpqQeWoHH6pfbNPOa3bzzvBQJl+hkLAxsvBAUJA8JnAAUL
CQgHAgIiAgYVCgkICwIDFgIBAh4HAheAAAoJEPbNPOa3bzzvKswQAJXzKSAY8sY8
F6Eas2oYwIDDdDurs8FiEnFghjUEO6MTt9AykF/jw+CQg2UzFtEyObHBymhgmhXE
3buVeom96tgM3ZDfZu+sxi5pGX6oAQnZ6riztN+VpkpQmLgwtMGpSMLl3KLwnv2k
WK8mrR/fPMkfdaewB7A6RIUYiW33GAL4KfMIs8/vIwIJw99NxHpZQVoU6dFpuDtE
1OuxGcCqGJ7mAmo6H/YawSNp2Ns80gyqIKYo7o3LJ+WRroIRlQyctq8gnR9JvYXX
42ASqLq5+OXKo4qh81blXKYqtc176BbbSNFjWnzIQgKDgNiHFZCdcOVgqDhwO15r
NICbqqwwNLj/Fr2kecYx180Ktpl0jOOw5IOyh3bf3MVGWnYRdjvA1v+/CO+55N4g
z0kf50Lcdu5RtqV10XBCifn28pecqPaSdYcssYSRl5DLiFktGbNzTGcZZwITTKQc
af8PPdTGtnnb6P+cdbW3bt9MVtN5/dgSHLThnS8MPEuNCtkTnpXshuVuBGgwBMdb
qUC+HjqvhZzbwns8dr5WI+6HWNBFgGANn6ageYl58vVp0UkuNP8wcWjRARciHXZx
ku6W2jPTHDWGNrBQO2Fx7fd2QYJheIPPAShHcfJO+xgWCof45D0vAxAJ8gGg9Eq+
gFWhsx4NSHn2gh1gDZ41Ou/4exJ1lwPM
=uVaX
-----END PGP PUBLIC KEY BLOCK-----
EOF
```
2. Determine whether to trust the `OpenPGP` key. Some factors to
 consider when deciding whether to trust the above key include the
 following:




	* The internet connection you’ve used to obtain the GPG key from this
	 website is secure.
	* The device that you are accessing this website on is secure.
	* AWS has taken measures to secure the hosting of the
	 `OpenPGP` public key on this website.
3. If you decide to trust the OpenPGP key, edit the key to
 trust with `gpg` similar to the following example:



```
$ gpg --edit-key 0xB840C08C29A90796A071FAA5F6CD3CE6B76F3CEF

    gpg (GnuPG) 2.0.22; Copyright (C) 2013 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.


    pub  4096R/4BF0B8D2  created: 2023-06-23  expires: 2025-06-22  usage: SCEA
                         trust: unknown       validity: unknown
    [ unknown] (1). AWS Deadline Cloud example@example.com

    gpg> trust
    pub  4096R/4BF0B8D2  created: 2023-06-23  expires: 2025-06-22  usage: SCEA
                         trust: unknown       validity: unknown
    [ unknown] (1). AWS Deadline Cloud aws-deadline@amazon.com

    Please decide how far you trust this user to correctly verify other users' keys
    (by looking at passports, checking fingerprints from different sources, etc.)

      1 = I don't know or won't say
      2 = I do NOT trust
      3 = I trust marginally
      4 = I trust fully
      5 = I trust ultimately
      m = back to the main menu

    Your decision? 5
    Do you really want to set this key to ultimate trust? (y/N) y

    pub  4096R/4BF0B8D2  created: 2023-06-23  expires: 2025-06-22  usage: SCEA
                         trust: ultimate      validity: unknown
    [ unknown] (1). AWS Deadline Cloud aws-deadline@amazon.com
    Please note that the shown key validity is not necessarily correct
    unless you restart the program.

    gpg> quit
```
4. ###### Verify the Deadline Cloud submitter installer


To verify the Deadline Cloud submitter installer, complete the following
 steps:


	1. Return to the Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home")
	**Downloads** page and download the signature file
	 for the Deadline Cloud submitter installer.
	2. Verify the signature of the Deadline Cloud submitter installer by
	 running:
	
	
	
	```
	gpg --verify ./DeadlineCloudSubmitter-linux-x64-installer.run.sig ./DeadlineCloudSubmitter-linux-x64-installer.run
	```
5. ###### Verify the Deadline Cloud monitor


###### Note

You can verify the Deadline Cloud monitor download using signature files or platform
 specific methods. For platform specific methods, see the Linux
 (Debian) tab, the Linux (RPM) tab, or the Linux
 (AppImage) tab based on your downloaded file type. 


To verify the Deadline Cloud monitor desktop application with signature files, complete
 the following steps:


	1. Return to the Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home")
	**Downloads** page and download the corresponding
	 .sig file, and then run
	
	
	**For .deb:**
	
	
	
	```
	gpg --verify ./deadline-cloud-monitor_`<APP_VERSION>`_amd64.deb.sig ./deadline-cloud-monitor_`<APP_VERSION>`_amd64.deb
	```
	
	**For .rpm:**
	
	
	
	```
	gpg --verify ./deadline-cloud-monitor_`<APP_VERSION>`_x86_64.deb.sig ./deadline-cloud-monitor_`<APP_VERSION>`_x86_64.rpm
	```
	
	**For .AppImage:**
	
	
	
	```
	gpg --verify ./deadline-cloud-monitor_`<APP_VERSION>`_amd64.AppImage.sig ./deadline-cloud-monitor_`<APP_VERSION>`_amd64.AppImage
	```
	2. Confirm that the output looks similar to the following:
	
	
	`gpg: Signature made Mon Apr 1 21:10:14 2024 UTC`
	
	
	`gpg: using RSA key
	 B840C08C29A90796A071FAA5F6CD3CE6B7`
	
	
	If the output contains the phrase `Good signature from "AWS
	 Deadline Cloud"`, it means that the signature has
	 successfully been verified and you can run the Deadline Cloud monitor installation
	 script.


Linux (AppImage)
To verify packages that use a Linux .AppImage binary, first complete steps
 1-3 in the Linux tab, then complete the following steps.


1. From the AppImageUpdate [page](https://github.com/AppImageCommunity/AppImageUpdate/releases/tag/continuous "https://github.com/AppImageCommunity/AppImageUpdate/releases/tag/continuous") in GitHub, download the
 **validate-x86\_64.AppImage** file.
2. After downloading the file, to add execute permissions, run the following
 command.



```
chmod a+x ./validate-x86_64.AppImage
```
3. To add execute permissions, run the following command.



```
chmod a+x ./deadline-cloud-monitor_`<APP_VERSION>`_amd64.AppImage
```
4. To verify the Deadline Cloud monitor signature, run the following command.



```
./validate-x86_64.AppImage ./deadline-cloud-monitor_`<APP_VERSION>`_amd64.AppImage
```

If the output contains the phrase `Validation successful`, it
 means that the signature has successfully been verified and you can safely
 run the Deadline Cloud monitor installation script.


Linux (Debian)
To verify packages that use a Linux .deb binary, first complete steps 1-3 in
 the Linux tab.


**dpkg** is the core package management tool in most
 debian based Linux distributions. You can verify
 the .deb file with the tool.


1. From the Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home")
**Downloads** page, download the Deadline Cloud monitor .deb file.
2. Replace `<APP_VERSION>` with the version
 of the .deb file you want to verify.



```
dpkg-sig --verify deadline-cloud-monitor_`<APP_VERSION>`_amd64.deb
```
3. The output will be similar to:



```
ProcessingLinux deadline-cloud-monitor_`<APP_VERSION>`_amd64.deb...
GOODSIG _gpgbuilder B840C08C29A90796A071FAA5F6CD3C 171200
```
4. To verify the .deb file, confirm that `GOODSIG` is present in
 the output.


Linux (RPM)
To verify packages that use a Linux .rpm binary, first complete steps 1-3 in
 the Linux tab.


1. From the Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home")
**Downloads** page, download the Deadline Cloud monitor .rpm file.
2. Replace `<APP_VERSION>` with the version
 of the .rpm file to verify.



```
gpg --export --armor "Deadline Cloud" > key.pub
sudo rpm --import key.pub
rpm -K deadline-cloud-monitor-`<APP_VERSION>`-1.x86_64.rpm
```
3. The output will be similar to:



```
deadline-cloud-monitor-deadline-cloud-monitor-`<APP_VERSION>`-1.x86_64.rpm-1.x86_64.rpm: digests signatures OK
```
4. To verify the .rpm file, confirm that `digests signatures OK`
 is in the output.
