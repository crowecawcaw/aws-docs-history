# Prerequisites: Steps you have to complete before you can upload data with DSBulk

You must complete the following tasks before you can start this tutorial.

1.  If you have not already done so, sign up for an AWS account by following the
    steps at [Setting up AWS Identity and Access Management](accessing.md#SettingUp.IAM "accessing.md#SettingUp.IAM").
2.  Create credentials by following the steps at [Create and configure AWS credentials for Amazon Keyspaces](access.md "access.md").
3.  Create a JKS trust store file.
    1.  Download the following digital certificates and save
        the files locally or in your home directory.

            1. AmazonRootCA1
            2. AmazonRootCA2
            3. AmazonRootCA3
            4. AmazonRootCA4
            5. Starfield Class 2 Root (optional – for backward compatibility)

        To download the certificates, you can use the following commands.

    ```
    curl -O https://www.amazontrust.com/repository/AmazonRootCA1.pem
    curl -O https://www.amazontrust.com/repository/AmazonRootCA2.pem
    curl -O https://www.amazontrust.com/repository/AmazonRootCA3.pem
    curl -O https://www.amazontrust.com/repository/AmazonRootCA4.pem
    curl -O https://certs.secureserver.net/repository/sf-class2-root.crt
    ```

    ###### Note

    Amazon Keyspaces previously used TLS certificates anchored to the Starfield Class 2 CA.
    AWS is migrating all AWS Regions to certificates issued under Amazon Trust Services (Amazon Root CAs 1–4).
    During this transition, configure clients to trust both Amazon Root CAs 1–4 and the Starfield root to ensure compatibility across all Regions. 2. Convert the digital certificates into trustStore files and add them to the keystore.

    ```
    openssl x509 -outform der -in AmazonRootCA1.pem -out temp_file.der
    keytool -import -alias amazon-root-ca-1 -keystore cassandra_truststore.jks -file temp_file.der

    openssl x509 -outform der -in AmazonRootCA2.pem -out temp_file.der
    keytool -import -alias amazon-root-ca-2 -keystore cassandra_truststore.jks -file temp_file.der

    openssl x509 -outform der -in AmazonRootCA3.pem -out temp_file.der
    keytool -import -alias amazon-root-ca-3 -keystore cassandra_truststore.jks -file temp_file.der

    openssl x509 -outform der -in AmazonRootCA4.pem -out temp_file.der
    keytool -import -alias amazon-root-ca-4 -keystore cassandra_truststore.jks -file temp_file.der

    openssl x509 -outform der -in sf-class2-root.crt -out temp_file.der
    keytool -import -alias cassandra -keystore cassandra_truststore.jks -file temp_file.der
    ```

    In the last step, you need to create a password for the keystore and trust each
    certificate. The interactive command looks like this.

    ```
    `Enter keystore password:
    Re-enter new password:
    Owner: CN=Amazon Root CA 1, O=Amazon, C=US
    Issuer: CN=Amazon Root CA 1, O=Amazon, C=US
    Serial number: 66c9fcf99bf8c0a39e2f0788a43e696365bca
    Valid from: Tue May 26 00:00:00 UTC 2015 until: Sun Jan 17 00:00:00 UTC 2038
    Certificate fingerprints:
     SHA1: 8D:A7:F9:65:EC:5E:FC:37:91:0F:1C:6E:59:FD:C1:CC:6A:6E:DE:16
     SHA256: 8E:CD:E6:88:4F:3D:87:B1:12:5B:A3:1A:C3:FC:B1:3D:70:16:DE:7F:57:CC:90:4F:E1:CB:97:C6:AE:98:19:6E
    Signature algorithm name: SHA256withRSA
    Subject Public Key Algorithm: 2048-bit RSA key
    Version: 3

    Extensions:

    #1: ObjectId: 2.5.29.19 Criticality=true
    BasicConstraints:[
     CA:true
     PathLen:2147483647
    ]

    #2: ObjectId: 2.5.29.15 Criticality=true
    KeyUsage [
     DigitalSignature
     Key_CertSign
     Crl_Sign
    ]

    #3: ObjectId: 2.5.29.14 Criticality=false
    SubjectKeyIdentifier [
    KeyIdentifier [
    0000: 84 18 CC 85 34 EC BC 0C 94 94 2E 08 59 9C C7 B2 ....4.......Y...
    0010: 10 4E 0A 08 .N..
    ]
    ]

    Trust this certificate? [no]: yes
    Certificate was added to keystore
    Enter keystore password:
    Owner: CN=Amazon Root CA 2, O=Amazon, C=US
    Issuer: CN=Amazon Root CA 2, O=Amazon, C=US
    Serial number: 66c9fd29635869f0a0fe58678f85b26bb8a37
    Valid from: Tue May 26 00:00:00 UTC 2015 until: Sat May 26 00:00:00 UTC 2040
    Certificate fingerprints:
     SHA1: 5A:8C:EF:45:D7:A6:98:59:76:7A:8C:8B:44:96:B5:78:CF:47:4B:1A
     SHA256: 1B:A5:B2:AA:8C:65:40:1A:82:96:01:18:F8:0B:EC:4F:62:30:4D:83:CE:C4:71:3A:19:C3:9C:01:1E:A4:6D:B4
    Signature algorithm name: SHA384withRSA
    Subject Public Key Algorithm: 4096-bit RSA key
    Version: 3

    Extensions:

    #1: ObjectId: 2.5.29.19 Criticality=true
    BasicConstraints:[
     CA:true
     PathLen:2147483647
    ]

    #2: ObjectId: 2.5.29.15 Criticality=true
    KeyUsage [
     DigitalSignature
     Key_CertSign
     Crl_Sign
    ]

    #3: ObjectId: 2.5.29.14 Criticality=false
    SubjectKeyIdentifier [
    KeyIdentifier [
    0000: B0 0C F0 4C 30 F4 05 58 02 48 FD 33 E5 52 AF 4B ...L0..X.H.3.R.K
    0010: 84 E3 66 52 ..fR
    ]
    ]

    Trust this certificate? [no]: yes
    Certificate was added to keystore
    Enter keystore password:
    Owner: CN=Amazon Root CA 3, O=Amazon, C=US
    Issuer: CN=Amazon Root CA 3, O=Amazon, C=US
    Serial number: 66c9fd5749736663f3b0b9ad9e89e7603f24a
    Valid from: Tue May 26 00:00:00 UTC 2015 until: Sat May 26 00:00:00 UTC 2040
    Certificate fingerprints:
     SHA1: 0D:44:DD:8C:3C:8C:1A:1A:58:75:64:81:E9:0F:2E:2A:FF:B3:D2:6E
     SHA256: 18:CE:6C:FE:7B:F1:4E:60:B2:E3:47:B8:DF:E8:68:CB:31:D0:2E:BB:3A:DA:27:15:69:F5:03:43:B4:6D:B3:A4
    Signature algorithm name: SHA256withECDSA
    Subject Public Key Algorithm: 256-bit EC (secp256r1) key
    Version: 3

    Extensions:

    #1: ObjectId: 2.5.29.19 Criticality=true
    BasicConstraints:[
     CA:true
     PathLen:2147483647
    ]

    #2: ObjectId: 2.5.29.15 Criticality=true
    KeyUsage [
     DigitalSignature
     Key_CertSign
     Crl_Sign
    ]

    #3: ObjectId: 2.5.29.14 Criticality=false
    SubjectKeyIdentifier [
    KeyIdentifier [
    0000: AB B6 DB D7 06 9E 37 AC 30 86 07 91 70 C7 9C C4 ......7.0...p...
    0010: 19 B1 78 C0 ..x.
    ]
    ]

    Trust this certificate? [no]: yes
    Certificate was added to keystore
    Enter keystore password:
    Owner: CN=Amazon Root CA 4, O=Amazon, C=US
    Issuer: CN=Amazon Root CA 4, O=Amazon, C=US
    Serial number: 66c9fd7c1bb104c2943e5717b7b2cc81ac10e
    Valid from: Tue May 26 00:00:00 UTC 2015 until: Sat May 26 00:00:00 UTC 2040
    Certificate fingerprints:
     SHA1: F6:10:84:07:D6:F8:BB:67:98:0C:C2:E2:44:C2:EB:AE:1C:EF:63:BE
     SHA256: E3:5D:28:41:9E:D0:20:25:CF:A6:90:38:CD:62:39:62:45:8D:A5:C6:95:FB:DE:A3:C2:2B:0B:FB:25:89:70:92
    Signature algorithm name: SHA384withECDSA
    Subject Public Key Algorithm: 384-bit EC (secp384r1) key
    Version: 3

    Extensions:

    #1: ObjectId: 2.5.29.19 Criticality=true
    BasicConstraints:[
     CA:true
     PathLen:2147483647
    ]

    #2: ObjectId: 2.5.29.15 Criticality=true
    KeyUsage [
     DigitalSignature
     Key_CertSign
     Crl_Sign
    ]

    #3: ObjectId: 2.5.29.14 Criticality=false
    SubjectKeyIdentifier [
    KeyIdentifier [
    0000: D3 EC C7 3A 65 6E CC E1 DA 76 9A 56 FB 9C F3 86 ...:en...v.V....
    0010: 6D 57 E5 81 mW..
    ]
    ]

    Trust this certificate? [no]: yes
    Certificate was added to keystore
    Enter keystore password:
    Owner: OU=Starfield Class 2 Certification Authority, O="Starfield Technologies, Inc.", C=US
    Issuer: OU=Starfield Class 2 Certification Authority, O="Starfield Technologies, Inc.", C=US
    Serial number: 0
    Valid from: Tue Jun 29 17:39:16 UTC 2004 until: Thu Jun 29 17:39:16 UTC 2034
    Certificate fingerprints:
     SHA1: AD:7E:1C:28:B0:64:EF:8F:60:03:40:20:14:C3:D0:E3:37:0E:B5:8A
     SHA256: 14:65:FA:20:53:97:B8:76:FA:A6:F0:A9:95:8E:55:90:E4:0F:CC:7F:AA:4F:B7:C2:C8:67:75:21:FB:5F:B6:58
    Signature algorithm name: SHA1withRSA (weak)
    Subject Public Key Algorithm: 2048-bit RSA key
    Version: 3

    Extensions:

    #1: ObjectId: 2.5.29.35 Criticality=false
    AuthorityKeyIdentifier [
    KeyIdentifier [
    0000: BF 5F B7 D1 CE DD 1F 86 F4 5B 55 AC DC D7 10 C2 ._.......[U.....
    0010: 0E A9 88 E7 ....
    ]
    [OU=Starfield Class 2 Certification Authority, O="Starfield Technologies, Inc.", C=US]
    SerialNumber: [ 00]
    ]

    #2: ObjectId: 2.5.29.19 Criticality=false
    BasicConstraints:[
     CA:true
     PathLen:2147483647
    ]

    #3: ObjectId: 2.5.29.14 Criticality=false
    SubjectKeyIdentifier [
    KeyIdentifier [
    0000: BF 5F B7 D1 CE DD 1F 86 F4 5B 55 AC DC D7 10 C2 ._.......[U.....
    0010: 0E A9 88 E7 ....
    ]
    ]


    Warning:
    The input uses the SHA1withRSA signature algorithm which is considered a security risk. This algorithm will be disabled in a future update.

    Trust this certificate? [no]: yes
    Certificate was added to keystore`
    ```

4.  Set up the Cassandra Query Language shell (cqlsh) connection and confirm that
    you can connect to Amazon Keyspaces by following the steps at [Using cqlsh to connect to
    Amazon Keyspaces](programmatic.md "programmatic.md").
5.  Download and install DSBulk.
    1. To download DSBulk, you can use the following code.

    ```
    curl -OL https://downloads.datastax.com/dsbulk/dsbulk-1.8.0.tar.gz
    ```

    2. Then unpack the tar file and add DSBulk to your `PATH` as shown in the following example.

    ```
    tar -zxvf dsbulk-1.8.0.tar.gz
    # add the DSBulk directory to the path
    export PATH=$PATH:./dsbulk-1.8.0/bin
    ```

    3. Create an `application.conf` file to store settings to be used by DSBulk.
       You can save the following example as
       `./dsbulk_keyspaces.conf`. Replace
       `localhost` with the contact point of your local
       Cassandra cluster if you are not on the local node, for example the DNS
       name or IP address. Take note of the file name and path, as you're going to need to specify this later in the `dsbulk load` command.

    ```
    datastax-java-driver {
      basic.contact-points = [ "`localhost`"]
      advanced.auth-provider {
            class = software.aws.mcs.auth.SigV4AuthProvider
            aws-region = `us-east-1`
      }
    }
    ```

    4. To enable SigV4 support, download the shaded `jar` file from [GitHub](https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin/releases/ "https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin/releases/")
       and place it in the DSBulk `lib` folder as shown in the following example.

    ```
    curl -O -L https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin/releases/download/4.0.6-shaded-v2/aws-sigv4-auth-cassandra-java-driver-plugin-4.0.6-shaded.jar
    ```
