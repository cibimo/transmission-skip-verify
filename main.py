import os
import bencodepy

TR_CONFIG = "/home/ubuntu/docker/transmission/config"

# 遍历 resume 文件夹中的文件
for filename in os.listdir(f"{TR_CONFIG}/resume/"):
    filepath = f"{TR_CONFIG}/resume/{filename}"

    # 打开并解析 .resume 文件
    with open(filepath, "rb") as file:
        data = bencodepy.decode(file.read())
    
    if data[b"paused"] == 1:
        print(data[b"destination"].decode(), data[b"name"].decode())
        
        # # 修改字段
        # data[b"paused"] = 0  # 修改为未暂停
        file_num = len(data[b'files'])
    
        data[b"progress"][b"blocks"] = b"all"
        data[b"progress"][b"have"] = b"all"
        data[b"progress"][b"dnd"] = [0] * file_num
        data[b"progress"][b"priority"] = [0] * file_num
    
        # 写回修改后的 .resume 文件
        with open(filepath, "wb") as file:
            file.write(bencodepy.encode(data))
        
        print(f"Modified: {filename}")
        print()
