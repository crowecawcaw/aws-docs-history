

# Limitations and notes for the Twenty CRM connector

The following are limitations and notes for the Twenty CRM connector:
+ Twenty CRM is supported as a source only. Writing to Twenty CRM is not supported.
+ Job bookmarks are not supported.
+ Twenty CRM applies a rate limit of 100 requests per minute.
+ When you do not set `SELECTED_FIELDS`, Twenty CRM returns a default set of up to 200 fields for an object that has more than 200 readable fields. Set `SELECTED_FIELDS` to read any field beyond that default set.