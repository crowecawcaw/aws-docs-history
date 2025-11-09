# Temporal Predicates

The following table shows a graphic representation of temporal predicates supported by
standard SQL and extensions to the SQL standard supported by Amazon Kinesis Data Analytics. It shows the
relationships that each predicate covers. Each relationship is represented as an upper interval
and a lower interval with the combined meaning _upperInterval predicate lowerInterval
evaluates to TRUE_. The first 7 predicates are standard SQL. The last 10 predicates,
shown in bold text, are Amazon Kinesis Data Analytics extensions to the SQL standard.

| Predicate             | Covered Relationships                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------- |
| CONTAINS              | Blue rectangular shapes arranged in horizontal rows, resembling a simplified layout or structure. |
| OVERLAPS              | Blue rectangular boxes arranged in rows, representing a structured layout or diagram.             |
| EQUALS                | Two horizontal blue rectangles with orange borders, stacked vertically.                           |
| PRECEDES              | Four blue rectangular shapes representing placeholder text or content blocks.                     |
| SUCCEEDS              | Four blue rectangular shapes arranged horizontally with gaps between them.                        |
| IMMEDIATELY PRECEDES  | Blue rectangular shapes representing text or content placeholders.                                |
| IMMEDIATELY SUCCEEDS  | Two horizontal blue rectangular shapes against a white background.                                |
| **LEADS**             | Four blue rectangular buttons with orange outlines, arranged horizontally.                        |
| **LAGS**              | Four blue rectangular bars of varying lengths arranged horizontally.                              |
| **STRICTLY CONTAINS** | Two blue rectangular shapes with orange outlines, one larger above a smaller one.                 |
| **STRICTLY OVERLAPS** | Two blue rectangular shapes, one longer than the other, stacked vertically.                       |
| **STRICTLY PRECEDES** | Two horizontal blue bars representing placeholder elements in a user interface.                   |
| **STRICTLY SUCCEEDS** | Two blue rectangular shapes representing UI elements or buttons.                                  |
| **STRICTLY LEADS**    | Two blue rectangular shapes representing text or content blocks.                                  |
| **STRICTLY LAGS**     | Two horizontal blue rectangular shapes, one above the other, against a white background.          |
| **IMMEDIATELY LEADS** | Two blue rectangular shapes, one longer than the other, stacked vertically.                       |
| **IMMEDIATELY LAGS**  | Two blue rectangular shapes, one longer than the other, stacked vertically.                       |

To enable concise expressions, Amazon Kinesis Data Analytics also supports the following extensions:

- Optional PERIOD keyword – The PERIOD keyword can be omitted.
- Compact chaining – If two of these predicates occur back to back, separated by an
  AND, the AND can be omitted provided that the right interval of the first predicate is
  identical to the left interval of the second predicate.
- TSDIFF – This function takes two TIMESTAMP arguments and returns their difference
  in milliseconds.
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

Finally, standard SQL allows the CONTAINS predicate to take a single TIMESTAMP as its
right-hand argument. For example, the following expression:

```
PERIOD(s, e) CONTAINS t
```

Is equivalent to the following:

```
s <= t AND t < e
```

## Syntax

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

## Example

The following example code records an alarm if a window is open while the air conditioning
is on:

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

The following query uses a temporal predicate to raise a fraud alarm when two people try
to use the same credit card simultaneously at two different locations:

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
