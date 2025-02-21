import imageio.v3 as iio
import numpy as np
import video
import sys

def order_video_frames(frames, start_index, length):
    # Sort the video frames array
    
    # The video is of size n=length and the array is of size 2*n
    #   * The second half of the array are empty frames.
    #   * Empty frames will have a frame value of 1000, so will be greater
    #     frames in the video.

    # Example (First iteration of bubble sort)
    # for i in range(0, length):
        # if (frames[i-1] < frames[i]):
            # temp = frames[i-1]
            # frames[i-1] = frames[i]
            # frames[i] = temp

    return start_index

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 H2_4.py <input.gif> <output.gif>")
        exit(0)

    # Read in input and output files
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Load the video clip
    video_clip = iio.imread(input_file, index=None)
    print("Number of frames:", len(video_clip))

    # Frame array for monitoring comparisons and swaps
    frames = []
    frame_array = video.FrameArray(frames)

    # Create frames to be ordered    
    for f in range(0,len(video_clip)):
        frames.append(video.Frame(video_clip[f], frame_array))

    # Double the size of the array to contain empty frames
    # these frames have a high frame number, so you can assume they
    # are always greater than the frames that you are sorting.
    for f in range(0,len(video_clip)):
        frames.append(video.Frame(np.array([[[1000]]]), frame_array))

    # Call the order video code
    start = order_video_frames(frame_array, 0, len(video_clip))
    print("Number of comparisons: ", frame_array.comps)
    print("Number of swaps: ", frame_array.swaps)

    # Prepare the output
    output_clip = []
    for f in range(0,len(video_clip)):
        output_clip.append(frame_array[start+f].frame)
    
    # Write final output video
    iio.imwrite(output_file, output_clip, fps=20, loop = 0)