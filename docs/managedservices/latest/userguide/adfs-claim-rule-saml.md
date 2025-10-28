# AD FS claim rule and SAML settings

ActiveDirectory Federation Services (AD FS) claim rule and SAML settings for AWS Managed Services (AMS)

For detailed step-by-step instructions on how to install and configure AD FS see
[Enabling Federation to AWS Using Windows Active Directory, ADFS, and SAML 2.0](https://aws.amazon.com/blogs/security/enabling-federation-to-aws-using-windows-active-directory-adfs-and-saml-2-0/ "https://aws.amazon.com/blogs/security/enabling-federation-to-aws-using-windows-active-directory-adfs-and-saml-2-0/").

## ADFS claim rule configurations

If you already have an ADFS implementation, configure following:

- Relying party trust
- Claims rules

The relying party trust and claims rules steps are taken from
[Enabling Federation to AWS Using Windows Active Directory, AD FS, and SAML 2.0](https://aws.amazon.com/blogs/security/enabling-federation-to-aws-using-windows-active-directory-adfs-and-saml-2-0/ "https://aws.amazon.com/blogs/security/enabling-federation-to-aws-using-windows-active-directory-adfs-and-saml-2-0/")blog

- Claims rules:
  - **Nameid**: Configuration per blog post
  - **RoleSessionName**: Configure as follows
    - **Claim rule name**: `RoleSessionName`
    - **Attribute store**: `Active Directory`
    - **LDAP Attribute**: `SAM-Account-Name`
    - **Outgoing Claim Type**:
      `https://aws.amazon.com/SAML/Attributes/RoleSessionName`
    - **Get AD Groups**: Configuration per
      [blog post](https://aws.amazon.com/blogs/security/enabling-federation-to-aws-using-windows-active-directory-adfs-and-saml-2-0/ "https://aws.amazon.com/blogs/security/enabling-federation-to-aws-using-windows-active-directory-adfs-and-saml-2-0/")
    - **Role claim**: Configure as follows

    ```

    c:[Type == "http://temp/variable", Value =~ "(?i)^AWS-([^d]{12})-"]

    ```

    ```

    => issue(Type = "https://aws.amazon.com/SAML/Attributes/Role", Value = RegExReplace(c.Value, "AWS-([^d]{12})-", "arn:aws:iam::$1:saml-provider/customer-readonly-saml,arn:aws:iam::$1:role/"));

    ```

## Web console

You can access the AWS Web console by using the link below replacing
`[ADFS-FQDN]` with the FQDN of your ADFS implementation.

https://`[ADFS-FQDN]`/adfs/ls/IdpInitiatedSignOn.aspx

Your IT department can deploy the above link to the user population via a Group Policy.

## API and CLI access with SAML

How to configure API and CLI access with SAML.

The python packages are sourced from the blog posts below:

- NTLM:
  [How to Implement Federated API and CLI Access Using SAML 2.0 and AD FS](https://aws.amazon.com/blogs/security/how-to-implement-federated-api-and-cli-access-using-saml-2-0-and-ad-fs/ "https://aws.amazon.com/blogs/security/how-to-implement-federated-api-and-cli-access-using-saml-2-0-and-ad-fs/")
- Forms:
  [How to Implement a General Solution for Federated API/CLI Access Using SAML 2.0](https://aws.amazon.com/blogs/security/how-to-implement-a-general-solution-for-federated-apicli-access-using-saml-2-0/ "https://aws.amazon.com/blogs/security/how-to-implement-a-general-solution-for-federated-apicli-access-using-saml-2-0/")
- PowerShell:
  [How to Set Up Federated API Access to AWS by Using Windows PowerShell](https://aws.amazon.com/blogs/security/how-to-set-up-federated-api-access-to-aws-by-using-windows-powershell/ "https://aws.amazon.com/blogs/security/how-to-set-up-federated-api-access-to-aws-by-using-windows-powershell/")

### Script configuration

1. Using Notepad++, change the default region to the correct region
2. Using Notepad++, disable SSL verification for test and dev environments
3. Using Notepad++, configure idpentryurl

`https://[ADFS-FDQN]/adfs/ls/IdpInitiatedSignOn.aspx?loginToRp=urn:amazon:webservices`

### Windows configuration

The instructions below are for the python packages. The credentials generated will be valid for 1 hour.

1.  [Download and install python (2.7.11)](https://www.python.org/downloads/ "https://www.python.org/downloads/")
2.  [Download and install AWS CLI tools](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/")
3.  Install the AMS CLI:
    1. Download the AMS distributables zip file provided by your cloud service delivery manager (CSDM) and unzip.

    Several directories and files are made available. 2. Open either the **Managed Cloud Distributables -> CLI -> Windows** or the **Managed Cloud Distributables -> CLI -> Linux / MacOS**
    directory, depending on your operating system, and:

    For **Windows**, execute the appropriate installer (this method only works on Windows 32 or 64 bits systems):

        * 32 Bits: ManagedCloudAPI\_x86.msi
        * 64 Bits: ManagedCloudAPI\_x64.msi

    For **Mac/Linux**, execute the file named: **MC_CLI.sh**. You can do this by running this command: `sh MC_CLI.sh`.
    Note that the **amscm** and **amsskms** directories and their contents must be in the same directory as the **MC_CLI.sh** file. 3. If your corporate credentials are used via federation with AWS (the AMS default configuration) you must install a credential
    management tool that can access your federation service. For example, you can use this AWS Security Blog
    [How to Implement Federated API and CLI Access Using SAML 2.0 and AD FS](https://blogs.aws.amazon.com/security/post/Tx1LDN0UBGJJ26Q/How-to-Implement-Federated-API-and-CLI-Access-Using-SAML-2-0-and-AD-FS "https://blogs.aws.amazon.com/security/post/Tx1LDN0UBGJJ26Q/How-to-Implement-Federated-API-and-CLI-Access-Using-SAML-2-0-and-AD-FS") for help configuring your credential management tooling. 4. After the installation, run `aws amscm help` and `aws amsskms help` to see commands and options.

4.  Download the required SAML script

Download to c:\aws\scripts 5. [Download PIP](https://bootstrap.pypa.io/get-pip.py "https://bootstrap.pypa.io/get-pip.py")

Download to c:\aws\downloads 6. Using PowerShell, install PIP

<pythondir>.\python.exe c:\aws\downloads\get-pip.py 7. Using PowerShell, install boto module

<pythondir\scripts>pip install boto 8. Using PowerShell, install requests module

<pythondir\scripts>pip install requests 9. Using PowerShell, install requests security module

<pythondir\scripts>pip install requests[security] 10. Using PowerShell, install beautifulsoup module

<pythondir\scripts>pip install beautifulsoup4 11. Using PowerShell, create a folder called .aws in the users profile (%userprofile%\.aws)

mkdir .aws 12. Using PowerShell, create a credential file in the .aws folder

New-Item credentials -type file –force

The credentials file mustn’t have a file extension

The filename must be all lowercase and have the name credentials 13. Open the credentials file with notepad and paste in the following data, specifying the correct region

```

[default]
output = json
region = us-east-1
aws_access_key_id =
aws_secret_access_key =

```

14. Using PowerShell, the SAML script and logon

<pythondir>.\python.exe c:\aws\scripts\samlapi.py

Username: [USERNAME]@upn

Choose the role you would like to assume

### Linux configuration

The credentials generated will be valid for 1 hour.

1. Using WinSCP, transfer the SAML script
2. Using WinSCP, transfer the Root CA certificate (ignore for test and dev)
3. Add the ROOT CA to the trusted root certificates (ignore for test and dev)

$ openssl x509 -inform der -in [certname].cer -out certificate.pem (ignore for test and dev)

Add contents of certificate.pem to end of /etc/ssl/certs/ca-bundle.crt file ((ignore for test dev) 4. Create .aws folder in home/ec2-user 5

```

[default]
output = json
region = us-east-1
aws_access_key_id =
aws_secret_access_key =

```

5. Using WinSCP, transfer the credentials file to .aws folder
6. Install boto module

$ sudo pip install boto 7. Install requests module

$ sudo pip install requests 8. Install beautifulsoup module

$ sudo pip install beautifulsoup4 9. Copy the script to home/ec2-user

Set the required permissions

Execute the script: samlapi.py
