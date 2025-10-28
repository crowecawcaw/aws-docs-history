AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# M2SFTP batch utility

M2SFTP is a JCL utility program designed to perform secure file transfers between systems using the Secure File Transfer Protocol (SFTP).
The program uses the Putty SFTP client, `psftp`, to perform the actual file transfers.
The program works similarly to a mainframe FTP utility program and uses user and password authentication.

###### Note

Public key authentication is not supported.

To convert your mainframe FTP JCLs to use SFTP, change `PGM=FTP` to `PGM=M2SFTP`.

###### Topics

- [Supported platforms](#m2sftp-platforms "#m2sftp-platforms")
- [Installing dependencies](#m2sftp-dependencies "#m2sftp-dependencies")
- [Configure M2SFTP for AWS Mainframe Modernization Managed](#m2sftp-configure-managed "#m2sftp-configure-managed")
- [Configure M2SFTP for AWS Mainframe Modernization runtime on Amazon EC2 (including AppStream 2.0)](#m2sftp-configure-customer-infra "#m2sftp-configure-customer-infra")
- [Sample JCLs](#m2sftp-jcl "#m2sftp-jcl")
- [Putty SFTP (PSFTP) client command reference](#m2sftp-cmd-ref "#m2sftp-cmd-ref")
- [Next steps](#m2sftp-next "#m2sftp-next")

## Supported platforms

You can use M2SFTP on any of the following platforms:

- AWS Mainframe Modernization Rocket Software (formerly Micro Focus) Managed
- Rocket Software Runtime (on Amazon EC2)
- All variants of Rocket Software Enterprise Developer (ED) and Rocket Software Enterprise Server (ES)
  products.

## Installing dependencies

###### To install the Putty SFTP client on Windows

- Download the [PuTTY SFTP](https://www.putty.org/ "https://www.putty.org/") client and install it.

###### To install the Putty SFTP client on Linux:

- Run the following command to install the Putty SFTP client:

```

  sudo yum -y install putty

```

## Configure M2SFTP for AWS Mainframe Modernization Managed

If your migrated applications are running on AWS Mainframe Modernization Managed, you will need to configure M2SFTP as follows.

- Set the appropriate Rocket Enterprise Server environment variables for MFFTP.
  Here are few examples:

      + `MFFTP_TEMP_DIR`
      + `MFFTP_SENDEOL`
      + `MFFTP_TIME`
      + `MFFTP_ABEND`

  You can set as few or as many of these variables as you want.
  You can set them in your JCL using the `ENVAR DD` statement.
  For more information on these variables, see [MFFTP Control Variables](https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/GUID-3F94BBC8-CB97-4642-A4A7-4235C0C079E2.html "https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/GUID-3F94BBC8-CB97-4642-A4A7-4235C0C079E2.html") in the Micro Focus documentation.

To test your configuration, see [Sample JCLs](#m2sftp-jcl "#m2sftp-jcl").

## Configure M2SFTP for AWS Mainframe Modernization runtime on Amazon EC2 (including AppStream 2.0)

If your migrated applications are running on AWS Mainframe Modernization runtime on Amazon EC2, configure M2SFTP as follows.

1.  Change the [Micro Focus JES Program Path](https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/GUID-BC8A1796-9EDE-48EB-8363-31C9BDE7F96B.html "https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/GUID-BC8A1796-9EDE-48EB-8363-31C9BDE7F96B.html") to include the binary location for batch utilities.
    If you need to specify multiple paths, use colons (`:`) to separate paths on Linux and semicolons (`;`) on Windows.
    - Linux: `/opt/aws/m2/microfocus/utilities/64bit`
    - Windows (32bit): `C:\AWS\M2\MicroFocus\Utilities\32bit`
    - Windows (64bit): `C:\AWS\M2\MicroFocus\Utilities\64bit`

2.  Set the appropriate Rocket Enterprise Server environment variables for MFFTP. Here are few examples:

        * `MFFTP_TEMP_DIR`
        * `MFFTP_SENDEOL`
        * `MFFTP_TIME`
        * MFFTP\_ABEND

    You can set as few or as many of these variables as you want.
    You can set them in your JCL using the `ENVAR DD` statement.
    For more information on these variables, see [MFFTP Control Variables](https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/GUID-3F94BBC8-CB97-4642-A4A7-4235C0C079E2.html "https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/GUID-3F94BBC8-CB97-4642-A4A7-4235C0C079E2.html") in the Micro Focus documentation.

To test your configuration, see [Sample JCLs](#m2sftp-jcl "#m2sftp-jcl").

## Sample JCLs

To test the installation, you can use either of the following sample JCL files.

**M2SFTP1.jcl**

This JCL shows how to call M2SFTP to send a file to a remote SFTP server.
Notice the environment variables that are set in the `ENVVAR DD` statement.

```
//M2SFTP1 JOB 'M2SFTP1',CLASS=A,MSGCLASS=X,TIME=1440
//*
//* Copyright Amazon.com, Inc. or its affiliates.*
//* All Rights Reserved.*
//*
//*-------------------------------------------------------------------**
//* Sample SFTP JCL step to send a file to SFTP server*
//*-------------------------------------------------------------------**
//*
//STEP01 EXEC PGM=M2SFTP,
//            PARM='127.0.0.1 (EXIT=99 TIMEOUT 300'
//*
//SYSFTPD  DD  *
RECFM FB
LRECL 80
SBSENDEOL CRLF
MBSENDEOL CRLF
TRAILINGBLANKS FALSE
/*
//NETRC    DD  *
machine 127.0.0.1 login sftpuser password sftppass
/*
//SYSPRINT DD  SYSOUT=*
//OUTPUT   DD  SYSOUT=*
//STDOUT   DD  SYSOUT=*
//INPUT    DD  *
type a
locsite notrailingblanks
cd files
put 'AWS.M2.TXT2PDF1.PDF' AWS.M2.TXT2PDF1.pdf
put 'AWS.M2.CARDDEMO.CARDDATA.PS' AWS.M2.CARDDEMO.CARDDATA.PS1.txt
quit
/*
//ENVVAR   DD *
MFFTP_VERBOSE_OUTPUT=ON
MFFTP_KEEP=N
/*
//*
//
```

**M2SFTP2.jcl**

This JCL shows how to call M2SFTP to receive a file from a remote SFTP server.
Notice the environment variables set in the `ENVVAR DD` statement.

```
//M2SFTP2 JOB 'M2SFTP2',CLASS=A,MSGCLASS=X,TIME=1440
//*
//* Copyright Amazon.com, Inc. or its affiliates.*
//* All Rights Reserved.*
//*
//*-------------------------------------------------------------------**
//* Sample SFTP JCL step to receive a file from SFTP server*
//*-------------------------------------------------------------------**
//*
//STEP01 EXEC PGM=M2SFTP
//*
//SYSPRINT DD  SYSOUT=*
//OUTPUT   DD  SYSOUT=*
//STDOUT   DD  SYSOUT=*
//INPUT    DD  *
open 127.0.0.1
sftpuser
sftppass
cd files
locsite recfm=fb lrecl=150
get AWS.M2.CARDDEMO.CARDDATA.PS.txt +
'AWS.M2.CARDDEMO.CARDDATA.PS2' (replace
quit
/*
//ENVVAR   DD *
MFFTP_VERBOSE_OUTPUT=ON
MFFTP_KEEP=N
/*
//*
//
```

###### Note

We strongly recommend storing FTP credentials in a NETRC file and restricting access to only authorized users.

## Putty SFTP (PSFTP) client command reference

The PSFTP client does not support all FTP commands.
The following list shows all the commands that PSFTP does support.

| Command | Description                                           |
| ------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| !       | Run a local command                                   |
| bye     | Finish your SFTP session                              |
| cd      | Change your remote working directory                  |
| chmod   | Change file permissions and modes                     |
| close   | Finish your SFTP session but do not quit PSFTP        |
| del     | Delete files on the remote server                     |
| dir     | List remote files                                     |
| exit    | Finish your SFTP session                              |
| get     | Download a file from the server to your local machine |
| help    | Give help                                             |
| lcd     | Change local working directory                        |
| lpwd    | Print local working directory                         |
| ls      | List remote files                                     |
| mget    | Download multiple files at once                       |
| mkdir   | Create directories on the remote server               |
| mput    | Upload multiple files at once                         |
| mv      | Move or rename file(s) on the remote server           |
| open    | Connect to a host                                     |
| put     | Upload a file from your local machine to the server   |
| pwd     | Print your remote working directory                   |
| quit    | Finish your SFTP session                              |
| reget   | Continue downloading files                            |
| ren     | Move or rename file(s) on the remote server           |
| reput   | Continue uploading files                              |
| rm      | Delete files on the remote server                     |
| rmdir   | Remove directories on the remote server               | ## Next steps To upload and download files into Amazon Simple Storage Service using SFTP, you could use M2SFTP in conjunction with the AWS Transfer Family, as described in the following blog posts. <br>• [Using AWS SFTP logical directories to build a simple data distribution service](https://aws.amazon.com/blogs/storage/using-aws-sftp-logical-directories-to-build-a-simple-data-distribution-service/ "https://aws.amazon.com/blogs/storage/using-aws-sftp-logical-directories-to-build-a-simple-data-distribution-service/") <br>• [Enable password authentication for AWS Transfer for SFTP using AWS Secrets Manager](https://aws.amazon.com/blogs/storage/enable-password-authentication-for-aws-transfer-for-sftp-using-aws-secrets-manager/ "https://aws.amazon.com/blogs/storage/enable-password-authentication-for-aws-transfer-for-sftp-using-aws-secrets-manager/") |
