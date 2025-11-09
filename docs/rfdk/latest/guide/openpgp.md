# OpenPGP keys for the RFDK

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

This topic contains the OpenPGP key for the RFDK. This key is used to code-sign the bundles that are published to the RFDK GitHub releases.

## RFDK OpenPGP key

|                 |                                                                                                                 |
| --------------- | --------------------------------------------------------------------------------------------------------------- |
| Key ID          | 0x83279914D7C7367B                                                                                              |
| Type            | RSA                                                                                                             |
| Size            | 4096/4096                                                                                                       |
| Created         | 2024-10-23                                                                                                      |
| Expires         | 2028-10-22                                                                                                      |
| User ID         | AWS Render Farm Deployment Kit <[aws-rfdk@amazon.com](mailto:aws-rfdk@amazon.com "mailto:aws-rfdk@amazon.com")> |
| Key fingerprint | 7348 7BEE 7A43 90F4 8758 8EA3 8327 9914 D7C7 367B                                                               |

Select the "Copy" icon to copy the following OpenPGP key:

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

mQINBGcZLoYBEAClsY/NFxMjT9C33HFzVCb/GwyE9VUcy22ZhobqWmMIvN8/lmwh
C9KS2oDX/4oq1k8QpYVZ5/ahkHk54wLkGaTljNI4//FvVmh+J8TJQWu7oqLfviIy
JqrgD5kEBjzdOHGf3rGbLbCADP9/+KTfnVvfVkzRNCJajdXbYp8+Ne830d4DpQkf
WWCbIlFDaMcEfFqsBbVP440rPsG3NQR3gOVX3u0c1mR9+mUI3HLaUHMWEkm+lqES
gTLVhXR1jis1EEyPzu9ukwojllcgcAK+5Z/NpEeESvpq0AFcE20HuIGjZ73PLWKE
h+A1TAvaVFxaxETXcxj/BtDrXQkwueyAEanEQ+2soYB0G6jBLj9qzm6UVb3Q0oKd
90rxsGm9adWnd1H3MgfkfWM7CKKeUk4W10Gs9dJXmkljYjuozcMG/y5dLQTbVKV+
KNwllilEthdsWDh2VNOsjcEQ3x3O1TYUnn1DbLGilf6raHjCKN3vAL5+YGx3zqzv
LhIz4stcEjfUy3fy4i2ID11LIm0+9BIZB7vFEGJMPySOB8zJaioXwlhnym/aidL5
DEpfg4f86xXG9GgvAYxVYw5xIdhLTp5b5OepRKushVZHTDuluNblLa7JHnjAmWrZ
mBcBYdKlRb1CHZAeQItozVdfN+xQKhhTVnI+Dnt7GyhqS49JlFHGSC7T1wARAQAB
tDRBV1MgUmVuZGVyIEZhcm0gRGVwbG95bWVudCBLaXQgPGF3cy1yZmRrQGFtYXpv
bi5jb20+iQJXBBMBCABBFiEEc0h77npDkPSHWI6jgyeZFNfHNnsFAmcZLoYCGy8F
CQeEzgAFCwkIBwICIgIGFQoJCAsCBBYCAwECHgcCF4AACgkQgyeZFNfHNnvSjhAA
jhxdxLtzhc5QtdV3k29nygcyv4bCJDGnH7yaOkcTlxacgTj4VKLFClvNZ9vES3Ch
wuyB52Qf91FvzxpCQXESOSR1Igf4dvrjvlhcZFQA/58N0/HZH5pb8JbfoGebgCGY
sCZlKIl/sqhmrIreaYK7ZleG3jg6jv5bZx2pD9weCvfBJYZWf4xSjZHa/an1GES2
VxOe4K4dCYtJN3osi71wOrmb0QHB8hJgIIz98a74fa9xDzeQN1DCFv2Yyk0ch8fp
+eTqstkRk24h51JMJxCBYhBroAYcNrP2VLI6JbHavY4H69gxDlm7jqpNlLztLTZU
TMbnPAPxI21IE2cKhCK3ksXqn9iYqKjAs0++Bv0iX4M0pcNALo5SvlfqgoR3GukB
r9CTbDmLCWU4YCkJs7JDeC8lmiN6cBiwKY8IlzIkfDQclzM6xD7w+FBNZAw0SGFT
nTMlTATG22FgLtiEX/nzQKx5BNsQS1XxP1BhJ/BWFobcpYIUjY8HyuhzxUUo6zJg
y85DuNTCeYslcrRIxPC0i1WkyZPtB3kz+fJMXCUmMurIRSBsynkCIyIfsW3IVO8k
TVy8OK9xxFZZcveetQBH9YDzeIO62ZBezHBUbq//gkkA0sU5UUHoDS4Ksecqmfu0
dN+TZKTNlkvaUJXrZjN4eUB3UFQ7mjXE02WRXcsNm8Q=
=7/KB
-----END PGP PUBLIC KEY BLOCK-----
```

## Verifying the integrity of GitHub release downloads

Each RFDK GitHub release will include both a release bundle asset (aws-rfdk-<VERSION>.zip) and a corresponding signature file (`aws-rfdk-<VERSION>.zip.sig`).

These instructions are written for Linux and assume you have a recent version of OpenPGP installed. To verify the release bundle asset, you will need to:

Import the RFDK OpenPGP key:

```
# Import RFDK's OpenPGP key
gpg --import --armor <<EOF
-----BEGIN PGP PUBLIC KEY BLOCK-----

mQINBGcZLoYBEAClsY/NFxMjT9C33HFzVCb/GwyE9VUcy22ZhobqWmMIvN8/lmwh
C9KS2oDX/4oq1k8QpYVZ5/ahkHk54wLkGaTljNI4//FvVmh+J8TJQWu7oqLfviIy
JqrgD5kEBjzdOHGf3rGbLbCADP9/+KTfnVvfVkzRNCJajdXbYp8+Ne830d4DpQkf
WWCbIlFDaMcEfFqsBbVP440rPsG3NQR3gOVX3u0c1mR9+mUI3HLaUHMWEkm+lqES
gTLVhXR1jis1EEyPzu9ukwojllcgcAK+5Z/NpEeESvpq0AFcE20HuIGjZ73PLWKE
h+A1TAvaVFxaxETXcxj/BtDrXQkwueyAEanEQ+2soYB0G6jBLj9qzm6UVb3Q0oKd
90rxsGm9adWnd1H3MgfkfWM7CKKeUk4W10Gs9dJXmkljYjuozcMG/y5dLQTbVKV+
KNwllilEthdsWDh2VNOsjcEQ3x3O1TYUnn1DbLGilf6raHjCKN3vAL5+YGx3zqzv
LhIz4stcEjfUy3fy4i2ID11LIm0+9BIZB7vFEGJMPySOB8zJaioXwlhnym/aidL5
DEpfg4f86xXG9GgvAYxVYw5xIdhLTp5b5OepRKushVZHTDuluNblLa7JHnjAmWrZ
mBcBYdKlRb1CHZAeQItozVdfN+xQKhhTVnI+Dnt7GyhqS49JlFHGSC7T1wARAQAB
tDRBV1MgUmVuZGVyIEZhcm0gRGVwbG95bWVudCBLaXQgPGF3cy1yZmRrQGFtYXpv
bi5jb20+iQJXBBMBCABBFiEEc0h77npDkPSHWI6jgyeZFNfHNnsFAmcZLoYCGy8F
CQeEzgAFCwkIBwICIgIGFQoJCAsCBBYCAwECHgcCF4AACgkQgyeZFNfHNnvSjhAA
jhxdxLtzhc5QtdV3k29nygcyv4bCJDGnH7yaOkcTlxacgTj4VKLFClvNZ9vES3Ch
wuyB52Qf91FvzxpCQXESOSR1Igf4dvrjvlhcZFQA/58N0/HZH5pb8JbfoGebgCGY
sCZlKIl/sqhmrIreaYK7ZleG3jg6jv5bZx2pD9weCvfBJYZWf4xSjZHa/an1GES2
VxOe4K4dCYtJN3osi71wOrmb0QHB8hJgIIz98a74fa9xDzeQN1DCFv2Yyk0ch8fp
+eTqstkRk24h51JMJxCBYhBroAYcNrP2VLI6JbHavY4H69gxDlm7jqpNlLztLTZU
TMbnPAPxI21IE2cKhCK3ksXqn9iYqKjAs0++Bv0iX4M0pcNALo5SvlfqgoR3GukB
r9CTbDmLCWU4YCkJs7JDeC8lmiN6cBiwKY8IlzIkfDQclzM6xD7w+FBNZAw0SGFT
nTMlTATG22FgLtiEX/nzQKx5BNsQS1XxP1BhJ/BWFobcpYIUjY8HyuhzxUUo6zJg
y85DuNTCeYslcrRIxPC0i1WkyZPtB3kz+fJMXCUmMurIRSBsynkCIyIfsW3IVO8k
TVy8OK9xxFZZcveetQBH9YDzeIO62ZBezHBUbq//gkkA0sU5UUHoDS4Ksecqmfu0
dN+TZKTNlkvaUJXrZjN4eUB3UFQ7mjXE02WRXcsNm8Q=
=7/KB
-----END PGP PUBLIC KEY BLOCK-----
EOF
```

Determine whether to trust the RFDK GPG key. Some factors to consider when deciding whether or not to trust the above key are:

- The internet connection you’ve used to obtain the GPG key from this website is secure;
- The device that you are accessing this website on is secure; and
- AWS has taken measures to secure the hosting of the OpenPGP public key on this site.

If you have decided to trust the RFDK GPG key, then run:

```
gpg --edit-key 0x83279914D7C7367B
gpg (GnuPG) 2.0.22; Copyright (C) 2013 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.


pub  4096R/D7C7367B  created: 2024-10-23  expires: 2028-10-22  usage: SCEA
                     trust: unknown       validity: unknown
[ unknown] (1). AWS Render Farm Deployment Kit <aws-rfdk@amazon.com>

gpg> trust
pub  4096R/D7C7367B  created: 2024-10-23  expires: 2028-10-22  usage: SCEA
                     trust: unknown       validity: unknown
[ unknown] (1). AWS Render Farm Deployment Kit <aws-rfdk@amazon.com>

Please decide how far you trust this user to correctly verify other users' keys
(by looking at passports, checking fingerprints from different sources, etc.)

  1 = I don't know or won't say
  2 = I do NOT trust
  3 = I trust marginally
  4 = I trust fully
  5 = I trust ultimately
  m = back to the main menu

Your decision? 5

pub  4096R/D7C7367B  created: 2024-10-23  expires: 2028-10-22  usage: SCEA
                     trust: ultimate      validity: unknown
[ unknown] (1). AWS Render Farm Deployment Kit <aws-rfdk@amazon.com>

gpg> quit
```

Finally, verify the signature:

```
$ gpg --verify aws-rfdk-1.5.0.zip.sig aws-rfdk-1.5.0.zip
gpg: Signature made Tue 10 Dec 2024 05:14:20 PM UTC using RSA key ID D7C7367B
gpg: Good signature from "AWS Render Farm Deployment Kit <aws-rfdk@amazon.com>" [unknown]
```

###### Warning

If GPG outputs an error about an incorrect signature, it is possible that the release bundle asset was tampered with or corrupted. If this occurs, please contact AWS
support for assistance.

## Historical RFDK OpenPGP keys

The below key may be used to validate releases of RFDK before RFDK version 1.5.0.

|                 |                                                                                                                 |
| --------------- | --------------------------------------------------------------------------------------------------------------- |
| Key ID          | 0x3717B1A67981EAE3                                                                                              |
| Type            | RSA                                                                                                             |
| Size            | 4096/4096                                                                                                       |
| Created         | 2020-08-13                                                                                                      |
| Expires         | 2024-08-12                                                                                                      |
| User ID         | AWS Render Farm Deployment Kit <[aws-rfdk@amazon.com](mailto:aws-rfdk@amazon.com "mailto:aws-rfdk@amazon.com")> |
| Key fingerprint | 5E9E FC5E CDD1 F793 3C49 5746 3717 B1A6 7981 EAE3                                                               |

Select the "Copy" icon to copy the following OpenPGP key:

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v2

mQINBF81nw0BEADX2iMDKbBEDoI9BSpfmgbuXJBED55fNhm8BuLxBbFEFkGJBg0U
MzxZvZxmAvRFmXBf8tDcACPOaf4odAuLpdfCh9anE6K8bgXn0C+mrE5GVd+EpT11
wVcM1QvWSGl8lms2pRBMUX4bP6G/vtYKHtJ2mBO+BUBzXMl+jUfjwzddLYLhbYJr
ayQneakNfGWGEUawNOTR13m7YMZhPAPd1qrgXfT4BlnYfwqE+Nqkz0iTi6L3X072
GyHXvq4so2Z0/NlUQZWWT8uX2bI5xWllpMGeCD/D4dtOF+1qJiTCEOQKmxwyoOsa
qWoWZCHXkUtlEORdSk1ks8ojGCkugnvI+lmwaJYe14oSHBuSMcd5gh7kfGug0RSj
b0jHVvNFv/lks0qNUUGr+2yXCP6fVmIKqHWC/K1Ewff0NkMZqvF/4snfSeBlpOcp
gCAm/DK2BaaSWnA9ma90EyauHJUMILZe3N89CIy4xeBUCzPN8Z51kGNCVSxFrICs
BWiz5SwcKS6mdm72WXhsxyet9X7IVUCK1WmDxEoYhknInS8fWYJ+/6RQwwy9mkoO
Vep4Cu+xlL3UJ9j0uSNEMnwpoxnxyNtB9IerqFaUwYEFtMZtb7nQy3rN05V9BsZj
Zv2pNwnQrihdS+Be2GZNwDGulfBQygRxra0tPxLrDCTVDY1Xn1Tr4GpLiQARAQAB
tDRBV1MgUmVuZGVyIEZhcm0gRGVwbG95bWVudCBLaXQgPGF3cy1yZmRrQGFtYXpv
bi5jb20+iQI/BBMBAgApBQJfNZ8NAhsvBQkHhM4ABwsJCAcDAgEGFQgCCQoLBBYC
AwECHgECF4AACgkQNxexpnmB6uNXoRAAuprgrhzOB5rheenqtT9Qb0Ij6IISd9WD
jFLwNlihZ1XvSqWRxguk9xAeGn4GScTGcUERXzyTIeYVP8WKMhgYJb63q1p6X2Mz
D7sIeRXoVB1voXBjOCnXAXnVPsO8kFzeB7LK3P+d6Bc3np+oYkqDmpmHJfC60ybb
YFLEatX4uCFMj+Be5W0xHzcp+GXgdtyXHZhljXBuTqLhbWiHfCBsOQoL+NVZ6EvE
xC2TnG1xYisk2I4FsJfPFIM3NvRzV9Q7AxOsQOJqd8oIWoxPGROKbYcnTZNUGxK0
gKkhUNqB6dTEq5P4UOuCxFsNmFeegu3UqKepdTuG2p75nZl26t1ndvwpiJzKu1p/
S1B6eSZQi3Rb4NHNgiNHP2/c705SXRd0KGGOXz1sB0Hm8dl8XUxHoEekCbhZm3vy
PIgz5jTaoBn28MW7Nf4ZY8zqnhn28sNhUdTtsB/fXJuW6iCLZUtGJ8qTycZerZrn
3H76+0HNQoZMJQauRrbnTnHyB1ltIGyhrgc08nV/wiTKwAo4tFVUaUJMZIr/xKgx
m35NXBjI/hxxStKCs0fBUY+lhywh1Q5qtJAmNrhMj9hJF3WCLIpdDbuthhovUa0o
+HbVUD4bqZKVrwxkkZ/yG8yqOi/R4dLY4Vkr9c/r/8wwOqBF+osexGcqzikyBakk
OFJdWUAoRF8=
=UcZE
-----END PGP PUBLIC KEY BLOCK-----
```
