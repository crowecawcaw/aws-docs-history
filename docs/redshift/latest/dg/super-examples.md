Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Examples of using semi-structured data in Amazon Redshift

The following examples demonstrate how to work with semi-structured data in Amazon Redshift using PartiQL syntax.
You will create a sample table to load a sample set of semi-structured data,
then query semi-structured data objects in a variety of use cases.

###### Note

We recommend that you set the `enable_case_sensitive_identifier` and `enable_case_sensitive_super_attribute` configuration
options before working with the SUPER data type. For more information, see
[enable_case_sensitive_identifier](r_enable_case_sensitive_identifier.md "r_enable_case_sensitive_identifier.md") and
[enable_case_sensitive_super_attribute](r_enable_case_sensitive_super_attribute.md "r_enable_case_sensitive_super_attribute.md").

## Loading semi-structured data

The following statements create a sample table and load a sample JSON object into the `all_data` SUPER column.

```
DROP TABLE IF EXISTS test_json;

SET enable_case_sensitive_super_attribute TO true;
SET enable_case_sensitive_identifier TO true;

CREATE TABLE test_json (all_data SUPER);

INSERT INTO test_json VALUES (JSON_PARSE('
{
   "data":{
      "pnr":{
         "type":"pnr",
         "pnrid":"123PQRS-2024-09-20",
         "bookingIdentifier":"123PQRS",
         "version":"5",
         "triggerType":"",
         "events":[
            {
               "eventType":"UPDATED",
               "type":"PART",
               "id":"123PQRS-2024-09-20-HO-1"
            },
            {
               "eventType":"CREATED",
               "type":"ABC",
               "id":"123PQRS-2024-09-20-OT-38"
            }
         ],
         "create":{
            "pnrCreateDate":"2024-09-20T16:56:00Z",
            "officeID":"OFFCID1234",
            "officeIDCategory":"Email"
         },
         "lastModification":{
            "dateTime":"2024-09-20T17:09:00Z"
         },
         "PARTDetails":[
            {
               "path":"1",
               "TrainPARTs":[
                  {
                     "PARTID":"123PQRS-2024-09-20-HO-1",
                     "departure":{
                        "departureStation":"XYZ",
                        "departureTimeLocal":"2024-10-03T06:30:00",
                        "departureTimeGMT":"2024-10-03T10:30:00Z"
                     },
                     "arrival":{
                        "arrivalStation":"ABC",
                        "arrivalTimeLocal":"2024-10-03T08:20:00",
                        "arrivalTimeGMT":"2024-10-03T15:20:00Z"
                     },
                     "marketing":{
                        "carrierCode":"XX",
                        "TrainNumber":"100"
                     },
                     "operating":{
                        "carrierCode":"YY",
                        "TrainNumber":"100-A"
                     },
                     "status":"ON",
                     "aircraft":{
                        "code":"222"
                     },
                     "class":"WC",
                     "first":"Y",
                     "seating":[

                     ]
                  }
               ]
            }
         ],
         "commuterInformation":[
            {
               "commuterID":"2",
               "commuterPNR":"123PQRS-2024-09-20-RO-2",
               "commuterTypeCode":"DOM",
               "firstName":"JOHN",
               "lastName":"MILLER"
            }
         ],
         "contactDetail":[
            {
               "emailContacts":[
                  {
                     "id":"123PQRS-2024-09-20-OT-4",
                     "contact":"JOHNMILLER@EXAMPLE.COM",
                     "purpose":[
                        "BUSINESS"
                     ],
                     "commuter":[
                        "123PQRS-2024-09-20-RO-2"
                     ],
                     "language":"EN"
                  },
                  {
                     "id":"123PQRS-2024-09-20-OT-5",
                     "contact":"HARVEYCORMIER@EXAMPLE.COM",
                     "purpose":[
                        "NOTIFICATION"
                     ],
                     "commuter":[
                        "123PQRS-2024-09-20-RO-2"
                     ],
                     "language":"EN"
                  }
               ]
            },
            {
               "phoneContacts":[
                  {
                     "id":"123PQRS-2024-09-20-OT-3",
                     "contact":"1234567890",
                     "purpose":[
                        "NOTIFICATION"
                     ],
                     "commuter":[
                        "123PQRS-2024-09-20-RO-2"
                     ],
                     "language":""
                  }
               ]
            },
            {
               "addressInfo":[
                  {
                     "id":"123PQRS-2024-09-20-OT-6",
                     "addressline":[
                        "112 PORT STREET"
                     ],
                     "provinceState":"CA",
                     "cityName":"SAN JOSE",
                     "postalCode":"12345",
                     "countryCode":"USA",
                     "purpose":[
                        "MAILING"
                     ],
                     "commuter":[
                        "123PQRS-2024-09-20-RO-2"
                     ]
                  }
               ]
            }
         ],
         "PendingService":[
            {
               "id":"123PQRS-2024-09-20-OT-26",
               "code":"MONO",
               "status":"",
               "text":"Broken Seat at Coach-No XYZ123 Seat-No 567",
               "trainCode":"WC-1",
               "TrainsArray":[
                  "123PQRS-2024-09-20-HO-1"
               ],
               "commuter":[
                  "123PQRS-2024-09-20-RO-2"
               ]
            },
            {
               "id":"123PQRS-2024-09-20-OT-27",
               "code":"OTHS",
               "status":"",
               "text":"Broken Seat at Coach-No XYZ567 Seat-No 111",
               "trainCode":"WC-1",
               "TrainsArray":[
                  "123PQRS-2024-09-20-HO-1"
               ],
               "commuter":[
                  "123PQRS-2024-09-20-RO-2"
               ]
            },
            {
               "id":"123PQRS-2024-09-20-OT-28",
               "code":"OTHS",
               "status":"",
               "text":"Broken Seat at Coach-No XYZ890 Seat-No 123",
               "trainCode":"WC-1",
               "TrainsArray":[
                  "123PQRS-2024-09-20-HO-1"
               ],
               "commuter":[
                  "123PQRS-2024-09-20-RO-2"
               ]
            },
            {
               "id":"123PQRS-2024-09-20-OT-29",
               "code":"OTHS",
               "status":"",
               "text":"Broken Seat at Coach-No XYZ111 Seat-No 333",
               "trainCode":"WC-1",
               "TrainsArray":[
                  "123PQRS-2024-09-20-HO-1"
               ],
               "commuter":[
                  "123PQRS-2024-09-20-RO-2"
               ]
            }
         ],
         "parts": [
            {
               "partname": "prop",
               "manufacturer": "local parts co",
               "quality": 2,
               "price": 10.00
            },
            {
               "partname": "prop",
               "manufacturer": "big parts co",
               "quality": null,
               "price": 9.00
            },
            {
               "partname": "prop",
               "manufacturer": "small parts co",
               "quality": 1,
               "price": 12.00
            },
            {
               "partname": "rudder",
               "manufacturer": "local parts co",
               "quality": 1,
               "price": 2.50
            },
            {
               "partname": "rudder",
               "manufacturer": "big parts co",
               "quality": 2,
               "price": 3.75
            },
            {
               "partname": "rudder",
               "manufacturer": "small parts co",
               "quality": null,
               "price": 1.90
            },
            {
               "partname": "wing",
               "manufacturer": "local parts co",
               "quality": null,
               "price": 7.50
            },
            {
               "partname": "wing",
               "manufacturer": "big parts co",
               "quality": 1,
               "price": 15.20
            },
            {
               "partname": "wing",
               "manufacturer": "small parts co",
               "quality": null,
               "price": 11.80
            }
         ],
         "count_by_color": [
            {
               "quality": "high",
               "red": 15,
               "green": 20,
               "blue": 7
            },
            {
               "quality": "normal",
               "red": 35,
               "green": null,
               "blue": 40
            },
            {
               "quality": "low",
               "red": 10,
               "green": 23,
               "blue": null
            }
         ]
       }
   },
   "id":"abcdefgh-ijklmnop-qrstuvwxyz123",
   "mainIds":[
      {
         "ID":"pqrstuvwxyz-aabbcc123",
         "Source":"NYC"
      }
   ]
}
'));
```

## Querying nested semi-structured data

The following statement uses PartiQL’s dot notation to extract the `pnrid` field,
which is nested three levels deep inside the top-level `all_data` object.

```
select all_data.data.pnr.pnrid::varchar from test_json;

 `pnrid
--------------------
 123PQRS-2024-09-20`
```

The following statement uses PartiQL’s bracket notation to specify and extract only
the first element from the `events` array nested inside the top-level object.

```
SELECT
    all_data.data.pnr.events[0]
FROM test_json;

 `events
---------------------------------
{
 "eventType":"UPDATED",
 "type":"PART",
 "id":"123PQRS-2024-09-20-HO-1"
}`
```

The following statement extracts the `eventType`
property of only the specified element from the `events` array.

```
SELECT
    all_data.data.pnr.events[0].eventType
FROM test_json;

 `eventtype
-----------
 "UPDATED"`
```

The following statements

## Using `enable_case_sensitive_identifier` and

`enable_case_sensitive_super_attribute` with semi-structured data

The following examples show how the configuration options
[enable_case_sensitive_identifier](r_enable_case_sensitive_identifier.md "r_enable_case_sensitive_identifier.md") and
[enable_case_sensitive_super_attribute](r_enable_case_sensitive_super_attribute.md "r_enable_case_sensitive_super_attribute.md")
differ when used for querying semi-structured data. For more information on these configuration options,
see [Accessing JSON fields with uppercase and mixed-case field
names or attributes](super-configurations.md#upper-mixed-case "super-configurations.md#upper-mixed-case").

In the following statement, resetting both configuration options to their default of false makes the query return NULL.

```
RESET enable_case_sensitive_identifier;
RESET enable_case_sensitive_super_attribute;

SELECT
    all_data.data.pnr.events[0].eventType
FROM test_json;

 `eventtype
-----------
NULL`
```

In following example, the sample query returns the desired result after
you wrap the case sensitive attributes
in double quotation marks and set `enable_case_sensitive_identifier` to true.

```
RESET enable_case_sensitive_identifier;
RESET enable_case_sensitive_super_attribute;

SELECT
    all_data.data.pnr.events[0]."eventType"
FROM test_json;

 `eventtype
-----------
NULL`

SET enable_case_sensitive_identifier TO true;

SELECT
    all_data.data.pnr.events[0]."eventType"
FROM test_json;

 `eventtype
-----------
 "UPDATED"`
```

In the following example, the sample query returns the desired result after you
set `enable_case_sensitive_super_attribute` to true
without wrapping the case sensitive attributes in double quotation marks.

```
RESET enable_case_sensitive_identifier;
RESET enable_case_sensitive_super_attribute;

SELECT
    all_data.data.pnr.events[0].eventType
FROM test_json;

 `eventtype
-----------
NULL`

SET enable_case_sensitive_super_attribute TO true;

SELECT
    all_data.data.pnr.events[0].eventType
FROM test_json;

 `eventtype
-----------
 "UPDATED"`
```

## Filtering semi-structured data

The following statement uses PartiQL syntax in the WHERE clause of a statement that
counts events of the type `UPDATED` to retrieve data of a certain attribute
from inside an array. You can use this syntax in any portion of
the query where you would normally reference columns.

```
SELECT COUNT(*)
FROM test_json
WHERE all_data.data.pnr.events[0].eventType = 'UPDATED';

 `count
------
 1`
```

The following example uses PartiQL’s bracket and
dot syntax in both GROUP BY and ORDER BY clauses.

```
SELECT all_data.data.pnr.events[0].eventType::varchar,
       COUNT(*)
FROM test_json
WHERE all_data.data.pnr.events[0].eventType IS NOT NULL
GROUP BY all_data.data.pnr.events[0].eventType
ORDER BY all_data.data.pnr.events[0].eventType;

 `eventtype | count
-----------+-------
 "UPDATED" | 1`
```

## Unnesting semi-structured data

The following statement uses PartiQL joins to unnest the `events` array.
Note that this join works even when the number of indexes for the array aren’t static.

For examples of unnesting semi-structured data using UNNEST in the FROM clause, see
[UNNEST examples](r_FROM_clause-unnest-examples.md "r_FROM_clause-unnest-examples.md").

```
SELECT
a.all_data.data.pnr.type::varchar type_info,
a.all_data.data.pnr.pnrid::varchar pnr_id ,
a.all_data.data.pnr.bookingIdentifier::varchar booking_id,
a.all_data.data.pnr.version::varchar version_info,
b.eventType::varchar event_type,
b.id::varchar event_id
FROM test_json a,
  a.all_data.data.pnr.events b;

 `type_info | pnr_id | booking_id | version_info | event_type | event_id
-----------+---------------------+------------+--------------+------------+-------------------------
 pnr | 123PQRS-2024-09-20 | 123PQRS | 5 | UPDATED | 123PQRS-2024-09-20-HO-1
 pnr | 123PQRS-2024-09-20 | 123PQRS | 5 | CREATED | 123PQRS-2024-09-20-OT-38`
```

## Unnesting nested arrays

The following statement uses PartiQL joins to unnest an array that’s nested inside another array.

For examples of unnesting semi-structured data using UNNEST in the FROM clause, see
[UNNEST examples](r_FROM_clause-unnest-examples.md "r_FROM_clause-unnest-examples.md").

```
SELECT
a.all_data.data.pnr.type::varchar type_info,
a.all_data.data.pnr.pnrid::varchar pnr_id ,
a.all_data.data.pnr.bookingIdentifier::varchar booking_id,
a.all_data.data.pnr.version::varchar version_info,
d.id::varchar email_record_id,
d.contact::varchar email_contact,
e::varchar email_purpose,
f::varchar email_commuter
FROM test_json a,
  a.all_data.data.pnr.contactDetail c,
  c."emailContacts" d,
  d.purpose e,
  d.commuter f;

 `type_info | pnr_id | booking_id | version_info | email_record_id | email_contact | email_purpose | email_commuter
-----------+---------------------+------------+--------------+-------------------------+---------------------------+---------------+-------------------------
 pnr | 123PQRS-2024-09-20 | 123PQRS | 5 | 123PQRS-2024-09-20-OT-4 | JOHNMILLER@EXAMPLE.COM | BUSINESS | 123PQRS-2024-09-20-RO-2
 pnr | 123PQRS-2024-09-20 | 123PQRS | 5 | 123PQRS-2024-09-20-OT-5 | HARVEYCORMIER@EXAMPLE.COM | NOTIFICATION | 123PQRS-2024-09-20-RO-2`
```

## Using semi-structured data in subqueries

The following statement uses a subquery in the WHERE clause to
return only a subsection of the results from the previous example.

```
SELECT
a.all_data.data.pnr.type::varchar type_info,
a.all_data.data.pnr.pnrid::varchar pnr_id ,
a.all_data.data.pnr.bookingIdentifier::varchar booking_id,
a.all_data.data.pnr.version::varchar version_info,
d.id::varchar email_record_id,
d.contact::varchar email_contact
FROM test_json a,
a.all_data.data.pnr.contactDetail c,
c."emailContacts" d
WHERE (SELECT COUNT(*) FROM d.purpose e WHERE e = 'BUSINESS') > 0;

 `type_info | pnr_id | booking_id | version_info | email_record_id | email_contact | email_purpose | email_commuter
-----------+---------------------+------------+--------------+-------------------------+---------------------------+---------------+-------------------------
 pnr | 123PQRS-2024-09-20 | 123PQRS | 5 | 123PQRS-2024-09-20-OT-4 | JOHNMILLER@EXAMPLE.COM | BUSINESS | 123PQRS-2024-09-20-RO-2`
```

## Aggregating queries using semi-structured data

The following statement uses the COUNT function to aggregate
the number of elements in the `PendingService` array.

```
SELECT
a.all_data.data.pnr.type::varchar type_info,
a.all_data.data.pnr.pnrid::varchar pnr_id ,
a.all_data.data.pnr.bookingIdentifier::varchar booking_id,
a.all_data.data.pnr.version::varchar version_info,
COUNT(*) AS total_pending_service
FROM test_json a,
  a.all_data.data.pnr.PendingService c
GROUP BY 1,2,3,4;

 `type_info | pnr_id | booking_id | version_info | total_pending_service
-----------+--------------------+------------+--------------+-----------------------
 pnr | 123PQRS-2024-09-20 | 123PQRS | 5 | 4`
```

## Using semi-structured data in materialized views

The following statement uses the statement from the previous example to create a materialized view.
The materialized view automatically
refresh the number of pending services when the base table gets new data.

```
CREATE MATERIALIZED VIEW mv_total_pending_service
AUTO REFRESH YES
AS
SELECT
a.all_data.data.pnr.type::varchar type_info,
a.all_data.data.pnr.pnrid::varchar pnr_id ,
a.all_data.data.pnr.bookingIdentifier::varchar booking_id,
a.all_data.data.pnr.version::varchar version_info,
COUNT(*) AS total_pending_service
FROM test_json a,
  a.all_data.data.pnr.PendingService c
GROUP BY 1,2,3,4;
```

## Using PIVOT and UNPIVOT with semi-structured data

The following statement uses PIVOT on the `partname` column to
return the average price of each part.

```
SELECT *
FROM
(
SELECT
c.partname::varchar, c.price
FROM test_json a,
  a.all_data.data.pnr.parts c)
PIVOT (AVG(price) for partname IN ('prop', 'rudder', 'wing'));

 `prop | rudder | wing
------------+--------------------+--------
 10.33 | 2.71 | 11.50`
```

In the previous example, the results are transformed into columns.
The following example shows a GROUP BY query that returns the
average prices in rows, rather than in columns.

```
SELECT partname, avg(price)
FROM (
SELECT
c.partname::varchar, c.price
FROM test_json a,
  a.all_data.data.pnr.parts c)
WHERE partname IN ('prop', 'rudder', 'wing')
GROUP BY partname;

 `partname | avg
----------+-------
 prop | 10.33
 rudder | 2.71
 wing | 11.50`
```

Following is a PIVOT example with
`manufacturer` as an implicit column.

```
SELECT *
FROM (
SELECT
c.quality, c.manufacturer::varchar
FROM test_json a,
  a.all_data.data.pnr.parts c) PIVOT (
count(*) FOR quality IN (1, 2, NULL)
);

 `manufacturer | 1 | 2 | null
-------------------+----+----+------
 local parts co | 1 | 1 | 1
 big parts co | 1 | 1 | 1
 small parts co | 1 | 0 | 2`
```

Following is an UNPIVOT example on the `quality` column.

```
SELECT *
FROM
(
SELECT
c.quality as quality
FROM test_json a,
  a.all_data.data.pnr.parts c)
UNPIVOT (cnt FOR column_header IN (quality));

 `column_header | cnt
-----------------+----
 quality | 2
 quality | 1
 quality | 1
 quality | 2
 quality | 1`
```
