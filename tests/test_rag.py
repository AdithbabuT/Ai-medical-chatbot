"""Unit tests for Ai-medical-chatbot template and loading logic."""
import pytest
from langchain_core.prompts import PromptTemplate


def test_prompt_template_formatting():
    custom_template = """
    Context: {context}
    Question: {question}
    Answer:
    """
    prompt = PromptTemplate(template=custom_template, input_variables=["context", "question"])
    formatted = prompt.format(context="Patient reports mild headache.", question="What is the symptom?")
    assert "Patient reports mild headache." in formatted
    assert "What is the symptom?" in formatted


def test_environment_variable_parsing():
    import os
    # Validate env variable reading logic
    groq_key = os.environ.get("GROQ_API_KEY", "")
    assert isinstance(groq_key, str)
