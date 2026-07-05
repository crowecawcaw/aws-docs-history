End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](../userguide/SunsetPlan.md "../userguide/SunsetPlan.md").

# What Are AMS Change Types?

Welcome to the AWS Managed Services (AMS) Change Type Reference. Change Types are the method
you use when submitting a request for change (RFC) to indicate what change you want and how it should be implemented.

Change types have a four-part classification scheme: category, subcategory, item, and
operation, "CSIO" for short. The category and subcategory are higher-level concepts, and the item and
operation specify an entity and the operation that is applied to the entity. For example,
the change type that creates an EC2 instance has the classification `Deployment | Advanced
 stack components | EC2 stack | Create`, and the change type that requests administrative
access to that instance has the classification `Management | Access | Stack admin access |
 Grant`. For more information about change types and requests for change (RFCs),
see [Change management](../userguide/change-mgmt.md "../userguide/change-mgmt.md") in the _AMS User Guide_.

This document provides a reference for all of the AMS change types. Any request for
change (RFC) that you submit to AMS requires that you specify a change type. If none of
the existing change types are appropriate for your request, you can use the `Management | Other | Other | Create` or `Management | Other | Other | Update` classifications.

To learn more about using change types, see the following topics in the _AMS User Guide_:

- [Understanding Change Types](../userguide/understanding-cts.md "../userguide/understanding-cts.md")
- [Understanding RFCs](../userguide/create-rfcs.md "../userguide/create-rfcs.md")
  For example walkthroughs of each change type, see the **Additional information** section for the change type,
  [Change Types by Classification](classifications.md "classifications.md").

For a comma-separated value file of change types, open this ZIP file:
[Change type CSV output file (output-12.2023.zip)](samples/output-12.2023.zip.md "samples/output-12.2023.zip.md").

###### Note

At this time, AMS operates in these AWS Regions:
US East (Virginia), US West (N. California), US West (Oregon), US East (Ohio), Canada (Central), South America (São Paulo), EU (Ireland), EU (Frankfurt), EU (London), EU (Paris), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo)

New Regions are added frequently, however all API calls and CLI operations are run out of `us-east-1`. To learn more, see
[AWS Regions and availability zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md").
