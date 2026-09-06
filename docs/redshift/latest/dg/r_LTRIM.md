

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# LTRIM function
<a name="r_LTRIM"></a>

Trims characters from the beginning of a string. Removes the longest string containing only characters in the trim characters list. Trimming is complete when a trim character does not appear in the input string.

## Syntax
<a name="r_LTRIM-synopsis"></a>

```
LTRIM( string [, trim_chars] )
```

## Arguments
<a name="r_LTRIM-arguments"></a>

 *string*   
A string column, expression, or string literal to be trimmed.

 *trim\_chars*   
A string column, expression, or string literal that represents the characters to be trimmed from the beginning of *string*. If not specified, a space is used as the trim character.

## Return type
<a name="r_LTRIM-return-type"></a>

The LTRIM function returns a character string that is the same data type as the input *string* (CHAR or VARCHAR). 

## Examples
<a name="r_LTRIM-example"></a>

The following example trims the year from the `listime` column. The trim characters in string literal `'2008-'` indicate the characters to be trimmed from the left. If you use the trim characters `'028-'`, you achieve the same result. 

```
select listid, listtime, ltrim(listtime, '2008-')
from listing
order by 1, 2, 3
limit 10;            

listid |      listtime       |     ltrim
-------+---------------------+----------------
     1 | 2008-01-24 06:43:29 | 1-24 06:43:29
     2 | 2008-03-05 12:25:29 | 3-05 12:25:29
     3 | 2008-11-01 07:35:33 | 11-01 07:35:33
     4 | 2008-05-24 01:18:37 | 5-24 01:18:37
     5 | 2008-05-17 02:29:11 | 5-17 02:29:11
     6 | 2008-08-15 02:08:13 | 15 02:08:13
     7 | 2008-11-15 09:38:15 | 11-15 09:38:15
     8 | 2008-11-09 05:07:30 | 11-09 05:07:30
     9 | 2008-09-09 08:03:36 | 9-09 08:03:36
    10 | 2008-06-17 09:44:54 | 6-17 09:44:54
```

LTRIM removes any of the characters in *trim\_chars* when they appear at the beginning of *string*. The following example trims the characters 'C', 'D', and 'G' when they appear at the beginning of VENUENAME, which is a VARCHAR column. 

```
select venueid, venuename, ltrim(venuename, 'CDG')
from venue
where venuename like '%Park'
order by 2
limit 7;             

venueid | venuename                  | btrim                    
--------+----------------------------+--------------------------
    121 | ATT Park                   | ATT Park                
    109 | Citizens Bank Park         | itizens Bank Park        
    102 | Comerica Park              | omerica Park             
      9 | Dick's Sporting Goods Park | ick's Sporting Goods Park
     97 | Fenway Park                | Fenway Park              
    112 | Great American Ball Park   | reat American Ball Park  
    114 | Miller Park                | Miller Park
```

The following example uses the trim character `2` which is retrieved from the `venueid` column.

```
select ltrim('2008-01-24 06:43:29', venueid) 
from venue where venueid=2;              

ltrim
------------------
008-01-24 06:43:29
```

The following example does not trim any characters because a `2` is found before the `'0'` trim character. 

```
select ltrim('2008-01-24 06:43:29', '0');              

ltrim
-------------------
2008-01-24 06:43:29
```

The following example uses the default space trim character and trims the two spaces from the beginning of the string. 

```
select ltrim('  2008-01-24 06:43:29');              

ltrim
-------------------
2008-01-24 06:43:29
```