import os
import shutil
import subprocess

# 获取当前脚本所在的目录
script_directory = os.path.dirname(os.path.abspath(__file__))

# 更改当前工作目录到脚本所在目录
os.chdir(script_directory)
print("当前工作目录已更改为:", os.getcwd())

# 1. 获取所有 JPEG 和 PNG 文件
image_files = [f for f in os.listdir('.') if f.endswith('.jpeg') or f.endswith('.png')]
print("找到的图像文件:", image_files)

# 2. 自动创建文件夹并归类图像文件
folders = {}
for image_file in image_files:
    # 获取文件前缀和后缀，例如 'dambreak.0001.jpeg' 的前缀是 'dambreak'，后缀是 'jpeg'
    prefix = image_file.split('.')[0]
    suffix = image_file.split('.')[-1]
    folder_key = f"{prefix}_{suffix}"
    print(f"处理文件: {image_file}, 前缀为: {prefix}, 后缀为: {suffix}")
    
    # 如果前缀+后缀文件夹不存在，则创建文件夹
    if folder_key not in folders:
        try:
            os.makedirs(folder_key, exist_ok=True)
            print(f"创建文件夹: {folder_key}")
        except Exception as e:
            print(f"创建文件夹 {folder_key} 时出错: {e}")
        folders[folder_key] = []
    
    # 将文件移动到对应的文件夹
    target_folder = folder_key
    try:
        shutil.move(image_file, os.path.join(target_folder, image_file))
        print(f"移动文件 {image_file} 到文件夹 {target_folder}")
    except Exception as e:
        print(f"移动文件 {image_file} 时出错: {e}")
    folders[folder_key].append(image_file)

# 3. 创建用于存储所有 GIF 的文件夹
all_gif_folder = os.path.join(script_directory, "ALLGIF")
if not os.path.exists(all_gif_folder):
    os.makedirs(all_gif_folder)
    print(f"创建 GIF 存储文件夹: {all_gif_folder}")
else:
    print(f"使用已有的 GIF 存储文件夹: {all_gif_folder}")

# 4. 提示用户确保 ImageMagick 已安装
print("请确保已安装 ImageMagick 并配置环境变量。")


# 5. 将文件夹中的图像文件转换为 GIF 动图
for folder, files in folders.items():
    if len(files) > 0:
        # 使用 ImageMagick 命令将文件夹中的图像文件转换为 GIF
        gif_name = os.path.join(folder, f"{folder}_animation.gif")
        command = ["convert", "-delay", "10", "-loop", "0"] + [os.path.join(folder, file) for file in files] + [gif_name]
        try:
            subprocess.run(command, check=True)
            print(f"成功生成 GIF: {gif_name}")
            # 复制生成的 GIF 到 ALLGIF 文件夹
            shutil.copy(gif_name, os.path.join(all_gif_folder, os.path.basename(gif_name)))
        except subprocess.CalledProcessError as e:
            print(f"生成 GIF 时出错: {e}")

print("所有 GIF 文件已生成。")
