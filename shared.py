import os



class system:
    name=os.name

    class cmd:
        if os.name=='posix':
            clear='clear'