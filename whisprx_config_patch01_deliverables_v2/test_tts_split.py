# tests/test_tts_split.py
from whisprx.tts_streamer import split_sentences

def test_split_sentences_basic():
    assert split_sentences("Hello world. How are you?") == ["Hello world", "How are you?"]
