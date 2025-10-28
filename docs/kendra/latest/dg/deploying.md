# Deploying Amazon Kendra

###### Note

Feature support varies by index type and search API being used. To see if this feature
is supported for the index type and search API you’re using, see [Index
types](hiw-index-types.md "hiw-index-types.md").

When it comes time to deploy Amazon Kendra search to your website, we provide source
code that you can use with React to get a head start on your application. The source code is
provided with no charge under a modified MIT license. You can use it as is or change it for
your own needs. The provided React app is an example to help you get started. It's not a
production ready app.

To deploy a search application with no code and generate an endpoint URL to your search
page with access control, see [Amazon Kendra
Experience Builder](deploying-search-experience-no-code.md "deploying-search-experience-no-code.md").

The following example code adds Amazon Kendra search to an existing React web
application:

- [https://kendrasamples.s3.amazonaws.com/kendrasamples-react-app.zip](https://kendrasamples.s3.amazonaws.com/kendrasamples-react-app.zip "https://kendrasamples.s3.amazonaws.com/kendrasamples-react-app.zip")—Sample
  files that developers can use to build a functional search experience into their
  existing React web application.
  The examples are modeled after the search page of the Amazon Kendra console. They
  have the same features for searching and displaying search results. You can use the whole
  example, or you can choose just one of the features for your own use.

To see the three components of the search page in the Amazon Kendra console, choose
the code icon (**</>**) from the right menu. Hover your pointer over
each section to see a brief description of the component and to get the URL of the
component's source.

###### Topics

- [Overview](#example-overview "#example-overview")
- [Prerequisites](#example-prereqs "#example-prereqs")
- [Setting up the example](#example-install "#example-install")
- [Main search page](#main-component "#main-component")
- [Search component](#search-component "#search-component")
- [Results component](#results-component "#results-component")
- [Facets component](#facets-component "#facets-component")
- [Pagination component](#pagination-component "#pagination-component")
- [Building a search experience with
  no code](deploying-search-experience-no-code.md "deploying-search-experience-no-code.md")

## Overview

You add the example code to an existing React web application to activate search. The
example code includes a Readme file with steps to set up a new React development
environment. The example data in the code example can be used to demonstrate a search.
The search files and components in the example code are structured as follows:

- Main search page (`Search.tsx`)—This is the main page that
  contains all of the components. This is where you integrate your application
  with the Amazon Kendra API.
- Search bar—This is the component where a user enters a search term and
  calls the search function.
- Results—This is the component that displays the results from Amazon Kendra. It has three components: Suggested answers, FAQ results, and
  recommended documents.
- Facets—This is the component that shows the facets in the search
  results and allows you to choose a facet to narrow the search.
- Pagination—This is the component that paginates the response from
  Amazon Kendra.

## Prerequisites

Before you begin, you need the following:

- Node.js and npm [installed](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm "https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"). Node.js version 19 or older is required.
- Python 3 or Python 2 [downloaded
  and installed](https://www.python.org/downloads/ "https://www.python.org/downloads/").
- [SDK for Java](../../../sdk-for-java/latest/developer-guide/setup.md "../../../sdk-for-java/latest/developer-guide/setup.md") or [AWS SDK for JavaScript](../../../sdk-for-javascript/latest/developer-guide/welcome.md "../../../sdk-for-javascript/latest/developer-guide/welcome.md") to make API calls to Amazon Kendra.
- An existing React web application. The example code includes a Readme file
  with steps on how to set up a new React development environment, including using
  required frameworks/libraries. You can also follow the quick start instructions
  in the [React
  documentation on creating a React web app](https://create-react-app.dev/docs/getting-started "https://create-react-app.dev/docs/getting-started").
- The required libraries and dependencies configured in your development
  environment. The example code includes a Readme file that lists the required
  libraries and package dependencies. Note that `sass` is required, as
  `node-sass` is deprecated. If you previously installed
  `node-sass`, uninstall this and install `sass`.

## Setting up the example

A complete procedure for adding Amazon Kendra search to a React application is in
the Readme file included in the code example.

###### To get started using kendrasamples-react-app.zip

1. Make sure you have completed the [Prerequisites](#example-prereqs "#example-prereqs"), including downloading and installing
   Node.js and npm.
2. Download kendrasamples-react-app.zip and unzip.
3. Open your terminal and go to
   `aws-kendra-example-react-app/src/services/`. Open
   `local-dev-credentials.json` and provide your credentials. Do not
   add this file to any public repository.
4. Go to `aws-kendra-example-react-app` and install the dependencies
   in `package.json`. Run `npm install`.
5. Launch a demo version of your app on your local server. Run `npm
start`. You can stop the local server by entering on your keyboard
   `Cmd/Ctrl + C`.
6. You can change the port or host (for example, IP address) by going to
   `package.json` and update the host and port: `"start":
"HOST=[host] PORT=[port] react-scripts start"`. If you use Windows:
   `"start": "set HOST=[host] && set PORT=[port] &&
react-scripts start"`.
7. If you have a registered website domain, you can specify this in
   `package.json` after your app name. For example,
   `"homepage": "https://mywebsite.com"`. You must run `npm
install` again to update new dependencies, and then run `npm
start`.
8. To build the app, run `npm build`. Upload the contents of the build
   directory to your hosting provider.

###### Warning

The React app is **not** production ready.
It's an example of deploying an app for Amazon Kendra search.

## Main search page

The main search page (`Search.tsx`) contains all of the example search
components. It includes the search bar component for output, the results components to
display the response from the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API, and a pagination
component for paging through the response.

## Search component

The search component provides a text box to enter query text. The
`onSearch` function is a hook that calls the main function in
`Search.tsx` to make the Amazon Kendra
[Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API call.

## Results component

The results component shows the response from the `Query` API. The results
are shown in three separate areas.

- Suggested answers—These are the top results returned by the
  `Query` API. It contains up to three suggested answers. In the
  response, they have the result type `ANSWER`.
- FAQ answers—These are the frequently asked questions results returned
  by the response. FAQs are added to the index separately. In the response, they
  have the type `QUESTION_ANSWER`. For more information, see [Questions
  and answers](in-creating-faq.md "in-creating-faq.md").
- Recommended documents—These are additional documents that Amazon Kendra returns in the response. In the response from the
  `Query` API, they have the type `DOCUMENT`.

The results components share a set of components for features like highlighting,
titles, links, and more. The shared components must be present for the result components
to work.

## Facets component

The facets component lists the facets available in the search results. Each facet
classifies the response along a specific dimension, such as author. You can refine the
search to a specific facet by choosing one from the list.

After you select a facet, the component calls `Query` with an attribute
filter that restricts the search to documents that match the facet.

## Pagination component

The pagination component allows you to display the search results from the
`Query` API in multiple pages. It calls the `Query` API with
the `PageSize` and `PageNumber` parameters to get a specific page
of results.
