# Using tags in AMS

###### Topics

- [AMS infrastructure automatic tagging](ams-auto-tagging.md "ams-auto-tagging.md")
- [AMS recommended tags](ams-tags.md "ams-tags.md")
- [Tag bulk update notes](ams-tags-bu-notes.md "ams-tags-bu-notes.md")
  Providing tags can be of great value. For in-depth information, read
  [Tagging Your Amazon EC2 Resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md").

RFCs that create instances, such as an Amazon S3 bucket or an AWS Elastic Load Balancer (ELB), generally provide a schema that enables
you to add up to seven tags (key/value pairs); you can add more tags to your S3 bucket by submitting a Management | Advanced
stack components | Amazon S3 storage | Update CT. Amazon EC2, Amazon EFS, Amazon RDS, and the multi-tiered (HA
Two-Tiered and HA One-Tiered) schemas allow up to fifty tags. Tags are specified in the
ExecutionParameters part of the schema.

When using the AMS console, you must enable the **Additional configuration** view in order to add tags.

###### Tip

Many CT schemas have a `Description` and `Name`
field near the top of the schema. Those fields are used to name the stack or stack
component, they do not name the resource you are creating. Some schemas offer a
parameter to name the resource you are creating, and some do not. For example, the CT
schema for Create Amazon EC2 stack does not offer a parameter to name the Amazon EC2 instance. In
order to do so, you must create a tag with the key "Name" and the value of what you want
the name to be. If you do not create such a tag, your Amazon EC2 instance displays in the Amazon EC2
console without a name attribute.

Are there tag restrictions? Yes:

- Tags are case sensitive.
- The maximum key length is 128 Unicode characters.
- The maximum value length is 256 Unicode characters.
- The maximum number of tags per resource is 50.
- The reserved prefix is `aws:`.
- AWS-generated tag names and values are automatically assigned the
  `aws:` prefix, which you can't assign. User-defined tag names have the prefix
  `user:` in the cost allocation report.
- Use each key only once for each resource. If you attempt to use the same
  key twice on the same resource, your request is rejected.
- Allowed characters are Unicode letters, white space, numbers, and the
  following special characters: + - = . \_ : /
  Which AWS resource types support tags? See [Now Organize Your AWS Resources by Using up to 50 Tags per Resource](https://aws.amazon.com/blogs/security/now-organize-your-aws-resources-by-using-up-to-50-tags-per-resource/ "https://aws.amazon.com/blogs/security/now-organize-your-aws-resources-by-using-up-to-50-tags-per-resource/").
