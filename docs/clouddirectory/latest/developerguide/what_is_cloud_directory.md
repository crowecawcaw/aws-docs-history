Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").
 

# What Is Amazon Cloud Directory?

Amazon Cloud Directory is a highly available multi-tenant directory-based store in AWS.
 These directories scale automatically to hundreds of millions of objects as needed for
 applications. This lets operations staff focus on developing and deploying applications that
 drive the business, not managing directory infrastructure. Unlike traditional directory systems,
 Cloud Directory does not limit organizing directory objects in a single fixed hierarchy. 

With Cloud Directory, you can organize directory objects into multiple hierarchies to
 support many organizational pivots and relationships across directory information. For example,
 a directory of users may provide a hierarchical view based on reporting structure, location, and
 project affiliation. Similarly, a directory of devices may have multiple hierarchical views
 based on its manufacturer, current owner, and physical location.

At its core, Cloud Directory is a specialized graph-based directory store that provides a
 foundational building block for developers. With Cloud Directory, developers can do the
 following:


* Create directory-based applications easily and without having to worry about
 deployment, global scale, availability, and performance
* Build applications that provide user and group management, permissions or policy
 management, device registry, customer management, address books, and application or
 product catalogs
* Define new directory objects or extend existing types to meet their application needs,
 reducing the code they need to write
* Reduce the complexity of layering applications on top of Cloud Directory
* Manage the evolution of schema information over time, ensuring future compatibility
 for consumers
Cloud Directory includes a set of API operations to access various objects and policies
 stored in your Cloud Directory-based directories. For a list of available operations, see [Amazon Cloud Directory API Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md"). For a list of operations and the permissions
 required to perform each API action, see [Amazon Cloud Directory API Permissions: Actions, Resources, and Conditions
 Reference](iam_auth_access_usingwith_iam_resourcepermissions.md "iam_auth_access_usingwith_iam_resourcepermissions.md").

For a list of supported Cloud Directory regions, see the [AWS
 Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#clouddirectory_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#clouddirectory_region") documentation. For additional resources, see [Cloud Directory Resources](resources.md "resources.md"). 


## What Cloud Directory Is Not


Cloud Directory is not a directory service for IT Administrators who want to manage or
 migrate their directory infrastructure.
