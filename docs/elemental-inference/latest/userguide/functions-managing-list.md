

# Listing and viewing functions
<a name="functions-managing-list"></a>

```
aws elemental-inference list-functions \
  --region {{us-west-2}} \
  --max-results 50

aws elemental-inference get-function \
  --region {{us-west-2}} \
  --id {{function-id}}
```

`list-functions` is paginated: pass up to 100 in `maxResults`, and pass the `nextToken` from the response to get the next page. Each summary includes the name, status, target, and `contextTypes`, so you can find the functions that use a particular kind of context without calling `get-function` for each one.