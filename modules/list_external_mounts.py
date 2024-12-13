import psutil

def list_external_volumes():
    external_volumes = []
    for part in psutil.disk_partitions(all=False):
        # 筛选出 /Volumes 下的设备，并排除系统分区
        if "/Volumes" in part.mountpoint and not part.mountpoint.startswith("/System/Volumes"):
            external_volumes.append(part.mountpoint)
    return external_volumes

if __name__ == "__main__":
    external_volumes = list_external_volumes()
    if external_volumes:
        print("Connected external storage devices:")
        n = 0
        for volume in external_volumes:
            n += 1
            print(f"[{n}] {volume}")
    else:
        print("No external storage devices found.")