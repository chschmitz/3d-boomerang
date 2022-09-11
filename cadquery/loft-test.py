import cadquery as cq

from jupyter_cadquery import show, set_defaults, open_viewer
from jupyter_cadquery.replay import enable_replay, disable_replay, reset_replay, get_context, replay, Replay, _CTX
from jupyter_cadquery.cad_objects import to_assembly

cv = open_viewer("Box", cad_width=640, height=480)

set_defaults(reset_camera=True, show_parent=False, axes=True, axes0=True)

use_replay = True

if use_replay:
    enable_replay(False, False)
    reset_replay()
    show_object = replay
else:
    disable_replay()
    show_object = show

sk1 = (
    cq.Sketch()
    .segment((0,0), (0,5),"s1")
    .arc((0.,5), (.5,2.5), (0.,0.),"a1")
    .constrain("s1","Fixed",None)
    .constrain("s1", "a1","Coincident",None)
    .constrain("a1", "s1","Coincident",None)
    .constrain("s1",'a1', "Angle", 90)
    .solve()
    .assemble()
)

sk2 = cq.Sketch();

for e in sk1._tags["s1"]:
    sk2.edge(e)
for e in sk1._tags["a1"]:
    sk2.edge(e)
sk2.assemble().moved(cq.Location(cq.Vector(0, 0, 3)))

result = (
    cq.Workplane()
    .placeSketch(sk1, sk2)
)

replay(sk1)
