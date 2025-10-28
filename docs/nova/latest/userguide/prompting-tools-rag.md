# Build your own RAG

When constructing your own _retrieval augmented generation_ (RAG)
system, you can leverage a retriever system and a generator system. The retriever can be
an embedding model that identifies the relevant chunks from the vector database based on
similarity scores. The generator can be a Large Language Model (LLM) that utilizes the
model's capability to answer questions based on the retrieved results (also known as
chunks). In the following sections, we will provide additional tips on how to optimize
the prompts for your RAG system.

###### Leverage the system prompt

As with other functionalities, enhancing the system
prompt can be beneficial. You can define the RAG Systems description in the system
prompt, outlining the desired persona and behavior for the model.

###### Use Model Instructions

You can include a dedicated `"Model
 Instructions:"` section within the system prompt, where you can provide
specific guidelines for the model to follow. For instance, you can list instructions
such as:

`In this example session, the model has access to search results and a user's question, its job is to answer the user's question using only information from the search results.`

```
`Model Instructions:
- You should provide concise answer to simple questions
when the answer is directly contained in search results,
but when comes to yes/no question, provide some details.
- In case the question requires multi-hop reasoning, you
should find relevant information from search results and
summarize the answer based on relevant information with
logical reasoning.
- If the search results do not contain information that
can answer the question, please state that you could not
find an exact answer to the question, and if search results
are completely irrelevant, say that you could not find an
exact answer, then summarize search results.
- Remember to add citations to your response using markers
like %[1]%, %[2]%, %[3]%, etc for the corresponding passage
supports the response.`
```

###### Avoid Hallucination by restricting the instructions

Bring more focus to instructions by clearly mentioning "DO NOT USE INFORMATION THAT IS NOT IN SEARCH
RESULTS!" as a model instruction so the answers are grounded in the provided
context.

```
`- DO NOT USE INFORMATION THAT IS NOT IN SEARCH RESULTS!`
```

###### Provide an input query followed by search results

Provide an input query followed
by the retriever search results or contextual chunks. The model works best when the
chunk results are provided after `Resource: Search Results:`

```
`{query}
Resource: Search Results: {rag_chunks_retreiver_results}`
```

###### Citations

Citations serve as helpful references back to the context provided to answer the question. Citations are generally utilized primarily to ground the LLM Answers. Citations are employed as an evaluation tool, enabling users to refer back to the cited sources from the context to assess whether the answers remain faithful to the provided information.

This is a sample prompt that should be added in the “Model Instructions” in your system prompt to enable the model to focus on producing citations in the answer:

```
`- Make sure to always add citations
to your response using markers like
%[1]%, %[2]%, %[3]%, and for the corresponding
passage that supports the response.`
```

You can combine all of the previous recommendations with the following prompt
template. This template will only generate based on retrieved chunks.

| Role   | Prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | In this session, the model has access to search results and a user's question, your job is to answer the user's question using only information from the search results. Model Instructions: <br>• You should provide concise answer to simple questions when the answer is directly contained in search results, but when comes to yes/no question, provide some details. <br>• In case the question requires multi-hop reasoning, you should find relevant information from search results and summarize the answer based on relevant information with logical reasoning. <br>• If the search results do not contain information that can answer the question, please state that you could not find an exact answer to the question, and if search results are completely irrelevant, say that you could not find an exact answer, then summarize search results. <br>• Remember to add a citation to the end of your response using markers like %[1]%, %[2]%, %[3]%, etc for the corresponding passage supports the response. <br>• DO NOT USE INFORMATION THAT IS NOT IN SEARCH RESULTS! |
| User   | {Query} Resource: Search Results: {search_results}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | ## Multimodal RAG When you create a multimodal RAG, there are a few additional best practices you should observe. <br>• Use images directly if they are not text-heavy (that is, natural scenes, text-sparse slides, infographics, and so on) Amazon Nova has been optimized to handle non-text-heavy images. You do not need to pass an additional text summary for these images in the grounded generation. <br>• Enhance text-heavy images with text summaries (e.g., PDF reports, papers). For text-heavy PDFs, the best approach is to retrieve both images (PDFs) and corresponding text summaries. The text summaries can help the model to identify relevant information from massive amounts of text in the original image. <br>• Let the model know that you are passing images. In the instructions, you can add a sentence like "`You will be provided with images and texts from search results`". |
