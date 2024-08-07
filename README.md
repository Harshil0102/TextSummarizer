# SummariseNLP
Text Summarisation of news articles into short formation 
Overview
The notebook Summariser.ipynb implements a text summarization model using a pre-trained BART model from the transformers library. The goal is to generate concise summary from news article.
Key Components
1.	Model and Tokenizer Initialization:
o	Loads the pre-trained BART model (facebook/bart-large-cnn) and tokenizer.
2.	Tokenization:
o	Tokenizes the dataset for input to the model, ensuring correct formats for source and target texts.
3.	Training and Evaluation:
o	Sets training parameters and initializes the Seq2SeqTrainer.
o	Evaluates the model using the ROUGE metric to measure summarization quality.
