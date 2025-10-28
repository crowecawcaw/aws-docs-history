# Search workloads

Full-text search capabilities empower customer applications within
internal networks, including content management systems and legal
documents. Additionally, they are used in internet-facing
applications such as catalog search on ecommerce websites and
content search. Let's explore a scenario in which Amazon OpenSearch Service is used in the context of an ecommerce platform.

## Use case: E-commerce product search

**Scenario**

Imagine you're managing the search functionality for an
ecommerce website. Your goal is to leverage Amazon OpenSearch Service
for efficient and relevant product searches, providing users
with a seamless shopping experience.

**Needed actions**

1. **Index product data:** Index
   your product catalog in Amazon OpenSearch Service. Each product is
   represented by a document containing attributes such as
   name, description, category and price. Define an appropriate
   mapping for the product index.
2. **Use full-text search:**
   Provide users the ability to search for products efficiently
   by using term matching queries with Amazon OpenSearch Service's
   full-text search capabilities. You can also implement a
   search-as-you-type feature to provide real-time suggestions
   as users type in the search bar.
3. **Use bucket and aggregation
   search:** Use aggregation and bucket search so that
   users can narrow down results by attributes like brand,
   category, size, and color. This enhances the user experience
   by providing filters to refine their search results.
4. **Sort and rank:** You can
   use OpenSearch's scoring capabilities to verify that search
   results are relevant and displayed in an order that meets
   user expectations.
5. **Add synonym and typo
   handling:** You can add synonym support and handle
   typos with features like fuzziness to provide relevant
   results to users despite synonyms or minor spelling
   mistakes.
