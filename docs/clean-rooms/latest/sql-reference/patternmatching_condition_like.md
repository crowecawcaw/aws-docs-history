

# LIKE
<a name="patternmatching_condition_like"></a>

The LIKE operator compares a string expression, such as a column name, with a pattern that uses the wildcard characters % (percent) and \_ (underscore). LIKE pattern matching always covers the entire string. To match a sequence anywhere within a string, the pattern must start and end with a percent sign. 

LIKE is case-sensitive.

## Syntax
<a name="patternmatching_condition_like-synopsis"></a>

```
expression [ NOT ] LIKE | pattern [ ESCAPE 'escape_char' ]
```

## Arguments
<a name="patternmatching_condition_like-arguments"></a>

 *expression*   
A valid UTF-8 character expression, such as a column name. 

LIKE  
LIKE performs a case-sensitive pattern match. To perform a case-insensitive pattern match for multibyte characters, use the [LOWER](LOWER.md) function on *expression* and *pattern* with a LIKE condition.  
In contrast to comparison predicates, such as = and <>, LIKE predicates don't implicitly ignore trailing spaces. To ignore trailing spaces, use RTRIM or explicitly cast a CHAR column to VARCHAR.  
The `~~` operator is equivalent to LIKE. Also the `!~~` operator is equivalent to NOT LIKE.

 *pattern*   
A valid UTF-8 character expression with the pattern to be matched. 

 *escape\_char*   
A character expression that will escape metacharacters characters in the pattern. The default is two backslashes ('\\\\'). 

If *pattern* does not contain metacharacters, then the pattern only represents the string itself; in that case LIKE acts the same as the equals operator.

Either of the character expressions can be CHAR or VARCHAR data types. If they differ, AWS Clean Rooms converts *pattern* to the data type of *expression*. 

LIKE supports the following pattern-matching metacharacters: 


| Operator  | Description  | 
| --- | --- | 
| %  | Matches any sequence of zero or more characters. | 
| \_ | Matches any single character. | 

## Examples
<a name="patternmatching_condition_like-examples"></a>

The following table shows examples of pattern matching using LIKE:


| Expression  | Returns  | 
| --- | --- | 
| 'abc' LIKE 'abc' | True | 
| 'abc' LIKE 'a%' | True | 
| 'abc' LIKE '\_B\_' | False | 
| 'abc' LIKE 'c%' | False | 

The following example finds all cities whose names start with "E": 

```
select distinct city from users
where city like 'E%' order by city;
city
---------------
East Hartford
East Lansing
East Rutherford
East St. Louis
Easthampton
Easton
Eatontown
Eau Claire
...
```

The following example finds users whose last name contains "ten" :

```
select distinct lastname from users
where lastname like '%ten%' order by lastname;
lastname
-------------
Christensen
Wooten
...
```

The following example finds cities whose third and fourth characters are "ea". : 

```
select distinct city from users where city like '__EA%' order by city;
city
-------------
Brea
Clearwater
Great Falls
Ocean City
Olean
Wheaton
(6 rows)
```

The following example uses the default escape string (\\\\) to search for strings that include "start\_" (the text `start` followed by an underscore `_`): 

```
select tablename, "column" from my_table_def 


where "column" like '%start\\_%'
limit 5;

     tablename     |    column
-------------------+---------------
 my_s3client      | start_time
 my_tr_conflict   | xact_start_ts
 my_undone        | undo_start_ts
 my_unload_log    | start_time
 my_vacuum_detail | start_row
(5 rows)
```

The following example specifies '^' as the escape character, then uses the escape character to search for strings that include "start\_" (the text `start` followed by an underscore `_`): 

```
select tablename, "column" from my_table_def 

where "column" like '%start^_%' escape '^' 
limit 5;

     tablename     |    column
-------------------+---------------
 my_s3client      | start_time
 my_tr_conflict   | xact_start_ts
 my_undone        | undo_start_ts
 my_unload_log    | start_time
 my_vacuum_detail | start_row
(5 rows)
```