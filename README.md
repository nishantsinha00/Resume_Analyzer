# Resume_Analyzer
Welcome to the Resume Analyzer App! This application allows users to upload their resumes and receive an analysis based on relevance to specific job postings. Below are the details of this app. The Resume Analyzer is a sophisticated tool designed to streamline and enhance the recruitment process. Leveraging the powerful OpenAI API and open-source sentence transformers from Hugging Face, this tool offers comprehensive and insightful analysis of resumes. By utilizing advanced natural language processing (NLP) techniques, it accurately evaluates key skills, experiences, and qualifications of candidates, providing detailed feedback and scoring to assist recruiters in making informed decisions. The integration of OpenAI's cutting-edge models ensures high accuracy and contextual understanding, while the Hugging Face sentence transformers enables precise scoring of various resume sectiond, making the Resume Analyzer an indispensable asset for modern HR departments.

## Steps to reproduce

```bash
# Steps to reproduce 
$ git clone https://github.com/nishantsinha00/Resume_Analyzer.git
$ conda create -n "env_name" python=3.11 #Creating virtual environment
$ proceed ([y]/n)? # When conda asks you to proceed, type 'y'
$ conda activate "env_name" #Activating the virtual environment
$ pip install -r requirements.txt
$ python manage.py runserver 
```

---

## Endpoints

### 1. `/upload`

#### Description
The `/upload` endpoint allows users to upload their resume files for analysis. This endpoint processes the uploaded resume and prepares it for relevance analysis against job postings.

#### Method
`POST`

#### Request
- **Content-Type**: `multipart/form-data`
- **Parameters**:
  - `file_uploaded` (file): The resume file to be uploaded. Supported formats: PDF, DOC, DOCX.

#### Example Request
```bash
curl -X POST http://yourdomain.com/upload \
  -F 'file_uploaded=@/path/to/your/resume.pdf'
```

#### Example Postman Request
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/upload/`
- **Body**:
  - Type: `form-data`
  - Key: `file_uploaded`
  - Value: Select your resume file (e.g., `cvGenerate.pdf`)

#### Response
- **201 Created**: Resume successfully uploaded and processed.
  ```json
  {
    "message": "POST API and you have uploaded a file named 'cvGenerate.pdf' saved at 'uploads\\cvGenerate.pdf'"
  }
  ```
- **400 Bad Request**: Invalid file format or missing file.
  ```json
  {
    "error": "No file uploaded"
  }
  ```

---

### 2. `/relevantCV`

#### Description
The `/relevantCV` endpoint analyzes the uploaded resume against specific job postings and returns a detailed analysis including the relevance of projects and professional experiences.

#### Method
`POST`

#### Request
- **Content-Type**: `application/json`
- **Parameters**:
  - `desc` (string): The job description to analyze the resume against.
  - `nCV` (integer): Number of CVs to be analyzed (usually 3 in this context).

#### Example Request
```bash
curl -X POST http://yourdomain.com/relevantCV \
  -H "Content-Type: application/json" \
  -d '{
        "desc": "As a Product Manager, you will work with new product introduction or Sustaining Operations teams on product readiness, launch & revamp, or sustaining operations...",
        "nCV": 3
      }'
```

#### Example Postman Request
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/relevantCV`
- **Body**: 
  - Type: `raw`
  - Format: `JSON`
  - Content:
  ```json
  {
    "desc": "As a Product Manager, you will work with new product introduction or Sustaining Operations teams on product readiness, launch & revamp, or sustaining operations...",
    "nCV": 3
  }
  ```

#### Response
- **200 OK**: Analysis completed successfully.
  ```json
  {
    "projects": [
        {
            "project_title": "Image classification with PyTorch",
            "short_description": "This PyTorch project trains an image classification model on the CIFAR-10 dataset. A CNN architecture with hyperparameters is modeled, trained, and tested to categorize images into 10 classes with high accuracy.",
            "tech_stack": ["python", "pytorch"],
            "time_duration": {
                "start": "04-2020",
                "end": "05-2020",
                "duration_months": 2
            },
            "relevancy": 5
        },
        {
            "project_title": "Stock price prediction with LSTM",
            "short_description": "The project develops an LSTM model to predict stock prices. Historical closing price data is used to train the recurrent neural network model. By analyzing sequential price patterns, the LSTM model makes multi-day ahead forecasts of a stock's future price.",
            "tech_stack": ["python", "pytorch", "SQL"],
            "time_duration": {
                "start": "10-2021",
                "end": "12-2021",
                "duration_months": 3
            },
            "relevancy": 3
        }
    ],
    "professional_experience": [
        {
            "role": "Data Scientist",
            "organization": "Swiggy",
            "short_description": "Built restaurant recommendation model for Swiggy's landing page to provide personalized suggestions for users based on order data and user attributes using collaborative filtering techniques to increase orders and revenue.",
            "tech_stack": ["python", "Flask", "Heroku", "MongoDB"],
            "time_duration": {
                "start": "05-2022",
                "end": "07-2022",
                "duration_months": 3
            },
            "relevancy": 4
        }
    ],
    "college": {
        "name": "IIT Bombay",
        "branch": "Electrical Engineering",
        "degree": "Dual Degree",
        "cgpa": 8.2,
        "start": "07-2018",
        "end": "05-2023"
    }
  }
  ```

---

## Technologies Used

### Django
A high-level Python Web framework that encourages rapid development and clean, pragmatic design.

### SentenceTransformers
A Python framework for state-of-the-art sentence, text, and image embeddings.

### OpenAI Text Generation & Embeddings API
OpenAI LLM's for text generation and embeddings.

### Faiss
An open source library for efficient similarity search and clustering of dense vectors. 

---
### Summary

The Resume Analyzer App simplifies the process of tailoring resumes to specific job postings by providing relevant feedback and suggestions. Use the `/upload` endpoint to submit your resume and the `/relevantCV` endpoint to get valuable insights on how to improve your resume's relevance to job postings.

---



