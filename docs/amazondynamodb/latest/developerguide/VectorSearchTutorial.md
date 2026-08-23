# Tutorial: Your first vector search

Imagine a product catalog where shoppers describe what they want in their own words
instead of matching exact keywords. You can store a vector embedding of each product
description in DynamoDB and then query a vector index to find the closest matches.

This tutorial creates a table with a vector index, generates 1024-dimension
embeddings with Amazon Bedrock Titan Text Embeddings V2, loads 50 products, and runs a
similarity search that returns the 5 closest matches. Every command can be pasted
directly into a terminal. For background on how embeddings work with DynamoDB, see [Generating vector embeddings](VectorSearchWorkingWith.md#VectorSearchWorkingWith.Embeddings "VectorSearchWorkingWith.md#VectorSearchWorkingWith.Embeddings").

###### About scale and recall

A production vector index holds millions to billions of vectors. Vector indexes
use approximate nearest neighbor search, and the recall characteristics of that
approach become observable only at much larger scale. Treat the 50-item catalog
here as a demonstration of the mechanics. For guidance on sizing and tuning, see
[Best practices for vector indexes](VectorSearchBestPractices.md "VectorSearchBestPractices.md").

## Prerequisites

Before you begin, make sure you have the following:

- AWS CLI version 2.36.16 or later. Vector index support was added to the
  AWS CLI and the AWS SDKs in the service model update released on August 4,

2026. Earlier versions do not recognize the
      `--vector-indexes` parameter or the
      `search-vectors` command. Check your version with `aws
 --version` and upgrade if needed. If you use an AWS SDK instead of
      the AWS CLI, you need `botocore` 1.43.64 or later, or the
      equivalent release of your language SDK.

- Credentials with permissions for the DynamoDB actions
  `CreateTable`, `DescribeTable`,
  `PutItem`, `BatchWriteItem`, `Scan`,
  `SearchVectors`, `UpdateTable`, and
  `DeleteTable`, and for the Amazon Bedrock action
  `InvokeModel`. `dynamodb:SearchVectors` is a new
  action, so existing policies that grant DynamoDB read access do not include
  it.
- Access to the Titan Text Embeddings V2 model enabled in Amazon Bedrock for your
  account and Region. Amazon Bedrock model access is granted per account and per Region,
  so you must enable the model before you can call it.
- `jq` installed for reshaping the model output into DynamoDB
  format.
- A Region where Amazon Bedrock Titan Text Embeddings
  V2 is available. Vector indexes are available in all commercial AWS
  Regions, so Amazon Bedrock model availability is the constraint on your Region
  choice. For Amazon Bedrock model availability, see [Model support by AWS Region](../../../bedrock/latest/userguide/models-regions.md "../../../bedrock/latest/userguide/models-regions.md") in the _Amazon Bedrock User
  Guide_.

###### Charges

This tutorial incurs charges for Amazon Bedrock model invocations and DynamoDB storage.
It makes 51 embedding calls, each billed as a Amazon Bedrock inference request, on
short single-sentence inputs. DynamoDB storage charges apply for as long as the
table and vector index exist.

###### Confirm which Region you are using

Every command in this tutorial must run in the same Region. Confirm the
Region that the AWS CLI will actually use before you start, because
`AWS_REGION` takes precedence over
`AWS_DEFAULT_REGION`, and both take precedence over the
`region` setting in your AWS CLI configuration file. A stray
`AWS_REGION` value in your shell creates the table somewhere other
than the Region you intended, and the Amazon Bedrock model might not be enabled there.
To remove all doubt, pass `--region
 `region`` explicitly on each command.

###### SearchVectors uses a separate endpoint

`SearchVectors` resolves to a dedicated search endpoint rather
than the standard DynamoDB endpoint. In a commercial Region, requests go to
`search-dynamodb.`region`.amazonaws.com`,
while every other operation in this tutorial goes to
`dynamodb.`region`.amazonaws.com`.
FIPS and dual-stack variants follow the same pattern. This has two
consequences:

- If your network restricts outbound traffic through a VPC endpoint,
  proxy, or egress allowlist, you must permit the search hostname as well.
  Otherwise `CreateTable` and the write operations succeed
  and only `SearchVectors` fails, typically with a connection
  error that does not indicate the cause.
- Do not use `--endpoint-url` to override the DynamoDB
  endpoint for these commands. A single override cannot serve both
  hostnames and will break search routing.

1. **Create a table with a vector index.** This
   creates a `Products` table with a vector index named
   `DescriptionIndex` on the `DescriptionVector`
   attribute. The index uses the `COSINE` distance function with
   1024 dimensions to match the Titan Text Embeddings V2 output. Because no
   vector index partition key is defined, you do not need a
   `SearchConditionExpression` to search.

```
aws dynamodb create-table \
    --table-name Products \
    --attribute-definitions AttributeName=ProductId,AttributeType=S \
    --key-schema AttributeName=ProductId,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --vector-indexes \
        "[
            {
                \"IndexName\": \"DescriptionIndex\",
                \"VectorAttribute\": {\"AttributeName\": \"DescriptionVector\"},
                \"Projection\": {\"ProjectionType\": \"ALL\"},
                \"Dimensions\": 1024,
                \"DistanceFunction\": \"COSINE\"
            }
        ]"
```

This example uses `ProjectionType` of `ALL` so that
every attribute is available to the search results. If you use
`INCLUDE` instead, note that the projected non-key attribute
budget is shared: the vector attribute counts as one attribute, and each
`INLINE_FILTER` search schema element counts as one.
`HASH` search schema elements do not count toward the
limit. 2. **Wait for the index to become active.** Run
this until `IndexStatus` is `ACTIVE`.

```
aws dynamodb describe-table \
    --table-name Products \
    --query 'Table.VectorIndexes[0].[IndexName,IndexStatus,Backfilling]'
```

For an index created as part of `CreateTable`, as in this
tutorial, `Backfilling` is not reported and the command returns
`null` for it. Use `IndexStatus` alone as your signal
in that case.

`Backfilling` is reported for a vector index that you add to an
existing table with `UpdateTable`. In that case, wait until
`IndexStatus` is `ACTIVE` and
`Backfilling` is not `true` before you search. Note
that `Backfilling` is reported only while the index is
`CREATING`, and is absent once the index is
`ACTIVE`.

###### Wait for the index, not just the table

Do not use `aws dynamodb wait table-exists` to gate the
search. That waiter matches on `Table.TableStatus`, which
becomes `ACTIVE` while the vector index can still be
`CREATING`. There is no waiter for vector index readiness, so
you must poll `DescribeTable` as shown. Searching an index that
is not yet `ACTIVE` fails with a `ValidationException`.
Searching during backfill also returns a `ValidationException`.
It does not return partial results.

For the same reason, you cannot delete the table until every vector
index has finished creating. `DeleteTable` returns
`ResourceInUseException` with the message "Cannot delete table
while indexes are being created, updated, or deleted."

After `IndexStatus` becomes `ACTIVE`, the search
endpoint can require additional time before it begins serving the index.
Retry `SearchVectors` on `ValidationException` during
that interval. 3. **Create the product catalog.** Save the
following 50 products to a tab-separated file named
`products.tsv`. Each line holds a product ID, a name, and a
one-sentence description. The catalog contains ten groups of five related
products, which makes the search results in the last step easy to
interpret.

```
p01	Insulated Travel Mug	A vacuum insulated stainless steel mug that keeps hot drinks warm for up to twelve hours.
p02	Stovetop Espresso Maker	A compact aluminum pot that brews strong espresso style coffee directly on a gas or electric burner.
p03	Manual Burr Coffee Grinder	A hand cranked grinder with adjustable ceramic burrs for consistent coffee grounds.
p04	Pour Over Coffee Dripper	A ceramic cone that sits on a mug and brews a single cup of filter coffee.
p05	Electric Milk Frother	A handheld battery powered whisk that creates dense foam for lattes and cappuccinos.
p06	Lightweight Running Shoe	A breathable mesh road shoe with cushioned foam midsole for daily training runs.
p07	Trail Running Shoe	An aggressive lugged outsole shoe built for grip on loose gravel and muddy trails.
p08	Moisture Wicking Running Socks	Ankle height socks knitted from synthetic yarn that pulls sweat away from the skin.
p09	Reflective Running Vest	A lightweight vest with high visibility strips for running safely after dark.
p10	Hydration Waist Belt	An elastic belt that holds two small water flasks and a phone during long runs.
p11	Ergonomic Mesh Office Chair	An adjustable desk chair with breathable mesh back and lumbar support for long work sessions.
p12	Sit Stand Desk Converter	A height adjustable platform that raises a monitor and keyboard for standing work.
p13	Monitor Arm Mount	A clamp mounted articulating arm that lifts a display off the desk surface.
p14	Under Desk Footrest	An angled cushioned platform that supports the feet and improves seated posture.
p15	Wireless Split Keyboard	A two piece keyboard that separates for a natural shoulder width typing position.
p16	Noise Cancelling Headphones	Over ear wireless headphones that actively silence engine noise on long flights.
p17	Wireless Earbuds	Compact in ear buds with a charging case and multi hour battery for commuting.
p18	Portable Bluetooth Speaker	A water resistant rechargeable speaker sized to fit in a backpack side pocket.
p19	Studio Monitor Headphones	Wired closed back headphones with flat frequency response for audio mixing.
p20	Wired Lapel Microphone	A small clip on microphone for recording clear speech during interviews.
p21	Four Season Backpacking Tent	A double wall tent with an aluminum pole set rated for wind and heavy rain.
p22	Down Sleeping Bag	A mummy shaped bag filled with compressible down insulation for cold weather camping.
p23	Inflatable Sleeping Pad	A lightweight pad that inflates in a few breaths and packs down to bottle size.
p24	Canister Camping Stove	A screw on burner that boils water quickly using a compact fuel canister.
p25	Rechargeable Camp Lantern	A collapsible lantern with adjustable brightness and a built in battery.
p26	Cast Iron Skillet	A preseasoned heavy pan that holds heat evenly for searing and oven baking.
p27	Nonstick Frying Pan	A coated aluminum pan that releases eggs and fish without added oil.
p28	Stainless Steel Stock Pot	A tall wide pot for boiling pasta and simmering large batches of soup.
p29	Enameled Dutch Oven	A heavy lidded pot that moves from stovetop to oven for slow braising.
p30	Bamboo Cutting Board	A large reversible board with a juice groove around the edge.
p31	Padded Laptop Backpack	A water resistant pack with a suspended sleeve that protects a fifteen inch laptop.
p32	Slim Laptop Sleeve	A close fitting neoprene case that shields a notebook inside a larger bag.
p33	Rolling Carry On Suitcase	A hard shell four wheel case sized to fit most overhead cabin bins.
p34	Packing Cube Set	Zippered fabric cubes that compress clothing and organize a suitcase.
p35	Leather Messenger Bag	A single strap shoulder bag with a padded compartment and interior pockets.
p36	Daily Facial Moisturizer	A light lotion with humectants that hydrates skin without leaving residue.
p37	Mineral Sunscreen Lotion	A broad spectrum zinc based sunscreen formulated for sensitive facial skin.
p38	Gentle Foaming Cleanser	A low pH face wash that removes oil and sunscreen without stripping the skin.
p39	Vitamin C Serum	A brightening serum applied before moisturizer to even skin tone over time.
p40	Overnight Repair Cream	A rich night cream with ceramides that restores the skin barrier while sleeping.
p41	Stainless Steel Dog Bowl	A weighted nonslip bowl that resists tipping during enthusiastic feeding.
p42	Padded Dog Harness	An adjustable chest harness that distributes pull away from the neck on walks.
p43	Retractable Dog Leash	A spring loaded leash that extends and locks at several walking lengths.
p44	Interactive Cat Puzzle Feeder	A slow feed tray that makes a cat work for dry food and eat more slowly.
p45	Self Cleaning Litter Box	An enclosed box with a raking mechanism that sifts waste after each use.
p46	Bypass Pruning Shears	Sharp hardened blades that make clean cuts on green stems and small branches.
p47	Long Handled Garden Spade	A steel bladed spade with a wooden shaft for turning soil and digging beds.
p48	Adjustable Hose Spray Nozzle	A metal nozzle that shifts from a fine mist to a strong jet stream.
p49	Raised Garden Bed Kit	Interlocking cedar panels that assemble into an elevated planting box.
p50	Drip Irrigation Starter Kit	Tubing and emitters that deliver water slowly to the base of each plant.
```

The separator between the three fields must be a literal tab character. If
you copy the catalog from a browser, verify that the tabs survived before you
continue. 4. **Generate an embedding for one product.** Run
a single embedding call first to confirm your Amazon Bedrock model access works. The
`inputText` field contains the text to embed,
`dimensions` sets the output size (valid values are 256, 512, or
1024), and `normalize` produces unit-length vectors, which is
recommended for cosine similarity search.

```
mkdir -p emb

aws bedrock-runtime invoke-model \
    --model-id amazon.titan-embed-text-v2:0 \
    --body '{"inputText":"A vacuum insulated stainless steel mug that keeps hot drinks warm for up to twelve hours.","dimensions":1024,"normalize":true}' \
    --cli-binary-format raw-in-base64-out \
    --content-type application/json \
    --accept application/json \
    emb/p01.json
```

The `--cli-binary-format raw-in-base64-out` flag is required.
AWS CLI v2 defaults to base64 encoding for binary parameters, so without this
flag the raw JSON body fails to send correctly. The response is written to
`emb/p01.json` and contains an `embedding` array of
1024 floating-point numbers. Confirm the dimension count.

```
jq '.embedding | length' emb/p01.json
```

The output is `1024`. 5. **Write the first product.** Transform the
embedding into the DynamoDB item format and write it. The stored vector attribute
uses the DynamoDB `L` (list) type wrapping each number in an
`N` type.

```
jq '{"ProductId":{"S":"p01"},"Title":{"S":"Insulated Travel Mug"},"DescriptionVector":{"L":[.embedding[]|{"N":(.|tostring)}]}}' emb/p01.json > item-p01.json

aws dynamodb put-item --table-name Products --item file://item-p01.json
```

###### Vector size and item limits

A 1024-dimension vector is well within the 400 KB DynamoDB item size
limit. Two factors drive how much space an embedding occupies in the
base table: the number of dimensions, and the number of significant
digits each value carries. DynamoDB stores a number in proportion to its
significant digits rather than at a fixed width. Embedding models
commonly return values with many significant digits, so a stored
embedding can be considerably larger than the same vector held at
32-bit floating point precision in the vector index. If item size
matters to your design, measure a representative item rather than
estimating from dimension count. 6. **Embed the remaining products.** This loop
generates an embedding for each remaining product. It skips any file that
already exists, so you can rerun it safely if a call fails.

```
while IFS=$'\t' read -r id title description; do
    [ -s "emb/$id.json" ] && continue
    body=$(jq -n --arg t "$description" '{inputText:$t,dimensions:1024,normalize:true}')
    aws bedrock-runtime invoke-model \
        --model-id amazon.titan-embed-text-v2:0 \
        --body "$body" \
        --cli-binary-format raw-in-base64-out \
        --content-type application/json \
        --accept application/json \
        "emb/$id.json" >/dev/null || echo "FAILED $id"
done < products.tsv

ls emb/*.json | wc -l
```

The count must be 50 before you continue. If any call printed
`FAILED`, run the loop again; it retries only the missing
files.

###### InvokeModel rate quotas

Amazon Bedrock applies request rate quotas to `InvokeModel`. If you
modify this loop to issue calls in parallel, expect throttling exceptions
on some calls, and always verify the final file count rather than assuming
every call succeeded. A partially embedded catalog loads without error and
produces search results that silently omit the missing products. 7. **Load the remaining products.** Build request
payloads of 25 items each, which is the maximum that
`BatchWriteItem` accepts.

```
batch=0
count=0
echo -n '{"Products":[' > batch-0.json
while IFS=$'\t' read -r id title description; do
    if [ "$count" -eq 25 ]; then
        echo ']}' >> "batch-$batch.json"
        batch=$((batch+1)); count=0
        echo -n '{"Products":[' > "batch-$batch.json"
    fi
    [ "$count" -gt 0 ] && echo -n ',' >> "batch-$batch.json"
    jq -c --arg id "$id" --arg title "$title" \
        '{PutRequest:{Item:{ProductId:{S:$id},Title:{S:$title},
          DescriptionVector:{L:[.embedding[]|{"N":(.|tostring)}]}}}}' \
        "emb/$id.json" >> "batch-$batch.json"
    count=$((count+1))
done < <(tail -n +2 products.tsv)
echo ']}' >> "batch-$batch.json"
```

The loop reads from a redirect rather than a pipe because a piped
`while` loop runs in a subshell in some shells, which discards the
`batch` and `count` values and produces malformed batch
files.

Submit each batch. `BatchWriteItem` can partially succeed, so
resubmit anything it returns in `UnprocessedItems`.

```
for f in batch-*.json; do
    cp "$f" pending.json
    for attempt in 1 2 3 4 5; do
        aws dynamodb batch-write-item \
            --request-items file://pending.json \
            --output json > resp.json
        left=$(jq '(.UnprocessedItems.Products // []) | length' resp.json)
        echo "$f attempt $attempt: unprocessed=$left"
        [ "$left" -eq 0 ] && break
        jq '.UnprocessedItems' resp.json > pending.json
        sleep 2
    done
done
```

Confirm that all 50 items are present.

```
aws dynamodb scan --table-name Products --select COUNT --query 'Count'
```

###### ItemCount updates are delayed

The `ItemCount` and `IndexSizeBytes` values that
`DescribeTable` reports for a vector index are updated
approximately every six hours, so immediately after a load they can still
read `0` even though every item was written. Use
`Scan` with `--select COUNT`, as shown, to verify a
load. Do not treat a zero `ItemCount` as a failed
load. 8. **Generate a query embedding and search.**
Embed the search phrase with the same model and dimension count that you used
for the stored items.

```
aws bedrock-runtime invoke-model \
    --model-id amazon.titan-embed-text-v2:0 \
    --body '{"inputText":"How can I make my desk more comfortable to work at","dimensions":1024,"normalize":true}' \
    --cli-binary-format raw-in-base64-out \
    --content-type application/json \
    --accept application/json \
    embedding-query.json
```

###### SearchVector format differs from stored vector format

When you store a vector in an item attribute, you wrap it in an
`L` (list) type: `{"L":[{"N":"0.123"},...]}`.
When you pass a query vector to `SearchVectors`, you use a
plain array of `N` values without the `L`
wrapper: `[{"N":"0.123"},...]`. The following
`jq` transform differs from the one you used for the stored
items for this reason. For more information, see [Basic search](VectorSearchWorkingWith.md#VectorSearchWorkingWith.Search.Basic "VectorSearchWorkingWith.md#VectorSearchWorkingWith.Search.Basic").

```
jq '[.embedding[]|{"N":(.|tostring)}]' embedding-query.json > query-vector.json

aws dynamodb search-vectors \
    --table-name Products \
    --index-name DescriptionIndex \
    --search-vector file://query-vector.json \
    --top-k 5 \
    --projection-expression "ProductId, Title" \
    --return-consumed-capacity TOTAL
```

The query vector and stored vectors must come from the same embedding model
and must have the same number of dimensions. Using a different model or
dimension count produces meaningless results or a validation error. 9. **Read the results.** DynamoDB returns results
sorted by similarity, with the most similar item first. Each result contains
the projected `Item` attributes and a `Score`.

```
{
    "SearchResults": [
        {
            "Item": {
                "ProductId": { "S": "p11" },
                "Title": { "S": "Ergonomic Mesh Office Chair" }
            },
            "Score": 0.6130197048187256
        },
        {
            "Item": {
                "ProductId": { "S": "p12" },
                "Title": { "S": "Sit Stand Desk Converter" }
            },
            "Score": 0.781868577003479
        },
        {
            "Item": {
                "ProductId": { "S": "p14" },
                "Title": { "S": "Under Desk Footrest" }
            },
            "Score": 0.816369354724884
        },
        {
            "Item": {
                "ProductId": { "S": "p13" },
                "Title": { "S": "Monitor Arm Mount" }
            },
            "Score": 0.8283305168151855
        },
        {
            "Item": {
                "ProductId": { "S": "p15" },
                "Title": { "S": "Wireless Split Keyboard" }
            },
            "Score": 0.8469693064689636
        }
    ],
    "ConsumedCapacity": {
        "VectorSearchRequestBytes": 31449.0
    }
}
```

Scores depend on the embedding model and the exact input text, so your
values will differ slightly. What matters is which items were selected and in
what order. The query did not contain the words chair, monitor, or keyboard,
yet the search returned all five desk and office products ahead of the other
45 items in the catalog. Nothing from the coffee, camping, or pet groups
appears.

Try other queries to see the same behavior with different groups. Repeat the
previous step with `"Something to brew fresh coffee at home"` and
the top results are the espresso maker, the pour over dripper, and the milk
frother. Repeat it with `"Keeping my dog safe on walks"` and the
leash and harness come first, followed by items that are only loosely related,
because the catalog contains just two products that closely match. That last
case is worth noting: the search always returns the number of items you ask
for, even when the catalog does not contain that many good matches. Use the
`Score` values, not the result count, to judge match
quality.

How to read a score depends on the distance function that the index
uses:

    * `COSINE` and `EUCLIDEAN` return the items
     with the smallest scores, so lower is more similar. Cosine scores range
     from 0 for identical direction to 2 for opposite direction.
    * `DOT_PRODUCT` returns the items with the highest scores,
     so higher is more similar.

This index uses `COSINE`, so the first result has the lowest
score. Searching with text identical to a stored description returns that item
first with a score at or near zero.

## Clean up

To avoid ongoing charges, delete the resources that you created in this tutorial.
Vector index storage is billed for as long as the index exists, whether or not you
run searches against it.

To delete the vector index but keep the `Products` table and its
items, use `UpdateTable`. The items remain in the table and only the
index is removed.

```
aws dynamodb update-table \
    --table-name Products \
    --vector-index-updates \
        "[
            {\"Delete\": {\"IndexName\": \"DescriptionIndex\"}}
        ]"
```

To delete the table and its vector index together, delete the table.

```
aws dynamodb delete-table --table-name Products
```

Confirm that the table is gone. The following command returns a
`ResourceNotFoundException` once deletion completes.

```
aws dynamodb describe-table --table-name Products
```

For more information about removing a vector index from a table you want to keep,
see [Deleting a vector index](VectorSearchWorkingWith.md#VectorSearchWorkingWith.Delete "VectorSearchWorkingWith.md#VectorSearchWorkingWith.Delete").

## Next steps

After you complete this basic vector search, explore these related topics.

- Filtering search results with a vector index partition key and inline
  filters — see [Basic search](VectorSearchWorkingWith.md#VectorSearchWorkingWith.Search.Basic "VectorSearchWorkingWith.md#VectorSearchWorkingWith.Search.Basic").
- Best practices for choosing distance functions, partition keys, and
  dimensions — see [Best practices for vector indexes](VectorSearchBestPractices.md "VectorSearchBestPractices.md").
- Monitoring for vector index capacity and metrics — see [Monitoring vector index capacity](VectorSearchMonitoring.md "VectorSearchMonitoring.md").
