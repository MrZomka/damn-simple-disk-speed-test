import time, shutil, os

def measure(size):
    with open(f"./.dsdst/{size}_temp", "wb") as out:
        out.truncate(size * 1024 * 1024)
    startWrite=time.time()
    shutil.copyfile(f"./.dsdst/{size}_temp", f"./.dsdst/{size}_temp_copied")
    endWrite=time.time()

    print(f"{size}MB ~ WRITE -> {round(size/(endWrite-startWrite), 2)} megabytes per second")

    chunk_size = 4096

    startRead=time.time()
    with open(f"./.dsdst/{size}_temp", "rb") as in_file:
        while True:
            chunk = in_file.read(chunk_size)
            
            if chunk == b"":
                break
    endRead=time.time()
    print(f"{size}MB ~ READ -> {round(size/(endRead-startRead), 2)} megabytes per second")
    os.remove(f"./.dsdst/{size}_temp")
    os.remove(f"./.dsdst/{size}_temp_copied")

path = ".dsdst"
if not os.path.exists(path):
   os.makedirs(path)
   print("The temporary directory was created.")

measure(256)
measure(512)
measure(1024)
measure(2048)
measure(4096)
os.rmdir("./.dsdst")
