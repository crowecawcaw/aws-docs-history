# Placeholder value filtering

Resource matching automatically ignores identifier values that are:

- all zeros (for example, `0`, `000000000`, `00-000-0000`);
- common placeholders, case-insensitive (`unknown`, `n/a`, `na`, `none`, `null`, `unassigned`, `pending`, `temp`, `test`);
- fewer than three characters; or
- empty or whitespace only.
