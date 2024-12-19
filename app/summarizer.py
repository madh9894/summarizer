from transformers import pipeline

def summarize_text(text, style):
    # Load the Hugging Face summarization pipeline
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # Adjust parameters based on style
    length_map = {"formal": (30, 130), "informal": (20, 100), "technical": (50, 200)}
    min_length, max_length = length_map.get(style, (30, 130))
    
    summary = summarizer(text, min_length=min_length, max_length=max_length, do_sample=False)
    return summary[0]["summary_text"]
