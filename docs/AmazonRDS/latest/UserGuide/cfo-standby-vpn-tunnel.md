# Configuring a VPN tunnel between RDS Custom for Oracle primary and replica instances

A VPN tunnel is an encrypted connection between two or more devices over a network. To
ensure the highest level of security for your Oracle Data Guard instances in RDS Custom for Oracle,
we strongly recommend that you implement a VPN tunnel to encrypt communication between
your primary and standby instances. The tunnel serves as a safeguard for sensitive data
as it travels the network between instances. While this configuration is optional, we
recommend it as a best practice to achieve data security and regulatory compliance.

Make sure you meet the following prerequisites:

- You have root access to the primary and standby hosts.
- You have the technical expertise to run the `ipsec` command.

###### To configure a VPN tunnel between a primary and replica in RDS Custom for Oracle

1. Add the security groups for both the primary instance and standby instance to
   the allow list using the following rules:

```
ACTION FLOW SOURCE PROTO PORT

ALLOW ingress this-SG 50 (ESP) all (N/A)
ALLOW egress this-SG 50 (ESP) all (N/A)

ALLOW ingress this-SG 17 (UDP) 500 (IKE)
ALLOW egress this-SG 17 (UDP) 500 (IKE)
```

2. Switch to the root user.

```
$ sudo su – root
```

3. Run the following commands on both the primary instance and the standby
   instance to initialize the Network Security Services (NSS) database under the
   user `root`.

```
ipsec initnss --nssdir /etc/ipsec.d
```

4. Generate RSA keys as follows:
   1. On the primary instance, generate the keys using either of the
      following `ipsec` commands, depending on your OS
      version.

   ```
   ipsec newhostkey --nssdir /etc/ipsec.d       ## for Oracle Linux Version 8
   ipsec newhostkey --output /etc/ipsec.secrets ## for Oracle Linux version 7.9
   ```

   2. Obtain the public key, which you need to create the configuration. In
      the following example, the primary instance is `left` because
      in `ipsec` parlance, `left` refers to the device
      you are currently configuring, and `right` refers to the
      device at the other end of the tunnel.

   ```
   ipsec showhostkey --left --ckaid `ckaid-returned-in-last-statement`
   ```

   3. On the standby instance, generate keys for the standby instance.

   ```
   ipsec newhostkey --nssdir /etc/ipsec.d       ## for Oracle Linux Version 8
   ipsec newhostkey --output /etc/ipsec.secrets ## for Oracle Linux version 7.9
   ```

   4. Obtain the public key for the standby instance, which you need to
      create the configuration. In the following example, the standby instance
      is `right` because it refers to the device at the other end
      of the tunnel.

   ```
   ipsec showhostkey --right --ckaid `ckaid-returned-in-last-statement`
   ```

5. Based on the RSA keys that you obtained, generate the configuration. The
   configuration is identical for both the primary instance and the standby
   instance. You can find the primary instance IPv4 address and standby instance
   IPv4 address in the AWS console.

On both the primary instance and the standby instance, save the following
configuration to the file
`/etc/ipsec.d/custom-fb-tunnel.conf`.

```
conn custom-db-tunnel
 type=transport
 auto=add
 authby=rsasig
 left=`IPV4-for-primary`
 leftrsasigkey=`RSA-key-generated-on-primary`
 right=`IPV4-for-standby`
 rightrsasigkey=`RSA-key-generated-on-standby`
```

6. On both the primary instance and the standby instance, start the
   `ipsec` daemon on both hosts.

```
ipsec setup start
```

7. Start the tunnel on either the primary instance or the standby instance. The
   output should look similar to the following.

```
[root@ip-172-31-6-81 ~]# ipsec auto --up custom-db-tunnel
181 "custom-db-tunnel" #1: initiating IKEv2 connection
181 "custom-db-tunnel" #1: sent IKE_SA_INIT request to 172.31.32.196:500
182 "custom-db-tunnel" #1: sent IKE_AUTH request {cipher=AES_GCM_16_256 integ=n/a prf=HMAC_SHA2_512 group=DH19}
003 "custom-db-tunnel" #1: initiator established IKE SA; authenticated peer '3584-bit PKCS#1 1.5 RSA with SHA1' signature using preloaded certificate '172.31.32.196'
004 "custom-db-tunnel" #2: initiator established Child SA using #1; IPsec transport [172.31.6.81-172.31.6.81:0-65535 0] -> [172.31.32.196-172.31.32.196:0-65535 0] {ESP/ESN=>0xda9c4815 <0xb742ca42 xfrm=AES_GCM_16_256-NONE DPD=passive}
[root@ip-172-31-6-81 ~]#
```
