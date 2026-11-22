

# Definitions

 The following terms are used throughout this lens. They represent the key concepts and personas in programmatic advertising that inform the best practices in each pillar. 

 Digital advertising (ads) refers to marketing through online channels, like websites and streaming content, as well as linear channels, like cable television. Digital ads span media formats, including text, image, audio, and video. They can help you achieve a variety of business goals, ranging from brand awareness to customer engagement. They can also help you launch new products and drive repeat sales. <a name="definitions-fig1"></a>

![Online video advertising logical environment showing the buy side (advertiser, agency, DSP), sell side (publisher, ad network, SSP, ad server), and technology intermediaries (ad exchange, DMP, CDP) and the data and bid flows between them](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/definitions-online-video-advertising-environment.jpg)

*Online video advertising logical environment*


## Digital advertising formats
<a name="digital-advertising-formats"></a>
+  **Search advertising:** Ads appearing in search engine results pages. Typically text ads that appear above or alongside organic search results. 
+  **Display advertising:** Ads using text and visual elements that appear on websites, apps, and devices alongside content. 
+  **Online video advertising:** Ads using a video format. Out-stream video ads appear alongside web content. In-stream video ads appear before, during, or after video content. 
+  **Streaming media advertising (OTT):** Video ads that appear in streaming media content delivered over the internet without satellite or cable. 
+  **Audio advertising:** Ads that play before, during, or after online audio content such as streaming music or podcasts. 
+  **Social media advertising:** Ads that appear on social media. 

## Programmatic advertising lifecycle roles
<a name="programmatic-advertising-lifecycle-roles"></a>

 **Buy side (advertiser):** 
+  **Advertiser:** A person, organization, or company that places paid promotion of a specific product, event, or service in public media to attract potential customers. 
+  **Agency:** An organization that, on behalf of clients, plans marketing and advertising campaigns and places advertisements in media. Agencies often use third-party technology services. 
+  **DSP (Demand-Side Platform):** Provides centralized aggregated media buying from multiple sources including ad exchanges, ad networks, and sell-side platforms, often through real-time bidding. DSPs don't provide standard campaign management services or direct publisher relationships. 

 **Sell side (publisher):** 
+  **Publisher:** A person or company that makes content in any form available for consumption, at no cost or for sale. 
+  **Ad network:** Provides an outsourced sales capability for publishers and aggregates inventory and audiences from numerous sources in a single buying opportunity for media buyers. 
+  **SSP (Sell-Side Platform):** Provides outsourced media selling and ad network management services for publishers. SSPs are typically differentiated from ad networks in not providing services for advertisers directly. 
+  **Ad server:** A system that manages, delivers, and tracks online ads. Used by publishers, advertisers, and ad networks. 

 **Technology intermediary:** 
+  **Ad exchange:** Provides a sales channel connecting publishers and ad networks with advertisers. Brings a technology system facilitating automated auction-based pricing, selling, and buying in real-time. 
+  **DMP (Data Management Platform):** An aggregator of third-party data made available commercially to enrich ad supply and expand targeting attributes. 
+  **CDP (Customer Data Platform):** A data solution that centralizes customer-related data to link and bridge multi-channel customer journeys through one identity profile. 

## Advertising technology terms
<a name="advertising-technology-terms"></a>
+  **Beacon:** Tracking pixels or tags used to measure ad performance, attribution, and analytics. 
+  **Click:** A metric counted every time someone clicks on an ad. 
+  **Fill rate:** Ad impressions generated in an ad space divided by the total inventory available on that ad space. 
+  **Impression:** An ad view counted every time a creative ad is served to a user. Considered one of the basic campaign performance indicators. 
+  **IAB (Interactive Advertising Bureau):** An advertising business organization that develops industry standards, conducts research, and provides legal support for the online advertising industry. 
+  **OpenRTB:** A standard of communication between buyers and sellers of real-time bidding advertising, allowing advertising platforms to speak the same language when conducting online media transactions. 
+  **RTB (Real-Time Bidding):** The process of purchasing and selling digital ad space through real-time auctions that occur in the time it takes a webpage to load. 
+  **Programmatic advertising:** The buying and selling of online media through automated systems and advertising platforms. 
+  **VAST (Video Ad Serving Template):** An XML schema developed by the IAB that allows in-stream video ads to be served from video ad servers and played in video players across websites and devices. 

## Publisher-specific terms
<a name="publisher-specific-terms"></a>
+  **FAST (Free Ad-Supported Streaming TV):** A streaming model where viewers watch free content in exchange for seeing ads. Publishers create continuous linear streaming channels from VOD content libraries, monetized through programmatic advertising. 
+  **SGAI (Server-Guided Ad Insertion):** A hybrid ad insertion approach where the server generates manifests with SCTE-35 markers (CDN-cacheable, viewer-agnostic) while the client device handles personalized ad fetching and rendering. Combines server-side intelligence with client-side execution. 
+  **SSAI (Server-Side Ad Insertion):** Ad insertion approach where the server stitches ads into the video stream before delivery, creating a personalized stream per viewer session. Provides uninterrupted playback and ad-blocker resistance. 
+  **CSAI (Client-Side Ad Insertion):** Ad insertion approach where the video player manages the full ad lifecycle (detection, request, rendering, and measurement) on the viewer's device. 
+  **SCTE-35:** A digital program insertion cueing message standard used to signal ad break opportunities within a video stream. Includes multiple message types: spliceinsert (immediate triggers), timesignal (scheduled markers), splicenull (heartbeat signals), and privatecommand (vendor-specific extensions). 
+  **EPG (Electronic Program Guide):** A listing of scheduled programming for a FAST channel, distributed to downstream systems and displayed in streaming apps. 
+  **Prebid Server:** An open-source server-side header bidding solution that sends parallel bid requests to multiple demand partners simultaneously, replacing the sequential waterfall model. 

## Identity and privacy terms
<a name="identity-and-privacy-terms"></a>
+  **UID2 (Unified ID 2.0):** An open-source identity framework that uses multi-layer hashing with rotating salt values and encrypted tokens to enable deterministic identity across publishers and advertisers without exposing raw PII. 
+  **IAB TCF (Transparency and Consent Framework):** An IAB Europe framework standardizing how consent is communicated through the programmatic supply chain using a consent string that travels with bid requests. 
+  **PET (Privacy-Enhancing Technology):** Technologies enabling advertising value to be derived from data while helping protect individual privacy, including differential privacy, secure multi-party computation, and data clean rooms. 
+  **GARM (Global Alliance for Responsible Media):** An advertiser-led initiative that defines the Brand Safety Floor (baseline content categories universally considered brand-unsafe) and the Brand Suitability Framework for advertiser-specific preferences. 
+  **Seller-defined audiences (SDA):** A privacy-preserving audience solution allowing publishers to create targetable segments based on first-party data, activated through real-time bidding without exposing individual user data. 