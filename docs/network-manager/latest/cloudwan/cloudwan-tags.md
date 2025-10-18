# Network resource attachment tags in AWS Cloud WAN

A tag is a metadata label that either you or AWS assigns to an AWS resource. Each tag
 consists of a key and a value. For tags that you assign, you define the key and the value.
 For example, you might define the key as `purpose` and the value as
 `test` for one resource.

Tags help you do the following:


* Identify and organize your AWS resources. Many AWS services support tagging,
 so you can assign the same tag to resources from different services to indicate that
 the resources are related.
* Control access to your AWS resources. For more information on controlling access
 to resources, see [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html") in the *AWS Identity and Access
 Management User Guide*.
If you are not the core network owner, any attachment tag that you add, modify, or delete
 might require acceptance on the part of the core network owner. These tags can be seen on
 the **Proposed Tags** tab until the time that the core network owner
 accepts or rejects them.


## Supported resources


The following core network resources support tagging:



* Core network
* Core network attachments
* Connect peer

For tagging support resources in Network Manager, see [Resources tags in AWS Global Networks for Transit Gateways](https://docs.aws.amazon.com/network-manager/latest/tgwnm/gnw-tagging.html "https://docs.aws.amazon.com/network-manager/latest/tgwnm/gnw-tagging.html").


###### Topics

* [Add or update a resource attachment tag](cloudwan-tag-proposed.md "cloudwan-tag-proposed.md")
* [Remove a resource attachment tag](cloudwan-tag-remove.md "cloudwan-tag-remove.md")
