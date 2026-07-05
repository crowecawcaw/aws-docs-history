Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SHOW VIEW

Shows the definition of a view, including for materialized views and late-binding views.
You can use the output of the SHOW VIEW statement to recreate the view.

## Syntax

```
SHOW VIEW [*schema\_name*.]*view\_name*
```

## Parameters

_schema\_name_

(Optional) The name of the related schema.

_view\_name_

The name of the view to show.

## Examples

Following is the view definition for the view `LA_Venues_v`.

```
create view LA_Venues_v as select * from venue where venuecity='Los Angeles';
```

Following is an example of the SHOW VIEW command and output for the view defined
preceding.

```
show view LA_Venues_v;
```

```
SELECT venue.venueid,
venue.venuename,
venue.venuecity,
venue.venuestate,
venue.venueseats
FROM venue WHERE ((venue.venuecity)::text = 'Los Angeles'::text);
```

Following is the view definition for the view `public.Sports_v` in the
schema `public`.

```
create view public.Sports_v as select * from category where catgroup='Sports';
```

Following is an example of the SHOW VIEW command and output for the view defined
preceding.

```
show view public.Sports_v;
```

```
SELECT category.catid,
category.catgroup,
category.catname,
category.catdesc
FROM category WHERE ((category.catgroup)::text = 'Sports'::text);
```
