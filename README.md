space-sim
=========

This was a `Physics I` extra credit assignment that displays a system of objects in motion reacting to each others presence in accordance to [Netwon's Third Law](http://en.wikipedia.org/wiki/Newton's_laws_of_motion).
The algorithm was developed in a single function at first and used a spreadsheet to plot the path of the planet.
After confirming that the method worked, I built a [PyGame](http://www.pygame.org) interface to display the graphics.
The challenging part of this program was to display what was happening with the models in the simulation.

By developing a simple camera model that allows the user to change the position of the view and zoom.
I also included a feature to keep a specific body in the center of the camera's view port so that one could simulate our understanding of the solar system before the Copernican Revolution. 

Video
------
### 3 Bodies
<http://www.youtube.com/embed/KKm9c603qiQ?rel=0&vq=hd720>

Screenshot
-----------
![Three Bodies](http://robmurrer.com/assets/projects/orbit/interface.png)

## Running
Must have PyGame installed.
`python main.py`
