import os

if "LOCAL_KEY" in os.environ:
    print(os.environ['LOCAL_KEY'] + '_hfvd')
else:
    print('ValueError')