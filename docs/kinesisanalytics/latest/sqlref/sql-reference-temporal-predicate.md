

# Temporal Predicates
<a name="sql-reference-temporal-predicate"></a>

The following table shows a graphic representation of temporal predicates supported by standard SQL and extensions to the SQL standard supported by Amazon Kinesis Data Analytics. It shows the relationships that each predicate covers. Each relationship is represented as an upper interval and a lower interval with the combined meaning *upperInterval predicate lowerInterval evaluates to TRUE*. The first 7 predicates are standard SQL. The last 10 predicates, shown in bold text, are Amazon Kinesis Data Analytics extensions to the SQL standard.


| Predicate | Covered Relationships | 
| --- | --- | 
| CONTAINS |  ![Blue rectangular shapes arranged in horizontal rows, resembling a simplified layout or structure.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_contains.png)  | 
| OVERLAPS |  ![Blue rectangular boxes arranged in rows, representing a structured layout or diagram.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_overlaps.png)  | 
| EQUALS |  ![Two horizontal blue rectangles with orange borders, stacked vertically.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_equals.png)  | 
| PRECEDES |  ![Four blue rectangular buttons or containers arranged in a staggered layout.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_precedes.png)  | 
| SUCCEEDS |  ![Four blue rectangular shapes arranged horizontally with gaps between them.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_succeeds.png)  | 
| IMMEDIATELY PRECEDES |  ![Two horizontal progress bars with blue fill and orange borders at different stages.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_immediately_precedes.png)  | 
| IMMEDIATELY SUCCEEDS |  ![Two horizontal blue rectangular shapes against a white background.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_immediately_succeeds.png)  | 
| **LEADS** |  ![Four blue rectangular buttons with orange outlines, arranged horizontally.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_leads.png)  | 
| **LAGS** |  ![Four horizontal progress bars or loading indicators of varying lengths.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_lags.png)  | 
| **STRICTLY CONTAINS** |  ![Two blue rectangular buttons with orange borders, one larger than the other.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_strictly_contains.png)  | 
| **STRICTLY OVERLAPS** |  ![Two blue rectangular buttons or UI elements of different sizes.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_strictly_overlaps.png)  | 
| **STRICTLY PRECEDES** |  ![Two horizontal blue bars representing placeholder elements in a user interface.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_strictly_precedes.png)  | 
| **STRICTLY SUCCEEDS** |  ![Two blue rectangular shapes representing UI elements or buttons.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_strictly_succeeds.png)  | 
| **STRICTLY LEADS** |  ![Two blue rectangular buttons with orange borders, one smaller above and one larger below.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_strictly_leads.png)  | 
| **STRICTLY LAGS** |  ![Two horizontal blue rectangular shapes, one above the other, against a white background.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_strictly_lags.png)  | 
| **IMMEDIATELY LEADS** |  ![Two blue rectangular buttons with orange borders, one larger above and one smaller below.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_immediately_leads.png)  | 
| **IMMEDIATELY LAGS** |  ![Two blue rectangular buttons with orange borders, one larger than the other.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sqlrf_immediately_lags.png)  | 

To enable concise expressions, Amazon Kinesis Data Analytics also supports the following extensions: 
+ Optional PERIOD keyword – The PERIOD keyword can be omitted.
+ Compact chaining – If two of these predicates occur back to back, separated by an AND, the AND can be omitted provided that the right interval of the first predicate is identical to the left interval of the second predicate.
+ TSDIFF – This function takes two TIMESTAMP arguments and returns their difference in milliseconds.

For example, you can write the following expression:

```
  PERIOD (s1,e1) PRECEDES PERIOD(s2,e2)
  AND PERIOD(s2, e2) PRECEDES PERIOD(s3,e3)
```

More concisely as follows:

```
(s1,e1) PRECEDES (s2,e2) PRECEDES PERIOD(s3,e3)
```

The following concise expression:

```
TSDIFF(s,e) 
```

Means the following:

 

```
CAST((e - s) SECOND(10, 3) * 1000 AS BIGINT)
```

Finally, standard SQL allows the CONTAINS predicate to take a single TIMESTAMP as its right-hand argument. For example, the following expression:

```
PERIOD(s, e) CONTAINS t
```

Is equivalent to the following:

```
s <= t AND t < e
```

## Syntax
<a name="sql-reference-temporal-predicate-syntax"></a>

Temporal predicates are integrated into a new BOOLEAN valued expression:

```
<period-expression> :=
  <left-period> <half-period-predicate> <right-period>

<half-period-predicate> := 
  <period-predicate> [ <left-period> <half-period-predicate> ]

<period-predicate> :=
   EQUALS
 | [ STRICTLY ] CONTAINS
 | [ STRICTLY ] OVERLAPS
 | [ STRICTLY | IMMEDIATELY ] PRECEDES
 | [ STRICTLY | IMMEDIATELY ] SUCCEEDS
 | [ STRICTLY | IMMEDIATELY ] LEADS
 | [ STRICTLY | IMMEDIATELY ] LAGS

<left-period> := <bounded-period>

<right-period> := <bounded-period> | <timestamp-expression>

<bounded-period> := [ PERIOD ] ( <start-time>, <end-time> )

<start-time> := <timestamp-expression>

<end-time> := <timestamp-expression>

<timestamp-expression> :=
  an expression which evaluates to a TIMESTAMP value

where <right-period> may evaluate to a <timestamp-expression> only if
the immediately preceding <period-predicate> is [ STRICTLY ] CONTAINS
```

This Boolean expression is supported by the following builtin function:

```
BIGINT tsdiff( startTime TIMESTAMP, endTime TIMESTAMP )
```

Returns the value of (endTime - startTime) in milliseconds.

```
```

## Example
<a name="sql-reference-temporal-predicate-example"></a>

The following example code records an alarm if a window is open while the air conditioning is on:

```
create or replace pump alarmPump stopped as
  insert into alarmStream( houseID, roomID, alarmTime, alarmMessage )
    select stream w.houseID, w.roomID, current_timestamp,
                   'Window open while air conditioner is on.'
    from
        windowIsOpenEvents over (range interval '1' minute preceding) w
    join
        acIsOnEvents over (range interval '1' minute preceding) h
    on w.houseID = h.houseID
    where (h.startTime, h.endTime) overlaps (w.startTime, w.endTime);
```

## Sample Use Case
<a name="sql-reference-temporal-predicate-sample-use-case"></a>

The following query uses a temporal predicate to raise a fraud alarm when two people try to use the same credit card simultaneously at two different locations:

```
create pump creditCardFraudPump stopped as
 insert into alarmStream
  select stream
    current_timestamp, creditCardNumber, registerID1, registerID2
  from transactionsPerCreditCard
  where registerID1 <> registerID2
  and (startTime1, endTime1) overlaps (startTime2, endTime2)
;
```

The preceding code example uses an input stream with the following dataset:

```
(current_timestamp  TIMESTAMP,
  creditCardNumber  VARCHAR(16),
  registerID1       VARCHAR(16),
  registerID2       VARCHAR(16),
  startTime1        TIMESTAMP,
  endTime1          TIMESTAMP,
  startTime2        TIMESTAMP,
  endTime2          TIMESTAMP)
```