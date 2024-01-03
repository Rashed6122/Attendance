import cv2
import os


def FrameCapture(path):
    # Get the directory of the video file
    video_directory = os.path.dirname(path)
    file_name = os.path.basename(path)

    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Get the frames per second (fps) and total number of frames
    fps = vidObj.get(cv2.CAP_PROP_FPS)
    total_frames = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the time spacing between frames
    time_spacing = total_frames // 15

    # Used as a counter variable
    count = 0

    # Checks whether frames were extracted
    success = 1

    while count < 15:
        # Calculate the frame index based on time spacing
        frame_index = int(count * time_spacing)

        # Set the video capture object to the desired frame
        vidObj.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

        # Read the frame
        success, image = vidObj.read()
        print(count)

        if success:
            # Saves the frames with frame-count in the video directory
            frame_path = os.path.join(video_directory, f"rame{count}.jpg")
            cv2.imwrite(frame_path, image)
            count += 1
        else:
            break

    # Release the video capture object
    vidObj.release()
        

def iterate_over_folders(directory):
    # Iterate over all entries (files and directories) in the specified directory
    for entry in os.scandir(directory):
        # Check if the entry is a directory
        if entry.is_dir():
            # Process the folder (subdirectory)
            folder_path = entry.path

            for filename in os.listdir(folder_path):
                # Check if the file is a video file (you can add more video file extensions if needed)
                if filename.endswith(".mp4") or filename.endswith(".mov") or filename.endswith(".MOV"):
                    video_file = os.path.join(folder_path, filename)
                    FrameCapture(video_file)

# Driver Code
if __name__ == '__main__':
    # Replace the video file path with your actual path
    video_file_path = "F:/semester 7/vision/Attendance/data/"

    iterate_over_folders(video_file_path)
    #FrameCapture(video_file_path)


