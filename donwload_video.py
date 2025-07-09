from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import os 



def rename_video(video_path, new_name):
    # Get the directory path and the current filename
    directory, filename = os.path.split(video_path)
    
    # Remove spaces from the new name and keep the file extension
    new_name = new_name.replace(" ", "_")
    
    # Split the filename and extension
    base_name, extension = os.path.splitext(filename)
    
    # Create the new filename with the new name and original extension
    new_filename = f"{new_name}{extension}"
    
    # Create the new path with the new filename
    new_path = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(video_path, new_path)


# Read video URLs from the text file
file_path = "HDTF_dataset/WRA_video_url.txt"

with open(file_path, "r") as file:
    video_urls = file.readlines()

output_dir = "HDTF/video_dataset/"
# Iterate through each video URL and download
for url in video_urls:
    try:
        vid_name, vid_url = url.strip().split(" ")
        # Replace spaces with underscores in the video name
        vid_name = vid_name.replace(" ", "_")
        # Download the video
        
        yt = YouTube(vid_url.strip())
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        # Create output directory if it doesn't exist

        # os.makedirs(output_dir, exist_ok=True)
        # Download the video with the modified name
        video_path_ = video.download(output_dir)
        rename_video(video_path_,vid_name)

        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")





# # Adjust frame rate to 25fps
# output_path = '/path_to_save_video/adjusted_video.mp4'
# clip = VideoFileClip(video_path)
# clip = clip.set_fps(25)

# # Adjust audio to match the new frame rate
# audio_clip = AudioFileClip(video_path)
# adjusted_audio = audio_clip.set_fps(25)

# # Composite video with adjusted audio
# final_clip = clip.set_audio(adjusted_audio)

# # Write the final clip with adjusted frame rate and audio
# final_clip.write_videofile(output_path)

# print("Video downloaded and frame rate adjusted successfully with matching audio.")