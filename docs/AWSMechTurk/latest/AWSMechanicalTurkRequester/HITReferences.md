# HIT references using `RequesterAnnotation`

When building processes that leverage Amazon Mechanical Turk (Mechanical Turk), it's often valuable to keep track
of identifiers associated with the data in each HIT, particularly when handling HIT responses
via notifications. For example, you might want to associate your HITs with a record in a
database such as Amazon DynamoDB, and want your HIT to reference the primary key of the record.

The `RequesterAnnotation` attribute is a useful option for tracking these
references. When you create a HIT using `CreateHIT` or `CreateHITWithHITType`, you can provide a `RequesterAnnotation`
field that contains arbitrary data about each HIT. Although it is limited to 255 ASCII
characters, this is generally adequate to capture identifiers that denote the origin of your
data. The data provided here is only visible to the requester who created the HIT.

When you receive a notification that a HIT has been completed, you can use the
`GetHIT` operation to retrieve the `RequesterAnnotation`. The
identifier captured in the `RequesterAnnotation` can then be used to make updates
in your database or other systems.
