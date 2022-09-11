import cadquery as cq

s1 = (
    cq.Sketch()
    .arc((-10, -10), (0, 0), (10, -10), "ie")       # inner elbow
    .segment((10, -10), (150, -200), "ri")            # right wing inner
    .arc((150, -200), (170, -220), (190, -200), "rt")  # right wingtip
    .arc((190, -200), (90, -100), (50, -10), "ro")    # right wing outer
    .arc((50, -10), (0, 50), (-50, -10), "oe")      # outer elbow
    .arc((-50, -10), (-90, -100), (-190, -200), "lo") # left wing outer
    .arc((-190, -200), (-170, -220), (-150, -200), "lt") # left wingtip
    .segment((-150, -200), (-10, -10), "li")   # left wing inner
    .constrain("ie", "ri", "Coincident", None)
    .constrain("ri", "rt", "Coincident", None)
    .constrain("rt", "ro", "Coincident", None)
    .constrain("ro", "oe", "Coincident", None)
    .constrain("oe", "lo", "Coincident", None)
    .constrain("lo", "lt", "Coincident", None)
    .constrain("lt", "li", "Coincident", None)
    .constrain("li", "ie", "Coincident", None)
    .constrain("ie", "ri", "Angle", 0)
    .constrain("ri", "rt", "Angle", 0)
    .constrain("rt", "ro", "Angle", 0)
    .constrain("ro", "oe", "Angle", 0)
    .constrain("oe", "lo", "Angle", 0)
    .constrain("lo", "lt", "Angle", 0)
    .constrain("lt", "li", "Angle", 0)
    .constrain("li", "ie", "Angle", 0)
    .constrain("lt", "Radius", 30)
    .constrain("rt", "Radius", 30)
    .constrain("ie", "Radius", 10)
    .constrain("oe", "Radius", 50)
    .solve()
    .assemble()
)

s2 = (
    cq.Sketch()
    .arc((-10, -10), (0, 0), (10, -10), "ie")       # inner elbow
    .segment((10, -10), (170, -180), "ri")            # right wing inner
    .arc((170, -180), (180, -220), (190, -200), "rt")  # right wingtip
    .arc((190, -200), (90, -100), (50, -10), "ro")    # right wing outer
    .arc((50, -10), (0, 50), (-50, -10), "oe")      # outer elbow
    .arc((-50, -10), (-90, -100), (-200, -210), "lo") # left wing outer
    .arc((-200, -210), (-180, -230), (-130, -210), "lt") # left wingtip
    .segment((-130, -210), (-10, -10), "li")   # left wing inner
    .constrain("ie", "ri", "Coincident", None)
    .constrain("ri", "rt", "Coincident", None)
    .constrain("rt", "ro", "Coincident", None)
    .constrain("ro", "oe", "Coincident", None)
    .constrain("oe", "lo", "Coincident", None)
    .constrain("lo", "lt", "Coincident", None)
    .constrain("lt", "li", "Coincident", None)
    .constrain("li", "ie", "Coincident", None)
    .constrain("ie", "ri", "Angle", 0)
    .constrain("ri", "rt", "Angle", 0)
    .constrain("rt", "ro", "Angle", 0)
    .constrain("ro", "oe", "Angle", 0)
    .constrain("oe", "lo", "Angle", 0)
    .constrain("lo", "lt", "Angle", 0)
    .constrain("lt", "li", "Angle", 0)
    .constrain("li", "ie", "Angle", 0)
    .constrain("lt", "Radius", 20)
    .constrain("rt", "Radius", 20)
    .constrain("ie", "Radius", 10)
    .constrain("oe", "Radius", 50)
    .solve()
    .assemble()
)

result = (cq.Workplane()
    .placeSketch(s1, s2.moved(cq.Location(cq.Vector(0, 0, 10))))
    .loft().faces("+Z").fillet(5))

#show_object(s1)
#show_object(s2)