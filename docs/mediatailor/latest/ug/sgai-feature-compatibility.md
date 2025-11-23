# MediaTailor server-guided ad insertion feature

compatibility matrix

AWS Elemental MediaTailor offers two ad insertion methods with different feature compatibility.
Server-guided ad insertion works differently from server-side ad insertion, which affects
compatibility with some MediaTailor features. Use this table to understand which features work
with each ad insertion method.

| Feature compatibility by ad insertion method | Feature                                 | Server-side ad insertion (SSAI)         | Server-guided ad insertion (SGAI) |
| -------------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------- |
| **Ad prefetching**                           | ✓ Supported                             | Not yet supported                       |
| **Ad suppression**                           | ✓ Supported                             | Not applicable                          |
| **Pre-roll ad behavior**                     | Controlled by MediaTailor configuration | Controlled by MediaTailor configuration |
| **Client-side ad tracking**                  | Uses GetTracking API                    | Uses TRACKING section in asset list     |
| **Server-side ad tracking**                  | ✓ Supported                             | ✓ Supported                             |
| **Ad-ID decoration**                         | ✓ Supported                             | ✗ Not compatible                        |

## Compatibility details

### Ad prefetching

Ad prefetching isn't currently supported.

### Ad suppression

Ad suppression isn't supported with server-guided ad insertion methods because
players only fetch ads they're going to play.

### Pre-roll ad behavior

Pre-roll ad timing works differently between insertion methods:

- **Server-side ad insertion:** MediaTailor controls
  when pre-roll ads play based on configuration settings
- **Server-guided ad insertion:** MediaTailor inserts
  pre-roll ads at the top of the manifest. Your player shows these ads first,
  then starts your content

### Ad tracking

Client-side ad tracking uses different mechanisms:

- **Server-side ad insertion:** Uses the
  GetTracking API endpoint
- **Server-guided ad insertion:** Tracking
  information is provided in the TRACKING section of each asset list
  response

### Ad-ID decoration

Ad-ID decoration is not compatible with server-guided ad insertion because the
fields that populate X-AD-CREATIVE-SIGNALING headers are only known when the asset
list is fetched, not when the manifest is written.
