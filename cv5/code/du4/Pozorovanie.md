## Pozorovanie - Robust škálovanie

Pred škálovaním som si všimol, že hlavné features mean area a worst area 
mali výrazne väčšie hodnoty ako ostatné, ktoré sa pohybovali okolo 0.

Po škálovaní sa tieto boxy zmenšili a výsledok sa najviac podobal na štandardizáciu.
Rozdiel bol v outliéroch, pri štandardizácii siahali približne do 12, 
zatiaľ čo pri Robust škálovaní až k 15 a jeden ešte viac.

Robust škálovanie je menej prísne voči outliérom, neodstraňuje ich úplne, 
ale zmierňuje ich vplyv na výsledky.