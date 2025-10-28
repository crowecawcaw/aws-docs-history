# Configuring a job with a C2PA manifest

To include a C2PA manifest in your MP4 output, you need to configure your job settings
with the necessary parameters for signing and embedding the manifest.

To include a C2PA manifest in an MP4 output by using the MediaConvert console:

1. In the **Output groups** section, add a **File**
   output group.
2. In **Output settings**, set **Container** to
   **MPEG-4 container**.
3. Expand **MPEG-4 container settings**.
4. For **C2PA manifest**, choose
   **Include**.
5. For **Certificate secret**, enter the name or ARN of the Secrets Manager secret that contains your C2PA public certificate chain in PEM format.
6. For **Signing KMS key**, enter the ID or ARN of the AWS KMS key used to sign the C2PA manifest.
   To include a C2PA manifest by using the API, SDK, or AWS Command Line Interface (AWS CLI), include the
   following in your MP4 container settings. Replace the example ARNs of the
   **Certificate secret** and **Signing KMS key** with
   your ARNs:

```
...
    "OutputGroups": [{
        "Name": "File Group",
        "OutputGroupSettings": {
            "Type": "FILE_GROUP_SETTINGS",
            "FileGroupSettings": {}
        },
        "Outputs": [{
            "VideoDescription": {...},
            "AudioDescriptions": [...],
            "ContainerSettings": {
                "Container": "MP4",
                "Mp4Settings": {
                    "C2paManifest": "INCLUDE",
                    "CertificateSecret": "arn:aws:secretsmanager:us-west-2:111122223333:secret:c2pa-certificate-abc123",
                    "SigningKmsKey": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
                }
            }
        }]
    }]
...
```
