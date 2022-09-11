import cadquery as cq

angle = 70

s1 = (
    cq.Sketch()
    .segment((0, 0), (0, -100), "center", True)
    .arc((-10, -10), (0, 0), (10, -10), "ie")       # inner elbow
    .segment((10, -10), (150, -200), "ri")            # right wing inner
    .arc((150, -200), (170, -220), (190, -200), "rt")  # right wingtip
    .arc((190, -200), (90, -100), (50, -10), "ro")    # right wing outer
    .arc((50, -10), (0, 20), (-50, -10), "oe")      # outer elbow
    .arc((-50, -10), (-90, -100), (-190, -200), "lo") # left wing outer
    .arc((-190, -200), (-170, -220), (-150, -200), "lt") # left wingtip
    .segment((-150, -200), (-10, -10), "li")   # left wing inner
    .arc((-50, -10), (-90, -95), (-180, -200), "la", True) # left airfoil
    .arc((-180, -200), (-170, -210), (-150, -200), "lat", True) # left airfoil tip
    .segment((10, -10), (160, -190), "ra", True) # right airfoil
    .arc((160, -190), (170, -200), (190, -200), "rat", True) # right airfoil tip
    .segment((-180, -200), (-190, -200), "law", True)
    .segment((150, -200), (160, -190), "raw", True)
    .constrain("ie", "ri", "Coincident", None)
    .constrain("ri", "rt", "Coincident", None)
    .constrain("rt", "ro", "Coincident", None)
    .constrain("ro", "oe", "Coincident", None)
    .constrain("oe", "lo", "Coincident", None)
    .constrain("lo", "lt", "Coincident", None)
    .constrain("lt", "li", "Coincident", None)
    .constrain("li", "ie", "Coincident", None) 
    .constrain("oe", "la", "Coincident", None)
    .constrain("la", "lat", "Coincident", None)
    .constrain("lat", "li", "Coincident", None)
    .constrain("ie", "ra", "Coincident", None) 
    .constrain("ra", "rat", "Coincident", None)
    .constrain("rat", "ro", "Coincident", None)
    .constrain("la", "law", "Coincident", None)
    .constrain("law", "lt", "Coincident", None)
    .constrain("ra", "raw", "Coincident", None)
    .constrain("raw", "rt", "Coincident", None)
    .constrain("ie", "ri", "Angle", 0)
    .constrain("ri", "rt", "Angle", 0)
    .constrain("rt", "ro", "Angle", 0)
    .constrain("ro", "oe", "Angle", 0)
    .constrain("oe", "lo", "Angle", 0)
    .constrain("lo", "lt", "Angle", 0)
    .constrain("lt", "li", "Angle", 0)
    .constrain("li", "ie", "Angle", 0)
    .constrain("la", "lat", "Angle", 0)
    .constrain("lat", "li", "Angle", 0)
    .constrain("ra", "rat", "Angle", 0)
    .constrain("rat", "ro", "Angle", 0)
    .constrain("lat", "Radius", 20)
    .constrain("rat", "Radius", 20)
    .constrain("lt", "Radius", 30)
    .constrain("rt", "Radius", 30)
    .constrain("ie", "Radius", 15)
    .constrain("oe", "Radius", 50)    
    .constrain("li", "center", "Angle", 180 - (angle / 2))
    .constrain("li", "ri", "Angle", 180 - angle)
    .solve()
    # .assemble()
)


show_object(s1)

