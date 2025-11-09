# sort

Use `sort` to display log events in ascending
(`asc`) or descending (`desc`) order by a
specified field. You can use this with the `limit` command to
create "top N" or "bottom N" queries.

The sorting algorithm is an updated version of natural sorting. If you
sort in ascending order, the following logic is used.

- All non-number values come before all number values.
  _Number values_ are values that include only
  numbers, not a mix of numbers and other characters.
- For non-number values, the algorithm groups consecutive numeric
  characters and consecutive alphabetic characters into separate
  chunks for comparison. It orders non-numeric portions by their
  Unicode values, and it orders numeric portions by their length first
  and then by their numerical value.
  For more information about Unicode order, see [List of
  Unicode characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters "https://en.wikipedia.org/wiki/List_of_Unicode_characters").

For example, the following is the result of a sort in ascending
order.

```
!:	>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> sorted by unicode order
#
*%04
0#	>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Alphanumeric starting with numbers
5A
111A   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Starts with more digits than 5A, so it sorted to be later than 5A
2345_
@	>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2345 is compared with @ in the unicode order,
@_
A	>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Values starting with letters
A9876fghj
a12345hfh
0	>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Number values
01
1
2
3
```

If you sort in descending order, the sort results are the reverse.

For example, the following query for Amazon VPC flow logs finds the top 15
packet transfers across hosts.

```
stats sum(packets) as packetsTransferred by srcAddr, dstAddr
    | sort packetsTransferred  desc
    | limit 15
```
