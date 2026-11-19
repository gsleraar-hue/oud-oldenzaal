# Bouwt index.html uit src.html door de Leaflet-CSS in te voegen.
from pathlib import Path
d = Path(__file__).parent
s = (d / "src.html").read_text(encoding="utf-8")
(d / "index.html").write_text(s.replace("/*LEAFLET_CSS*/", (d / "leaflet.css").read_text(encoding="utf-8")), encoding="utf-8")
print("index.html gebouwd")
