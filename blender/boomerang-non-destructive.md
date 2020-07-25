   * Set units to mm (Scene Properties → Units)
   * Delete default cube, camera, light
   * Create topology for one wing
      * Add plane and scale to reasonable size (e.g. 150 mm x 40 mm)
      * Apply scale (Ctrl-A)
      * Subdivide length and width-wise using loop cuts (Ctrl-R)
      * Select three corner vertices in each upper corner and merge those (M)
      * Create and move around topology as needed
   * Create vertex groups
      * outer, inner, weld
   * Create three wings and place symmetrically around center
      * Create an empty and rotate 120 deg around Z
      * Add Array modifier and create two more wings
      * Remove relative offset and use object offset with the empty as the object
      * Move empty so that wings line up around world origin
   * Weld wings together
      * Add Weld modifier
      * Constrain to vertex group "weld"
      * Set welding distance to 1 mm or thereabouts
      * Move around weld vertices so they actually weld
   * Extrude into third dimension using Solidify modifier
      * Add Solidify modifier: method "Simple", offset 1, thickness e.g. 4 mm
      * Tune airfoils by selecting "Interior" vertex group,
        Factor for trailing edge/leading edge thickness
   * Add Subdivision Surface modifier
      * Check "On Cage" to see original topology
      * Crease edge loops in Properties panel as desired
