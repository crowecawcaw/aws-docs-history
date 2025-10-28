# Managing your

Tape Gateway

Managing your gateway includes tasks such as configuring cache storage and upload buffer
space, working with virtual
tapes, and doing general maintenance. If you haven't created a gateway, see
[Getting started with AWS Storage Gateway](GettingStarted.md "GettingStarted.md").

Following, you can find information about how to manage your Tape Gateway
resources.

**Topics**

- [Editing Basic Gateway Information](edit-gateway-information.md "edit-gateway-information.md") - Learn how to use the Storage Gateway console to edit basic information for an existing
  gateway, including the gateway name, time zone, and CloudWatch log group.
- [Managing Automatic Tape
  Creation](managing-automatic-tape-creation.md "managing-automatic-tape-creation.md") - Learn how to configure
  Tape Gateway to create new virtual tapes automatically to maintain the minimum
  number of available tapes that you specify.
- [Archiving Virtual Tapes](archiving-tapes-vtl.md "archiving-tapes-vtl.md") - Learn
  how to configure archival of your tapes to either the S3 Glacier Flexible Retrieval or
  S3 Glacier Deep Archive storage class when you create a new tape.
- [Moving tapes to S3 Glacier Deep Archive
  storage class](moving-tapes-vtl.md "moving-tapes-vtl.md") - Learn how to
  move your tapes from S3 Glacier Flexible Retrieval to S3 Glacier Deep Archive
  for long-term data retention and digital preservation at a very low cost.
- [Retrieving Archived Tapes](retrieving-archived-tapes-vtl.md "retrieving-archived-tapes-vtl.md") - Learn how to access data
  stored on an archived virtual tape by first retrieving the tape to your
  Tape Gateway.
- [Viewing tape usage statistics](tape-usage.md "tape-usage.md") - Learn how to view the
  amount of data stored on a tape using the Storage Gateway console.
- [Deleting virtual tapes from your
  Tape Gateway](deleting-tapes-vtl.md "deleting-tapes-vtl.md") - Learn
  how to delete virtual tapes from your Tape Gateway by using the Storage Gateway
  console.
- [Deleting Custom Tape Pools](deleting-tape-pools-vtl.md "deleting-tape-pools-vtl.md")

* Learn how to delete a custom tape pool using the Storage Gateway console.

- [Deactivating Your Tape Gateway](disabling-gateway-vtl.md "disabling-gateway-vtl.md") -
  Learn how to deactivate a Tape Gateway if the gateway has failed and you want to
  recover the tapes from the failed gateway to another gateway.
- [Understanding Tape Status](understand-tapes-status.md "understand-tapes-status.md")

* Learn about the various tape status values that Storage Gateway reports to help determine
  whether a tape is functioning normally, or if there is a problem that might require
  action on your part.

- [Moving your data to a new gateway](migrate-data.md "migrate-data.md") - Learn how to move
  data between gateways as your data and performance needs grow, or if you receive an
  AWS notification to migrate your gateway.
