# Export an AWS Certificate Manager public

certificate

The following procedures walks you through how you can export an ACM public
certificate in the ACM console. Alternatively, you can use the [`export-certificate`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/export-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/export-certificate.html") AWS CLI or [ExportCertificate](../APIReference/API_ExportCertificate.md "../APIReference/API_ExportCertificate.md")
API action.

###### Note

ACM public certificates created prior to June 17, 2025 cannot be exported.

## Export a public certificate (console)

1. Sign in to the AWS Management Console and open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/ "https://console.aws.amazon.com/acm/").
2. Choose **List certificates** and select the checkbox of
   the certificate you want to export.
   1. Alternatively, you can select the certificate. In the certificate
      detail page, select **Export**.

3. Choose **More actions** and then choose
   **Export**.
4. Enter and confirm a passphrase for the private key.
5. You can download or copy the certificate files.

###### Note

In the ACM console, you’re able to export .pem certificate files.
You can convert the .pem file to another file format, like .ppk. For
more information, see this [re:Post article](https://repost.aws/knowledge-center/ec2-ppk-pem-conversion "https://repost.aws/knowledge-center/ec2-ppk-pem-conversion").

## Export a public certificate (AWS CLI)

Use the [`export-certificate`](../../../cli/latest/reference/acm/export-certificate.md "../../../cli/latest/reference/acm/export-certificate.md") AWS CLI command or [ExportCertificate](../APIReference/API_ExportCertificate.md "../APIReference/API_ExportCertificate.md") API action to export a public certificate and private
key. You must assign a passphrase when you run the command. For added security, use
a file editor to store your passphrase in a file, and then supply the passphrase by
supplying the file. This prevents your passphrase from being stored in the command
history and prevents others from seeing the passphrase as you type it in.

###### Note

The file containing the passphrase must not end in a line terminator. You can
check your password file like this:

```
$ file -k passphrase.txt
passphrase.txt: ASCII text, with no line terminators
```

The following examples pipe the command output to `jq` to apply PEM
formatting.

````
[Windows/Linux]$ aws acm export-certificate \
    --certificate-arn arn:aws:acm:us-east-1:`111122223333`:certificate/`certificate_ID` \
    --passphrase fileb://path-to-passphrase-file  \
| jq -r '"\(.Certificate)\(.CertificateChain)\(.PrivateKey)"' ``` This outputs a base64-encoded, PEM-format certificate, also containing the certificate chain and encrypted private key, as in the following abbreviated example. ``` -----BEGIN CERTIFICATE----- MIIDTDCCAjSgAwIBAgIRANWuFpqA16g3IwStE3vVpTwwDQYJKoZIhvcNAQELBQAw EzERMA8GA1UECgwIdHJvbG9sb2wwHhcNMTkwNzE5MTYxNTU1WhcNMjAwODE5MTcx NTU1WjAXMRUwEwYDVQQDDAx3d3cuc3B1ZHMuaW8wggEiMA0GCSqGSIb3DQEBAQUA ... 8UNFQvNoo1VtICL4cwWOdLOkxpwkkKWtcEkQuHE1v5Vn6HpbfFmxkdPEasoDhthH FFWIf4/+VOlbDLgjU4HgtmV4IJDtqM9rGOZ42eFYmmc3eQO0GmigBBwwXp3j6hoi 74YM+igvtILnbYkPYhY9qz8h7lHUmannS8j6YxmtpPY= -----END CERTIFICATE----- -----BEGIN CERTIFICATE----- MIIC8zCCAdugAwIBAgIRAM/jQ/6h2/MI1NYWX3dDaZswDQYJKoZIhvcNAQELBQAw EzERMA8GA1UECgwIdHJvbG9sb2wwHhcNMTkwNjE5MTk0NTE2WhcNMjkwNjE5MjA0 NTE2WjATMREwDwYDVQQKDAh0cm9sb2xvbDCCASIwDQYJKoZIhvcNAQEBBQADggEP ... j2PAOviqIXjwr08Zo/rTy/8m6LAsmm3LVVYKLyPdl+KB6M/+H93Z1/Bs8ERqqga/ 6lfM6iw2JHtkW+q4WexvQSoqRXFhCZWbWPZTUpBS0d4/Y5q92S3iJLRa/JQ0d4U1 tWZyqJ2rj2RL+h7CE71XIAM//oHGcDDPaQBFD2DTisB/+ppGeDuB -----END CERTIFICATE----- -----BEGIN ENCRYPTED PRIVATE KEY----- MIIFKzBVBgkqhkiG9w0BBQ0wSDAnBgkqhkiG9w0BBQwwGgQUMrZb7kZJ8nTZg7aB 1zmaQh4vwloCAggAMB0GCWCGSAFlAwQBKgQQDViroIHStQgNOjR6nTUnuwSCBNAN JM4SG202YPUiddWeWmX/RKGg3lIdE+A0WLTPskNCdCAHqdhOSqBwt65qUTZe3gBt ... ZGipF/DobHDMkpwiaRR5sz6nG4wcki0ryYjAQrdGsR6EVvUUXADkrnrrxuHTWjFl wEuqyd8X/ApkQsYFX/nhepOEIGWf8Xu0nrjQo77/evhG0sHXborGzgCJwKuimPVy Fs5kw5mvEoe5DAe3rSKsSUJ1tM4RagJj2WH+BC04SZWNH8kxfOC1E/GSLBCixv3v +Lwq38CEJRQJLdpta8NcLKnFBwmmVs9OV/VXzNuHYg== -----END ENCRYPTED PRIVATE KEY----- ``` To output everything to a file, append the `>` redirect to the previous example, yielding the following command: ``` $ aws acm export-certificate \ --certificate-arn arn:aws:acm:us-east-1:`111122223333`:certificate/`certificate_ID` \ --passphrase fileb://path-to-passphrase-file \
| jq -r '"\(.Certificate)\(.CertificateChain)\(.PrivateKey)"' \ > /tmp/export.txt ```
````
