# To process all audio files
# import json
# import whisper
# import os

# model = whisper.load_model("large-v2")

# audios = os.listdir("audios")

# for audio in audios:
#     if("_" in audio):
#         number = audio.split("_")[0]
#         title = audio.split("_")[1][:-4]
#         print(number , title)
#         result = model.transcribe(audio = f"audios/{audio}",
#                           language = "hi",
#                           task = "translate",
#                           word_timestamps= False)
        
#         chunks = []
#         for segment in result["segments"]:
#             chunks.append({"number": number,"title": title, "start": segment["start"], "end": segment["end"] , "text": segment["text"]})

#         chunks_with_metadata = {"chunks": chunks, "text": result["text"]}

#         with open(f"jsons/{audio}.json", "w")as f:
#             json.dump(chunks_with_metadata , f)  
            
# To process only one file            
import json
import whisper
import os

model = whisper.load_model("large-v2")

# File you want to process
audio = "8_Inline & Block Elements in HTML.mp3"

# Extract number and title safely
number, rest = audio.split("_", 1)
title = os.path.splitext(rest)[0]

# Transcribe and translate
result = model.transcribe(
    audio=f"audios/{audio}",
    language="hi",
    task="translate"
)

# Prepare chunks
chunks = [
    {"number": number, "title": title, "start": seg["start"], "end": seg["end"], "text": seg["text"]}
    for seg in result["segments"]
]

# Final JSON structure
chunks_with_metadata = {"chunks": chunks, "text": result["text"]}

# Save to file
with open(f"jsons/{audio}.json", "w", encoding="utf-8") as f:
    json.dump(chunks_with_metadata, f, ensure_ascii=False, indent=2)
