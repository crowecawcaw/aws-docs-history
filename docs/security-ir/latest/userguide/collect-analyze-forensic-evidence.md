# Collect and analyze forensic evidence

Forensics, as mentioned in the [Preparation](preparation.md "preparation.md") section of this document, is the
process of collecting and analyzing artifacts during incident response. On AWS, it is
applicable to infrastructure domain resources such as network traffic packet captures,
operating system memory dump, and for service domain resources such as AWS CloudTrail logs.

The forensics process has the following fundamental characteristics:

- **Consistent** – It follows the exact steps documented,
  without deviations.
- **Repeatable** – It produces the exact same results when
  repeated against the same artifact.
- **Customary** – It’s publicly documented and widely
  adopted.

It is important to maintain a chain of custody for artifacts collected during incident response.
Using automation and having automatic documentation of this collection generated can help,
in addition to storing the artifacts in read-only repositories. Analysis should only be
performed on exact replicas of the collected artifacts to maintain integrity.
