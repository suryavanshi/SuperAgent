from agent.transcript import Transcript


def test_transcript_adds_entries():
    transcript = Transcript()
    transcript.add("hello")
    transcript.add("world")
    assert transcript.render() == "hello\nworld"
