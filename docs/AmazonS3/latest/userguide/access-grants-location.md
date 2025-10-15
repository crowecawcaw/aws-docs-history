# Working with S3 Access Grants locations

After you [create an Amazon S3 Access Grants
 instance](access-grants-instance-create.md "access-grants-instance-create.md") in an AWS Region in your account, you register an S3 location in that
 instance. An S3 Access Grants location maps the default S3 location (`s3://`), a bucket, or a prefix to an AWS Identity and Access Management (IAM) role. S3 Access Grants assumes this IAM role to vend temporary credentials to the grantee that is accessing that particular location. You must first register at least one location in your S3 Access Grants instance before you can create an access grant. 

You can register a location, view a location's details, edit a location, and delete a location.

###### Note


 After you register the first location in your S3 Access Grants instance, your instance still does not have any individual access grants in it. To create an access grant, see [Create grants](access-grants-grant-create.md "access-grants-grant-create.md").
 

###### Topics

* [Register a location](access-grants-location-register.md "access-grants-location-register.md")
* [View the details of a registered location](access-grants-location-view.md "access-grants-location-view.md")
* [Update a registered location](access-grants-location-edit.md "access-grants-location-edit.md")
* [Delete a registered location](access-grants-location-delete.md "access-grants-location-delete.md")
