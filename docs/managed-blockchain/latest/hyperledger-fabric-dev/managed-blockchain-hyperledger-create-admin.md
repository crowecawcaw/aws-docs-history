# Register and Enroll a

Hyperledger Fabric Admin

Only identities who are admins within a Hyperledger Fabric member can install
and query chaincode.

Creating an admin in Hyperledger Fabric is a three-step process.

1. You _register_ the identity with the Hyperledger Fabric CA.
   Registering stores the user name and password in the CA database as an admin.
2. After you register, you _enroll_ the identity. This sends the
   CA a Certificate Signing Request (CSR). The CA validates that the identity is registered
   and otherwise valid, and returns a signed certificate. The certificate is stored in the
   Hyperledger Fabric client machine's local Membership Service Provider (MSP).
3. You then copy the certificate to the `admincerts` subdirectory, and the certificate
   validates the role of the identity as an admin. Similarly, the CA updates the local MSP
   for the member's peer nodes and the ordering service so that the admin is recognized.

For more information, see [Fabric CA User's Guide](https://hyperledger-fabric-ca.readthedocs.io/en/release-1.4/users-guide.html "https://hyperledger-fabric-ca.readthedocs.io/en/release-1.4/users-guide.html") and [Membership](https://hyperledger-fabric.readthedocs.io/en/release-2.2/membership/membership.html "https://hyperledger-fabric.readthedocs.io/en/release-2.2/membership/membership.html") in Hyperledger Fabric documentation.

When you first create a member in a Hyperledger Fabric network on AMB Access, you specify the member's first user. AMB Access
registers the identity of this user automatically with the Hyperledger Fabric CA. This is called a
_bootstrap identity_. Even though the identity is registered, the remaining steps need to be performed. The identity must then enroll itself as an
admin and certificates must be updated. After the steps are complete, the identity can install
chaincode and can be used to enroll additional identities as admins.

After you enroll an identity as an admin, it may take a minute or two until the identity is able to use the admin certificate to perform tasks.

###### Important

AMB Access does not support revoking user certificates. After an admin is created,
the admin persists for the life of the member.

To register and enroll an identity as an admin, you must have the following:

- The member CA endpoint
- The user name and password either of the bootstrap identity or of an admin
  with permissions to register and enroll identities
- A valid certificate file and the path to the MSP directory of your identity,
  which will register the new administrator

## Registering an

Admin

The following example uses a [Fabric-CA Client CLI](https://hyperledger-fabric-ca.readthedocs.io/en/release-1.4/clientcli.html "https://hyperledger-fabric-ca.readthedocs.io/en/release-1.4/clientcli.html")
`register` command to register an admin with these options:

- `--url` specifies the endpoint of the CA along with an existing
  user name of an admin with permissions to register, such as the bootstrap
  identity. The example uses a user name of `Example-AdminUser`
  with password `Example-Password123`.
- `--id.name` and `--id.secret` parameters establish
  the user name and password for the new admin.
- `--id.type` is set to `user` and
  `--id.affiliation` is set to the member name to which the
  admins belong. The example member name is `org1`.
- `--id.attrs` is set to `'hf.admin=true'`. This is a
  property specific to AMB Access that registers the identity as an admin.
- The `--tls.certfiles` option specifies the location and file
  name of the AMB Access TLS certificate that you copied from Amazon S3 (see [Step 5.1: Create the Certificate File](get-started-enroll-admin.md#get-started-enroll-member-create-cert "get-started-enroll-admin.md#get-started-enroll-member-create-cert")).
- `--mspdir` specifies the MSP directory on the local machine
  where certificates are saved. The example uses
  `/home/ec2-user/admin-msp`.

```
fabric-ca-client register \
–-url https://`Example-AdminUser`:`Example-Password123`@`ca.m-K46ICRRXJRCGRNNS4ES4XUUS5A.n-MWY63ZJZU5HGNCMBQER7IN6OIU.managedblockchain.`us-east-1`.amazonaws.com:30002` \
--id.name `AdminUser2` --id.secret `Password456` \
–-id.type user --id.affiliation `org1` \
--id.attrs ‘hf.Admin=true’ --tls.certfiles `/home/ec2-user/managedblockchain-tls-chain.pem` \
--mspdir `/home/ec2-user/admin-msp`
```

## Enrolling an Admin

After registering an identity as an admin, or creating a member along with the bootstrap identity, you can use the [Fabric-CA Client CLI](https://hyperledger-fabric-ca.readthedocs.io/en/release-1.4/clientcli.html "https://hyperledger-fabric-ca.readthedocs.io/en/release-1.4/clientcli.html")
`enroll` command to enroll that identity as an admin. This is shown in
the following example using these options:

- `-u` (an alternative for `--url`) specifies the
  endpoint of the CA along with the user name and password of the identity that you
  are enrolling.
- `tls.certfiles` specifies the location and file name of the
  AMB Access TLS certificate that you copied from Amazon S3 (see [Step 5.1: Create the Certificate File](get-started-enroll-admin.md#get-started-enroll-member-create-cert "get-started-enroll-admin.md#get-started-enroll-member-create-cert")).
- `-M` (an alternative for `--mspdir`) specifies the
  MSP directory on the local machine where certificates are saved. The example
  uses `/home/ec2-user/admin-msp`.

```
fabric-ca-client enroll \
-u https://`Example-AdminUser`:`Example-Password123`@`ca.m-K46ICRRXJRCGRNNS4ES4XUUS5A.n-MWY63ZJZU5HGNCMBQER7IN6OIU.managedblockchain.`us-east-1`.amazonaws.com:30002` \
--tls.certfiles /home/ec2-user/managedblockchain-tls-chain.pem \
-M `/home/ec2-user/admin-msp`
```

## Copying the Admin

Certificate

After you enroll the admin, copy the certificates from the `signcerts`
directory to the `admincerts` directory as shown in the following
example. The MSP directory `/home/ec2-user/admin-msp` is used in the
example, and the example assumes that you are running the command in the
`/home/ec2-user` directory.

```
cp -r admin-msp/signcerts admin-msp/admincerts
```
