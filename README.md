# News article Summariser

## Overview
The `Summariser.ipynb` notebook implements a text summarization model using a pre-trained BART model from the `transformers` library. The goal of this notebook is to generate concise summaries from news articles.

## Key Components

### 1. Model and Tokenizer Initialization
- **Description**: Loads the pre-trained BART model (`facebook/bart-large-cnn`) and tokenizer.
- **Libraries**: `transformers`

### 2. Tokenization
- **Description**: Tokenizes the dataset for input to the model, ensuring the correct formats for source and target texts.
- **Process**: Converts text into tokens that the BART model can understand.

### 3. Training and Evaluation
- **Training**:
  - **Description**: Sets training parameters and initializes the `Seq2SeqTrainer`.
  - **Parameters**: Includes settings for learning rate, batch size, number of epochs, etc.
- **Evaluation**:
  - **Description**: Evaluates the model using the ROUGE metric to measure summarization quality.
  - **Metric**: ROUGE (Recall-Oriented Understudy for Gisting Evaluation) - evaluates the quality of summaries.

## Installation

### Prerequisites
- `transformers` library
- `datasets` library
- `torch` library


