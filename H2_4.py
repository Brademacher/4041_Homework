# import imageio.v3 as iio
# import numpy as np
# import video
# import sys

# Needs to be fast-ish, with emphasis on minimizing swaps #
# I think a modified merge sort that uses insertion sort to avoid #
# getting down to leafs will help lower swap count #
# Need to check for runs natural runs in array #
# Keep track of small subsets in array that are sorted (runs) #
# Try to reach some threshold for subset size to make insertion sort more efficient *
# Then implement modified merge sort to combine them #

# insertion sort to handle runs #
# uses l and r as start and end indices for run #
def my_insertion_sort (arr, l, r):
    for i in range (l, r):
        j = i
        while j > l and (arr[j] < arr[j - 1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

# merge function to combine sorted runs #
# Using the same variables as textbook pseudocode #
def merge(A, p, q, r):
    nl = q - p
    nr = r - q
    L = [0] * nl
    R = [0] * nr

    for i in range(nl):
        print("inside i: " + str(i))
        L[i] = A[p + i]
    for j in range(nr):
        print("inside j: " + str(j))
        R[j] = A[q + j + 1]

    i, j, k = 0, 0, 1
    
# putting sorting and combining values of two runs #
    while (i < nl) and (j < nr):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

# Handling whichever subarray (run) has leftover elements #
    while i < nl:
        A[k] = L[i]
        i += 1
        k += 1

    while j < nr:
        A[k] = R[j]
        j += 1
        k += 1

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
    runs = []
    start_index = 0
    end_index = 0
    for i in length:
        if frames[i] >= frames[i + 1]:
            start_index = i
            i += 1
        

    return start_index



if __name__ == '__main__':
    
    rArr1 = [3, 5, 7, 1, 121, 42, 11, 45, 69, 4447]
    rArr2 = [1, 5, 8, 9, 121, 2, 3, 11, 69, 4447]
    n = len(rArr2)
    q = n // 2
    merge(rArr2, 0, q, n)

    n = len(rArr1)

    
    
   

    
    # if len(sys.argv) < 3:
    #     print("Usage: python3 H2_4.py <input.gif> <output.gif>")
    #     exit(0)

    # # Read in input and output files
    # input_file = sys.argv[1]
    # output_file = sys.argv[2]

    # # Load the video clip
    # video_clip = iio.imread(input_file, index=None)
    # print("Number of frames:", len(video_clip))
    
    # # Frame array for monitoring comparisons and swaps
    # frames = []
    # frame_array = video.FrameArray(frames)

    # # Create frames to be ordered    
    # for f in range(0,len(video_clip)):
    #     frames.append(video.Frame(video_clip[f], frame_array))

    # # Double the size of the array to contain empty frames
    # # these frames have a high frame number, so you can assume they
    # # are always greater than the frames that you are sorting.
    # for f in range(0,len(video_clip)):
    #     frames.append(video.Frame(np.array([[[1000]]]), frame_array))

    # # Call the order video code
    # start = order_video_frames(frame_array, 0, len(video_clip))
    # print("Number of comparisons: ", frame_array.comps)
    # print("Number of swaps: ", frame_array.swaps)

    # # Prepare the output
    # output_clip = []
    # for f in range(0,len(video_clip)):
    #     output_clip.append(frame_array[start+f].frame)
    
    # # Write final output video
    # iio.imwrite(output_file, output_clip, fps=20, loop = 0)