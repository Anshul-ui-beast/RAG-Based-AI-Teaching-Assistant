# Converts the video to mp3
import os
import subprocess

files = os.listdir("videos")
for file in files:
    tutorial_number = file.split(".")[0].split(" #")[1]
    file_name = file.split(" _ ")[0]
    print(tutorial_number, file_name)
    subprocess.run(["ffmpeg" , "-i" , f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])
    
# To extract 10 sec from every video
# import os
# import subprocess

# files = os.listdir("videos")
# for file in files:
#     tutorial_number = file.split(".")[0].split(" #")[1]
#     file_name = file.split(" _ ")[0]
    
#     print(f"Processing {file}...")
    
#     subprocess.run([
#         "ffmpeg", 
#         "-ss", "0", 
#         "-i", f"videos/{file}", 
#         "-t", "10", 
#         "-vn", 
#         f"audios/{tutorial_number}_{file_name}.mp3"
#     ])
    
#     print(f"Finished extracting audio for {file_name}.")