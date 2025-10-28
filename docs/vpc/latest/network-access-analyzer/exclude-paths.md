# Exclusion conditions in Network Access Analyzer

A Network Access Scope produces findings only for paths that match at least one match
condition, but do not match any exclusion conditions.

An exclusion condition can contain source, destination, and through fields. Each field is
optional, but you must specify at least one field. Each source and destination can include a
resource statement, a packet header statement, or both.

A through entry contains exactly one element that contains a resource statement. It excludes
paths that contain the specified network component anywhere along the path, not just at the
beginning or end. You can use a through entry in combination with a source, a destination, or
both a source and a destination.
