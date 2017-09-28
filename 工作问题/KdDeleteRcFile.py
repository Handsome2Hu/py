import os

filepath = sys.argv[1]

os.remove(filepath)
os.rename(filepath+'_',filepath)