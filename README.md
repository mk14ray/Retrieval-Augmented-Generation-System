# **RAG System API`s**

This API allows users to upload files or provide URLs containing textual data, which is then processed and stored for efficient querying. It also enables users to ask questions based on the uploaded data.

---

## **Features**
1. **Data Upload**:
   - Accepts `.txt` and `.pdf` files.
   - Supports URL-based textual data ingestion.
2. **Query System**:
   - Allows users to query the uploaded data.
   - Leverages a RAG system for response generation.

---

## **Endpoints**

### 1. **Upload Data**
#### **POST** `/upload_data`
Uploads data from either a file or a URL and processes it for future queries.

#### **Parameters**
- **Form Data**:
  - `url` *(Single)*: A URL pointing to the data source.
  - `file` *(Single)*: A `.txt` or `.pdf` file.

#### **Example Request**
1. **Uploading a File**:
- **Upload File**
   *Request Body schema: multipart/form-data*
-  **url** - Url (string) or Url (null) (Url)
- **file** - File (string) or File (null) (File)

#### **Responses**
- **200 OK**:
  ```json
  {
    "message": "Data uploaded and processed successfully"
  }
  ```
- **400 Bad Request**:
  - If no file or URL is provided.
  - If the file type is unsupported.

---

### 2. **Ask Query**
#### **POST** `/ask_query`
Sends a question to the system based on the uploaded data.

#### **Parameters**
- **Query Parameter**:
  - `query` *(Required)*: The question to ask.

#### **Responses**
- **200 OK**:
  ```json
  {
    "answer": "The document discusses AI advancements and applications."
  }
  ```
- **400 Bad Request**:
  - If the query is empty or invalid.

---

## **Installation and Setup**

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. **Create Anaconda Environment (conda python env)**
   ```
   python version:3.10.0
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Create local Env File**:
   ```
   1.create (.env) file outside
   2. add the variable for api key: OPENAI_API_KEY
   3. OPENAI_API_KEY = "sk--******kkl0A"
   ```

4. **Run the API**:
   ```bash
   python app.py
   ```

5. **Access the API**:
   - Navigate to `http://localhost:8000/docs` for interactive API documentation.

6. **Go to the upload file api**:
   - Attach the data : url, file
   - Then click on "execute"

6. **Go to the ask query api**:
   - Askthe question: query
   - Then click on "execute"
---

## **Project Structure**
```
.
├── main.py                   # Main API file
├── core/
│   ├── document_loader.py    # Handles document loading and processing
│   ├── vector_store.py       # Stores document vectors for querying
│   └── rag.py                # Implements the RAG system for response generation
├── data/                     # Directory for uploaded files
└── requirements.txt          # Python dependencies
```

---

## **Key Modules**

### **1. `document_loader.py`**
Processes files or URLs and extracts text for indexing.

### **2. `vector_store.py`**
Stores vector representations of processed documents for efficient querying.

### **3. `rag.py`**
Implements a Retrieval-Augmented Generation system for generating responses based on queries.

---

## **Supported File Types**
- `.txt`
- `.pdf`

## **Other Data**
- `url`
---

## **Error Handling**
- Provides clear error messages for invalid inputs (e.g., unsupported file types, missing parameters).

---

## **Thank You**
😊😊😊😊😊😊😊
---