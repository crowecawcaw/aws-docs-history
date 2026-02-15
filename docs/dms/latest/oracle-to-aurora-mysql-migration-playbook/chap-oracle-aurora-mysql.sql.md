# Oracle DBMS_RANDOM and MySQL RAND function

With AWS DMS, you can generate random numbers or values during data migration from Oracle to MySQL or vice versa. Oracle’s `DBMS_RANDOM` package and MySQL’s `RAND` function provide methods for generating random data, which can be useful for tasks like creating test data, simulating real-world scenarios, or introducing randomness into algorithms.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                |
| -------------------------------- | ---------------------------------- | ------------------------- | -------------------------------------------------------------- |
| Three star feature compatibility | No automation                      | N/A                       | Different syntax and missing options may require code rewrite. |

## Oracle usage

Oracle `DBMS_RANDOM` package provides functionality for generating random numbers or strings as part of an SQL statement or PL/SQL procedure.

The `DBMS_RANDOM` Package stored procedures include:

- **NORMAL** — Returns random numbers in a standard normal distribution.
- **SEED** — Resets the seed that generates random numbers or strings.
- **STRING** — Returns a random string.
- **VALUE** — Returns a number greater than or equal to 0 and less than 1 with 38 digits to the right of the decimal. Alternatively, you could generate a random number greater than or equal to a low parameter and less than a high parameter.

`DBMS_RANDOM.RANDOM` produces integers in the range [-2^^31, 2^^31].

`DBMS_RANDOM.VALUE` produces numbers in the range [0,1] with 38 digits of precision.

### Examples

Generate a random number.

```
select dbms_random.value() from dual;

DBMS_RANDOM.VALUE()
.859251508

select dbms_random.value() from dual;

DBMS_RANDOM.VALUE()
.364792387
```

Generate a random string. The first character determines the returned string type and the number specifies the length.

```
select dbms_random.string('p',10) from dual;
DBMS_RANDOM.STRING('P',10)

la'?z[Q&/2

select dbms_random.string('p',10) from dual;
DBMS_RANDOM.STRING('P',10)

t?!Gf2M60q
```

For more information, see [DBMS_RANDOM](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_RANDOM.html#GUID-8DC48B0C-3707-4172-A306-C0308DD2EB0F "https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_RANDOM.html#GUID-8DC48B0C-3707-4172-A306-C0308DD2EB0F") in the _Oracle documentation_.

## MySQL usage

The MySQL `RAND` function is not fully equivalent to Oracle `DBMS_RANDOM` because it does not generate string values. However, there are other functions in that can be used in combination to achieve full functionality.

`RAND` function returns a random floating-point value `v` in the range `0 ⇐ v < 1.0`.

You can use the `RAND` function with a seed value to reset the seed. If an integer argument N is specified, it is used as the seed value:

- With a constant initializer argument, the seed is initialized once when the statement is prepared and prior to execution.
- With a non-constant initializer argument such as a column name, the seed is initialized with the value for each invocation of `RAND()`.

### Examples

Generate a random number.

```
select RAND();

RAND()
0.30244802525494996
```

To obtain a random integer `R` in the range `i ⇐ R < j`, use the expression `FLOOR(i + RAND() * (j − i))`. For example, to obtain a random integer in the range `7 ⇐ R < 12`, use:

```
SELECT FLOOR(7 + (RAND() * 5));

FLOOR(7 + (RAND() * 5))
8
```

Generate an eight-character string of digits.

```
SELECT SUBSTRING(MD5(RAND()) FROM 1 FOR 8);
```

Generate an eight-character string containing characters only.

```
SELECT concat(substring('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', rand()*52+1, 1),
substring('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', rand()*52+1, 1),
substring('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', rand()*52+1, 1),
substring('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', rand()*52+1, 1),
substring('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', rand()*52+1, 1),
substring('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', rand()*52+1, 1),
substring('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', rand()*52+1, 1),
substring('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', rand()*52+1, 1))
```

For more information, see [RAND()](https://dev.mysql.com/doc/refman/5.7/en/mathematical-functions.html#function_rand "https://dev.mysql.com/doc/refman/5.7/en/mathematical-functions.html#function_rand") in the _MySQL documentation_.
