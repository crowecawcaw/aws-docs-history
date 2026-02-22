# Prepare to bring your IP address range to your AWS account:

Authorization

To ensure that only you can bring your IP address space to Amazon, we require two authorizations:

- You must authorize Amazon to advertise the IP address range.
- You must provide proof that you own the IP address range and so have the authority
  to bring it to AWS.

###### Note

When you use BYOIP to bring an IP address range to AWS, you can't transfer ownership of that
address range to a different account or company while we're advertising it. You also can't
directly transfer an IP address range from one AWS account to another account. To transfer
ownership or to transfer between AWS accounts, you must deprovision the address range,
and then the new owner must follow the steps to add the address range to their AWS account.
To authorize Amazon to advertise the IP address range, you provide Amazon with a signed
authorization message. Use a Route Origin Authorization (ROA) to provide this
authorization. A ROA is a cryptographic statement about your route announcements that
you create through your Regional Internet Registry (RIR). A ROA contains the IP address
range, the Autonomous System Numbers (ASN) that are allowed to advertise the IP address
range, and an expiration date. The ROA authorizes Amazon to advertise an IP address
range under a specific Autonomous System (AS).

A ROA does not authorize your AWS account to bring the IP address range to AWS. To
provide this authorization, you must publish a self-signed X.509 certificate in the
Registry Data Access Protocol (RDAP) remarks for the IP address range. The certificate
contains a public key, which AWS uses to verify the authorization-context signature that
you provide. Keep your private key secure and use it to sign the authorization-context
message.

The following sections provide detailed steps for completing these authorization tasks. The
commands in these steps are supported on Linux. If you use Windows, you can access the
[Windows
Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about "https://docs.microsoft.com/en-us/windows/wsl/about") to run Linux commands.

## Steps to provide authorization

- [Step 1: Create a ROA object](#using-byoip.prepare-steps-1 "#using-byoip.prepare-steps-1")
- [Step 2: Create a self-signed X.509 certificate](#using-byoip.prepare-steps-2 "#using-byoip.prepare-steps-2")
- [Step 3: Create a signed authorization message](#using-byoip.prepare-steps-3 "#using-byoip.prepare-steps-3")

## Step 1: Create a ROA object

Create a ROA object to authorize Amazon ASN 16509 to advertise your IP address range
as well as the ASNs that are currently authorized to advertise the IP
address range. The ROA must contain the /24 IP address that you want to bring to AWS
and you must set the maximum length to /24.

For more information about creating a ROA request, see the following sections, depending
on where you registered your IP address range:

- ARIN: [ROA Requests](https://www.arin.net/resources/rpki/roarequest.html "https://www.arin.net/resources/rpki/roarequest.html")
- RIPE: [Managing ROAs](https://www.ripe.net/manage-ips-and-asns/resource-management/certification/resource-certification-roa-management "https://www.ripe.net/manage-ips-and-asns/resource-management/certification/resource-certification-roa-management")
- APNIC: [Route Management](https://www.apnic.net/wp-content/uploads/2017/01/route-roa-management-guide.pdf "https://www.apnic.net/wp-content/uploads/2017/01/route-roa-management-guide.pdf")

## Step 2: Create a self-signed X.509 certificate

Create a key pair and a self-signed X.509 certificate, and then add the certificate to the
RDAP record for your RIR. The following steps describe how to perform these tasks.

###### Note

The `openssl` commands in these steps require OpenSSL
version 1.0.2 or later.

## To create and add an X.509

certificate

1. Generate an RSA 2048-bit key pair using the following command.

```
openssl genrsa -out private.key 2048
```

2. Create a public X.509 certificate from the key pair using the following command.

```
openssl req -new -x509 -key private.key -days 365 | tr -d "\n" > publickey.cer
```

In this example, the certificate expires in 365 days, after which time it can’t be trusted.
When you run the command, make sure that you set the `–days` option to the desired value for
the correct expiration. When you're prompted for other information, you can accept the default values. 3. Update the RDAP record for your RIR with the X.509 certificate by using the following steps, depending
on your RIR.

    1. View your certificate using the following command.



    ```
    cat publickey.cer
    ```
    2. Add the certificate that you previously created to the RDAP record for your RIR.
     Be sure to include the `-----BEGIN CERTIFICATE-----` and `-----END
     CERTIFICATE-----` strings before and after the encoded portion. All of
     this content must be on a single, long line. The procedure for updating RDAP depends
     on your RIR:




    	* For ARIN, use the [Account Manager
    	 portal](https://account.arin.net/public/secure/dashboard "https://account.arin.net/public/secure/dashboard") to add the certificate in the "Public Comments" section
    	 for the "Network Information" object representing your address range. Do not
    	 add it to the comments section for your organization.
    	* For RIPE, add the certificate as a new "descr" field to the "inetnum" or
    	 "inet6num" object representing your address range. These can usually be
    	 found in the "My Resources" section of the [RIPE
    	 Database portal](https://apps.db.ripe.net/db-web-ui/myresources/overview "https://apps.db.ripe.net/db-web-ui/myresources/overview"). Do not add it to the comments section for your
    	 organization or the "remarks" field of the above objects.
    	* For APNIC, email the certificate to [helpdesk@apnic.net](mailto:helpdesk@apnic.net "mailto:helpdesk@apnic.net") to manually add it to the "remarks" field
    	 for your address range. Send the email using the APNIC authorized contact
    	 for the IP addresses.
    You can remove the certificate from your RIR's record after the provisioning stage
     below has been completed.

## Step 3: Create a signed authorization message

Create the signed authorization message to allow Amazon to advertise your IP address range.

The format of the message is as follows, where the `YYYYMMDD` date is the
expiration date of the message.

```
1|aws|`aws-account`|`address-range`|`YYYYMMDD`|SHA256|RSAPSS
```

## To create the signed

authorization message

1. Create a plaintext authorization message and store it in a variable named
   `text_message`, as the following example shows. Replace the
   example account number, IP address range, and expiration date with your own
   values.

```
text_message="1|aws|`123456789012`|`203.0.113.0/24`|`20191201`|SHA256|RSAPSS"
```

2. Sign the authorization message in `text_message` using the key pair that you created in the
   previous section.
3. Store the message in a variable named `signed_message`, as the following example shows.

```
signed_message=$(echo $text_message | tr -d "\n" | openssl dgst -sha256 -sigopt
						rsa_padding_mode:pss -sigopt rsa_pss_saltlen:-1 -sign private.key -keyform PEM | openssl base64 |
						tr -- '+=/' '-_~' | tr -d "\n")
```
