import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc
from IPython.display import HTML

# Please do the following:
#   conda install -c conda-forge ffmpeg

class AnimatedScatter(object):
  def __init__(self, get_positions, frames=20):
    self.get_positions = get_positions
    self.stream = self.data_stream()
    self.fig, self.ax = plt.subplots()
    self.anim = animation.FuncAnimation(self.fig, self.update, frames=frames, interval=20, init_func=self.setup_plot, blit=False)

  def setup_plot(self):
    self.scat = self.ax.scatter([], [], vmin=0, vmax=1, cmap="jet", edgecolor="k")
    self.ax.axis([0, 50, 0, 50])
    return self.scat,

  def data_stream(self):
    frame = 0
    while True:
      yield self.get_positions(frame)
      frame += 1

  def update(self, i):
    data = next(self.stream)
    self.scat.set_offsets(data)
    return self.scat,

  def show_html_video(self):
    return HTML(self.anim.to_html5_video())