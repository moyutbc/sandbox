seq -w 01 20 | xargs -n 1 -I@ python3 f0_2_fc.py case5-@/f0_@.csv case5-@/fc_@.csv
