**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Amazon Pinpoint segments

When you create a campaign, you choose a _segment_
to send that campaign to. A segment is a group of your customers that share certain attributes.
For example, a segment might contain all of your customers who use version 2.0 of your app on an
Android device, or all customers who live in the city of Los Angeles. You can send multiple campaigns to a single segment, and you can send
a single campaign to multiple segments.

###### Note

We recommend you use data from all segments you import, and delete segment data from a
project you no longer need. For example, you can [delete endpoints programmatically](../developerguide/audience-define-remove.md "../developerguide/audience-define-remove.md") to remove unutilized
segment data. Accumulating segment data within a project may cause delays in subsequent
import processes.

There are two types of segments that you can create in Amazon Pinpoint:

- Dynamic segments – Segments that are based on
  attributes that you define. Dynamic segments can change over time. For example, if
  you add new endpoints to Amazon Pinpoint, or if you modify or delete existing endpoints, the
  number of endpoints in that segment may increase or decrease. For more information
  about dynamic segments, see [Building segments](segments-building.md "segments-building.md").
- Imported segments – Segments that are created outside
  of Amazon Pinpoint and saved in CSV or JSON format. When you create an imported segment, you
  upload your files to Amazon Simple Storage Service (Amazon S3). Amazon Pinpoint retrieves the files from Amazon S3 and
  creates new endpoints based on the contents of those files. Imported segments are
  static—they never change. To make changes, you must reimport the segment with
  those changes. When you create a new segment, you can use an imported segment as a
  base segment, and then refine it by adding filters. For more information about
  importing segments, see [Importing segments](segments-importing.md "segments-importing.md").
