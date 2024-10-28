# GIFcreatorforParaview
### 功能介绍

这个脚本用于自动化处理 Paraview 生成的图像文件，将其归类并生成 GIF 动画。适用于需要批量处理图像并生成动画的场景，特别是 CFD 或 DEM 模拟结果的可视化。

#### 主要功能：
1. **自动归类图像文件**：
   - 脚本会自动识别当前目录下的 JPEG 和 PNG 文件，并根据文件的前缀和后缀创建相应的文件夹，将图像文件分类保存。

2. **生成动画 GIF**：
   - 对于每个文件夹内的图像文件，使用 ImageMagick 生成对应的动画 GIF。动画会根据图像文件的顺序依次生成。

3. **集中存储 GIF 文件**：
   - 生成的每个 GIF 文件会被保存在各自的文件夹中，并额外复制到一个名为 `ALLGIF` 的文件夹中，方便统一管理和查看。

#### 使用方法：
1. **图像归类**：将 Paraview 生成的 JPEG 或 PNG 图像文件放置在脚本所在的目录下，脚本会自动将它们根据前缀和后缀进行分类存放。
2. **动画生成**：执行脚本后，ImageMagick 会被用来生成动画 GIF。请确保系统中已经安装了 ImageMagick 并配置了环境变量。
3. **帧率设置**：可以通过修改脚本中的 `-delay` 参数来调整动画的帧率，值越小动画播放越快。

#### 依赖：
- **Python 3.x**：用于执行脚本。
- **ImageMagick**：用于将图像文件合成为 GIF 动画。

#### 注意事项：
- 在运行脚本之前，请确保系统中已安装 ImageMagick，可以通过以下命令进行安装：
  - Windows: `winget install ImageMagick.ImageMagick` 或 `choco install imagemagick`
  - Linux: `sudo apt-get install imagemagick`
  - macOS: `brew install imagemagick`
- 如果 ImageMagick 没有安装，脚本会提示安装步骤。

该脚本旨在简化 Paraview 输出结果的后处理过程，帮助用户快速生成可视化动画，从而更好地分析和展示仿真结果。

