# emote_statistics
Analysis of BTTV and FFZ emote size on Twitch for [chatterino](https://github.com/Chatterino/chatterino2/). 
Specifically the discussion of the use of 4x emoted in [PR #3812](https://github.com/Chatterino/chatterino2/pull/3812).
Here are the collected statistics about the emote size for different resolutions.

![width_vs_height_hist](https://user-images.githubusercontent.com/2222562/209447318-62a0b773-c38c-4c1c-be97-37ca650d46f4.png)

The emotes for the histogram are "binned" to group emotes that are near in size to get a general idea.
The number in the image are the number of emotes that are in that bin.
```
DATA: 54509 bttv emotes loaded
    1 -> xbin = 3.50px | ybin = 1.30px | 54508 emotes
    2 -> xbin = 6.95px | ybin = 2.60px | 54509 emotes
    3 -> xbin = 13.95px | ybin = 5.25px | 54508 emotes
DATA: 19723 ffz emotes loaded
    1 -> xbin = 5.15px | ybin = 2.40px | 19723 emotes
    2 -> xbin = 10.30px | ybin = 4.85px | 19723 emotes
    4 -> xbin = 20.60px | ybin = 9.70px | 19723 emotes
```


The main conclusion I can see are the following:
- BTTV in general has much lower variance in height compared to FFZ which has two grouping of emotes
- FFZ has a lot of common emotes that are around 30px wide, and another bunch that are 35px wide
- BTTV wide emotes are in general around ~28px tall
- FFZ wide emotes are a little shorter at ~22px tall
- The 3x BTTV are ~110px high which is what we expect for 3x emotes 128px?
- FFZ's 4x are ~110px and ~128px (see the two groups in the bottom right), which seems to indicate that they have a mix of short and correct height 4x emotes?





This is the scatter plot version:
![width_vs_height_scatter](https://user-images.githubusercontent.com/2222562/209447320-b853efd7-d5fb-4521-ac6a-1e7297cf80c7.png)



