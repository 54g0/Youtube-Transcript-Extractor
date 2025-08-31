from youtube_transcript_extractor import YoutubeTranscriptExtractor
url= "https://www.youtube.com/watch?v=Ok7Q2LGvQPI&t=1s"
extractor = YoutubeTranscriptExtractor(url)
transcript = extractor.extract_transcript()
print(transcript)
cleaned_transcript = extractor.clean_transcript()
print(cleaned_transcript)
transcript_text = extractor.get_transcript_text()
print(transcript_text)