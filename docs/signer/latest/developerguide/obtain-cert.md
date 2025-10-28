# Obtain and import a code-signing certificate

Before you can use AWS Signer with AWS IoT Device Management or Amazon FreeRTOS, you must have or
obtain a code-signing certificate. Code-signing certificates typically contain a
`Digital Signature` value in the `Key Usage` extension and
a `Code Signing` value in the `Extended Key Usage`
extension.

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 4111 (0x100f)
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=US, ST=Washington, L=Seattle, O=Example Company, OU=Corp, CN=www.example.com/emailAddress=corp@www.example.com
        Validity
            Not Before: Nov 14 17:32:30 2017 GMT
            Not After : Nov 14 17:32:30 2018 GMT
        Subject: C=US, ST=Washington, L=Seattle, O=Example Company, OU=corp, CN=www.example.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:ac:96:8f:64:1a:4d:5c:cc:e4:50:a9:19:f3:c1:
                    03:8f:1a:db:f5:15:18:65:fb:6e:3f:84:ae:02:9e:
                    a2:e1:62:40:05:10:b6:35:59:63:c7:b3:17:4a:e1:
                    12:9f:29:42:e4:2b:bb:83:db:b1:cd:42:83:0a:9f:
                    70:ca:81:6a:9b:58:1d:4e:a0:69:04:bc:0b:f4:7e:
                    34:fc:af:79:f1:31:6c:7e:a5:eb:b1:85:9e:5e:ef:
                    df:34:7c:aa:13:01:f5:cc:ee:a1:9c:d9:4d:17:e8:
                    c8:8b:d0:77:2e:80:3f:7e:41:ea:84:2f:11:22:59:
                    bd:fa:90:eb:26:ec:e7:b2:0e:9d:ce:b5:8a:a0:b9:
                    17:4c:8b:3a:b5:28:61:eb:d3:a6:ed:db:5c:26:e6:
                    7d:af:33:b6:9f:f0:9d:fb:fc:10:e0:52:cb:60:5c:
                    08:c3:33:4a:b4:8a:4e:3a:54:4e:43:3d:b9:f2:5e:
                    4e:89:95:c2:a5:df:88:a2:24:71:d3:ee:b3:ef:0b:
                    18:1d:55:54:16:ff:9b:95:6e:ae:71:d3:f2:d1:7e:
                    f2:8b:67:34:f8:11:fe:ab:8f:6b:88:c3:b9:8e:1d:
                    07:bc:62:27:45:7e:0c:a0:7b:ef:bf:26:f8:50:df:
                    ac:d8:8f:a5:ed:fe:9f:ee:20:dc:a6:33:3e:94:25:
                    ce:67
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints:
                CA:FALSE
            X509v3 Subject Key Identifier:
                22:93:86:26:D3:1B:32:1C:79:1B:5C:E4:EB:2A:6A:DB:77:87:D7:FB
            X509v3 Authority Key Identifier:
                keyid:0D:CE:76:F2:E3:3B:93:2D:36:05:41:41:16:36:C8:82:BC:CB:F8:A0
            X509v3 Key Usage:
                Digital Signature
            X509v3 Extended Key Usage:
                Code Signing
    Signature Algorithm: sha256WithRSAEncryption
         38:41:ba:c3:f0:88:97:3e:a1:0f:e3:d4:55:d6:d0:a2:4e:ac:
         da:83:67:27:49:23:88:9b:20:e1:e1:b7:55:78:3c:5a:9b:7a:
         75:ee:3a:0f:ed:20:4e:23:31:29:ac:07:91:61:f1:86:75:08:
         fa:f5:3c:4a:7b:79:3c:39:a5:45:97:10:5c:f4:a0:04:af:e8:
         5b:ca:d1:a5:ce:14:dc:14:c6:54:b1:ba:6a:2c:52:2c:2f:07:
         52:8a:a7:00:97:c7:ee:65:bb:df:36:7f:53:d0:7d:a4:6e:ba:
         bb:d2:d4:b5:25:bb:b1:0d:bd:91:10:28:e1:34:df:79:01:78:
         45:4e
```

###### Important

We recommend that you purchase a code-signing certificate from a company with
a good reputation for security. Do not use a self-signed certificate for any
purpose other than testing. Encouraging your users to trust arbitrary
certificates with no reputational backing is a poor security practice.

After you have obtained the certificate, you must import it into AWS Certificate Manager
(ACM). ACM returns an Amazon Resource Name (ARN) for the certificate. You must
use the ARN when you call the [StartSigningJob](signer/latest/api/API_StartSigningJob.md "signer/latest/api/API_StartSigningJob.md") action. For more information about importing, see
[Importing Certificates](../../../acm/latest/userguide/import-certificate.md "../../../acm/latest/userguide/import-certificate.md")
in the AWS Certificate Manager User Guide.
