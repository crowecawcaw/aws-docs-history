# Transfer files to a Linux instance using SCP

One way to transfer files between your local computer and a Linux instance is to use
the secure copy protocol (SCP). SCP is a good option for simple operations, such as
as one-time file copies. SCP secures files transfers using the same .pem file that
you use to connect to an instance using SSH. If you need to keep files synchronized,
or if the files are large, **rsync** is faster and more efficient
than SCP. For security, use **rsync** over SSH, as **rsync**
transfers data using plain text by default.

Before you connect to your Linux instance using SCP, complete the following tasks:

- Complete the general prerequisites.
  - Check that your instance has passed its status checks.
    It can take a few minutes for an instance to be ready to accept connection requests.
    For more information, see [View status checks](viewing_status.md "viewing_status.md").
  - [Get the required instance details](connection-prereqs-general.md#connection-prereqs-get-info-about-instance "connection-prereqs-general.md#connection-prereqs-get-info-about-instance").
  - [Locate the private key and set permissions](connection-prereqs-general.md#connection-prereqs-private-key "connection-prereqs-general.md#connection-prereqs-private-key").
  - [(Optional) Get the instance fingerprint](connection-prereqs-general.md#connection-prereqs-fingerprint "connection-prereqs-general.md#connection-prereqs-fingerprint").

- Allow inbound SSH traffic from your IP address.

Ensure that the security group associated with your instance allows incoming SSH
traffic from your IP address. For more information, see [Rules to connect to instances from your computer](security-group-rules-reference.md#sg-rules-local-access "security-group-rules-reference.md#sg-rules-local-access").

- Install an SCP client.

Most Linux, Unix, and Apple computers include an SCP client by default. If
yours doesn't, the OpenSSH project provides a free implementation of the full
suite of SSH tools, including an SCP client. For more information, see [https://www.openssh.com](https://www.openssh.com "https://www.openssh.com").
The following procedure steps you through using SCP to transfer a file using the
instance's public DNS name, or the IPv6 address if your instance has one.

###### To use SCP to transfer files between your computer and your instance

1. Determine the location of the source file on your computer and the destination
   path on the instance. In the following examples, the name of the private key
   file is `key-pair-name.pem`, the file to transfer is
   `my-file.txt`, the username for the instance is
   ec2-user, the public DNS name of the instance is
   `instance-public-dns-name`, and the IPv6 address of the
   instance is `2001:db8::1234:5678:1.2.3.4`.
   - (Public DNS) To transfer a file to the destination on the instance,
     enter the following command from your computer.

   ```
   scp -i `/path/key-pair-name`.pem `/path/my-file.txt` `ec2-user`@`instance-public-dns-name`:`path/`
   ```

   - (IPv6) To transfer a file to the destination on the instance if the
     instance has an IPv6 address, enter the following command from your
     computer. The IPv6 address must be enclosed in square brackets (`[
]`), which must be escaped (`\`).

   ```
   scp -i `/path/key-pair-name`.pem `/path/my-file.txt` `ec2-user`@\[`2001:db8::1234:5678:1.2.3.4`\]:`path/`
   ```

2. If you haven't already connected to the instance using SSH, you see a response
   like the following:

```
The authenticity of host 'ec2-198-51-100-1.compute-1.amazonaws.com (10.254.142.33)'
can't be established.
RSA key fingerprint is 1f:51:ae:28:bf:89:e9:d8:1f:25:5d:37:2d:7d:b8:ca:9f:f5:f1:6f.
Are you sure you want to continue connecting (yes/no)?
```

(Optional) You can optionally verify that the fingerprint in the security
alert matches the instance fingerprint. For more information, see [(Optional) Get the instance fingerprint](connection-prereqs-general.md#connection-prereqs-fingerprint "connection-prereqs-general.md#connection-prereqs-fingerprint").

Enter `yes`. 3. If the transfer is successful, the response is similar to the
following:

```
Warning: Permanently added 'ec2-198-51-100-1.compute-1.amazonaws.com' (RSA)
to the list of known hosts.
my-file.txt                                100%   480     24.4KB/s   00:00
```

4. To transfer a file in the other direction (from your Amazon EC2 instance to your
   computer), reverse the order of the host parameters. For example, you can
   transfer `my-file.txt` from your EC2 instance to the a
   destination on your local computer as `my-file2.txt`, as
   shown in the following examples.
   - (Public DNS) To transfer a file to a destination on your computer,
     enter the following command from your computer.

   ```
   scp -i `/path/key-pair-name`.pem `ec2-user`@`instance-public-dns-name`:`path/my-file.txt path/my-file2.txt`
   ```

   - (IPv6) To transfer a file to a destination on your computer if the
     instance has an IPv6 address, enter the following command from your
     computer. The IPv6 address must be enclosed in square brackets (`[
]`), which must be escaped (`\`).

   ```
   scp -i `/path/key-pair-name`.pem `ec2-user`@\[`2001:db8::1234:5678:1.2.3.4`\]:`path/my-file.txt path/my-file2.txt`
   ```
