from moviepy.editor import VideoFileClip
import os

def split_video_with_audio(video_path, time_intervals, output_directory):
    # Load the video clip
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    
    # Set the audio for the entire video clip
    video_clip = video_clip.set_audio(audio_clip)
    
    # Iterate over each time interval
    for i, time_interval in enumerate(time_intervals):
        # Parse the time interval
        start_time, end_time = time_interval.split('-')
        start_minutes, start_seconds = map(int, start_time.split(':'))
        end_minutes, end_seconds = map(int, end_time.split(':'))
        
        # Convert start and end times to seconds
        start_time_seconds = start_minutes * 60 + start_seconds
        end_time_seconds = end_minutes * 60 + end_seconds
        
        # Extract the clip
        clip = video_clip.subclip(start_time_seconds, end_time_seconds)
        
        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)
        
        # Construct the output file path
        output_filename = os.path.join(output_directory, f"{os.path.splitext(os.path.basename(video_path))[0]}_{i+1}.mp4")
        
        clip.write_videofile(output_filename, codec="libx264")
        
        # Close the clip
        clip.close()

    # Close the original video clip
    video_clip.close()

# Example usage:
annot_time_split = "HDTF_dataset/WRA_annotion_time.txt"

with open(annot_time_split, "r") as file:
    annot_time_split_data = file.readlines()
for a_d in annot_time_split_data:
    vid_name, interval = a_d.split(" ")[0],a_d.split(" ")[1:]
    print(vid_name,interval)
    video_path = f"HDTF/video_dataset/{vid_name}"
    time_intervals = interval # List of time intervals in the format "start-end"
    output_directory = "./split_time"  # Output directory where the videos will be saved
    # exit()
    try:
        split_video_with_audio(video_path, time_intervals, output_directory)
    except  Exception as e :
        print("Error is getting " ,e)



# import os

# def write_sorted_video_names_to_txt(directory, output_file):
#     # Get all files in the directory
#     files = os.listdir(directory)
    
#     # Filter out only the video files
#     video_files = [file for file in files if file.endswith('.mp4')]
    
#     # Sort the video file names
#     sorted_video_files = sorted(video_files)
    
#     # Write sorted video names to the output file
#     with open(output_file, 'w') as f:
#         for video_file in sorted_video_files:
#             f.write(video_file + '\n')

# # Example usage:
# directory = "HDTF/split_time"
# output_file = "./training_video_name.txt"

# write_sorted_video_names_to_txt(directory, output_file)