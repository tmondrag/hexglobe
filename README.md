# Hexglobe
## Yet another attempt at partitioning a globe into hexagons and pentagons

This is related to what I was trying to do with tmondrag/hexpartition . This 
attempt starts with the data structure rather than getting lost in the details 
of data representation maybe?

Anyhow, this was inspired by the Gosper Curve and Gosper Island concepts 
(or flowsnakes, as they are refered to by Gardner), detailed at the
[Gosper Curve](https://en.wikipedia.org/wiki/Gosper_curve) wiki article and
[Hierarchical Hexagonal Clustering and Indexing](doc/HeirarchicalHexagons.pdf)

Here's one idea about how to subdivide a hexegon and pentagon tile
![Figure illustrating how to divie a hexagon into 49 smaller hexagons, and a 
pentagon into 40 smaller hexagons + 1 smaller pentagon](doc/hexglobe_tiles.png)
