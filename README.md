# 2024-S1-UM-1


this project follows up from 2023-S1-UM-8, and there will be a trick
with the script generator to combine them

this project follows up from 2023-S1-UM-8, and we should add those obsnums here for the combo

galaxy is in: 2250 - 2750   for a given vlsr=2500 , we use a wider dv=250, dw=300. Should confirm with PI if this is enough

Mysteriously beam 13 came back to live on 12-mar

b_order=1 seems appropriate, as there is a bit of a slope

ccdcross  @mom0.tab . center=62,33 box=10  > mom0.txt
tabplot mom0.txt 3 4 -2 2 -2 2 point=2,0.2
