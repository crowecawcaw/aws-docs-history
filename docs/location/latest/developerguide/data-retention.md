# Data retention in Amazon Location

The following characteristics relate to how Amazon Location collects and stores data for the
service:

- **Amazon Location Service Trackers** – When you use the
  Trackers APIs to track the location of entities, their coordinates can be
  stored. Device locations are stored for 30 days before being deleted by the
  service.
- **Amazon Location Service Geofences** – When you use the
  Geofences APIs to define areas of interest, the service stores the geometries
  you provided. They must be explicitly deleted.

###### Note

Deleting your AWS account delete all resources within it. For additional
information, see the [AWS Data
Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/").
