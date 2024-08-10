# News Article Summariser

## Overview
The `Summariser` is a Flask web application that provides text summarization for news articles using the pre-trained `Falconsai/text_summarization` model from the `transformers` library. Users can input a news article and specify the maximum summary length to generate concise summaries.

## Key Components

### 1. Model and Pipeline Initialization
- **Description**: Loads the pre-trained text summarization model (`Falconsai/text_summarization`) using the `transformers` pipeline.
- **Libraries**: `transformers`, `Flask`

### 2. Web Application
- **Description**: A simple web application built with Flask. It allows users to input a news article and specify the desired summary length.
- **Endpoints**:
  - `/` (GET, POST): The main route where users can submit an article for summarization and receive the summary.

### 3. Summarization Process
- **Description**: Processes the input article to generate a summary based on user-defined maximum and minimum lengths.
- **Parameters**:
  - `max_length`: Maximum length of the summary (as specified by the user).
  - `min_length`: Minimum length of the summary, set to half of the `max_length` by default.

## Installation

### Prerequisites
- `transformers` library
- `Flask` library
- `torch` library
