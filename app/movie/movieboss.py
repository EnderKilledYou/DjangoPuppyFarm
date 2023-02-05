from app.hello_doggo.queueboss.queueboss import QueueBossBase
import os.path
import shutil

import requests
from moviepy.editor import *


class MovieBoss(QueueBossBase):
    def _process(self, job):
        imgs = job['imgs']
        clips = [self.download_image(m)
                 for m in imgs]

        clip1 = VideoFileClip(clips[0])  # add 10px contour
        clip2 = clip1.fx(vfx.blackwhite)
        clip3 = clip1.fx(vfx.invert_colors)
        clip4 = clip1.crossfadein(2.0)
        final_clip = clips_array([[clip1.margin(10), clip2.margin(10)],
                                  [clip3.margin(10), clip4.margin(10)]])
        final_clip.resize(width=480).write_videofile("my_stack.mp4")
        os.system("my_stack.mp4")
        pass

    def download_image(url):
        filename = url.split("/")[-1]
        filename2 = filename.split(".")[0] + ".mp4"
        if os.path.exists(filename2):
            return filename2

        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(url, stream=True)

        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True

            # Open a local file with wb ( write binary ) permission.
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

            print('Image sucessfully Downloaded: ', filename)
            ImageClip(filename).set_duration(2).write_videofile(filename2, 24)
            print('Image saved Downloaded: ', filename2)
            return filename2
        else:
            print('Image Couldn\'t be retreived')
            raise Exception("bad url")
