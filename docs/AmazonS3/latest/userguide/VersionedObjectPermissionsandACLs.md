# Configuring versioned object

permissions

Permissions for objects in Amazon S3 are set at the version level. Each version has its own
object owner. The AWS account that creates the object version is the owner. So, you
can set different permissions for different versions of the same object. To do so, you
must specify the version ID of the object whose permissions you want to set in a
`PUT Object versionId acl` request. For a detailed description and
instructions on using ACLs, see [Identity and Access Management for Amazon S3](security-iam.md "security-iam.md").

###### Example— Setting permissions for an object version

The following request sets the permission of the grantee with canonical user ID `b4bf1b36f9716f094c3079dcf5ac9982d4f2847de46204d47448bc557fb5ac2a`, to `FULL_CONTROL` on the
key, `my-image.jpg`, version ID,
`3HL4kqtJvjVBH40Nrjfkd`.

```
PUT /my-image.jpg?acl&versionId=3HL4kqtJvjVBH40Nrjfkd HTTP/1.1
Host: bucket.s3.amazonaws.com
Date: Wed, 28 Oct 2009 22:32:00 GMT
Authorization: AWS AKIAIOSFODNN7EXAMPLE:0RQf4/cRonhpaBX5sCYVf1bNRuU=
Content-Length: 124

<AccessControlPolicy>
  <Owner>
    <ID>75cc57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a</ID>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
        <ID>a9a7b886d6fd24a52fe8ca5bef65f89a64e0193f23000e241bf9b1c61be666e9</ID>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
  </AccessControlList>
  </AccessControlPolicy>
```

Likewise, to get the permissions of a specific object version, you must specify its
version ID in a `GET Object versionId acl` request. You need to include the
version ID because, by default, `GET Object acl` returns the permissions of
the current version of the object.

###### Example— Retrieving the permissions for a specified object version

In the following example, Amazon S3 returns the permissions for the key,
`my-image.jpg`, version ID,
`DVBH40Nr8X8gUMLUo`.

```
GET /my-image.jpg?versionId=DVBH40Nr8X8gUMLUo&acl HTTP/1.1
Host: bucket.s3.amazonaws.com
Date: Wed, 28 Oct 2009 22:32:00 GMT
Authorization: AWS AKIAIOSFODNN7EXAMPLE:0RQf4/cRonhpaBX5sCYVf1bNRuU
```

For more information, see [GetObjectAcl](../API/RESTObjectGETacl.md "../API/RESTObjectGETacl.md") in the _Amazon Simple Storage Service API Reference_.
