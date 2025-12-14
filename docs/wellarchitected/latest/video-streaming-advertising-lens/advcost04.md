# Database optimization

| ADVCOST04: How are you optimizing user profile storage, access, and<br>replication? |
| ----------------------------------------------------------------------------------- |
|                                                                                     |

User profile databases tend to be large ranging from 100-200 million to 5 billion user
profiles and contain a wide range of data about users' online activities and interactions.
Storage and Access to this data can increase cost.

###### Best practices

- [ADVCOST04-BP01 Consider lower cost storage for older User
  Profile data](advcost04-bp01.md "advcost04-bp01.md")
- [ADVCOST04-BP02 Consider multi-level caching for user
  profile data](advcost04-bp02.md "advcost04-bp02.md")
- [ADVCOST04-BP03 Store profiles in a single Region and
  replicate asynchronously](advcost04-bp03.md "advcost04-bp03.md")
