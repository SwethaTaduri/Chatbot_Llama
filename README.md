**CSV Chatbot: LLaMA-Driven Data Dialogues Using LangChain**

**Project Description:**

This project develops two models: the With-Indexing Model, which uses LangChain for efficient storage and retrieval and the Without-Indexing Model, which directly interacts with OpenAI's LLaMA LLM. These models significantly contribute to personalized medicine and innovative therapies for improved patient outcomes.

**System Architecture:**
 



**Techniques and Tools:**
**Programming language :**  Python

**Platform used :**       Google Colaboratory

**Project Approach :**  With Index Model and Without Index Model
                   
**Techniques          :**   LangChain, NLP, RAG

**LLM                    :**   LLaMA model

**Data Loading      :**   CSV Loader

**Chunking             :**   Character Text Splitter

**Embeddings         :**   Hugging Face

**Vector Datastore :**  Pinecone

**User Interface      :**  Streamlit

**Methodology:**

**I.	With-Index Model:** The with-indexing model uses LangChain to store crucial data from TCGA reports as vectors, providing fast retrieval. It searches for these vectors based on user prompts to generate answers quickly and accurately.

-	**Data Loading:** Loads data from TCGA_Reports CSV file using CSVLoaderclass() and divides the CSV data into smaller chunks with CharacterTextSplitter() for efficient processing.
-	**Vector Conversion and Storage:** Converts textual data into numerical vectors with Hugging Face Embeddings and stores high-dimensional vectors efficiently in a Vector Data Store with Pinecone.
- **Similarity Search and Query Formulation:** Retrieves relevant chunks from TCGA reports using Pinecone's similarity search and formulates search queries based on user prompts with LangChain.
- **Response Generation and Delivery:** Generates and delivers responses to users through the Streamlit interface.

**II.	Without-Index Model:** This model does not rely on pre-stored data for generating responses. It directly interacts with the LLaMA large language model to process the user queries and generate answers based on its extensive training and knowledge base.
- **User Prompt Formulation:** Users interact via Streamlit , considering TCGA data or broader cancer research for queries.
- **OpenAI LLaMA Response Generation:** Draws from vast knowledge to provide comprehensive responses without specific data retrieval.
- **System Response Delivery:** Delivers OpenAI LLaMA's generated responses through a Streamlit User Interface.
   
**Attached:**

•	The repository contains Jupyter Notebooks demonstrating the step-by-step process of data analysis, model creation and evaluation.

•	Documentation provides insights into the methodologies and findings.

**Conclusion:**
Comparing with and without index models provides insights into efficient cancer research information retrieval, showcasing with-index LangChain's potential for better medical understanding. The closer to 1 cosine scores indicate the relevance of the output response to the query, emphasizing the precision and accuracy of the retrieved information.





