

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# \+ (Concatenation) operator
<a name="r_DATE-CONCATENATE_function"></a>

Concatenates a DATE to a TIME or TIMETZ on either side of the \+ symbol and returns a TIMESTAMP or TIMESTAMPTZ. 

## Syntax
<a name="r_DATE-CONCATENATE_function-synopsis"></a>

```
date + {time | timetz}
```

The order of the arguments can be reversed. For example, *time* \+ *date*.

## Arguments
<a name="r_DATE-CONCATENATE_function-arguments"></a>

 *date*   
A column of data type `DATE` or an expression that implicitly evaluates to a `DATE` type. 

 *time*   
A column of data type `TIME` or an expression that implicitly evaluates to a `TIME` type. 

 *timetz*   
A column of data type `TIMETZ` or an expression that implicitly evaluates to a `TIMETZ` type. 

## Return type
<a name="r_DATE-CONCATENATE_function-return-type"></a>

TIMESTAMP if input is *date* \+ *time*. 

TIMESTAMPTZ if input is *date* \+ *timetz*. 

## Examples
<a name="r_DATE-CONCATENATE_function-examples"></a>

### Example setup
<a name="r_DATE-CONCATENATE_function-example-setup"></a>

To set up the TIME\_TEST and TIMETZ\_TEST tables used in the examples, use the following command.

```
create table time_test(time_val time);

insert into time_test values
('20:00:00'),
('00:00:00.5550'),
('00:58:00');
   
create table timetz_test(timetz_val timetz);
   
insert into timetz_test values
('04:00:00+00'),
('00:00:00.5550+00'),
('05:58:00+00');
```

### Examples with a time column
<a name="r_DATE-CONCATENATE_function-examples-time"></a>

The following example table TIME\_TEST has a column TIME\_VAL (type TIME) with three values inserted. 

```
select time_val from time_test;
            
time_val
---------------------
20:00:00
00:00:00.5550
00:58:00
```

The following example concatenates a date literal and a TIME\_VAL column.

```
select date '2000-01-02' + time_val as ts from time_test;
            
ts
---------------------
2000-01-02 20:00:00
2000-01-02 00:00:00.5550
2000-01-02 00:58:00
```

The following example concatenates a date literal and a time literal. 

```
select date '2000-01-01' + time '20:00:00' as ts;
            
         ts
---------------------
 2000-01-01 20:00:00
```

The following example concatenates a time literal and a date literal. 

```
select time '20:00:00' + date '2000-01-01' as ts;
            
         ts
---------------------
 2000-01-01 20:00:00
```

### Examples with a TIMETZ column
<a name="r_DATE-CONCATENATE_function-examples-timetz"></a>

The following example table TIMETZ\_TEST has a column TIMETZ\_VAL (type TIMETZ) with three values inserted. 

```
select timetz_val from timetz_test;
            
timetz_val
------------------
04:00:00+00
00:00:00.5550+00
05:58:00+00
```

The following example concatenates a date literal and a TIMETZ\_VAL column. 

```
select date '2000-01-01' + timetz_val as ts from timetz_test;
ts
---------------------
2000-01-01 04:00:00+00
2000-01-01 00:00:00.5550+00
2000-01-01 05:58:00+00
```

The following example concatenates a TIMETZ\_VAL column and a date literal. 

```
select timetz_val + date '2000-01-01' as ts from timetz_test;
ts
---------------------
2000-01-01 04:00:00+00
2000-01-01 00:00:00.5550+00
2000-01-01 05:58:00+00
```

The following example concatenates a DATE literal and a TIMETZ literal. The example returns a TIMESTAMPTZ which is in the time zone UTC by default. UTC is 8 hours ahead of PST, so the result is 8 hours ahead of the input time.

```
select date '2000-01-01' + timetz '20:00:00 PST' as ts;
            
           ts
------------------------
 2000-01-02 04:00:00+00
```