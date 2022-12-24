import json
import os
import time
import matplotlib as mpl
import matplotlib.pyplot as plt


def do_plotting_yeah(ax, data, title, scales):
    # loop through each emote scale and compute its histogram
    for idx, scale in enumerate(scales):
        text = [data[key][scale]['href'] for key in data if scale in data[key]]
        img_w0 = [data[key][scale]['w'] for key in data if scale in data[key]]
        img_h0 = [data[key][scale]['h'] for key in data if scale in data[key]]

        # # HISTOGRAM VERSION
        hist, xbins, ybins, im = ax[idx].hist2d(img_w0, img_h0, bins=20, cmap='turbo', norm=mpl.colors.LogNorm())
        # https://stackoverflow.com/questions/43538581/printing-value-in-each-bin-in-hist2d-matplotlib
        for i in range(len(ybins) - 1):
            for j in range(len(xbins) - 1):
                binsz_x = 0.5 * (xbins[j + 1] - xbins[j])
                binsz_y = 0.5 * (ybins[j + 1] - ybins[j])
                ax[idx].text(xbins[j] + binsz_x, ybins[i] + binsz_y, f"{hist.T[i, j]:.0f}", color="k", ha="center",
                             va="center", fontweight="bold", fontsize=8)
        plt.colorbar(im, ax=ax[idx])
        print(
            f"\t{scale} -> xbin = {(xbins[1] - xbins[0]):.02f}px | ybin = {(ybins[1] - ybins[0]):.02f}px | {len(text)} emotes")

        # SCATTER PLOT VERSION
        # ax[idx].scatter(img_w0, img_h0)
        # print(f"{scale}x BTTV EMOTES")
        # for i, txt in enumerate(text):
        #     ax[idx].annotate(str(i), (img_w0[i], img_h0[i]))
        #     print(f"{i} -> {txt}")

        ax[idx].set_title(f"{scale}x {title} EMOTES", fontsize=30)
        ax[idx].set_xlabel("width", fontsize=24)
        if idx == 0:
            ax[idx].set_ylabel("height", fontsize=24)
        ax[idx].tick_params(axis='both', which='major', labelsize=16)


# array of all our emotes we have
dir = "./data/"
time_start = time.time()

fig, ax = plt.subplots(2, 3, figsize=(20, 12))

# BTTV: load data from file
data_bttv = json.load(open(dir + "bttv_emotes.json"))
print(f"DATA: {len(data_bttv)} bttv emotes loaded")
do_plotting_yeah(ax[0], data_bttv, "BTTV", ["1", "2", "3"])

# FFZ: load data from file
data_ffz = json.load(open(dir + "ffz_emotes.json"))
print(f"DATA: {len(data_ffz)} ffz emotes loaded")
do_plotting_yeah(ax[1], data_ffz, "FFZ", ["1", "2", "4"])

# print how long the script took
print(f"DATA: Took {round((time.time() - time_start) / 60.0, 2)} minutes to complete...")

# finally export to file
plt.tight_layout()
dir = "./output/"
if not os.path.exists(dir):
    os.makedirs(dir)
fig.savefig(dir + "width_vs_height_hist.png")

# show to the user!
plt.show()
