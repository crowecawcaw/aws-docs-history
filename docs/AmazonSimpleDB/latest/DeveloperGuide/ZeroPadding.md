# Zero Padding

After all the numbers in a data set are positive, ensure they are properly represented for
lexicographical comparisons. For example, the string "10" comes before "2" in lexicographical
order. If we zero pad the numbers to five digits, "00002" comes before "00010" and are
compared correctly. Additionally, the offset is valid for numbers up to 5 digits and future
numbers such as 00402 and 02987 are properly represented in this scheme.

To determine the right number of digits for zero padding, determine the largest number in
your data set (accounting for negative number conversions), determine the offset number
(maximum number of digits for that number without a decimal point), and convert all your
numbers by appending zeros to them until they match the digit length of the offset number.

The following is sample data set with an offset applied.

```
100014.58, 87463.209, 20171109, 755378.34, 99977
```

If you zero pad the data set as well, the following is the resulting data set.

```
00100014.58, 00087463.209, 20171109, 00755378.34, 00099977
```

From this result set, the original query `'attribute' > '500'` is now `'attribute' > '00100500'`.
