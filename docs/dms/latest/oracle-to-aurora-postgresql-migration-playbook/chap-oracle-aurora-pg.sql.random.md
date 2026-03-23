# Oracle DBMS_RANDOM and PostgreSQL RANDOM function

With AWS DMS, you can generate random numbers or randomly select data for various purposes, such as testing, sampling, or introducing randomness in your applications. Oracle `DBMS_RANDOM` and PostgreSQL `RANDOM` function provide methods to generate random numbers or randomly select data from a specified dataset.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                            |
| -------------------------------- | ---------------------------------- | ------------------------- | ------------------------------------------ |
| Three star feature compatibility | No automation                      | N/A                       | Different syntax may require code rewrite. |

## Oracle usage

Oracle `DBMS_RANDOM` package provides functionality for generating random numbers or strings as part of an SQL statement or PL/SQL procedure.

The `DBMS_RANDOM` Package stored procedures include:

- **NORMAL** — Returns random numbers in a standard normal distribution.
- **SEED** — Resets the seed that generates random numbers or strings.
- **STRING** — Returns a random string.
- **VALUE** — Returns a number greater than or equal to 0 and less than 1 with 38 digits to the right of the decimal. Alternatively, you could generate a random number greater than or equal to a low parameter and less than a high parameter.

`DBMS_RANDOM.RANDOM` produces integers in the range [-2^^31, 2^^31].

`DBMS_RANDOM.VALUE` produces numbers in the range [0,1] with 38 digits of precision.

**Examples**

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

## PostgreSQL usage

PostgreSQL doesn’t provide a dedicated package equivalent to Oracle `DBMS_RANDOM`, a 1:1 migration isn’t possible. However, you can use other PostgreSQL functions as workarounds under certain conditions. For example, generating random numbers can be performed using the `random()` function. For generating random strings, you can use the value returned from the `random()` function coupled with an `md5()` function.

**Examples**

Generate a random number.

```
select random();
random

0.866594325285405
(1 row)

select random();
random

0.524613124784082
(1 row)
```

Generate a random string.

```
select md5(random()::text);
md5

f83e73114eccfed571b43777b99e0795
(1 row)

select md5(random()::text);
md5

d46de3ce24a99d5761bb34bfb6579848
(1 row)
```

To generate a random string of the specified length, you can use the following function.

```
create or replace function random_string(length integer) returns text as
$$
declare
  chars text[] := '{0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z}';
  result text := '';
  i integer := 0;
begin
  if length < 0 then
    raise exception 'Given length cannot be less than 0';
  end if;
  for i in 1..length loop
    result := result || chars[1+random()*(array_length(chars, 1)-1)];
  end loop;
  return result;
end;
$$ language plpgsql;
```

The following code example shows the result of using this function.

```
select random_string(15);
random_string

5emZKMYxB9C2vT6
(1 row)

select random_string(10);
random_string

tMAxfql0iM
(1 row)
```

## Summary

| Description                               | Oracle                                         | PostgreSQL                           |
| ----------------------------------------- | ---------------------------------------------- | ------------------------------------ |
| Generate a random number                  | `select dbms_random.value() from dual;`        | `select random();`                   |
| Generate a random number between 1 to 100 | `select dbms_random.value(1,100) from dual;`   | `select random()*100;`               |
| Generate a random string                  | `select dbms_random.string('p',10) from dual;` | `select md5(random()::text);`        |
| Generate a random string in upper case    | `select dbms_random.string('U',10) from dual;` | `select upper(md5(random()::text));` |

For more information, see [Mathematical Functions and Operators](https://www.postgresql.org/docs/13/functions-math.html "https://www.postgresql.org/docs/13/functions-math.html") and [String Functions and Operators](https://www.postgresql.org/docs/10/functions-string.html "https://www.postgresql.org/docs/10/functions-string.html") in the _PostgreSQL documentation_.
